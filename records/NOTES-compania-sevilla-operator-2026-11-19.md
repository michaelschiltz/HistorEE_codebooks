# NOTES — compania-sevilla-2026-11-19: operator brief for a blind first coding of the Seville capital-and-labour compañía, from Martínez Gijón (1970)

Committed together with the predictions file, the prompt, the bundle's README, the priors template and the coder's filled priors (sha256 `e384ba4319a9cb79deb4f9494e6928479086bfef46f433e5395ca42e43d53880`, checked by the operator against the bundle copy), before the coding chat opened any source. Written 2026-11-19 by `ai` (`claude-opus-5-5`) as operator, in the chat that ran the Carrera de Indias sweep, OCR'd and measured the editions, and read all ten deeds in full. This chat must not code; the coding goes to a fresh chat inside the blind bundle.

## 1. Scope

**Decided by MS (2026-11-18, confirmed 2026-11-19).**
- A new row in `organizational_forms` for the Seville *compañía* between capital and a travelling factor-partner.
- It is a form of its own, not a recoding of `comanda` / `commenda`: different period, jurisdiction and notarial practice. Its relation to those rows is declared as non-independence and comparison, not as identity (§5).
- Commission agency (*encomienda*, *comisión*) is out of scope.
- The 18th-century Seville and Cádiz *compañías* and the Cádiz *riesgo* are later, separate rows.

**Ruled by MS on 2026-11-19 ("Sure", 14:44), each as the operator recommended.** The table is kept as the record of what was put and what was accepted.

| No. | Decision | Ruling (= recommendation) |
|---|---|---|
| D1 | Row name | `compania_factoria_sevilla`. The deeds' own words for the relation are *compañía y factoría* and *factor y compañero* (docs. 3, 8, 10). The working label `compania_capital_trabajo_sevilla` describes the analysis, not the source. |
| D2 | Which deeds define the row | Docs. 3, 8 and 9: capital from one or more principals, a travelling factor who brings labour (doc. 3: labour and a token 80 ducados against 3,000), a quarter of profit to him. Doc. 2 (equal capital, one partner travels) falls outside that definition. All ten deeds go in the bundle; the coder assigns each deed to the row or not and says why, as on the comanda pass. |
| D3 | The rest of the appendix | Docs. 4–7 (commission sale, salaried factors) and 1, 10 (powers) are in the bundle as context and comparison, not as evidence for the row's cells, except that doc. 10 may bear on duration and death (it executes the death clause of a *factoría y compañía* with the principals of doc. 8). |
| D4 | A `_alloc` row in `loss_mitigation_forms` | Not in this batch. The loss question is carried by `CF2` and `LR6`; an allocation row on three deeds would duplicate them. Revisit when the Burgos and Cádiz risk material is coded. |
| D5 | Secondary witness | None in the bundle. Gutiérrez García 1998 (`NJHKYNGF`) is catalogued but its holding was not checked and it has not been read; the editor's own study (pp. 5–42) is withheld from the bundle (§7) and read at application. |
| D6 | MS's reading of doc. 8's loss clause (ruled 2026-11-19) | **Withhold it and score it.** It is a reading of one clause, not a convention for abbreviated or formulaic clauses; handing it to the coder would give the coder the instance value of `CF2` for doc. 8. The coder's independent reading of the same clause is the most informative single test this batch has. |
| D7 | Variation across deeds in other cells | `CF3` (principal count) also differs: doc. 3 one principal (bilateral), docs. 8 and 9 three and two (multilateral). MS's ruling of 2026-11-19 covers loss allocation (`CF2`, `LR6`). Recommendation: do not extend it now; the coder meets `CF3` blind, and the general question (what a row codes when its deeds differ on a cell that has no value for that) is put at application with the coder's report in hand. |

## 2. What this operator session spent

**No budget was declared before reconnaissance, which breaks the budget-first rule; recorded as such**, on the precedent of `comanda-primary-operator` and `venetian-pass-operator`. The session began as a source sweep and OCR work and turned into selection without stopping to budget. Reconciled after the fact:

