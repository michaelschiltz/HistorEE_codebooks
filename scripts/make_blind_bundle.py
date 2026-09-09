#!/usr/bin/env python3
"""Build a blind working copy: remove withheld material rather than forbidding it.

Three blind codings have now leaked, and all three leaked the same way. The protocol
was enforced by INSTRUCTING the coder not to read certain files, and a coder must
IDENTIFY a file in order to avoid it. Identification is disclosure:

  2026-08-16  the value sets stated the codings under test (repaired: definition/exemplar)
  2026-08-18  matching `source-session` frontmatter to find quarantined vault notes
              returned twelve FILENAMES, and in this vault a filename is a claim
  2026-08-18  locating the insertion point in a reverse-chronological logbook surfaced
              the withheld entry's sub-headings

This script removes the material instead. What is absent cannot be identified, so the
brief need not list it -- and the withheld list is itself a leak, since naming
"logbook/4 section 2026-08-13 (iv)" discloses that a pre-registration exists.

Writes a NEW directory and never mutates the source repos. The manifest of what was
removed is written OUTSIDE the bundle, for the maintainer.

Usage:
  python3 scripts/make_blind_bundle.py --out ~/blind-2026-08-20 \
      --codebooks . --vault ../myfoamrepo \
      --withhold-dates 2026-08-16,2026-08-17,2026-08-18 \
      --withhold-sessions maritime-blind-recoding,bodemerij-amsterdam-blind-coding

Then hand the coder ONLY the bundle path. Their output comes back as CSVs or patches
against the base commits recorded in the manifest.
"""
import argparse, fnmatch, re, shutil, subprocess
from pathlib import Path

LOG = []


def note(msg):
    LOG.append(msg)
    print(msg)


def head_of(repo: Path) -> str:
    try:
        return subprocess.run(["git", "--no-optional-locks", "-C", str(repo),
                               "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return "UNKNOWN"


# A floor, not the mechanism: these are never copied even when tracked.
def _floored(rel: Path) -> bool:
    """True if a repo-relative path falls inside the standing exclusion floor.

    Deliberately NOT `shutil.ignore_patterns`, which matches a bare name at
    every level of the tree. Under that rule `proposed*` also drops
    `records/proposed-rows-*.csv` -- seven tracked files that are the committed
    evidence of what each batch proposed, and exactly the material a bundle may
    legitimately carry. `proposed*` means **a folder at the repo root**, and the
    floor now says so.
    """
    parts = rel.parts
    if not parts:
        return False
    if parts[0] == ".git" or fnmatch.fnmatch(parts[0], "proposed*"):
        return True
    if "__pycache__" in parts:
        return True
    return rel.name.endswith(".tar")


def tracked_files(repo: Path):
    """Paths git tracks in `repo`, relative to it."""
    out = subprocess.run(["git", "--no-optional-locks", "-C", str(repo),
                          "ls-files", "-z"], capture_output=True, text=True,
                         check=True).stdout
    return [p for p in out.split("\0") if p]


def copy_repo(src: Path, dst: Path):
    """Copy a repo into the bundle, tracked files only, and report the rest.

    This used to be a copytree minus an enumerated list of names, and an
    enumerated list protects only what somebody remembered to name. It did not
    name `graph/graph.svg` -- a stale Graphviz render, untracked and gitignored
    since 2026-08-02, left behind in the vault's working tree -- so every bundle
    built since shipped a thousand note titles the repository had not held for
    five weeks. Being ignored by git bought nothing, because **a copy of the
    working tree is not a copy of the repository**.

    So the rule is inverted. Copy what the repository tracks, which is the set
    somebody has actually reviewed and committed, and decide nothing else here.
    Untracked is not the same as junk -- a note written this morning is
    untracked too -- so nothing is dropped silently: whatever did not make it in
    is listed in the build log for the operator to read before handing over.
    """
    def _ignore(dirpath, names):
        base = Path(dirpath)
        return {n for n in names if _floored((base / n).relative_to(src))}

    try:
        tracked = tracked_files(src)
    except Exception as exc:
        shutil.copytree(src, dst, ignore=_ignore)
        note(f"copied {src.name} at {head_of(src)[:8]} "
             f"-- *** UNFILTERED FALLBACK: `git ls-files` failed ({exc}). "
             f"Every untracked file in the working tree is in this bundle. ***")
        return

    kept = 0
    for rel in map(Path, tracked):
        s, d = src / rel, dst / rel
        if not s.is_file() or _floored(rel):
            continue
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(s, d)
        kept += 1
    note(f"copied {src.name} at {head_of(src)[:8]} -- {kept} tracked file(s)")

    floored, review = 0, []
    for s in sorted(src.rglob("*")):
        if not s.is_file():
            continue
        rel = s.relative_to(src)
        if (dst / rel).exists():
            continue
        if _floored(rel):
            floored += 1
        else:
            review.append(rel.as_posix())
    if floored:
        note(f"  {floored} file(s) excluded by the standing floor "
             f"(.git, __pycache__, proposed*, *.tar)")
    if review:
        note(f"  {len(review)} UNTRACKED file(s) in {src.name} were NOT copied "
             f"-- read this list before handing over the bundle:")
        for rel in review:
            note(f"    - {rel}")
        note("  ^ anything here the coder legitimately needs belongs in the repo, "
             "committed, not copied into the bundle by hand.")


def drop_csv_column(path: Path, column: str):
    """Remove one column from a CSV, preserving quoting of every other field."""
    import csv, io
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    if not rows or column not in rows[0]:
        return
    fields = [f for f in rows[0] if f != column]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for r in rows:
        r.pop(column, None)
        w.writerow(r)
    path.write_text(buf.getvalue(), encoding="utf-8", newline="")
    note(f"  stripped column '{column}' from {path.name}")


def drop_csv_rows(path: Path, column: str, values) -> int:
    """Remove whole rows whose `column` is in `values`, preserving the rest verbatim."""
    import csv, io
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    if not rows or column not in rows[0]:
        return 0
    keep = [r for r in rows if r.get(column) not in values]
    if len(keep) == len(rows):
        return 0
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0]), lineterminator="\n")
    w.writeheader(); w.writerows(keep)
    path.write_text(buf.getvalue(), encoding="utf-8", newline="")
    return len(rows) - len(keep)


