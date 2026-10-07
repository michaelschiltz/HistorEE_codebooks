# Coding notes — the Crown of Aragon comanda (2026-10-07)

**Status: proposal. Nothing is written to `data.csv`, `recodings.csv` or the vocabularies; no `git` was run.** Four fragment files sit beside this note in `proposed-of/`. Coder: `ai`, `claude-opus-5-5`; `coder_effort` is entered as `.NR` because the session's effort label is not visible to the coder — MS to fill before application.

## Not a blind batch, and what this chat saw

MS ruled the batch open on 2026-10-07: the material was newly acquired and no blind was available to spend. Before coding, this chat read the live `commenda`, `societas_maris`, `qirad`, `commenda_alloc` and `qirad_alloc` cells, the pilot record (`claude/commenda-pilot-applied-2026-09-28.md`) and the adjudication worksheet's four definitional questions. **No falsification claim is made and no priors file exists.** The fragments were written before the comparative tables below were computed.

**Standing-table row for `logbook/4` (draft):** slug `comanda-crown-of-aragon-2026-10-07`; spent: the commenda family, frame and mechanism alike (live cells, pilot results, reveal); prejudices any later blind re-code of `commenda`, `societas_maris`, `commenda_alloc`, `comanda*`; does not touch other forms.

## Decisions MS made in this session, before coding

