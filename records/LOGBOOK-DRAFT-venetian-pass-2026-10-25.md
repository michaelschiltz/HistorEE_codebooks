# LOGBOOK DRAFT — venetian-pass-2026-10-25

Two entries, for the top of logbook 4 (tests and results) and logbook 5 (sources). Draft only: `agreement`, `value_at_recoding` and the scoring against the operator's withheld predictions are for application, and are not computed here.

---

**For logbook 4:**

## 2026-10-25 — ai — Venetian blind pass: 14 cells of `societas_maris` and `commenda_alloc` re-coded from the 865 acts of Morozzo della Rocca & Lombardo (1940)

Blind re-coding (`condition = blind`) by `claude-opus-5-5` at effort `high`, in a fresh chat inside the bundle `~/GitHub/_blind-venetian-pass-2026-10-25`, from the Latin of the edition's 865 acts with the editors' apparatus removed. The priors (`PRIORS-venetian-pass-filled-2026-10-25.md`, sha256 `2733d8a01768e66f583d3c25b4a72100f0b96315c903f85178fff156cfe91b72`) were committed and pushed before any source was opened. The commit id and ledger entry were not given to the coding chat; insert them here.

Method:

- A type census of all 865 acts by dispositive formula and the terms each act uses.
- Strata: 170 profit-share acknowledgments (A); 83 releases of such contracts (R); 1 agency act (B).
- Systematic samples of 60 each from A and R, `random.seed(20261025)`; B taken whole.
- Instance coding of 121 acts, with every parsed clause quoted verbatim, and a form-level summary per cell.

Frequencies count distinct contracts and describe the printed selection, not Venetian practice.

| recoding_id | record_id | type_id          | char_id | value            | confidence | n  | modal share | agreement |
| ----------- | --------- | ---------------- | ------- | ---------------- | ---------- | -- | ----------- | --------- |
| OF-R0253    | OF-0290   | `societas_maris` | `CF1`   | P                | medium     | 30 | 100%        | pending   |
| OF-R0254    | OF-0292   | `societas_maris` | `CF3`   | bilateral        | high       | 31 | 97%         | pending   |
| OF-R0255    | OF-0566   | `societas_maris` | `CI1`   | common           | medium     | 30 | 100%        | pending   |
| OF-R0256    | OF-0293   | `societas_maris` | `LR6`   | symmetric        | medium     | 4  | 100%        | pending   |
| OF-R0257    | OF-0283   | `societas_maris` | `TS2`   | single-venture   | medium     | 26 | 88%         | pending   |
| LM-R0080    | LM-0527   | `commenda_alloc` | `MC1`   | allocation       | high       | 56 | 100%        | pending   |
| LM-R0081    | LM-0533   | `commenda_alloc` | `PR1`   | 0                | medium     | 56 | 100%        | pending   |
| LM-R0082    | LM-0529   | `commenda_alloc` | `RB1`   | capital-provider | high       | 56 | 100%        | pending   |
| LM-R0083    | LM-0556   | `societas_maris` | `MB3`   | voluntary        | low        | 4  | 100%        | pending   |
| LM-R0084    | LM-0555   | `societas_maris` | `MC1`   | allocation       | medium     | 6  | 100%        | pending   |
| LM-R0085    | LM-0561   | `societas_maris` | `PR1`   | 0                | medium     | 4  | 100%        | pending   |
| LM-R0086    | LM-0557   | `societas_maris` | `RB1`   | shared           | high       | 6  | 100%        | pending   |
| LM-R0087    | LM-0558   | `societas_maris` | `RB2`   | .NR              | .NR        | 0  | —           | pending   |
| LM-R0088    | LM-0560   | `societas_maris` | `RB4`   | 1                | medium     | 5  | 80%         | pending   |

What the pass found that the cells do not show:

- **A change c.1200.** The bilateral shape (traveller contributes a third, profit by halves, mutual discharge on total loss) holds in 26 of the 28 distinct 12th-century contracts whose recitals state both contributions. From 1200 the printed acknowledgments are unilateral: 52 of 53 sampled, 48 of them three-quarters to the investor, at the investor's peril.
- **Recommendation: a phase split** of the `societas_maris` and `commenda_alloc` rows, put to MS; not repaired here. Non-blind on dating: the `societas_maris` period field, read before coding, states the same end date.
- The word *collegantia* nearly drops out of the acknowledgments after 1200: 3 of 150, against 13 of 20 before.
- Fixed-return finance outnumbers profit-share contracts among the printed 12th-century acknowledgments (56 against 20); in the 13th century, profit-share contracts outnumber it (150 against 31).

Problems flagged, not repaired:

- `LR6` depends on `LR2`, which is not in the bundle.
- `CF1 = P` and the form assignment rest on one clause.
- `RB1`, `RB4`, `MC1` and `LR6` for `societas_maris` are read from one clause.
- `CF3`'s "bilateral" collides with the type name's.
- No. 207 entered stratum R in breach of the stratum's own rule.

Weakest values: `MB3 = voluntary` (low, analyst-imposed; `.NR` recommended as the alternative) and the `.NR` of `RB2`.

Checks: `frictionless validate` on scratch copies of both `recodings` resources, with the foreign key removed: both `VALID`. A hand sweep of values against `allowed_values` and of `.NR` propagation: clean. All 1,436 instance-table quotations checked against the source: 0 failures. Record: `proposed-of/NOTES-venetian-pass-coding-2026-10-25.md` and the census and instance CSVs. Cite them from `records/` once copied there, not from `proposed-of/`.

---

**For logbook 5:**

## 2026-10-25 — ai — Source for the Venetian blind pass: Morozzo della Rocca & Lombardo 1940, Latin of acts 1-865 (OCR, apparatus removed)

The coding chat was given one file, `sources/morozzo-lombardo-1940_acts-1-865_latin.txt`, which the operator extracted from the OCR text layer of the BEIC reproduction (2026-10-24, pdftotext 22.02) and stripped of the editors' regests, archival lines, notes, introductions and indexes. Its header states that it is outside the deposit's CC BY 4.0 grant.

Measured in the chat:

- The 865 acts are complete (1-865, no gaps); vol. II begins at act 467.
- OCR damage is common in dating clauses and names. Twenty acts state no year, or have a lost or garbled dating clause, and 34 have no readable place.
- Quotations carry act number and printed page and are verbatim as the OCR gives them, so they should be checked against the page images at adjudication. Priority clauses: nos. 19, 141, 238, 377, 801, and the bracketed restorations in no. 769.

No page images, PDF or apparatus were available. Year and place in the type census are as stated, unconverted.