def rebuild_views(cb: Path, datasets):
    """Regenerate the views of scrubbed datasets, or remove them.

    A component view tabulates every coded form on that component, so shipping the
    committed views beside a scrubbed data.csv states the withheld values outright --
    the same leak the codebook removal prevents, and the one this script missed until
    2026-09-07. Regeneration is preferred to deletion because code-a-form step 1.3 has
    the coder read these views; deletion is the fallback when the generator will not
    run. Only the scrubbed datasets' views are touched.
    """
    views, builder = cb / "views", cb / "scripts" / "build_views.py"
    if not views.exists() or not datasets:
        return
    for ds in sorted(datasets):
        targets = sorted(views.glob(f"{ds}--*"))
        if not targets:
            continue
        comps = sorted({p.stem.split("--", 1)[1] for p in targets
                        if "--" in p.stem and p.suffix == ".md"})
        rebuilt = []
        for c in comps:
            cmd = ["python3", str(builder), "--dataset", ds, "--component", c]
            if ds == "organizational_forms":
                cmd += ["--mechanism", "all"]
            try:
                subprocess.run(cmd, cwd=str(cb), capture_output=True,
                               check=True, timeout=120)
                rebuilt.append(c)
            except Exception:
                pass
        for f in targets:
            comp = f.stem.split("--", 1)[1] if "--" in f.stem else ""
            if f.suffix == ".md" and comp in rebuilt:
                continue
            f.unlink()
            note(f"  removed views/{f.name} (it tabulates the withheld rows)")
        if rebuilt:
            note(f"  regenerated {len(rebuilt)} view(s) for {ds} "
                 f"from the scrubbed data.csv")


def drop_sections(path: Path, dates, level="## "):
    """Delete every level-2 section whose heading mentions a withheld date.

    A section runs from its heading to the next heading at the same level. Leaves a
    visible gap in the sequence, which is fine: the coder already knows the pass is
    blind. What must not leak is CONTENT, not the fact of absence.
    """
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith(level)] + [len(lines)]
    cut, removed = set(), []
    for a, b in zip(starts, starts[1:]):
        if any(d in lines[a] for d in dates):
            cut.update(range(a, b))
            removed.append(lines[a].strip())
    if not cut:
        return
    path.write_text("\n".join(l for i, l in enumerate(lines) if i not in cut),
                    encoding="utf-8", newline="")
    for r in removed:
        note(f"  removed from {path.name}: {r}")


