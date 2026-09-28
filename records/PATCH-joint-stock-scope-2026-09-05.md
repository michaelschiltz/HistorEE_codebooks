# Draft scope note for the `joint_stock` type row — for approval, NOT applied

Written 2026-09-05 by `ai` at the maintainer's instruction, after the shielding-witness coding pass. **Nothing has been written into `vocabularies/organizational_form_type.csv`.** This file is a draft for approval and a correction to something I already said.

---

## Correction, marked, because I got this wrong once already

`NOTES-shielding-witness-coding-2026-09-05.md` §5.3, the logbook draft, and the draft commit message all say that `joint_stock` is a type row **"with no scope note and no cells at all"**. The second half is **false** and the corrected text is now in those files with the same marking.

The error came from reading the `entity-shielding` view, where `joint_stock` shows `--` on `AP1`, `AP2` and `AP4` — three characteristics out of thirty-two. Counting rows by `type_id` in `data.csv` gives the real figure. **`joint_stock` carries two cells**, and 10 of the census's 40 type codes carry none (`waqf_ahli`, `ie`, `kabu_nakama`, `mudaraba`, `ortoq`, `piaohao`, `ton_ya`, `hegu_gangu`, `gugu_death_share`, `confraternita`). `joint_stock` is not among them.

The lesson is worth keeping: **a `--` in a scoped view means "no row on this characteristic", and a component view covers three or four characteristics, so it cannot tell you whether a form is uncoded.** Count in `data.csv`.

## What the two cells are, and why they settle the question

| | |
|---|---|
| `OF-0032` | `joint_stock LP1 = 1` · `high` · `articulation=.NR` · `Harris 2020` · `en` · `coder=ai` · `source_read=unknown` · note: **"chartered legal personhood"** |
| `OF-0033` | `joint_stock AP3 = P` · `low` · `articulation=.NR` · `Harris 2020` · `en` · `coder=ai` · `source_read=unknown` · note: "limited liability a late and plural achievement, not an original feature" |

**`LP1=1` with the note "chartered legal personhood" already fixes the referent.** `joint_stock` is the **chartered** corporation. The deed-of-settlement company is the form defined by *not* being chartered, and it codes `LP1=0`. The two rows are therefore not in competition on the evidence — they differ on the first characteristic either of them touches.

**So I was wrong to call this a blocker, and I withdraw that.** What remains is a documentation gap, not a coding one: the referent is fixed in a cell note where no reader of the type vocabulary will look, and Televantos's glossary makes "joint stock company" a synonym for the *unincorporated* form (printed 183), so a future coder reading only `code,name,tradition,period,key_source` can reasonably take `joint_stock` to cover it. The note below closes that. It does **not** need to land ahead of the rows.

## The limit on what I can write, stated plainly

**I have not read Harris 2020 and cannot write a positive scope note from a source I have not opened.** The citation resolves — Ron Harris, *Going the Distance: Eurasian Trade and the Rise of the Business Corporation, 1400–1700* (Princeton University Press, 2020), ISBN 9780691150772 — and its title says *business corporation*, which corroborates the chartered reading. But a scope note written from a title is exactly the "coded from secondary description without opening the source" that `source_read=none` exists to mark.

What I can write from sources I have read is a **boundary** — what `joint_stock` is not, against `deed_of_settlement_company`, from Televantos. That is the draft below. The positive half is left for whoever holds Harris 2020, and is marked as such in the text so it cannot be mistaken for settled.

## Draft text for the `key_source` field

