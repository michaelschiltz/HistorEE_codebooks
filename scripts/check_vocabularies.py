#!/usr/bin/env python3
"""Structural and semantic validation of vocabularies/*.csv.

The controlled vocabularies carry `allowed_values`, the component and
work-package assignments, and the dependence columns that the datasets are
checked against. They are NOT declared frictionless resources, so
`frictionless validate` never sees them: a malformed vocabulary row silently
corrupts whatever reads it, and CI cannot tell.

That is not hypothetical. Two rows shipped with an unquoted comma inside a
field — `loss_mitigation_type.csv` (`warichi_iwade`) and `amount_unit.csv`
(`ryo`) — each parsing with one field too many and shifting every value after
it. EDITING-CSV.md warns about precisely this failure, but only for data.csv.

WHY THE VOCABULARY EXISTS AT ALL. A Table Schema can only express what is true
of a *column*. The vocabulary expresses what is true of a *cell given another
cell*: which values `value` may take depends on that row's `char_id`, and
whether the cell exists at all depends on `applicability_on`. Frictionless
cannot state a conditional constraint, so the vocabulary is not a convenience
duplicate of the schema — it holds constraints the schema is structurally
incapable of holding. Hence the division of labour this script enforces:

  * a controlled value WITH a vocabulary file  -> the vocabulary is authoritative
  * a small closed schematic set with none     -> the datapackage enum is
  * never both, except where duplication buys standalone validation for
    third-party consumers (see ENUM_VOCAB below)

Checks (all fatal):

  STRUCTURE, per vocabulary file
    1. Header present, non-empty, free of duplicates and stray whitespace.
    2. Every row has exactly as many fields as the header — the ragged-row check.
    3. First column (the code) non-empty and unique within the file.
    4. No field carries leading or trailing whitespace (the alignment-padding
       bug that broke `clearing_records` once; see CHANGELOG 0.2.0).
    5. UTF-8 without BOM, LF line endings, per .gitattributes.

  REFERENTIAL, per dataset
    6. Every `type_id` and `char_id` used resolves to a code in the matching
       vocabulary.
    7. Every `value` is either a missing token or a member of that
       characteristic's `allowed_values` — the conditional constraint the Table
       Schema cannot express, and which CONTRIBUTING §5 previously left to a
       manual sweep.

  AGREEMENT, where a field is deliberately duplicated
    8. A datapackage `enum` and its vocabulary's `code` column list the same
       set. Duplication is kept only where it lets an outside consumer running
       plain `frictionless validate` get the same enforcement we do; this check
       is what stops the two copies drifting.
    9. A code appearing in more than one TYPE vocabulary describes the same
       institution in both, so `name`, `tradition` and `period` must match.
       `societas_maris` is the only such code and its two rows drifted: the
       organizational row carried the researched window while
       `loss_mitigation_type.csv` still read `10-13c`, flagged for
       reconciliation on 2026-08-18 and not closed until 2026-08-31. Every
       other cross-dataset institution uses an `_alloc` code whose stem lives
       in the other file, so its rows cannot disagree; a shared code can, and
       nothing was watching. Period is a property of the institution, not of
       a coding pass.

Standard library only, deterministic, no wall-clock dependency — matching
build_codebook.py so CI needs no new runtime.

Usage:
    python3 scripts/check_vocabularies.py
"""

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_DIR = ROOT / "vocabularies"

# Tokens treated as "no value here". A cell holding one of these is not
# measured against allowed_values.
#
# These are NOT restated from the schemas — they are read out of each dataset's
# own `missingValues` by missing_values() below, so the two cannot drift. The
# constant here is only the fallback for reading a vocabulary file, which has no
# schema of its own, and for the case where a datapackage cannot be parsed.
MISSING_FALLBACK = {"", ".NR", ".IL", ".NA"}


def missing_values(dataset: str) -> set[str]:
    """The dataset's own declared missingValues, so this script cannot drift
    from the schema it is checking against."""
    dp = ROOT / "datasets" / dataset / "datapackage.json"
    if not dp.exists():
        return set(MISSING_FALLBACK)
    try:
        pkg = json.loads(dp.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"datasets/{dataset}/datapackage.json: not valid JSON ({e})")
        return set(MISSING_FALLBACK)
    tokens: set[str] = set()
    for res in pkg.get("resources", []):
        mv = res.get("schema", {}).get("missingValues")
        if mv is not None:
            tokens |= set(mv)
    if not tokens:
        err(f"datasets/{dataset}/datapackage.json: no missingValues declared; "
            "falling back to the built-in token set")
        return set(MISSING_FALLBACK)
    return tokens

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

# (dataset, field) -> vocabulary file, for the few fields deliberately carried
# in BOTH a datapackage enum and a vocabulary. Extend this when a new such pair
# is created — an unregistered duplicate is exactly what drifts unnoticed.
ENUM_VOCAB = {
    ("clearing_records", "instrument_type"): "instrument_type.csv",
    ("clearing_records", "amount_unit"): "amount_unit.csv",
}

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


