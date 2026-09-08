# Forms selection — the shielding witnesses, 2026-09-05

**Operator session. Slug `shielding-witness-scheme`.** Nothing coded, no row proposed, `data.csv` untouched, no `git` run. Companion to `claude/mutual-pole-coding-2026-09-04.md`, which this session read in full before planning.

Census at the start of the session: `organizational_forms` **707 rows, 30 form codes, 26 institutions, version 0.9.0**. Eleven zero-instance values, nine one-instance values.

## 0. The decision

**Next batch: `deed_of_settlement_company` + `compagnie_antwerpen`, coded blind, two forms and two independent witnesses on one question.**

- **`deed_of_settlement_company`** — the English unincorporated joint-stock company constituted by trust deed, c.1720–1844. Source: Televantos 2020, `KWGBQ6VN`, printed 35–53 and 143–181.
- **`compagnie_antwerpen`** — the Antwerp general partnership/company under the *Costuymen* of 1582 and 1608, sixteenth century. Source: De Ruysscher 2020, `THGK3Z7T`, printed 235–265 minus the Holland pages.

Both slugs are working names. **Both scopes are open questions the coder settles first, from the sources, before a cell is opened** — see §5.

## 1. Why this batch: the criterion is the source, not the empty cell

Two consecutive batches have now ended with the same sentence in the logbook. 2026-09-04: *"`entity-shielding` gains one `AP4=1` and nothing else. `AP1` and `AP2` are `.NR` on both new forms. Two forms were added to the entity census and the component that carries most of the WP2 argument learned nothing from either."* The 08-30 *commenda*-family batch ended two thirds in missingness on the same columns.

The standing table says why. `AP1` reads `.NR` on **11 of 20** coded forms and `AP2` on **10 of 20**. Those are not gaps in the world; they are gaps in the intake. **Not one form in the entity census was coded from a source that asks the creditor-priority question.** Ottoman accounting studies, Beguine social history, guild history, *fiqh* on capital-labour contracts and Italian company history all describe institutions without ever asking whose creditors reach which pool first, so the honest coding is `.NR` and the column stays empty however many forms arrive.

So the selection criterion this session used was not *which zero-instance value can I fill* but **which held source asks the creditor question of a named historical form**. That criterion is testable in advance by term count, which is what §2 does, and it changed the answer completely: three forms that looked strong on the previous brief were killed by it, and the two that survive were sitting in the library unread, tagged from sweeps that had already found them and passed over them.

**This generalises the 2026-09-04 finding rather than repeating it.** That session's rule was: *wherever two intakes have run on different questions, the second census's forms are cheap and blind at once.* This session found the same mechanism inside one library rather than between two censuses — **Televantos was acquired 2026-08-30, tagged `entity-shielding`, and read as analytic vocabulary for a medieval Italian batch; De Ruysscher was found on 2026-08-29, tagged `entity-sweep-2026-08-29`, and never opened at all.** Both were classified by the question the finding session was asking, not by the question they answer. A library is indexed by what you wanted last time.

## 2. Holdings, verified before the batch was fixed

Every claim below is measured on `macbook-air-local` against the ZotMoov store (412 files, all extracted to text for this sweep). Variants tried are stated, per the standing rule of 2026-08-31 as extended on 2026-09-04.

### 2.1 The two forms are supported

**Televantos 2020 `KWGBQ6VN` — *Capitalism Before Corporations* (OUP, Oxford Legal History Series).** 225 PDF pages, clean text layer. **Offset re-measured at six points across the whole book — PDF 41/61/75/171/199/225 = printed 16/36/50/146/174/200, constant, `printed = PDF − 25`.** The 08-30 record had two points and an *approx.* on the chapter start; both are now exact. **Chapter 2 §2 "The Deed of Settlement Company" runs PDF 60–78 = printed 35–53; chapter 7 "Partnership Dissolution and Bankruptcy" opens PDF 168 = printed 143.**

