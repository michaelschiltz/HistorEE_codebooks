#!/usr/bin/env python3
"""Page-count audit of an OCR or transcription run. Local only: the PDFs and the
run folders live in Zotero and in ~/ocr, not in this repository, so CI cannot
see them. The summary line it prints is what goes into the error-rate register
(logbook/4-appendix-error-rates.csv, measure `pages-empty` or `pages-missing`).

A run that prints DONE can have dropped pages: a page the engine returned
nothing for, a page the batch never reached, a file written empty after a
rate limit. The log does not show it; a count against the page range does.

Two modes.

  --pdf FILE        Text layer of a PDF. Counts the words pdftotext finds on
                    every page and reports the pages under --min-words.
                    A blank or plate page is legitimately empty; list the pages
                    you expect to be empty with --expect-empty and they are
                    reported separately.

  --dir FOLDER      Per-page output files of a run (e.g. ~/ocr/yam_texts with
                    p-001.txt ... p-155.txt). Given --pattern and --pages, reports
                    the pages whose file is missing and the files under
                    --min-words.

This checks presence, not correctness. Ink on the page that no word covers --
a dropped line tail, a lost block -- needs the image comparison of
records/SCRIPTS-venetian-ocr-2026-11-05/cover.py.

Usage:
  python scripts/audit_text_layer.py --pdf madurell.pdf --pages 22-459 --min-words 20
  python scripts/audit_text_layer.py --dir ~/ocr/yam_texts --pattern 'p-{:03d}.txt' --pages 1-155
Exit:   1 if any page fails, else 0. Needs poppler (pdftotext, pdfinfo) for --pdf.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path


def page_set(spec):
    out = set()
    for part in (spec or "").split(","):
        part = part.strip()
        if not part:
            continue
        a, _, b = part.partition("-")
        out |= set(range(int(a), int(b or a) + 1))
    return out


def n_pages(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))


def words_on_page(pdf, p):
    txt = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    return len(txt.split())


def audit_pdf(a):
    total = n_pages(a.pdf)
    pages = page_set(a.pages) or set(range(1, total + 1))
    beyond = sorted(p for p in pages if p > total)
    expect = page_set(a.expect_empty)
    low, expected_low = [], []
    for p in sorted(x for x in pages if x <= total):
        w = words_on_page(a.pdf, p)
        if w < a.min_words:
            (expected_low if p in expect else low).append((p, w))
    print(f"{a.pdf.name}: {total} pages in file; {len(pages)} audited; "
          f"{len(low)} under {a.min_words} words; {len(expected_low)} expected empty; {len(beyond)} beyond the file")
    for p, w in low:
        print(f"  page {p}: {w} words")
    if beyond:
        print(f"  pages requested beyond the file: {beyond[:10]}")
    return 1 if (low or beyond) else 0


def audit_dir(a):
    pages = page_set(a.pages)
    if not pages:
        sys.exit("--dir needs --pages")
    missing, low = [], []
    for p in sorted(pages):
        f = a.dir / a.pattern.format(p)
        if not f.exists():
            missing.append(p)
            continue
        w = len(f.read_text(encoding="utf-8", errors="replace").split())
        if w < a.min_words:
            low.append((p, w))
    stray = sorted({f.name for f in a.dir.iterdir() if f.is_file()} - {a.pattern.format(p) for p in pages})
    print(f"{a.dir}: {len(pages)} pages expected; {len(missing)} missing; {len(low)} under {a.min_words} words; "
          f"{len(stray)} files outside the range")
    if missing:
        print(f"  missing: {missing[:20]}{' …' if len(missing) > 20 else ''}")
    for p, w in low:
        print(f"  page {p}: {w} words")
    return 1 if (missing or low) else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pdf", type=Path)
    g.add_argument("--dir", type=Path)
    ap.add_argument("--pages", help="e.g. 1-155 or 22-459,470")
    ap.add_argument("--pattern", default="p-{:03d}.txt", help="file name per page, Python format")
    ap.add_argument("--min-words", type=int, default=1)
    ap.add_argument("--expect-empty", help="pages expected to carry no text (plates, blanks)")
    a = ap.parse_args()
    return audit_pdf(a) if a.pdf else audit_dir(a)


if __name__ == "__main__":
    sys.exit(main())
