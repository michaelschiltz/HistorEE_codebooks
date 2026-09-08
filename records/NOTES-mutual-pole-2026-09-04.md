# The mutual pole as an entity question — forms-selection brief, 2026-09-04

**Operator session. Nothing coded, no row proposed, `data.csv` untouched, no `git` run.** Session slug proposed for the logbook 4 standing table: `mutual-pole-scheme` (see §7).

## 1. Why this batch, and why it is not the batch that failed on 2026-08-30

`organizational_forms` stands at **28 forms over 26 institutions, 643 cells**, with `fraterna` and `compagnia` merged. The census's own diagnostic gap has not moved since it was first stated on 2026-08-29: **the entity census contains no cooperative, while the loss census next door is 47 forms of overwhelmingly mutual institutions.** `FP1=mutual-provision` still has no instance.

The 2026-08-30 attempt to close it on `raiffeisen_kasse` and `schulze_delitzsch_verein` produced no rows because the library held nothing. The correction is not to find better German sources first. It is that **the mutual pole was already in the library under other names** — under *guild*, *confraternity*, *friendly society*, *avarız* — and had been read into `loss_mitigation_forms` while nobody asked it the entity questions. The 2026-08-30 commenda-family pass established the precedent and the machinery: a form coded in one census may be coded in the other on a different question set, with `cooccurrence_basis=same-institution` declared.

Three rows are proposed: **`avariz_vakfi`**, **`friendly_society_england`**, **`confraternita`**.

## 2. What the batch is aimed at

Eleven values have zero instances. Five are substantive and reachable; the rest are `P` grades on characteristics with few forms, plus `LR5=na`, which remains a defect rather than a gap (logbook 1; and see the 2026-08-30 recommendation that it be dropped or annotated as reserved-and-unused, still not actioned).

| target | why this batch reaches it | which row |
|---|---|---|
| `FP1=mutual-provision` | the census's flagship gap; all three rows are candidates | all three |
| `LR6=downside-only` | locator is **decision-maker**: an unpaid steward or *mütevelli* bearing loss without a share of gain | friendly society, avarız |
| `LR2=attenuated` | paid or externally appointed management against lay membership | friendly society, confraternita |
| `AP4=P` or `AP4=0` | see §3 — the sharpest pre-registered target in the batch | avarız |
| `TS4=1` | a body that can alter its own rules by internal decision; a registered society amending enrolled rules is the best candidate in the census | friendly society |

**`LR1=none` should be expected to miss, and for a reason worth recording in advance.** Its locator is `labour-party`. A mutual society has no labour party in the capital-labour sense, so the cell will most likely read `.NA` rather than `none`. If that is right, `LR1=none` is in the same position as `LR5=na` — **unreachable by coding rather than unfilled** — and should come off the zero-instance list on the same argument. The batch tests this; it does not assume it.

## 3. The pre-registered expectations

Written as falsifiable statements before any cell is opened, per `CHARACTER-CODING.md`.

1. **`avariz_vakfi` will separate from `waqf_khayri` on `FP1` and on little else.** If it separates on nothing but `FP1`, the row is a purpose variant of a coded form and the census has bought one value at the price of a row — the `waqf_ahli` objection, now tested rather than assumed. If it separates on `AP4`, `MG2` or `MG4` as well, it is a distinct form.
2. **`avariz_vakfi AP4` is the one cell that could break `AP4` open.** `AP4` currently holds two forms and a single value; it discriminates nothing. The mahalle endowment is the case where founder and beneficiary may be the same body — the quarter — and where a founder may have reserved administration. A reading of `P` or `0` gives `AP4` its first contrast. A reading of `1` leaves `AP4` a column that has never once varied, and that fact should then be written into the vocabulary beside the 2026-08-30 note.
3. **`friendly_society_england` will code `LP1=0`, `LP2=0` and `LP3=P`** — property vested in trustees, standing to sue only through them under statute. It is wanted as the **negative pole**: `begijnhof LP3=1` and `casa_san_giorgio LP3=P` mean little without a form that has the mutual purpose and none of the personality.
4. **The three rows will agree on `FP1` and disagree on everything in the `legal-personality` component.** If instead they agree across `LP1`–`LP3`, the batch has found that mutual purpose predicts entity architecture, which nothing in the census currently suggests.
5. **The `entity-shielding` component will stay the emptiest WP2 facet.** It was 0/3 on both forms of the 2026-08-29 batch and `AP2=0` reached only three forms after fraterna/compagnia. Nothing in these three sources is written to answer it.

## 4. Holdings — verified before the batch, not after

The 2026-08-29 rule applied. Every held PDF was opened and its text layer tested by extraction; page offsets were measured against printed folios visible in the extracted text, never inferred from a page count.

**No OCR bottleneck in this batch.** All eighteen files tested carry working text layers at 1,800–3,500 characters per page. This is the opposite of the fraterna/compagnia situation and should shorten the pass considerably.

### Offsets measured

