#!/usr/bin/env python3
"""Count audit of the batch record: nothing dropped, nothing added, nothing orphaned.

A pass that prints DONE can still have lost rows -- a parse failure, a rate
limit, a successor file built from a filter that missed something. The log
says nothing; only the counts do. This script checks the counts that the
tracked record makes checkable, and checks nothing else.

  C1  instances -> corpus     every instance names an act that is in its corpus
                              census, in the same volume.
  C2  instance identity       instance ids are unique.
  C3  instances <-> codings   every coded row names an instance that exists, and
                              every instance carries at least one coded row,
                              except an instance assigned to `neither` whose
                              instance row has no blank field: it was read in
                              full and evidences no characteristic (ruled by MS,
                              records/RULINGS-count-audit-2026-11-15.md).
  C4  coded rows              no blank `state`; no articulated state (anything
                              but .NR, .IL, .NA) without a quote; no repeated
                              (instance, characteristic) pair.
  C5  successors              a successor record keeps its predecessor's set of
                              keys exactly. A correction changes fields, not
                              membership; a membership change (an act split in
                              two) is declared below with the record that makes it.
  C6  registration            every census, instance and coding file
                              in records/ is named below, as current, superseded
                              or standalone. An unregistered file fails, so a new
                              successor cannot be skipped by this script unseen.
  C7  blind scope             every cell in a bundle's cells-in-scope.csv exists
                              in data.csv with the same form and characteristic,
                              and its blind recoding id exists in recodings.csv.
  C8  manifests               every hash in a MANIFEST-*.sha256 is the hash of a
                              tracked file, under any name, or is excepted below
                              with its reason. Source PDFs under ./sources/ are
                              never committed (records/README.md) and are
                              excepted as a class.
  C9  quoted hashes           every sha256 quoted in backticks in records/*.md,
                              logbook/*.md or CHANGELOG.md is the hash of a
                              tracked file.
  C10 sample -> instances     where the census marks its sample, every sampled act
                              has an instance and every instance's act is sampled.

The pass list is explicit rather than inferred, for the reason
check_dependence.py keeps its blocking values explicit: which file is current
is a decision, not a pattern. C6 is what keeps the explicit list honest.

records/ is read, never written (records/README.md).

Usage:  python scripts/check_counts.py
Exit:   1 if any check fails, else 0.
"""
import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REC = ROOT / "records"
MISSING = {".NR", ".IL", ".NA"}
ROMAN = {"I": "1", "II": "2", "III": "3", "IV": "4"}

# --- Passes ---------------------------------------------------------------
# corpus_key / instance_key name the act number in each file; vol names the
# volume column where both files carry one (values compared through ROMAN).
PASSES = [
    {
        "name": "venetian-pass",
        "corpus": "CORPUS-morozzo-lombardo-2026-11-05-ii.csv",
        "corpus_key": "act",
        "instances": "INSTANCES-venetian-pass-2026-11-05-ii.csv",
        "instance_key": "act_no",
        "vol": "vol",
        "chars": "INSTANCE-CHARS-venetian-pass-2026-10-25.csv",
    },
    {
        "name": "comanda-primary",
        "corpus": "act-census-2026-11-03.csv",
        "corpus_key": "doc_no",
        "instances": "instances-2026-11-03.csv",
        "instance_key": "doc_no",
        "chars": "instance-chars-2026-11-03.csv",
        # C10: census rows in the sample, by the census's own column.
        "sample": ("in_sample", {"mod3", "directed", "non-contract"}),
    },
    {
        # Two editions (Cassinese, Scriba); no census file was built for them.
        "name": "commenda-primary",
        "corpus": None,
        "instances": "INSTANCES-commenda-primary-2026-09-28.csv",
        "chars": "INSTANCE-CHARS-commenda-primary-2026-09-28.csv",
    },
]

# Superseded record -> its successor, and the key whose set must be kept.
SUCCESSORS = [
    ("CORPUS-morozzo-lombardo-2026-10-25.csv", "CORPUS-morozzo-lombardo-2026-11-05.csv", "act"),
    ("CORPUS-morozzo-lombardo-2026-11-05.csv", "CORPUS-morozzo-lombardo-2026-11-05-ii.csv", "act"),
    ("INSTANCES-venetian-pass-2026-10-25.csv", "INSTANCES-venetian-pass-2026-11-05.csv", "instance_id"),
    ("INSTANCES-venetian-pass-2026-11-05.csv", "INSTANCES-venetian-pass-2026-11-05-ii.csv", "instance_id"),
    ("act-census-2026-10-27.csv", "act-census-2026-11-03.csv", "doc_no"),
    ("instances-2026-10-27.csv", "instances-2026-11-03.csv", "instance_id"),
]