Whole-book counts: `deed of settlement` **69**, `joint stock` 84, `Bubble Act` 36, `reputed ownership` 57, `limited liability` 43, `dissolution` 70, `jingle` 18, `separate estate` 16, `joint estate` 12, `legal personalit*` **14**, `transferable share` 10, `Companies Act` 14, `1844` ×24. The deed-of-settlement hits are **a continuous dense run at printed 35–53**, not scatter — nineteen consecutive pages, six or more hits on several of them.

**De Ruysscher 2020 `THGK3Z7T` — *Entity shielding y los inicios del patrimonio de las sociedades (Amberes, siglos XVI–XVII)*, AHDE XC, printed 235–265.** 31 PDF pages, clean text layer, 3,000–4,400 chars/page. **Offset measured at fifteen consecutive verso points, PDF 2–30 = printed 236–264, `printed = PDF + 234`.** Recto running heads carry the title; verso pages carry the number.

Whole-article counts: `entity shielding` **41**, `acreedor` **49**, `sociedad` 174, `socio` 138, `responsabilidad` 26, `patrimonio` 21, `liquidación` 16, `insolven*` 12, `Amberes` 86, `1582` ×22, `1608` ×23, `personalidad jurídica` 1.

**`source_lang=es` is already in the `organizational_forms` enum** (checked: `ja, nl, de, fr, en, es, he, arc, ar, la, it, tr, pl, pt`). **No schema commit is needed ahead of this batch** — unlike `tr` on 2026-09-04. `zh` is still absent from this dataset's enum and present in the loss dataset's; that gap is unchanged and is not this batch's business.

### 2.2 Three candidates killed by the same test, and one of the three had been recommended

Each was a live proposal before the count was run. Each count is over the whole file.

**Allen 2022 `NDNTDAI2` — the Edinburgh craft incorporations. Falsified, and this is the one that matters.** The 2026-09-04 Zotero pass wrote onto the item that this is *"the British alternative … nearer the entity questions than any English friendly-society item … the row to code if `friendly_society_england` stays blocked"*, and added, correctly, *"NOT SWEPT for entity terms on 2026-09-04; do that before relying on it."* Swept: **`incorporat*` 131 — and `creditor` 1, `legal personalit*` 0, `sue`/`sue and be sued` 0, `common seal` 0, `body corporate` 0, `perpetual succession` 0.** The 131 is the craft body's *name* — "the Incorporation of Mary's Chapel" — not an answer to anything. **A term-count false positive of exactly the kind the count is run to catch, and it would have passed unexamined if the note had not said to check.** The verdict is Cordery's verdict: social and financial history of a mutual, not legal history of an entity. Recorded on the item; the 09-04 relevance note is withdrawn there in place, not deleted.

**Frank 2018 `UNWASN6P` — the Italian confraternity as a financial body. Acquired since the last pass, and falsified.** The item was the top of the 09-04 acquisition list — *"the single best confraternity-as-financial-body source in the library and it cannot be read"* — and **MS acquired it at 15:24 on 2026-09-04, one hour after the pass that called it blocking.** Its `Extra` still read `NO ATTACHMENT` when this session opened it; a second instance of the 09-04 lesson that a note recording an *action* rots, this time in the other direction. **The file is not the chapter: it is the whole 549-page Böhlau volume**, Lobenwein/Scheutz/Weiß (eds), *Bruderschaften als multifunktionale Dienstleister der Frühen Neuzeit in Zentraleuropa* (VIÖG 70, Wien 2018). Offset measured at twenty consecutive points, `printed = PDF − 1`; Frank = PDF 136–145. Over those ten pages: `Bank` 45, `monte` 27, `Monte di` 14, `Kredit` 20, `Zins` 13 — against **`universitas` 0, `persona giuridica` 0, `Rechtspersönlichkeit` 0, `Korporation` 0, `juristisch` 0, `Vermögen` 0, `Gläubiger` 0, `Haftung` 0, `Stiftung` 0, `capital` 0.** Frank is about confraternities running *Monti di Pietà* and lending at interest. **The 09-04 prediction that he would supply the `CI` cluster is wrong, and he would not have unblocked `confraternita`.**

