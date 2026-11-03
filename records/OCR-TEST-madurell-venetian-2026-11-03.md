# OCR test: text layers against best-model Tesseract, Madurell 1973 and Morozzo della Rocca & Lombardo 1940 (2026-11-03)

**Run by the assistant (`claude-opus-5-5`) on 2026-11-03 at MS's request. No data change.** The test asks two questions. How good are the text layers the comanda and Venetian passes coded from? And does re-running OCR with Tesseract's best models help?

It also corrects an attribution made the same day, in `records/CORRECTIONS-madurell-translation-2026-11-03.md` (§ "Field corrections in `instances`", amounts) and in logbook 5. Those blamed the wrong amounts of 2026-10-27 on the text layer. They were not the layer's.

## What was compared

**The layers.** Both PDFs carry a layer made by OCRmyPDF 17.13.0:

- Madurell (Zotero `QQ427RZ4`): Tesseract 5.5.3, created 2026-10-27 04:45Z, before the comanda pass. Scans are 400 ppi, 1-bit.
- Morozzo della Rocca & Lombardo vol. I (`HMZ7K7BQ`): Tesseract 5.3.4, OCR of 2026-10-24. Scans are 150 ppi JPEG, from the BEIC reproduction.

The layer was read with `pdftotext` in default mode.

**The re-runs.** Tesseract 4.1.1 on the device VM was run on 300–400 dpi greyscale renderings (`pdftoppm`), with `--oem 1 --psm 6`, using MS's models:

- `tessdata_fast` `lat` (Homebrew `tesseract-lang` 4.1.0);
- `tessdata_best` `lat`, `lat+spa` (Madurell) or `lat+ita` (Venetian), and the `Latin` script model.

**The references.**
- Madurell: the image-based transcriptions of the translation test (Google Docs L05, L10, L13, L19), for PDF pages 188, 243, 269 and 328 (printed pp. 189, 244, 270, 329). The regests and archival lines are excluded.
- Venetian: PDF page 120 (printed p. 87), transcribed for this test from the page image. The image is 150 ppi, and one reading (*colla* or *colta*) is uncertain.

**The measure.** Word recall against the reference, after lowercasing, stripping punctuation and joining line-end hyphens. It counts reference words found in sequence. It ignores insertions, so text the reference excludes (regests, apparatus) does not count against an engine. Scripts and reference text are in `proposed-of/ocr-test-2026-11-03/` (untracked: the reference is the edition's text).

## Results

**Madurell 1973, word recall:**

| PDF page (printed) | ref. words | layer | fast `lat` | best `lat` | best `lat+spa` | best `Latin` |
|---|---|---|---|---|---|---|
| 188 (189) | 336 | 97.0 | 95.2 | 94.9 | 95.2 | 96.7 |
| 243 (244) | 299 | **81.6** | 97.0 | 97.0 | 97.7 | 98.3 |
| 269 (270) | 338 | 95.6 | 97.0 | 97.0 | 97.9 | 97.6 |
| 328 (329) | 310 | 92.3 | 97.4 | 97.4 | 97.7 | 98.4 |

- **Number words were present in the layer on all four pages** (20 of 20). The only number word any engine lost was a re-run's: *sep-/tuaginta* on p. 189, broken by a stray mark at the line end.
- **The layer's losses are structural.** Line tails are dropped (p. 329: *personaliter bona etc.*, *minoris etatis tantum*, a witness's name), and on p. 244 a whole 40-word block is lost. That block is doc 110's quarter-share and **risk clause** (*preterea predicta comanda vestra sit ubique ad voluntatem Dei et ad vestri risicum, periculum et fortunam, prout Dominus Deus salvaverit*). A clause missing from a layer is not missing from the act.
- **Fast and best `lat` scored the same here.** The `Latin` script model was best or within half a point on every page.

**Morozzo della Rocca & Lombardo 1940, vol. I, PDF 120 (p. 87), 362 reference words:**

| layer | fast `lat` | best `lat` | best `lat+ita` | best `Latin` |
|---|---|---|---|---|
| 89.0 | 90.1 | 90.9 | 91.4 | **94.8** |

- **The 150 ppi scan is the constraint.** *t*/*l*, *c*/*e* and *et*/*el* confusions dominate every engine (*nepoie*, *quielus*, *suprascriplis*, *lestis*).
- **The layer and a best-model re-run are not independent.** On this page they share 23 wrong words of 362 (*ego*, *tuus*, *toto*, *nepote*, *quietus*, *promitto*, *notarius*, *complevi* among them). Comparing the two flags 27 errors that only one engine made. It cannot flag the 23 that both made, because both are Tesseract.

## The amounts of 2026-10-27: an extraction error, not an OCR error

The comanda pass's coding chat read one file: `sources/madurell-garcia-sanz-1973_docs-1-255_acts.txt`, built by the operator from the layer with `pdftotext -layout` (in `~/GitHub/_work-comanda-primary-2026-10-27/`, untracked).

- **The full amount is in that file in place for 54 of the 56 amounts corrected on 2026-11-03.** The other two:
  - doc 15: the number words are present but displaced by interleaved lines (*trecentas et implicatas in quatuor libras*);
  - doc 90: *quingentas* is followed by OCR debris (*quingentas PP ere v sani libras*).
- **The 54 share one pattern.** The value recorded is the true amount less its leading number words: *una libras* for *octingentas quinquaginta una libras*, *sexaginta libras* for *trecentas sexaginta libras*, *septingentas libras* for *duas mille septingentas libras*. That is the signature of a field extraction that kept only the number word next to the unit.
- **The date lines are there too.** At least 52 of the 58 head date lines filled on 2026-11-03 are in the same file in place; the other six were not matched by a crude normalisation, not shown absent.
- **So the 2026-11-03 statements that the layer "dropped leading number words at line breaks" are wrong.** They appear in the CORRECTIONS note's amount heading, in logbook 5 (2026-11-03 and (ii)), in CONTRIBUTING §3 as first written, and in two vault notes. The amounts themselves are correct, read from the images. What is wrong is the cause given. The logbooks, CONTRIBUTING and the vault notes are corrected in place; the CORRECTIONS note is a verbatim record and stands with this file beside it.

## What follows

1. **Before blaming the OCR, check the text the field was filled from.** A wrong verbatim field is as likely an extraction error as a recognition error, and only the source text tells them apart.
2. **A Tesseract re-run is a second opinion from the same school, not an independent witness.** Use disagreement between two runs to flag a line for the image. Never use agreement to clear one.
3. **For these editions, the `Latin` script model from `tessdata_best`, on a 300–400 dpi rendering, is the best of the engines tried.** On the Venetian page it roughly halves the layer's word error (11.0 % → 5.2 %). On the Madurell pages it recovers the blocks the layer dropped.
4. **Recommended:** re-OCR both Venetian volumes with that model before any further coding from them, and the Madurell volume too, for its dropped blocks. Keep the old layers for comparison. Five pages is a small sample; the next comparison should be on a seeded random draw of pages.
