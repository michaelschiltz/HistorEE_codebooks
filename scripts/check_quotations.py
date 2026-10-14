#!/usr/bin/env python3
"""Checks on original-script quotations in the census datasets.

THE CONVENTION (CONTRIBUTING §4, "Original script"). A cell whose source is
written in a non-Latin script quotes the clause it rests on in that script,
inline in `notes`, before any transliteration or translation. The quotation is
repeated in every cell it supports: storage is free, and a cell must be
checkable on its own by a reader who has filtered the deposit down to one
(type_id, char_id) without a join. Duplication buys that, and these checks pay
for it by catching the copies when they drift apart.

Until 2026-10-14 the practice was informal. Japanese and Chinese cells already
quoted their originals (236 of 278 `ja` cells, 16 of 21 `zh`); not one of the
49 `ar` cells and none of the 7 `arc` cells carried a character of the script
their source is written in. The Arabic clauses stood in an ASCII
transliteration that cannot be reversed — it writes ʿayn and hamza alike and
drops the emphatics.

Checks:

  HYGIENE, every field of every data.csv and recodings.csv (fatal)
    1. Text is in Unicode NFC. Never NFKC: compatibility folding erases the
       CJK compatibility ideographs (U+F900–FAFF) an edition may print on
       purpose.
    2. No Arabic presentation forms (U+FB50–FDFF, U+FE70–FEFF). They are the
       signature of OCR output and of text copied out of a PDF; they render
       like the base letters and do not match them in a search.
    3. No Private Use Area code points. A character with no Unicode code point
       is described (IDS, or a GlyphWiki reference) in prose, not encoded in a
       private slot that means nothing outside one font.

  DRIFT, across both data.csv files (fatal)
    4. Two cells quoting the same passage must quote it identically. A pair of
       original-script runs that share most of their letters, and agree on at
       least six letters on each side of a difference of at most three letters,
       is reported: that is one passage, copied twice,
       corrected or mistyped in one copy only. The check never says which copy
       is right — that is a matter of re-reading the page.

  COVERAGE, data.csv (reported; fatal under --strict)
    5. An `articulated` cell whose `source_lang` is written in a non-Latin
       script carries at least one character of that script in `notes`.
       `articulated` means the tradition said it in its own idiom; the idiom
       is evidenced best in its own script. A source that printed only a
       transliteration gives no original to quote: say so in the note
       ("original not printed in <source>") and the cell is exempt.

Standard library only, deterministic.

Usage:
    python3 scripts/check_quotations.py            # coverage reported, not fatal
    python3 scripts/check_quotations.py --strict   # coverage fatal too
"""

import argparse
import csv
import difflib
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATASETS = ["organizational_forms", "loss_mitigation_forms"]

SCRIPTS = {
    "Han": [(0x3400, 0x4DBF), (0x4E00, 0x9FFF), (0xF900, 0xFAFF), (0x20000, 0x3134F)],
    "Kana": [(0x3040, 0x30FF), (0x31F0, 0x31FF), (0xFF66, 0xFF9F)],
    "Arabic": [(0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF)],
    "Hebrew": [(0x0590, 0x05FF)],
    "Syriac": [(0x0700, 0x074F)],
    "ImperialAramaic": [(0x10840, 0x1085F)],
}

# source_lang -> scripts any one of which satisfies coverage. Aramaic is printed
# in square (Hebrew) script in the Talmudic editions, in Syriac script for
# Syriac texts, and in Imperial Aramaic only in epigraphic editions.
LANG_SCRIPTS = {
    "ar": {"Arabic"},
    "he": {"Hebrew"},
    "arc": {"Hebrew", "Syriac", "ImperialAramaic"},
    "zh": {"Han"},
    "ja": {"Han", "Kana"},
}

PRESENTATION = [(0xFB50, 0xFDFF), (0xFE70, 0xFEFF)]
PUA = [(0xE000, 0xF8FF), (0xF0000, 0xFFFFD), (0x100000, 0x10FFFD)]

EXEMPT_MARK = "original not printed in"
FLANK = 6        # equal LETTERS (not marks) required on each side of a difference
MAX_DIFF = 3     # a divergence of more letters than this is a different excerpt, not drift:
                 # formulaic text (פלגא באגר פלגא בהפסד / פלגא באגר תרי תילתי בהפסד) shares
                 # long stretches between genuinely different clauses
SAME_PASSAGE = 0.7  # share of the shorter run's letters the two runs must have in common
MIN_RUN = 6      # script characters a run needs before it is compared
SEED = 6         # n-gram used to find candidate pairs
ELLIPSIS = {"…", "⋯", "‥"}  # an elision ends a run: an excerpt is not a variant


def in_ranges(cp: int, ranges) -> bool:
    return any(a <= cp <= b for a, b in ranges)


def script_of(ch: str):
    cp = ord(ch)
    for name, ranges in SCRIPTS.items():
        if in_ranges(cp, ranges):
            return name
    return None


def letters(s: str) -> int:
    """Base letters only: Arabic and Hebrew vowel marks are not counted, so a
    vocalised and an unvocalised copy of one phrase weigh the same."""
    return sum(1 for c in s if unicodedata.category(c)[0] == "L")


def strip_marks(s: str) -> str:
    return "".join(c for c in s if unicodedata.category(c)[0] != "M")


