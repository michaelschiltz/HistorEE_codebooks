# Venetian OCR check, second part (2026-11-05): the old layer's losses, eight incised charters, ten live quotations

**Applied by the assistant (`claude-opus-5-5`) on 2026-11-05, continuing the check of the morning at MS's instruction ("continue").** Rulings in `records/RULINGS-venetian-ocr-2026-11-05.md`. The ledger is `records/CORRECTIONS-venetian-ocr-2026-11-05-ii.csv`: 26 changes, one per field.

Successor file: `records/CORPUS-morozzo-lombardo-2026-11-05-ii.csv` (865 rows) succeeds `CORPUS-morozzo-lombardo-2026-11-05.csv`, which is untouched. The `-ii` suffix marks a second successor on the same day. The instance records do not change.

## 1. A correction to the morning's verdict

`CORRECTIONS-venetian-ocr-2026-11-05.md` says, of these editions, that "the layers drop no text silently". That is true of the 2026-11-03 layer (`Latin_best`) and **false of the 2026-10-24 layer, from which the census and the bundle were built.**

**The test.** Every page of the 121 instance acts (224 pages, 9,098 text lines) was rendered from the scan. Any run of ink that no word box of the layer covers was flagged.

- The test was checked beforehand on a page from which words had been deleted by hand; those were flagged.
- The 2026-11-03 layer raises no flag on any of the 224 pages.
- The 2026-10-24 layer raises 186.

The words under the 186 flags were recovered from the new layer and searched for in the old layer's text of the same page and in the bundle (`SCRIPTS-venetian-ocr-2026-11-05/`):

| status | spans |
|---|---|
| word fragments (fewer than 3 letters) | 11 |
| present in the old layer, misplaced or split | 112 |
| missing from the old layer | 63 |

Of the 63, about 40 are also missing from the bundle the coder read. Almost all are formulaic: invocations («Christi.», one whole invocation line in no. 538), witnesses' names, «reddidi», «misso», «consilii».

Checked against the coded fields:

- **No. 489:** «Pasce Rexur[rectionis]» is cut, but the bundle has «Pasce R rectionis». TS2 `single-venture` stands.
- **No. 834:** «viatico» is lost. TS2 and the destination field rest on other words.
- **No. 391:** «casis» is lost from «in duplo de terris et casis». `security` is `.NR` on other grounds.
- **No. 683:** «maris» is misplaced, not lost; the bundle has it.

**No coded value rests on a lost word.** The losses that matter are in the editors' archival lines (§2).

## 2. Census `incised_flag`: eight charters missed

The census's `incised_flag` was checked against the new layer for all 865 acts. Eleven disagreements were flagged. Each was read on the page image:

- **Census wrong, «Carta incisa» printed:** 247, 327, 340, 381, 706, 786, 811, 859.
  - In 381, 811 and 859 the old layer had lost the words (`LAYER-LOST`).
  - In the other five the census missed words that the layer had (`CENSUS-MISS`).
- **Census right; the script's misses:** 285 («Carta 1ncC18a» in the layer) and 489 («La pergamena è in-cisa»).
- **No. 246 is put to MS (V-246 below)**: «La parte inferiore del documento è incisa e mancante sui lati e alle estremità».

All eight now read `1`. Effect on `NOTES-morozzo-lombardo-selection-2026-10-25.md` §6.5 point 3, which is not edited:

- Incised investment contracts: 69 → **73** of 164 (706, 786, 811, 859).
- Incised releases: unchanged at 3 of 354.
- Incised acts in the edition: 109 → 117.

Three of the eight are instance acts (786, 811, 859). The instance records carry no incision field. No live cell quotes the incision counts.

## 3. Live quotations against the page images

All quotations in live `data.csv` cells that cite this edition were located on their pages and read on the image. Ten OCR forms in six cells were corrected in place, in the cell notes only. Each cell's note records its correction; the ledger lists them all.

| cell | was | now |
|---|---|---|
| LM-0533 | *parlibus* | *partibus* |
| LM-0555, LM-0557 | *maris el genlis* | *maris et gentis* |
| LM-0560 | *absil*, *eril* | *absit*, *erit* |
| OF-0290 | *el ego posui* | *et ego posui* |
| OF-0293 | *medielatem* | *medietatem* |
| LM-0555, LM-0557, OF-0293 | *debeat, Si vero* | *debeat. Si vero* |

The other quotations match the page as printed. One is cut short in the cell («…dividere»), but the print runs on «et partiri debeam»: that is a quotation boundary, not an error. No value, confidence or articulation changes.

`recodings.csv` carries the same OCR forms in its quotations. It is the record of the coding as it was made and is not edited.

## Rulings put to MS

**V-246: is act 246 incised?** The editors write «La parte inferiore del documento è incisa e mancante sui lati e alle estremità» of a testament.

**Recommendation: leave `incised_flag` at 0.** The phrase describes damage: the parchment is cut and missing on the sides and at the edges. It does not describe the cancelling cut of a discharged contract, and a testament is not cancelled on discharge. No. 489 («La pergamena è incisa con totale abrasione della parte inferiore») stays at 1: it is an investment contract with a surviving quittance, the case a cancelling cut belongs to.