| item | file | pp | printed = | measured at |
|---|---|---|---|---|
| Kıvrım 2019 `GSC5PEAH` | avarız, Ayntab | 16 | **PDF + 33** | PDF 10 = 43 (one point only — confirm by eye) |
| Kars 2020 `GAZN2XVN` | avarız, Istanbul court records | 28 | **PDF + 159** | PDF 10 = 169, PDF 20 = 179 |
| Küçük 2025 `NAQKKKN7` | avarız accounting, Kastamonu | 37 | **PDF + 146** | PDF 10 = 156, PDF 20 = 166 |
| Gürsoy 2019 `VM4K33C4` | cash waqf registers 1491–1828 | 32 | **PDF + 94** | PDF 10 = 104, 20 = 114, 30 = 124 |
| Gazzini 2020 `D6QT9WDX` | **whole Hellwege volume**, 289 pp | 289 | **PDF − 1** | four points, PDF 20/30/40/60 |
| Schewe 2000 `3DUN35AT` | **whole book**, 345 pp | 345 | **PDF − 1** | five points |
| van Leeuwen 2016 `9X5DN2VN` | chapter offprint, printed 17-82 | 66 | **PDF + 16** | five points |

**RETRACTED, and the retraction is instructive.** This section first reported that Küçük carried a second page sequence, on a bare `7` extracted from PDF 30. Re-measured page by page in the Zotero pass later the same day, **the offset is constant at `+146` across all 37 pages**: every odd PDF page carries its folio and they all agree. The stray small numbers — `11`, `2`, `7`, `5`, `4` and a `1851` — come from **even** pages only and are table numbers and account figures sitting where a folio would be. The false alarm was produced by sampling every tenth page and happening to land on versos. **Sample consecutively before declaring a break.** The one genuine non-constant offset in the library is Sapori 1978, and §12 records what became of it.

### Term sweep, run across orthographic variants

Per the 2026-08-31 rule: a presence test is not evidence of absence until it has been run across variants, and a sweep must state which variants it tried.

**`avariz_vakfi` — richly answerable.** Across the four Turkish items: *mütevelli* 36/45/40/17, *vakfiye* 2/3/5/–, *vâkıf* 2/4/–/19, *kadı* 8/13/9/7, *muhasebe* 1/4/12/73, *nema* –/4/8/31, *tevliyet* 1/–/–/2, *para vakfı* 4/2/3/15, *istiğlal*, *murabaha*, *ferağ* all present. Administrator, deed, court, accounts, return, office of administration and alienation are all on the page. `MG2`, `MG4`, `LP2`, `TS1`, `TS3`, `FP4`, `AP4` and the `CI` cluster are all in reach from held material.

**`confraternita` — answerable on personality, and this was not obvious.** Gazzini 2020 in the Hellwege volume carries *universitas* 4, *legal personality* 3, *corporate* 24, *persona* 17, *property* 17, *statut\** 334; Gazzini's Italian chapter `MBFIBZNA` carries *giuridic\** 7, *universitas* 2, *ente* 40, *patrimoni\** 7. **On this evidence the "confraternity as universitas" sweep was not needed**, which is the answer the sweep would have given at the cost of a search.

**`friendly_society_england` — not answerable, and this is the batch's first finding.** Across Rusnock & Dietz 2012, Prom 2010 and Wallace 2000 combined: **`trustee` appears once.** *Registrar* twice, *incorporat\** three times across three articles, *Friendly Societies Act* not once, *legal personality* not once. The three held articles are about sickness definitions, discipline and charitable sentiment. **The row cannot be coded from held material, and would have produced an all-`.NR` `legal-personality` block had the batch been run without this check.** That is the 2026-08-30 credit-cooperative failure caught one step earlier.

### Stubs — items with no attachment at all

`9ZVWGV6W` **Cordery, *British Friendly Societies, 1750–1914*** (the standard monograph) · `4JTWXSNP` Broten 2012 · `UNWASN6P` **Frank, *Bruderschaften als Bank*** (the best confraternity-as-financial-body source in the library) · `EPDJN54N` Bos 2017 · `H9HVG7C8` Heirbaut 2018 · `5784B4VQ` van Steensel 2014. `57I7DHIC` Lanaro 1998 is present but as `.epub`.

### An infrastructure finding

**`~/Zotero` on `macbook-air-local` is not the live library.** It holds 1,134 storage folders and a `zotero.sqlite` with 13,389 items, and **none of the attachment keys of the census's own items resolve in it**. The live attachments are ZotMoov-managed under `Library/CloudStorage/GoogleDrive-…/My Drive/Zotero/logs/ZotMoov` (409 files). The 2026-08-31 note that "I cannot reach Zotero's storage directly" is now **out of date**: with that folder granted, `pdftotext`, `pdfinfo`, `qpdf` and **`tesseract`** are all present on the device, so bulk text-layer testing, offset measurement and OCR can be done in one sweep on your machine and no longer require files to be supplied one at a time. The four PDFs re-supplied by hand on 2026-08-31 could have been handled this way.

## 5. Undermind — two searches, both completed

Workspace: *HistorEE — entity and corporate forms census*.

### 5.1 Friendly societies — the search answered a different question than the one asked, and the answer is more useful

The sweep returned **no modern doctrinal legal history at all.** The seventeen results are led by nineteenth- and early-twentieth-century practitioner treatises, law reports and the statutes themselves: Fuller, *The law relating to friendly societies* (two editions), Diprose & Gammon's *Reports of Law Cases Affecting Friendly Societies*, Davis on the 1875 Act read against the Trade Unions Act 1871, Holdsworth's annotated 1875 Act, Pratt, and the consolidating Act of 1829 itself. **The legal status of the friendly society has apparently not been written as history; it exists as practitioner literature.**