def drop_standing_rows(path: Path, sessions) -> int:
    """Remove a quarantined session's row from a standing table.

    logbook 4's spent-blind table is NOT a dated `## ` section, so --withhold-dates
    never reaches it, and each row states in detail what its session read and which
    cells and characteristics it therefore prejudices. That is a description of the
    batch under test written by the operator who designed it. The operator's own row
    for the current batch is the worst case: it names the cells, the sources and the
    doctrine, and it is written the same day the bundle is built.

    Added 2026-09-07, after a built bundle was found carrying the row for its own
    batch. Rows are matched on the leading `| `slug` |` cell, so the table's prose
    paragraphs and every other row survive.
    """
    if not path.exists():
        return 0
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    keep = [l for l in lines
            if not any(l.startswith(f"| `{sl}` |") for sl in sessions)]
    if len(keep) == len(lines):
        return 0
    path.write_text("".join(keep), encoding="utf-8", newline="")
    return len(lines) - len(keep)


def drop_notes_by_session(vault: Path, sessions):
    """Remove quarantined notes AND every surviving reference to them.

    Deleting the files alone is worse than useless: the MOC hubs keep listing the
    titles, surviving notes keep linking to them, and in this vault a title IS a claim
    -- "The isqa refuses the agent's shield" needs no body to leak. Deletion without
    dereferencing also breaks validate_vault.py, which hands the coder a list of the
    withheld titles as an error report. Found by running this script, 2026-08-19.
    """
    notes_dir = vault / "notes"
    if not notes_dir.exists():
        return []
    removed = []
    for p in sorted(notes_dir.glob("*.md")):
        head = p.read_text(encoding="utf-8")[:600]
        m = re.search(r"^source-session:\s*(\S+)", head, re.M)
        if m and m.group(1) in sessions:
            removed.append(p.stem)
            p.unlink()
    for t in removed:
        note(f"  removed note: {t}")
    if not removed:
        return removed
    scrubbed = 0
    for f in sorted(vault.rglob("*.md")):
        txt = orig = f.read_text(encoding="utf-8")
        for t in removed:
            e = re.escape(t)
            # A wikilink may be WRAPPED across a line break -- this vault hard-wraps
            # some notes -- so match the title with \s+ between its words rather than
            # a literal space, and allow an alias. A line-oriented pattern missed a
            # wrapped link of the form "[[Some withheld title spanning a\nline break]]"
            # and left the title standing in a note the coder reads: found by hand
            # 2026-09-07, and in this vault a title IS a claim. This comment carries no
            # real title, because this script SHIPS INSIDE THE BUNDLE.
            w = r"\s+".join(re.escape(x) for x in t.split())
            link = rf"\[\[{w}(?:\s*\|[^\]]*)?\]\]"
            # MOC list entries and Foam link-reference definitions: drop the line
            txt = re.sub(rf"(?m)^[-*] +{link}.*\n", "", txt)
            txt = re.sub(rf"(?m)^\[{e}\]: .*\n", "", txt)
            # inline references: keep the sentence, lose the claim
            txt = re.sub(link, "[withheld]", txt)
        if txt != orig:
            f.write_text(txt, encoding="utf-8", newline="")
            scrubbed += 1
    note(f"  dereferenced withheld titles in {scrubbed} file(s)")
    # The exported graph embeds every note title verbatim -- a third leak surface,
    # invisible to validate_vault.py because the graph is generated, not linked.
    # Regenerate from the scrubbed note set; delete it if the exporter will not run.
    exporter = vault / "scripts" / "export_graph.py"
    if (vault / "graph").exists():
        before = {f: f.stat().st_mtime_ns for f in sorted((vault / "graph").rglob("*"))
                  if f.is_file()}
        ok = False
        if exporter.exists():
            try:
                subprocess.run(["python3", str(exporter)], cwd=str(vault),
                               capture_output=True, check=True, timeout=120)
                ok = True
            except Exception:
                ok = False
        if ok:
            # The exporter does not rewrite every artefact in graph/. graph.svg is a
            # committed Graphviz rendering it leaves alone, and it embeds every title
            # of the note set it was rendered from -- so a bundle that removed notes
            # shipped their titles in the SVG. Found by hand on 2026-09-07, after the
            # regeneration had been trusted since it was written. Anything the
            # exporter did not rewrite is stale by definition and cannot be trusted;
            # delete it rather than reason about which artefacts carry titles.
            stale = [f for f, m in before.items()
                     if f.exists() and f.stat().st_mtime_ns == m]
            for f in stale:
                f.unlink()
            note("  regenerated graph/ from the scrubbed note set"
                 + (f"; removed {len(stale)} stale artefact(s) the exporter does not "
                    f"rewrite ({', '.join(f.name for f in stale)}) -- they embed the "
                    f"titles of the removed notes" if stale else ""))
        else:
            shutil.rmtree(vault / "graph")
            note("  removed graph/ (exporter unavailable; it embeds every title)")
    return removed


