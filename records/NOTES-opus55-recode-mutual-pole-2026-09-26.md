# Operator brief: blind reliability re-code of `avariz_vakfi` and `bruderschaft_salzburg` by Claude Opus 5.5 (high), 2026-09-26

**For the maintainer, not the coder.** This file holds the baseline and the withheld predictions. It is untracked when the bundle is built, so the bundle does not carry it. It must never be copied into the bundle.

Pass slug: `opus55-recode-mutual-pole-2026-09-26`. Operator standing-table slug: `opus55-recode-mutual-pole-scheme`. Operator: Chat A, Claude Opus 5.5. The operator does not code and does not open the coding chat.

## 1. What this batch is

This is a reliability re-code, not an evidence update. The 64 cells of the 2026-09-04 mutual-pole batch (`OF-0644`–`OF-0707`) were coded blind by **Claude Opus 5, effort high**. They are re-coded blind by **Claude Opus 5.5, effort high**, from the same five sources read in full. The coder gets those five PDFs and no other source. The rows go to `recodings.csv` with `adjudication=pending`.

**What this can and cannot show.** A different model is a second rater with a shared upstream, not an independent one (manifest Limits; logbook 6, 2026-09-26). Named effort levels are not comparable across models. And the two coding conditions are **not identical**; §6 lists every asymmetry. Several of them bias towards disagreement.

## 2. Budget, drafted before reconnaissance (13:14 UTC), and its reconciliation

| question | rung planned | rung reached | note |
|---|---|---|---|
| Q1 Which vault slugs discuss the forms or their sources? | 1 and 3 (term counts; `source-session` slugs) | **4, not budgeted** | See the overspends below |
| Q2 Which logbook sections carry the batch's reasoning? | 2 (headings for 2026-09-04/05/06) | 2 | |
| Q3 Do the siblings rest on the same pages? | 3 (`source_ref` fields) | 3 | |
| Q4 Holdings and offsets | 0–2 | 2 | |
| Q5 Baseline and predictions | 5 (the 64 live cells; `records/NOTES-mutual-pole-*`) | 5, plus the original bundle's `SESSION-PROMPT.md` and `CODING-BRIEF.md` | The prompt read was added so that the new prompt could match the old conditions (§6) |
| Q6 Residual mentions | 5 on flagged snippets | 5 | |

**Overspends, and what forced them.**

1. **The first test build printed about 55 titles of withheld vault notes** to this session's terminal. These were the script's `removed note:` log lines, and nothing forced it: I did not suppress them. The titles are mostly archive-survey repository notes. Two are not: *"A perfectly correlated peril leaves only the time average"* and *"A scheme for extending the cooperative pooling census"*. **Suppress those lines on any future build.**
2. **To decide whether to withhold `isqa-qirad-commenda`**, I read one 120-character snippet from its notes (§4.2). That is rung 5, forced because a count could show the slug was dirty but not whether the mention stated a value.

**Standing row for logbook 4:** filed at the top of the standing table, verbatim from §10.

## 3. Holdings (Q4)

| item | Zotero | file in bundle `sources/` | pp | printed = | checked at | md5 (first 12) |
|---|---|---|---|---|---|---|
| Kars 2020 | `GAZN2XVN` (att. `CQ4L4NHZ`) | `Kars2020_GAZN2XVN.pdf` | 28 | PDF + 159 | PDF 5, 15, 25 | `116d9a9421f4` |
| Küçük 2025 | `NAQKKKN7` (att. `JNZHR9BT`) | `Kucuk2025_NAQKKKN7.pdf` | 37 | PDF + 146 | PDF 5, 15, 35 | `964cfe6202e8` |
| Kıvrım 2019 | `GSC5PEAH` (att. `7WXXB6CH`) | `Kivrim2019_GSC5PEAH.pdf` | 16 | PDF + 33 | PDF 3, 9, 15 | `1179222429c5` |
| Gürsoy 2019 | `VM4K33C4` (att. `R4QC5ZL3`) | `Gursoy2019_VM4K33C4.pdf` | 32 | PDF + 94 | PDF 10, 14, 16, 20, 28, 30 (folios on even pages only) | `f8897302aab4` |
| Klieber 2001 | `SR4E4QM7` (att. `VEUB2IG2`) | `Klieber2001_SR4E4QM7.pdf` | 37 | PDF + 33 | PDF 3, 19, 35 | `df1cf00bb89e` |

