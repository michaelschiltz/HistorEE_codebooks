#!/usr/bin/env python3
"""Apply a proposed row fragment to its dataset's data.csv, matching on record_id.

Replacements only: every record_id in the fragment must already exist. Refuses to
run otherwise, so a fragment of NEW rows cannot be applied by accident — appending
is a different operation with different preconditions (contiguous ids, no clash)
and belongs in its own batch script.

Lives in scripts/ deliberately. The previous version of this file sat in
proposed-of/, which .gitignore matches as `proposed*/`, so it was never in the
index and was lost when the staging folders were cleared on 2026-08-31. Anything
worth running twice belongs in a tracked directory.

    python3 scripts/apply-fragment.py <fragment.csv> [...]          # dry run
    python3 scripts/apply-fragment.py --write <fragment.csv> [...]

Reports the `value` fill count before and after. That number is what decides
whether codebook.md has gone stale: a pure replacement leaves the row count
untouched, so `build_codebook.py --check` is the only thing that will notice,
and only if you run it.

Standard library only, deterministic, no wall-clock dependency.
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREFIX = {"OF": "organizational_forms",
          "LM": "loss_mitigation_forms",
          "CR": "clearing_records"}
MISSING = {"", ".NR", ".IL", ".NA"}


def die(msg: str) -> None:
    print(f"ABORT: {msg}", file=sys.stderr)
    raise SystemExit(1)


def read_csv(path: Path) -> list[list[str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.reader(fh))


def apply_one(frag_path: Path, write: bool) -> bool:
    frag = read_csv(frag_path)
    if len(frag) < 2:
        die(f"{frag_path}: no data rows")
    fhdr, frows = frag[0], frag[1:]

    prefixes = {r[0][:2] for r in frows}
    if len(prefixes) != 1:
        die(f"{frag_path}: rows span more than one dataset ({sorted(prefixes)})")
    prefix = prefixes.pop()
    if prefix not in PREFIX:
        die(f"{frag_path}: unknown record_id prefix {prefix!r}")
    dataset = PREFIX[prefix]

    data_path = ROOT / "datasets" / dataset / "data.csv"
    if not data_path.exists():
        die(f"{data_path} not found")
    data = read_csv(data_path)
    dhdr, drows = data[0], data[1:]

    if fhdr != dhdr:
        die(f"{frag_path}: header does not match {dataset}/data.csv.\n"
            f"       fragment: {fhdr}\n       data.csv: {dhdr}")

    idx = {r[0]: i for i, r in enumerate(drows)}
    unknown = [r[0] for r in frows if r[0] not in idx]
    if unknown:
        die(f"{frag_path}: record_id(s) not present in {dataset}/data.csv: "
            f"{unknown}. This script replaces rows; it does not append them.")

    dup = {r[0] for r in frows if [x[0] for x in frows].count(r[0]) > 1}
    if dup:
        die(f"{frag_path}: record_id(s) appear twice in the fragment: {sorted(dup)}")

    changes, noop = [], []
    for r in frows:
        old = drows[idx[r[0]]]
        (noop if old == r else changes).append((old, r))

    if noop and not changes:
        die(f"{frag_path}: every row is already identical to data.csv. "
            "Already applied?")

    before = sum(1 for r in drows if r[3] not in MISSING)
    after = before
    print(f"  {frag_path.name} -> {dataset}/data.csv")
    for old, new in changes:
        diffs = [f"{dhdr[i]} {old[i]!r} -> {new[i]!r}"
                 for i in range(len(dhdr)) if old[i] != new[i] and dhdr[i] != "notes"]
        note = "  (+notes)" if old[-1] != new[-1] else ""
        print(f"    {new[0]}  {new[1]}/{new[2]}  " + "; ".join(diffs) + note)
        if old[3] not in MISSING and new[3] in MISSING:
            after -= 1
        elif old[3] in MISSING and new[3] not in MISSING:
            after += 1
    for old, new in noop:
        print(f"    {new[0]}  unchanged, skipped")
    print(f"    rows {len(drows)} (unchanged); `value` fill {before} -> {after}")

    if write:
        for old, new in changes:
            drows[idx[new[0]]] = new
        with data_path.open("w", newline="", encoding="utf-8") as fh:
            csv.writer(fh, quoting=csv.QUOTE_MINIMAL,
                       lineterminator="\n").writerows([dhdr] + drows)
    return before != after


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--write"]
    write = "--write" in sys.argv
    if not args:
        print(__doc__)
        return 1

    fill_moved = False
    for a in args:
        p = Path(a)
        if not p.exists():
            die(f"{a}: not found")
        fill_moved |= apply_one(p, write)

    if not write:
        print("\ndry run - nothing written. Re-run with --write to apply.")
        return 0

    print("\nwritten. Now, in this order:")
    if fill_moved:
        print("  python3 scripts/build_codebook.py datasets/<dataset>   "
              "# REQUIRED - the fill count moved")
    print("  python3 scripts/build_codebook.py --check")
    print("  python3 -m frictionless validate datasets/<dataset>/datapackage.json")
    print("  python3 scripts/check_dependence.py datasets/<dataset>")
    print("  python3 scripts/check_vocabularies.py")
    print("  python3 scripts/build_views.py --component <c>   # if a coded value changed")
    print("This script does not run git.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
