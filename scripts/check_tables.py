#!/usr/bin/env python3
"""Enforce aligned Markdown tables on hand-written prose.

House style: a Markdown table's rows are padded to equal column widths, so the
table is legible in the raw file and not only after rendering. The generators
have produced aligned tables since the beginning (`md_table` in
`build_codebook.py`, shared with `build_views.py` since 2026-09-05); hand-written
tables in the logbooks, the CHANGELOG and the doctrine files had no such rule and
no check, and 25 of 37 of them had drifted ragged by 2026-09-08.

    python scripts/check_tables.py [PATH ...]        # report, exit 1 on any
    python scripts/check_tables.py --fix [PATH ...]  # align in place

Only whitespace between the pipes is ever changed. The rewrite is verified by
re-parsing both versions with the same Markdown parser the soft-wrap checker
uses and asserting that every cell's content is identical; a file whose cells
would change is left alone and reported as an error, never written.

GENERATED FILES ARE CHECKED BUT NEVER FIXED. `datasets/*/codebook.md` and
`views/*.md` come from their build scripts, so a ragged table there is a bug in
the generator and must be fixed at the source. Checking them is deliberate: it
asserts that `md_table`'s idea of alignment and this script's agree.
"""
from __future__ import annotations

import argparse
import fnmatch
import sys
import unicodedata
from pathlib import Path

from markdown_it import MarkdownIt

REPO = Path(__file__).resolve().parent.parent

# A verbatim legal document; nobody formats its tables and it must stay byte-exact.
EXCLUDE = ["LICENSE-DATA.md"]

# Checked for drift, but --fix refuses them: the fix belongs in the generator.
GENERATED = ["datasets/*/codebook.md", "views/*.md"]

_MD = MarkdownIt("commonmark").enable("table")


def _match(rel: str, pats: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, p) for p in pats)


def width(text: str) -> int:
    """Display width in a monospace font: East-Asian wide/fullwidth count two.

    `md_table` uses len() instead. No generated table has ever contained a wide
    character, so the two agree today; logbook 5 has eleven rows that would
    misalign under len(), which is why this script does it properly.
    """
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1 for c in text)


def pad(text: str, w: int, align: str) -> str:
    slack = w - width(text)
    if slack <= 0:
        return text
    if align == "r":
        return " " * slack + text
    if align == "c":
        left = slack // 2
        return " " * left + text + " " * (slack - left)
    return text + " " * slack


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_delimiter(line: str) -> bool:
    s = line.strip()
    return (s.startswith("|") and s.replace("|", "").strip() != ""
            and set(s.replace("|", "").strip()) <= set("-: "))


def find_tables(lines: list[str]) -> list[tuple[int, int]]:
    """Return (start, end) line indices of each table block, end exclusive."""
    out, i = [], 0
    while i < len(lines):
        if (lines[i].lstrip().startswith("|") and i + 1 < len(lines)
                and is_delimiter(lines[i + 1])):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out.append((i, j))
            i = j
        else:
            i += 1
    return out


def aligns_of(delim: str) -> list[str]:
    out = []
    for c in split_row(delim):
        left, right = c.startswith(":"), c.endswith(":")
        out.append("c" if left and right else "r" if right else "l")
    return out


def render(block: list[str]) -> list[str]:
    header, delim, body = block[0], block[1], block[2:]
    aligns = aligns_of(delim)
    rows = [split_row(header)] + [split_row(r) for r in body]
    ncol = len(aligns)
    # A row with the wrong cell count is left exactly as it is: reflowing it
    # would invent or drop a cell, and that is a content change.
    if any(len(r) != ncol for r in rows):
        return block

    widths = [max(width(r[i]) for r in rows) for i in range(ncol)]

    def sep(w: int, a: str) -> str:
        if a == "r":
            return "-" * (w + 1) + ":"
        if a == "c":
            return ":" + "-" * w + ":"
        return "-" * (w + 2)

    out = ["| " + " | ".join(pad(c, w, a) for c, w, a in zip(rows[0], widths, aligns)) + " |",
           "|" + "|".join(sep(w, a) for w, a in zip(widths, aligns)) + "|"]
    for r in rows[1:]:
        out.append("| " + " | ".join(pad(c, w, a) for c, w, a in zip(r, widths, aligns)) + " |")
    return out


def cells_of(text: str) -> list[str]:
    return [t.content for t in _MD.parse(text) if t.type == "inline"]


def process(path: Path, fix: bool, generated: bool) -> tuple[int, int]:
    """Return (ragged tables, tables whose rewrite was refused)."""
    original = path.read_text(encoding="utf-8")
    lines = original.split("\n")
    ragged = refused = 0
    for start, end in reversed(find_tables(lines)):
        block = lines[start:end]
        new = render(block)
        if new == block:
            continue
        # Content guard: the rewrite may move whitespace and nothing else.
        if cells_of("\n".join(block)) != cells_of("\n".join(new)):
            print(f"{path}:{start + 1}: REFUSED — rewrite would change cell "
                  f"content; left untouched", file=sys.stderr)
            refused += 1
            continue
        ragged += 1
        if fix and not generated:
            lines[start:end] = new
    if fix and not generated and ragged:
        path.write_text("\n".join(lines), encoding="utf-8")
    return ragged, refused


def discover() -> list[Path]:
    out = []
    for p in sorted(REPO.rglob("*.md")):
        rel = p.relative_to(REPO).as_posix()
        if rel.startswith((".git/", "proposed-of/", "proposed/")):
            continue
        if _match(rel, EXCLUDE):
            continue
        out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--fix", action="store_true", help="align tables in place")
    args = ap.parse_args()

    targets = [p for p in args.paths] if args.paths else discover()
    ragged = refused = checked = gen_ragged = 0
    for path in targets:
        path = path.resolve()
        if not path.exists():
            print(f"warning: {path} does not exist", file=sys.stderr)
            continue
        rel = path.relative_to(REPO).as_posix() if REPO in path.parents else path.name
        generated = _match(rel, GENERATED)
        checked += 1
        r, x = process(path, args.fix, generated)
        refused += x
        if generated and r:
            gen_ragged += r
            print(f"{rel}: {r} ragged table(s) — GENERATED FILE, fix "
                  f"md_table in its build script, not the file", file=sys.stderr)
        elif r:
            ragged += r
            if not args.fix:
                print(f"{rel}: {r} ragged table(s)", file=sys.stderr)

    if refused:
        print(f"\n{refused} table(s) refused: a rewrite would have changed cell "
              f"content. Fix those by hand.", file=sys.stderr)
        return 1
    if args.fix:
        print(f"aligned {ragged} table(s) in {checked} file(s).")
        return 1 if gen_ragged else 0
    if ragged or gen_ragged:
        print(f"\n{ragged + gen_ragged} ragged table(s). Run: "
              f"python scripts/check_tables.py --fix", file=sys.stderr)
        return 1
    print(f"{checked} file(s) OK — all Markdown tables aligned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
