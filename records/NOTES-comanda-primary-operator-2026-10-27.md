# NOTES — comanda-primary-2026-10-27: operator brief for a blind primary pass on the Barcelona acts of Madurell Marimón & García Sanz (1973)

Written 2026-10-27 by `ai` (`claude-opus-5-5`) as operator, in the chat that OCR'd the edition. This chat has read the source and the live cells and must not code; the coding goes to a fresh chat inside `~/GitHub/_blind-comanda-primary-2026-10-27`.

## 1. Scope, as decided by MS

**There is no Barcelona row.** The census carries the Catalan comanda as four rows: `comanda` (33 cells) and `comanda_ad_societatem` (33) in `organizational_forms`, and `comanda_alloc` (10) and `comanda_ad_societatem_alloc` (10) in `loss_mitigation_forms`, all coded open on 2026-10-07 and scoped to the Crown of Aragon. The operator first told MS, before checking, that the matrix might hold "one Barcelona row"; that was wrong, and is corrected here.

**MS chose `comanda` and `comanda_alloc`: 43 cells.** The edition is a witness for the unilateral comanda and hardly for the loss-sharing one: whole-text counts give *ad societatem* 0, *societatem* 6, *sive societas* 0. The `comanda_ad_societatem` rows are not recoded; the coder records any act it assigns to them.

**A Barcelona edition coding a Crown-of-Aragon row.** Every value this pass returns is a Barcelona witness to a row whose scope includes Vic, Mallorca and Valencia. The coder's notes should say so wherever a cell's value could differ by place; the adjudication decides whether a Barcelona-only value replaces a row-wide one.

## 2. What this operator session spent

**No budget was declared before reconnaissance, which breaks the budget-first rule; recorded as such,** on the precedent of `venetian-pass-operator`. The session began as OCR work and turned into selection without stopping to budget. Reconciled after the fact:

| question                                                 | rung reached                                                                                                                              | why that rung                                                                                    |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| where the comanda sits in the matrix, and how many cells | 1 (counts) and 3 (`type_id`, `char_id`)                                                                                                   | needed to scope                                                                                  |
| what the live cells rest on                              | 3 (`source_ref`, `source_read`, `source_lang`)                                                                                            | needed for non-independence                                                                      |
| whether a blind is available at all                      | 5, on logbook 4's standing table only                                                                                                     | the 2026-10-07 row records "no blind was available"; five comanda and commenda rows read in full |
| what the bundle must scrub                               | 1 (counts of mentions), then 5 on 8 definitions                                                                                           | the redactions have to be exact                                                                  |
| the live values, for the predictions                     | 5 on values, confidence and `source_ref` of the 43 cells; **notes not read**                                                              | predictions need the values                                                                      |
| the type rows                                            | 5, all four comanda type rows in full                                                                                                     | the boundary between the rows is stated there                                                    |
| the edition                                              | 5: docs 1–4, 108 and 151's opening in full; intro pp. 120–121; all 255 editors' summaries; clause counts                                  | measurement and extraction                                                                       |
| the vault                                                | 3: `source-session` slugs, and 4: the titles of the 22 withheld notes, read by script into a file for the residual scan and not displayed | the scan needs the titles                                                                        |

**Prejudices** any later blind coding of `comanda` and `comanda_alloc` by this chat, of the Madurell–García Sanz documents named above, and any blind re-scoring of this pass by this chat. The standing-table row is in §10.

## 3. The edition measured

**Inputs.** The labelled, OCR'd PDF in Zotero (`VPX7DFWD`, attachment `QQ427RZ4`), split by script into 255 documents (printed pp. 151–378). Per-page `pdftotext -layout`; each document's heading, the editors' summary and the archival block separated by pattern; three garbled headings (docs 20, 151, 223) pinned by hand. Scripts and intermediates in `~/GitHub/_work-comanda-primary-2026-10-27/`, untracked; the coding chat is forbidden to open that folder.

**Dates.** Heading dates are OCR-unreliable in a systematic way: 3↔8 and 2↔9 (doc 1 reads 1286 for 1236; doc 10, 1960 for 1260). Years were assigned by choosing, per document, among the heading as read and its digit-confusion variants, the reading that keeps the sequence non-decreasing (the edition is chronological): 184 as read, 60 corrected, 11 bounded by their neighbours only. Corrected years can be a few years out; good for 25-year bins, not for exact dating. The bundle carries no editors' dates.

**Act types**, from the editors' summaries (the coder never sees them):

