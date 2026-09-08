# Proposal — two forms into `organizational_forms`, blind mutual-pole batch, 2026-09-04

Coded by an assistant session working only inside `~/GitHub/_blind-mutual-pole-2026-09-04`. `data.csv`, `datapackage.json`, `codebook.md`, `views/` and the vocabularies in the bundle were **not** modified; `git` was not run. Everything below is a proposal.

## 0. What is here

- `proposed-rows-mutual-pole-2026-09-04.csv` — 64 rows, `OF-0644`–`OF-0707`, two forms × 32 characteristics.
- `proposed-type-rows-mutual-pole-2026-09-04.csv` — **three** rows for `vocabularies/organizational_form_type.csv`, one of them an uncoded umbrella. Per logbook 2's deliverables rule these belong in their own commit, before the batch that motivated them.
- `PATCH-source-lang-tr-2026-09-04.md` — a one-value schema defect this batch exposes. **Not applied.** Until it is, `frictionless validate` fails on 28 of these rows.
- `LOGBOOK-DRAFT-mutual-pole-2026-09-04.md` — entries for logbooks 2, 4, 5 and 6.
- `COMMIT-MSG-mutual-pole-2026-09-04.txt`.

`record_id`s are computed from the bundle's own last ID (`OF-0643`) and run consecutively. The `code-a-form` skill says to use placeholders because parallel threads collide; logbook 2 §7 says to compute them from the data. The repo rule is followed and the collision risk is stated here instead: **re-check the last ID before merging.**

## 1. The two decisions taken before any cell was opened

### 1.1 `confraternita`'s scope: the row is NOT coded, and a narrowed child is coded instead

**Decision.** `confraternita` is created as an **uncoded umbrella** type row. The coded row is **`bruderschaft_salzburg`** — the post-Tridentine Bruderschaft and Liebesbund of the city and archdiocese of Salzburg, 1600–1950, in Klieber's own term of art the *Fraternität*. No Italian row is created.

**Why, in the sources' own words.** Klieber contrasts his object with medieval predecessors on free access (printed 47–48), with the Venetian *scuole grandi* and other Italian *confraternite* on political role (printed 61), and with the romance lands on the charitable dimension, which in Salzburg is "ein eher bescheidenes und eindeutig nachrangiges Engagement" (printed 57–59). Gazzini restricts herself to Italian religious associations "only when they were mainly composed of professionals" (printed 173) and treats *corporazioni* and *confraternite* as contiguous and in some periods indistinguishable (printed 171). One row over both would take its values from two authors each of whom says his or her object differs from the other's, and any divergence inside it would be an artefact of tradition rather than of institution — which is exactly the hazard the brief named.

**And only one of the two can carry an `organizational_forms` row at all.** Gazzini's chapter and its Italian twin answer almost nothing this dataset asks: no legal personality, no asset partitioning, no capital lock-in, no transferable claims, no succession. They are also already the source of `confraternity_fund_it` in the loss census, so coding from them here would enter one witness twice. Klieber answers property, capital, governance, membership, entry, authorisation, succession and purpose.

**Consistency with the standing instruction.** Logbook 2 carries the note of 2026-08-13, taken from this very Klieber article, that the loss-census `confraternity_fund` "cannot be one row for Latin Christendom". It was honoured there by splitting after the fact; it is honoured here by never creating the single row.

**What the narrowing costs.** The Italian confraternity is not in `organizational_forms` and the umbrella row says what would put it there: Frank, *Bruderschaften als Bank* (`UNWASN6P`), which has **no attachment** and is the item that would have carried the capital questions, and behind it a confraternity-as-*universitas* literature that no held item treats.

### 1.2 Co-occurrence, declared before the rows were written

- `avariz_vakfi` → `avariz_fund@loss_mitigation_forms`; `avariz_vakfi_kirkcesme@loss_mitigation_forms`, basis **`same-institution`**, as directed.
- `confraternita` (umbrella) → `bruderschaft_salzburg`; `confraternity_fund@loss_mitigation_forms`, basis **`same-institution`**, on the `confraternity_fund` / `confraternity_fund_it` precedent.
- `bruderschaft_salzburg` → `confraternita`, basis **`same-institution`**.