Two consequences. First, this is **cheap**: every one of those is out of copyright and on Archive.org, HathiTrust or Google Books, so the acquisition is a download rather than a purchase — but it is a download Undermind cannot perform (every item returned `PDF ✗`), so it is a manual step. Second, coding from a practitioner treatise sets `articulation` differently from coding from a historian: Fuller states the law as a practitioner, which is **actor's-category evidence of a legal position**, not an analyst's reconstruction. That is a better epistemic position than the census usually enjoys and should be said in the row's notes.

Three modern items are worth more than their rank suggests:

- **Morley 2017, *The Common Law Corporation: The Power of the Trust in Anglo-American Business History*** — the trust supplying property-holding, continuity and creditor protection without incorporation. **This is a census-level source, not a friendly-society source.** It bears on `LP1`/`LP2`/`AP1`/`AP2` for every unincorporated form the census holds or will hold, and it is the natural doctrinal counterweight to Hansmann, Kraakman & Squire, who are already the census's spine on entity shielding.
- **McC. 1949, *Trusts for Unincorporated Associations. Legal Entity and Perpetuity*** (*Virginia Law Review*) — frames legal entity and perpetuity together, which is exactly the `LP` × `TS1` pairing.
- **Logan 2003**, thesis on the Ancient Order of Foresters — bears on whether a **lodge is a body separate from its order**. That is the `begijnhof` coding-unit problem in another costume (a court beguinage being a federation of legally separate sub-institutions), and it decides whether `friendly_society_england` is one row or two.

Also: **McIlroy 1998 on *Hornby v. Close*** — the case that held trade unions were not legal entities — is the nearest thing to a decided-case answer on the whole class.

### 5.2 Avarız vakfı — the question was answered affirmatively

**Yes: the form is documentable outside the Turkish literature, and the two most useful items go straight at the coding unit.**

- **Canbakal 2004, *Some Questions on the Legal Identity of Neighborhoods in the Ottoman Empire*** — whether the *mahalle* itself is a legal person. This decides `avariz_vakfi`'s coding unit before a cell is opened: is the endowment the entity, or is the quarter the entity and the endowment its property? DOI prefix **`10.3406` — Persée**, so per logbook 5 it is freely available at the repository and Zotero's OA fetcher will report otherwise. Do not trust the fetcher on this one.
- **Cohen 1996, *Communal Legal Entities in a Muslim Setting: Theory and Practice*** (*Islamic Law and Society*) — communal legal personality in Islamic law, directly on `LP1`.
- **Wilkins 2009, *Forging Urban Solidarities*** (Aleppo, 1640–1700) — an English-language monograph on Ottoman urban collective institutions and the avarız assessment.
- **Mandaville 1979, *Usurious Piety: The Cash Waqf Controversy in the Ottoman Empire*** and **Çizakça 1995, *Cash Waqfs of Bursa, 1555–1823*** — the legal controversy and the classic empirical series. Çizakça is already cited in logbook 4 on `avariz_vakfi_kirkcesme`, so the loss census and the entity census would rest on a shared source at exactly one point; declare it.
- **Aslan 2025, *Osmanlı Toplumunda Avârız Vakıfları ve İşlevi*** — a general analytical treatment rather than a single-town study, and Undermind reports a PDF available.

## 6. Co-occurrence, which must be declared before the rows are written

All three institutions are already in `loss_mitigation_forms`, and the declaration is not optional.

| new entity row | loss-census row(s) | basis |
|---|---|---|
| `avariz_vakfi` | `avariz_vakfi_kirkcesme`, `avariz_fund` | `same-institution` |
| `friendly_society_england` | `friendly_society_england`, `friendly_society_female_england` | `same-institution` |
| `confraternita` | `confraternity_fund_it` | `same-institution` |

**The shared-source risk is real and is not the same as the co-occurrence.** Küçük 2025 is the source behind `avariz_vakfi_kirkcesme`'s accounting cells and is also the best entity source for the new row. Where a cell in the new row and a cell in the old row rest on the same page of the same author, the two censuses are not independent evidence and no cross-census agreement between them counts as a finding. This is the `mudaraba` problem in a new place and should be stated in the row header, not discovered afterwards.

## 7. Blinding

The vault has not argued this pole. Counts across `notes/`, `mynotes/` and `mocs/`: *friendly societ\** **0 files**, *scuola* **0**, *collegium* **0**, *guild box* **0**, *genossenschaft* **0**, *raiffeisen* **0**, *mont-de-piété* **0**; *confraternit\** 3, *avariz* 2, *widows* 4. **This is the first entity-side batch in the project where the blind is genuinely available and the sources are also cheap** — the 2026-08-29 observation that blindness and cheapness are inversely ordered does not hold here, and the reason is that the material entered the library through the loss census, which the entity-side vault notes were not written against.

Accordingly: **build a blind bundle.**

```
python scripts/make_blind_bundle.py \
  --withhold-dates 2026-09-04 \
  --withhold-sessions shareholding-and-pooling-scheme,entity-census-scheme,entity-questions-commenda-family,fraterna-compagnia-acquisition,mutual-pole-scheme
```

Verify before handing off, as on 2026-08-29: `proposed-of/` and `CHANGELOG.md` absent; the withheld notes removed **and dereferenced** from the MOC, the Foam link-reference definitions and inline wikilinks; `validate_vault.py` clean; no surviving mention of any withheld title; and — because this dataset has been bitten before — that `build_views.py --check` actually produces a non-empty WP1 view for `organizational_forms`.

