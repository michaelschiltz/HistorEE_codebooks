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
import argparse, re, shutil, subprocess
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


def copy_repo(src: Path, dst: Path):
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", "__pycache__",
                                                            "proposed*", "*.tar"))
    note(f"copied {src.name} at {head_of(src)[:8]}")


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
        return
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
        return
    scrubbed = 0
    for f in sorted(vault.rglob("*.md")):
        txt = orig = f.read_text(encoding="utf-8")
        for t in removed:
            e = re.escape(t)
            # MOC list entries and Foam link-reference definitions: drop the line
            txt = re.sub(rf"(?m)^[-*] +\[\[{e}\]\].*\n", "", txt)
            txt = re.sub(rf"(?m)^\[{e}\]: .*\n", "", txt)
            # inline references: keep the sentence, lose the claim
            txt = re.sub(rf"\[\[{e}\]\]", "[withheld]", txt)
        if txt != orig:
            f.write_text(txt, encoding="utf-8", newline="")
            scrubbed += 1
    note(f"  dereferenced withheld titles in {scrubbed} file(s)")
    # The exported graph embeds every note title verbatim -- a third leak surface,
    # invisible to validate_vault.py because the graph is generated, not linked.
    # Regenerate from the scrubbed note set; delete it if the exporter will not run.
    exporter = vault / "scripts" / "export_graph.py"
    if (vault / "graph").exists():
        ok = False
        if exporter.exists():
            try:
                subprocess.run(["python3", str(exporter)], cwd=str(vault),
                               capture_output=True, check=True, timeout=120)
                ok = True
            except Exception:
                ok = False
        if ok:
            note("  regenerated graph/ from the scrubbed note set")
        else:
            shutil.rmtree(vault / "graph")
            note("  removed graph/ (exporter unavailable; it embeds every title)")


def residual_mentions(root: Path, types):
    """Report every surviving mention of a withheld type, for hand review.

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
    """
    hits = []
    for f in sorted(root.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in {".md", ".csv", ".json", ".txt"}:
            continue
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for t in sorted(types):
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
    for extra in (cb / "logbook").glob("*.csv"):
        if any(d in extra.name for d in dates):
            extra.unlink(); note(f"  removed {extra.name}")
    types = {t for t in a.withhold_types.split(",") if t}
    next_ids = {}
    residual = []
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
        drop_notes_by_session(vt, sessions)

    if types:
        residual = residual_mentions(out, types)

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
           "A withheld type is still named in the files below. This is expected and cannot\n"
           "be automated away: characteristic definitions, neighbouring forms' cell notes and\n"
           "other type rows' scope prose all legitimately discuss it, and all must survive.\n"
           "READ EACH ONE AND DECIDE. A mention that merely names the form is usually fine;\n"
           "a mention that states one of its VALUES, or the reasoning behind one, is a leak\n"
           "and must be redacted by hand or the neighbouring type withheld as well.\n\n"
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