**A departure from the commission, and it must be visible.** The brief directed `cooccurrence_basis=same-institution` against `confraternity_fund_it`. Under the scope decision above that declaration would be **false**: `confraternity_fund_it` is Gazzini's medieval Italian material and `bruderschaft_salzburg` is Klieber's early-modern Salzburg material — different institution, region and centuries. A false co-occurrence declaration is worse than none, so it is not made. The relation that does hold between them is **evidential, not institutional**: both reach the census through one analyst's question set, the guild-and-confraternity mutual-support frame of the Hellwege volume. `cooccurrence_basis` has no value for that; logbook 5 asked for one on 2026-08-19 (`same-analytic-frame`) and did not get it. Flagged, not repaired.

### 1.3 Küçük 2025 is behind both censuses, and the agreement between them is not evidence

Küçük 2025 is the sole source of `avariz_vakfi_kirkcesme`'s twenty-three cells in `loss_mitigation_forms` **and** the best entity source for `avariz_vakfi` here. The overlapping pages are printed **147–156 and 161**, which carry that row's `MC1`, `LS1`, `PY0`–`PY2`, `VF1`, `DR1`, `RB3` and `PR1` and this row's `LR3`, `LR4`, `CI2`, `TS1`, `LR2` and `FP4`. **Wherever a cell here and a cell there rest on the same page of the same author the two censuses are not independent evidence and no agreement between them is a finding.** This is written into the type row as well as here.

Two further independence problems are declared on the type row and repeated here because they bit during coding:

1. **Kars 2020 and Kıvrım 2019 are one witness on the norms and two on the cases.** Kıvrım was accepted 31-12-2019 and Kars 03-10-2020; Kars carries Kıvrım in his bibliography and cites him. The sentence on trustees being elected by the residents and registered at court, and the sentence that the waqf's claim carried no privilege over other claims, appear in both with the city swapped — and the second descends from Akgündüz, *Osmanlı Tatbikatında Vakıf Müessesesi*, 228–229. What is genuinely separate is Kıvrım's Ayntab court evidence and Kars's Istanbul replacement evidence. The loss census recorded this on 2026-08-19 (iv); it was confirmed here by reading both in full.
2. **`avariz_vakfi` shares a doctrinal substrate with `waqf_khayri`.** Agreement at `TS1`, `TS2`, `CI2`, `LR2`, `LR4`, `MG1` and `FP1` rests on the law of *vakıf*, not on two observations of two institutions. `cooccurrence_basis` names institutional relations only.

## 2. What was coded, and on what

`coder=ai`, `review_status=unreviewed`, `reviewed_by=none`, `source_read=full` throughout: all five sources were read cover to cover (Küçük 37 pp., Kars 28 pp., Kıvrım 16 pp., Gürsoy 32 pp., Klieber 37 pp.), which is what licenses the `high` confidences. Page offsets were taken from the Zotero `Extra` fields and not re-derived; every printed folio cited was seen in a running head with its neighbours either side.

| | substantive | `.NR` | `.NA` |
|---|---:|---:|---:|
| `avariz_vakfi` | 21 | 7 | 4 |
| `bruderschaft_salzburg` | 16 | 13 | 3 |

`bruderschaft_salzburg`'s thirteen `.NR` cells are mostly one fact: Klieber's field is the organisation type, its *Totendienst*, its membership and its finances, and he never puts the questions of personhood, standing, creditor priority or liability. His own term sweep confirms it — no *Rechtsperson*, no *juristische Person*, no *Körperschaft* anywhere in 37 pages. The coverage profile of both rows is a map of their bibliographies, not of the institutions; that is the standing caution of logbook 5, 2026-08-29 (iii), and it holds here.

## 3. Cells declined, and why

**`avariz_vakfi`.** `LP1` — no source puts the personhood question; the DIA definition Kars quotes at 164 is the genus. `AP1` — not answered, and the sentence that looks like an answer is not: the waqf's claim carrying no privilege is about the waqf **as creditor** of a dead borrower's estate, not about creditors reaching the corpus. `AP2` — the withdrawal limb is answered and belongs to `CI2`; the creditor limb is untouched, and `.NR` rather than `P` because the missing half is evidence, not structure. `AP3` and `LR1` — not addressed; note that both diverge from `waqf_khayri`'s `.NA`, because these sources show the fund incurring obligations of its own, so the questions are unanswered rather than inapplicable. `CI3`/`CI4` — no interest in the fund is described and none is denied; the `compagnia CI3` decision of 2026-08-31 refused exactly this inference. `FP2` — no statement either way. `.NA`: `LR5` (LR4=0), `LR6` (LR2=veiled), `MG3` (MG1=beneficiary), `CF2` (CF1=0).

