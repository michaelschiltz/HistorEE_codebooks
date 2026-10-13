# Priors — the *she* association death mutual aid, `she_death_aid` (2026-10-13)

**Written by the assistant (`claude-opus-5-5`, effort `high`) before any document of the corpus was read for coding, and to be committed by MS before item 4 of `records/NOTES-she-associations-2026-10-13.md` opens. Pass slug `she-associations-2026-10-13`; open, not blind.**

**What these priors already know, declared.** They are not uninformed. Before writing them the assistant had read: the vault note "Dunhuang she associations - bylaws for a funeral fund" (including its quotations of one death circular's schedule, 麵一斗、粟一斗、色物半疋, of a women's bylaw's schedule, and of the penalties: a banquet for the association, three strokes of the stick for a member trying to leave); logbook 2, 2026-09-12 (xi); Ning and Hao's preface counts as recorded in the vault (pp. 7–21); Ning and Hao's table of contents (PDF 44–73, titles, dates and shelfmarks only, `records/CORPUS-she-associations-2026-10-13.csv`); the editors' note to bylaw no. 10 (p. 32); one page of commentary (p. 319) read for the OCR test; and the values and notes of the neighbouring rows in `loss_mitigation_forms` (`guild_box_brabant`, `guild_relief_england`, `guild_box_dutch`, `confraternity_fund_it`, `friendly_society_england`, `averia_pool`, `shenhui_gu_alloc`, and the three `PY1 = life-event` rows). No bylaw, circular or register text has been read.

**Form of each prior:** expected value; confidence in the prior (not the house cell confidence); what reading would falsify it.

## Mechanism and membership

- **`MC1` pooling.** High. Falsified if contributions at a death are a gift with no reciprocal claim (charity), or if the death benefit is bought from the officers.
- **`MB1` locality**, with kinship (親情社, no. 4) and confession as variants. Low. The neighbourhood names (儒風坊西巷社, 旌坊巷女人社) suggest locality; kinship would be the census's first `MB1 = kinship`. **Expected inadequacy:** `MB1` has no value for gender, so the women's associations cannot be expressed on it. Falsified if the practical bylaws define membership by kin or by religious community more often than by place.
- **`MB2` 1** (entry needs the association's acceptance; the petitions 社狀牒 include applications to join). Medium. Falsified if anyone in the neighbourhood was a member by residence.
- **`MB3` voluntary**, exit restricted by penalty. High. Falsified if membership was imposed (the officially levied register S. 3978 is the case to watch, and it is excluded from the evidence by ruling 1).

## Contributions

- **`CN1` ex-post-assessment** (a levy in kind at each death). Medium. This would be the census's second instance, after `general_average`. Falsified if death aid is paid out of a standing stock (the 義聚 of the loan registers) built from periodic dues, which would make it `ex-ante-periodic`.
- **`CN2` equal** (a fixed schedule per member). Medium-high. Falsified if the schedule varies by rank, office or wealth.
- **`CN3` 1** (default enforced by the association: fines, the banquet penalty, second demands 再限納物). Medium-high. Falsified if the bylaws state penalties that the registers and fines records never show applied (that would be `P`).

## Hazard

- **`HZ1` idiosyncratic.** Low. Deaths in a member's household are individual events; an epidemic would make them covariate. Falsified if the documents show deaths clustered in time or mention epidemic or famine as a reason for second demands (then `mixed`).
- **`HZ2` .NR.** Low. Expected that nothing speaks to it.

## Payout

- **`PY0` individual-indemnity.** Low. The bereaved member receives the goods for the funeral. Alternative: the goods are consumed at a funeral the association itself performs, which leans toward a service rather than an individual payout; that would test the value set.
- **`PY1` life-event.** Medium. **Expected to meet the logged defect** (logbook 6): the trigger is a death in the member's household (parent, spouse, child, sibling; the death circulars' titles name 妻, 母, 父, 弟, 兄弟, 阿婆), not the member's own death or another member's, and `PY1` names the kind of event without its locus.
- **`PY2`: no value fits; expected `.NR` or a flag.** Low. The value set (rotation, auction, indemnity, need-assessed) has no state for a fixed in-kind schedule paid irrespective of the loss. Falsified if contributions are scaled to the funeral's cost (then `indemnity`).
- **`PY3` 1** (the fixed schedule caps the draw independently of the cost of the funeral). Medium.

## Loss-sharing and liability

- **`LS1` .NR**, **`LS2` .NR**, **`LS3` .NR.** Low each. With a levy at each death there is no fund to exhaust or to claim on. Falsified if the 義聚 serves funerals (then `LS2` may be coded) or if second demands go beyond the schedule (then `LS3` may be `P`).

## Verification

- **`VF1` official-adjudication**, the association's office (錄事 issuing the circular) establishing that the death occurred. Low. Alternative `communal-attestation`. Falsified if the circular simply relays the bereaved member's notice with no act of the officers.
- **`VF2` loss-occurrence.** Low.

## Governance and duration

- **`GV1` collective** (rules made and re-made by the members, 再立條件; officers chosen). Medium. Falsified if the three officers (三官) fix the rules and the members only subscribe (then `elder-fixed`, the census's first).
- **`DR1` open-ended.** Medium. **`DR2` .NA.**

## Peril bearers and pricing

- **`RB1`, `RB2`, `RB4`: not coded, and `RB3` `.NR`, on the neighbours' practice.** High. `PR1` 0. High.

## Row-level priors

- **The women's associations (nos. 7, 8) separate from the others on no cell**, so no split is needed. Low. Falsified if they differ on `CN1`, `CN2`, `PY1` or `GV1`.
- **The 義聚 loan stock does not serve funerals**, so it stays out of the row and is parked (ruling 1a). Low.
- **At least a third of the 20 circulars and 27 registers counted as practical from the table of contents will turn out to be drafts or copies** on reading the editors' notes (the preface puts the practical circulars at about sixty of 193). Medium.
