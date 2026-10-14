# Brief: the *muḍāraba* row from al-Sarakhsī, and the *qirāḍ* rows re-coded from Mālikī texts (2026-10-14)

**Status: APPROVED by MS in chat on 2026-10-14 (14:46 JST): all six recommendations of §6 accepted; recorded as rulings 1–6 in `records/RULINGS-mudaraba-qirad-2026-10-14.md`. Pass slug `mudaraba-qirad-2026-10-14` (ruling 6); this file keeps the draft slug in its name pending MS's confirmation of a rename. Text below unchanged from the draft except this status line. Nothing had been read for coding when it was written. Open, not blind: the blind on this material was spent by `comanda-adjudications-2026-10-11` (al-Sarakhsī 22, 27, 51), `commenda-italian-recode-2026-10-12` (22, 41, 48) and `latin-hanafi-mixing-tests-2026-10-13` (vols. 11, 19 and every vol. 22 *khalṭ* cluster; the *Muwaṭṭaʾ*'s *Kitāb al-qirāḍ* in full; the *Mudawwana*'s searched). Coder `claude-opus-5-5`, effort `high`. The row is opened after test 2 of the mixing tests; the selection this implies is declared at §5.5.**

Starting state, read from `.git/logs/HEAD`: `HistorEE_codebooks` at "Add she_death_aid: Dunhuang she association death mutual aid"; `myfoamrepo` at "She association note: coded section, S. 527 oil quota corrected". No `.lock` file in either `.git`.

Read for this brief: `claude/latin-hanafi-mixing-tests-2026-10-13.md` and `claude/she-associations-2026-10-13.md` (project docs); `records/RULINGS-latin-hanafi-mixing-tests-2026-10-13.md`; the type rows `mudaraba`, `qirad`, `commenda`, `comanda`, `comanda_ad_societatem` (`organizational_form_type.csv`) and `qirad_alloc`, `commenda_alloc`, `comanda_alloc`, `comanda_ad_societatem_alloc` (`loss_mitigation_type.csv`); logbook 2, 2026-08-18 (ii) and the recap at l. 608; logbook 5, 2026-10-12 (iii) and 2026-10-13 (iv)–(viii); every live `qirad` and `qirad_alloc` cell with its note; both characteristic vocabularies in full; `CHARACTER-CODING.md` (tests 3–5 and the component sets); `CONTRIBUTING.md` (headings and §4); the vault note "The mudaraba is revocable not locked in". No source was opened.

## 1. What stands now (counts over the files)

**`mudaraba`** (`organizational_form_type.csv`; "Islamic", 7c onward): zero cells, "a determination rather than an omission" (logbook 2, 2026-08-18 (ii)). Two grounds: one institution under two names (Ramli 2018, 97), and "the schools are not known to diverge on any of the 32 characteristics". Falsification condition: `TS3`, which "needs a Mālikī source the library does not hold".

**`qirad`** (`organizational_forms`; "Islamic (Maliki)", 7c onward): 23 of 33 characteristics coded. By source:

| basis | cells | ids |
| --- | --- | --- |
| Mālikī text | 1 | `OF-0903` `CI5` |
| al-Sarakhsī, directly or through Ramli 2018 | 12 (2 substantive, 10 `.NR`) | `OF-0907` `MG2`; `OF-0571` `LP2 = 0`, low; `.NR`: `0069`, `0070`, `0570`, `0572`–`0574`, `0576`–`0579` |
| Udovitch 1970 / 1962 or `[verify]`; `source_read = unknown`, articulation `.NR`, coder `claude-opus-5` | 8 | `0068` `TS2`, `0071` `LR2`, `0072` `LR3`, `0073` `LR4`, `0075` `CF1`, `0076` `CF2`, `0077` `CF3`, `0089` `LR6` |
| `.NA` by disposition | 2 | `0074` `LR5`, `0575` `AP4` |
| not coded | 10 | `TS1`, `TS3`, `TS4`, `MG1`, `MG3`, `MG4`, `FP1`–`FP4` |