- Each item's `… 1.pdf` duplicate in ZotMoov is byte-identical to its original (same md5).
- The `storage:` imported attachments of Kars, Küçük and Gürsoy are missing on disk. They were not needed.
- All five offsets agree with the 2026-09-04 brief §12.2.

## 4. What was withheld, and why

### 4.1 Types

`avariz_vakfi,bruderschaft_salzburg,avariz_vakfi_kirkcesme,avariz_fund`.

**Loss-census siblings: both withheld, as MS recommended.**

- `avariz_vakfi_kirkcesme` (LM-0489–0511) cites Küçük 2025, 150–152.
- `avariz_fund` (LM-0564–0586) cites Kars 2020, Kıvrım 2019 and Gürsoy 2019.

They state facts from the same pages the coder will read. A re-coder who can see them can anchor on a sibling coding instead of the page, and a reliability test cannot tell that from agreement. **The cost is an asymmetry:** the original coder had all 46 sibling rows in its bundle (counted in `_blind-mutual-pole-2026-09-04`). See §6.

### 4.2 Sessions (30)

- **The 24 archive-survey slugs** in the logbook 4 standing table.
- **The mutual-pole slugs:** `mutual-pole-scheme` (1 note) and `mutual-pole-application` (0 notes; passed so that its standing row is stripped).
- **Found by count**, each a single note naming the forms or their sources: `ottoman-communal-funds` (Küçük and Kırkçeşme) and `shareholding-and-pooling-scheme` (Klieber and *avarız*).
- `joint-stock-scope-verification` (0 notes). Its standing row records re-opening Kıvrım 2019 to test `avariz_vakfi`'s scoping.
- `opus55-recode-mutual-pole-scheme`, this operator's own row.

**`isqa-qirad-commenda` was deliberately NOT withheld.** It has one mention in 14 notes, in `Count degrees of freedom not cells`, and that sentence states a value (a withheld form "coding `1`" on a characteristic). A test build that withheld the slug removed a note whose title contains `isqa`, which then matched as a residual across the whole bundle and cost 14 unrelated notes. **The sentence was redacted by hand instead** (§5).

Vault hits for `Bruderschaft` and `Salzburg`: zero.

The build removed **285 vault notes**, dereferenced their titles in 26 files and regenerated `graph/`.

### 4.3 Dates

`--withhold-dates 2026-09-04`. It removed five sections:

- logbook 2: the forms' entry;
- logbook 4: the zero-instance entry;
- logbook 5: the five-sources entry;
- logbook 6: 09-04 and 09-04 (ii).

**2026-09-05 was not withheld.** Every 09-05 heading is shielding-witness material. The mentions of these forms inside it were handled as residuals instead, so the coder keeps the `AP2`/`TS1` doctrine those entries carry.

## 5. Residual mentions and how each was resolved

The bundle was built in the device VM's scratch space, redacted there, re-scanned, and only then copied to `~/GitHub`. So nothing had to be deleted in a connected folder. Manifest, build log and redaction log sit beside the bundle.

**Deleted from the bundle's `records/`** (live copies untouched):

- the four named mutual-pole files: `NOTES-mutual-pole-2026-09-04.md`, `NOTES-mutual-pole-coding-2026-09-04.md`, `proposed-rows-mutual-pole-2026-09-04.csv`, `proposed-type-rows-mutual-pole-2026-09-04.csv`;
- **four more found by the scan:**
  - `NOTES-joint-stock-scope-verification-2026-09-06.md` and `NOTES-joint-stock-scope-2026-09-05.md`: the sub-pool scoping of `avariz_vakfi` and a mention of `bruderschaft_salzburg`;
  - `NOTES-shielding-witness-2026-09-05.md`: it states `FP1=mutual-provision` for `bruderschaft_salzburg` and the `AP4=P` near-miss on `avariz_vakfi`;
  - `proposed-retire-joint-stock-cells-2026-09-06.csv`: the same `AP4=P` near-miss.
- The other `records/` files were scanned. `NOTES-deed-of-settlement-shielding-recode-2026-09-07.md` names the batch `mutual-pole` only as a count of priors files, which states no value, and was kept.

