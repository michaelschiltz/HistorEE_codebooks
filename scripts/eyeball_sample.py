#!/usr/bin/env python3
"""Seeded sample of record fields for a blind human reading (the 'eyeball check').

The check measures how often a field of a batch's instance record disagrees with
the printed source, read by a person who has not seen the record. It yields the
error-rate register's `human-independent` x `random-seeded` rows
(logbook/4-appendix-error-rates.csv). The protocol for the first run is
records/PROTOCOL-eyeball-madurell-2026-11-19.md.

Three subcommands:

  draw   Draw the sample from the instance record with a fixed seed. Writes the
         reading sheet (no record values, no strata) and the draw key (strata
         and record columns, no record values). The sheet is committed and
         pushed before the reader opens the source; the key is held out of the
         tree until scoring and checked then against the sha256 in the protocol.

  score  Compare the filled sheet with the record. A line matches when the two
         agree after normalisation (case, accents, punctuation, spacing, u/v,
         i/j); for a clause line, also when the record's excerpt is contained in
         the reading, and for 'none' against a coded absence. Every other line
         is flagged for adjudication, where the maintainer rules it a content
         error, a form error, or a reader's slip. The score never decides a
         content error by itself.

  census Write a reading sheet for one field across every instance, leaving out
         the lines a previous sheet already read (the escalation rule of the
         protocol: a stratum with two or more content errors in its ten goes
         to a full census). The key carries no strata and may be committed
         with the sheet. Added 2026-11-20 for the date census.

Usage:
  python scripts/eyeball_sample.py census --field date --exclude-key KEY.csv --sheet SHEET.md --key KEY2.csv
  python scripts/eyeball_sample.py draw  --seed 20261119 --sheet SHEET.md --key KEY.csv
  python scripts/eyeball_sample.py score --sheet FILLED.md --key KEY.csv --out SCORED.csv

The draw is deterministic: the same record file and seed give the same sample.
"""
import argparse
import csv
import hashlib
import random
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORD = ROOT / "records" / "instances-2026-11-03.csv"
PER_STRATUM = 10
ABSENT_TOKENS = {".NR", ".NA", ""}

# Question put to the reader for each field. The same wording serves a field
# whether the record holds a value or a coded absence, so the sheet does not
# reveal which lines are absences.
QUESTIONS = {
    "amount": "Capital entrusted: the sum and the money, as printed. Write 'none' if the act states no sum.",
    "date": "Dating clause: as printed, in full. Write 'none' if the act carries no date.",
    "parties": "Parties: every person named as a party, each with his or her role (who entrusts, who receives, any other party), names as printed. Write 'none' if no party is named.",
    "destination": "Destination of the venture: as printed. Write 'none' if the act names none.",
    "risk": "Risk clause: the clause placing the goods or the capital at someone's risk (risicum, periculum, fortuna, or the like), verbatim. Write 'none' if the act has no such clause.",
    "security": "Obligation clause: the clause binding a person or goods for performance (obligo ..., or the like), verbatim. Write 'none' if the act has no such clause.",
}

# Wording for a census sheet, tightened after the 2026-11-20 adjudication.
CENSUS_QUESTIONS = {
    "date": "Dating clause: every dating clause in the act's own text (an opening date line, a closing 'Actum est hoc ...', or both), each in full as printed, including the year. Not the editor's heading. Write 'none' if the act carries no date.",
}
ACT_NOTE = (" The edition prints more than one act under this number; read act {n}, counting each instrument printed "
            "under the number in order, including one introduced by 'Simile ...' or 'aliud instrumentum'.")

# field -> (column holding the verbatim value, column holding the coded state)
COLUMNS = {
    "amount": ("amount_as_read", None),
    "date": ("date_as_read", None),
    "parties": ("parties", None),
    "destination": ("destination", None),
    "risk": ("peril_clause_quote", "peril_clause"),
    "security": ("security_quote", "security"),
}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_record():
    with RECORD.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def populations(rows):
    """Six strata. Whole columns for the four verbatim fields; the two clause
    families split by the record's state into present (a quotation) and absent
    (coded 'none')."""
    pops = {s: [] for s in ("amount", "date", "parties", "destination", "clause-present", "clause-absent")}
    for r in rows:
        for field in ("amount", "date", "parties", "destination"):
            pops[field].append((r["instance_id"], field))
        for field in ("risk", "security"):
            quote_col, state_col = COLUMNS[field]
            if r[state_col] == "none":
                pops["clause-absent"].append((r["instance_id"], field))
            elif r[quote_col] not in ABSENT_TOKENS:
                pops["clause-present"].append((r["instance_id"], field))
    return {s: sorted(p) for s, p in pops.items()}


