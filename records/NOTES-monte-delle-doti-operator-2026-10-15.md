# Operator brief, part 2: the Florentine *monte delle doti* — one loss row, 1425–1530, coded blind from a minimal bundle (2026-10-15)

- **Slug:** `monte-delle-doti-operator`. Operator (Chat A, part 2), 2026-10-15, `claude-opus-5-5`. It is spent on this form and never codes it. Part 1 is `monte-delle-doti-scheme` (`records/NOTES-monte-delle-doti-scheme-2026-10-14.md`, §§1–14), which this brief cites and does not re-spend.
- **Status:** items 1–6 of MS's instruction are done. The coding chat has not been opened. MS commits this brief, the priors template and the prompt (§11), builds the bundle (§9), and opens the coding chat with the prompt.
- **NOT FOR THE CODING CHAT.** §10 holds the withheld predictions, and §§5–6 hold what this session read of the sources. The minimal bundle (§9) carries neither this file nor part 1's record. §9.4 is the absence check.

## 1. Inputs and the order of work

Read first, on MS's instruction: part 1's record in full; its logbook 4 standing-table row; logbook 2, 2026-10-14 (iii). Then the spend budget was declared to MS in chat **before any reconnaissance** (reconciled in §2). Then, in order: holdings (§3); the tables (§4); scope, with each rung-5 question written down in chat before the read (§5); the declarations (§6); the files (§§9–11).

## 2. Spend: the budget as declared, and the reconciliation