**So the open item's "`OF-0907` and the eleven Ramli-based cells" is 12 of the row's 22 cells that rest on no Mālikī text.** The other eight rest on Udovitch, who is not held with text (`RPV4XSBG` is a linked-URL stub), and whose *Partnership and Profit* is built chiefly on the early Ḥanafī texts [to confirm: not held]; none of the eight shows a reading.

**`qirad_alloc`** (`loss_mitigation_forms`): named "Qirāḍ / muḍāraba (loss-allocation aspect)", tradition **"Islamic", not Mālikī**. Ten cells, the commenda family's declared set (`MC1`, `MB3`, `RB1`–`RB4`, `PR1`, `PY0`, `VF1`, `VF2`). Eight rest on Ramli 2018 on al-Sarakhsī (Harris 2007 or Ackerman-Lieberman 2011 alongside on four); `VF1` and `VF2` on al-Sarakhsī directly; **none on a Mālikī text.** It is not in the open item, but it is the loss-side twin of `qirad` and ruling 1 reaches it.

**Family coverage.** Organizational side: `commenda` 23, `societas_maris` 23, `comanda` 33, `comanda_ad_societatem` 33, `isqa` 32, `qirad` 23. Loss side: `commenda_alloc`, `qirad_alloc`, `comanda_alloc` and `isqa_alloc` carry the same ten cells; `LS3` is deliberately uncoded on the family (it would restate `AP3`); 7 of the 8 rows with `PY0 = .NA` carry no `PY1`–`PY3` row.

**The vault note the type rows lean on is not evidence.** "The mudaraba is revocable not locked in" is `status: seed` and carries `[verify against fiqh sources — the schools diverge here]` on exactly the Mālikī point. The `qirad` type row says it "would close `CI2` (to 0)"; it cannot close anything. It is a hypothesis for the priors file.

## 2. Ruling 1, scope: reopen the determination, in both datasets

**Recommendation: reopen.** Four grounds, strongest first.

(a) **The determination's premise has failed on a coded characteristic.** Rulings 1–3 of 2026-10-13: unconsented mixing is a liability event that ends the trust in Ḥanafī law and is lawful, without liability, in Mālikī law, and `qirad CI5` had to be recoded because the Ḥanafī rule had been carried into the Mālikī row. `CI5` is description (component `none`), so this falsifies the premise but licenses no comparative claim.

(b) **The determination's own falsification condition can now be run.** `TS3` needed a Mālikī source; the *Muwaṭṭaʾ*'s *Kitāb al-qirāḍ* and the *Mudawwana*'s are now in reach (no. 2027 bears on recall, per the open item). `TS3` is `perpetual-succession`, WP2, and `CI2` (`capital-lock-in`, WP2) turns on the same passages. Because `TS3` was named on 2026-08-18, before any Mālikī text was read, a separation there tests a condition fixed in advance.

(c) **The split test.** A single "Islamic" row would have to carry one school's `CI5` value or a `P`, and `P` is never heterogeneity across instances. A value that differs across a row's scope is the signal to split the row.

(d) **Hygiene.** The alternative to a Ḥanafī row is not a clean `qirad` row. It is a Mālikī row carrying 12 Ḥanafī cells and 8 on a mainly Ḥanafī secondary work: the error refused at ruling 3 of 2026-10-07 and repaired once already at `OF-0903`. Blanking those cells without a Ḥanafī row throws the evidence away.

**Strongest objection: one institution entered twice.** The two rows will agree on the contract core by construction (`CF1`, `CF2`, `LR3`, `LR6`, `RB1`, `RB2`, `RB4`, `PR1` at least). Any similarity count over the census gains a near-duplicate pair, and the Islamic side of the commenda family doubles its weight.

**Answer.** The census already carries this cost on the Latin side and has a rule for it: `commenda`, `comanda` and `comanda_ad_societatem` are separate rows of one migrated institution, and Genoa, Pisa and Catalonia count as one Latin datum. Applied here: `mudaraba` and `qirad` count as **one Islamic datum** in any comparative claim, and agreement on core cells is declared as construction in both type rows before any cell lands (§5). The gain is confined to cells where the rows part. If after coding they part only on `none` characteristics, the component sets learn nothing and the split stands on hygiene alone. That is an acceptable result and should be reported as one, not as a failed pass.

