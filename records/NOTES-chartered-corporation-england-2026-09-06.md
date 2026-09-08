# Forms selection — `chartered_corporation_england`, 2026-09-06

**Operator session (Chat A). Slug `chartered-corporation-scheme`.** Nothing coded, no row proposed, `data.csv` untouched, no `git` run. Written by the session that verified Harris 2000, whose blind on this material was already spent — which is why the selection work is done here rather than in the coding chat, where it would destroy the blind it needs.

Census at the start: `organizational_forms` **801 rows, 43 form codes, 32 coded forms, version 0.9.0**, with `record_id` gaps at `OF-0032` and `OF-0033`.

## 1. The form, and its boundaries

**`chartered_corporation_england` — the English business corporation incorporated by Royal Charter, letters patent or Act of Parliament, c.1600–1844.** Constitutive instrument: the charter or the Act. The pool is the joint stock; the members are the shareholders.

**It is the row `joint_stock` should have been.** `joint_stock` was retired to an uncoded umbrella on 2026-09-06 precisely because it spanned a family rather than naming a form; this row takes the referent its `LP1=1` cell note ("chartered legal personhood") always had, narrowed to one polity so that it does not sit above the `voc` rows.

**NOT, and each exclusion has a reason:**

- **NOT `deed_of_settlement_company`**, which is the unincorporated counterpart, 1720–1844, `LP1=0`. The two differ on the first characteristic either touches, by construction. Televantos's glossary makes "joint stock company" a synonym for the unincorporated form, so **where a source uses that phrase of an English concern between 1720 and 1844 the coder must establish that the passage bears on a CHARTERED entity before any cell takes a value from it**, and must say so in the cell note.
- **NOT the VOC**, and not any Dutch company. The `voc_1602/1612/1623` rows exist and are coded from other sources. Harris discusses the VOC at length; **that material is out of scope and must be coded from nowhere.**
- **NOT the umbrella `joint_stock`**, which now carries zero cells and must stay that way.
- **NOT the pre-1600 regulated corporation, the guild, the municipal or ecclesiastical corporation.** Harris's chapter 1 and chapter 2 cover them; they are a different institution and this row is the *business* corporation with joint-stock capital.
- **Period question the coder must settle and not assume:** Harris's book runs 1720–1844 in its title but his chapter 2 reaches back to the 1550s. **Whether this row starts at 1600 (with the EIC) or 1720 (with the Bubble Act) is a scope decision, and the coder should propose it with evidence rather than inherit it from the title.** The `deed_of_settlement_company` precedent is a warning: its period claims 1720–1844 while every coded cell rests on 1790–1827 evidence.

## 2. The source, verified

**Harris, R., *Industrializing English Law: Entrepreneurship and Business Organization, 1720–1844*, Cambridge University Press. CITE AS `Harris 2000`.**

- **Edition, and it is not what was ordered.** The PDF is **CUP's 2004 electronic edition of the 2000 first-edition typesetting** — copyright page "© Cambridge University Press 2004 / First published in printed format 2000", distilled from PostScript 26 August 2004. Not the 2011 paperback reprint, not the "2010" of its ZotMoov filename. **The pagination is the 2000 first edition's, which is what the literature cites.** Four dates attach to this book; use 2000.
- **Offset `printed = PDF − 18`**, derived independently: **301 of 312 folio hits agree**, continuous PDF 20 → 349, plus **eight structural checks** against the Contents (ch. 1 at printed 14, ch. 2 at 39, ch. 3 at 60, ch. 6 at 137, ch. 8 at 201, Conclusion 287, Bibliography 301, General Index 326), all exact. 349 PDF pages, 941,433 characters, clean text layer, no OCR needed.
- **What it answers**, by whole-book term count: `incorporat*` 572, `joint-stock` 558, `trust` 438, `partnership` 333, `unincorporated` 273, `charter` 180, `monopoly` 115, `limited liability` 83, `transferab*` 82, `shareholder` 75, `legal personalit*` 23, `sue and be sued` 16, `dissolution` 15, `unlimited liability` 4, `perpetual succession` 3.
- **What it does NOT answer, and the coder must not paper over it.** `creditor` occurs **13 times in 331 pages, and seven of the thirteen are the PUBLIC creditors of the State** — the national debt and the South Sea conversion. The remainder bear on members' liability *to* creditors, which is `AP3`/`LR1`, not on creditor priority *in entity assets*, which is `AP1`/`AP2`. **`AP1` and `AP2` must not be filled by inference from the liability material one column over.**