**Goddard & Smalley 2024 — the Guild of St George, Nottingham.** `guild` 241, `bequest` 30, `fraternit*` 25 — against `legal personalit*` 0, `creditor` 0, `common seal` 0, `mortmain` 0, `sue` 0. Does not reach the entity questions.

### 2.3 The mutual pole, and the cash waqf, restated as a finding

**`friendly_society_england` is still blocked and the Tier 1 acquisition has not happened.** Fuller, Diprose & Gammon, Holdsworth, Daly and the rest of the Archive.org list return nothing in the library. The row stays deferred on the 08-30 credit-cooperative rule.

**The cash waqf was tested and rejected, and the negative is worth recording because the holdings are enormous.** Fourteen studies of the *para vakfı* carry 190/170/129/95/78/76/76/63/62/61/58/55/43/36 form-terms — and **entity-terms 0 on all but one** (Deniz 2026, 8). It is the *avarız* pattern exactly: Ottoman accounting and court-register scholarship, superb on flows and silent on the entity. A `cash_waqf` entity row would be a third waqf sibling producing a third all-`.NR` `entity-shielding` result, on sources partly shared with `avariz_vakfi`. **Rejected on evidence, not on the sibling objection alone.**

**`societas_publicanorum` was considered and rejected on a different ground.** Its form-terms sit at 50/44/35/30/29/27 — but every one of those files is Hansmann/Kraakman/Squire, Padgett, Le Bris or Zhang & Morley, i.e. **theory discussing it comparatively.** There is no dedicated study in the library. Coding it would be the census coding its own framing source. A Malmendier acquisition would change this.

## 3. The value tables, computed before any row exists

Computed from `datasets/organizational_forms/data.csv` at 707 rows against `allowed_values` in `vocabularies/organizational_form_characteristic.csv`, **before the batch was fixed and before any cell was written.** Recorded here so that a filled value can be told from a lucky one afterwards.

### Zero-instance values — eleven

| char | value | name | component / WP |
|---|---|---|---|
| `AP4` | `P` | separation from founder estate | entity-shielding / WP2 |
| `AP4` | `0` | separation from founder estate | entity-shielding / WP2 |
| `TS1` | `P` | perpetual succession | perpetual-succession / WP2 |
| `TS4` | `1` | mutability of purpose | perpetual-succession / WP2 |
| `LR1` | `none` | liability extent | owner-shielding / WP1 |
| `LR2` | `attenuated` | outcome coupling | outcome-coupling / WP1 |
| `LR3` | `P` | profit-and-loss sharing | loss-sharing / WP1 |
| `LR4` | `P` | risk pooling | risk-pooling / WP1 |
| `LR5` | `na` | pooling correlation | risk-pooling / WP1 |
| `LR6` | `downside-only` | coupling symmetry | outcome-coupling / WP1 |
| `MG3` | `P` | entry restriction | none |

Unchanged from 2026-09-04 except that `FP1=mutual-provision` has left the set — filled by `bruderschaft_salzburg`, and now a one-instance value. **`LR5=na` remains shadowed by the `.NA` sentinel (logbook 1) and `LR1=none` remains suspect on its `labour-party` locator; the 08-30 recommendation on both is still not actioned.**

### One-instance values — nine

| char | value | sole instance |
|---|---|---|
| `LP3` | `0` | `isqa` |
| `AP1` | `0` | `isqa` |
| `AP2` | `P` | `asiento_averia` |
| `CI1` | `none` | `waqf_khayri` |
| `LR5` | `synchronising` | `asiento_averia` |
| `MG2` | `founder-fixed` | `waqf_khayri` |
| `FP1` | `mutual-provision` | `bruderschaft_salzburg` |
| `FP4` | `0` | `hegu_yingu` |
| `CF2` | `P` | `nakai_fictive_household` |

### The standing prohibitions this batch does not lift