| Question | Rung reached | Why that rung |
|---|---|---|
| Holdings and editions for the Carrera de Indias | 0 (catalogue) and 5 on the editions' structure | the sweep and acquisition (`claude/carrera-de-indias-sweep-2026-11-18.md`) |
| Text layers | 2 for 69 PDFs; 5 on 10 pages each of Martínez Gijón 1970, 1983 and Madurell 1961 | measurement against the images |
| The ten deeds of Martínez Gijón 1970 | **5: all ten read in full against the page images**, a clause inventory written (`claude/martinez-gijon-1970-reading-kit-2026-11-19.md`), doc. 8 transcribed and translated in full (Drive, `translations/Martinez-Gijon-1970/D08`) | MS asked for help reading the deeds before ruling on the row |
| The editor's study, pp. 5–42 | 5 on fragments only: the editor's note on modernised spelling (p. 43) and pages met during OCR measurement (PDF 2, 10, 25, 33) | measurement |
| The vocabulary | 5: names, value sets and applicability of all 33 `organizational_form_characteristic` codes; definitions of `CF2`, `LR3`, `LR6` in full | needed to answer MS's question on the loss cell |
| Live values of comparison rows | 1: counts of `CF2` values over the 30 cells; 5: the notes of 7 `CF2` cells (`commenda`, `ortoq_equity`, `ortoq_loan`, `societas_maris`, `comanda`, `comanda_ad_societatem`, `mudaraba`), read for precedent | MS's question on the loss cell |
| The vault | 1 and 3: term counts over 653 notes and `source-session` slugs of the matching notes; no titles, no bodies | the `--withhold-sessions` question |
| Earlier paperwork | 3: file names in `records/`; 5: headings and §1–§2 of `NOTES-comanda-primary-operator-2026-10-27.md`, the opening of `PREDICTIONS-comanda-primary-operator-2026-10-27.md`, ruling headings of `RULINGS-residual-default-2026-10-22.md`, two passages of `RULINGS-comanda-adjudications-2026-10-11.md` | to follow the house form and find precedent |

**Spent, by topic.** The row's cell values: spent (all deeds read, the loss clause ruled). `CF2` of the comparison rows listed above: spent. The vault: clean (counts and slugs only). The matrix values of rows other than those named: clean.

**Prejudices** any blind coding of this row by this chat, any blind re-scoring of the coding by this chat, and any later blind coding of `CF2` for the seven rows whose notes were read. It does not prejudice the coding chat, which works from the bundle. The standing-table row is in §10.

## 3. The edition measured

Martínez Gijón, "La práctica del comercio por intermediario en el tráfico con las Indias durante el siglo XVI", *AHDE* 40 (1970), pp. 5–84 (Zotero `K36HMDA9`, attachment `27R6WUAW`); PDF p. *n* = printed p. *n*+4. Apéndice documental pp. 43–84 (PDF 39–79), ten deeds, APS Oficio XV, notaries Bernal González Vallecillo (1516–1524) and Alonso de Cazalla (1538–1550).

**Text layer** (OCRmyPDF 16.13, Tesseract 4.1.1, `tessdata_best` Latin, 2026-11-18; measured on 8 pages, then the whole appendix read against the images on 2026-11-19):

| Class | Finding | Obliges an image check in the coding chat? |
|---|---|---|
| Numerals | Fail in headings and the editor's footnotes: 15838 for 1538 (doc. 1), "Libro 1.9" for 1.º, folio markers "r9", "v9", "fol. 88 v" for 83 vº (doc. 2). Sums and dates inside the deeds are written in words and read correctly. | Yes, every numeral in a heading or archival line |
| Characters | 2–7 errors a page in the appendix: dotless *ı*, `e!`, `ì`, `}`, *Il* for *ll*; joins and splits (*car gadas*, *obligadoa*) | Yes, for every quotation |
| Proper names | At risk: "Iope", "Ybħar", "Gonzałlo" | Yes |
| Structure | No scrambled order, no lost lines found in the appendix | No |
| Truncation | None found | No |
| Headings | Running heads garbled; the small-caps rubrics (*Compañía*, *Factoría*, *Pacto*, *Obligación*, *Poder*) read with case errors | Yes, if a rubric is cited |

**Edition-level facts the coder must be told.**
- The editor states (p. 43) that he modernised the spelling. Quotations are his text (CONTRIBUTING §3, 2026-11-18).
- The rubrics are not evidence of roles or of type: doc. 7 is headed *Compañía* and is a salaried service contract.
- Conflicts inside the print, recorded and not resolved: doc. 2 is signed "Juan de Córdoba.—Juan Hernández", with no Pero Fernández; doc. 4 gives its penalty as 100,000 and as 50,000 maravedís; doc. 9's header has "Fols." with no numbers; doc. 10's header has fols. 405r–v and the text a marker "fol. 450 vº"; doc. 8 names an attorney in the incorporated power as both "Alonso Díaz de Herrera" and "de Llerena", and Hernán Pérez as "Fernando Pérez" and "Hernández Pérez"; name variants Fernández/Hernández de Loya (8), Bernardino/Bernaldino (7), Ybar/Eibar (6).

