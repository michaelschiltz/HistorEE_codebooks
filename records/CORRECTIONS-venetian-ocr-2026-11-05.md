# Corrections to the Venetian primary records from an image check of years and amounts (2026-11-05)

**Applied by the assistant (`claude-opus-5-5`) on 2026-11-05 at MS's instruction (regest years checked edition-wide, then the repo's records scoped against them).** The source is the page images of Morozzo della Rocca & Lombardo 1940 (Zotero `HMZ7K7BQ`, `L4VTQIKI`), read region by region through the Zotero connector. No `data.csv` or `recodings.csv` cell changes.

The 2026-10-25 files are untouched. The corrected records are successor files:

- `records/CORPUS-morozzo-lombardo-2026-11-05.csv` (865 rows)
- `records/INSTANCES-venetian-pass-2026-11-05.csv` (121 rows)

`INSTANCE-CHARS-venetian-pass-2026-10-25.csv` needs no successor: no characteristic state changes.

**The ledger is `records/CORRECTIONS-venetian-ocr-2026-11-05.csv`: 44 changes, one row per field, with old value, new value, rule and the page read.** Files are written LF; the 2026-10-25 census is CRLF.

## What was checked

**The text the census read.** The two extracts were rebuilt from the files set aside in `ZoteroFiles/_pre-OCR originals/2026-10-24 layer/` with `pdftotext` 22.02 in default mode. Their hashes (`23befe9f…`, `9900e261…`) are those in `NOTES-morozzo-lombardo-selection-2026-10-25.md` §2, so every cause below is traced in the text the census was actually built from.

**Census `year`, all 865 acts.** Each year was compared by script with the Latin dating clause of the same act in the 2026-11-03 layer (`Latin_best`), allowing *more veneto* (January–February one year later). Acts not found on that layer (38) were checked on the old layer's Latin, segmented with the census's own `positions.json`. Every disagreement was read on the page image.