**`AP4` is `1`×3 and `.NA`×17.** Three coded forms, one value between them, no discriminating power, and the prohibition written into the characteristic's own definition stands. **Neither proposed form is founder-endowed**, so neither can lift it. The forms that would are pious foundations, chantries, the charitable trust and the *fideicommissum*, and **the library holds none of them** (`chantry` 7 hits in the one candidate file, `mortmain` 0; no `fideicommissum` item at all). This is the census's oldest unrelieved blocker and it is an acquisition problem, not a selection problem.

**The `entity`-locator sub-pool recode audit required by the 2026-08-31 rule has still not been run.** Until it has, no similarity or difference claim on `entity-shielding` or `legal-personality` may rest on a form with sub-pools. Both proposed forms must be scoped with that rule in hand — see §5.

## 4. Co-occurrence and non-independence, declared before any row exists

### 4.1 Co-occurrence, for `organizational_form_type.csv`

**`deed_of_settlement_company`**

- ~~`cooccurs_with: joint_stock` · `cooccurrence_basis: uncertain`.~~ **CORRECTED 2026-09-05, LATER THE SAME DAY: MS SETTLED THIS. THE TWO ARE TWO INSTITUTIONS.** The declaration is therefore `cooccurs_with: joint_stock` · `cooccurrence_basis: same-polity` — same polity, same century, contrasting regimes, different institutions, no shared source. `joint_stock` holds two cells, `LP1=1` and `AP3=P`, both from Harris 2020, and `LP1=1` is consistent with it being the *chartered* company, so **no cell of it needs recoding and none is to be touched by this batch.** What is left over is a one-line clarity problem and not a coding one: the type row is named simply "Joint-stock corporation" and nothing in it says *chartered*. Flagged for a later pass, deliberately not repaired here (§5.3 stands as written for that reason).
- `cooccurs_with: friendly_society_england` (loss census) · `same-polity`. Both are English unincorporated associations holding property through trustees. No shared source, no shared institution. **Reverse declaration required in `loss_mitigation_type.csv`.**

**`compagnie_antwerpen`**

- `cooccurs_with: natie` · `same-polity`. Both Antwerp; different institutions; no shared source.
- **No declaration against `voc_1602`/`voc_1612`/`voc_1623`, and the absence is deliberate.** De Ruysscher's article does discuss the VOC charter of 1602, at printed 257 and 261–263. **That is a scope rule, not a co-occurrence** — see §4.2(c).

**Both new rows**: `cooccurs_with` each other is **not** declared. Different polities, different centuries, different institutions, no contact. The relation between them is that they answer the same question, which is not what this field records.

### 4.2 Non-independence, and this is the part that binds

**(a) Both sources engage Hansmann, Kraakman & Squire 2006, and HKS is a coded source in this census.** Televantos: `Hansmann` 14, `Kraakman` 12, `Squire` 10, `asset partitioning` 12. De Ruysscher: 17/17/17, `entity shielding` 41. HKS 2006 is the source behind **`compagnia`'s `LP1`, `LP2`, `LP3`, `AP1`, `AP2`, `AP3`, `TS2`, `CI1`, `LR4`, `LR5`, `MG1`, `MG4`, `FP1`, `FP2`, `FP3` and `CF3`.** Therefore: **agreement between either new row and `compagnia` on any entity characteristic is not two witnesses wherever both sides trace to HKS.** The coder must check, cell by cell, whether the passage used is the author's own evidence or his restatement of HKS, and say which in the cell note.

**(b) Televantos and De Ruysscher are independent of each other, and this was tested rather than assumed.** `Ruysscher` returns **0** in Televantos; `Televantos` returns **0** in De Ruysscher. No citation relation in either direction, different languages, archives, polities and centuries. Subject to (a), agreement between the two new rows **is** two witnesses.

**(c) Each row rests on one witness, and that was tested too.** `deed of settlement` returns **0** in Harris 2020, **0** in De Ruysscher, **0** in Le Bris et al. 2026, and **1** in HKS 2006 — the framing source, not a second witness. No held item gives an independent reading of either form. **Consequence: no agreement internal to a row corroborates it, and neither row may be treated as two independent cases against anything.** This is the `fraterna`/`compagnia` shape and it is accepted here with eyes open, because the alternative — coding both English forms out of Televantos — would have put *two* rows under one witness instead of one each.

