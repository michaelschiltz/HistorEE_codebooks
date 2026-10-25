# Rulings in the clearance of the pending recodings queue (2026-10-25)

**Status: ruled by MS in chat on 2026-10-25, each on a recommendation put by the assistant (`claude-opus-5-5`, effort `high`). Recorded here by the assistant. Pass slug `queue-clearance-2026-10-25`; open, not blind. No source was re-read for ruling 1; it rules on the rows as they stand.**

## The queue as found

At HEAD `82e6724`, 157 rows in the two `recodings.csv` files carried `adjudication = pending`: 36 in `loss_mitigation_forms`, 121 in `organizational_forms`. They come from three passes, none of them younger than 2026-09-28:

| pass                                   | `loss_mitigation_forms` | `organizational_forms` | rows |
|----------------------------------------|-------------------------|------------------------|------|
| `opus55-recode-mutual-pole-2026-09-26` | 0                       | 64                     | 64   |
| `commenda-primary-2026-09-28`          | 24                      | 38                     | 62   |
| `commenda-secondary-2026-09-28`        | 12                      | 19                     | 31   |
| all                                    | 36                      | 121                    | 157  |

No live cell under any of the 157 has been rewritten since the row was entered: no later `replaced` or `overruled` recoding sits on the same `record_id`. The two adjudication worksheets in `proposed-of/` (`ADJUDICATION-opus55-recode-mutual-pole-2026-09-26.md`, `ADJUDICATION-commenda-pilot-2026-09-28.md`) listed only the value disagreements; the rows left pending are, with eleven exceptions, the agreements those worksheets did not list.

Split by script against the live `data.csv`, into three tranches:

- **Tranche 1 — 98 rows.** `agreement = agree`, and the recoding's `confidence` equals the live cell's. 12 in `loss_mitigation_forms`, 86 in `organizational_forms`.
- **Tranche 2 — 48 rows on 26 cells.** `agree`, but the confidence differs.
- **Tranche 3 — 11 rows.** `disagree`, all from the mutual-pole pass (`avariz_vakfi` 7, `bruderschaft_salzburg` 4): the eleven entries of the mutual-pole worksheet.

## 1. Tranche 1 — the 98 agreeing rows are `kept`

`adjudication` `pending` → `kept`, `adjudicated_by` `none` → `MS`, on these rows and on no other field:

- `loss_mitigation_forms` (12): LM-R0001, LM-R0008, LM-R0018, LM-R0019, LM-R0027, LM-R0031, LM-R0037, LM-R0038, LM-R0046, LM-R0050, LM-R0056, LM-R0057. Commenda primary arm: `societas_maris` 6, `commenda_alloc` 2; secondary arm: `societas_maris` 2, `commenda_alloc` 2.
- `organizational_forms` (86): OF-R0001, OF-R0004–R0009, OF-R0011, OF-R0012, OF-R0014–R0016, OF-R0018, OF-R0021, OF-R0023–R0025, OF-R0027, OF-R0029, OF-R0031–R0033, OF-R0035–R0042, OF-R0044, OF-R0046–R0050, OF-R0053, OF-R0054, OF-R0057, OF-R0059, OF-R0061–R0065, OF-R0072, OF-R0074–R0076, OF-R0079, OF-R0086, OF-R0091, OF-R0092, OF-R0095, OF-R0096, OF-R0101–R0103, OF-R0105–R0107, OF-R0114, OF-R0121, OF-R0125, OF-R0127, OF-R0133, OF-R0134, OF-R0137, OF-R0138, OF-R0143, OF-R0144, OF-R0147–R0149, OF-R0156, OF-R0163, OF-R0167, OF-R0169, OF-R0175, OF-R0176, OF-R0179, OF-R0180, OF-R0185, OF-R0186, OF-R0189, OF-R0190. Mutual-pole pass: `bruderschaft_salzburg` 23, `avariz_vakfi` 21; commenda primary arm: `societas_maris` 14, `commenda` 12; secondary arm: `commenda` 8, `societas_maris` 8.

`data.csv` is unchanged: `kept` means the live value stands, and the live cell's `source_ref`, `confidence` and `articulation` stand with it.

**What these agreements are worth, which the ruling does not raise:**

- **Commenda primary arm.** The sampled acts carry the live value. But the live `societas_maris` and `commenda` cells rest on van Doosselaere 2009, whose dataset is built from the same Genoese cartularies, so primary and live are one evidence base and their agreement is one witness, not two (worksheet, "What the rows cannot tell you"). The effective n is the number of notaries: Scriba and Cassinese in Genoa, Amalric in Marseille.
- **Commenda secondary arm.** It re-read the literature the live cells were coded from. Its agreement shows the coding reproduces; it does not show the coding is right.
- **Mutual-pole pass.** Both coders are Claude models (`claude-opus-5` live, `claude-opus-5-5` re-code), so agreement is weak evidence of reliability; and the re-code's filled priors were not committed before coding (worksheet, third paragraph).

**Correction of the recommendation as put in chat.** The assistant described the primary-arm agreements as confirming the values on the Genoese and Marseille acts. That overstated them, for the reason in the first bullet. The ruling does not depend on it: `kept` follows from value equality alone.

**Left open by this ruling:**

- **The mutual-pole worksheet's definitional questions 3 and 4** — `AP4` with plural, cumulative founders, and `MG4` religious against customary. Their cells are among the 98 (OF-R0007 `avariz_vakfi AP4 = 1`; OF-R0025 and OF-R0057, `MG4 = religious` on both forms), and agreeing on a value answers neither question. Questions 1 (`LR4` and a spiritual hazard) and 2 (`CF1` on waqf-type forms) sit on Tranche 2 cells.
- **Articulation.** 31 of the 98 rows differ from the live cell in `articulation` (11 mutual-pole, 12 commenda primary, 8 commenda secondary); in the mutual-pole rows the re-code says `analyst-imposed` each time. Not adjudicated here.
- **Re-basing.** Where a primary-arm row supplies an act-level basis for a cell whose live `source_ref` is secondary, moving the cell onto it is a separate, cell-by-cell decision, made by a new recoding row as in the rulings of 2026-10-12.

## Carried

- **Tranche 2 (48 rows, 26 cells).** To be ruled in three parts, as recommended: (a) the 3 `commenda_alloc` and 8 `societas_maris` cells where the commenda arms put confidence below the live `high` are carried into the Venetian pass, which re-rules those cells with the Venetian half of the evidence; (b) `commenda` OF-0081 (`LR2`) and OF-0087 (`CF3`), whose live `source_ref` is `[verify]`, to be re-based on the primary arm, and OF-0090 (`LR6`) to be read at the acts; (c) the 9 mutual-pole cells where the re-code is one step lower each time, to be read at the pages.
- **Tranche 3 (11 rows).** Item by item from the cited pages, with Tranche 2(c), in the order of the mutual-pole worksheet. Three were coded before a definition changed and are read under the current one: `MG2` (OF-R0055; clarified 2026-10-11, ruling 3), `LR4` (OF-R0019; clarified 2026-10-12, D3) and `LR5` (OF-R0020; exists only if `LR4` is not `0`).