## 4. Reading conventions

**Given to the coder** (rulings in force, or doctrine already in CONTRIBUTING §3):
1. A deed read in full in the edition is `primary-transactional`; the editor's study is secondary and one witness with the edition on anything they share.
2. Quotations are the editor's modernised text, cited by printed page and APS reference.
3. Rubrics and the editor's headings are not evidence of roles or type.
4. An absence read off the text layer is a claim about the layer: every coded absence and every quoted clause is checked against the page image, which the bundle carries.
5. The coder does not invent values or tokens. Answer 4 of the six asks, as on every pass, for any characteristic that did not fit the evidence; nothing further is said about deeds that answer a question differently, because whether the coder reports that unprompted is scored (predictions file, scoring rule 2). A sentence instructing it was drafted into the prompt and removed at read-back.

**Withheld from the coder** (ruled by MS, scored afterwards; see the predictions file): the reading of doc. 8's loss clause (D6), and the contract-set value for `CF2` and `LR6`.

## 5. Non-independence, declared before the rows

- **One editor's selection.** All ten deeds were chosen by Martínez Gijón from "more than 100" protocols for a study of intermediary trade. Agreement among them is not evidence of how common their terms were.
- **One office.** All ten are Oficio XV, two notaries in succession. Clause drafting is the office's as much as the parties'.
- **One set of principals twice.** Docs. 8 and 10 have the same three principals (Gonzalo Jorge, Hernán Pérez the younger, Rodrigo Pérez) and two different factor-partners; doc. 8 names the second (Pedro Fernández de Carmona) as their *compañero*.
- **One author.** The study (pp. 5–42) and the edition are one witness on anything they share. Martínez Gijón 1979 (`Q2CCUAHW`, on order by ILL) is the same author and is `primary-normative`/secondary on law to 1737; it can never fill a practice cell.
- **The comparison rows.** `comanda`, `comanda_ad_societatem`, `commenda`, `societas_maris` and `mudaraba` are coded from other editions. Nothing in this batch corroborates or contradicts them, and no agreement with them is a finding about the Seville form. The census separated `comanda` from `comanda_ad_societatem` on the loss rule (type rows, 2026-10-07); MS has ruled that this row is not split that way (2026-11-19), because the deeds' names do not sort them and each split row would rest on one deed.

## 6. Cells that are not a blind test

- `CF1` (capital-labour asymmetry): the row's definition (D2) states a labour-supplying factor; `CF1` is fixed by construction for docs. 8 and 9. Doc. 3 (labour and 80 ducados against 3,000) is the only test.
- `LR3` (profit-and-loss sharing): the definition states a quarter of profit to the factor; `LR3` = 1 by construction under the clarification of 2026-10-12 ("a negotiated ratio that does not follow capital … is 1").
- `MG4` (authorization source): private notarial contract throughout; near-certain, scored apart.

## 7. The bundle

- **Edition pages:** Martínez Gijón 1970, PDF pp. 39–79 (the appendix and the p. 43 note), as the OCR'd PDF and as page images at 300 dpi. **The study, pp. 5–42, is withheld** (D5): it is the editor's analysis of the same deeds and would prime the coder; it is read at application.
- **Not in the bundle:** this brief, the reading kit, the D08 translation, the audit and sweep docs, the predictions file, Madurell 1961 (Barcelona, out of scope), Martínez Gijón 1983 (freight contracts).
- **Vocabulary:** as live, 0.13.0, without the contract-set value.
- **Command** (first coding; no rows of this form exist, so nothing to withhold by type):

```sh
python3 scripts/make_blind_bundle.py --out ~/GitHub/_blind-compania-sevilla-2026-11-19
```