**And the scope rule that falls out of it:** the Antwerp row is coded from the **Antwerp** material. De Ruysscher's Holland and VOC pages, concentrated at printed 257 and 261–263, are about the VOC, and the census already carries three VOC rows coded from de Jong & Jonker, Gelderblom and de Jongh. **A cell on `compagnie_antwerpen` taken from those pages would silently make a VOC claim.** Not to be done.

**(d) An evidential relation that `cooccurrence_basis` cannot express, and which therefore lives here and in the row header.** De Ruysscher's article is a **rebuttal of HKS** — strong entity shielding was *"excepcional y de mínima importancia"*, shielding arose from liquidation practice rather than legislative design, and even VOC limited liability rested largely on *iura in personam*. The census's `compagnia AP1=1 / AP2=0` cells rest on HKS. **So a coded Antwerp row stands in a disputing relation to coded cells elsewhere in the matrix, and the vocabulary has no field for that** — the same defect logged in logbook 6 for the assessed negative. Per `bazacle_mill FP1=mixed`, **the disagreement is recorded as a coding, not resolved as a verdict**, and the row header must say so. **This is a theory call and it is MS's** (§5.4).

## 5. What the coder settles first, before a cell is opened

**5.1 The scope of `deed_of_settlement_company`.** Televantos treats the deed of settlement company inside a chapter on *trusts in business structures*, beside testamentary trading trusts. Is the census's unit the deed-of-settlement company specifically, or the wider class of English unincorporated associations constituted by trust deed? Settle it from the source's own terms, name the constitutive instrument, and state the period the row claims.

**5.2 The scope of `compagnie_antwerpen`.** De Ruysscher writes about *las sociedades* in Antwerp under the *Costuymen* of 1582 and 1608. **Is that a form or a doctrinal category?** This is the `confraternita` question again, and the 2026-09-04 answer there was that the sources refused the umbrella in their own words. If they refuse it here, **say so and code nothing** — an uncoded umbrella with a reasoned refusal is a result, as `confraternita` was.

**5.3 The `joint_stock` row is an umbrella with two cells and the new row may collide with it.** `joint_stock` = `LP1=1`, `AP3=P`, Harris 2020. **Do not recode it inside this batch** — the standing rule against repairing a defect in the batch that motivates it. Flag the collision, propose the scoping, leave it.

**5.4 The `entity` locator and sub-pools.** Apply the 2026-08-31 rule. A deed-of-settlement company's trustees hold the capital; a partnership's joint estate sits against the partners' separate estates. **Decide what "the entity" is for each row before coding `LP1`–`LP3`, `AP1`, `AP2`, `MG4`, `FP2`, `FP4`, and record the decision.** A cell the source supports only at sub-pool level is `.NR`, not a value carried over.

**5.5 `articulation`.** Televantos quotes deeds, pleadings and Eldon's notebooks; De Ruysscher quotes the *Costuymen*. Where the tradition's own words are on the page, `articulated` is available — and the entity census rarely gets it. Where the term is the modern analyst's, it is `analyst-imposed`. Do not let one carry the other.

## 6. The blind, and it is genuinely available here

The vault was swept by term count only — no note title opened, no body read beyond the counts. **It has argued none of this material:**

`deed of settlement` **0 files** · `unincorporated` **0** · `Televantos` **0** · `Bubble Act` **0** · `jingle` **0** · `separate estate` **0** · `reputed ownership` **0** · `Eldon` **0** · `English partnership` **0** · `trading trust` **0** · `Capitalism Before Corporations` **0**.

Against that, `limited liability` 19 files / 40 hits and `joint-stock` 17/31 — the general theory notes, which argue the *concepts* and name none of these forms. **The blind is real and it is cheap, and the mechanism is the one generalised on 2026-09-04:** the vault's entity notes were written against the theory intake, so a form that entered the library as analytic vocabulary for someone else's batch has never been argued.

## 7. This session's row for the standing spent-blind table

Drafted here for entry verbatim into `logbook/4`, on the rule that a slug omitted is a quarantine not applied.

