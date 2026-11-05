# Rulings on the Venetian OCR check (2026-11-05)

**Ruled by MS on 2026-11-05 ("Recommendation accepted").** Recorded by the assistant (`claude-opus-5-5`).

## V-156: act 156's census year is 1162

The regest of act 156 (Morozzo della Rocca & Lombardo 1940, vol. I, p. 154; PDF 187) prints «Costantinopoli, 11?9 marzo», the third digit damaged and most likely a 6. The Latin dating clause reads «millesimo centesimo sexagesimo secundo, mense marcii, inditione decima» (1162, ind. X); the endorsement «1172 marzo»; the editors print the act between nos. 155 and 158, both 1162.

**Ruling: the census year is 1162, taken from the Latin dating clause and the indiction against the regest numeral, which is read as a misprint.** The value in `records/CORPUS-morozzo-lombardo-2026-11-05.csv` stands. Its ledger rule in `records/CORRECTIONS-venetian-ocr-2026-11-05.csv` (seq 10, `OCR-DIGIT+LATIN`) is to be read as `PRINT-LATIN`; see `records/ADDENDUM-venetian-ocr-2026-11-05.md` §2. Period unchanged (1150-1199).

## V-246: pending

Put to MS on 2026-11-05 in `records/CORRECTIONS-venetian-ocr-2026-11-05-ii.md`. Recommendation: `incised_flag` stays 0.

## V-246 ruled (added 2026-11-05, after the pending entry above): act 246 is not incised

**Ruled by MS on 2026-11-05 ("recommendation accepted").** The editors' «La parte inferiore del documento è incisa e mancante sui lati e alle estremità» (vol. I, PDF 273; a testament) describes damage, not the cancelling cut of a discharged contract. `incised_flag` stays 0 in `records/CORPUS-morozzo-lombardo-2026-11-05-ii.csv`. No. 489 («La pergamena è incisa con totale abrasione della parte inferiore», an investment contract with a surviving quittance) stays 1.