def residual_mentions(root: Path, terms):
    """Report every surviving mention of a withheld TYPE CODE OR NOTE TITLE, for hand review.

    Removing a form's own rows is automatable; removing every OTHER row's discussion
    of it is not, because the content that discusses it -- characteristic definitions,
    neighbouring forms' cell notes, other type rows' scope and co-occurrence prose --
    is exactly what the coder needs and must survive. A re-coding bundle therefore
    always leaks something, and the only safe posture is to make the leak visible.
    Added 2026-09-07 after a test bundle left the answer to the cell under test
    standing in a neighbouring row's note.

    Scans the WHOLE bundle -- both halves -- and runs LAST, after every removal, so
    that it reports what actually ships rather than what was about to be deleted.
    The vault half needs it as much as the codebooks half: vault notes are removed
    by session slug, so a note written by an unlisted session can still name the
    form and state one of its values.

    It sweeps withheld NOTE TITLES too, not only type codes. In this vault a title is
    a claim, and a removed note's title survives wherever prose quotes it rather than
    links it -- logbook 4's standing spent-blind table quotes note titles as evidence
    of what a session spent, and no dereferencer reaches a quotation. Added 2026-09-07
    after a bundle shipped a withheld title in exactly that table.
    """
    hits = []
    for f in sorted(root.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in {".md", ".csv", ".json", ".txt"}:
            continue
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for t in sorted(terms):
            for i, line in enumerate(txt.splitlines(), 1):
                if t in line:
                    j = line.index(t)
                    hits.append((str(f.relative_to(root)), t, i,
                                 " ".join(line[max(0, j - 90):j + 160].split())))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--codebooks", default=".")
    ap.add_argument("--vault", default="../myfoamrepo")
    ap.add_argument("--withhold-dates", default="")
    ap.add_argument("--withhold-sessions", default="")
    ap.add_argument("--withhold-types", default="",
                    help="type_id codes whose rows to remove -- required for a RE-coding "
                         "test, omit for a first coding. Next free record_id goes in the "
                         "manifest, since the coder can no longer compute it.")
    ap.add_argument("--keep-exemplar", action="store_true")
    ap.add_argument("--keep-changelog", action="store_true")
    a = ap.parse_args()

    dates = [d for d in a.withhold_dates.split(",") if d]
    sessions = {s for s in a.withhold_sessions.split(",") if s}
    out = Path(a.out).expanduser()
    if out.exists():
        raise SystemExit(f"refusing to overwrite existing {out}")
    out.mkdir(parents=True)

    cb_src, vt_src = Path(a.codebooks).resolve(), Path(a.vault).resolve()
    cb, vt = out / cb_src.name, out / vt_src.name
    bases = {cb_src.name: head_of(cb_src), vt_src.name: head_of(vt_src)}

    copy_repo(cb_src, cb)
    if not a.keep_exemplar:
        for v in sorted((cb / "vocabularies").glob("*.csv")):
            drop_csv_column(v, "exemplar")
    for lb in sorted((cb / "logbook").glob("*.md")):
        drop_sections(lb, dates)
        n = drop_standing_rows(lb, sessions)
        if n:
            note(f"  removed {n} standing-table row(s) for withheld session(s) "
                 f"from {lb.name} (a row states what its session spent, and which "
                 f"cells it prejudices)")
    for extra in (cb / "logbook").glob("*.csv"):
        if any(d in extra.name for d in dates):
            extra.unlink(); note(f"  removed {extra.name}")
    types = {t for t in a.withhold_types.split(",") if t}
    next_ids = {}
    residual = []
    removed_titles = []
    if types:
        import csv as _csv, io as _io
        for d in sorted((cb / "datasets").glob("*/data.csv")):
            rows = list(_csv.DictReader(d.open(encoding="utf-8")))
            if not rows:
                continue
            keep = [r for r in rows if r.get("type_id") not in types]
            if len(keep) == len(rows):
                continue
            pre = rows[0]["record_id"].rsplit("-", 1)[0]
            width = len(rows[0]["record_id"].rsplit("-", 1)[1])
            nxt = max(int(r["record_id"].rsplit("-", 1)[1]) for r in rows) + 1
            next_ids[d.parent.name] = f"{pre}-{nxt:0{width}d}"
            buf = _io.StringIO()
            w = _csv.DictWriter(buf, fieldnames=list(rows[0]), lineterminator="\n")
            w.writeheader(); w.writerows(keep)
            d.write_text(buf.getvalue(), encoding="utf-8", newline="")
            note(f"  removed {len(rows) - len(keep)} row(s) for "
                 f"{', '.join(sorted(types))} from {d.parent.name}/data.csv")
        for cbk in sorted((cb / "datasets").glob("*/codebook.md")):
            cbk.unlink(); note(f"  removed {cbk.parent.name}/codebook.md (row counts would betray the removal)")
        for v in sorted((cb / "vocabularies").glob("*_type.csv")):
            n = drop_csv_rows(v, "code", types)
            if n:
                note(f"  removed {n} vocabulary row(s) for "
                     f"{', '.join(sorted(types))} from vocabularies/{v.name} "
                     f"(key_source states the reasoning under test)")
        rebuild_views(cb, set(next_ids))

    if not a.keep_changelog:
        (cb / "CHANGELOG.md").unlink(missing_ok=True)
        note("  removed CHANGELOG.md (it records the reasoning under test)")

    if vt_src.exists():
        copy_repo(vt_src, vt)
        removed_titles = drop_notes_by_session(vt, sessions) or []

    if types or removed_titles:
        residual = residual_mentions(out, set(types) | set(removed_titles))

    manifest = out.parent / (out.name + ".manifest.md")
    manifest.write_text(
        "# Blind bundle manifest — FOR THE MAINTAINER, NOT THE CODER\n\n"
        + "".join(f"- base `{k}` = `{v}`\n" for k, v in bases.items())
        + f"- withheld dates: {', '.join(dates) or 'none'}\n"
        + f"- withheld sessions: {', '.join(sorted(sessions)) or 'none'}\n"
        + f"- withheld types: {', '.join(sorted(types)) or 'none'}\n"
        + ("".join(f"- NEXT FREE record_id for {k}: `{v}` -- SUPPLY THIS TO THE CODER\n"
                   for k, v in next_ids.items()) if next_ids else "")
        + "\n"
        "## Removed\n\n" + "".join(f"- {l}\n" for l in LOG) + "\n"
        + ("## RESIDUAL MENTIONS -- HAND REVIEW REQUIRED BEFORE THE BUNDLE SHIPS\n\n"
           "A withheld type code, or the TITLE of a withheld vault note, is still named in\n"
           "the files below. This is expected and cannot be automated away: characteristic\n"
           "definitions, neighbouring forms' cell notes and other type rows' scope prose all\n"
           "legitimately discuss a withheld form and must survive, and prose that QUOTES a\n"
           "note title -- logbook 4's standing table does, as evidence of what a session\n"
           "spent -- is beyond the reach of any dereferencer.\n"
           "READ EACH ONE AND DECIDE. A mention that merely names the form is usually fine;\n"
           "a mention that states one of its VALUES, or the reasoning behind one, is a leak,\n"
           "and so is a quoted note title, because in this vault a title IS a claim. Redact\n"
           "by hand, or withhold the neighbouring type or session as well.\n\n"
           + "".join(f"- `{f}`:{ln} (`{t}`) -- {snip}\n"
                     for f, t, ln, snip in residual) + "\n"
           if residual else "")
        + "## Limits\n\n"
        "Removal stops leakage; it does not create independence. Same coder and same\n"
        "model means this remains test-retest, not inter-rater — logbook 4 2026-08-13 (iv).\n"
        "The operator must name every relevant --withhold-sessions slug; the script cannot\n"
        "guess which sessions formed expectations. Content that legitimately belongs -- other\n"
        "forms' row notes, key_source fields -- is NOT scrubbed, and should not be: the blind\n"
        "covers the forms under test, not the whole matrix. FOR A RE-CODING\n"
        "(--withhold-types) the forms under test are the exception and are scrubbed\n"
        "everywhere they are stated: their data.csv rows, their vocabulary type rows\n"
        "(whose key_source states the very reasoning under test), every codebook.md, and\n"
        "the component views that tabulate them. Before 2026-09-07 the type rows and the\n"
        "views were left in place, which made a re-coding bundle state its own answer.\n",
        encoding="utf-8", newline="")
    print(f"\nbundle: {out}\nmanifest: {manifest}")


if __name__ == "__main__":
    main()