| slug | session | what it spent |
|---|---|---|
| `shielding-witness-scheme` | 2026-09-05, operator | Read the whole live `organizational_forms` `data.csv` at 707 rows — per-form cell counts and the full `LP1`–`LP3`, `AP1`–`AP4`, `TS1`, `TS2`, `CI2`–`CI4`, `LR1` value grid for all 21 forms carrying entity cells — the whole `organizational_form_characteristic.csv` including the `entity`-locator rule and the `AP4` prohibition, both type vocabularies' rosters, the loss census's coded-form roster and cell counts, the three `datapackage.json` enums, and `logbook/4`'s standing-slug section and its 2026-09-04, 2026-08-30 (ii) and 2026-08-30 entries in full. Computed and recorded the complete zero-instance and one-instance value tables at 707 rows, the `AP1`×`AP2` cross-tabulation, and the finding that no `LP1=0` form in the census carries `CI3=1`. Read the Claude-project records `mutual-pole-coding-2026-09-04`, `mutual-pole-handoff-2026-09-04`, `mutual-pole-selection-2026-09-04`, `zotero-pass-2026-09-04` and `next-forms-entity-census-2026-08-29` in full. Ran **term counts only** over the vault for 35 terms — no title opened, no body read. Extracted all 412 ZotMoov PDFs to text and ran entity-term and form-term sweeps across the whole store; read Televantos's and De Ruysscher's front matter, contents and running heads for offsets, and Frank's chapter and the Böhlau volume's contents. Prejudices any later blind coding of `deed_of_settlement_company` and `compagnie_antwerpen` on every characteristic, and of `AP1`, `AP2`, `AP4`, `TS1`, `CI3` and the `legal-personhood` and `entity-shielding` group signatures generally. Brief at `proposed-of/NOTES-shielding-witness-2026-09-05.md`. |

## 8. Zotero, changed today

Four items rewritten. `Extra` was **read before replace** on all four, per the 2026-09-04 error.

- **`THGK3Z7T` De Ruysscher** — `Extra` was empty; now carries readability, the fifteen-point offset, the term sweep, the adversarial-witness note and the non-independence finding. Tags `+HistorEE-census`, `+page-offset-measured`, `+attachment-verified-2026-09-05`, `+shielding-witness-sweep-2026-09-05`, `+entity-questions-supported`.
- **`KWGBQ6VN` Televantos** — 08-30 record kept in place; six-point offset added, chapter starts made exact, the deed-of-settlement counts and the single-witness test added. The 08-30 relevance caveat is kept and marked as still correct *on its own terms*, with the note that it does not travel to an English row.
- **`UNWASN6P` Frank** — the false `NO ATTACHMENT` finding is quoted and superseded rather than deleted; acquisition date, the whole-volume container, the twenty-point offset, the falsifying term counts and the Klieber non-independence added. `−no-attachment`, `−acquisition-wanted`.
- **`NDNTDAI2` Allen** — the 09-04 relevance note is kept and **withdrawn in place** with the sweep that falsifies it, and what remains true of it on the loss side is stated separately.

## 9. Acquisition list, in order of what each would move

1. **Harris 2000, *Industrializing English Law*, and Morley 2017, *The Common Law Corporation*.** The second witness for `deed_of_settlement_company`. Without one the row can never corroborate itself.
2. **A founder-endowed form.** Anything on chantries, the English charitable trust, the *fideicommissum* or a German *Stiftung* with a legal-historical treatment. **This is the only thing that lifts the `AP4` prohibition**, which has now stood through three batches.
3. **Fuller, Diprose & Gammon, Holdsworth, Daly** — public domain, Archive.org, identifiers in `claude/mutual-pole-handoff-2026-09-04.md`. Unblocks `friendly_society_england`.
4. **Malmendier on the *societas publicanorum*.** Would let the census take a form the theory keeps naming and it has never coded.
5. **De Ruysscher 2023, "Grotius and Limited Liability" `DJXK8TF9`** — held, unread, tagged `cooperative-pole-sweep-2026-08-29`. `partenrederij` was coded from Grotius. Cheapest unopened item in the library.