# ----------------------------------------------------------------- structure

def check_file(path: Path) -> tuple[set[str], dict[str, dict]]:
    """Validate one vocabulary. Returns (codes, rows-by-code)."""
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
        return set(), {}

    rows = list(csv.reader(text.splitlines()))
    if not rows:
        err(f"{rel}: empty file")
        return set(), {}

    header = rows[0]
    if not header or not any(h.strip() for h in header):
        err(f"{rel}: missing or empty header")
        return set(), {}
    for h in header:
        if h != h.strip():
            err(f"{rel}: header field {h!r} has leading/trailing whitespace")
    dupes = {h for h in header if header.count(h) > 1}
    if dupes:
        err(f"{rel}: duplicate header field(s) {sorted(dupes)}")

    codes: set[str] = set()
    by_code: dict[str, dict] = {}
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
            by_code[code] = dict(zip(header, row))
    return codes, by_code


# --------------------------------------------------------------- referential

def check_dataset(name: str, type_v: str, char_v: str,
                  codes: dict[str, set[str]], rows: dict[str, dict]) -> None:
    data = ROOT / "datasets" / name / "data.csv"
    if not data.exists():
        return
    types, chars = codes.get(type_v), codes.get(char_v)
    if types is None or chars is None:
        err(f"datasets/{name}: a registered vocabulary failed to load; "
            "reference check skipped")
        return

    # read the dataset's own missing tokens rather than restating them
    MISSING = missing_values(name)

    # allowed_values per characteristic, split on the pipe
    allowed: dict[str, set[str]] = {}
    for code, r in rows.get(char_v, {}).items():
        spec = (r.get("allowed_values") or "").strip()
        if spec and spec not in MISSING_FALLBACK:
            allowed[code] = {v.strip() for v in spec.split("|") if v.strip()}

    with data.open(encoding="utf-8", newline="") as fh:
        for n, row in enumerate(csv.DictReader(fh), start=2):
            t, c, v = row.get("type_id"), row.get("char_id"), row.get("value")
            if t and t not in types:
                err(f"datasets/{name}/data.csv:{n}: type_id {t!r} not in {type_v}")
            if c and c not in chars:
                err(f"datasets/{name}/data.csv:{n}: char_id {c!r} not in {char_v}")
                continue
            # the conditional constraint: value must suit THIS characteristic
            if c and v is not None and v not in MISSING:
                permitted = allowed.get(c)
                if permitted and v not in permitted:
                    err(
                        f"datasets/{name}/data.csv:{n}: {c} = {v!r} not in "
                        f"allowed_values {sorted(permitted)}"
                    )


# ----------------------------------------------------------------- agreement

def check_cooccurrence(codes: dict[str, set[str]], rows: dict[str, dict]) -> None:
    """Every code listed in cooccurs_with must exist.

    Added after a dangling pair was written within minutes of this script's
    first version — the referential check covered data.csv but not the
    vocabulary's own new column. Cross-dataset references take the documented
    form `code@dataset`.
    """
    DATASET_VOCAB = {ds: tv for ds, (tv, _) in REGISTERED.items()}
    for vocab, by_code in rows.items():
        for code, r in by_code.items():
            spec = (r.get("cooccurs_with") or "").strip()
            basis = (r.get("cooccurrence_basis") or "").strip()
            if not spec or spec in MISSING_FALLBACK:
                continue
            if not basis or basis in MISSING_FALLBACK:
                err(f"{vocab}: {code} lists cooccurs_with but no "
                    "cooccurrence_basis — the level must be declared")
            for ref in (x.strip() for x in spec.split(";") if x.strip()):
                target, _, ds = ref.partition("@")
                pool = codes.get(DATASET_VOCAB.get(ds, vocab)) if ds else codes.get(vocab)
                if ds and ds not in DATASET_VOCAB:
                    err(f"{vocab}: {code} references unknown dataset {ds!r} in {ref!r}")
                elif pool is not None and target not in pool:
                    err(f"{vocab}: {code} cooccurs_with {ref!r}, which is not a "
                        "code in the target vocabulary")
                elif target == code:
                    err(f"{vocab}: {code} lists itself in cooccurs_with")