> SCOPE, DRAFTED 2026-09-05 AND DELIBERATELY PARTIAL: THE POSITIVE HALF IS UNWRITTEN BECAUSE NOBODY HAS READ THE SOURCE. This row is the CHARTERED business corporation - incorporated by Royal Charter, letters patent or Act, with legal personality in the entity itself. That referent is not new here: it is already fixed by the row's own `LP1=1`, whose cell note reads 'chartered legal personhood'. What the row has never had is a note saying so where a reader of this vocabulary would find it.
>
> BOUNDARY AGAINST `deed_of_settlement_company`, WHICH IS WHY THIS NOTE EXISTS. Televantos 2020's glossary (printed 183) defines 'deed of settlement or joint stock company' as one term: 'A business which raised capital by issuing shares and/or bonds... Legally, deed of settlement companies were partnerships, but made use of some rules of trusts law in an attempt to emulate the benefits of incorporation.' THE PHRASE 'JOINT STOCK COMPANY' IN THE ENGLISH LITERATURE OF 1720-1844 THEREFORE NAMES THE UNINCORPORATED FORM AS OFTEN AS THE CHARTERED ONE, and a coder meeting this row cold could reasonably read it as covering both. It does not. The two forms differ on the first characteristic either touches: `joint_stock LP1=1`, `deed_of_settlement_company LP1=0` - 'a partnership was not a legal entity and so could not own property' (Televantos, printed 18), and the courts refused to treat these companies as anything else (43-46). WHERE A SOURCE USES 'joint stock company' OF AN ENGLISH CONCERN BETWEEN 1720 AND 1844, THE CODER MUST ESTABLISH THAT THE PASSAGE BEARS ON A CHARTERED ENTITY BEFORE ANY CELL TAKES A VALUE FROM IT, and record that judgement in the cell note.
>
> THE POSITIVE SCOPE IS NOT WRITTEN HERE AND MUST NOT BE INFERRED FROM THIS NOTE. The key source resolves - Harris, R., 'Going the Distance: Eurasian Trade and the Rise of the Business Corporation, 1400-1700', Princeton University Press 2020, ISBN 9780691150772 - but NOBODY HAS READ IT FOR THIS ROW: both cells carry `source_read=unknown` and `articulation=.NR`. Note also that the source's own period is 1400-1700 while this row reads '17c onward', which is a discrepancy nobody has explained. Whoever opens Harris 2020 should write the positive half and fix or defend the period.
>
> UMBRELLA PROBLEM, FLAGGED AND NOT RESOLVED, AND IT IS LARGER THAN THE BOUNDARY ABOVE. On the chartered reading this row is a PARENT of rows already coded at full 32 - `voc_1602`, `voc_1612` and `voc_1623` are chartered European corporations of the 17th century and fall squarely inside 'Joint-stock corporation | European | 17c onward'; `casa_san_giorgio` arguably does too. That is the same defect logbook 2, 2026-08-29 records for `ie`, `piaohao` and `kabu_nakama`, where a parent row sits above coded children. THE CHOICE IS THE MAINTAINER'S AND IS NOT TAKEN HERE: either narrow this row to a referent its children do not occupy, or retire it and move its two cells, or keep it as a declared umbrella that may never enter a similarity claim against its own children. Until that is decided, NO COMPARATIVE CLAIM ON THE LEGAL-PERSONALITY OR OWNER-SHIELDING COMPONENTS MAY PUT `joint_stock` AND ANY `voc` ROW ON THE SAME FOOTING.

## Two data-quality facts noticed and not repaired

1. **`OF-0032` carries `confidence=high` on `source_read=unknown`.** The application checklist in `run-a-coding-batch` says `high` only on a full read. Three other early seed cells do the same — `natie FP2` and `CI3`, and `nacion_cofradia FP3`, all `high` / `unknown`. This is a pre-existing pattern in the census's earliest rows, not something this batch introduced, and recoding another row's `confidence` is not mine to do.
2. **Both `joint_stock` cells carry `articulation=.NR`**, which is the honest state for a row nobody has read the source for, and should stay `.NR` rather than being defaulted to `analyst-imposed` when someone eventually does.

## Recommendation

Apply the draft `key_source` text above **with the rest of the batch, not ahead of it** — the earlier recommendation that it land as its own commit first rested on the false "no cells" claim and is withdrawn. Leave the two cells alone. Treat the umbrella question as a separate decision with its own logbook entry, because it touches four coded rows and this batch has no evidence bearing on it.
