# Forms selection — `deed_of_settlement_company`, shielding re-coding, 2026-09-07

**Operator session (Chat A). Slug `deed-of-settlement-shielding-recode`.** Nothing coded, no cell changed, `data.csv` untouched by this brief, no `git` run. Written by the session that read Getzler & Macnair, whose blind on these cells is therefore wholly spent — which is why the coding goes to a fresh chat.

Census at the start: `organizational_forms` **833 rows, 44 form codes, 33 coded forms, version 0.9.0**, gaps at `OF-0032` and `OF-0033`.

## 1. What is being re-coded, and what is not

**`deed_of_settlement_company`, five cells only: `AP1`, `AP2`, `AP4` (entity-shielding) and `AP3`, `LR1` (owner-shielding).** Coded **de novo**, not reviewed: the existing five are withheld from the bundle so that the coder reaches its own values and the two sets are compared afterwards. The other 27 cells are untouched, because no new evidence bears on them and re-coding a cell without new evidence invites drift rather than testing anything.

**SCOPE OF THE FORM, unchanged from 2026-09-05 and reproduced in the coding prompt because the type row is withheld:** the English **unincorporated joint-stock company constituted by deed of settlement**, c.1720–1844 — a partnership whose elaborately drafted articles excluded the default partnership rules and settled legal title to the circulating trade assets on a fixed body of trustees, with control divided between directors, a general court of proprietors and those trustees. Constitutive instrument: the deed of settlement, a private deed, with no Royal Charter, patent or Act. **Out of scope:** the testamentary trading trust; the ordinary Regency partnership of owner-managers; jointly run shipping and mining businesses; and chartered or statutory corporations.

## 2. Why now — the trigger, stated so the coder's independence can be judged

`AP1=1` sits at `high` confidence on **one source**. On 2026-09-07 a second was read and it describes the same doctrine very differently in weight: robust from 1682 and entrenched by statute in 1825, against the existing coding's derivative-and-defeasible reading. **That is a disagreement between two readings of one rule, and this census records disagreement as a coding rather than as a verdict.** Whether it changes a value is exactly what the re-coding is for.

## 3. Sources

1. **Televantos, A., *Capitalism Before Corporations* (OUP 2020)**, DOI `10.1093/oso/9780198870340.001.0001`, offset `printed = PDF − 25` verified 2026-09-05 at printed 15, 35, 55, 75, 105, 143 and 175. **CHAPTERS 3–6 WERE NEVER READ** by the 2026-09-05 batch and are squarely on this batch's question: `…003.0003` *The Use of Trusts in Business Structures* (31–60), `…003.0006` *The Authority of Trustees and Executors* (101–118), `…003.0007` *Trusts and the Risk of Bankruptcy* (121–142). **Reading them is the largest single gain available and costs nothing.**
2. **Getzler, J. & Macnair, M., 'The Firm as an Entity before the Companies Acts'**, in Brand, Costello & Osborough (eds), *Adventures of the Law* (Four Courts Press, Dublin, 2005), 267–288; Zotero `ES5SAP4D`, repaired 2026-09-07. **CITATION LIMIT, AND IT BINDS THE CODING:** the held PDF is the Oxford working paper No 47/2006, not the Four Courts printing, and carries **no folio marks**, so the offset cannot be measured and **no cell may cite a printed page from it**. Cite by section heading and case name, or acquire the printing.

## 4. Non-independence — ONE REQUIRED CHECK IS UNPERFORMED AND THE CODER MUST DO IT FIRST

**Televantos 2020 post-dates Getzler & Macnair 2005 by fifteen years and may cite it.** If he does, agreement between them on the jingle rule is one claim and its echo, not two witnesses. **This has not been measured and no cell may treat them as two witnesses until it is.** The coder's first act is a term count of `Getzler` and `Macnair` across Televantos's full text, with every hit's context read, reported in the deliverable whatever it returns.

**Known already:** Getzler & Macnair cite **Harris 2000** four times and rely on him for the Bubble Act, Eldon, and the assimilation of deed-of-settlement companies to partnership — so they are **not** independent of Harris there, and Harris is a coded source in this census. They cite **Hansmann & Kraakman 2000**, so unlike Harris they are inside the framework `AP1`'s wording comes from. They cite DuBois and Hunt only as orthodoxy to argue against.

