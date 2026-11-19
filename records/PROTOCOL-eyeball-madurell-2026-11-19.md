# Protocol: eyeball check of the Madurell instance record (2026-11-19)

**Written by the assistant (`claude-opus-5-5`) on 2026-11-19, on the design put to MS on 2026-11-17 and accepted, before the sample was drawn. To be committed and pushed, with the draw script, this file and the blank reading sheet, before MS opens the printed volume. Nothing in this file is changed after the push; corrections go in a successor file.**

## What is measured

How often a field of `records/instances-2026-11-03.csv` (the comanda-primary instance record, 118 instances from Madurell Marimón & García Sanz 1973, Zotero `VPX7DFWD`) disagrees in substance with the printed text. The reader is MS, reading the printed volume (his own copy), blind to the record. The result is the first row of the error-rate register (`logbook/4-appendix-error-rates.csv`) that is both `human-independent` and `random-seeded`, and so the first citable rate (`scripts/check_error_rates.py`).

**What is not measured.** The categorical columns (`loss_rule`, `security`, `duration` and the like) are the coder's readings, not transcriptions, and the cell values rest on them through `instance-chars-2026-11-03.csv`; this check reaches them only through the clause quotations and the coded absences. The OCR layer is not measured: the record was corrected against the page images on 2026-11-03.

## Sample

- **Population.** All 118 instances, whatever their assignment (83 `comanda`, 2 `comanda_ad_societatem`, 33 neither). The mod3 subset is reported apart at scoring.
- **Six strata, ten fields each, 60 in all**, drawn by `scripts/eyeball_sample.py draw --seed 20261119` (the seed is the date):
  1. `amount`: `amount_as_read`, every instance;
  2. `date`: `date_as_read`, every instance;
  3. `parties`: `parties`, every instance;
  4. `destination`: `destination`, every instance;
  5. `clause-present`: a risk clause (`peril_clause_quote`) or an obligation clause (`security_quote`) where the record quotes one;
  6. `clause-absent`: the same two clauses where the record codes the clause absent (`peril_clause` or `security` = `none`).

  In strata 1–4 a `.NR` in the record is in the population like any value: if the act states what the field asks for, the `.NR` is an error.
- **The sheet does not reveal the strata.** Each line gives the document number, the act within the entry where an entry holds two, the printed page and one question. The question for a field is the same whether the record holds a value or a coded absence, and every question allows the answer `none`. Lines are in random order.
- **The draw key** (strata and record columns, no record values) is held outside the tree, in `proposed-of/`, until scoring, and checked then against the sha256 below. It goes into `records/` with the scored sheet.

## Reading

- MS reads each act in full in the printed volume and writes his answer after `Reading:` on the sheet, as printed: spelling, abbreviations and numerals as the edition prints them; editorial brackets kept.
- While reading, the instance record, the instance-chars file, the text layer, the scan and the translation Docs stay closed. **Declared exposure:** MS reviewed the translation Docs (L01–L24) in November 2026, so he is not naive to the acts; he has not read the instance record's fields. The check measures the record against the print, not the reader's memory, and the notes will say so.
- The filled sheet is frozen under its sha256 before anything is scored.

## Scoring and error classes, fixed now

- **Automatic step.** `scripts/eyeball_sample.py score` compares each reading with the record after normalisation (case, accents, punctuation, spacing, u/v, i/j). A line matches if the two agree; a clause line also matches if the record's excerpt is contained in the reading; `none` matches a coded absence. Every other line is flagged. The score decides no error by itself.
- **Adjudication.** MS rules each flagged line, seeing the record value and his reading, into one class:
  - **content error** (counts toward the rate): a numeral, sum, unit, date element, name, role, place or word of a clause that differs from the print; part of what the field is defined to hold omitted (a date cut before the year the print gives; a party missing); text outside the field that adds a person, place or term (a witness entered as a party); a value where the print has none, or `.NR` / `none` where the print states it;
  - **form error** (counted apart, as in the Yamamoto pass): spelling, abbreviation or expansion, capitalisation, word division, a letter cut at the start or end of an excerpt that leaves the word identifiable, an excerpt shorter than the clause, a different but faithful format of the same parties;
  - **reader's slip**: the record is right and the reading is wrong; not counted against the record.
- **Rate.** Content errors over 60, overall and per stratum, with the 95% interval of the Beta(1 + k, 1 + n − k) posterior under a **flat prior**. The strata are equal-sized, not proportional, so the overall figure is a rate over the sampled mix of fields; a record-level rate weighted by the stratum populations is reported beside it. No informative prior is taken from the register's earlier, non-independent figures (ER-0001 to ER-0022).
- **Escalation, fixed now.** If a stratum shows two or more content errors in its ten, MS reads that field (for the clause strata, that clause family) across all 118 instances, and the census replaces the sample for that field.

## Predictions, before the draw

Made by the assistant, which has seen the column distributions of the record (counts of `.NR` and coded absences) and the opening words of some quotations, but not the drawn lines.

1. **Dates and amounts each show at least one content error**, as predicted on 2026-11-17: some `date_as_read` values stop before the year, and at least one amount begins mid-phrase.
2. **Parties show no content error**, as predicted on 2026-11-17; form errors expected.
3. **Destination: at most one content error.** Added today.
4. **Clause quotations: no content error, several form errors** (excerpts that begin mid-word). Added today.
5. **Coded absences: at most one content error.** Added today.

## Hashes, recorded at the draw

To be completed in the section below by the draw itself and not edited afterwards.

- Record drawn from: `records/instances-2026-11-03.csv`, sha256 `c1cc49824f0b8aa9bcad54a1cb9c6eed5e32fc096ffdf9bac646c7dee0dce0fa`.
- Blank reading sheet: `records/SHEET-eyeball-madurell-2026-11-19.md`, sha256 `0c51a80723b366d6e2968b05204dc8df2cf78cb3352e519f19513fd9dd4fc18c`, 60 lines, eight of them naming the act within a two-act entry.
- Draw key, held in `proposed-of/DRAW-KEY-eyeball-madurell-2026-11-19.csv` until scoring: sha256 2e6594e5f4c671c24e8a87fd702063be0b74bf6abf5710232212629c3c1b826d (not in backticks: the key is outside the tree until scoring, and `check_counts.py` C9 resolves backticked hashes against files in the tree).
- Populations: 118 in each of strata 1–4; 168 clause quotations; 41 coded clause absences.
- The draw was run twice and gave an identical key and sheet. The scorer's sheet parser was tested once on a copy of the sheet answered `none` throughout; it reported 16 matches. The per-line results were not displayed and the copy was deleted.