| # | question | planned | reached | what forced any excess |
|---|---|---|---|---|
| 1a | holdings | 0–2 | 0 (copy of `zotero.sqlite`), 1 (sha1, whole-file `pdftotext` counts), 2 (`pdfinfo`, `pdffonts`, `pdfimages`, page-edge numbers over every page) | — |
| 1b | tables | 1; 5 on the delta only | 1, then a full recompute, compared programmatically against part 1's §7. Only differences were printed, and there were none | Nothing new spent. The recompute re-reads material part 1 spent, and was the cheapest proof that no cell had been edited in place |
| 2a | split | 2; 1; contingent 5 | 2 (Molho ch. 2 has no subsection titles; K&M 1978 has one section numeral), 1 (per-page year and legislative-term counts), then **5 on R5-A, R5-B, R5-D**, each written down in chat first | Titles named no reform, and counts can locate a change but cannot say what changed |
| 2b | organizational row | 2; 1; contingent 5 | 1 (entity-term counts per page), **5 on R5-C**, written down first | Counts showed `Monte comune` 60 and `separate`/`distinct`/`own` 5 in ch. 2. They cannot decide the §5 criterion |
| 2c | Kirshner 2015 ch. 5 | 2; 1 | 2 (table captions, candidate headings), 1 (term counts), 0 (the book's "Original Publication Information", p. 215, read whole: it is bibliographic) | — |
| 2d | "The Morning After" | 1; 2 | 1 (word counts, Latin function-word counts per page, a word-sequence match ratio computed without display), 2 (locations of the endnotes and the appendix) | — |
| 2e | C2 | 3 | 3 (type-vocabulary columns of both censuses), plus **5 on repository prose**, read to verify a precedent part 1 said did not exist: logbook 2's two lines on the `deed_of_settlement_company` declaration, and five `CHANGELOG.md` lines matching `deed_of_settlement` (which carry that row's and `compagnia`'s owner-shielding values, already spent by part 1's whole-matrix read) | The column count contradicted part 1, and the prose was needed to see whether the precedent was deliberate. It concerns another form and prejudices nothing about this one |
| 3 | declarations | 1; 3 | 1 (Gazzini's two works: own-term and author counts), **3–5 on `confraternity_fund_it`**: its `source_ref` values and one-line note contexts | A count found Florence named in 11 of that row's 23 cells, and C1 had to be re-assessed |
| 4 | vault | 1; 3; 4 if needed | 1 and 3 only (term counts; `source-session` slugs of the four matching notes). **No title, no body** | Under budget. The minimal bundle ships no vault, so the two `dowry` notes part 1 left open need no decision |
| 5 | bundle | 1; matching lines | 1 (term counts over every candidate bundle file), plus the matching lines in `data.csv` notes and the type vocabulary, as part 1 did | — |

**Passive exposure, disclosed:**
- Commands that printed page tops showed first lines of body text: Molho p. 1 (Introduction), Kirshner 2015 pp. 229, 230, 233, 291, 292, 309, 310. That is one line each.
- The claude.ai Project's doc titles are listed in this chat's context.
- I read the tooling and precedent files: `make_blind_bundle.py`; the commenda-pilot operator brief's bundle sections; `PRIORS-she-associations-2026-10-13.md`; `PROMPT-commenda-primary-2026-09-28.txt`. None concerns this form.

## 3. Holdings, re-verified against part 1's §14

**The holdings are as §14 states, with these changes and corrections:**

- **MS has trashed four items since §14:** `WCWDZ3HE` (the review-carrying book duplicate), `UGAWLMKP`, `DKVV9U4C`, and `4V7KSUYZ`, which was already in the Trash. `ZL89FSGR` (Amazon duplicate of Kirshner 2015) is live and outside the collection. The three loose duplicates in `ZoteroFiles` are still on disk, attached now only to trashed items.
- **Still not held:** Kirshner 1978, *Pursuing Honor* (`DF85C2L9`, no attachment); Carboni 1999; Chabot & Fornasari 1997.
- **Correction: Molho 1994's offset is printed = pdf − 21, not "pdf + 20".** Measured on 358 page edges, uniform from pdf 23 to pdf 479. So **ch. 2 is pdf 48–100**, not 47–99; ch. 3 is pdf 101–148; ch. 4 is pdf 149–201. Part 1's per-chapter counts are shifted by one page, which changes them by a few hits at most. **The Zotero Extra field of `96G86SL5` carries the wrong offset and should be corrected (§12).**
- **Correction: Kirshner 2015 is not an Internet Archive scan.** It is the publisher's typeset PDF: `Producer: PyPDF2`; embedded StempelGaramond Type 1C fonts on every page; images on two pages only. Its text layer is the typesetter's, so its figures may be read from the text and checked against the page. **Molho 1994 is an Internet Archive scan** (`GlyphLessFont` OCR over JPX images), as is K&M 1978's JSTOR scan (jbig2 images with a hidden Times text layer). Figures from those two are read from the page image.
- **"The Morning After" 2009 is verified,** from the author's own book: Kirshner 2015, "Original Publication Information", p. 215. It is in *From Florence to the Mediterranean and Beyond*, ed. Curto, Dursteler, Kirshner and Trivellato, vol. 1, **29–61**, Florence: Olschki, 2009. **The Zotero item `HXZ3FL7E` gives pp. 29–62, which is wrong.** The same page shows that **ch. 5 reprints Kirshner & Klerman 1991**, in *Banchi pubblici, banchi privati e monti di pietà nell'Europa preindustriale* (Genoa: Società Ligure di Storia Patria), vol. 1, 369–98.

Whole-file counts reproduce §14 to within normalisation, because hyphenated line breaks are joined here:

| work | sha1 (12) | PDF pp. | offset (printed =) | `monte delle dot` / `dowry fund` / `Monte` / `Monte comune` / `official*` |
|---|---|---|---|---|
| Kirshner & Molho 1978 | `0a3ab3f16156` | 36 | pdf + 402 (35 edges) | 27 / 50 / 103 / 7 / 11 |
| Molho 1994 | `b05eb031b656` | 480 | **pdf − 21** (358 edges) | 140 / 312 / 1082 / 43 / 109 |
| Kirshner 2015 | `aab8dfe0fa97` | 471 | pdf − 8 (432 edges) | 17 / 61 / 261 / 18 / 99 |
| "The Morning After" 2009 | `fe48ea6c822d` | 34 | pdf + 28 (from §13) | 4 / 22 / 89 / 2 / 34 |
| Molho & Pescarmona 1986 | `74ff28423d18` | 25 | pdf + 145 | 40 / 0 / 91 / 1 / 0 |
| Carboni 2022 | `48ba651ddb1f` | 23 | pdf + 219 | 4 / 14 / 38 / 0 / 3 |
| Morrison et al. 1977 | `1b71615d12a7` | 6 | pdf + 486 | 8 / 5 / 22 / 0 / 4 |
| Morrison et al. 1985 | `5b30907935c8` | 8 | pdf + 527 | 4 / 49 / 6 / 0 / 5 |
| Guinn 2010 | `a043200deae0` | 8 | — | 5 / 3 / 5 / 0 / 2 |

## 4. Value tables at the live row count

**Unchanged.** `loss_mitigation_forms` has 795 rows, 51 forms, last id `LM-0795`. `organizational_forms` has 948 rows, 36 forms, last id `OF-0950`. Neither has changed since part 1. The value distribution of every one of the 26 loss and 33 organizational characteristics was recomputed and compared with part 1's §7. **There were 0 differences**, so §7's zero- and one-instance tables stand as written and are cited, not reprinted. The characteristic vocabularies were last modified on 2026-10-12 and 2026-10-13, before part 1, so no `allowed_values` moved either.

## 5. Scope, decided

### 5a. The split test: one row, `1425-1530`; no boundary is known to move a cell

**What changed, from the named passages (R5-A, R5-B, R5-D).** The detail is withheld in §10.1, because every item is evidence the coder must find for itself. In outline, the legislation moved:
- the deposit's fate when the girl died or entered religion before marrying, in 1433 and 1437;
- the model deposit and the yields, in 1428, 1433 and 1436, and by price scales from 1458 to 1463;
- the terms on offer, in 1433, 1459 and 1479;
- the medium of deposit and payout, between cash and Monte credits, from 1440/1 through 1503;
- eligibility and capacity, with investor categories from 1452/3 and a subscription ceiling (*ritratto*) from 1470;
- the separation of the fund's creditors from the commune's, which was ended in 1496.

**The argument.** A boundary splits the row only if it moves a characteristic this census codes:
- The rate, term and price-scale changes are changes of degree inside one value. They are **variants**, on the Pisa land-partnership precedent (logbook 2, 2026-10-12 (iv)).
- The medium of deposit and payout, and the 1496 merger, bear on no loss characteristic as defined.
- **The 1433 and 1437 changes are the hard case.** They change how much of the contribution the depositor loses when the payout trigger fails. No characteristic in the loss vocabulary codes that quantity; it is not a peril-bearer (`RB1`), a residual claim (`LS2`) or a loss-sharing rule (`LS1`). So on the vocabulary as written they are variants too, **and that is an argument from the vocabulary, not from the coding**. The alternative reading is stated fairly: if `RB1` is read with the girl's death as the peril, its value could differ across 1433. The coder decides that.
- The eligibility categories and the subscription ceiling could move `MB2`. Again, that is the coder's call.

**Decision.** One row, period **`1425-1530`**, tradition **`Tuscan (Florentine)`**. The end date is the last republican regime: Molho dates the tension between regimes "from 1498 to 1530", and the first measure of the new regime, a special gabella on depositors in January 1530/1, falls outside it.

**The coder applies the split test cell by cell, at every dated change it finds, and is not told the dates** (§10.2). Where a cell's value would differ across a change, it reports a split proposal in its adjudications. It does not split silently and does not code `P` for change over time. This is the code-a-form split test, with the boundary left for the coder to find, because naming a date in the prompt would tell it where this session expects a change.

### 5b. No `organizational_forms` row: the criterion fails on present evidence

The record's §5 criterion requires assets, administration or claims of the fund's own, distinguishable from the commune's public debt. R5-C finds the opposite (§10.1):
- The founding bill invited deposits with the officials of the funded public debt (Molho 30).
- Administration lay with the *officiales et camerari montis* (31).
- The fund was an account inside the Monte that was serviced by buying Monte comune credits (37).
- Its cash was diverted to war expenditure (49, 63).
- Its accounts were "difficult to separate" from the city's general expenditures (50).
- From 1496 its creditors were no longer distinguished from the commune's (77).

The counter-evidence is one phrase: K&M 1978, 409, "the fund's officials". That is the authors' shorthand. Molho's paraphrase of the bill, and the Latin he quotes, both name the Monte's officials.

**Decision: not warranted.** An organizational row would code the *Monte comune* under the fund's name, which is the umbrella defect. **Reopen only if Kirshner 1978, *Pursuing Honor*, is acquired and shows officials, books or assets of the fund's own.**

### 5c. Kirshner 2015 ch. 5, "The Seven Percent Fund": out

Its four tables are encumbrance types, Florentine and non-Florentine accounts, holding patterns, and credits held to redemption. `encumb` occurs 105 times in 17 pp., `credit` 198, and the dowry-fund terms 8. It reprints a 1991 paper in a volume on public banks (§3). **It treats a fund of the commune's debt. That is out of scope under part 1's §6, and it does not ship.**

### 5d. "The Morning After": the 2015 ch. 4, not the 2009 version

**The premise that only the 2009 version carries the Latin appendix is false.** Kirshner 2015 moves it to **Appendix 4, "Confessio dotis of Chirico di Giovanni of Florence", pp. 230–231**: 512 of the 548 words of the 2009 appendix (pp. 60–61) are matched in it. The 2015 body is 8,237 words, and 90% of its word sequence occurs in order in the 2009 text. Its notes are endnotes, at pp. 292–309. **So the two are one text, lightly revised, and both carry the appendix.**

**Chosen: 2015**, for three reasons:
- it is the author's revision, and his Introduction says the earlier essays were revised;
- its container is CrossRef-verified for the book;
- the census already holds the book.

The cost is that it ships as three page ranges and its notes are not on the page. The chapter DOI (`10.3138/9781442664517-007`) is **unverified**: CrossRef refused the query (HTTP 429, 2026-10-15).

The fair alternative is 2009: it is self-contained, has footnotes in place, and its container is now verified from the 2015 book's p. 215. MS can swap it in by changing one line of §9.3. **Never both.**

### 5e. C2, `compagnia@organizational_forms` at `same-polity`: recommended, both directions; MS decides

- **Part 1 said there was no precedent for a cross-dataset `same-polity` declaration. There is one.** `deed_of_settlement_company` declares `friendly_society_england@loss_mitigation_forms` at `same-polity`, written on 2026-09-05 (logbook 2). Its reverse went into prose, because `friendly_society_england` already declared `guild_mutual_aid` at `uncertain`.
- **Here the column can carry both directions.** `compagnia` reads `.NR` / `.NR`, so writing `monte_delle_doti@loss_mitigation_forms` / `same-polity` degrades nothing. The new row has no other declaration (C1).
- **Overlap.** `compagnia` is "13-15c"; this row is 1425–1530.
- **Why declare.** Any comparative statement that sets this row beside `compagnia` sets two institutions of one polity beside each other. They share a fiscal and legal environment, so their agreement is not two data points.
- **Recommendation: declare it, in both directions, in the batch that applies the row.**

### 5f. Confidence cap

**N1 makes the whole literature one witness, so no cell takes `high`.** The cap is **`medium`**. It applies even to an `articulated` cell that quotes an enactment, because the quotation reaches us through the same two scholars' selection from the same registers.

### 5g. Scope, restated for the prompt

- **In:** the Florentine *monte delle doti*, 1425–1530.
- **Out:**
  - the commune's funded public debt itself, and its other funds and instruments;
  - charitable dowry endowments (*doti di carità*);
  - any other city's dowry fund;
  - the commenda family.

## 6. Declarations, final, before any row exists

### Non-independence

- **N1. One witness: confirmed, and extended.**
  - Shipped: K&M 1978; Molho 1994; Kirshner 2015 ch. 4 (= the 2009 essay, revised); Morrison, Kirshner & Molho 1977 and 1985.
  - Held but not shipped: Molho & Pescarmona 1986; Kirshner & Klerman 1991/2015.
  - All work from the fund's own registers, and every author is Kirshner, Molho or a co-author of theirs. The 2015 chapter's first note cites Molho 1994, 125. Agreement among them is not corroboration. Hence the cap (§5f).
- **N2. Carboni 2022 is not shipped.** It is still presumed dependent for Florence (Kirshner 13 / Molho 13), its citing contexts are still unread, and it is now moot for this batch. Its Bolognese half is out of scope.
- **N3. Coudy 1957: unchanged, and enforced by construction.** Coudy is not shipped, so no cell can rest on him.
- **N4. Kohn 1999, Kuehn 2008, Miner 2020: unchanged, and enforced by construction.** None is shipped.
- **N5. The census's own record is not a witness: unchanged, and enforced by construction.** The minimal bundle carries no logbook, no vault and no `records/` file beyond the priors template.
- **N6 (new). The bundle's `data.csv` is house practice, not a witness.** Its neighbours are coded from other sources, and none cites Kirshner or Molho (0 hits). The `avariz_fund` and `avariz_vakfi_kirkcesme` notes describe orphans' marriage portions as a life-event payout; that is calibration a coder will see and is disclosed (§9.5).

### Co-occurrence

- **C1. Within `loss_mitigation_forms`: none declared. Re-assessed, with one hazard added.**
  - `confraternity_fund_it` is "Latin Christendom / Italian", which is not a polity, so no declaration fits the column. But **11 of its 23 cells cite Florentine cases** in their notes: the oliandoli e pizzicagnoli fund of 1345, and Florentine hospitals.
  - It is independent of N1 by measurement. Gazzini 2020 has 0 hits on Kirshner and 0 on Molho, and Gazzini 2020b likewise.
  - So **a comparative statement setting this row beside `confraternity_fund_it` on a cell whose note rests on Florentine evidence is partly same-polity.** That is recorded in prose and must be said wherever the comparison is made.
  - `marine_insurance` ("Italian city-states") was also assessed. Its source and cells name no Florence, so it is not a hazard.
- **C2.** Recommended, in both directions (§5e). MS decides.
- **C3. Moot.** No organizational row (§5b).
- **C4. Holds, and binds harder than part 1 thought.** The fund sat inside the *Monte comune* (§5b), which has no row. So any comparative statement about the fund's counterparty or governance is a statement about the commune's public debt, which this census does not code.
- **C5. Unchanged.** The hypothesis that the tontine descends from the Italian *monti* stays in prose. Nothing shipped bears on it, and N3 bars Coudy.

## 7. Corrections to part 1's record, which is not edited

`records/` is preserved verbatim, so the corrections are made here and in logbook 4's row, and not in part 1's file:
1. Molho 1994's offset and chapter ranges (§3).
2. Kirshner 2015 is not an Internet Archive scan (§3).
3. A cross-dataset `same-polity` precedent exists (§5e).
4. `HXZ3FL7E`'s pages are 29–61 (§3).
5. Kirshner 2015 ch. 4 carries the Latin appendix (§5d).

## 8. Bundle design: minimal, on the commenda-pilot precedent of 2026-09-28

**Recommended: the minimal bundle. It differs from the commenda pilot in carrying the loss census's live `data.csv`.**

- **Why minimal.**
  - Measured over the tracked repository, this fund is named only in part 1's record (53 lines), logbook 2 (7), logbook 4 (4) and logbook 5 (1).
  - In the vault it is named only in four notes: the two withheld survey sessions, `stoic-cooperation-loci` and `source-editions-survey`.
  - The vault therefore gives the coder nothing it may use (N5), and shipping it would cost a rung 3–4 decision on two notes.
  - The full-repository option ships logbook 2 2026-10-14 (iii), which states the organizational-row criterion this brief has now decided, plus logbook 5 and this brief and part 1's record, which must be deleted by hand.
  - Including less leaks less, and **every residual mention in the full option is avoidable at no cost to the coding**.
- **Why carry `data.csv`.** The commenda pilot dropped it because the forms under test were in it. This form is new, and no cell of it exists. Carrying the live matrix restores what the pilot gave up: the calibration of house practice from other rows' notes. It also lets code-a-form Step 1.3, the comparative view, be done as written.
- **The fair alternative** is `make_blind_bundle.py --withhold-sessions italian-archives-survey,european-archives-survey,monte-delle-doti-scheme,monte-delle-doti-operator --withhold-dates 2026-09-10`, then deleting the two records and verifying absence by term count. It also ships the logbooks, and so the house practice in prose. Its costs are the residual hand-review items listed above, plus the two vault notes.

## 9. The bundle: contents, sources, commands, checks

### 9.1 Layout (`~/GitHub/_blind-monte-delle-doti-2026-10-15`)

- At the root:
  - `README.md` (§9.3);
  - `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md` and `EDITING-CSV.md`, copied unedited. A term count found no mention of dowries, the *monte*, tontines, Florence, marriage or widows in any of them;
  - `PRIORS-monte-delle-doti-2026-10-15.md`, the template, which the coder fills as `PRIORS-monte-delle-doti-filled-<date>.md`.
- `datasets/loss_mitigation_forms/`: `data.csv`, `recodings.csv`, `datapackage.json` (which references both).
- `vocabularies/`:
  - `loss_mitigation_characteristic.csv`, **with the `exemplar` column dropped**, on precedent; the round-trip was tested byte-identical before the drop;
  - `loss_mitigation_type.csv`.
- `views/loss_mitigation_forms--risk-pooling.md`. **No `build_views.py`**, so the bundle's view cannot be overwritten.
- `scripts/`: `check_dependence.py`, `check_vocabularies.py` and `check_quotations.py`. All three were tested inside a trial build. `check_vocabularies.py` reported "2 files, 86 codes … valid", `check_dependence.py` reported "dependence problems: 0", and `check_quotations.py` reported "0 error(s)".
- `sources/` (§9.2) and an empty `proposed-of/`.

### 9.2 Sources, exact files and printed pages

**Shipped.** The file name carries the printed range, and the README gives each file's page map. All cuts were made in the trial build and checked against page-edge numbers.

| bundle file | from (`ZoteroFiles`) | PDF pages | printed pages |
|---|---|---|---|
| `kirshner-molho-1978_jmh50_pp403-438.pdf` | Kirshner and Molho - 1978 - … .pdf | 1–36 (whole) | 403–438 |
| `kirshner-molho-1978_p403_ocr.txt` | OCR of pdf 1 (400 dpi grey, `tesseract -l eng`) | 1 | 403 (521 words in the trial) |
| `molho-1994_frontmatter_title-cip-contents-dates.pdf` | Molho - 1994 - … .pdf | 4–5, 12, 21 | title, CIP, contents, Note on Dates |
| `molho-1994_ch2-3_pp27-127.pdf` | same | 48–148 | 27–127 (ch. 2 "The Monte delle Doti"; ch. 3 "Investors and Beneficiaries") |
| `molho-1994_app1-sources_pp351-360.pdf` | same | 372–381 | 351–360 |
| `molho-1994_ms-sources-abbreviations_pp433-434.pdf` | same | 454–455 | 433–434 |
| `kirshner-2015_frontmatter_title-copyright-contents-origpub-abbrev.pdf` | Kirshner - 2015 - … Italy.pdf | 3–6, 223, 247–248 | title, ©, contents, p. 215, pp. 239–240 |
| `kirshner-2015_ch4_pp94-113_app4_pp230-231_notes_pp292-309.pdf` | same | 102–121, 238–239, 300–317 | 94–113; 230–231; 292–309. **p. 309 also opens ch. 5's notes**, which are out of scope and disclosed in the README |
| `morrison-kirshner-molho-1977_aje106_pp487-492.pdf` | Morrison et al. - LIFE CYCLE EVENTS … .pdf | 1–6 | 487–492 |
| `morrison-kirshner-molho-1985_ajph75_pp528-535.pdf` | Morrison et al. - 1985 - … .pdf | 1–8 | 528–535 |

**Not shipped, and why:**
- Kirshner 2015 ch. 5: §5c.
- "The Morning After" 2009: §5d.
- Molho & Pescarmona 1986: N1. It is the same witness, it is an analysis of investors' social geography, and Molho's ch. 3 treats investors at greater length.
- Carboni 2022: N2, and Bologna is out of scope.
- Guinn 2010: five own-term hits; not a treatment.
- Molho 1994 chs. 1 and 4–7 and appendices 2–6: these treat marriage and the ruling class, not the fund's terms. Ch. 4, "Registrations in the Monte", uses the registrations as data on marriages.
- Kirshner 1978: not held.

The coder is told it may ask for more, with the page range and the cell it would move. MS decides.

### 9.3 Commands (macOS; `brew install qpdf poppler tesseract` if missing)

```sh
R=~/GitHub/HistorEE_codebooks
Z="$HOME/Library/CloudStorage/GoogleDrive-michael.schiltz@gmail.com/My Drive/ZoteroFiles"
B=~/GitHub/_blind-monte-delle-doti-2026-10-15
[ -e "$B" ] && { echo "refusing: $B exists"; exit 1; }
mkdir -p "$B"/{datasets/loss_mitigation_forms,vocabularies,views,scripts,sources,proposed-of}
cp "$R"/{CLAUDE.md,CONTRIBUTING.md,CHARACTER-CODING.md,EDITING-CSV.md} "$B"/
cp "$R"/records/BUNDLE-README-monte-delle-doti-2026-10-15.md "$B"/README.md
cp "$R"/records/PRIORS-monte-delle-doti-2026-10-15.md "$B"/
cp "$R"/datasets/loss_mitigation_forms/{data.csv,recodings.csv,datapackage.json} "$B"/datasets/loss_mitigation_forms/
cp "$R"/vocabularies/{loss_mitigation_characteristic.csv,loss_mitigation_type.csv} "$B"/vocabularies/
cp "$R"/views/loss_mitigation_forms--risk-pooling.md "$B"/views/
cp "$R"/scripts/{check_dependence.py,check_vocabularies.py,check_quotations.py} "$B"/scripts/
python3 - "$B/vocabularies/loss_mitigation_characteristic.csv" <<'PY'
import csv, io, sys
p = sys.argv[1]; raw = open(p, newline='', encoding='utf-8').read()
rows = list(csv.reader(io.StringIO(raw)))
o = io.StringIO(); csv.writer(o, lineterminator='\n').writerows(rows)
assert o.getvalue() == raw, "round-trip not byte-identical: stop"
i = rows[0].index('exemplar'); [r.pop(i) for r in rows]
o = io.StringIO(); csv.writer(o, lineterminator='\n').writerows(rows)
open(p, 'w', newline='', encoding='utf-8').write(o.getvalue()); print("exemplar dropped")
PY
cd "$B/sources"
KM="$Z/Kirshner and Molho - 1978 - The Dowry Fund and the Marriage Market in Early Quattrocento Florence.pdf"
M="$Z/Molho - 1994 - Marriage Alliance in Late Medieval Florence.pdf"
K="$Z/Kirshner - 2015 - Marriage, Dowry, and Citizenship in Late Medieval and Renaissance Italy.pdf"
qpdf --empty --pages "$KM" 1-36 -- kirshner-molho-1978_jmh50_pp403-438.pdf
pdftoppm -f 1 -l 1 -r 400 -gray "$KM" /tmp/km403
tesseract /tmp/km403-01.pgm kirshner-molho-1978_p403_ocr -l eng && rm /tmp/km403-01.pgm
qpdf --empty --pages "$M" 4-5,12,21 -- molho-1994_frontmatter_title-cip-contents-dates.pdf
qpdf --empty --pages "$M" 48-148  -- molho-1994_ch2-3_pp27-127.pdf
qpdf --empty --pages "$M" 372-381 -- molho-1994_app1-sources_pp351-360.pdf
qpdf --empty --pages "$M" 454-455 -- molho-1994_ms-sources-abbreviations_pp433-434.pdf
qpdf --empty --pages "$K" 3-6,223,247-248 -- kirshner-2015_frontmatter_title-copyright-contents-origpub-abbrev.pdf
qpdf --empty --pages "$K" 102-121,238-239,300-317 -- kirshner-2015_ch4_pp94-113_app4_pp230-231_notes_pp292-309.pdf
qpdf --empty --pages "$Z/Morrison et al. - LIFE CYCLE EVENTS IN 15TH CENTURY FLORENCE RECORDS OF THE.pdf" 1-6 -- morrison-kirshner-molho-1977_aje106_pp487-492.pdf
qpdf --empty --pages "$Z/Morrison et al. - 1985 - Epidemics in Renaissance Florence..pdf" 1-8 -- morrison-kirshner-molho-1985_ajph75_pp528-535.pdf
for f in *.pdf; do printf '%s %s\n' "$(pdfinfo "$f" | awk '/^Pages/{print $2}')" "$f"; done
```

Expected page counts: 36, 4, 101, 10, 2, 7, 40, 6, 8. The OCR file should hold about 500 words. **The OCR must be checked against the page image before any cell rests on p. 403**, and the README tells the coder so.

### 9.4 Absence check, before the coder is opened

```sh
cd "$B"
grep -rIlE "monte-delle-doti-(scheme|operator)|NOTES-monte|italian-archives-survey|european-archives-survey|WITHHELD — the coding chat|R5-[A-D]" . ; echo "text hits above: expect none"
for f in sources/*.pdf; do pdftotext "$f" - 2>/dev/null | grep -cE "monte-delle-doti-(scheme|operator)" ; done | sort | uniq -c   # expect only 0
ls -R "$B" | grep -iE "records|logbook|CHANGELOG|myfoamrepo|organizational" ; echo "expect nothing above"
python3 scripts/check_vocabularies.py && python3 scripts/check_dependence.py datasets/loss_mitigation_forms | tail -1 && python3 scripts/check_quotations.py | tail -1
shasum -a 256 README.md PRIORS-monte-delle-doti-2026-10-15.md sources/*
```

The check was run on a trial build in a scratch directory on 2026-10-15. It printed no text hit, nine zeros for the PDFs, and the three script lines quoted in §9.1. (A first version that searched for the bare word `withheld` hit one commenda re-coding note in `recodings.csv`, which uses the word about another batch, so the pattern was narrowed.)

### 9.5 Leaks that cannot be removed, disclosed to the coder

1. The `code-a-form` skill's description names "tontine" among example institutions. It states no value.
2. The bundle's `data.csv` and type vocabulary carry the tontine and widows'-fund rows, and the *avariz* rows' notes on orphans' marriage portions. That is house practice, not a prediction (N6).
3. Training knowledge. The priors template asks for the textbook account, clause by clause.

**Channel check: run on the prompt, the README and the priors template, against §10 and both loaded skills.** Method: a regex over all three files for every date in §10.1, every value predicted in §10.2, and the R5-C terms (`revert`, `refund`, `repaid`, `retain`, `Monte comune`, `public debt`, `official`, `account`, `ritratto`, `credit`, `cash`, `nun`, `vows`, `morte`, `diverted`, `surplus`, `commune`, `counterparty`, `eligib`, `categor`, `gabella`), each hit read in context.

**Changed after the read-back:**
- **Prompt, scope sentence.** The draft excluded "the commune's funded public debt itself and its other funds and instruments". "Its *other* funds" implies that the dowry fund was one of the debt's funds, which is the §5b finding and bears on `GV1` and `MC1`. It now reads: "the commune's public debt (the Monte comune) … Code no cell from evidence that concerns only those."
- **README, dating example.** The draft used `1432/3`, which pointed at the principal dated change in §10.1. It now uses `1466/7`.

**Hits kept, and why:**
- The priors template lists every characteristic's `allowed_values`, which are in the bundle's vocabulary anyway. Its hits on predicted values are the value set, not a prediction.
- The README carries Morrison et al. 1985's title, "Epidemics in Renaissance Florence". It is the source's own title and bears on `HZ1`. It is disclosed here, not removed.
- The prompt's sentence "The fund ran for over a century under changing legislation" is the minimum the split test needs. It names no date and no change. It is kept deliberately.

**Not found in any of the three files:** a date from §10.1 (other than the period's end, 1530, which is scope), any R5-C term outside the scope sentence, and any §10.2 prediction outside the template's value lists. The two skills, read against §10, carry only the generic characteristic codes and the word "tontine" in `code-a-form`'s description (item 1 above).

## 10. WITHHELD — the coding chat must never see this section

### 10.1 What the named passages say (R5-A to R5-D)

- **1425 (K&M 404, 406).** The Signoria's bill of 23 February 1425 founded the fund. "If the girl died before the term of the deposit expired (even if in the meantime she had married and consummated her marriage), or if she never married, **the deposit reverted to the commune**" (406). Molho 30: fathers were "invited to deposit with the officials of the funded public debt (Monte comune) 100 florins in cash for a term of either seven and a half or fifteen years".
- **1428 (K&M 407).** The model deposit was cut to 75 florins, with nominal yields of 13.48% (15 years) and 17.41% (7½ years). "The legislation of 1425 did not produce the desired results."
- **April 1433 (K&M 407–408).** The model deposit fell to 60 florins, and terms of 5, 7½, 11 and 15 years were offered. "Most important, the sum deposited into the Monte would now be **repaid to the father** of a young girl who died before the term of deposit had elapsed … one year and one day after the girl's death". Brothers came next, and "in case the dead girl was survived neither by her father nor by any brothers, the commune would retain the money" (408).
- **1436 (K&M 409).** The model deposit rose to 70 florins.
- **15 May 1437 (K&M 409).** Deposits were refunded if a girl took perpetual vows. *"tunc statim facta professione legitime dicta puella professa habeatur et reputetur tamquam vere mortua ad contenta dumtaxat in presenti provisione"* (409 n. 16).
- **1425 registers (K&M 409).** The founding law required the "fund's officials" to keep books and registers.
- **1440/1 (Molho 37).** Deposits in Monte credits were first invited in February 1439/40 and made mandatory in March 1440/1.
- **1443/4–mid-1440s (Molho 47).** Matured dowries were paid in monthly instalments, then in Monte comune credits at a discount.
- **1452/3 (Molho 52).** "For the first time, [legislators] distinguished categories of investors". Interest was withheld from private creditors but not from the Dowry Fund account (48).
- **1458–1463 (Molho 54–55).** Deposit sizes were scaled to Monte prices and repeatedly revised. A provision of February 1462/3 says the longest term, **"per cagione della morte"**, was of "greater utility" to the Fund (55). The eleven-year term was abolished in 1459.
- **1470–1477 (Molho 53).** The *ritratto* (a ceiling on the sum subscribed) was "provisionally set at 165,000 florins in 1470, was lowered to 100,000 florins in 1471/2, increased to 150,000 florins in 1475/6, and finally lowered to 100,000 florins in 1477". For *contadine* and *distrettuali*, payment of dowries was delayed one year after maturity. "Similar measures were applied to the restitution of capital for girls who died or beca[…]": the sentence was cut at the filter's length limit, and its end was not read (53).
- **1478 (Molho 71).** "Legislation set the cash portion at 20 percent of the Monte dowry's value."
- **1479 (Molho 55).** The five-year term was abolished.
- **1488/9–1503 (Molho 74–75).** Deposits were made wholly in Monte credits (1488/9), then had to be cashed in under the 1491 conversion; mixed credit and *paghe* deposits followed in 1502–1503.
- **1496 (Molho 77).** "The distinction between regular communal creditors and Dowry Fund creditors was now eliminated."
- **1498–1530/1 (Molho 76–78).** Three short-lived regimes ran from 1498 to 1530. A special gabella was put on depositors in January 1530/1, with fines subtracted from the capital returned to a dead girl's survivors (78).
- **Administration (R5-C).** Molho 31: *officiales et camerari montis*. Molho 37: the *creditum puellarum maritandarum*, serviced by buying Monte comune credits. Molho 49: 40,000 florins diverted "from its account to the city's military expenses", in the expectation that girls' deaths would produce a surplus. Molho 50: "difficult to separate the Dowry Fund accounts from those of the city's general expenditures". Molho 63: officials "could not easily resist pressure to divert funds assigned to the dowry account".

### 10.2 Predictions, to be scored against the coding

Confidence is this session's, in the prediction. "Basis" says whether the prediction rests on a passage read (§10.1) or on general knowledge, which is not evidence.

| char | prediction | conf. | basis |
|---|---|---|---|
| `MC1` | `allocation` (the commune as named counterparty, terms fixed by law); alternative `spreading` | low | read (Molho 30; K&M 406) |
| `MB1` | `territorial-subject` or `.NR`; **value-set strain expected**: eligibility runs on citizenship and fiscal status (households eligible to hold Monte credits) | low | partly read (Molho 61, counts only beyond) |
| `MB2` | `1`, or a **split proposal** across 1452/3–1470 | low | read (Molho 52–53) |
| `MB3` | `voluntary` | high | read ("invited", Molho 30) |
| `CN1` | `ex-ante-lump`, the census's **third** (after `shenhui_gu_alloc`, `tontine_en_1693`) | high | read |
| `CN2` | `proportional-to-stake`, or a value-set flag (the depositor chooses the sum) | low | general |
| `CN3` | `.NA` or `.NR` (paid up front) | low | general |
| `HZ1` | `mixed` (death covariate in epidemics; marriage idiosyncratic) | low | Morrison 1985's title; general |
| `HZ2` | `0` | low | general |
| `PY0` | `individual-indemnity`, with a **value-set flag**: a fixed sum on a life event fits neither indemnity nor draw | low | general |
| `PY1` | `life-event` (the fifth instance) | high | read |
| `PY2` | `.NA` (PY1 determines it) or `.NR` | medium | vocabulary |
| `PY3` | `1` (a fixed sum by schedule) | medium | read (Table 1 cited, K&M 408) |
| `LS1` | `.NR` | medium | general |
| `LS2` | `0` (the commune, not depositors, took any surplus) | low | read (Molho 49) |
| `LS3` | `0` | medium | general |
| `VF1` | `documentary` (consummation and the *confessio dotis*), the value's **second instance** | medium | ch. 4 title and Appendix 4 title |
| `VF2` | `loss-occurrence` | low | general |
| `GV1` | `external-administered` | high | read (Molho 30–31, 63) |
| `DR1` | `open-ended` | medium | general |
| `DR2` | `.NA` | medium | vocabulary |
| `RB1`–`RB4` | not coded, or `.NR`, on neighbours' practice; **`RB1` may be argued across 1433** | low | vocabulary |
| `PR1` | `1`, possibly `articulated` from the 1462/3 "per cagione della morte" provision | medium | read (Molho 55) |

**Row-level predictions:**
1. The coder identifies **April 1433** as the principal dated change, unprompted.
2. It runs the split test on 1433 and, on the vocabulary as written, **records it as a variant rather than proposing a split**. If it splits, the cell named will be `RB1` or `MC1`. Low.
3. It proposes a split, or flags drift, on **`MB2`** across 1452/3–1470. Low.
4. It finds the fund's administration to be the commune's, and flags (without being asked) that an organizational row would code the *Monte comune*. Medium.
5. It caps confidence at `medium` and declares N1 in its notes. High, since the prompt says so.
6. It measures Molho's offset from the file and notices nothing wrong. The prompt gives printed ranges, so there is nothing to notice. This is a control.
7. Its `.NR` count is highest on `loss-sharing` and `owner-shielding`. Medium.

## 11. Files written by this session (all in `records/`)

- `NOTES-monte-delle-doti-operator-2026-10-15.md`: this brief. **Never shipped.**
- `PRIORS-monte-delle-doti-2026-10-15.md`: the template. **Shipped.**
- `PROMPT-monte-delle-doti-2026-10-15.txt`: the kickoff prompt. It is pasted into the coding chat and is not in the bundle.
- `BUNDLE-README-monte-delle-doti-2026-10-15.md`: copied into the bundle as `README.md`.

**Order:**
1. MS commits these four files and the logbook 4 row.
2. MS builds the bundle (§9.3) and runs the absence check (§9.4).
3. MS opens the coding chat with the prompt. It fills the priors, prints their sha256, and **stops**.
4. MS commits the filled priors and confirms the hash.
5. Only then does the coder open a source.

## 12. Left for MS, not done here

- **Zotero `96G86SL5`, Extra:** replace "PAGE OFFSET: printed = pdf + 20" and "ch. 2 … = pdf 47–99" with **printed = pdf − 21; ch. 2 = pdf 48–100; ch. 3 = pdf 101–148; ch. 4 = pdf 149–201**.
- **Zotero `HXZ3FL7E`:**
  - pages 29–62 → **29–61**;
  - the container can lose its `metadata-unverified` flag, on the evidence of Kirshner 2015, p. 215.
- **`records/NOTES-monte-delle-doti-scheme-2026-10-15.tmp`:** an empty file, mtime 2026-10-14 15:04, left by part 1. Delete it, or check that it is ignored, before a `git add -A` sweeps it in. This session did not create it and has not removed it.
- **C2:** decide.
- **The loose duplicates and `ZL89FSGR`:** as §14 of part 1 left them.

## 13. This session's standing-table row

Filed in logbook 4, slug `monte-delle-doti-operator`.