1. The four pilot definitional questions were ruled: `proposed-of/RULINGS-commenda-pilot-definitional-2026-10-07.md`. Rulings 1 (two-limb formulary rule), 2 (no minority `P`), 3 (CI1 vocabulary question) and 4 (acts' silence on verification is `.NR`) are applied throughout.
2. Two rows in each census. **Split on the loss rule, not on terrain** (MS, after the evidence of Martínez Gijón 1966 was put to him; his first choice had been sea against land): `comanda` (unilateral; the investor bears the capital loss) and `comanda_ad_societatem` (loss shared in the profit proportion). Loss rows `comanda_alloc`, `comanda_ad_societatem_alloc` take the same ten characteristics as `commenda_alloc`.
3. Foam notes were written first (13 notes, `source-session: comanda-crown-of-aragon-2026-10-07`; vault validator green).

## Sources read, and how

| source | Zotero | read | text layer / offset |
|---|---|---|---|
| Consolat de Mar, Capmany/Font Rius 1965 | XWHD38V2 ("…mar 1.pdf") | caps. 88, 209–221, 254, 279 | good; printed = PDF − 66 |
| Pardessus II (1831), ch. XII — misfiled on XWHD38V2 ("…mar.pdf") | (NVAVD6WC) | same chapters, for the French and the concordance | good; Pardessus = Capmany + 1 |
| Martínez Gijón 1966, *AHDE* 36 | XLNCQXGB | pp. 379–410 (sections A–B) | image only; OCR'd 2026-10-07; printed = PDF + 378 |
| Martínez Gijón 1974, *HID* 1 | MWTFU4CG | whole | good; printed = PDF + 262 |
| Martínez Gijón 1964, *AHDE* 34 | U7ASLIDI | **not read** (OCR paused) | image only |
| García Sanz 1959 (1221 contract), *Ausa* 3 no. 27 | LBK7RJDU | whole | OCR'd |
| García Sanz 1959, "Tipos ausetanos", *Ausa* 3 no. 30 | H9VVVKUT | whole | OCR'd; running heads 285–293 |
| García Sanz 1963, *Ausa* 43 | VRZXUQGD | not read beyond Martínez Gijón's quotations | OCR'd |
| Hancock 2025, Oxford DPhil | NYIFPB3T | ch. 1 (16–19), ch. 4 (91–101), ch. 6 (188–193) | good; printed = PDF − 17 |
| Fynn-Paul 2017, *TSEG* 14:3 | W8A2BZYR | whole | good; running pages 85–107 = PDF + 84 |
| Polonio 2014 | EXRTPC38 | 239–245 | good |
| Cuadrada & López Pérez 1991 | X9Z35SMG | 77–79 | good |
| Carrère 1967 | SUK377UG | grep only (646, 668–669) | noisy OCR |

**Numbers quoted from the OCR'd articles (profit shares, years, page references) were read from the OCR, not re-checked against page images.** They are the obvious first thing to verify before application.

## (a) The fragments

- `proposed-rows-comanda-2026-10-07-organizational_forms.csv` — 64 rows, `OF-XXXX-01` … `-64` (32 each for `comanda`, `comanda_ad_societatem`).
- `proposed-rows-comanda-2026-10-07-loss_mitigation_forms.csv` — 20 rows, `LM-XXXX-01` … `-20`.
- `proposed-type-rows-comanda-2026-10-07-organizational_forms.csv`, `…-loss_mitigation_forms.csv` — two type rows each, with scope, exclusions, non-independence and the not-yet-consultable list in `key_source`.

## (b) Cells declined

**`comanda` (organizational), 19 `.NR` and 2 `.NA` of 32.** `.NR` on default law under ruling 1: LP1, LP2, LP3, AP2, LR4 (and LR5 by dependence). `.NR` because no source asks: AP1 (cap. 219 partitions accounts, not creditor ranks), AP3 and LR1 (every rule read runs investor–agent, none to outside creditors), TS1, TS3 (cap. 214 binds a promised comanda only), TS4, CI2, CI3, CI4, FP2, FP3, FP4 (notarised is not registered). `.NR` as value-set misfit: MG2. `.NA`: AP4, MG3.

**`comanda_ad_societatem`, 20 `.NR` and 2 `.NA` of 32.** As above, plus CI1 (craft acts silent on mixing) and TS3 (one revocable-at-will clause against fixed terms elsewhere).

**`comanda_alloc`: VF1 `.NR` as misfit** (see adjudication 2); PY0 `.NA`. **`comanda_ad_societatem_alloc`: VF1, VF2 `.NR`** (ruling 4: no normative layer, acts silent); PY0 `.NA`.

**Per component** (substantive of coded): `comanda` — loss-sharing 2/2, outcome-coupling 2/2, perpetual-succession 1/4, none 6/11, and **0 in entity-shielding (0/3), legal-personality (0/3), owner-shielding (0/2), risk-pooling (0/2), transferable-claims (0/2), capital-lock-in (0/1)**. `comanda_ad_societatem` the same pattern (none 5/11). The Catalan literature is about the contract between the parties; it is silent on every entity question.

## (c) Adjudications for MS

1. **`RB3 = general-estate` in both loss rows is the first instance of that value in the loss census, and it contradicts `commenda_alloc RB3 = none`.** Martínez Gijón (1966, 401) states that personal and real guarantees on all the commendatary's goods are "usually included" in unilateral and bilateral acts; the Vic 1240 act has the formula (384). What they secure is the duty to render account and restore what was not lost by an excused cause — not the capital against peril. Hancock's 54.9 % general-pledge figure is for all contract types, not comandas alone. Under ruling 1 both limbs are met. This bears directly on pilot entries 19 and 21, where chat P moved `RB3` from `general-estate`/`surety` to `none`; the Catalan evidence supports P's stage-4 reading on the Italian rows too, but that is MS's call on those rows.
2. **`VF1` for `comanda_alloc` is coded `.NR` as a value-set misfit, not silence.** The *Consolat* names the mode: a sworn account, believed unless the investor proves otherwise (cap. 279); "just reasons" shown, or prison (cap. 220); witnesses for a failed purchase (cap. 216). None of `communal-attestation`, `official-adjudication`, `documentary` fits a rebuttable sworn self-account. A value now has a form that would take it; whether to add one is a theory call and is **not proposed** here.
3. **`MG2` is a misfit for every principal–agent contract** (agent decides within the principal's instructions). Same for `commenda` (not coded there).
4. **`CI1 = several-accounts` for `comanda` rests on the *Consolat*'s articulated default** (cap. 219, *comanda sparsa*), at `low`, because the acts also show commingling (*simil cum meis mercibus*) and no count of the modes is available. Live `commenda CI1 = common` (ruling 3). Whether a normative default may carry a cell whose transactional mode is unmeasured is a rule question; the alternative is `.NR` until Madurell is digitised.
5. **`source_lang` has no `ca`.** The *Consolat* text is Catalan; cells citing it are entered `es` (Capmany's Castilian translation and apparatus, which were read). Adding `ca` widens an enum, which is a minor version bump on the 0.2.0 precedent.
6. **`comanda` against `commenda`: the differences are differences of evidence, not of form.** LP1 (.NR/0), AP1 (.NR/P), AP3 (.NR/0), LR1 (.NR/unlimited-several), LR4 (.NR/0) all separate only because the Catalan sources do not ask and ruling 1 keeps their silence `.NR`. The substantive cells agree (CF1, CF2, LR3, LR6, TS2, RB1, RB2, RB4, PR1, VF2). The rows separate substantively on **CI1** and **RB3** only.
7. **`comanda_ad_societatem` against `societas_maris`:** agree on RB1/RB2 `shared` and LR6 `symmetric`; differ on **CF1** (1/P: the agent's money contribution is a minority here), **CF2** (P/0: here the agent bears part of the *investor's* capital loss, there only his own contribution) and **RB4** (0/1: here the agents must make good their share; there the obligation lapses on loss). If CF2 = P holds, this row is not the Catalan *societas maris* but a distinct allocation, and on CF2 and RB4 it moves toward the `isqa` (CF2 = 1, `isqa_alloc` RB4 = 0).
8. **The evidence for `comanda_ad_societatem` is thin and declared so in the type row**: about six quoted acts, two secondary authors with a shared upstream. Confidence is `medium` or `low` throughout.
9. **Fynn-Paul's 91 "land commendas" are not one form.** His Example 1 is a deposit, his Example 2 a loss-sharing comanda. His decline series (102–106) therefore counts a word. The deposit is excluded from both rows on structure (it reverses CF2).

## The six answers

1. **What was coded, on what evidence.** Two forms in two censuses: 22 substantive organizational cells and 15 substantive loss cells, from the *Consolat de Mar* (normative, in the tradition's words), Martínez Gijón 1966/1974 and García Sanz 1959 (quoting thirteenth-century acts), Hancock 2025 (1,432 acts, counts), Fynn-Paul 2017, Cuadrada & López Pérez, Polonio 2014.
2. **What could not be coded, and why.** Every entity-shielding, legal-personality, owner-shielding, transferable-claims and capital-lock-in cell: the sources treat the comanda only between its parties. VF1 (misfit), MG2 (misfit), the ad-societatem verification pair (no normative layer).
3. **Expectations falsified.** None claimed: the batch is open and no priors were filed. Reported instead: the coder expected the sea/land frame to carry the split, and Martínez Gijón's acts showed it does not; MS re-scoped the rows before coding.
4. **Characteristics that did not fit.** VF1 (sworn self-account), MG2 (agent under instructions), CI1 (single investor, single agent; ruling 3), `source_lang` (no Catalan).
5. **Dependence or well-formedness problems noticed and not repaired.** VF2 coded while VF1 is `.NR` in `comanda_alloc` (the pattern chat P flagged as item 4). LR5 is `.NR` because LR4 is `.NR` — correct by the applicability rule, but it means the risk-pooling component of both rows is empty by inheritance. Pre-existing: the loss `datapackage.json` names nonexistent vocabulary files (carried from 2026-09-28).
6. **What to acquire next, and which cell it would move.** Madurell & García Sanz 1973 (digitisation by MS): CI1 and RB3 by count, CF3, TS2 variants, and the ad-societatem row's frequency. *Societats mercantils* 1986: the boundary between `comanda_ad_societatem` and the *societas*. OCR of Polonio Luque 2012 (text volume): clause frequencies 1349–1450. Martínez Gijón 1964 and 1966 section C: the deposit boundary and the *Consolat* reading. Sayous 1931 (EUC): the Barcelona cathedral acts at first hand. Colon & Garcia, *Llibre del Consolat de Mar* (1981, T9CM7AWV): the critical text.

## What the matrix learned

- **New value-instance:** `RB3 = general-estate`, in both loss rows — the value existed in the vocabulary (widened 2026-08-16) with no form holding it.
- **New separation within the commenda family:** `CF2 = P` (`comanda_ad_societatem`) sits between `0` (`commenda`, `societas_maris`, `qirad`, `ortoq_equity`, `comanda`) and `1` (`isqa`, `ortoq_loan`); the only other `P` in the column is `nakai_fictive_household`. `RB4 = 0` is shared with `isqa_alloc` alone; every other partnership- and loan-family row with a value has `1`. The resemblance to the *ʿisqa* on these two cells is reported, not interpreted: no shared descent is claimed and none is excluded.
- **No new signature on any WP2 component**: all WP2 components are empty on both rows.
- **Not corroboration:** the substantive agreement of `comanda` with `commenda` is parallelism in a shared drafting tradition; see the type row's non-independence declaration.

## Checks run (scratch copy outside the repository, fragments appended with temporary ids OF-0836…0899, LM-0741…0760)

- `check_vocabularies.py`: "✓ vocabularies valid — 6 files, 170 codes …" (after one whitespace fix in a `key_source`).
- `check_dependence.py datasets/organizational_forms` and `… datasets/loss_mitigation_forms`: "dependence problems: 0" each.
- `frictionless validate` (5.x, installed for the session) on both datapackages: all four resources VALID.
- Value sweep of the 84 new rows: every value in `allowed_values` or a missingness token; `.NA` propagated; `.NR` with `.NR` confidence and articulation; no `[verify]`. 0 failures.
- Not run: `build_codebook.py`, `build_views.py` (they would write; the proposal changes no live file).

## Housekeeping found (not repaired)

- XWHD38V2 carries Pardessus t. II as its first PDF; NVAVD6WC (Pardessus) wants it. 54KLRXV3 (Sayous 1931) carries Sayous 1936. Both tagged `attachment-mismatch` in Zotero.
- Duplicates: Ferrer i Mallol 1974, GANRSSUW and 8QTWZBIR; Polonio 2014 has two identical attachments.
- Fynn-Paul 2017 pages set to the running pages 85–107 (header says 5–36); Cuadrada & López Pérez footer reads 1992.