## 5. Co-occurrence — nothing new to declare

The row exists and its declarations stand: `joint_stock` and `friendly_society_england@loss_mitigation_forms`, both at `same-polity`, with the reverse declaration in the latter's `key_source`. A `chartered_corporation_england` reverse declaration was added to this row's `key_source` on 2026-09-07 and is withheld with it. **No new relation is created by a re-coding.**

## 6. The blind — what it protects, what it cannot, and one bounded leak disclosed

**The bundler could not blind a re-coding until today.** `--withhold-types` removed `data.csv` rows and every `codebook.md`, but left the **vocabulary type row** (whose `key_source` states the reasoning under test) and **all nine views** (which tabulate the withheld values) in place. Both fixed ahead of this batch; see logbook 3, 2026-09-07.

**`chartered_corporation_england` is withheld as well, and not for tidiness.** Its `AP1` cell note, written 2026-09-07, names Getzler & Macnair, the jingle rule and this row's `AP1` outright. A test bundle withholding only `deed_of_settlement_company` left `jingle`, `Getzler` and `Macnair` standing in `data.csv`. Withholding both types removes them; verified by grep on the test bundle.

**THE BOUNDED LEAK THAT REMAINS, DISCLOSED RATHER THAN PAPERED OVER.** `vocabularies/organizational_form_characteristic.csv` **must survive** — the coder needs `allowed_values`, `applicability_on` and the definitions — and the `entity`-locator text repeated across eight definitions says of this very form that its trust *"settles LEGAL TITLE over one undivided joint stock rather than partitioning it… and the partners' separate estates lie outside the arrangement and are the very thing AP1 measures against, so reading them as sub-pools would make AP1 predict itself."* **That is a scoping and locator statement, not a value**, and it is the reason the sub-pool audit returned this form as non-sub-pool. **The coder will see it. It is not scrubbable without destroying the vocabulary.** Recorded here so that no one later mistakes it for independence. The new manifest lists 39 such residual mentions for hand review.

**Vault:** not opened by this session and not needed. The form-specific counts were zero on the 2026-09-05 sweep and no question here requires a note.

## 7. The bundle command

**BUILT 2026-09-07. This is the command as actually run, and it gained two slugs the first draft did not have.**

```sh
python3 scripts/make_blind_bundle.py \
  --out ~/GitHub/_blind-deed-of-settlement-recode-2026-09-07 \
  --codebooks ~/GitHub/HistorEE_codebooks \
  --vault ~/GitHub/myfoamrepo \
  --withhold-types deed_of_settlement_company,chartered_corporation_england \
  --withhold-dates 2026-09-05,2026-09-06,2026-09-07 \
  --withhold-sessions shielding-witness-coding,shielding-witness-scheme,chartered-corporation-scheme,chartered-corporation-coding,joint-stock-scope-scheme,joint-stock-scope-verification,mutual-pole-application,harris-omega-naties,deed-of-settlement-shielding-recode
```

**`harris-omega-naties` was added because the vault carries `Harris 2020 on the late plurality of limited liability`** — two notes under that slug — and `AP3` and `LR1` are two of the five cells under test. In this vault a filename is a claim, and `joint-stock-scope-scheme` is quarantined for having read that very title. The five form-specific terms (`deed of settlement`, `jingle`, `joint estate`, `separate estate`, `Televantos`, `Getzler`, `Macnair`) return **zero** across the vault, as §6 predicted; it is the liability chronology, not the form, that the vault could have leaked.

**`deed-of-settlement-shielding-recode` — this session's own slug — was added because logbook 4's standing table is not a dated section and nothing scrubbed it.** The first built bundle contained this session's own row, naming the five cells, both sources and the doctrine. The script now drops standing-table rows by slug, and **the operator must list their own slug**; the script cannot infer it.

**Then, by hand, before the coder is given the path — ALL OF THIS WAS DONE ON 2026-09-07 and the bundle is built; the steps are kept as the record and as the recipe for the next re-coding:**