**Withheld from the coding session deliberately, and not to be volunteered:** that `FP1=mutual-provision` is the target and has no instance; the `AP4` expectation in §3(2); the prediction that `friendly_society_england` codes `LP1=0`/`LP2=0`/`LP3=P`; and the argument in §2 that `LR1=none` may be locator-unreachable. The last of these especially — if the coder reaches `.NA` on `LR1` independently, that is a result; if told to expect it, it is nothing.

### Proposed logbook 4 standing-table row

| slug | session | what it spent |
|---|---|---|
| `mutual-pole-scheme` | 2026-09-04, operator | Read the `MOC - Entity-shielding and corporate forms` note list — 33 note **titles** — as `entity-census-scheme` did, and re-spent it on the same terms. Read the whole live `organizational_forms` `data.csv` (form and cell counts, per-form cell counts), the whole `organizational_form_characteristic.csv` including the `AP4`, `LR1`, `LR2`, `LR6`, `MG4`, `TS4` and `FP1` definitions and locators, the `organizational_form_type.csv` roster, the loss-census form roster, and logbook 4's standing-slug section. Computed and recorded the full zero-instance and one-instance value tables. Prejudices any later blind coding of these three forms on every characteristic, and of `AP4`, `LR1` and `FP1` generally. Also ran **term-count** greps over the vault (counts only, no titles opened, no bodies read) for eighteen mutual-pole terms; recorded because a count is weak evidence about a vault but is not nothing. Brief at `proposed-of/NOTES-mutual-pole-2026-09-04.md`. |

## 8. Acquisition list, ranked, obtainability checked first

**Tier 1 — required before `friendly_society_england` can be coded at all.**

1. **Fuller, *The law relating to friendly societies*** (either edition) — public domain; Archive.org / HathiTrust.
2. **Diprose & Gammon, *Reports of Law Cases Affecting Friendly Societies*** — public domain; the decided cases on trustees, officers and dissolution.
3. **Holdsworth**, annotated Friendly Societies Act 1875, and the **1829 consolidating Act** — public domain; the statutory text itself.
4. **Morley 2017, *The Common Law Corporation*** — not public domain; a census-level source, worth acquiring whether or not this batch runs.

**Tier 2 — would decide open questions.**

5. **Canbakal 2004** — free at Persée (`10.3406/ANATM.2004.985`); decides the avarız coding unit.
6. **Cohen 1996** (`10.1163/1568519962599186`) and **Mandaville 1979** (`10.1017/S0020743800000118`) — `LP1` and the cash-waqf legality question.
7. **Çizakça 1995** (`10.1163/1568520952600407`) — already load-bearing in the loss census; acquire the item properly rather than citing it twice from a quotation.
8. **Logan 2003** — the lodge-versus-order question, i.e. whether the friendly society is one row or two.
9. **Cordery 2003** `9ZVWGV6W` and **Frank, *Bruderschaften als Bank*** `UNWASN6P` — both already **in Zotero as stubs**; getting a PDF for each is the cheapest single improvement to the batch.
10. **Aslan 2025** (`10.7827/turkishstudies.82613`) and **Durmuş 2022** — Undermind reports PDFs available for both.

**Not now.** McC. 1949, Fisher 1970, Edwards 1999, Hardwick, Pratt, McIlroy 1998 — useful, none of them blocking.

## 9. What was not done, and what is open

- **Nothing coded. No row proposed. `data.csv` not edited. No `git` run.** Committing remains MS's.
- **The `LR5=na` recommendation of 2026-08-30 is still not actioned** — drop the literal or annotate it reserved-and-unused. `LR1=none` may need the same treatment; §2 says why and the batch tests it.
- **The Sapori 1978 offset break at PDF 74 appears never to have reached the Zotero item.** Nor have the four stale `OCR REQUIRED` / `REPLACE THE ATTACHMENT` notes on Lane, Hunt, English and Sapori, nor the replacement of the 77-page English attachment with the 156-page one. These are a Zotero session, not a coding session, and they are now cheap to do from the device.
- **`confraternita` has no settled type code, period or tradition.** Italian *confraternita* and German *Bruderschaft* may not be one form; Klieber's Salzburg material runs 1600–1950 against Gazzini's medieval Italian. Decide the row's scope before coding it, or the row will be a Sereno case by construction.
- **The umbrella boundary questions remain unsettled**: `ie`, `piaohao`, `kabu_nakama`.
- **`maona_chios_1347`, the `voc_1602`/`voc_1612` thinness, and `casa_san_giorgio LP3`** are all still open from 2026-08-29; Castelein 2013 `SFJF4V7Z` is acquired and unread.

## 10. Two repository findings, independent of this batch

Both were turned up by running the pre-merge check sequence exactly as `CONTRIBUTING.md` and `CLAUDE.md` prescribe it. Both are one-line fixes and **no fix is proposed here** — `scripts/` is yours.

### 10.1 `check_dependence.py` exits 0 on an argument it does not understand

The script takes a **dataset directory path positionally** — `python scripts/check_dependence.py datasets/loss_mitigation_forms`, with `organizational_forms` as the default when no argument is given. It has no `argparse`. Any argument it cannot map to a registered vocabulary falls into this branch:

```
print(f"no characteristic vocabulary registered for {name!r}; nothing to check")
return 0
```