| outcome                                                                        | acts |
|--------------------------------------------------------------------------------|------|
| Latin dating clause agrees (732 on the new layer, 27 on the old)               | 759  |
| disagreement resolved, census right (*more veneto*, editors' reckoning, parser) | 28   |
| disagreement resolved, census wrong (corrected here)                           | 12   |
| no Latin parse; regest year agrees across both layers                          | 57   |
| no Latin parse; old layer only                                                 | 9    |

Of the 40 disagreements, 32 were read on the page image. Eight were settled in the text: six where the regest month is January or February (*more veneto*: nos. 102, 155, 345, 504, 599, 787), one running-head misread (no. 356) and one Latin numeral broken by a scrambled line (no. 844).

The last two rows (66 acts) rest on the regest's Arabic numerals in Tesseract output only. Two Tesseract runs agreeing does not clear a reading (`OCR-TEST-madurell-venetian-2026-11-03.md`). They are listed under "Open".

**Instance `date`, 121 rows.** Parsed from the verbatim Latin and compared with the corrected census year: no disagreement. The verbatim fields carry the old layer's OCR forms (*oclavo*), which do not affect the year.

**Instance amounts.** `capital_stans` was searched in the new layer for number words dropped before the recorded phrase. Every `capital_tractator` of the form "X of Y" (22) was checked against its `capital_stans` (Y − X = stans). Every flag was read on the image.

## Census corrections (12)

| act | census | image | cause | rule |
|-----|--------|-------|-------|------|
| 56  | 1120 | 1130 | 3 read as 2 | OCR-DIGIT |
| 58  | 1120 | 1130 | 3 read as 2 | OCR-DIGIT |
| 113 | 1255 | 1155 | default-mode extraction put the cross-reference "l'atto del 1155 ottobre" (itself misread 1255) before the regest year | OCR-ORDER |
| 122 | 1155 | 1156 | damaged 6 | OCR-DIGIT |
| 156 | 1159 | 1162 | regest's third digit damaged; Latin «sexagesimo secundo», ind. X, agrees with 1162 and with nos. 155 and 158 | OCR-DIGIT+LATIN |
| 275 | 1116 | 1176 | 7 read as 1 | OCR-DIGIT |
| 299 | 1119 | 1179 | 7 read as 1 | OCR-DIGIT |
| 302 | 1119 | 1179 | 7 read as 1 | OCR-DIGIT |
| 306 | 1119 | 1179 | 7 read as 1 | OCR-DIGIT |
| 353 | 1184 | 1185 | default-mode extraction put the endorsement's «1184, 13 fevrer» first | OCR-ORDER |
| 402 | 1188 | 1191 | the regest cites another date first («rimpatrio del novembre 1188. Rialto, 1191 ottobre») | RULE-FIRSTYEAR |
| 413 | 1191 | 1192 | default-mode extraction put the endorsement's «1191» first | OCR-ORDER |

Five acts change `period`: 113 (1230-1261 → 1150-1199); 275, 299, 302, 306 (<1150 → 1150-1199). Each corrected row carries a dated note in `image_check`.

**Effect on `NOTES-morozzo-lombardo-selection-2026-10-25.md` §6.** That file is a verbatim record and is not edited. Its tables change as follows:

- Period totals: <1150 98 → 94; 1150-1199 343 → 348; 1230-1261 217 → 216.
- §6.3: release <1150 60 → 57, 1150-1199 177 → 180; sea loan / exchange <1150 2 → 1, 1150-1199 18 → 19; mandate 1150-1199 26 → 27, 1230-1261 19 → 18.
- §6.4: S. Zaccaria <1150 86 → 82, 1150-1199 280 → 285, 1230-1261 34 → 33.
- §6.5: every share quoted is unchanged at its rounding (releases 61% and 52%; investment contracts 3% and 5%; Mairano 104 of 348, 30%; overseas 111 of 348, 32%). The twelfth-century count of 20 investment contracts against 100 investment-related releases, and the bilateral-marker and quarter-share counts by period, are unchanged: no corrected act is an investment contract, and act 302's move stays inside the twelfth century.

## Instance corrections (6)

Every one is a field-extraction error. The amount is in the source text (old layer and the bundle the coder read); the field took the wrong words. Five are releases or contracts that recite more than one sum.

| instance | act | field(s) | was | now (read on image) | rule |
|----------|-----|----------|-----|---------------------|------|
| VP26-R-141 | 141 | stans, tractator | scrambled; "sum garbled" | «libras denariorum ducentas quinquaginta»; 125 of 375 libre | FILL-IMAGE |
| VP26-R-209 | 209 | stans | «perperos» | «perperos auri veteres pensantes centum» | EXTRACT-DROP |
| VP26-A-377 | 377 | stans | the traveller's «quinquaginta» | «libras denariorum venecialium centum» | EXTRACT-CLAUSE |
| VP26-R-380 | 380 | stans | the imperial indemnity clause, number words dropped | «perperis auri veteribus pensantibus quinquaginta quinque» | EXTRACT-CLAUSE |
| VP26-R-418 | 418 | stans | the indemnity received, «duobus» dropped | «quinquaginta quinque perperis auri veteribus pensantibus» | EXTRACT-CLAUSE |
| VP26-R-459 | 459 | stans, tractator, currency | the recited loan (25 libre veronenses) | «perperis auri veteribus pensantibus quinquaginta»; 25 of 75 perperi; perperi auri veteres | EXTRACT-CLAUSE |

No form assignment changes: in all six the traveller's own stake is stated, so each stays `societas_maris`. No live cell quotes a wrong amount. LM-0557 (`recodings.csv`) already quotes no. 418's «quinquaginta quinque perperis» correctly.

## What follows

1. **The census rule "first year in the regest" needs the image where a regest cites another date or an endorsement sits beside it.** Four of the twelve errors (113, 353, 402, 413) are reading-order or rule errors, not digit errors.
2. **The amount errors repeat the 2026-10-27 signature.** A verbatim amount field in an act with several sums is the field to read on the image.
3. **The new layer is no independent witness for Arabic numerals.** It shares the old layer's digit errors at 58 and 73 and adds its own (122, 156, 213). The Latin dating clause, written in words, is the better cross-check.

## Open

- **66 census years rest on the regest's numerals only.** Two layers agree: 1, 2, 3, 4, 6, 7, 27, 32, 33, 34, 35, 52, 57, 139, 162, 198, 201, 215, 223, 225, 234, 284, 360, 431, 447, 448, 450, 451, 452, 453, 454, 488, 529, 530, 531, 532, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 552, 611, 645, 659, 660, 692, 698, 755, 758, 790. One layer only: 5, 199, 258, 390, 449, 533, 801, 807, 811. Many are early acts dated by indiction alone, or fragments.
- **Other verbatim fields of the 121 instances** (parties, places, quotations) were not re-read here.