def check_boundary(rows: dict[str, dict]) -> None:
    """A declared boundary_basis must carry a boundary_confidence, and vice versa.

    Same shape as the cooccurs_with / cooccurrence_basis pairing above and for
    the same reason: a basis asserted without a confidence reads as settled when
    it is not, and a confidence without a basis says how sure we are of nothing.
    `bottomry` and `respondentia` are the motivating case — the boundary between
    them rests on contemporary terminology at LOW confidence pending notarial
    evidence, and that pair of facts has to travel together.
    """
    ALLOWED = {
        "contemporary-terminology",
        "contemporary-legal-form",
        "structural-difference",
        "analyst-split",
        "documented-instance",
    }
    CONF = {"high", "medium", "low"}
    for vocab, by_code in rows.items():
        for code, r in by_code.items():
            if "boundary_basis" not in r:
                continue
            basis = (r.get("boundary_basis") or "").strip()
            conf = (r.get("boundary_confidence") or "").strip()
            has_b = basis and basis not in MISSING_FALLBACK
            has_c = conf and conf not in MISSING_FALLBACK
            if has_b and not has_c:
                err(f"{vocab}: {code} declares boundary_basis {basis!r} but no "
                    "boundary_confidence — how sure must travel with on what grounds")
            if has_c and not has_b:
                err(f"{vocab}: {code} declares boundary_confidence {conf!r} but no "
                    "boundary_basis — a confidence about nothing")
            if has_b and basis not in ALLOWED:
                err(f"{vocab}: {code} boundary_basis {basis!r} not in "
                    f"{sorted(ALLOWED)}")
            if has_c and conf not in CONF:
                err(f"{vocab}: {code} boundary_confidence {conf!r} not in "
                    f"{sorted(CONF)}")


def check_enum_agreement(codes: dict[str, set[str]]) -> None:
    for (name, field), vocab in ENUM_VOCAB.items():
        dp = ROOT / "datasets" / name / "datapackage.json"
        if not dp.exists():
            continue
        pkg = json.loads(dp.read_text(encoding="utf-8"))
        found = None
        for res in pkg.get("resources", []):
            for f in res.get("schema", {}).get("fields", []):
                if f["name"] == field:
                    found = f.get("constraints", {}).get("enum")
        if found is None:
            err(f"datasets/{name}/datapackage.json: field {field!r} has no enum, "
                f"but {vocab} is registered as its duplicate in ENUM_VOCAB")
            continue
        vocab_codes = codes.get(vocab)
        if vocab_codes is None:
            continue
        only_schema = set(found) - vocab_codes
        only_vocab = vocab_codes - set(found)
        if only_schema:
            err(f"datasets/{name} {field}: in datapackage enum but not in "
                f"{vocab}: {sorted(only_schema)}")
        if only_vocab:
            err(f"datasets/{name} {field}: in {vocab} but not in the "
                f"datapackage enum: {sorted(only_vocab)}")


def check_type_row_agreement(rows: dict[str, dict]) -> None:
    """A code in two type vocabularies is one institution, so its descriptive
    fields must agree.

    Only the fields that describe the INSTITUTION are compared. `key_source`,
    `cooccurs_with` and the boundary columns are deliberately excluded: those
    describe a coding pass and legitimately differ between the two censuses,
    which measure different aspects of the same form.
    """
    SHARED_FIELDS = ("name", "tradition", "period")
    type_vocabs = [tv for tv, _ in REGISTERED.values()]

    seen: dict[str, list[str]] = {}
    for vocab in type_vocabs:
        for code in rows.get(vocab, {}):
            seen.setdefault(code, []).append(vocab)

    for code, homes in sorted(seen.items()):
        if len(homes) < 2:
            continue
        for field in SHARED_FIELDS:
            values: dict[str, list[str]] = {}
            for vocab in homes:
                row = rows[vocab][code]
                if field not in row:
                    continue
                values.setdefault((row.get(field) or "").strip(), []).append(vocab)
            if len(values) > 1:
                shown = "; ".join(
                    f"{', '.join(v)}={k!r}" for k, v in sorted(values.items())
                )
                err(f"{code}: {field} differs across type vocabularies — {shown}. "
                    "A code shared by two type vocabularies names one institution; "
                    "its descriptive fields must match.")


def main() -> int:
    files = sorted(VOCAB_DIR.glob("*.csv"))
    if not files:
        print(f"no vocabularies found in {VOCAB_DIR}", file=sys.stderr)
        return 1

    codes: dict[str, set[str]] = {}
    rows: dict[str, dict] = {}
    for path in files:
        c, r = check_file(path)
        codes[path.name], rows[path.name] = c, r

    for name, (type_v, char_v) in REGISTERED.items():
        check_dataset(name, type_v, char_v, codes, rows)

    check_cooccurrence(codes, rows)
    check_boundary(rows)
    check_enum_agreement(codes)
    check_type_row_agreement(rows)

    if errors:
        print(f"\n✗ {len(errors)} vocabulary error(s):")
        for e in errors:
            print(f"  {e}")
        return 1

    total = sum(len(c) for c in codes.values())
    print(
        f"✓ vocabularies valid — {len(files)} files, {total} codes; "
        "no ragged rows, all references resolve, "
        "all values within allowed_values, enums agree, shared type rows agree"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