**Ruling 1b, the loss side.** If reopened, `qirad_alloc`'s ten cells are all Ḥanafī evidence in a row coded `qirad`, and a `mudaraba_alloc` coded from al-Sarakhsī would enter that witness twice. **Recommendation:** re-scope `qirad_alloc` to Mālikī (name → "Qirāḍ (loss-allocation aspect)", tradition "Islamic" → "Islamic (Maliki)"), re-code it from the Mālikī texts, and code `mudaraba_alloc` (new type code) from al-Sarakhsī. **Alternative:** reopen on the organizational side only and leave `qirad_alloc` as the generic Islamic row. That is cheaper, but its same-institution link would then join a Mālikī `qirad` to a Ḥanafī-sourced loss row.

**Ruling 1c, type-row fields.** `mudaraba` tradition "Islamic" → "Islamic (Hanafi)". Both rows claim "7c onward". The evidence is Mālik (d. 795) and Saḥnūn (d. 854) for one, and for the other al-Sarakhsī (d. c. 1090), whose *Mabsūṭ* comments on al-Marwazī's abridgement of al-Shaybānī (d. 805). **Recommendation:** narrow both periods to the texts' span, "8c–9c (Malik, Sahnun)" and "8c–11c (al-Shaybani to al-Sarakhsi)", since a row's period claims stability across it and one text per school cannot show that. Every `key_source` change is append-only with a dated entry; the 2026-08-18 determination stays in place, bracketed as superseded.

**No version bump on any reading:** a new type code, new rows, in-place recodings and type-row field text are all below the bar (`CONTRIBUTING` §5).

## 3. What gets coded if reopened

| row | dataset | source | cells |
| --- | --- | --- | --- |
| `mudaraba` | organizational | al-Sarakhsī, *al-Mabsūṭ* 22 (*Kitāb al-muḍāraba*); 11 and 19 only where 22 refers to them | 33 attempted; new ids |
| `qirad` | organizational | *Muwaṭṭaʾ*, *Kitāb al-qirāḍ*, nos. 2015–2056; *Mudawwana* 3, 629–664 | 33 attempted: 23 edited in place, with a `recodings.csv` row for any change of value, confidence, articulation or source; 10 new |
| `mudaraba_alloc` | loss | al-Sarakhsī | the family's ten (ruling 2); new ids |
| `qirad_alloc` | loss | Mālikī texts | the family's ten, edited in place |

**Ruling 2, the loss-side cell set.** "Every characteristic attempted" departs from the family, whose four alloc rows carry the same ten cells. **Recommendation:** read for all 26 and enter the family's ten. Propose another of the sixteen only where a text addresses it substantively, and then for both Islamic rows, flagged as having no Latin comparator. List the rest in the declined section, one line each. `LS3` stays uncoded on the family precedent. **Alternative:** enter all 26 on both rows; that mostly adds `.NA` and `.NR` cells with no information.

**Evidence moves by re-reading, never by copying.** No `qirad` cell's value or note is transferred to `mudaraba`. Each `mudaraba` cell is coded afresh from al-Sarakhsī's text; Ramli 2018 may locate a passage, never carry a cell, since it reads the same text. **A `qirad` cell with no Mālikī text goes to `.NR`, never to the Ḥanafī value by default.** A re-point with the value unchanged still takes a recodings row (precedents `LM-R0062`, `LM-R0063`). Next ids in the live files today: `OF-0908`, `LM-0786`, `OF-R0225`, `LM-R0067`, to be taken again from the live files at application.

**Sources and their state.** All three are read on the transcriptions themselves; nothing is downloaded and no text layer is quoted.