**`bruderschaft_salzburg`.** `LP1`, `LP3`, `AP1`, `AP2`, `AP3`, `TS3`, `CI3`, `CI4`, `LR1`, `LR2`, `LR6`, `FP2` — all source silence, each with the pages read recorded in `source_ref`. **`MG2` is `.NR` for a different reason and the note says so: no fitting value.** Klieber's second typological axis divides *selbständige* fraternities, with their own Präfekt, Assistenten, Konsilium and lay Verwalter, from *betreute* ones whose leadership and finance lay with an abbot, superior, rector or reverend mother — and the largest body in his study is of the second kind. The type spans `collective` and something close to `single-principal`, and `MG2` admits no mixed value. `.NA`: `AP4` (no founder — the AP4 locator rule of 2026-08-30 makes this `.NA` and not `0`), `CF2` (CF1=0).

## 4. The gap, and what I did about it

The brief says the vocabulary and the views let a coder compute the census's zero-instance set unaided, and that reaching such a value because a source took you there is a result while going looking for one is not.

**I computed it, and the timing is the material fact.** All five sources were read in full **before** the computation, and the computation was made **before** any cell was written. The set at that moment was: `AP4` {P, 0} · `TS1` {P} · `TS4` {1} · `LR1` {none} · `LR2` {attenuated} · `LR3` {P} · `LR4` {P} · `LR5` {na} · `LR6` {downside-only} · `MG3` {P} · `FP1` {mutual-provision}.

**Exactly one of those eleven is filled by this batch: `FP1=mutual-provision`, by `bruderschaft_salzburg`.** It rests on Klieber's own historical definition at printed 50 — an association formed "zur Bildung geistig-geistlicher Fonds … für einen gut vorbereiteten (Sterbstunde), würdigen (Begräbnis) und/oder leidgeminderten (Fegefeuer) Übergang" — on the *Umlagesystem bzw. Generationenvertrag* at printed 43, and on the enrolment slips in the members' own words at printed 45. `pious-charitable` is declined on Klieber's own finding that the charitable half of the usual formula is negligible in Salzburg. **The disclosure is in the cell note, and the test offered to a reviewer is the contrast with `avariz_vakfi`, where the same value was considered and declined** because the donors there are named individuals relieving a quarter they do not draw on.

**Three near misses, recorded because they are the honest part.**

1. **`LR6=downside-only`, reached and withdrawn.** I first read the *mütevelli*'s fixed salary (Küçük 154) against his personal liability to make the corpus good (Küçük 151) and his dismissal for lending without security (Gürsoy 110) as no upside plus real downside — which gives `LR2=coupled` with `LR6=downside-only`, and `downside-only` is empty. Re-reading the same pages took it back: those liabilities are for **breach**, not for outcome, and when a properly secured loan goes bad the loss falls on the fund, not on him (Kars 183–184, trustees non-suited against empty estates). The cell is `LR2=veiled`, `LR6=.NA`.
2. **`AP4=P`, reached and declined.** Gürsoy 112–113 shows that a waqf constituted by bequest is not binding while the founder lives and may be revoked at will (22 of her 109), and Kıvrım 37 has two founders endowing houses with occupancy reserved for life. `AP4=P` would have relieved the column's own recorded paralysis — "two coded forms and one value between them … no discriminating power". **Declined**, because the census reserves `P` for structural half-presence within one arrangement and not for heterogeneity across instances of a type; the revocability fact is coded once, at `TS3=P`, rather than twice. **`AP4` therefore still has one value and its prohibition still stands.**
3. **`TS4=1`.** Kıvrım 36 has the income coming to be spent where the village or quarter council decided. Read as an internal power that is `TS4=1`, an empty value. Coded `P` at `low` instead, because the passive "usulü getirilmiştir" does not say who introduced the practice, the founder's *şart* is elsewhere enforced against interference, and the sentence is Kıvrım's, reproduced by Kars, both descending from İpşirli's DİA article.

## 5. Adjudications for the maintainer