1. **Redact `datasets/organizational_forms/data.csv`, `compagnie_antwerpen_1582` `AP2` (`OF-0744`).** Its note ends *"see … the `deed_of_settlement_company` AP2 note. Both that row and this one read P and the two P's are not the same state, so they are not agreement."* **That states one of the five values under test.** Cut from "and the `deed_of_settlement_company` AP2 note" to the end of the sentence; the well-formedness flag and the `PATCH-AP2` pointer before it can stay. Found by the new residual audit on its first run, and by nothing else.
2. **Read the rest of the manifest's RESIDUAL MENTIONS section.** Dry-run on 2026-09-07 returned **27** entries. The other 26 are judged safe and the reasoning is recorded so it need not be redone: eight are the `entity`-locator text in `organizational_form_characteristic.csv`, disclosed to the coder in the prompt (§6 above); five state values of this form on characteristics **outside** the batch's five (`FP2=0`, `CF3=multilateral`, `MG1=.NR`) and the blind covers the cells under test, not the whole row; five are logbook 1 and logbook 4 lines that name the form without a value; the rest are scope and co-occurrence prose in the `joint_stock`, `compagnie_antwerpen_1582`/`1608` and `friendly_society_england` rows, which the coder needs. **The `joint_stock` row does state `deed_of_settlement_company` `LP1=0`** — outside the five, and it is the boundary rule the coder must have.
3. **Sweep the vault half of the real manifest by hand as well.** The audit covers both halves, but the machine this brief was written on could not reach `myfoamrepo`, so the vault path is tested only against a synthetic vault. Vault notes are removed by session slug; a note from an unlisted session can still state a value.
4. **Copy the two source PDFs into `sources/`** — the script has no source option and never has. Do not grant the Zotero store instead: it hands the coder 400+ PDFs and a second witness to find.
5. **No `record_id` is needed.** This is a re-coding of five existing cells, not an append: the prompt tells the coder to use placeholders and says the maintainer reconciles the five proposed rows against the five they replace. *(Corrected 2026-09-07: as first written this step told the operator to supply the next free id, which is the first-coding instruction and would have invited five new rows beside the old ones.)*

## 8. WITHHELD FROM THE CODER — predictions, so that falsification means something

**Not to be given to Chat B, and the prompt has been read back against this section line by line.**

1. **`AP1` returns `1`.** Both readings agree the joint estate went to joint creditors first; they differ on how securely.
2. **`AP2` returns `P`, with a changed note.** The creditor limb gains a substantive rule from *Ex parte Elton*; the member limb is unchanged. If the coder raises confidence, that is the second source working.
3. **`AP3` returns `0`.** Getzler & Macnair's "veil" is asset partitioning between classes of creditor, not shielding of partners from venture creditors. If the coder reads their *quasi*-limited-liability language as `P`, that is the error this prediction is for.
4. **`LR1` returns `unlimited-joint`.**
5. **`AP4` returns `.NA`.** No founder; the form arises by deed. The zero-instance prohibition passes a sixth batch.
6. **The coder will find the Televantos / Getzler-Macnair difference and want to record it as a disagreement rather than pick a winner.** This is the one I most want to see reached independently.
7. **No zero-instance value filled.** `AP4=P`, `AP4=0` and `LR1=none` are all empty and none of them fits.
8. **The coder will find that `AP4`'s own definition states a stale form count** — it says "two coded forms and one value between them" and there are now three.
9. **The `Getzler` count in Televantos will be non-zero**, and the two will prove less independent than they look.

## 9. This session's row for the standing spent-blind table

Budget was declared before reconnaissance and is reconciled in logbook 4, 2026-09-07 (ii). **It ended one rung below budget:** rung 2 was planned and spent on the bundler; rung 5 on the matrix was planned and spent only on the five columns' distributions, which this session had already seen; the vault was budgeted at rung 0 and not opened at all.

## 10. The Chat B prompt, and what was cut out of it

`proposed-of/PROMPT-deed-of-settlement-shielding-recode-2026-09-07.txt`, written after this brief and **read back against §8 line by line**, on the standing lesson from 2026-09-06 when the first chartered-corporation prompt handed the coding chat two of its own predictions and had to be withdrawn by the coder rather than the operator.