**Vault check (2026-11-19, rungs 1 and 3: term counts and `source-session` slugs; no titles or bodies read).** 653 notes. Zero hits for *Oficio XV*, *Cazalla*, *Vallecillo*, *factoría*, *factor y compañero*. *Martínez Gijón* appears in 12 notes (17 with the unaccented spelling), all in comanda sessions (`comanda-crown-of-aragon-2026-10-07` 6, `comanda-adjudications-2026-10-11` 2, `comanda-commenda-retrieval-report-2026-10-09` 2, `comanda-primary-application` 1, `madurell-translation-test` 1, one note without a slug); none of them contains *intermediario*, *1970* or *Indias*, so they cite other works of his, not this edition. *Carrera de Indias* (3), *Casa de la Contratación* (2) and *Sevilla/Seville* (8/6) sit in archive surveys, `source-editions-survey`, `referee-round-5` and `borrower-from-hell-ergodicity`. **The vault is clean on the deeds; the count proves it and no title was read.** No `--withhold-sessions`: the comanda notes concern rows whose values the bundle's `data.csv` carries anyway.

**Logbook.** One dated section concerns this batch: logbook 5, `## 2026-11-18 — ai — what each class of evidence can carry: five rulings by MS before the Carrera de Indias batch`. It is withheld with `--withhold-dates 2026-11-18` (no other section carries that date). The doctrine itself stays in the bundle through CONTRIBUTING §3, whose example citation names "ed. Martínez Gijón 1970, doc. 3" and quotes its opening formula. That is a disclosed, unremovable leak: it gives the source and an opening formula, no clause and no value.

**Final command** (on MS's Mac):

```sh
cd ~/GitHub/HistorEE_codebooks
python3 scripts/make_blind_bundle.py --out ~/GitHub/_blind-compania-sevilla-2026-11-19 \
    --codebooks . --vault ../myfoamrepo --withhold-dates 2026-11-18
mkdir -p ~/GitHub/_blind-compania-sevilla-2026-11-19/sources
cp proposed-of/compania-sevilla-sources/Martinez-Gijon-1970-AHDE40-pp43-84.pdf \
   ~/GitHub/_blind-compania-sevilla-2026-11-19/sources/
```

The excerpt is PDF pp. 39–79 of the attachment (41 pages, 3.7 MB): the OCR layer of 2026-11-18 over the original 1-bit page images, which the coder renders with `pdftoppm` for every image check. Its first page (printed p. 43) begins with the last lines of the editor's study (on powers of attorney of 1549, footnotes 110–111) and carries the note on modernised spelling: a disclosed leak of a few lines of the withheld study.

## 8. Read-back

Before the coding prompt is handed over, it is read back against the predictions file and every sentence that appears in both is deleted. The loaded skills (`code-a-form`, `run-a-coding-batch`) are read back against it too. Anything that cannot be removed is disclosed in the coding notes.

**Clarifications sent to the coder after the priors, before step 4** (raised by the coder; both are errors in the operator's prompt, copied from a recoding prompt):
- *Record IDs.* The prompt said to take the next `record_id` from the bundle's `data.csv`. `code-a-form` requires placeholder IDs (`OF-XXXX-01`, …) for a first coding, so that parallel batches cannot collide; real IDs are assigned at application from the live file. Ruling: placeholders.
- *`source_class`.* The prompt asked for it, but `data.csv` has no such column (only `recodings.csv` has). Ruling: keep the `data.csv` columns, state the class at the start of each cell's `notes`, and raise it in the coding notes, as the coder proposed.

## 9. For MS, before the coding chat opens

1. ~~Rule on D1–D7 (§1).~~ Done, 2026-11-19.
2. ~~Run the bundle command (§7).~~ Done, 2026-11-19.
3. Commit this brief (moved to `records/`) and the predictions file, together with the coder's priors file, before the coding chat opens any source.
4. ~~Confirm the vault check.~~ Done, 2026-11-19: clean; no sessions withheld; one logbook date withheld.

## 10. Standing-table row, for `logbook/4` (to be filed when the batch is applied)

`compania-sevilla-operator-2026-11-19` · 2026-11-19 · spent: the ten deeds of Martínez Gijón 1970 in full, with a reading kit and a full translation of doc. 8; MS's ruling on doc. 8's loss clause; the `organizational_forms` vocabulary (33 codes); `CF2` counts over 30 cells and the notes of 7 `CF2` cells; parts of the comanda-primary operator paperwork · prejudices: blind coding of the Seville row by this chat; blind re-scoring by this chat; blind coding of `CF2` for `commenda`, `ortoq_equity`, `ortoq_loan`, `societas_maris`, `comanda`, `comanda_ad_societatem`, `mudaraba` · clean: the vault; matrix values of all other rows and cells.