# Membership changes a successor may make, each with the record that makes it.
SUCCESSOR_ADDS = {
    "instances-2026-11-03.csv": ({"CMD-174-2", "CMD-204-2", "CMD-217-2"},
        "three acts split in two (records/CORRECTIONS-madurell-translation-2026-11-03.md)"),
}

# Records that belong to no pass with instances, and why.
STANDALONE = {
    "CORPUS-she-associations-2026-10-13.csv": "census of Yamamoto IV(A); no instance pass has been run on it",
    "TYPE-CENSUS-commenda-primary-2026-09-28.csv": "type census of the pass; rows are types, not instances",
    "TYPE-CENSUS-venetian-pass-2026-10-25.csv": "type census of the pass; rows are types, not instances",
    "instance-chars-2026-10-27.csv": "codings of 2026-10-27, superseded by instance-chars-2026-11-03.csv with derived rows added",
}

# C3: an instance may carry no coded row only if it is assigned to `neither` and
# its instance row is complete -- every field a value, .NR or n/a, none blank --
# so that "read in full, evidences nothing" is distinguishable from "not reached".
# Ruled by MS, 2026-11-15 (records/RULINGS-count-audit-2026-11-15.md, ruling 1).
NO_ROW_FORM = "neither"

# Manifest entries that are legitimately not tracked under their bundle-time hash.
MANIFEST_EXCEPTIONS = {
    ("MANIFEST-commenda-primary-2026-09-28.sha256", "./PRIORS-commenda-primary-2026-09-28.md"):
        "bundle-time copy; the committed priors is records/PRIORS-commenda-primary-2026-09-28.md, "
        "whose hash NOTES-commenda-primary-coding-2026-09-28.md records",
    ("MANIFEST-commenda-secondary-2026-09-28.sha256", "./PRIORS-commenda-secondary-2026-09-28.md"):
        "bundle-time copy; the committed priors is records/PRIORS-commenda-secondary-2026-09-28.md",
}

failures = []
warnings = []


def fail(check, msg):
    failures.append(f"{check}: {msg}")