## 3. Holdings: this is a single-witness row, and that is the batch's main weakness

**Measured, not assumed.** Of the obvious second witnesses, **only one is held**: `Dari-Mattiacci et al. 2013, The Emergence of the Corporate Form`. Not held: DuBois 1938, Scott, Shannon, Holdsworth, Kyd 1793, Blackstone, Freeman/Pearson/Taylor, Hilt, Morley 2016, Turner, Acheson, Guinnane, Lamoreaux, Ireland, Johnson, Micklethwait, Bainbridge.

**And the one held witness is an awkward one, in a way that must be declared before a cell is written:**

1. **It is already in this census** as the source of `voc_1602`, `voc_1612` and `voc_1623`. Coding it here would enter one source twice, and no agreement between this row and any `voc` row on a cell drawn from it is a finding.
2. **Harris rejects it by name.** At Harris 2020, printed 646–647: *"I think that this interpretation of historical facts is misjudged."* So the two witnesses **actively disagree**, which under the `bazacle_mill FP1=mixed` disposition is codeable as a disagreement and is arguably worth more than agreement would be — but it is not corroboration and must not be recorded as such.

**Recommendation: code from Harris 2000 as principal source, use Dari-Mattiacci only on the EIC and only with the two declarations above in the cell note.** State in the type row that the row is effectively single-witness. This is the same weakness that killed the `AP4` testamentary-trust batch on 2026-09-05; it is accepted here because Harris 2000 is a full monograph squarely on the form and wholly outside the HKS grid, which no other held source is.

## 4. Non-independence, declared BEFORE any row exists

- **Harris 2000 and Harris 2020 are ONE AUTHOR TWICE.** Harris 2020 §2.3 — shareholders not arrestable, the act of 1662, the judgment of 1671 — is a compressed restatement of Harris 2000 **printed 128**, same three indications in the same order. **No cell may count them as two witnesses**, and the `joint_stock` type row already carries this declaration.
- **Harris 2000 and Morley 2016 share DuBois 1938** (`dubois` 26 hits in Harris 2000). If Morley is ever acquired, agreement on eighteenth-century unincorporated material may be DuBois read twice.
- **Harris 2000 is INDEPENDENT of HKS 2006** — `hansmann` 0, `kraakman` 0, `squire` 0, measured across the full text. It predates them by six years. **This is the corrective the shielding-witness brief §11.3 asked for and could not get**, and it is the strongest single reason to run this batch: `compagnia`, `deed_of_settlement_company` and both Antwerp rows all sit inside the HKS grid, and this row will not.
- **Independent of Televantos and of Morley as authors** (`televantos` 0, `blair` 0, `freeman` 0, `pearson` 0; the two `morley` hits are John Morley on Gladstone, 1903, checked by reading the contexts).

## 5. Co-occurrence, declared before the row exists

- **`deed_of_settlement_company` at `same-polity`** — same polity, overlapping century, contrasting regimes, no shared source. The chartered/unchartered pair is the point.
- **`joint_stock`**: NOT declared. It is an uncoded umbrella and this row is what it should have been; a co-occurrence between a row and the umbrella it replaces is not an institutional relation.
- **NOT declared against `voc_1602/1612/1623`**, and the absence is deliberate: Harris treats the EIC and VOC together, but that is a **scope rule**, not a co-occurrence. If Dari-Mattiacci is used the *evidential* relation must be recorded in prose, because `cooccurrence_basis` holds one basis per row — fifth recurrence of the single-basis defect.
- **The reverse declaration** must be written into `deed_of_settlement_company`'s `key_source` prose, since its `cooccurrence_basis` is already `same-polity` and pointing elsewhere.

## 6. The blind: what it protects here, and what it does not

