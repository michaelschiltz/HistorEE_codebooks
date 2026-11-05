# Scripts of the Venetian OCR check, 2026-11-05

Run in the assistant's workspace against `o1.pdf`/`o2.pdf` (the 2026-10-24 files, `_pre-OCR originals/2026-10-24 layer/`, SHA-256 `a35ba9e4…`, `a0e30104…`) and `v1.pdf`/`v2.pdf` (the attachments as of 2026-11-05, `e1664697…`, `90f9c137…`). Recorded as run; see `records/CORRECTIONS-venetian-ocr-2026-11-05-ii.md`.

- `cover.py`: per page, finds text lines in the 150 dpi rendering of the scan and flags ink not covered by any word box of the text layer (letter gaps bridged, runs of 25 px or more). Checked against a page with words deleted by hand (flagged) before use.
- `runcov.py`: runs `cover.py` over every page of the 121 instance acts (`acts.json`), for one layer.
- `dropped.py`: for each flag, takes the words of the 2026-11-03 layer under the uncovered ink and assigns the act.
- `lost_words.py`: separates words truly missing from the old layer from words present elsewhere on the page; also tests the bundle text.
- `incised_check.py`: census `incised_flag` against the 2026-11-03 layer.
- `loc.py`: locates a quotation on its page and crops the image lines, for reading.
