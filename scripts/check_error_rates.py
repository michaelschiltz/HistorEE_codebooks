#!/usr/bin/env python3
"""Check the error-rate register, logbook/4-appendix-error-rates.csv, and say
which of its rates may be cited as independent.

One row per measurement of one stage of one pass: a text layer, an OCR
re-run, a field extraction. `n` is the number of reference units compared,
`errors` the number of units the reference read differently (wrong, dropped
or omitted), `rate` = errors / n to four places.

Two columns decide what a rate is evidence of, and they are the reason the
register exists rather than the numbers scattered across records/:

  sample          chosen-pages    pages someone picked; a rate for those pages
                  all-units       every unit of the pass compared
                  random-seeded   units drawn by a committed seed before reading
  reference_type  assistant-image-read   the assistant's own reading of the image
                  maintainer-image-read  MS reading the image, not blind to the value
                  human-independent      a person reading the image blind to the
                                         value under test

Only `human-independent` against `random-seeded` or `all-units` is an
independent error rate. Everything else is a measurement, recorded so that it
is not lost and labelled so that it is not over-cited. A comparison against
the assistant's own reading shares the assistant's blind spots: the Yamamoto
pilot found its reference had regularised two readings toward the expected
wording, where the OCR was also wrong.

`record` names the repository file the measurement comes from. A measurement
whose record lives outside the repository is prefixed `external:` and warned
about: the register can point there, but the deposit cannot check it.

Usage:  python scripts/check_error_rates.py
Exit:   1 on a malformed row, else 0. The citable count is reported, not enforced.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "logbook" / "4-appendix-error-rates.csv"
COLUMNS = ["measure_id", "measured_on", "pass", "work", "stage", "configuration", "unit", "n",
           "errors", "rate", "sample", "reference_type", "reference", "record", "notes"]
STAGES = {"text-layer", "ocr-rerun", "transcription", "translation", "field-extraction"}
SAMPLES = {"chosen-pages", "all-units", "random-seeded"}
REFERENCES = {"assistant-image-read", "maintainer-image-read", "human-independent"}


def main():
    errors, warnings = [], []
    with REGISTER.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            print(f"FAIL header is {reader.fieldnames}, expected {COLUMNS}")
            return 1
        rows = list(reader)

    works = set()
    wpath = ROOT / "references" / "works.csv"
    if wpath.exists():
        with wpath.open(encoding="utf-8", newline="") as f:
            works = {r["label"] for r in csv.DictReader(f)}

    for k, r in enumerate(rows, start=1):
        where = f"line {k + 1} ({r['measure_id']})"
        if r["measure_id"] != f"ER-{k:04d}":
            errors.append(f"{where}: ids run ER-0001 upward without gaps; expected ER-{k:04d}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["measured_on"]):
            errors.append(f"{where}: measured_on is not YYYY-MM-DD")
        for col, allowed in (("stage", STAGES), ("sample", SAMPLES), ("reference_type", REFERENCES)):
            if r[col] not in allowed:
                errors.append(f"{where}: {col} '{r[col]}' not in {sorted(allowed)}")
        try:
            n, e = int(r["n"]), int(r["errors"])
            if n <= 0 or not 0 <= e <= n:
                errors.append(f"{where}: needs n > 0 and 0 <= errors <= n")
            elif r["rate"] != f"{e / n:.4f}":
                errors.append(f"{where}: rate {r['rate']} is not errors/n = {e / n:.4f}")
        except ValueError:
            errors.append(f"{where}: n and errors must be integers")
        for col in ("pass", "work", "configuration", "unit", "reference", "record"):
            if not r[col].strip():
                errors.append(f"{where}: {col} is empty")
        rec = r["record"]
        if rec.startswith("external:"):
            warnings.append(f"{where}: record outside the repository ({rec[9:].strip()[:60]})")
        elif not (ROOT / rec).exists():
            errors.append(f"{where}: record {rec} does not exist")
        if works and r["work"] not in works:
            warnings.append(f"{where}: work '{r['work']}' is not in references/works.csv")

    citable = [r for r in rows if r["reference_type"] == "human-independent"
               and r["sample"] in {"random-seeded", "all-units"}]
    print(f"{len(rows)} measurements")
    for (ref, smp), c in sorted(Counter((r["reference_type"], r["sample"]) for r in rows).items()):
        print(f"  {ref:22} {smp:14} {c}")
    print(f"{len(citable)} citable as independent error rates")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("FAIL", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