**One paragraph was written and then deleted.** It told the coder that where the two sources differ the difference is itself a finding, and not to average them or resolve them quietly in the note. That is prediction §8.6 — *"the coder will find the difference and want to record it as a disagreement rather than pick a winner"*, the one this brief most wants reached independently — and putting it in the prompt would have made the prediction unfalsifiable. It is also **redundant**: `code-a-form` already says "where scholars disagree, record the disagreement as a coding, not a verdict", and the prompt's first line loads that skill. **A prompt sentence that restates the doctrine the coder is about to load is never worth its leak risk.**

Checked absent from the prompt by term count: `Elton`, `unlimited`, `jingle`, `1682`, `1825`, `veil`, `founder`, `.NA`, `zero-instance`, `disagree`, `verdict`. The prompt does not name which source triggered the re-coding, or in which direction either reading runs.

## 11. The bundle as built, 2026-09-07

`~/GitHub/_blind-deed-of-settlement-recode-2026-09-07`, from codebooks `faa6e378` and vault `4257039d`.

- **769 rows, 31 types** against 833 and 33 live; 64 rows and 2 vocabulary rows removed; nine views regenerated from the scrubbed data; three codebooks and `CHANGELOG.md` deleted; 8 standing-table rows and 2 vault notes removed, 13 files dereferenced, `graph.svg` deleted as stale.
- **Two hand redactions performed:** `OF-0744`'s `AP2` note, cut at *"and the `deed_of_settlement_company` AP2 note…"* to the end of the sentence, which stated a cell under test; and — made unnecessary by the standing-row rule and so not carried into the final build — logbook 4's two quotations of the withheld note title.
- **Sources copied in by hand:** `sources/Televantos_2020_Capitalism_Before_Corporations.pdf` (225 PDF pages; **offset `printed = PDF − 25` re-verified in the bundle at PDF 56, 126, 146 and 200**, and the three unread chapters' DOIs land exactly where §3 said — `…0003` at printed 31, `…0006` at 101, `…0007` at 121, so the file is the whole book despite its ZotMoov filename) and `sources/Getzler_Macnair_2005_The_Firm_as_an_Entity.pdf` (19 pages, working-paper version, no folio marks, as §3 warns).
- **The prompt sits at the bundle root**, as on 2026-09-06, and `proposed-of/` is created empty for the coder's deliverables. `proposed-of/` is gitignored, so **no earlier batch's brief or prompt is in the bundle** — verified.
- **Zero across both repos:** `jingle`, `Getzler`, `Macnair`, `Holdsworth`, `Ex parte Elton`, and both withheld note titles. **22 residual mentions** remain, all reviewed under step 2 above.
- **The bundle checks clean against itself:** `check_vocabularies.py` at 164 codes, `check_dependence.py`, and `build_views.py --check` reporting the regenerated views consistent with the scrubbed data.

**Three further defects in `make_blind_bundle.py` were found while building it** — the unregenerated `graph.svg`, the line-oriented wikilink dereferencer, and the unscrubbed standing table — and are logbook 3, 2026-09-07 (ii). **All three are in the vault half or in prose the morning's patch had trusted, and none would have been found by reading a manifest.** The rule that follows: build the real bundle before writing the logbook entry, not after.

**`OF-0836` is the next free `record_id`**, per the manifest. The prompt does not use it — the coder writes placeholders and the maintainer reconciles five rows against five — but it is recorded here because the manifest is not kept.

**AMENDED after the bundle was built, and only about absence.** The banner now names the two removal surfaces the first draft could not know about — **standing-table rows** and the deleted **graph artefact** — and says that two passages were **redacted by hand, one inside another form's cell note**, so that a truncated note is not read as a statement about the form under test. A second paragraph says that cell notes and logbook entries cite files under `proposed-of/`, which is not shipped, and that a dangling reference is not a hole to fill. **Neither amendment adds content**: the leak-term check returns zero on all eleven terms, `Getzler` excepted, which the prompt must name because measuring him is the coder's first act.
