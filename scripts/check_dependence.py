#!/usr/bin/env python3
"""Check the declared character dependences in organizational_form_characteristic.csv
against the codings in a dataset's data.csv.

Two relations are checked, and they are deliberately distinct:

  applicability_on  -- whether a cell should exist at all. If the gating
                       characteristic takes a blocking value, the dependent
                       must be .NA; if it does not block, .NA is suspicious.
  dependence_group  -- whether a cell adds evidence. Members of a group encode
                       the same underlying fact, so a contrast appearing in all
                       of them is one datum, not several. Reported, not enforced:
                       collinearity is the expectation here, not an error.

frictionless validates types, enums and keys. It cannot see either of these,
because both live in the vocabulary rather than in the Table Schema.

Usage:  python scripts/check_dependence.py [datasets/organizational_forms]
Exit:   1 if an applicability violation is found, else 0.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

# Gate values that make the dependent characteristic inapplicable.
# Keyed (dependent, gate). Kept explicit rather than inferred: "which values
# block" is a substantive claim about the characteristic, not a rule.
BLOCKING = {
    ("LR5", "LR4"): {"0"},
    ("LR6", "LR2"): {"veiled"},
    ("CF2", "CF1"): {"0", ".NA"},
    ("MG3", "MG1"): {"contract", "beneficiary"},
}
MISSING = {".NR", ".IL", ".NA"}


def load(dataset: Path, vocab: Path):
    chars = {r["code"]: r for r in csv.DictReader(vocab.open(encoding="utf-8"))}
    rows = list(csv.DictReader((dataset / "data.csv").open(encoding="utf-8")))
    grid = defaultdict(dict)
    for r in rows:
        grid[r["type_id"]][r["char_id"]] = r["value"]
    return chars, grid


def check_applicability(chars, grid):
    problems = 0
    for dep, c in chars.items():
        gate = c.get("applicability_on", ".NA")
        if gate in MISSING:
            continue
        for form, cells in grid.items():
            if dep not in cells or gate not in cells:
                continue
            gv, dv = cells[gate], cells[dep]
            blocking = BLOCKING.get((dep, gate), set())
            if gv in blocking and dv != ".NA":
                print(f"  VIOLATION  {form}: {gate}={gv} makes {dep} inapplicable, but {dep}={dv}")
                problems += 1
            elif gv not in blocking and gv != ".NA" and dv == ".NA":
                print(f"  SUSPECT    {form}: {gate}={gv} does not block, yet {dep}=.NA "
                      f"(should this be .NR?)")
                problems += 1
    if not problems:
        print("  no applicability problems")
    return problems


def report_groups(chars, grid):
    groups = defaultdict(list)
    for code, c in chars.items():
        g = c.get("dependence_group", ".NA")
        if g not in MISSING:
            groups[g].append(code)
    for g, members in sorted(groups.items()):
        members = sorted(members)
        print(f"\n  [{g}] {members}")
        sigs = defaultdict(list)
        for form, cells in grid.items():
            if not all(m in cells for m in members):
                continue
            sigs[tuple(cells[m] for m in members)].append(form)
        for sig, forms in sigs.items():
            print(f"    {dict(zip(members, sig))}  <- {', '.join(sorted(forms))}")
        n_forms = sum(len(v) for v in sigs.values())
        n_sigs = len(sigs)
        if n_forms < 3:
            print(f"    {n_forms} forms coded - too few to say anything; "
                  f"any two characteristics look collinear at n=2")
            continue
        if n_sigs == 1:
            print(f"    {n_forms} forms, 1 signature - ZERO VARIANCE, carries no information yet")
            continue
        # A group collapses to one degree of freedom only if knowing any member
        # determines every other. Counting distinct signatures does NOT test this:
        # n forms with n signatures is equally consistent with total independence.
        # The real test is whether each ordered pair is a function.
        separated = []
        for a in members:
            for b in members:
                if a == b:
                    continue
                mapping = defaultdict(set)
                for sig in sigs:
                    mapping[sig[members.index(a)]].add(sig[members.index(b)])
                for av, bvs in mapping.items():
                    if len(bvs) > 1:
                        separated.append((a, b, av, sorted(bvs)))
        # Separation via a missing token is weaker evidence than separation
        # between two substantive values: .NA says the cell does not apply,
        # which is a fact about scope rather than about the characteristics
        # varying independently.
        strong = [s for s in separated
                  if s[2] not in MISSING and not (set(s[3]) & MISSING)]
        if not separated:
            print(f"    {n_forms} forms - every member determines every other: "
                  f"COLLAPSED to one degree of freedom across the coded set")
        else:
            verdict = ("SEPARATED on substantive values" if strong
                       else "separated only via missing tokens - weak, scope not independence")
            print(f"    {n_forms} forms - {verdict}:")
            seen = set()
            for a, b, av, bvs in separated:
                key = tuple(sorted((a, b)))
                if key in seen:
                    continue
                seen.add(key)
                weak = "" if (av not in MISSING and not (set(bvs) & MISSING)) else "   [weak: via .NA]"
                print(f"      {a}={av} occurs with {b} in {bvs}"
                      f" - {a} does not determine {b}{weak}")



def check_articulation(dataset: Path) -> int:
    """'articulated' asserts the tradition stated the function in its own idiom.
    That cannot rest on a placeholder citation: a modern secondary work is
    admissible only where it quotes the doctrinal text, which '[verify]' by
    definition does not."""
    import csv as _csv
    problems = 0
    for r in _csv.DictReader((dataset / "data.csv").open(encoding="utf-8")):
        if r.get("articulation") == "articulated" and r.get("source_ref") in ("[verify]", ".NR", ""):
            print(f"  VIOLATION  {r['record_id']} {r['type_id']}/{r['char_id']}: "
                  f"articulated but source_ref={r['source_ref']!r}")
            problems += 1
    if not problems:
        print("  no articulation problems")
    return problems


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    dataset = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "datasets/organizational_forms"
    vocab = root / "vocabularies/organizational_form_characteristic.csv"
    chars, grid = load(dataset, vocab)

    print("=== applicability (enforced) ===")
    problems = check_applicability(chars, grid)
    print("\n=== articulation (enforced) ===")
    problems += check_articulation(dataset)
    print("\n=== redundancy groups (reported) ===")
    report_groups(chars, grid)
    print(f"\napplicability violations: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