def draw(args):
    rows = read_record()
    by_id = {r["instance_id"]: r for r in rows}
    rng = random.Random(args.seed)
    pops = populations(rows)
    picked = []
    for stratum in ("amount", "date", "parties", "destination", "clause-present", "clause-absent"):
        for inst, field in rng.sample(pops[stratum], PER_STRATUM):
            picked.append((stratum, inst, field))
    rng.shuffle(picked)

    key_rows, sheet = [], []
    for line, (stratum, inst, field) in enumerate(picked, 1):
        r = by_id[inst]
        key_rows.append({"line": line, "instance_id": inst, "doc_no": r["doc_no"], "act_in_entry": r["act_in_entry"],
                         "page_printed": r["page_printed"], "field": field, "stratum": stratum,
                         "record_column": COLUMNS[field][0], "population": len(pops[stratum])})
        act = f" (act {r['act_in_entry']} of the entry)" if r["act_in_entry"] != "1" or \
            sum(1 for x in rows if x["doc_no"] == r["doc_no"]) > 1 else ""
        sheet.append(f"## {line}. Doc. {r['doc_no']}{act}, printed p. {r['page_printed']}\n\n"
                     f"Question: {QUESTIONS[field]}\n\nReading: \n")

    with open(args.key, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(key_rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(key_rows)
    head = (f"# Reading sheet: eyeball check, Madurell Marimón & García Sanz 1973\n\n"
            f"Drawn by `scripts/eyeball_sample.py draw --seed {args.seed}` from `records/{RECORD.name}` "
            f"(sha256 `{sha256(RECORD)}`). {len(sheet)} lines. Read each act in full in the printed volume and "
            f"answer the question after `Reading:` on the same line. Do not open the instance record, the text "
            f"layer or the translation Docs until the filled sheet is frozen. Protocol: "
            f"`records/PROTOCOL-eyeball-madurell-2026-11-19.md`.\n\n")
    Path(args.sheet).write_text(head + "\n".join(sheet), encoding="utf-8")
    print(f"record   {RECORD.name}  sha256 {sha256(RECORD)}")
    print(f"sheet    {args.sheet}  sha256 {sha256(args.sheet)}")
    print(f"key      {args.key}  sha256 {sha256(args.key)}")
    for s, p in pops.items():
        print(f"stratum  {s:15s} population {len(p)}")


def census(args):
    rows = read_record()
    with open(args.exclude_key, encoding="utf-8", newline="") as f:
        done = {r["instance_id"] for r in csv.DictReader(f) if r["field"] == args.field}
    todo = [r for r in rows if r["instance_id"] not in done]
    multi = {d for d in {r["doc_no"] for r in rows} if sum(1 for x in rows if x["doc_no"] == d) > 1}
    key_rows, sheet = [], []
    for line, r in enumerate(todo, 1):
        key_rows.append({"line": line, "instance_id": r["instance_id"], "doc_no": r["doc_no"],
                         "act_in_entry": r["act_in_entry"], "page_printed": r["page_printed"], "field": args.field,
                         "stratum": "census", "record_column": COLUMNS[args.field][0], "population": len(todo)})
        act = f" (act {r['act_in_entry']} of the entry)" if r["doc_no"] in multi else ""
        note = ACT_NOTE.format(n=r["act_in_entry"]) if r["doc_no"] in multi else ""
        sheet.append(f"## {line}. Doc. {r['doc_no']}{act}, printed p. {r['page_printed']}\n\n"
                     f"Question: {CENSUS_QUESTIONS[args.field]}{note}\n\nReading: \n")
    with open(args.key, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(key_rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(key_rows)
    head = (f"# Census sheet: {args.field}, Madurell Marimón & García Sanz 1973\n\n"
            f"Written by `scripts/eyeball_sample.py census --field {args.field}` from `records/{RECORD.name}` "
            f"(sha256 `{sha256(RECORD)}`), leaving out the {len(done)} instances already read on the eyeball sheet. "
            f"{len(sheet)} lines, in record order. Read each act in the printed volume and answer after `Reading:`. "
            f"Do not open the instance record, the text layer or the translation Docs until the filled sheet is pushed. "
            f"Rulings that set this census: `records/RULINGS-eyeball-madurell-2026-11-20.md`.\n\n")
    Path(args.sheet).write_text(head + "\n".join(sheet), encoding="utf-8")
    print(f"sheet {args.sheet} sha256 {sha256(args.sheet)}; key {args.key} sha256 {sha256(args.key)}; {len(sheet)} lines")


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = s.replace("v", "u").replace("j", "i")
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def read_sheet(path):
    text = Path(path).read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^## (\d+)\..*?^Reading:[ \t]*(.*?)(?=^## \d+\.|\Z)", text, re.M | re.S):
        out[int(m.group(1))] = m.group(2).strip()
    return out


def score(args):
    rows = {r["instance_id"]: r for r in read_record()}
    readings = read_sheet(args.sheet)
    with open(args.key, encoding="utf-8", newline="") as f:
        key = list(csv.DictReader(f))
    out = []
    for k in key:
        line = int(k["line"])
        reading = readings.get(line, "")
        r = rows[k["instance_id"]]
        value = r[k["record_column"]]
        field = k["field"]
        coded_absent = (value in ABSENT_TOKENS) or (field in ("risk", "security") and r[COLUMNS[field][1]] == "none")
        read_absent = norm(reading) in ("none", "")
        if not reading:
            result = "unread"
        elif coded_absent and read_absent:
            result = "match"
        elif coded_absent != read_absent:
            result = "flag"
        elif norm(value) == norm(reading):
            result = "match"
        elif (field in ("risk", "security") or k["stratum"] == "census") and norm(value) in norm(reading):
            result = "match"
        else:
            result = "flag"
        out.append({**k, "reading": reading, "record_value": value, "auto_result": result,
                    "ruling": "", "error_class": ""})
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    n = len(out)
    print(f"{n} lines: {sum(o['auto_result'] == 'match' for o in out)} match, "
          f"{sum(o['auto_result'] == 'flag' for o in out)} flagged, {sum(o['auto_result'] == 'unread' for o in out)} unread")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("draw")
    d.add_argument("--seed", type=int, required=True)
    d.add_argument("--sheet", required=True)
    d.add_argument("--key", required=True)
    c = sub.add_parser("census")
    c.add_argument("--field", required=True, choices=sorted(CENSUS_QUESTIONS))
    c.add_argument("--exclude-key", required=True)
    c.add_argument("--sheet", required=True)
    c.add_argument("--key", required=True)
    s = sub.add_parser("score")
    s.add_argument("--sheet", required=True)
    s.add_argument("--key", required=True)
    s.add_argument("--out", required=True)
    a = ap.parse_args()
    {"draw": draw, "census": census, "score": score}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