**Vault, measured at rung 1 (term counts only — no title opened, no body read):** the vault is **clean on this form**. `chartered corporation` 0 files, `Bubble Act` 0, `Royal Charter` 0, `letters patent` 0, `unincorporated` 0, `Companies Act 1844` 0, `quo warranto` 0, `corporate personality` 0, `Harris 2000` 0, `Industrializing English Law` 0, `DuBois` 0. `East India Company` **1 file / 4 hits**. Per the standing rule, a count can prove a vault clean and only a title can prove it dirty, so **the counts were accepted and no title was opened.**

**Dirty on the frame, not on the form.** 53 files mention Harris; 37 of those also carry a liability or shielding term. Their `source-session` slugs, obtained at rung 3 without rendering a filename:

| slug | notes | |
|---|---|---|
| `ron-harris-tradeoffs` | 24 | **withhold** |
| `eic-voc-archives` | 6 | **withhold** — the EIC is this form's central instance |
| `harris-omega-naties` | 2 | **withhold** — holds the note whose title spent the Harris 2020 blind |
| `referee-round-5` | 16 | MS's call |
| `isqa-qirad-commenda` | 14 | probably not — Islamic partnership, Harris appears for the *commenda* |
| `cooperation-synchrony` | 2 | probably not |

**A measurement that failed, recorded as a failure.** An attempt to score each slug for English-frame specificity returned 24/24, 2/2, 6/6, 16/16, 14/14 and 2/2 — 100% everywhere, because "charter", "English" and "Parliament" saturate an entity-shielding vault. **The filter discriminated nothing and its output is not evidence.** The form-specific terms being 0 vault-wide is the real answer.

**THE HONEST CAVEAT, AND IT SHOULD DECIDE HOW MUCH WEIGHT THE RESULT CARRIES: the vault blind is weak here, because the source IS Harris.** Withholding the vault's notes about Harris's argument does not blind the coder to Harris's argument — the coder reads it directly, at length, in the book. What the vault blind buys is narrower: it stops the coder arriving with the *census's accumulated* view of the limited-liability chronology, which is Harris 2020's later and stronger claim, and confirming it.

**PER-TOPIC SCOPE, ADDED 2026-09-06 (iv) AT THE CODING CHAT'S REQUEST, AND IT IS THE RIGHT WAY TO STATE THIS.** The frame is dirty and the mechanism is clean, in the 09-05 brief's own terms, and the spend is asymmetric: **operator-side the limited-liability chronology is spent** — `joint-stock-scope-scheme` read a note title stating Harris 2020's thesis, and this brief's own §4 restates the relation between that article and printed 128 — while **coder-side, inside a correctly built bundle with a non-leaking prompt, it is not**, because the three withheld slugs carry it and the coder meets the argument only in the source. **CONSEQUENCE THAT MUST BE DECLARED IN THE TYPE ROW: agreement between this row's `AP3` or `LR1` and Harris 2020's chronology is NOT independent corroboration.** It is one author's argument reaching the census twice, once through the source and once through the operator who chose the source. Declare it; do not let the bundle imply it was tested.

**THE BUNDLE IS NEVERTHELESS WORTH BUILDING, AND FOR THE OTHER REASON: the matrix blind is fully intact and nothing has spent it for this form.** The coder must not see the zero-instance table, the one-instance table, or the coded values of `deed_of_settlement_company` and the `voc` rows — otherwise "a zero-instance value was filled" means nothing, and the coder can tune values to separate this row from its neighbour. **That is what this bundle is for.** The vault withholding is secondary and cheap.

## 7. The bundle command

```sh
python3 scripts/make_blind_bundle.py \
  --out ~/GitHub/_blind-chartered-corporation-2026-09-06 \
  --codebooks ~/GitHub/HistorEE_codebooks \
  --vault ~/GitHub/myfoamrepo \
  --withhold-sessions ron-harris-tradeoffs,eic-voc-archives,harris-omega-naties
```

**THE SOURCE IS NOT IN THE BUNDLE AND THE SCRIPT WILL NOT PUT IT THERE.** `make_blind_bundle.py` copies only `--codebooks` and `--vault`; it has no source option. Harris 2000's PDF must be copied into the bundle by hand — `sources/` alongside the two repos — **before** the coder is given the path. Granting the Zotero store instead is the worse arrangement: it hands the coder 412 PDFs to browse and a second witness to find, and this row is declared single-witness. Check what the three existing bundles did and follow it.