def read(name):
    with (REC / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def vol(v):
    v = (v or "").strip()
    return ROMAN.get(v, v)


def check_pass(p):
    inst = read(p["instances"])
    ids = [r["instance_id"] for r in inst]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        fail("C2", f"{p['instances']}: repeated instance ids {sorted(dup)[:5]}")

    if p.get("corpus"):
        corpus = read(p["corpus"])
        keys = [r[p["corpus_key"]] for r in corpus]
        if len(keys) != len(set(keys)):
            fail("C1", f"{p['corpus']}: act numbers are not unique, so instances cannot be matched")
        by_act = {r[p["corpus_key"]]: r for r in corpus}
        for r in inst:
            act = r[p["instance_key"]]
            if act not in by_act:
                fail("C1", f"{p['instances']}: {r['instance_id']} names act {act}, not in {p['corpus']}")
            elif p.get("vol") and vol(r[p["vol"]]) != vol(by_act[act][p["vol"]]):
                fail("C1", f"{r['instance_id']}: volume {r[p['vol']]} against corpus {by_act[act][p['vol']]}")

    chars = read(p["chars"])
    coded = {r["instance_id"] for r in chars}
    by_id = {r["instance_id"]: r for r in inst}
    no_row = 0
    for i in sorted(set(ids) - coded):
        r = by_id[i]
        blank = [k for k, v in r.items() if not (v or "").strip()]
        if not r.get("form_assigned", "").startswith(NO_ROW_FORM):
            fail("C3", f"{p['name']}: instance {i} has no coded row and is not assigned to `{NO_ROW_FORM}`")
        elif blank:
            fail("C3", f"{p['name']}: instance {i} has no coded row and blank fields {blank[:4]}, "
                       f"so it cannot be shown to have been read")
        else:
            no_row += 1
    if p.get("sample"):
        col, values = p["sample"]
        sampled = {r[p["corpus_key"]] for r in corpus if r[col] in values}
        have = {r[p["instance_key"]] for r in inst}
        for a in sorted(sampled - have):
            fail("C10", f"{p['corpus']}: act {a} is in the sample ({col}) but has no instance")
        for a in sorted(have - sampled):
            fail("C10", f"{p['instances']}: act {a} has an instance but is not in the sample ({col})")
    for i in sorted(coded - set(ids)):
        fail("C3", f"{p['name']}: {p['chars']} codes {i}, which is not in {p['instances']}")

    pairs = set()
    for n, r in enumerate(chars, start=2):
        state = r["state"].strip()
        if not state:
            fail("C4", f"{p['chars']} line {n}: blank state ({r['instance_id']} {r['char_id']})")
        elif state not in MISSING and not r.get("quote", "").strip():
            fail("C4", f"{p['chars']} line {n}: state {state} with no quote ({r['instance_id']} {r['char_id']})")
        pair = (r["instance_id"], r["char_id"])
        if pair in pairs:
            fail("C4", f"{p['chars']} line {n}: {pair} coded twice")
        pairs.add(pair)
    return len(inst), len(chars), no_row


def check_successors():
    for old, new, key in SUCCESSORS:
        a = {r[key] for r in read(old)}
        b = {r[key] for r in read(new)}
        allowed = SUCCESSOR_ADDS.get(new, (set(), ""))[0]
        if a - b or (b - a) - allowed:
            fail("C5", f"{new} drops {sorted(a - b)[:5]} / adds {sorted((b - a) - allowed)[:5]} against {old}")


def check_registration():
    named = set(STANDALONE)
    for p in PASSES:
        named |= {p["instances"], p["chars"]} | ({p["corpus"]} if p.get("corpus") else set())
    for old, new, _ in SUCCESSORS:
        named |= {old, new}
    for f in sorted(REC.glob("*.csv")):
        if re.match(r"(CORPUS|INSTANCES|INSTANCE-CHARS|TYPE-CENSUS|act-census|instances|instance-chars)-", f.name) \
                and f.name not in named:
            fail("C6", f"records/{f.name} is not registered in check_counts.py (current, superseded or standalone)")
    for n in sorted(named):
        if not (REC / n).exists():
            fail("C6", f"check_counts.py names records/{n}, which does not exist")


def check_scope():
    data, rec_ids = {}, {}
    for d in ("organizational_forms", "loss_mitigation_forms"):
        with (ROOT / "datasets" / d / "data.csv").open(encoding="utf-8", newline="") as f:
            data[d] = {r["record_id"]: r for r in csv.DictReader(f)}
        with (ROOT / "datasets" / d / "recodings.csv").open(encoding="utf-8", newline="") as f:
            rec_ids[d] = {r["recoding_id"] for r in csv.DictReader(f)}
    n = 0
    for scope in sorted(REC.glob("BUNDLE-*/cells-in-scope.csv")):
        with scope.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                n += 1
                cell = data[r["census"]].get(r["record_id"])
                if cell is None or (cell["type_id"], cell["char_id"]) != (r["type_id"], r["char_id"]):
                    fail("C7", f"{scope.parent.name}: {r['record_id']} is not {r['type_id']} {r['char_id']} in data.csv")
                if r["recoding_id_blind"] not in rec_ids[r["census"]]:
                    fail("C7", f"{scope.parent.name}: blind recoding {r['recoding_id_blind']} missing from recodings.csv")
    return n


def tracked_hashes():
    out = {}
    for f in ROOT.rglob("*"):
        if f.is_file() and ".git" not in f.parts and not any(part.startswith("proposed") for part in f.parts):
            out.setdefault(hashlib.sha256(f.read_bytes()).hexdigest(), []).append(f)
    return out


def check_manifests(hashes):
    pdfs = 0
    for m in sorted(REC.glob("MANIFEST-*.sha256")):
        for line in m.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            h, name = line.split(None, 1)
            name = name.strip()
            if h in hashes:
                continue
            if name.startswith("./sources/") and name.lower().endswith(".pdf"):
                pdfs += 1
                continue
            if (m.name, name) in MANIFEST_EXCEPTIONS:
                continue
            fail("C8", f"{m.name}: {name} ({h[:12]}…) matches no tracked file and is not excepted")
    return pdfs


def check_quoted(hashes):
    files = sorted(REC.glob("*.md")) + sorted((ROOT / "logbook").glob("*.md")) + [ROOT / "CHANGELOG.md"]
    n = 0
    for f in files:
        for m in re.finditer(r"sha256[^`\n]{0,40}`([0-9a-f]{64})`", f.read_text(encoding="utf-8")):
            n += 1
            if m.group(1) not in hashes:
                fail("C9", f"{f.relative_to(ROOT)}: quoted sha256 {m.group(1)[:12]}… matches no tracked file")
    return n


def main():
    for p in PASSES:
        ni, nc, nr = check_pass(p)
        print(f"{p['name']}: {ni} instances, {nc} coded rows; {nr} `{NO_ROW_FORM}` instances read in full with no row")
    check_successors()
    check_registration()
    print(f"blind scope: {check_scope()} cells")
    hashes = tracked_hashes()
    print(f"manifests: {check_manifests(hashes)} source PDFs excepted as a class")
    print(f"quoted hashes: {check_quoted(hashes)} checked")
    for w in warnings:
        print("warning:", w)
    for f in failures:
        print("FAIL", f)
    print(f"{len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
