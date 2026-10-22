# references/

`works.csv` resolves every work a `source_ref` names to an item in the maintainer's Zotero library. `source_ref` itself stays a Chicago author-date short form, which is what the codebooks and views print; this file is the bridge from that short form to a record someone can open.

One row per distinct work label, written exactly as it appears in `source_ref` (`Kars 2020`, `Gelderblom, de Jong & Jonker 2010`, `Giovanni Scriba I`). Columns:

| Column       | Content                                                                     |
|--------------|-----------------------------------------------------------------------------|
| `label`      | the label as written in `source_ref`; matched as a prefix, longest first    |
| `zotero_key` | the 8-character Zotero item key of the copy actually read                   |
| `citekey`    | that item's Better BibTeX / Zotero citation key                             |
| `status`     | `resolved`, `not-in-library` (cited, no Zotero item yet) or `ambiguous`     |
| `notes`      | why this item and not another: duplicates, editions, the copy holding a PDF |

`scripts/check_citations.py` enforces it. CI runs it offline: every author-date work in a `source_ref` must have a row, and an inline `(Zotero XXXXXXXX)` key must agree with its row. Run `python scripts/check_citations.py --zotero` locally, against a read-only copy of the library, to confirm each key exists, is not in the trash, and carries the recorded citekey. Merging duplicates in Zotero changes which key survives; the local run catches a row left pointing at the merged-away key.

**A row proves that a cited work exists and which record is meant. It says nothing about whether the work supports the cell.** That is what `source_read`, the blind re-code and the primary-against-secondary arms are for.

Built 2026-10-22 from an adjudicated bootstrap (logbook 3, 2026-10-22).
