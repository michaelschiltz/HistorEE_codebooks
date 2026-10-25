# Rulings in the clearance of the pending recodings queue (2026-10-25)

**Status: ruled by MS in chat on 2026-10-25, each on a recommendation put by the assistant (`claude-opus-5-5`, effort `high`) and accepted as proposed. Recorded here by the assistant. Pass slug `queue-clearance-2026-10-25`; open, not blind. No source was re-read for ruling 1, which rules on the rows as they stand; the sources read for rulings 2–5 are listed before ruling 2.**

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

## Tranche 2 — how it divides

Ruled in three parts, as recommended: (a) the 3 `commenda_alloc` and 11 `societas_maris` cells (6 in `loss_mitigation_forms`, 5 in `organizational_forms`; 32 rows) where the commenda arms differ from the live confidence are carried into the Venetian pass, which re-rules those cells with the Venetian half of the evidence, and their rows stay `pending` until then (the count was given in chat as 3 and 8; the script count is 3 and 11); (b) `commenda` `LR2`, `CF3` and `LR6`, rulings 2–4 below; (c) the 9 mutual-pole cells where the re-code is one step lower each time, to be read at the pages with Tranche 3.

**Sources read for rulings 2–5, on the page images through the Zotero connector on MS's machine:** *Il cartolare di Giovanni Scriba* I (`QTEG4PM7`, file `DHLLKXEI`), pp. 39 (LXXII, LXXIII), 48 (LXXXIX), 184–185 (CCCLIII–CCCLVI); *Guglielmo Cassinese* I (`G4TIJ2FM`, file `HFIT7SSW`), pp. 19 (41), 52 (124–126); Blancard I (`HF8ME3N7`, file `KAZIK3NZ`), pp. 274 (Amalric 27–29), 316 (Amalric 123–126); and, in the text layer, van Doosselaere 2009 (`V4S222VJ`, file `RHJHE7WQ`), 65–68 (printed = PDF − 18). Scriba's offset is not the logbook's: printed p. 39 = PDF 104 (− 65), p. 48 = PDF 113, p. 185 = PDF 254 (− 69).

## 2. `commenda LR2 = coupled` (OF-0081) — re-based, `medium` → `high`

New row `OF-R0245` **replaced**: `coupled`, `high`, `articulated`, `la`. The working party takes an agreed share of profit in terms — Scriba LXXII (1156, p. 39), *proficui quod in eis Deus dederit quartam habere debet*; Cassinese 41 (1191, p. 19), *ad terciam proficui*; Cassinese 125 (1191, p. 52), *ad quartam proficui*; Amalric 29 and 125 (Blancard I, 274, 316), *ad quartam partem lucri* — and van Doosselaere 2009, 66–67 finds only a handful of 4,860 commenda ties of 1154–1265 departing from the fixed quarter. Arm P: coupled in 52 of 59 speaking acts. The previous `source_ref` was `[verify]`. Arm rows `OF-R0068`, `OF-R0110`, `OF-R0152` **kept**. The gratuitous minority is handled by ruling 5.

## 3. `commenda CF3 = bilateral` (OF-0087) — re-based, `medium` → `high`