- **al-Sarakhsī, *al-Mabsūṭ*:** Dār al-Maʿrifa, Beirut, as the transcribed title pages name it; Arabic Wikisource; page = the bracketed number. Not in Zotero. The extent of *Kitāb al-muḍāraba* in vol. 22 is to be measured on the transcription (rung 2) before the priors are written.
- ***Muwaṭṭaʾ*:** Yaḥyā's recension, Arabic Wikisource, nos. 2015–2056, read in full on 2026-10-13 for mixing. Edition not stated.
- ***Mudawwana*:** al-Maktaba al-Shāmila book 587 (Dār al-Kutub al-ʿIlmiyya, 1994; pagination stated to match the print). Searched for *khalṭ* on 2026-10-13; 637, 641, 645, 647–648 and 650–651 read.

## 4. Coding order, checked against both vocabularies (33 and 26)

Each block takes the Ḥanafī cell from al-Sarakhsī, then the Mālikī cell from the *Muwaṭṭaʾ* and *Mudawwana*, each from its own text. For each cell: evidence (text, page, count), one recommendation with confidence and the prior's fate. Then stop for MS's ruling.

- **O1, contract core (8):** `CF1`, `CF2`, `CF3`, `LR2`, `LR3`, `LR4`, `LR5`, `LR6`.
- **O2, term and exit (5):** `TS2`, `TS3`, `CI2`, `TS1`, `TS4`. This block runs the pre-named test.
- **O3, creditors and entity (8):** `AP3`, `LR1`, `AP1`, `AP2`, `AP4`, `LP1`, `LP2`, `LP3`.
- **O4, capital (4):** `CI1`, `CI3`, `CI4`, `CI5`.
- **O5, governance and frame (8):** `MG1`, `MG2`, `MG3`, `MG4`, `FP1`, `FP2`, `FP3`, `FP4`.
- **L1, the family's ten:** `MC1`, `MB3`, `RB1`, `RB2`, `RB3`, `RB4`, `PR1`, `PY0`, `VF1`, `VF2`.
- **L2, read and declined or proposed (16):** `MB1`, `MB2`, `CN1`, `CN2`, `CN3`, `HZ1`, `HZ2`, `PY1`, `PY2`, `PY3`, `LS1`, `LS2`, `LS3`, `GV1`, `DR1`, `DR2`.

The organizational blocks total 8 + 5 + 8 + 4 + 8 = 33, and the loss blocks 10 + 16 = 26: every characteristic in both vocabularies appears once. That makes 118 cell decisions over seven stops.

## 5. Declarations before any row (item 4)

**Non-independence.**

1. **One text per school.** The Ḥanafī witness is al-Sarakhsī alone. His *Mabsūṭ* carries the earlier Ḥanafī statements through al-Marwazī and al-Shaybānī, but it is one witness. On the Mālikī side, the *Muwaṭṭaʾ* and the *Mudawwana* are one witness: the *Mudawwana* is Saḥnūn recording Ibn al-Qāsim on Mālik, and it restates the *Muwaṭṭaʾ*'s rules (637 restates no. 2035). That makes two data points, not four.
2. **Shared upstream on the core.** Both schools rest the contract on the same early reports and on an asserted consensus. Their agreement on the core is therefore one witness on what they share, and parallelism if it is called anything; it is not counted as corroboration in either direction.
3. **Ramli 2018 and al-Sarakhsī are one witness.** So would Udovitch 1970 be, if acquired, on what it takes from the Ḥanafī texts [to confirm].
4. **The family.** `mudaraba`, `qirad`, `commenda`, `societas_maris`, `comanda`, `comanda_ad_societatem` and `isqa` form one family. The Latin rows are one datum (Genoa, Pisa, Catalonia), and the two Islamic rows become one datum by this pass. Agreement across Latin and Islamic rows is parallelism, not convergence.
5. **Selection.** The row is opened after test 2, *because* the schools were seen to differ on mixing. **`CI5`'s separation is the reason for opening and carries no weight as a result of this pass.** `TS3` is the only separation named before any Mālikī text was read. Any other separation is a finding of an open pass and is to be read as one.