**Line-level redaction in Markdown.** Each hit line became `[withheld 2026-09-26: this passage discusses a form under blind re-coding]`; table rows were dropped. The rule was any line naming a withheld type code or the title of a withheld note, and, inside the codebooks repo, any line naming one of the five sources, *avarız*, *Bruderschaft*, *Liebesbund*, Salzburg or *Fraternität*. Lines redacted:

- logbook 1: 10;
- logbook 2: 41;
- logbook 4: 58, including the standing-table rows that quote withheld titles or name these forms;
- logbook 5: 25;
- logbook 6: 1;
- vault `MOC - Ottoman archives`: 7;
- vault notes: `Count degrees of freedom not cells` 1, `Drelichman and Voth 2014 …` 2, `The contingent asiento is a missing form …` 1. The last two quote a withheld archive-note title (an archive's name). That redaction is collateral and harmless.

`check_tables.py --fix` was then run **inside the bundle only**, re-aligning two tables that had lost rows.

**Field-level redaction in CSVs:**

- **`organizational_form_characteristic.csv`, 9 fields:**
  - the sub-pool audit paragraph repeated in the `LP1`, `LP2`, `LP3`, `AP1`, `AP2`, `MG4`, `FP2` and `FP4` definitions. It states `avariz_vakfi`'s *bölük* scoping and that `bruderschaft_salzburg` has "one Vermoegen reported as a single annual balance", which is its `CI1`. Both clauses were replaced with a withheld marker.
  - The `AP4` definition's count, "The three are avariz_vakfi, begijnhof and waqf_khayri, all coding 1": the sentence was replaced. **This is the census's AP4 value for the form under test, sitting in a definition every coder reads.**
- **`organizational_form_type.csv`, 3 fields:**
  - `confraternita` `key_source` replaced whole; it is the original coder's scope reasoning and names what Klieber does and does not answer.
  - `confraternita` `cooccurs_with`: the dangling `bruderschaft_salzburg` was dropped, so `check_vocabularies.py` passes inside the bundle.
  - `joint_stock` `key_source`: the `AP4=P … DECLINED on avariz_vakfi` clause was cut.
- **`loss_mitigation_type.csv`, 2 fields:**
  - `confraternity_fund` `key_source`: the 2026-08-19 Klieber characterisation, including the quoted "ein eher bescheidenes und eindeutig nachrangiges Engagement", which bears on `FP1`, and the 2026-09-04 back-reference naming the coded child.
  - `cash_waqf` `key_source`: the sibling code was replaced.
- **`loss_mitigation_forms/data.csv`, 4 neighbour cell notes** (LM-0344, LM-0527, LM-0535, LM-0597): the sibling codes were replaced with `[withheld form]`. They state loss-census values of the siblings, not organizational values.

**Kept after review:**

- `loss_mitigation_type.csv` keeps one `Klieber` mention (the 2026-08-13 instruction that the loss row "cannot be one row for Latin Christendom"; it states no value) and three `avarız` mentions (a Zotero collection name, and Çizakça's Bursa cash waqfs, which are not these sources).
- `loss_mitigation_forms/data.csv` keeps one withheld-note title, *Archivio di Stato di Venezia*, as the archive holding a 1199 *colleganza*: an institution name, not a claim.

**Final re-scan of the bundle**, covering every `.md .csv .json .txt .svg .html .py` file for the three type codes, all 285 withheld titles and twelve source terms: **zero hits beyond the kept items above.**

**Checks inside the bundle after redaction:**

- `check_vocabularies` valid (162 codes);
- `check_dependence` 0/0 on both directories;
- frictionless VALID on all four resources;
- softwrap OK (16 files);
- tables OK;
- all 9 organizational views current with `--mechanism all`, and the loss risk-pooling view current.

**Next free ids (manifest):** `record_id` **OF-0836** / LM-0741; `recoding_id` **OF-R0001** / LM-R0001. Both `recodings.csv` files are empty.

**Base commits:** `HistorEE_codebooks` `2b5f634f`; `myfoamrepo` `b93b2ae6`.

**Scripted `git`, disclosed.** `make_blind_bundle.py` itself calls `git --no-optional-locks rev-parse` and `ls-files` (read-only, lock-free). They ran from the device VM on three builds: two tests and the real one. No other `git` was run.

## 6. Comparability: how the two coding conditions differ

| | original, 2026-09-04 (Opus 5, high) | re-code, 2026-09-26 (Opus 5.5, high) |
|---|---|---|
| Source access | Zotero MCP on the whole collection `6CCV6QAK`, including Gazzini ×2, Schewe, van Leeuwen and Wallis as background | **five PDFs in `sources/` only**; all source tools forbidden |
| Sibling loss-census rows (46) | **visible** | withheld |
| Klieber characterisation in the `confraternity_fund` `key_source` | **visible** | redacted |
| Scope | set by the coder (it narrowed `confraternita` to `bruderschaft_salzburg`) | **fixed for the coder** by type name and period |
| Non-independence of Küçük and the Kırkçeşme row | stated in the prompt | not stated (the siblings are withheld) |
| Logbook, vocabulary and vault context | the census at 643 rows, before these forms | the census at 833 rows, with later doctrine (sub-pool audit, `AP2` two-questions, `record_id` gaps), minus the redactions |
| Priors | none written | written and committed before any source is opened |

**Direction of the bias.** The first two rows give the original coder more to lean on, so they bias towards disagreement. The fixed scope biases towards agreement on scope-dependent cells. The later doctrine could move either way. **Score model agreement with this table beside it.**

## 7. Baseline: the 64 live cells (all `coder_model=claude-opus-5`, `coder_effort=high`, `source_read=full`)

| char | avariz_vakfi id | value | confidence | articulation | bruderschaft_salzburg id | value | confidence | articulation |
|---|---|---|---|---|---|---|---|---|
| `LP1` | OF-0644 | `.NR` | .NR | .NR | OF-0676 | `.NR` | .NR | .NR |
| `LP2` | OF-0645 | `1` | medium | articulated | OF-0677 | `1` | high | articulated |
| `LP3` | OF-0646 | `1` | medium | articulated | OF-0678 | `.NR` | .NR | .NR |
| `AP1` | OF-0647 | `.NR` | .NR | .NR | OF-0679 | `.NR` | .NR | .NR |
| `AP2` | OF-0648 | `.NR` | .NR | .NR | OF-0680 | `.NR` | .NR | .NR |
| `AP3` | OF-0649 | `.NR` | .NR | .NR | OF-0681 | `.NR` | .NR | .NR |
| `AP4` | OF-0650 | `1` | medium | articulated | OF-0682 | `.NA` | .NA | .NA |
| `TS1` | OF-0651 | `1` | high | articulated | OF-0683 | `1` | high | analyst-imposed |
| `TS2` | OF-0652 | `open` | high | .NR | OF-0684 | `open` | high | analyst-imposed |
| `TS3` | OF-0653 | `P` | medium | .NR | OF-0685 | `.NR` | .NR | .NR |
| `TS4` | OF-0654 | `P` | low | .NR | OF-0686 | `0` | medium | analyst-imposed |
| `CI1` | OF-0655 | `common` | medium | .NR | OF-0687 | `common` | medium | analyst-imposed |
| `CI2` | OF-0656 | `1` | high | articulated | OF-0688 | `1` | medium | analyst-imposed |
| `CI3` | OF-0657 | `.NR` | .NR | .NR | OF-0689 | `.NR` | .NR | .NR |
| `CI4` | OF-0658 | `.NR` | .NR | .NR | OF-0690 | `.NR` | .NR | .NR |
| `LR1` | OF-0659 | `.NR` | .NR | .NR | OF-0691 | `.NR` | .NR | .NR |
| `LR2` | OF-0660 | `veiled` | medium | .NR | OF-0692 | `.NR` | .NR | .NR |
| `LR3` | OF-0661 | `0` | medium | .NR | OF-0693 | `0` | medium | analyst-imposed |
| `LR4` | OF-0662 | `0` | medium | .NR | OF-0694 | `1` | high | articulated |
| `LR5` | OF-0663 | `.NA` | .NA | .NA | OF-0695 | `diversifying` | medium | analyst-imposed |
| `LR6` | OF-0664 | `.NA` | .NA | .NA | OF-0696 | `.NR` | .NR | .NR |
| `MG1` | OF-0665 | `beneficiary` | high | articulated | OF-0697 | `membership` | high | articulated |
| `MG2` | OF-0666 | `collective` | medium | articulated | OF-0698 | `.NR` | .NR | .NR |
| `MG3` | OF-0667 | `.NA` | .NA | .NA | OF-0699 | `0` | high | articulated |
| `MG4` | OF-0668 | `religious` | medium | .NR | OF-0700 | `religious` | high | articulated |
| `FP1` | OF-0669 | `pious-charitable` | medium | .NR | OF-0701 | `mutual-provision` | high | articulated |
| `FP2` | OF-0670 | `.NR` | .NR | .NR | OF-0702 | `.NR` | .NR | .NR |
| `FP3` | OF-0671 | `P` | low | .NR | OF-0703 | `P` | medium | analyst-imposed |
| `FP4` | OF-0672 | `1` | high | articulated | OF-0704 | `P` | medium | analyst-imposed |
| `CF1` | OF-0673 | `0` | medium | .NR | OF-0705 | `0` | medium | analyst-imposed |
| `CF2` | OF-0674 | `.NA` | .NA | .NA | OF-0706 | `.NA` | .NA | .NA |
| `CF3` | OF-0675 | `multilateral` | medium | .NR | OF-0707 | `multilateral` | high | analyst-imposed |

**Tallies.**

- `avariz_vakfi`: 20 substantive, 8 `.NR`, 4 `.NA`. Confidence: high 5, medium 13, low 2.
- `bruderschaft_salzburg`: 17 substantive, 13 `.NR`, 2 `.NA`. Confidence: high 9, medium 8.

**Live `data.csv` equals `records/proposed-rows-mutual-pole-2026-09-04.csv`** on value, confidence and articulation for all 64 cells. Nothing changed at application.

**Two pre-existing defects, flagged and not repaired:**

1. The original coder's own tally (§2 of `NOTES-mutual-pole-coding-2026-09-04.md`: 21/7/4 and 16/13/3) disagrees with its rows.
2. `avariz_vakfi` carries `articulation=.NR` on **12 substantive cells**.

## 8. Withheld predictions

Scored at application in logbook 4. **Value agreement expected at about 48–54 of 64.** Disagreements should cluster on the cells the original notes themselves recorded as judgement calls. Metadata should come back weaker on balance, following the 2026-09-07 test-retest.

**`avariz_vakfi`**

1. `LP3` goes from `1` to `P` (weaker), on the trustee-standing reading, since standing is exercised through the *mütevelli*.
2. `MG2` goes from `collective` to `.NR` (no fitting value) or to a single-principal value (weaker), because many deeds name the trustee themselves.
3. `TS4` goes from `P·low` to `0`: the founder's *şart* binds.
4. `FP3` goes from `P·low` to `0` or `.NR`.
5. `TS3=P` reproduces, at about 60%; if it moves, it moves to `.NR`.
6. `CI1` is at risk of `several-accounts` if the coder scopes below the mahalle. The fixed scope makes this less likely than it would be in an open pass.
7. `LR4=0` is at risk of `P`, if the collective relief of a community levy is read as pooling.
8. At least one of the entity `.NR` cells becomes substantive, `AP1` most likely. The trap is the sentence that the waqf's claim carries no privilege over other claims.
9. `AP3` and/or `LR1` are at risk of `.NA` rather than `.NR`.
10. `AP4=1`, `TS1`, `TS2`, `CI2`, `MG1`, `FP1`, `FP4`, `CF1` and `CF3` reproduce.
11. The coder fills `articulation` on cells the original left `.NR`: a metadata difference, not a value one.

**`bruderschaft_salzburg`**

12. `MG2` goes from `.NR` to `collective` (stronger), taking the *selbständige* type as the norm.
13. `LP3` goes from `.NR` to `P` (stronger), on the Pfleggericht *Amtshilfe* passages.
14. `LR5=diversifying` is at risk of `.NR`.
15. At least one of `FP3=P` and `FP4=P` moves.
16. `FP1=mutual-provision` reproduces, with `pious-charitable` as the risk. The asymmetry in §6 makes a move here more likely, not less.
17. `LR4=1`, `MG3=0`, `MG4`, `TS1`, `TS2`, `CI2`, `LR3=0`, `CF1`, `CF3` and `AP4=.NA` reproduce.

**The antecedent limit does not bite in this batch.** Whole forms are re-coded, so the coder resolves `CF1`, `LR2`, `LR4` and `MG1` itself, and every dependent cell is coded against its own antecedent.

## 9. Channel check

**Prompt against §8.** Read back sentence by sentence. Two sentences were deleted:

- one inviting the coder to object to the scope, which pointed at predictions 2 and 6;
- the doctrine sentence on `P`, which is in `CLAUDE.md` and was amplified in the prompt against predictions 3, 4 and 15.

**No sentence of §8 appears in the prompt.** The prompt names no characteristic value and no characteristic by name, beyond `LP1` and `CF3` as the ends of the id ranges.

**Skill files against §8.** These cannot be removed (the skills are read-only) and are disclosed here:

- `code-a-form`: *"A column that already carries a zero-instance value gets worse, not better, when given a second — the `AP4` lesson"*. This bears on prediction 10 (`AP4=1` reproduces, `P` declined). It does not name the form.
- `code-a-form` and `run-a-coding-batch`: `confraternita` given twice as the example of *"an uncoded row with a reasoned refusal"*. This tells the coder the umbrella exists, which the bundle's type vocabulary shows anyway. It states no value of `bruderschaft_salzburg`.
- `run-a-coding-batch`: `_blind-mutual-pole-2026-09-04` and `mutual-pole-scheme` as examples. These name the earlier batch, not its values.
- `code-a-form`: *avarız* as a Zotero search-term example. Harmless, and the coder is forbidden Zotero.

The prompt tells the coder to report anything in a loaded skill that appears to imply a value. It does not name these items, because naming them would point at them.

## 10. Standing-table row (filed in logbook 4)

`opus55-recode-mutual-pole-scheme` | 2026-09-26, operator | What it read:

- the whole live `organizational_forms` rows for `avariz_vakfi` and `bruderschaft_salzburg` (all 64 cells with values, confidences, articulations and notes) and `records/proposed-rows-mutual-pole-2026-09-04.csv`, diffed against them;
- `records/NOTES-mutual-pole-2026-09-04.md` §§4 and 12.2 and `records/NOTES-mutual-pole-coding-2026-09-04.md` in full;
- the original bundle's `SESSION-PROMPT.md` and `CODING-BRIEF.md`;
- the two type rows in full; the `source_ref` fields of the two loss-census siblings;
- this table in full; the logbook headings for 2026-09-04 to 09-06;
- the vocabulary fields that name these forms (sub-pool paragraph, `AP4` count, `confraternita`, `joint_stock` and `confraternity_fund` `key_source`) and four loss-census neighbour notes, all in order to redact them.

It ran vault term counts per slug (rungs 1 and 3) and **by accident printed about 55 titles of withheld notes** from a build log (rung 4, unbudgeted). It read one snippet of `isqa-qirad-commenda`. It re-measured the five offsets.

Prejudices any later blind coding of `avariz_vakfi` and `bruderschaft_salzburg` on every characteristic, of the two loss-census siblings, of `confraternita`'s scope, and of `AP4` generally. Brief at `records/NOTES-opus55-recode-mutual-pole-2026-09-26.md`.

## 11. What MS does next

1. Commit this brief, the empty priors template and the prompt in live `records/`, **or** at least this brief. It must not reach the coder, and it cannot, since the bundle is already built.
2. Open the coding chat as the prompt's header says, with **only** `~/GitHub/_blind-opus55-mutual-pole-2026-09-26` granted, and paste the prompt.
3. **When the coder says its priors are written:** copy `~/GitHub/_blind-opus55-mutual-pole-2026-09-26/HistorEE_codebooks/records/PRIORS-opus55-recode-mutual-pole-2026-09-26.md` over the live `records/` template and **commit it**. Only then tell the coder to open the sources. **This is the one commit that must precede the coding.**
4. Application (Chat C, later): copy the coder's rows into live `recodings.csv`, fill `value_at_recoding` from §7 and `agreement`, score §8 in logbook 4, and copy the bundle's `proposed-of/` record into `records/`.