def runs(text: str):
    """Maximal stretches of non-Latin text. Combining marks are always part of
    a run; spaces and non-ASCII punctuation (、。「」، ؛) are absorbed when they
    sit between two script characters, so a vocalised Arabic phrase or a
    Japanese clause with 、 is one run. ASCII punctuation and digits end a run:
    '327 長值貧門; 328 一隻' is a list of items, not one quotation. Returns the
    runs with at least MIN_RUN script characters."""
    out, cur, n, pending = [], [], 0, []

    def close():
        if n >= MIN_RUN:
            out.append("".join(cur))

    for ch in text:
        cat = unicodedata.category(ch)
        if script_of(ch):
            cur.extend(pending)
            pending = []
            cur.append(ch)
            n += 1
        elif cur and cat[0] == "M":
            cur.extend(pending)
            pending = []
            cur.append(ch)
        elif cur and ch not in ELLIPSIS and (ch == " " or (cat[0] in "PZ" and ord(ch) > 0x7F)):
            pending.append(ch)
        else:
            close()
            cur, n, pending = [], 0, []
    close()
    return out


def read(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def hygiene(rel: str, rows, errors):
    for i, r in enumerate(rows, start=2):
        rid = r.get("record_id") or r.get("recoding_id") or f"line {i}"
        for k, v in r.items():
            if not v:
                continue
            if unicodedata.normalize("NFC", v) != v:
                errors.append(f"{rel} {rid} {k}: not NFC")
            bad = sorted({f"U+{ord(c):04X}" for c in v if in_ranges(ord(c), PRESENTATION)})
            if bad:
                errors.append(f"{rel} {rid} {k}: Arabic presentation forms {', '.join(bad[:5])}")
            bad = sorted({f"U+{ord(c):04X}" for c in v if in_ranges(ord(c), PUA)})
            if bad:
                errors.append(f"{rel} {rid} {k}: Private Use Area {', '.join(bad[:5])}")


def drift(items, errors):
    """items: (record_id, run) across BOTH censuses — the same clause is often
    quoted in an organizational cell and its _alloc twin."""
    index = defaultdict(set)
    for n, (_, run) in enumerate(items):
        for j in range(len(run) - SEED + 1):
            index[run[j:j + SEED]].add(n)
    pairs = set()
    for bucket in index.values():
        if 1 < len(bucket) < 200:
            b = sorted(bucket)
            for x in range(len(b)):
                for y in range(x + 1, len(b)):
                    if items[b[x]][0] != items[b[y]][0]:
                        pairs.add((b[x], b[y]))
    seen = set()
    for x, y in sorted(pairs):
        (ra, a), (rb, b) = items[x], items[y]
        # Compare base letters only: a vocalised and an unvocalised copy of one
        # phrase are the same quotation pointed differently, not a variant.
        a, b = strip_marks(a), strip_marks(b)
        if a == b or a in b or b in a:
            continue
        ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
        shared = sum(letters(a[i1:i2]) for tag, i1, i2, _, _ in ops if tag == "equal")
        if shared < SAME_PASSAGE * min(letters(a), letters(b)):
            continue   # two passages sharing common words, not one passage twice
        for k in range(1, len(ops) - 1):
            tag, i1, i2, j1, j2 = ops[k]
            before, after = ops[k - 1], ops[k + 1]
            if (tag != "equal" and before[0] == "equal" and after[0] == "equal"
                    and max(letters(a[i1:i2]), letters(b[j1:j2])) <= MAX_DIFF
                    and letters(a[before[1]:before[2]]) >= FLANK
                    and letters(a[after[1]:after[2]]) >= FLANK):
                key = (ra, rb, a[i1:i2], b[j1:j2])
                if key in seen:
                    continue
                seen.add(key)
                ctx = a[max(i1 - 8, 0):i2 + 8]
                errors.append(f"{ra} / {rb}: same passage quoted differently: "
                              f"'{a[i1:i2]}' vs '{b[j1:j2]}' in …{ctx}…")


def coverage(rel: str, rows, report):
    for r in rows:
        need = LANG_SCRIPTS.get(r.get("source_lang", ""))
        if not need or r.get("articulation") != "articulated":
            continue
        notes = r.get("notes", "")
        if EXEMPT_MARK in notes:
            continue
        if not any(script_of(c) in need for c in notes):
            report.append(f"{rel} {r['record_id']} {r['type_id']} {r['char_id']} "
                          f"[{r['source_lang']}]: articulated, no {'/'.join(sorted(need))} in notes")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="make coverage gaps fatal")
    args = ap.parse_args()
    errors, gaps, items = [], [], []
    for ds in DATASETS:
        for name in ("data.csv", "recodings.csv"):
            p = ROOT / "datasets" / ds / name
            if not p.exists():
                continue
            rel = f"datasets/{ds}/{name}"
            rows = read(p)
            hygiene(rel, rows, errors)
            if name == "data.csv":
                items += [(r["record_id"], run) for r in rows for run in runs(r.get("notes", ""))]
                coverage(rel, rows, gaps)
    drift(items, errors)
    for e in errors:
        print(f"ERROR {e}")
    for g in gaps:
        print(f"{'ERROR' if args.strict else 'GAP'} {g}")
    print(f"check_quotations: {len(errors)} error(s), {len(gaps)} coverage gap(s)"
          f"{' (fatal: --strict)' if args.strict else ' (reported, not fatal)'}")
    return 1 if errors or (args.strict and gaps) else 0


if __name__ == "__main__":
    sys.exit(main())