## 10. Open, carried forward

Unchanged from 2026-09-04 unless noted: the `check_dependence.py` under-reporting defect (two instances, second logged 09-04); bare `build_views.py --check` verifying one view; `LR5=na` and `LR1=none`; `zh` absent from the `organizational_forms` enum; `*.pdf` not gitignored; the `source_lang` enum-agreement check across the three datapackages; Kars 2020 vs 2021; the six strains in logbook 6; `casa_san_giorgio LP3` with `SFJF4V7Z` **which has no attachment and no children** — checked today, still a stub.

---

# Addendum — MS's four decisions, and the second-witness question answered, 2026-09-05

## 11.1 The four decisions

1. **`joint_stock` and `deed_of_settlement_company` are two institutions.** §4.1 corrected in place; the declaration is `same-polity`. No `joint_stock` cell is touched. The type row's name does not say *chartered* and should eventually; flagged, not repaired.
2. **Follow De Ruysscher.** The Antwerp row is coded from what the source says, including where it cuts against a claim that coded cells elsewhere rest on. Recorded as a coding and not resolved as a verdict, per `bazacle_mill FP1=mixed`; reviewable. §4.2(d) stands and the row header must carry it.
3. **Second witness: check Harris or Morley.** Answered in §11.2. **Morley.**
4. **`AP4` is carried to its own acquisition session with an Undermind sweep.** Not folded into this batch. Spec in §11.4.

## 11.2 Morley settles it, and Harris 2000 is not the redundant one

**Morley, "The Common Law Corporation: The Power of the Trust in Anglo-American Business History", *Columbia Law Review* 116 (2016), no. 8, 2145. CITATION CORRECTION: the project's docs have been saying "Morley 2017" since 2026-09-04. The volume is 116 and the year is 2016; SSRN 2905724 is 2017 and that is the posting, not the publication.** Open access at the *Columbia Law Review* and on SSRN, so the acquisition is a download. **Fetching it is MS's step and no URL goes into `source_ref`.**

Checked against the essay itself rather than from its reputation. It answers, on primary evidence, every column the row is wanted for:

| column | what Morley supplies | evidence |
|---|---|---|
| `AP1` entity shielding | firm creditors' priority in trust assets | fraudulent-transfer statutes 1377/1487/1543/1571, Statute of Frauds 1677, Chancery cases |
| `AP2` liquidation protection | members cannot withdraw or force dissolution | ***Van Sandau v Moore* (1826)**; Collyer, Gow, Story, Bisset on capital lock-in by agreement |
| `CI3`, `CI4` transferable, depersonalised interest | shares traded; equitable/legal title split | *Richmond v City of London* (1702), 900 shares at £10; an eighteenth-century market in shares |
| `TS1` perpetual succession | trust deeds declaring indefinite existence | Freeman, Pearson & Taylor's deed survey |
| `LP3` capacity to sue | company sues and is sued through trustees | the *City of London* cases |
| `LP1`, `AP3`, `LR1` | limited liability without incorporation | Part III.B |

Period 1600s–1844 for England, which is the row's period; also 1850s–1930s United States, which is out of scope and must not feed the row. And the scale evidence the row's boundaries need: **224 of 514 companies formed 1720–1844 were unincorporated**, trusts outnumbered corporations more than ten to one in the 1845 census, and only 4 of 882 unincorporated companies chose to incorporate after 1844.

**But it does not remove the single-witness problem, and the reason is the §1.5 shared-upstream rule rather than a citation relation.** Televantos and Morley are independent authors who disagree, and they read **the same documents**. Counted in Televantos: `Van Sandau` 5 hits, cited at printed 40, 48, 50–51 and quoted at 1 Russ 462 — the very case Morley uses for liquidation protection. `Story` 116, `Gow` 31, `Collyer` 3, `Bisset` 2 — Morley's treatise base, all present. `Freeman` 26, `Pearson` 29, `Taylor` 83 — the deed survey, present. **So on `AP2` and on the treatise-based cells their agreement is one document read twice, not two witnesses.** They are two witnesses on *interpretation*, which is a real gain and a smaller one than "second source acquired" sounds. **The coder must say, per cell, whether Morley is corroborating Televantos's reading or corroborating his own reading of the same report.**