So `check_dependence.py --dataset organizational_forms` prints *"no characteristic vocabulary registered for '--dataset'; nothing to check"* and **exits 0 having checked nothing**. So does `--help`. So does any typo, and so does `datasets/organizational_forms/data.csv` — the file rather than its directory, which is the natural thing to type.

This matters because **`build_views.py` and `build_codebook.py` both take `--dataset`**, so the flag form is the one a person or an assistant will reach for by analogy, and it is the form that silently passes. It is the same failure shape as the 2026-08-30 finding that `build_views.py` produced an empty but plausible view for this dataset: a check that reports success without having run. **The runs reported as "`check_dependence` 0 problems" on 2026-08-30 and 2026-08-31 should be repeated in the correct form before they are relied on.**

Run correctly this session, both datasets are clean: `dependence problems: 0` for `organizational_forms` (default, no argument) and for `datasets/loss_mitigation_forms`. Suggested fix: return non-zero from the unregistered branch, and name the accepted argument in the message.

### 10.2 `build_views.py --check` verifies one view, not the views directory

`--check` compares the **single** view that the current `--dataset`/`--component`/`--format` arguments resolve to against its file on disk. Bare `python scripts/build_views.py --check` therefore checks `views/loss_mitigation_forms--risk-pooling.md` and prints `current`, and **the nine `views/organizational_forms--*.md` files are not looked at.** They can all be stale and the gate passes.

There is a second edge, met immediately: for `organizational_forms` a component check also needs `--mechanism all`, because the dataset has no mechanism characteristic and the default is not `all`. Without it every component returns an error message rather than a check result — which is a loud failure, not a silent one, but it means the nine views cannot be checked by any single documented command.

Swept by hand this session — nine components, each with `--dataset organizational_forms --component <c> --mechanism all --check` — **all nine are current.** The tree is fine; the gate is not. Suggested fix: with `--check` and no `--component`, walk `views/` and check every file that the current dataset can generate; this is also the CI step that the 2026-08-30 note called for and left unwritten.

**Bearing on the blind bundle:** the handoff verification in §7 should sweep all nine views by hand until this is fixed, rather than trusting a bare `--check`.

## 11. The bundle was built, and building it found that the blind does not hold

Bundle at `~/GitHub/_blind-mutual-pole-2026-09-04`, manifest beside it. Verified: `CHANGELOG.md` absent, `proposed*/` absent, all three withheld vault notes removed and dereferenced, `validate_vault.py` clean at **216 notes** (219 less the three), and — swept by hand, per §10.2 — all nine `organizational_forms` views current.

Then the surviving-title check found one hit, and following it up produced the session's most consequential result.

### 11.1 The defect

**`make_blind_bundle.py` scrubs the vault. It does not read the logbooks.** And on 2026-08-30 the forms-selection brief of 2026-08-29 was preserved verbatim into `logbook/2`, because it cross-referenced itself six times and splitting it would have broken every reference. That was the right call for the document. Its consequence was not foreseen.

`logbook/2`, §2, in the bundle as the script produced it:

> **Thirteen values in `organizational_forms` have no instance.** … `TS4` `1` — purpose mutable … `LR1` `none` … `LR2` `attenuated` … `LR6` `downside-only` … `FP1` **`mutual-provision`** …
>
> **`FP1=mutual-provision` is the finding.** … *The entity census contains no cooperative.* Meanwhile the loss census is 47 forms of overwhelmingly mutual institutions — kō, guild chests, tontines, **friendly societies, avarız funds** — none of which has ever been coded as an entity.

That is this batch's entire target list, two of its three rows named, and the value it is meant to fill set in bold — **in a tracked file the coding protocol requires the coder to read.** `logbook/4` then adds that a previous batch was selected to fill `FP1=mutual-provision` and failed to.

**So the blind, as the script builds it, was worth nothing for any zero-instance target.** Not for this batch and not for any future one.

### 11.2 What this does and does not do to the record

**It does not touch the 2026-08-29 `begijnhof`/`partenrederij` result.** That brief was pasted into `logbook/2` on 2026-08-30, after those rows were coded; `logbook/4` records that the brief was not read until afterwards, and that is still true. The damage is prospective, not retrospective.

**It is a general defect, not a fact about this batch.** Any operator brief preserved into a tracked logbook converts a spent blind into a permanently spent one for every later session, because the only scrubber the project has does not look there. The vault has a `source-session` field and a machine that reads it; the logbooks have neither.

### 11.3 What was done about it, which is a stopgap

Three passages were excised **from the bundle copy only** and replaced with a visible banner naming what was withheld and why. `logbook/2` 149–168 and 194–200, `logbook/4` 182–189. Nothing in the tracked repository was altered. The excision is recorded in the bundle manifest.

**A visible hole is right and a silent one would not be.** The coder is told that a passage stating targets has been withheld, which is honest and is also the vault scrubber's own convention; leaving an unexplained gap invites the coder to reconstruct it.

### 11.4 What is still disclosed, and the distinction that matters

`mutual-provision`, `attenuated` and `downside-only` remain in `organizational_form_characteristic.csv` as allowed values, and the views show which values the matrix holds. **A coder with the matrix can always compute the zero-instance set**, and no bundle short of withholding the vocabulary can prevent it.

So the blind this bundle protects is narrower than §7 assumed, and §7's withholding list should be read accordingly: **what is withheld is not the computable fact but the instruction** — that these values are targets, that this batch was selected to fill them, and which form was expected to supply which. The coding session should be told this explicitly. A coder who works out unaided that `FP1` has no `mutual-provision` instance and codes toward it has done something quite different from a coder who was told to.

