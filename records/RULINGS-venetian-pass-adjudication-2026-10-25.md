# Rulings adjudicating the Venetian pass (2026-10-25)

**Status: ruled by MS in chat on 2026-10-25 ("Recommendations adopted"), on five tranches of recommendations put by the assistant (`claude-opus-5-5`, effort `high`) as operator, and applied by the assistant the same day.** Pass `venetian-pass-2026-10-25`. The blind coding was frozen and pushed (`280bf50`) before any cell was adjudicated, and the operator's withheld predictions were scored first (logbook 4, 2026-10-25). The six adjudication rules applied here are those of `records/RULINGS-venetian-pass-2026-10-25.md`, cited below as rules 1–6.

## The queue as found

At `280bf50`, 32 rows in the two `recodings.csv` files carried `adjudication = pending`, all on the 14 cells of this pass: 8 in `organizational_forms` (`societas_maris` `CF1`, `CF3`, `CI1`, `LR6`, `TS2`) and 24 in `loss_mitigation_forms` (`commenda_alloc` `MC1`, `PR1`, `RB1`; `societas_maris` `MB3`, `MC1`, `PR1`, `RB1`, `RB2`, `RB4`), from the passes `commenda-primary-2026-09-28` and `commenda-secondary-2026-09-28`. The blind Venetian coding proposed 14 more (`OF-R0253`–`R0257`, `LM-R0080`–`R0088`).

## How a change reaches `data.csv`

As in rulings 2–5 of `records/RULINGS-queue-clearance-2026-10-25.md`: the blind rows are adjudicated on their value, and each cell that gains evidence from the Venetian acts gets a new `open` row stating the merged cell, adjudicated `replaced` (`OF-R0258`–`R0262`, `LM-R0089`–`R0097`). Every changed cell's note gains one bracketed addition naming its row, its tranche, the clause relied on, and the stratum of its Venetian evidence (date, fondo, named dossiers, copies). The rest of each note is unchanged.

`source_lang` moves from `en` to `la` only where `articulation` moves to `articulated` on the Latin of the acts (`CF1`, `CF3`, `CI1`, `TS2`, `RB4`, `RB2`); elsewhere the Latin is added to a basis that remains the secondary literature, and the language stays.

## Tranche 1 — `societas_maris` `CF1`, `CF3`, `CI1`, `TS2`

**Ruled:** blind rows `OF-R0253`, `R0254`, `R0255`, `R0257` **kept**. Values and confidence unchanged. Each cell adds the Venetian acts to its `source_ref` (26 to 31 acts: 4 contracts and the releases that recite both contributions, admissible for existence, parties, capital and route under rule 2), a note on date, fondo, dossiers and copies (rules 1, 4, 5), and `articulation` → `articulated`, the Latin stating each value in terms. New rows `OF-R0258` (`CF1`), `R0259` (`CF3`), `R0260` (`CI1`), `R0261` (`TS2`), `replaced`.

## Tranche 2 — the clause-based `societas_maris` cells

**Ruled:**

- `LR6` symmetric: blind row `OF-R0256` **kept**; act 334 added. The coder's flag that `LR6`'s applicability could not be checked is resolved: `LR2` is `coupled`, not `veiled`. New row `OF-R0262`, `replaced`.
- `RB1` shared: blind row `LM-R0086` **kept**; the clause added. The two after-the-fact loss cases (the 1171 imperial seizure, acts 380 and 418, one contract; the Pisan seizure, act 787) are named in the note with rule 3's caveat. New row `LM-R0094`, `replaced`.
- `RB4` 1: blind row `LM-R0088` **kept**. **The coder's `0` variant (act 380) is discounted**: a release that does not recite the clause yields nothing for a loss term (rule 2). `articulation` analyst-imposed → `articulated` on «nichil inde pars parti inquirere debeat» (no. 334). New row `LM-R0095`, `replaced`.
- `MC1` allocation and `PR1` 0: blind rows `LM-R0084`, `LM-R0085` **kept**; evidence added. New rows `LM-R0092`, `LM-R0093`, `replaced`.
- `MB3` voluntary: blind row `LM-R0083` **kept** on value. The Venetian acts are silent on choice, so no act is cited; the note records the silence. New row `LM-R0096`, `replaced` (note only). Whether `MB3` is anything but definitional for a two-party contract is carried.

## Tranche 3 — `commenda_alloc` `MC1`, `PR1`, `RB1`

**Ruled:** blind rows `LM-R0080`, `R0081`, `R0082` **kept**. The Venetian evidence is added: 56 sampled contracts, 52 after 1200, fondi Procuratori 23, S. Zaccaria 17, Cancelleria Inferiore 14; the peril clause «in tuo periculo maris et gentis ... clarefactum» in 160 of the 170 profit-share contracts (the coder's census), which `RB1` had cited at one remove from Held 2025. `MC1` is not blind and takes no weight on that account. New rows `LM-R0089`, `R0090`, `R0091`, `replaced`.

## Tranche 4 — `societas_maris RB2`, the one disagreement

**Ruled:** blind row `LM-R0087` (`.NR`) **overruled**: no Venetian act separates loss from the market from loss to the peril, and one source's silence does not override another's statement. The live `shared` is **kept**, re-based on its one articulated primary witness, Scriba DCXCII (p. 374), found by the September primary arm (`LM-R0033`); `articulation` analyst-imposed → `articulated`; **confidence high → medium**, since the cell rests on one Genoese act and an undifferentiated secondary statement. New row `LM-R0097`, `replaced`. The three September `RB2` rows are kept with the rest (tranche 5).

## Tranche 5 — the coder's phase split, the September rows, carried items

**Ruled:**

- **Phase split declined**, as rule 1 requires. The coder's own assignment by terms already sends the pre-1200 bilateral acts to `societas_maris` and the post-1200 unilateral acts to `commenda_alloc`, and no cell takes different values within either form across the two strata: the four pre-1200 unilateral contracts read as the thirteenth-century ones do. The change c.1200 is recorded as description in the `key_source` of `commenda`, `commenda_alloc` and both `societas_maris` type rows.
- **The 32 September rows on these cells: kept.** All 32 equal the live values. Pending rows in both packages: **0**.
- **Carried:** one traveller with many investors (Redolfus de Suligo, 15 colleganze in August 1234, acts 676–690) bears on `commenda CI5`, not in scope; `MB3` for two-party contracts; `TS2` has no state for a season bounded by the convoy calendar.

## Also applied

- `references/works.csv`: `Morozzo della Rocca & Lombardo 1940` (Zotero `GXRRAIUK`) registered.
- Checks: frictionless VALID on both packages; dependence 0 on both; vocabularies valid; citations 0 errors; quotations `--strict` 0; soft-wrap and tables; `organizational_forms` codebook regenerated twice, `cmp`-identical (`articulation` fill 362 → 365 of 948); all nine `organizational_forms` views and the loss census's `risk-pooling` view `current`.