**Harris 2000, *Industrializing English Law: Entrepreneurship and Business Organization, 1720–1844* (CUP), is the genuinely independent one, and he takes the opposite verdict.** Morley cites him repeatedly as the leading modern work and rejects his characterisation: Harris has the trust as *"a fragile, inferior alternative"* that *"could not offer most of the features inherent in the joint-stock business corporation"*; Morley has it *"remarkably effective"*, with entity shielding *"almost as strong"*. They also split on the Bubble Act — Harris has it significantly restricting unincorporated companies, Morley has it *"widely ignored"* and possibly increasing trust use. **That is a dispute about the row's own cells, and under `bazacle_mill FP1=mixed` the census's job is to hold it open rather than pick a side.**

**Recommendation. One acquisition: Morley 2016, because it is free and it answers the columns. Two: Harris 2000 next, and he is the one that makes the row honest rather than merely fuller.**

## 11.3 A recruitment hazard this creates, and it must be in the row headers

**Both of this batch's second witnesses are HKS-sceptics.** Morley argues against Blair and Hansmann that *"the corporation was almost never the exclusive source of strong-form entity shielding in Anglo-American law"*; De Ruysscher argues against HKS that strong shielding was *"excepcional y de mínima importancia"*. Meanwhile **`compagnia`'s `AP1=1` and `AP2=0` rest on HKS 2006**, as do fourteen of its other cells.

So if this batch is coded with Morley on one row and De Ruysscher on the other, the census acquires two rows whose evidence is drawn from one side of a live dispute, set against an existing row drawn from the other. **That is a recruitment bias of exactly the shape the 2026-09-04 brief diagnosed for the mutual pole** — the intake selecting the answer — and the fact that it was arrived at by a source-quality criterion rather than a doctrinal one does not make it not so. **State it in both row headers and in `logbook/5`.** Harris 2000 is the corrective, which is the second reason to want him.

## 11.4 The `AP4` session, specified and not started

Carried out of this batch on MS's instruction. What it needs:

- **Target**: a founder-endowed form taking `AP4` other than `1`. The column is `1`×3 / `.NA`×17 and its own definition forbids it entering any similarity or difference claim until this happens. Three batches have now passed it by.
- **Candidates**: the English chantry, the charitable trust and the *use*, the German or Austrian *Stiftung*, the *fideicommissum*, the *mont-de-piété* / *Monte di Pietà*, the college or hospital foundation.
- **Library state, measured today**: nothing. `chantry` 7 hits in one file with `mortmain` 0 and `legal personalit*` 0; no `fideicommissum` item; `Monte di Pietà` appears only inside Frank's ten pages. **This is an acquisition problem and an Undermind sweep is the right instrument.**
- **What the sweep must ask**, because the 09-04 friendly-society sweep shows the framing decides the result: not *"what is a chantry"* but **whether the founder's estate and the endowed corpus were separate — revocability, reversion on failure, the founder's creditors' reach, and whether the founder or his heirs kept the presentation, the *tevliyet* equivalent, or a reserved life interest.** A social or devotional history of chantries will answer none of it, exactly as Allen and Goddard & Smalley did not.
- **A caution worth carrying**: `AP4=P` was reached on `avariz_vakfi` and declined on 09-04, because the census reserves `P` for structural half-presence within one arrangement and not for heterogeneity across instances. The next candidate will present the same temptation.

## 11.5 Zotero, further changes

- **`KWGBQ6VN` Televantos** — the single-witness paragraph is corrected: Morley 2016 is named as the second witness, with the shared-document caveat and the *Van Sandau* / Story / Gow / Collyer / Freeman–Pearson–Taylor overlap counted.
- **Morley 2016 and Harris 2000** are not in the library. Neither is to be entered until MS has the file; per §1.5 an item created for its metadata with a linked file is the preferred arrangement.