### 11.5 For MS

1. **A repair to `make_blind_bundle.py` is not proposed here** — `scripts/` is yours, and §10 already carries two script findings. But the shape is clear: the logbooks need something the scrubber can read. A fenced marker around preserved briefs, or a `withheld-if-session:` line on the block, would let one pass over `logbook/` do what the vault pass already does.
2. **Until then, every bundle needs the hand pass**, and that is a step the manifest cannot check for itself.
3. **The wider question is whether preserving operator briefs into the logbooks is right at all.** It was done for referential integrity and it is good for the deposit. It is corrosive to the blind. The two goods are in genuine conflict and the resolution is above this session's pay grade.

## 12. The Zotero pass, 2026-09-04 — sixteen items corrected, and one live citation query

Run after the brief above, on MS's instruction. **Nothing coded; `data.csv` still untouched.** The library is a working instrument, not the deposit, so it is edited in place; every change below is recorded here because the Extra fields are not under version control and this note is the only audit trail.

### 12.1 All four "OCR REQUIRED" items were already fixed

`BKP6IHET` Lane · `Q33XD6ZQ` Hunt · `9E49DMEK` English · `3BCUQHDF` Sapori. Every one of them carried an `Action: OCR REQUIRED` or `REPLACE THE ATTACHMENT` instruction dated 2026-08-31. **All four instructions had been carried out and none of the notes said so.** Verified against the files themselves: Lane 19 pp / 58,670 chars, Hunt 303 pp / 758,239, English **156 pp** / 353,427, Sapori 120 pp / 197,541. Two items additionally carried a `STUB: metadata only, no PDF` line that was false when written.

The English attachment question raised on 2026-08-31 is **closed**: the item holds the complete 156-page copy. The 77-page image-only fragment still sits in the ZotMoov folder under the same name without the trailing ` 1`, extracts zero characters, and is recorded on the item as not-to-be-reattached.

**The general lesson is about instruction notes, not about OCR.** A note that says *do this* becomes a lie the moment it is obeyed, and nothing in the workflow retires it. Four such notes survived four days and would have sent the next session to re-acquire files it already had. Where a note records a fact (an offset, a term count) it stays true; where it records an action it needs a closing entry. Every correction written today is phrased as a dated finding with its measurement, and where an instruction was withdrawn it says so explicitly rather than being deleted.

### 12.2 Offsets re-measured, and mostly on an order of magnitude more evidence

| item | before | after |
|---|---|---|
| Lane 1944 `BKP6IHET` | `+177`, **1 point** | `+177`, **12 points** |
| Hunt 1994 `Q33XD6ZQ` | `−12`, 2 points | `−12`, **9 points**, plus a facing-page check |
| Sapori 1978 `3BCUQHDF` | `−6` flat, 4 points | **`−6` to PDF 73, `−4` from PDF 74**, 62 points |
| Kıvrım 2019 `GSC5PEAH` | `+33`, 1 point | `+33`, **15 consecutive** |
| Küçük 2025 `NAQKKKN7` | `+146`, break suspected | `+146` **constant**, whole article; break retracted |
| Gürsoy 2019 `VM4K33C4` | — | `+94`, 3 points |
| Kars 2020 `GAZN2XVN` | — | `+159`, 2 points |
| Gazzini 2020 `D6QT9WDX` | — | `−1` volume-wide; **chapter located at PDF 166–193** |
| Gazzini 2020 `MBFIBZNA` | — | `+71`, 9 points |
| Klieber 2001 `SR4E4QM7` | — | `+33`, 21 points |
| Allen 2022 `NDNTDAI2` | — | `+209`, 37 consecutive |
| Rusnock & Dietz 2012 `464UFQK7` | — | `+58`, 13 points |
| Prom 2010 `GEUE49NE` | — | `+887`, 20 consecutive |
| Wallace 2000 `TP2UBGPR` | — | `+52`, 19 consecutive |
| Schewe 2000 `3DUN35AT` | — | `−1`, 5 points |
| van Leeuwen 2016 `9X5DN2VN` | — | `+16`, 5 points; **chapter offprint, not a container** |

### 12.3 The Sapori break, bounded — and a citation it puts in question

The 2026-08-31 pass measured Sapori at four points and got a flat `−6`. **All four fell before the break.** Measured across the whole book at 62 points, the offset is `−6` through PDF 73 and `−4` from PDF 74: the folios run `… LXVI, LXVII, LXX, LXXI …`, so **LXVIII and LXIX are absent from the file** at a plate opening.

Two consequences, both now on the item.

**(a) The 2026-08-31 content-check misplaced a passage, and misattributed another.** It recorded the Tommaso Portinari passage at *"printed LXXIII (PDF 79)"* and said the `L'evoluzione della compagnia` / *responsabilità illimitata e solidale* text was on the same page. The PDF page was right and the folio was two too low — **PDF 79 is LXXV** — and the liability passage is not there at all: it is on **PDF 50 = XLIV**, the *corpo di compagnia* page the same note had already identified. `data.csv` `OF-0641` (`compagnia CF1`) cites LXXV and is correct.

