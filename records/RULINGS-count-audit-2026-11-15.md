# Rulings: the count audit's first run (2026-11-15)

**Status: ruled by MS in chat on 2026-11-15.** The first run of `scripts/check_counts.py` raised two questions, put to him with the assistant's recommendations. He ruled: "Absolutely, recommendations accepted." No `data.csv`, `recodings.csv` or record values change.

## Ruling 1: a `neither` instance may carry no coded row

**The question.** The comanda pass (`records/instances-2026-11-03.csv`, `records/instance-chars-2026-11-03.csv`) leaves 23 instances assigned to `neither` without a coded row, while 10 others assigned to `neither` carry one. The Venetian pass codes its `neither` releases on CF3 and TS2 from their recitals.

**The finding behind the recommendation.** The difference follows the coders' common rule, a row wherever the act bears on a characteristic, applied to different sample designs.

- The 10 with rows each evidence one thing: CF2 `.NR` on the four custom-only *notule* (docs 75, 78, 81, 84), LP3 on the protest (186), TS4 on the collective act of some sixty investors (193), CI3 on the cession (253), VF1 on the carriage chapters (255); doc 105 is a full contract moved to `neither` on 2026-11-03 (D105) and keeps its ten rows.
- The 23 without rows are deposits, a sailing licence, quittances, receipts, a procuration and an exchange acknowledgment: none evidences a characteristic of a placement of capital.
- All 118 instance rows of 2026-11-03 are complete: every field holds a value, `.NR` or `n/a`, none is blank. The 23 were read; "no row" does not stand for "not reached".
- The Venetian pass sampled releases as a stratum (R) on purpose, as evidence of the colleganza's terms, and so coded their recitals. The comanda pass took its 15 non-contract acts to check the census assignment, not as evidence of terms.

**Ruled.** An instance may carry no coded row if, and only if, it is assigned to `neither` and its instance row has no blank field. `check_counts.py` enforces this (C3) for every pass; VP26-R-207, the Venetian frame defect recorded in `records/NOTES-venetian-pass-coding-2026-10-25.md`, falls under the same rule.

**Declined.** Backfilling the comanda quittances (docs 21, 88, 94, 111, 234; the five *apochae* of 97) with recital rows to match the Venetian practice. Release recitals are weak evidence of terms on the Venetian pass's own count (of 166 investment-related releases, 70 abbreviate the contract they discharge and 7 mention the peril), and these instances feed no form's cells.

**Open item, recorded.** Several of these acts record outcomes, not terms: pro rata payment (88), partial restitution (94), five pro rata recoveries (97), return of capital and profit (111). They are the conduct layer, and they record losses. They do not belong in `instance-chars`, which codes contract characteristics; a separate outcome table across the comanda and Venetian passes is to be considered.

## Ruling 2: the Yamamoto OCR pilot gets a repository record

**Ruled.** The pilot of 2026-11-10 existed only as a project document, so its row in `logbook/4-appendix-error-rates.csv` pointed outside the repository. It is now `records/OCR-TEST-yamamoto-2026-11-10.md`, a verbatim copy of that document, and ER-0011 points there. The copy holds measurements, substitution pairs and single characters, not a transcription of the edition, which dates from 1989.