| period    | docs | comanda contracts | accounts | returns, releases | cessions, renewals | other                                  |
| --------- | ---- | ----------------- | -------- | ----------------- | ------------------ | -------------------------------------- |
| 1236–1299 | 66   | 61                | 2        | 1                 | 0                  | 2 (a partnership; a bailiff's licence) |
| 1300–1349 | 36   | 31                | 3        | 1                 | 0                  | 1 (a payment of sums advanced)         |
| 1350–1399 | 56   | 55                | 0        | 1                 | 0                  | 0                                      |
| 1400–1449 | 61   | 57                | 1        | 1                 | 0                  | 2 (a formulary; a sea exchange)        |
| 1450–1501 | 25   | 22                | 1        | 0                 | 2                  | 0                                      |
| undated   | 11   | 10                | 0        | 0                 | 0                  | 1 (an insurance contract, doc 255)     |
| total     | 255  | 236               | 7        | 4                 | 2                  | 6                                      |

Doc 20's summary is garbled and doc 179 is a comanda paid by a bill of exchange; both counted as contracts. The edition is a selection of comandas and the act types follow from that: the Venetian edition, by contrast, was 41% releases.

**Clauses in comanda contracts**, documents with at least one hit, by period (regex over OCR text; a floor, not a count):

| clause                                                                   | 1236–99 | 1300–49 | 1350–99 | 1400–49 | 1450–1501 |
| ------------------------------------------------------------------------ | ------- | ------- | ------- | ------- | --------- |
| peril or fortune (*ad fortunam*, *periculo*, *sicut Deus salvaverit*)    | 37/50   | 6/28    | 36/51   | 16/54   | 8/19      |
| a quarter of profit to the agent                                         | 40/50   | 8/28    | 24/51   | 7/54    | 0/19      |
| a third or a half of profit                                              | 2/50    | 1/28    | 3/51    | 0/54    | 1/19      |
| *in comuni* (the agent's fund)                                           | 4/50    | 5/28    | 14/51   | 5/54    | 1/19      |
| a term in years                                                          | 1/50    | 0/28    | 2/51    | 0/54    | 0/19      |
| a single voyage (*in presenti viatico*, *facto dicto viatico*, *viagio*) | 37/50   | 12/28   | 29/51   | 12/54   | 15/19     |
| *societas*, *ad societatem*                                              | 1/50    | 2/28    | 1/51    | 0/54    | 0/19      |
| oath formulae                                                            | 2/50    | 0/28    | 4/51    | 13/54   | 2/19      |
| general obligation of goods                                              | 25/50   | 3/28    | 21/51   | 2/54    | 0/19      |

The denominators here count only contracts named as comandas in the summaries; §3's table adds the 24 whose summaries omit the word.

**The archive confound.** From the archival lines: of 1236–1299, 58 of 66 documents are cathedral parchments (ACB, *Diversorum*); of 1300–1349, 11 ACB and 25 notarial registers (AHPB); from 1350, notarial registers throughout (AHPB 137, with one ACB, three AHC and one formulary). **The fall in stated clauses after 1300 runs with a change in the kind of record**, from the engrossed instrument to the register entry, whose formulae the notary cut short with *etc.* A frequency over this edition is a frequency over its record types as much as over practice. The bundle removes the archival lines, as the Venetian bundle did; prediction 8 scores whether the coder sees the confound unaided.

**Withheld from the bundle that the coder might want:** 24 editors' notes reporting marginal cancellations in the registers (docs 138–254), which bear on settlement; 7 notes that a document was previously published (Sayous and others). Both are the editors' writing, and an open pass can use them.

## 4. What the live rows rest on

`comanda`: 31 of 33 cells `source_read=partial`, 2 `.NA`; `source_ref` most often the *Llibre del Consolat de Mar* (Capmany/Font Rius 1965; 24 cells), Martínez Gijón 1966 (26), Hancock 2025 (12), with Fynn-Paul 2017, Martínez Gijón 1974, Polonio 2014 and García Sanz 1959 once or twice. `comanda_alloc`: the same base, 9 of 10 partial. **The 1973 edition is cited in at most one cell**: `OF-0847` (`CI1`) cites "Hancock 2025, 17 (citing Madurell & Garcia Sanz I, 94-96)". A volume I suggests their two-volume *Sociedades mercantiles medievales en Barcelona* (1986), not this edition **[to confirm]**. If so, the edition is cited in no live cell, and this pass is its first use as evidence.

## 5. Non-independence, declared before the rows

1. **One author twice.** A. García Sanz co-edited the 1973 edition and wrote García Sanz 1959 (*Ausa*), cited in one live `comanda` cell and in 30 of 33 `comanda_ad_societatem` cells. The 1959 documents are from Vic and the 1973 documents from Barcelona, so the acts are different witnesses. The interpretive layer they share is the editors' writing, which the bundle strips. **Agreement between this pass and a live cell resting on García Sanz 1959 is agreement between two witnesses who share an editor, not between two independent readings.**
2. **The Hancock 2025 cell** cites Madurell & García Sanz at second hand (§4). If the cited work prints documents also in the 1973 edition, `OF-0847` and this pass share an upstream on those documents **[to confirm]**.
3. **Martínez Gijón 1966** predates the edition but worked in the same archives (AHPB, ACB); overlap of documents is possible and was not checked **[to confirm]**.
4. **The mirror case.** The *Consolat de Mar* is normative and independent of the acts. Where this pass returns `.NR` on a cell the live row carries from the Consolat (`VF1`, `VF2` are the likeliest), that is **silence, not contradiction**: an act that does not say how loss is proved does not testify against a rule that does.
5. **Carrère 1975** (`5EMKJEE5`) reviews this edition and is not an independent witness to anything it supports.

## 6. Cells that are not a blind test

`comanda CF2`, `comanda_alloc RB1`, `RB2`, `RB4`: **the census split the two Catalan rows on the loss rule (2026-10-07, MS's decision)**, so an act assigned to `comanda` carries that rule by construction. The coder codes them all the same, and they are scored apart. `RB2` keeps a test of its own: whether any act separates market loss from loss to the peril. `comanda_alloc MC1`: the type name states it, as on the Venetian pass.

**A methodological consequence, stated rather than handled silently.** A characteristic used as the boundary between two rows cannot afterwards be evidence that the rows differ, and the census's comparison of `comanda` with `commenda` on `CF2` inherits this: the `comanda` side of it is a definition, not a finding. What this pass can still find is whether the Barcelona acts **contain** loss-sharing comandas at all, which is an act-level count, not a cell.

## 7. The bundle

Minimal, on the commenda-pilot and Venetian precedent: no `data.csv`, logbooks, CHANGELOG, codebooks, views, `records/` or vault. Contents and redactions are listed in its `README.md`; the build log, 18 lines, is `~/GitHub/_work-comanda-primary-2026-10-27/bundle-build.log`. In brief:

- `sources/`: 255 documents, the acts only, 571 KB, headed `=== doc N | p. P ===`; editors' dates, summaries, archival lines, introduction, glossary and indexes removed; four entries with further acts marked.
- `vocab/`: all 33 organizational characteristics (all are in scope); the loss vocabulary cut to the 10 in scope, `exemplar` dropped.
- **Redactions:** CHARACTER-CODING test 1's worked case; the `source_lang` description in both schemas (the source `ca` was added for); `AP1` (a Barcelona chapter and the comanda's recoded value); `VF1` (the first instance of `claimant-oath`, three family statements, a Consolat citation); `RB3` (the Catalan general obligation of goods); the ruling file name in `CI1`, `CI5`, `MG2`, `CF2`, `VF1`, `RB3`; the evidence parentheticals of both comanda `period` fields. Every replacement asserted to match exactly once.
- **Residual scan,** whole bundle, after every removal, for the four type codes outside the files meant to carry them, the 22 withheld vault titles, and the live row's source names: two hits, both expected. One is the Marseille example *lucrum omnium comandarum* in `LR4`, disclosed as a known leak; the other is "Ausa" inside "causal".
- **Known leaks, disclosed to the coder** (README, seven items): the type names, which state the boundary and `MC1`; the traditions and periods; related forms' values in eleven definitions (48 mentions; doctrine, and kept); `VF1`'s history; `LR4`'s Marseille example; CHARACTER-CODING test 4's class reasoning; general knowledge.
- **Skills:** `code-a-form` and `run-a-coding-batch` checked for comanda, Catalan, Barcelona, Consolat and the family's values: none.
- **Account memory,** which a chat outside the Project still receives: no comanda content (checked: profile, HistorEE and book area files). The prompt forbids memory tools and past-chat search, since this chat is findable.

**Sampling,** fixed in the README before the coder reads: census of all 255; full coding of every document whose number is divisible by 3 and every non-contract act; directed search recorded as such.

**Hashes** (sha256): `sources/madurell-garcia-sanz-1973_docs-1-255_acts.txt` `c8740e020ad0b5135262158907131ebf9a4c78e2a9079aec3685c21ccb02ef0e`; `PRIORS-TEMPLATE.md` `12138b966d8f6f14d0e7339e405ec027b0b9f42ad005fc8c060e90fa3b351acf`; `README.md` `66b8c4d8f9d9f47c5d8070ca12343c392d48d699a259c773eb10aa53173c7494`; `cells-in-scope.csv` `424126ffab446dd3777dbdaee4510bdf45f12b54fe70a5b44c4d7bb222a3026c`.

## 8. Read-back

The prompt (`records/PROMPT-comanda-primary-coding-2026-10-27.md`), the README and the priors template were read back against `PREDICTIONS-comanda-primary-operator-2026-10-27.md`, by script for any shared six-word run and then by hand. One shared run in the priors template: the boundary sentence, a design fact the coder needs and not a prediction; kept. By hand: the template's question on abbreviated entries would have primed prediction 3 and was deleted; "God's fortune" (the peril formula) and the Consolat de Mar were taken out of two questions; the README's instruction to date acts from their own clauses makes prediction 7 no test, and the predictions file says so in place; §2.2 of the template primes prediction 4, and the predictions file says so in place.

## 9. For MS, before the coding chat opens

1. **Commit order.** Commit this file, the predictions file and the prompt now, before the coding chat starts. Start the coding chat **outside** the claude.ai Project, connect only `~/GitHub/_blind-comanda-primary-2026-10-27`, paste the prompt. Commit its filled priors when it gives you the sha256; only then tell it to read.
2. **Rights.** The acts are medieval but the transcription is the editors' (Barcelona, 1973). The Venetian pass copied its source text into `records/BUNDLE-venetian-pass-2026-10-25/sources/`, which is in the public repository. **Recommendation: when the batch is applied, copy everything of this bundle into `records/` except `sources/`, and record the source file's sha256 instead.** Your decision; it may also bear on the Venetian copy.
3. **The withheld editors' notes** (24 cancellations, 7 publication notes) and the archive confound are material for an open pass after adjudication, not for this one.
4. **The operator's own exposure.** This chat holds your project memory, including the existence of the 2026-10-09 retrieval report and of the Venetian pass, and has seen pages of the editors' introduction. None of that is in the bundle; it is why this chat does not code.

## 10. Standing-table row, for `logbook/4` (to be filed when the batch is applied)

| `comanda-primary-operator` | 2026-10-27, OCR and operator | **No budget was declared before reconnaissance, which breaks the budget-first rule; recorded as such** (reconciled after the fact in `records/NOTES-comanda-primary-operator-2026-10-27.md` §2). Spent: the values, confidence and `source_ref` of the 43 cells of `comanda` and `comanda_alloc` (notes not read); all four comanda type rows in full; the standing-table rows `comanda-crown-of-aragon-2026-10-07`, `comanda-adjudications-2026-10-11`, `comanda-commenda-retrieval-report-2026-10-09`, `latin-hanafi-mixing-tests-2026-10-13` and `mudaraba-qirad-2026-10-14` in full; the definitions of `AP1`, `VF1` and `RB3` in full; mention counts over both censuses, both vocabularies and the vault; the titles of the 22 vault notes under six comanda and commenda slugs, by script into a file and not displayed. Of Madurell Marimón & García Sanz 1973: docs 1–4, 108 and 151's opening in full; the introduction at pp. 120–121; all 255 editors' summaries and archival lines; clause counts by period. **Prejudices** any later blind coding of `comanda` and `comanda_alloc` by this chat, of the documents named, and any blind re-scoring of `comanda-primary-2026-10-27` by this chat. Touches no other form. Record at `records/NOTES-comanda-primary-operator-2026-10-27.md`. |

## 11. Files

- `records/NOTES-comanda-primary-operator-2026-10-27.md` (this file).
- `records/PREDICTIONS-comanda-primary-operator-2026-10-27.md` (withheld).
- `records/PROMPT-comanda-primary-coding-2026-10-27.md` (the kickoff, verbatim).
- `~/GitHub/_blind-comanda-primary-2026-10-27/` (the bundle; untracked).
- `~/GitHub/_work-comanda-primary-2026-10-27/` (extraction scripts, per-page text, `docs.json` with the editors' summaries, `years.csv`, `doc-measure.csv`, `bundle-build.log`, `bundle.sha256`; untracked, and not for the coding chat).