New row `OF-R0246` **replaced**: `bilateral`, `high`, `articulated`, `la`. One investor in the modal act (Scriba LXXII; Cassinese 41; Amalric 29, 125); arm P 96 of 130 (Scriba 10 of 10, Cassinese 38 of 60, Amalric 48 of 60); van Doosselaere 2009, 70 n. 11, 2,705 single- against 504 multiple-investor commendas, 1210–1300. Multilateral is variation across instances, recorded by count (Cassinese 125, two investors *de societate quam habent insimul*; Cassinese 22 of 60). `CF3` is nominal, so no `P`. **Objection put and answered:** Cassinese's 37% multilateral is a minority in every notary and in van Doosselaere's later sample, so the modal value is not in doubt, which is what `medium` would have to express. The previous `source_ref` was `[verify]`. Arm rows `OF-R0116`, `OF-R0158` **kept** (the secondary arm's `OF-R0074` was kept in ruling 1).

## 4. `commenda LR6 = upside-only` (OF-0090) — re-based, `high` → `medium`

New row `OF-R0247` **replaced**: `upside-only`, `medium`, `analyst-imposed`, `la`. Basis: van Doosselaere 2009, 65 (the investor "bore all liability for loss", the traveller "bore no capital risk") and 68 (his loss "was limited to the value of his labor"); Amalric 29 and 125, where *ad fortunam Dei et usum maris et tuum resegum* stands with *ad quartam partem lucri* in one act; Amalric 364 and 931 as read by arm P, not re-read. The previous `source_ref`, "Harris 2020", carried no page and was never verified. **Grounds for `medium`:** (i) `LR6` shares the `agent-loss-exposure` group with `CF2`; upside-only is `CF2 = 0` plus a share of profit, so it cannot be more certain than `commenda CF2 = 0` at `medium` (OF-0086); (ii) the direction is stated in terms only at Marseille, and in the Genoese acts sampled the peril is unstated, a question of default law (ruling 1 of 2026-10-07). `analyst-imposed`: no act states the direction; it is composed from two clauses. Variant symmetric: Scriba CCCLV (14 February 1158, p. 185), *Capitale tuum super me salvum erit*, profit halved — drafted *in societatem*, a commenda by structure (ruling 9 of 2026-10-12). Arm rows `OF-R0117`, `OF-R0159` **kept** (the secondary arm's `OF-R0075` was kept in ruling 1; its `high` is not adopted).

## 5. Scope: the gratuitous commenda is outside `commenda`

Ruling 13 of 2026-10-12 assigns acts to `commenda` by structure: the working party trades capital he did not contribute *for a share of profit*. **A gratuitous commenda — no share of profit to the working party (*gratis*; *capitale et proficuum tuum*, Scriba LXXXIX, 30 June 1156, p. 48) — fails that structure and is outside the row.** It is recorded in the cells' notes as a neighbouring arrangement, not as a variant. Van Doosselaere 2009, 67 n. 8 counts it among the rare exceptions to the standard payout (*gratis et amore*, perhaps an exchange of favour). Arm P's seven: Scriba LXXXIX, CCLXXXVII, DCCXLVII; Cassinese 383, 500, 750, 1087. Recorded in the `commenda` type row (`vocabularies/organizational_form_type.csv`, `key_source`).

**Consequence, carried:** `commenda CF2 = 0` (OF-0086) cites four Scriba acts, and two of them are gratuitous — LXXXIX (*Hoc debeo portare ad tuum resicum … capitale et proficuum tuum*) and CCLXXXVII (*quicquid enim sunt vel erunt tibi esse debent*). The cell is to be re-pointed to the acts that remain (Scriba CV, CXVIII; Amalric 29, 125, 364). The value is not expected to move.

## Carried

- **Tranche 2(a)** — 14 cells, 32 rows, into the Venetian pass (above).
- **Tranche 2(c) and Tranche 3** — 9 cells (9 rows) and 11 rows, one sitting, from the pages.
- **`commenda CF2` re-pointing** (ruling 5).
- **`CF3`'s definition says "number of principals", but the cells apply it to the number of parties.** One investor and one working party is `bilateral` on `qirad` and `mudaraba` ("two parties in the base case"), on `comanda` (an investor bound to one commendatary) and now on `commenda`; the `isqa` and `societas_maris` notes say "two principals". On the definition's words a single-investor commenda has one principal. A wording question for the vocabulary, not ruled here.
- **Tranche 3, order and definitions.** Item by item from the cited pages, with Tranche 2(c), in the order of the mutual-pole worksheet. Three were coded before a definition changed and are read under the current one: `MG2` (OF-R0055; clarified 2026-10-11, ruling 3), `LR4` (OF-R0019; clarified 2026-10-12, D3) and `LR5` (OF-R0020; exists only if `LR4` is not `0`).