**(b) An open query on `OF-0627`, and it should go to MS not to a coder.** `compagnia LR1 = unlimited-joint`, described in its own note as *the best-evidenced cell on the row*, cites `Sapori 1978, XXXVI, XLIV, XCIII`. XXXVI (PDF 42) and XLIV (PDF 50) are confirmed to carry *responsabilità illimitata e solidale*. A sweep of PDF 40–120 finds that wording on **three pages only — 42, 50 and 96** — and PDF 96 is **XCII**, not XCIII. **The third locator looks one folio high.** The likely cause is on the item too: PDF 96's folio extracts as `XClil`, and reading that string as XCIII rather than XCII is the obvious slip. **Not changed.** Check it against the page image and amend the cell if confirmed.

### 12.4 A third OCR failure mode, and the family they belong to

Hunt's **verso** running heads extract with letters for digits: `2o6` for 206, `2o8` for 208, `2io` for 210. A search for a verso page number as digits returns nothing. Sapori's Roman folios mangle the same way (`XClil` for XCII).

Put beside the 2026-08-31 finding that *sopracorpo* is absent because the term is *sopraccorpo*, the project now has three ways a presence test lies:

1. **orthographic variance** — the term is spelled otherwise (*sopracorpo* / *sopraccorpo* / *corpo di compagnia*);
2. **character substitution in OCR** — the string is there but not in the characters searched (`2o6`, `XClil`);
3. **sampling artefact** — a real regularity is missed, or a false one invented, by sampling at a stride that aligns with recto/verso (§4's retracted Küçük break).

Each is now recorded on the item where it was found. The standing rule from 2026-08-31 — *state which variants a sweep tried* — should be extended: **state which variants, which character substitutions, and at what stride.**

### 12.5 The friendly-society negative, written onto the items

`464UFQK7`, `GEUE49NE` and `TP2UBGPR` are each tagged `entity-questions-not-supported` and carry the joint finding: across all three, **`trustee` appears once**, `Friendly Societies Act` and `legal personality` not at all. Wallace is the least negative — the Rose Act and quarter-sessions enrolment are mentioned, in passing, in a literary reading. `9ZVWGV6W` Cordery and `UNWASN6P` Frank carry acquisition notes saying what each would and would not close; `4JTWXSNP` Broten carries a note saying it would close nothing, being actuarial.

**`NDNTDAI2` Allen 2022 is flagged as the British alternative.** *Corporate Charity for 'the House'* on the Edinburgh craft incorporations' pensions and widows' fund is nearer the entity questions than any of the English friendly-society items, it is held and readable, and if `friendly_society_england` stays blocked it is the row to code instead. It was **not** swept for entity terms today; do that first. Note also logbook 4's standing flag that `widows_fund_scotland`'s `PR1=1` rests on a `[verify]` and is the first candidate for a re-read against the source — one pass could discharge both.

### 12.6 Errors made in this pass

- **The Küçük page-break, invented and retracted within the hour.** §4 as first written asserted a second page sequence. It was a sampling artefact. Corrected in §4, and the retraction is written onto the item rather than quietly dropped.
- **One item's `Extra` was replaced without being read first.** `4JTWXSNP` Broten lost two metadata lines (its citation key and a Semantic Scholar provenance note). Caught immediately and **restored in full** from the update tool's own before/after echo, so nothing was lost. The other items written without a prior read — `NDNTDAI2`, `9ZVWGV6W`, `UNWASN6P` — had empty `Extra` fields, confirmed from the same echo. **Read before replace. The tool replaces the whole field.**

### 12.7 Still to do in the library

- **`HistorEE — mutual pole (entity questions)`** was created (key `6CCV6QAK`) and **the 18 items are not yet filed into it** — the collection was not visible to the read path until Zotero synced.
- **Duplicate attachments to prune:** `VM4K33C4` carries four, two of them imported files with an identical filename; `GAZN2XVN` and `NAQKKKN7` carry three each. All duplicates of one file.
- **`~/Zotero` on the device is a stale second profile** — 1,134 storage folders, a `zotero.sqlite` with 13,389 items, and not one of the census's attachment keys resolving in it. The live attachments are ZotMoov'd to Google Drive. Worth deciding whether the stale profile should exist at all; at minimum nobody should point a tool at it expecting the live library.

## 13. Cordery and Broten arrived, and the batch narrowed to two forms

MS supplied both PDFs on 2026-09-04. Both verified the same day: **Cordery 244 pp / 607,682 chars, Broten 67 pp / 109,942 chars**, working text layers, no OCR needed. Both items' `Extra` fields rewritten; the `NO ATTACHMENT` and `acquisition-wanted` notes withdrawn.

### 13.1 Cordery does not unblock the row, and the sweep said so in advance

**What he supplies, in quantity:** the statutory chronology and the registration regime — `registrar` 88, `Friendly Societies Act` 7, `1793` 17, `1829` 16, `1834` 18, `1846` 12, `1875` 38, `enrol*` 42, `justices` 8, `certif*` 13, `incorporat*` 9, `corporate` 8, `corporation` 7, `dissolution` 2, `industrial and provident` 2, `Hornby` 1. And the row-splitting question: `lodge` 88, `affiliated order` 73, `Oddfellow*` 167, `Forester*` 66.

**What he does not supply:** `trustee` **1**. `legal personality` **0**. `unincorporated` **0**. `trusts` **0**. `act of parliament` **0**.

**`LP2` is the cell the row is chiefly wanted for** — whether the society held property in its own name or only through trustees, as the negative pole against `begijnhof LP3=1` — and Cordery does not answer it. §5.1's summary of the Undermind result predicted exactly this: he maps societies, orders and lodges as governance and social structures rather than as legally distinct entities. **A prediction made before the file arrived and confirmed on the file.**

Broten came out as predicted too, and more starkly: `trustee`, `trusts`, `incorporat*`, `unincorporated`, `corporate`, `corporation`, `property`, `statute`, `treasurer`, `embezzl*`, `perpetu*`, `legal personality`, `quarter session`, `justices`, `enrol*` — **all absent**. Actuarial throughout. Its one entity-side use is as a second witness on lodges.

### 13.2 The batch is now two forms

**`avariz_vakfi` + `confraternita`, coded blind. `friendly_society_england` deferred to a second batch.** MS's decision, and it is the decision the 2026-08-30 credit-cooperative failure argues for: a row whose whole diagnostic value sits in its `legal-personality` block should not be coded while that block would be all-`.NR`. The `FP1` target is reachable from either remaining row, so the batch still does its main work.

### 13.3 The Archive.org sweep — the row goes from unsourceable to over-sourced

Every Tier 1 item is free, public-domain and carries a full OCR text layer. Identifiers verified against item metadata; none is access-restricted.

| item | Archive.org identifier | notes |
|---|---|---|
| **Fuller, *The Law of Friendly Societies* (1898)** | `lawoffriendlysoc0000fbad` | 282 pp; PDF + EPUB + OCR text |
| Fuller, *Friendly Societies and Industrial & Provident Societies* (1910) | `friendlysocietie0000fran` | the later edition |
| **Diprose & Gammon, *Reports of Law Cases Affecting Friendly Societies* (1897)** | `cu31924017177787` | 669 pp; the decided cases; Cornell copy |
| **Holdsworth, *The Friendly Societies Act, 1875, with Explanatory Introduction and Notes*** | `friendlysocieti00holdgoog` | the annotated statute |
| Pratt, *The Law Relating to Friendly Societies* (1867) | `lawrelatingtofr00pratgoog` | pre-1875 regime |
| Tamlyn, *A Digest of the Laws of Friendly Societies and Savings Banks* (1827) | `adigestlawsfrie00tamlgoog` | **pre-1829**, so the regime before consolidation |
| Wright, *A Dialogue … wherein the Act 10 Geo. IV* (1830) | `adialoguebetwee00wriggoog` | contemporary discussion of the 1829 Act |
| White, *A Handy Book on the Law of Friendly, Industrial and Provident, Building, and Loan Societies* (1865) | `ahandybookonlaw00whitgoog` | comparative across mutual forms |
| Royal Commission on Friendly and Benefit Building Societies, First Report (1871) | `b21365477` | the official inquiry |
| Hardwick (1859) | `historypresentpo00hard` | |

**And the one that was not on anybody's list, which may be the most useful of the lot:**

**Daly, *Club Law and the Law of UNREGISTERED Friendly Societies* (1889)**, `clublawlawofunre00daly`, Butterworth, 135 pp, explicitly not in copyright, full OCR. A 1923 successor edition exists at `dailysclublawlaw0000herb`.

**An unregistered society is the pure `LP1=0` / `LP2=0` pole**, and a treatise written about precisely that class — against Fuller and Holdsworth on the registered one — gives the row an *internal* contrast rather than a single reading. It also poses the one-row-or-two question a second time, on a different axis from the lodge/order one: registered against unregistered may be two forms, as `voc` was three. **Whether `friendly_society_england` is one row, two, or three is now an evidential question rather than a shrug.**

Note also the epistemic point from §5.1: Fuller, Holdsworth and Diprose state the law as practitioners, so these are **actor's-category** sources on a legal position, not an analyst's reconstruction. Set `articulation` accordingly, and say so in the row notes — the census rarely gets evidence of this kind.

**Not downloaded here.** These are external files and fetching them is MS's step; the identifiers above resolve at `https://archive.org/details/<identifier>`.

### 13.4 An incidental find in the ZotMoov folder

**`de Roover - Rise & Decline Of Medici Bank.pdf`**, 28.9 MB, dated 2026-08-30, sitting in the store. That is the **1963** *Rise and Decline of the Medici Bank, 1397–1494* — the book HKS actually rely on, which the 2026-08-31 pass recorded as unacquired and never returned by the deep search, and which is a different work from the 1948 monograph attached to `BJ8TSRTA`. It does not appear to be attached to any item. Worth a Zotero item of its own and a re-check of any `compagnia` or Medici citation that currently passes through the 1948 text.

### 13.5 Handoff

`CODING-BRIEF.md` written into the bundle root at `~/GitHub/_blind-mutual-pole-2026-09-04`. It names the two forms, points at the Zotero collection and the measured offsets, sets the `confraternita` scope question and the co-occurrence declarations as things to settle *before* opening a cell, states plainly what the bundle withholds and what remains computable, and gives the corrected check invocations from §10 so the coding session does not run the two silently-passing ones.

**This session must not do the coding.** It has read the vault MOC, the whole live matrix, the characteristic definitions and the logbook standing tables, and it wrote the pre-registration in §3. The bundle exists so that a session which has read none of that can code against it. Open a fresh chat on the bundle.

Bundle re-verified after the brief was added: `CHANGELOG.md` and `proposed-of/` absent, `validate_vault.py` clean at 216 notes.
