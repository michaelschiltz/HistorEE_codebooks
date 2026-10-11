# Rulings on the nine comanda adjudications (2026-10-11)

**Status: ruled by MS in chat on 2026-10-11, item by item, each on a recommendation put by the assistant (`claude-opus-5-5`) and accepted as proposed unless stated. Recorded here by the assistant. The adjudications are those listed in `records/NOTES-comanda-coding-2026-10-07.md`, section (c). Rulings 1 and 6 also dispose of commenda pilot worksheet entries 19 and 21 (`RB3`); no other worksheet entry is ruled by this file.**

Sources read first-hand in the course of the rulings, beyond the batch record: García Sanz 1959, "Tipos ausetanos de la commenda en el siglo XIII", *Ausa* 3 no. 30, pp. 292–293 (docs. 3–6), from page images (Zotero `H9VVVKUT`); Hancock 2025, pp. 190–191, from the text layer (`NYIFPB3T`); Fynn-Paul 2017, pp. 93–96 and 102–103 (`W8A2BZYR`); Fynn-Paul, *Family, Work, and Household in Late Medieval Iberia* (Routledge, first published 2018; Zotero `32CK6XPU`), ch. 4 and its notes 31–35 and 124–126, from a calibre conversion whose page numbers are not the print's.

## 1. `RB3` — the security clause

`comanda_alloc` and `comanda_ad_societatem_alloc` keep `RB3 = general-estate` (medium). The 1230 Vic act naming *fideiussores* stays a variant in notes (ruling 2 of 2026-10-07).

The 2026-10-09 interim report's claim that `RB3` is defective — that it fails to separate security for the capital against the peril from security for the agent's performance — is withdrawn. No value in the set secures against the peril: the bottomry pledge secures repayment conditional on arrival and is lost with the ship. Every security secures whatever obligation survives the allocation of the peril, which `RB1` and `RB4` record. What separates the comanda from bottomry is the object of the security, which is `RB3`'s question. The Catalan general obligation of goods is a contractual clause creating a general hypothec [to confirm for Catalan law against Martínez Gijón 1966 §C or the Catalan notarial literature], not a liability rule; `isqa_alloc RB3 = none` stands on its own ground (a liability rule already carried at `AP3`/`LR1`).

Pilot entries 19 and 21: `LM-R0043` (`commenda_alloc`) and `LM-R0053` (`societas_maris`), arm P stage 5, `none`, are **replaced** — the value is unchanged but its basis becomes the observed formulary absence under ruling 1 of 2026-10-07, which caps it at `medium` and `analyst-imposed`. `LM-R0005`, `LM-R0015` (arm S, `.NR`), `LM-R0024` (stage 4, `surety`) and `LM-R0034` (stage 4, `general-estate`) are **kept**: the existing value stands.

`RB3`'s definition gains: "The security attaches to whatever obligation survives the allocation of the peril (`RB1`, `RB4`); no value secures against the peril itself." No split.

## 2. `VF1` — the sworn self-account

`VF1` gains the value `claimant-oath`: the loss is established by the claimant's own account, given on oath or subject to oath on demand; no third party verifies unless the counterparty contests. Defined by mode only. Whether the oath is decisive or rebuttable is recorded in each cell's notes, not in the value, because it is a burden-of-proof question that the 2026-08-13 split of `VF1` from `VF2` deliberately keeps out of `VF1`.

`comanda_alloc VF1 = claimant-oath`, medium, articulated, normative (*Consolat* cap. 279); notes record the rebuttable oath, cap. 220 and cap. 216 (witnesses for a failed purchase, a market-loss variant). `comanda_ad_societatem_alloc VF1` stays `.NR` (ruling 4 of 2026-10-07). `qirad_alloc` and `isqa_alloc` are **not** touched; a reading of Udovitch 1970, "Theory and Practice of Islamic Law" (`FJGG8BHL`) and of Mishnah *Shevuʿot* 7:8 is logged as open work. No version bump: a vocabulary value is not a declared datapackage constraint.

## 3. `MG2` — governance mode in principal–agent contracts

`MG2`'s definition is clarified, the value names kept: "Locus of residual control over the arrangement's operations. `single-principal`: one party holds that control, whether an owner, a head partner or a managing agent acting within a mandate. Ex-ante instructions bounding the mandate are contract terms, recorded in notes, not a governance mode." Consequence stated: `MG2` alone no longer says whether control sits with capital or labour; that is read from `CF1` and `CF2`.

`comanda MG2 = single-principal`, medium, articulated. `comanda_ad_societatem MG2` stays `.NR`, its ground changed from value-set misfit to not established (plural agents in some acts; the modal number uncounted). `commenda`, `qirad` and `societas_maris` lack `MG2` cells; to be coded at the Italian re-code.

## 4. `CI1` — capital structure: split

`CI1` asked two questions. It is narrowed to: "How the contributions of more than one party are held within the arrangement: `common` (merged in one stock), `several-accounts` (held in distinct accounts or ownership halves within it), `none` (no stock pooled from several contributors — a single contributor's capital, or an endowment)." This also settles the gap logged by ruling 3 of 2026-10-07: a single investor's capital entrusted to a single agent takes `none`, on the `waqf_khayri` precedent.

New characteristic `CI5`, segregation from the holder's other capital: `segregated | commingled`; component `none`, work package `none`; locator `arrangement`. "Whether the arrangement's capital is kept apart from other capital that the person conducting it holds or trades." It is not shielding: creditors' reach stays with `AP1`–`AP4`. Evidence that the two questions separate: arm P's Genoese acts hold `CI1` constant while Scriba and Amalric commingle and Cassinese keeps capital *separatim* (8 of 15 speaking). Schema growth: minor bump.