1. **`avariz_vakfi LP2=1` is a stronger value than `waqf_khayri LP2=P`, and `LP3=1` is stronger than its `P`.** The ground is that Kuran describes waqf doctrine while these four work registers in which the fund transacts and litigates. A reviewer may prefer `P` on the doctrinal point that in Hanafi law the corpus is owned by no person; the note states both readings.
2. **`avariz_vakfi LP3=1` carries the `begijnhof` caveat.** Standing is always exercised through the *mütevelli*, and Kars 183 says he is "a creditor like any other". If standing is read as running through the trustee rather than the institution, the cell drops to `P`.
3. **`avariz_vakfi MG2=collective` is the batch's main substantive result and is `medium` for a stated reason.** Many deeds name the trustee themselves (Kars 176; Gürsoy 109, 115). Governance is founder-fixed at constitution and collective in succession, and `MG2` admits no such value.
4. **The scoping of `avariz_vakfi` to the fiscal community unit is a decision, not a description.** Kıvrım 39 has Ammu mahalle divided into nine *bölük* each with its own trustee and its own cash. Scoped to the mahalle this is a **sub-pool form**, `CI1` reads `several-accounts`, and logbook 1's standing prohibition would bar any entity-shielding or legal-personality claim resting on it until the sub-pool audit is run. **If you prefer the mahalle scoping, apply that prohibition to this row.**
5. **`bruderschaft_salzburg` should probably be split, and is not.** *Selbständig* against *betreut* is Klieber's own axis and it spans `MG2`. Two rows on one source would manufacture agreement on every other cell — the `mudaraba` and `begijnhof`-1585 situation. Falsification condition on the type row: split when a second Salzburg or south-German source gives a cell-level value differing across the two. Katzinger on the Upper Austrian towns and Ardaillou on Vienna, both cited by Klieber, are the candidates.
6. **`MG4=religious` on both rows was coded from the sources and not by consistency.** `CHARACTER-CODING.md` records `MG4=religious` on the *ʿisqa* as having been coded "for consistency with `waqf_khayri`, which is precisely the prohibited move". Here: Kars 175 quotes a deed founded expressly "İmam Züfer kavli ile", and Küçük 149–151 works the Ebussuud fetva; Klieber 50 makes episcopal approbation constitutive. The counter-elements (the 15 per cent ceiling fixed by *kanun*; the 1866 Vereinsgesetz) are named in the notes, and `MG4` has no `mixed`.
7. **A citation flag, not repaired.** Zotero dates Kars **2020**; the article's own running head reads *TAD* C.40/S.69, **2021**, 160–187. The loss census cites "Kars 2020" and these rows follow it for consistency. One of the two is wrong.

## 6. Defects noticed and NOT repaired

1. **`source_lang` has no `tr` in `organizational_forms`** while `loss_mitigation_forms` has both `tr` and `zh`. Twenty-eight of these rows are Turkish-sourced and `frictionless validate` rejects every one. See `PATCH-source-lang-tr-2026-09-04.md`. Left for its own commit under the standing rule that a defect is not repaired inside the batch that exposed it — but note that this one **blocks the batch**, so it must be merged first rather than merely recorded.
2. **`check_dependence.py` still prints the weakest separation for a pair and hides the strongest**, the defect logged on 2026-08-18. Second instance, on this batch: it reports `LP2=P occurs with LP3 in ['.NR','P']` and does **not** report that after these rows `LP2=1` occurs with `LP3` in `{1, P}` — a **substantive** separation where the printed one is weak. See §7.
3. **`organizational_form_type.csv` has no `boundary_basis` / `boundary_confidence` columns**, so the scope reasoning for three new type rows has nowhere structured to live and sits in `key_source` prose. Third recurrence, after logbook 2, 2026-08-29.
4. **`cooccurrence_basis` cannot express an assessed negative, nor an evidential (as against institutional) relation.** Both bit here. Second and third recurrences of the shape logged at logbook 6, 2026-08-09 (ii) and logbook 5, 2026-08-19.
5. **`CI1` again.** An avarız *sandık* aggregating successive endowments into one chest is the same well-formedness strain recorded on 2026-08-31 (ii): the column cannot say *how the pool came to exist*. Not proposed, on the rule that the repair must not arrive in the pass that finds it.
6. **`FP4`'s "political authority" does not separate in a prince-archbishopric.** In Salzburg before 1803 the approving ecclesiastical authority and the territorial prince are the same person. A third member of the comparative-concept family `CHARACTER-CODING.md` already flags at `AP4`, `MG4` and `FP4`.
7. **`views/*.md` render nominal characteristics as integer indices** (`LR1` 0–3, `TS2` 0–2, `LR5` 0–1) in the same table whose legend reads "`0` an observed absence". The legend for the codes is given under "Character states", so this is documented rather than wrong, but a reader scanning `TS2` sees `0` for `open`. Recorded, nothing proposed.

