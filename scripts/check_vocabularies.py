#!/usr/bin/env python3
"""Structural validation of vocabularies/*.csv.

The controlled vocabularies carry `allowed_values`, the component and
work-package assignments, and the dependence columns that the datasets are
checked against. They are NOT declared frictionless resources, so
`frictionless validate` never sees them: a malformed vocabulary row silently
corrupts whatever reads it, and CI cannot tell.

That is not hypothetical. Two rows shipped with an unquoted comma inside a
field — `loss_mitigation_type.csv` (`warichi_iwade`) and `amount_unit.csv`
(`ryo`) — each parsing with one field too many and shifting every value after
it. EDITING-CSV.md warns about precisely this failure, but only for data.csv.

Checks (all fatal):
  1. Header is present, non-empty, free of duplicates and of stray whitespace.
  2. Every row has exactly as many fields as the header — the ragged-row check.
  3. The first column (the code) is non-empty and unique within the file.
  4. No field carries leading or trailing whitespace (the alignment-padding bug
     that broke `clearing_records` once already; see CHANGELOG 0.2.0).
  5. The file is UTF-8 without a BOM and uses LF line endings, per
     .gitattributes.

Referential (fatal): every `type_id` and `char_id` used in a dataset resolves
to a code in the matching vocabulary.

Standard library only, deterministic, no wall-clock dependency — matching
build_codebook.py so CI needs no new runtime.

Usage:
    python3 scripts/check_vocabularies.py
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_DIR = ROOT / "vocabularies"

# dataset -> (type vocabulary, characteristic vocabulary)
REGISTERED = {
    "organizational_forms": (
        "organizational_form_type.csv",
        "organizational_form_characteristic.csv",
    ),
    "loss_mitigation_forms": (
        "loss_mitigation_type.csv",
        "loss_mitigation_characteristic.csv",
    ),
}

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# ----------------------------------------------------------------- structure

def check_file(path: Path) -> set[str]:
    """Validate one vocabulary. Returns the set of codes it defines."""
    rel = path.relative_to(ROOT)
    raw = path.read_bytes()

    if raw.startswith(b"\xef\xbb\xbf"):
        err(f"{rel}: starts with a UTF-8 BOM; save as UTF-8 without BOM")
    if b"\r\n" in raw:
        err(f"{rel}: CRLF line endings; .gitattributes requires LF")

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        err(f"{rel}: not valid UTF-8 ({e})")
        return set()

    rows = list(csv.reader(text.splitlines()))
    if not rows:
        err(f"{rel}: empty file")
        return set()

    header = rows[0]
    if not header or not any(h.strip() for h in header):
        err(f"{rel}: missing or empty header")
        return set()
    for h in header:
        if h != h.strip():
            err(f"{rel}: header field {h!r} has leading/trailing whitespace")
    dupes = {h for h in header if header.count(h) > 1}
    if dupes:
        err(f"{rel}: duplicate header field(s) {sorted(dupes)}")

    codes: set[str] = set()
    seen: dict[str, int] = {}
    for n, row in enumerate(rows[1:], start=2):
        if not row:
            err(f"{rel}:{n}: blank row")
            continue
        if len(row) != len(header):
            err(
                f"{rel}:{n}: {len(row)} fields, header has {len(header)} "
                f"— ragged row (first value {row[0]!r}). "
                "Usually an unquoted comma inside a field."
            )
            continue
        for i, field in enumerate(row):
            if field != field.strip():
                err(
                    f"{rel}:{n}: field {header[i]!r} has leading/trailing "
                    f"whitespace ({field!r})"
                )
        code = row[0]
        if not code.strip():
            err(f"{rel}:{n}: empty code in first column")
            continue
        if code in seen:
            err(f"{rel}:{n}: duplicate code {code!r} (first seen at line {seen[code]})")
        else:
            seen[code] = n
            codes.add(code)
    return codes


# --------------------------------------------------------------- referential

def check_references(vocab_codes: dict[str, set[str]]) -> None:
    for dataset, (type_v, char_v) in REGISTERED.items():
        data = ROOT / "datasets" / dataset / "data.csv"
        if not data.exists():
            continue
        types = vocab_codes.get(type_v)
        chars = vocab_codes.get(char_v)
        if types is None or chars is None:
            err(f"datasets/{dataset}: a registered vocabulary failed to load; "
                "reference check skipped")
            continue
        with data.open(encoding="utf-8", newline="") as fh:
            for n, row in enumerate(csv.DictReader(fh), start=2):
                t, c = row.get("type_id"), row.get("char_id")
                if t and t not in types:
                    err(f"datasets/{dataset}/data.csv:{n}: type_id {t!r} "
                        f"not in {type_v}")
                if c and c not in chars:
                    err(f"datasets/{dataset}/data.csv:{n}: char_id {c!r} "
                        f"not in {char_v}")


def main() -> int:
    files = sorted(VOCAB_DIR.glob("*.csv"))
    if not files:
        print(f"no vocabularies found in {VOCAB_DIR}", file=sys.stderr)
        return 1

    vocab_codes: dict[str, set[str]] = {}
    for path in files:
        vocab_codes[path.name] = check_file(path)

    check_references(vocab_codes)

    if errors:
        print(f"\n✗ {len(errors)} vocabulary error(s):")
        for e in errors:
            print(f"  {e}")
        return 1

    total = sum(len(c) for c in vocab_codes.values())
    print(
        f"✓ vocabularies valid — {len(files)} files, {total} codes, "
        "no ragged rows, all dataset references resolve"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