`comanda CI5 = segregated`, low, articulated, normative (cap. 219; *simil cum meis mercibus* as the commingling variant). `comanda CI1 = .NR` (the third mode reported by Hancock, a community of investments in shares, is uncounted). `comanda_ad_societatem` `CI1` and `CI5` `.NR`. The other `CI1` cells are re-read against the narrowed definition; any that answer the old (c) question go to `recodings.csv` as pending, not into `data.csv`.

## 5. `source_lang` — `ca`, and `zh` mirrored

`ca` is added to `source_lang` in both censuses (data and recodings); `zh` is mirrored into `organizational_forms` so that both carry the identical set. A check that the `source_lang` enums of the two censuses agree is added to `check_vocabularies.py`. Comanda cells move `es` → `ca` cell by cell: a cell whose decisive passage is a *Consolat* chapter read in Catalan becomes `ca`; a cell resting on Martínez Gijón or García Sanz stays `es`. Versions: `organizational_forms` 0.11.0 → 0.12.0; `loss_mitigation_forms` 0.8.0 → 0.9.0. MS added: rarer languages will follow (Bactrian etc.). Scripts such as Visigothic are not languages and are not coded in `source_lang`.

## 6. `comanda` against `commenda` — differences of evidence

Accepted. Differences on `LP1`, `AP1`, `AP3`, `LR1` and `LR4` are differences of evidence: the Italian values rest on Harris 2007, who addresses default law and outside creditors; no Catalan source read does; importing Harris would repeat the hygiene error refused in ruling 3 of 2026-10-07. Both type rows carry the sentence. Separations after rulings 1–5: substantive on `RB3` and `VF1` (the commenda value of `VF1` disputed, pilot entry 16); `CI1` no longer separates; `CI5` and `MG2` not comparable until the Italian re-code. A hypothesis is recorded, not encoded: commingling (`CI5`) and pro-rata loss among the investors whose goods were mixed (`LR4`) may be linked; the Italian re-code can test it. Arm P's disputes on the five commenda cells remain open.

## 7. `comanda_ad_societatem` against `societas_maris` and the *ʿisqa*

The separating cells are five, not three: `CF1`, `CF2`, `TS2`, `RB3`, `RB4`. `CF2 = P` and `RB4 = 0` stand, now read from the page images of Vic 1273 (García Sanz 1959, doc. 5): *Et si diminutio in dicto capitali venerit mitamus nos et tu talem partem qualem accepimus in lucro quousque tuum dictum capitalem tibi penitus reintegretur*, with a separate unconditional promise *quisque in solidum* to restore the comanda at a year and no peril clause. The claw-back reading of *talem partem qualem* was considered and set aside (*pars*; *mitamus nos et tu*; Manresa 1323 *lucri et amissionis*; Vic 1230 *restituam tibi medium*, via Martínez Gijón). Quotation corrected to the print's *capitalem*.

`CF2`'s definition is clarified: "`1` = the whole of the principal's capital loss; `P` = a defined fraction of it, a tranche or a proportion; `0` = none of it."

`isqa CF2` is re-coded `1` → `P` (the manager bears the loss on the loan half, about half the advance) and adjudicated **replaced**. The *ʿisqa* and the comanda *ad societatem* then agree on `CF2` and `RB4` and differ in construction (a loan tranche against an allocation clause), which no cell records and none should.

Notes, not cells: doc. 5 is local trade in wine and shoemaking; doc. 6 (1274, livestock *comanda ad parceriam*, out of scope) names loss-sharing on a diminution *ad consuetudinem mercatorum*.

## 8. Thin evidence for `comanda_ad_societatem`

The row stands. Its type row gains: the five `high` cells (`LR3`, `MG1`, `FP1`, `MC1`, `MB3`) are entailed by the row's scope and carry no weight in any comparison; doc. 5 read first-hand; doc. 6's custom; Hancock's ceiling (fewer than half of the 352 risk-clause acts share the loss in either way, so under about 12 per cent of 1,432) and her capital-proportional shared-risk act (*Societats mercantils* doc. 27), evidence that a second bilateral loss rule exists in Catalonia and is not coded. Acquisition order: *Societats mercantils* 1986, then Madurell & García Sanz 1973. Correction: Sayous 1931 is not held (the PDF on `54KLRXV3` is Sayous 1936).

## 9. Fynn-Paul's 91 commendas

Accepted, revised after the monograph. The series may be cited for the history of the word and its users only, never as a frequency or chronology of either coded row. The deposit exclusion is restated on the claim, not on `CF2`: the pure deposit (*comanda sive puro deposito, reddere quo velitis*; García Sanz doc. 4) is a credit instrument — fixed claim, no shared outcome — and enters the census, if ever, beside `sea_loan`. The trading deposit (Barcelona 1215 and 1248, Martínez Gijón 1964, 76–78, printed in Sayous 1931, not held) is in scope by structure and is parked as a candidate in logbook 2, no type code. The monograph confirms that the profit-share clause is in "some of the acts" (ch. 4 n. 34) and that the deposit formula dominates by the 1340s (n. 35), so the loss-sharing variant is a minority in the Bages too; whether the *lucri* acts carry *et amissionis* is known only for Manresa 1323. Archival tags, AHCM, Sarta papers: SF 1324 4i12; SF 1332 10k3; SF 1332 12k3 (*lucri*); SF 1332 1k12; SF 1342 6i6 (deposit formula); FT1 1326 17k12 (goods obliged for an agricultural loan). To the vault, not the matrix: the spread-or-concentrate observation, the *censal* substitution, and the Sarta–Amargos–Des Valls *societas* with no company capital (ch. 4 nn. 124–126).