**`--withhold-types` is deliberately omitted: this is a FIRST coding, not a re-coding**, so no rows are removed and the coder takes the next free `record_id` from the tree. **Note for whoever checks the manifest: `data.csv` is 801 rows with a last id of `OF-0803` and gaps at 32–33, so row count and last id no longer agree.** The next free id is **`OF-0804`**.

## 8. Withheld from the coder deliberately — predictions, so that falsification means something

**These are this session's expectations, recorded before any cell exists and NOT to be given to Chat B.** **CORRECTION, 2026-09-06 (iv), and it is against this brief's own author: the FIRST PROMPT WRITTEN FOR CHAT B GAVE THREE OF THEM AWAY.** `PROMPT-chartered-corporation-coding-2026-09-06.txt` handed the coder the `creditor` 13-hits/seven-public measurement together with an instruction not to fill `AP1` or `AP2` — which is prediction 1 below, verbatim in substance — and quoted the source's own conclusion at printed 128–129 on `LR1` and `AP3`, which is predictions 2 and 3. **The bundle cannot scrub the prompt, so the prompt is the one channel the blind does not cover, and this brief's author used it to leak this brief's own withheld section.** Caught by the coding chat before a cell was written, not by me. v1 is kept and marked; `PROMPT-chartered-corporation-coding-v2-2026-09-06.txt` supersedes it and names no page and no conclusion. **Standing lesson for the next operator: write the prompt, then read it back against the withheld section and delete every sentence that appears in both.** Reconcile them against the coder's output afterwards; a falsified prediction is the batch's main product.

1. **`AP1` and `AP2` will be `.NR`.** Predicted from `creditor` = 13 hits, seven of them about the State's creditors. If the coder returns substantive values here, either the prediction is wrong or the cells are inferred, and the cell notes will show which.
2. **`AP3` = `0`.** Harris's whole thesis is that owner shielding was absent in this period.
3. **`LR1` will be `.NR` or contested.** Printed 128–129 says in terms there was "no coherent, well-defined conception of limited liability" and sets out the paid-up / unpaid-balance / above-nominal gradation as a question contemporaries confused. **This is the row that would show whether `LR1` needs the multiple-of-subscription value** — but the regimes that need it postdate 1844, so probably not here.
4. **`LP1` = `1`, `LP2` = `1`, `LP3` = `1` or `P`.**
5. **`MG4` = `state-charter`.** Would be the eleventh instance.
6. **`FP2` = `1`** (`monopoly` 115 hits).
7. **`FP4` = `0`** before 1844, flipping at the Companies Act — the same boundary `deed_of_settlement_company` records.
8. **`TS1` = `1`, `TS2` = `open`.**
9. **No zero-instance value will be filled.** The ten empty values are `AP4=P`, `AP4=0`, `TS4=1`, `LR1=none`, `LR2=attenuated`, `LR3=P`, `LR4=P`, `LR5=na`, `LR6=downside-only`, `MG3=P`, and this form is not founder-endowed, not a pooling arrangement, and not a candidate for any of them. **`AP4` will be `.NA` and the prohibition will pass a fifth batch.**
10. **The risk-pooling and loss-sharing facets will learn nothing**, as they did on all three of the last batch's rows.

## 9. This session's row for the standing spent-blind table

| slug | session | what it spent |
|---|---|---|
| `chartered-corporation-scheme` | 2026-09-06, operator | Ran **term counts only** over the vault for 17 form-specific and frame terms — no title opened, no body read — and extracted `source-session` slugs at rung 3 for the 37 Harris-plus-liability notes without rendering a filename. Read the live `organizational_forms` `data.csv` at 801 rows and computed the full zero-instance and one-instance value tables on it, plus the value distributions of the sixteen columns this form would touch. Listed the ZotMoov store for second witnesses and read `make_blind_bundle.py`'s interface. **Carries forward everything spent by `joint-stock-scope-verification` the same day**, including Harris `6FN9JG5S` read in full and Harris 2000's front matter, offset, term counts and printed 127–129. Prejudices any later blind coding of `chartered_corporation_england`, `AP3`, `LR1`, `MG4`, `FP2` and the limited-liability chronology generally. Brief at `proposed-of/NOTES-chartered-corporation-england-2026-09-06.md`. |