**Co-occurrence** (`cooccurrence_basis`):

- `mudaraba` ↔ `qirad`: `same-institution`, already declared both ways. Both `key_source`s are to say that it now means one institution under two schools' law.
- `mudaraba` ↔ `mudaraba_alloc@loss_mitigation_forms`: `same-institution`, new, both ways.
- `mudaraba_alloc` ↔ `qirad_alloc`: `same-institution`, new, both ways.
- **Ruling 3, the Latin links.** The existing `commenda` ↔ `qirad` and `commenda_alloc` ↔ `qirad_alloc` links were declared when `qirad` stood for Islamic law in general. With `qirad` Mālikī, they assert a school-level identity that no source read establishes. **Recommendation:** add no link from `mudaraba` or `mudaraba_alloc` to any Latin row, leave the existing links standing in this pass, and flag them in both `key_source`s. Whether the Latin link should name both Islamic rows, one, or neither is a theory call for MS, outside this pass.
- **`boundary_basis`.** `mudaraba_alloc` takes `contemporary-legal-form` (the schools' own law of the contract), with confidence set after coding. `qirad_alloc`'s `contemporary-terminology`/`high` describes its boundary with `commenda_alloc` and stays. The column holds one basis, so the second boundary goes into `qirad_alloc`'s `key_source` in prose.

## 6. For MS to rule before the priors

1. Reopen the determination: **recommended**.
2. 1b: re-scope `qirad_alloc` to Mālikī and code `mudaraba_alloc`: **recommended**.
3. 1c: `mudaraba` tradition "Islamic (Hanafi)", and both periods narrowed to the texts: **recommended**.
4. Ruling 2: the family's ten loss cells, plus substantive extras on both Islamic rows: **recommended**.
5. Ruling 3: add no Latin link and flag the existing ones: **recommended**.
6. The slug.

Nothing else needs ruling before the priors.

## 7. After approval

1. Measure the chapter's extent (rung 2). Write `records/PRIORS-<slug>.md` with one prior per cell per row, each a value plus what would falsify it. MS commits it, and I confirm the commit from `.git/logs/HEAD` before reading.
2. Work through blocks O1–O5, L1 and L2, recording rulings in `records/RULINGS-<slug>.md` as they are given.
3. Write `records/proposed-rows-<slug>.csv` and `proposed-type-rows-<slug>.csv`. Round-trip `data.csv` (both datasets) and both type vocabularies byte-identically, and ask before writing `data.csv`.
4. Application:
   - rows, recodings and type rows;
   - logbooks: 2 (the determination reversed), 4 (the standing-table row, the `TS3` test, the priors scored), 5 (sources), 6 if needed;
   - `CHANGELOG`;
   - the full check suite;
   - the vault: the revocability note's `[verify]` discharged or not, and the *qirāḍ* notes;
   - the project doc.

## 8. Standing-table row, drafted as a budget

`mudaraba-sarakhsi-2026-10-14` | 2026-10-14 | open pass; spends nothing not already spent. al-Sarakhsī 22 was spent by `comanda-adjudications-2026-10-11`, `commenda-italian-recode-2026-10-12` and `latin-hanafi-mixing-tests-2026-10-13`; the *Muwaṭṭaʾ* and *Mudawwana* *qirāḍ* chapters by the last of these. This pass reads them in full for coding. Before the priors, rung 2 only (the extent of the chapter). | Prejudices later blind coding of `mudaraba`, `qirad`, `mudaraba_alloc` and `qirad_alloc`, all already prejudiced. To be reconciled at the close.

## 9. Out of scope unless MS adds it; flags carried, not repaired

**Out of scope:**

- the Shāfiʿī *qirāḍ* (al-Shīrāzī);
- the Roman deposit texts;
- Venice;
- acquiring Udovitch 1970.

**Carried, not repaired:**

- `OF-0902`'s note, with its stale Catalan contrast;
- logbook 5, 2026-10-12 (iii);
- the `qirad` type row's claim that the revocability note "would close `CI2`" (§1), to be bracketed at application.