## 7. Checks run

All on a scratch copy outside the bundle; the bundle's `data.csv`, `datapackage.json`, vocabularies and `views/` are untouched.

```
python3 scripts/check_vocabularies.py                          ✓ 6 files, 162 codes, valid
python3 scripts/check_dependence.py                            ✓ 0 problems (organizational_forms, the default)
python3 scripts/check_dependence.py datasets/loss_mitigation_forms   ✓ 0 problems
python3 scripts/check_softwrap.py                              ✓ no hard-wrapped prose
python3 scripts/build_codebook.py --check                      ✗ organizational_forms/codebook.md stale (expected: +64 rows)
python3 -m frictionless validate datasets/clearing_records/…        VALID
python3 -m frictionless validate datasets/loss_mitigation_forms/…   VALID
python3 -m frictionless validate datasets/organizational_forms/…    ✗ 28 constraint-errors, all source_lang="tr"
```

`frictionless` was **not** installed on the machine and was installed for this check (5.19.0). With `tr` added to the enum in the scratch copy the same dataset validates **VALID** and the error count falls from 28 to 0 — which is the whole diagnosis.

The nine organizational views were checked one per component with `--mechanism all`; all nine were **current** on the pristine bundle and all nine go **stale** with these rows, as they must. Regenerating in scratch gives 30 forms × the component set and reproduces cleanly.

The two silent passes were verified rather than assumed:

- `python3 scripts/build_views.py --check` reports `views/loss_mitigation_forms--risk-pooling.md: current` and exits **0**, having checked nothing in this dataset.
- `python3 scripts/check_dependence.py --dataset organizational_forms` prints `no characteristic vocabulary registered for '--dataset'; nothing to check` and exits **0**.

## 8. What the batch did to the matrix

**One value gain in the whole census: `FP1=mutual-provision`.** Ten zero-instance values remain empty, and `AP4`'s prohibition is not lifted.

**A new substantive separation inside `legal-personhood`, which the checker does not print.** `avariz_vakfi` is the census's first form reading `LP2=1` **and** `LP3=1` — capacity to hold property and standing to sue, both full — and it does so with `LP1=.NR`. Before this batch every `LP2=1` form read `LP3` as `P` or `.NR`. After it, `LP2=1` occurs with `LP3` in `{1, P}` on substantive values: **capacity to hold property as an entity does not determine standing to sue as one**, now shown from the positive side as `begijnhof` showed it from the negative on 2026-08-29 (iii). Contingent on `LP3=1` surviving the trustee caveat at §5.2.

**Two new group signatures.** `[legal-personhood]` gains `{.NR, 1, 1}` (`avariz_vakfi`) and `{.NR, 1, .NR}` (`bruderschaft_salzburg`); `[capital-immobility]` gains `{AP2:.NR, CI2:1}` on both rows.

**An observation, offered as an observation and not as a finding.** Both forms lock a perpetual principal and spend only its income, and both do it by making the administrator answerable for any diminution: Küçük 151 for the *mütevelli*'s *tazmin*, Klieber 56–57 for loans that carried no repayment schedule so the principal "trotz ständiger Zinszahlungen ungeschmälert erhalten blieb". They are unrelated traditions and neither source knows the other. That is a parallel drafting solution and nothing in this batch licenses a claim of descent or of independent arrival; `convergence` in the reserved cladistic sense is not available, and `parallelism` would need a shared ancestral condition nobody here has shown. It is also two rows coded by one coder in one pass, on `capital-lock-in`, which is a WP2 component — so it is precisely the shape `CHARACTER-CODING.md` says not to bank.

**And the negative that matters more.** `entity-shielding` gains one `AP4=1` and nothing else: `AP1` and `AP2` are `.NR` on both new rows. The component that carries most of the WP2 argument was 26% filled before the `nakai` recode, 25% after, and after this batch it is thinner still in proportion. Two forms were added to the entity census and the entity-shielding facet learned nothing.
