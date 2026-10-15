# Priors — the Florentine *monte delle doti*, `loss_mitigation_forms` (filled, 2026-10-15)

Filled from the template `PRIORS-monte-delle-doti-2026-10-15.md`. **No file in `sources/` has been opened, listed or read** at the time of writing; the directory's existence is known from the bundle's top-level listing and its contents only from the README's page-map table.

- **Row under test:** one row, the Florentine *monte delle doti*; tradition `Tuscan (Florentine)`; period `1425-1530`.
- **Coder:** `claude-opus-5-5`. Effort setting: not exposed to me inside this session, so I do not state one; MS to fill `coder_effort` from the session settings (the six other forms coded by `claude-opus-5-5` in this census carry `high`, which is house history, not evidence about this session).
- **Date filled:** 2026-10-15 (Asia/Tokyo).

## 1. Exposure, declared

- Bundle files read (doctrine, vocabularies, views, `data.csv`, type vocabulary), and how far:
  - `README.md`, in full.
  - `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `EDITING-CSV.md`: each in full.
  - `PRIORS-monte-delle-doti-2026-10-15.md` (the template): in full.
  - `vocabularies/loss_mitigation_characteristic.csv`: in full, every column of all 26 rows (`definition`, `allowed_values`, `applicability_on`, `locator`, `component`, `dependence_*`).
  - `vocabularies/loss_mitigation_type.csv`: header, and `code`/`name`/`tradition`/`period` of all 60 rows; every column of four rows (`tontine_fr_royal`, `widows_fund_scotland`, `life_annuity_priced`, `she_death_aid`); value counts of `boundary_basis`, `boundary_confidence`, `cooccurrence_basis` over the column.
  - `views/loss_mitigation_forms--risk-pooling.md`: in full (second line: filter `MC1 = pooling`, 30 forms × 9 characteristics).
  - `datasets/loss_mitigation_forms/datapackage.json`: package metadata and every field name, type, constraint and description of both resources.
  - `datasets/loss_mitigation_forms/data.csv` (795 rows, last id LM-0795): header; a regex sweep of every field of every row for `dot[ie]|dowr|florent|tuscan|kirshner|molho|marriage` (15 hits, contexts of ~400 characters read); value counts over the column for 16 characteristics (MB1, PY1, PY2, LS1, LS2, LS3, VF1, GV1, DR1, DR2, RB1, RB2, RB3, RB4, CN2, HZ2); the `type_id`/`char_id`/`value` of the last ten rows (mudaraba_alloc); a count of rows by `type_id` where `coder_model = claude-opus-5-5`.
  - `datasets/loss_mitigation_forms/recodings.csv`: line count only, and the regex sweep above (0 hits).
  - `scripts/*.py`: not read; regex sweep only (0 hits).
  - Skills loaded and read in full: `code-a-form`, `run-a-coding-batch`.
- Rows of `data.csv` you read cell by cell, if any:
  - `tontine_en_1693`, LM-0079 to LM-0088 (10 cells), every field.
  - `craft_widows_fund_edinburgh`, LM-0408 to LM-0428 and LM-0459 (22 cells), every field.
  - `she_death_aid`, LM-0763 to LM-0785 (23 cells), every field.
  - Partial notes (the regex contexts only) of LM-0496, LM-0498 (`avariz_vakfi_kirkcesme`), LM-0571, LM-0573, LM-0574 (`avariz_fund`), LM-0587, LM-0588, LM-0590 to LM-0593, LM-0596, LM-0601, LM-0606, LM-0609 (`confraternity_fund_it`).
- Any leak noticed in the bundle or in a loaded skill (quote it and give the file):
  - **None found.** The sweep above over every non-source file in the bundle and both skills returned no mention of a dowry fund, of Florence's *monte*, of Kirshner or of Molho. The 15 `data.csv` hits concern other forms: Ottoman orphans' "marriage portions" (`avariz_*`) and the Florentine guild *societas* of the *oliandoli e pizzicagnoli* of 1345 in `confraternity_fund_it` (Gazzini). Neither states or implies a value for this form. The skills mention neither the form nor its sources.
  - **Not a leak but recorded:** the kickoff prompt is truncated mid-sentence ("Do not repair a vocabulary or schema defect: flag it. Do"), so the validation instructions it refers to ("Then validate (below)") did not reach me. I will ask for them before step 5.
- **Training knowledge, declared.** I know the subject from training: Kirshner and Molho's 1978 *JMH* article, Molho's 1994 *Marriage Alliance*, Kirshner's dowry essays, and the general literature on the Florentine public debt. That knowledge informs everything in §2–§4 and nothing after.

## 2. The textbook account, clause by clause

Training knowledge only. One clause per line, each with my confidence in the clause.

- Founding and founder:
  - Established by the Florentine commune by legislation of 1424/5 (1425 modern style), during the war with Milan, as a branch of or adjunct to the public debt (the Monte comune). *High.*
  - Two stated motives: to raise money for the commune and to facilitate marriage (and with it population and the honour of families) by making dowries affordable. *Medium-high.*
  - The first law attracted few depositors; the fund was substantially reformed in 1433, after which deposits grew. *Medium-high on the reform, medium on the year 1433.*
- Who could deposit, and for whom:
  - Deposits were made for girls (*fanciulle*), not boys, typically by fathers, but also by other relatives or third parties. *High that girls only; medium on third parties.*
  - Depositors were overwhelmingly from Florentine citizen families, the elite heavily over-represented; I am unsure whether non-citizens or contado residents were formally excluded. *Medium on the social profile; low on a formal citizenship rule.*
  - Girls were enrolled young, often in early childhood; I do not know of a formal age limit. *Medium that young; low on any limit.*
- What was deposited, how, and for how long:
  - A sum chosen by the depositor, paid in at entry, in cash or (I believe) in Monte comune credits valued at a fraction of par. *Medium on cash; low-medium on credits.*
  - Two terms, roughly 7½ and 15 years, the payout a multiple of the deposit fixed by the term: about 250 per 100 at 7½ years and about 500 per 100 at 15 years, an implicit annual yield near 11–12 per cent. *Medium on the two terms; low-medium on the multiples.*
  - The yield was well above the Monte comune's ordinary interest, the margin funded by the forfeits the commune expected. *Medium.*
- What was paid, to whom, and on what event:
  - The capital and accrued sum, the "dowry of the Monte", was paid on the girl's marriage, to the husband, not to the girl or her father. *High.*
  - Payment required the consummation of the marriage, proved to the Monte's officials; a husband could not collect on a betrothal alone. *Medium-high.*
  - A girl who reached the term unmarried did not forfeit at once; the deposit stayed and could be collected on a later marriage. *Low-medium.*
  - A girl who entered a convent: by some later provision a portion was paid as a monastic dowry, otherwise the deposit was lost. *Low.*
- What happened to the deposit if that event did not occur:
  - Under the 1425 law, if the girl died before marrying the deposit was forfeited to the commune. *Medium.*
  - The 1433 reform let the depositor (or his heirs) recover the principal, without the accrued gain, on the girl's death; this is what made the fund attractive. *Medium.*
- Who administered the fund, and inside what:
  - The officials of the Monte (*ufficiali del Monte*), communal magistrates, inside the commune's public debt administration; depositors had no governing voice. *High.*
  - The deposits were not segregated as a stock of cash: they were absorbed into the commune's finances, so the fund's solvency was the commune's. *Medium.*
- What changed over the fund's life, and when:
  - 1433: return of principal on death (above). *Medium.*
  - From the 1470s, and acute in the late 1470s and 1480s, the commune could not pay maturing dowries in full or on time: payments were delayed, and part was paid in cash and part in Monte credits or deferred instalments; rates on new deposits were reduced. *Medium on a crisis in the 1470s–80s; low on the instruments and dates.*
  - Further reorganisation around 1494 (the expulsion of the Medici) and under the restored Medici and the duchy, past 1530. *Low.*
  - Additional terms or deposit options were added after 1433 (I half-remember shorter or intermediate terms). *Low.*
- Anything else:
  - The Monte's registers record each girl's date of deposit, age, marriage, death or entry into religion, which is why Morrison, Kirshner and Molho used them for mortality and epidemics. *High.*
  - Some 19,000–20,000 girls were enrolled between 1425 and the 1530s. *Low.*
  - Husbands sometimes delayed or failed to collect, and the Monte paid out only on formal proof, with a long procedure; Kirshner's "morning after" title points to collection as a problem in its own right. *Medium.*
  - The husband's obligation to restore the dowry on the dissolution of the marriage was secured in ordinary Florentine practice by guarantors (*mallevadori*); I do not know whether the Monte itself required such a guarantee before paying. *Low.*

## 3. Expectations, one per characteristic

Confidence below is confidence in the prior, not house cell confidence.

- **`MC1`** (mitigation mechanism; component `risk-pooling`; allowed `allocation|spreading|pooling`; applicability `.NA`)
  - expected value: `pooling`, flagged as a hard call. The forfeits of girls who died (before 1433: whole deposits; after: the accrued gain) fund the yield paid to girls who married, so the hazard of a daughter's death is mutualised across depositors through the fund. The alternative is `spreading`: the commune, a party with no stake in any marriage, guarantees a fixed sum and keeps the forfeits as its margin, which is a transfer to a third party for an implicit premium.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: the sources show the payout fixed by law irrespective of the fund's forfeits, with the commune as residual claimant and its officials pricing the scheme as the commune's gain or loss (→ `spreading`); or the fund described purely as a deposit with interest owed by the commune (→ `allocation`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no; but the value will be analyst-imposed.
- **`MB1`** (membership basis; component `none`; allowed `kinship|locality|occupation|confession|contract|territorial-subject`; applicability `.NA`)
  - expected value: `contract` (membership by making a deposit), with `territorial-subject` the alternative if eligibility was limited to citizens or subjects of the Florentine state.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: a stated rule restricting deposits to Florentine citizens, or to residents of city and dominion (→ `territorial-subject`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`MB2`** (entry restriction; component `none`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `1` (closed to a defined class: girls, possibly of a stated age or status), not numerically restricted.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: any girl could be enrolled by anyone with no status, age or citizenship rule, and nothing else closes entry (→ `0`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`MB3`** (participation basis; component `risk-pooling`; allowed `voluntary|compulsory`; applicability `.NA`)
  - expected value: `voluntary`.
  - confidence in this prior (high / medium / low): high.
  - what reading would falsify it: a law compelling deposits, e.g. as a condition of office or as a forced conversion of Monte comune credits.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`CN1`** (contribution timing; component `risk-pooling`; allowed `ex-ante-periodic|ex-ante-lump|ex-post-assessment`; applicability `.NA`)
  - expected value: `ex-ante-lump`.
  - confidence in this prior (high / medium / low): high.
  - what reading would falsify it: deposits payable by instalments as a rule (→ `ex-ante-periodic`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`CN2`** (contribution basis; component `loss-sharing`; allowed `equal|proportional-to-stake|proportional-to-capacity`; applicability `.NA`)
  - expected value: `proportional-to-stake` (the depositor chooses the sum and the payout scales with it), with a poor fit flagged: no value says "chosen by the member".
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: a fixed unit of deposit (→ `equal`), or deposits graded by the family's wealth or tax assessment (→ `proportional-to-capacity`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`CN3`** (contribution enforceability; component `loss-sharing`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `.NA`: the deposit is paid at entry, so there is no outstanding contribution whose non-payment could be compelled.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: instalment deposits with a sanction for default (→ `1`), or lapse without sanction (→ `0`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): yes, if not `.NA`.
- **`HZ1`** (hazard correlation; component `risk-pooling`; allowed `idiosyncratic|covariate|mixed`; applicability `.NA`)
  - expected value: `mixed`: a daughter's death is idiosyncratic in ordinary years and covariate in plague years, and the commune's own default is perfectly covariate across depositors.
  - confidence in this prior (high / medium / low): medium.
  - what reading would falsify it: the epidemiological articles find no synchronised mortality among enrolled girls (→ `idiosyncratic`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no; Morrison, Kirshner and Molho 1985 should ask it directly.
- **`HZ2`** (hazard responsiveness; component `risk-pooling`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `.NR`; if the sources speak, `P` on the census's reading (the claim responding to the cover: marriages timed to maturity, contested consummation).
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: the sources show the timing of marriage or of claims driven by the deposit's maturity (→ `P`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): yes.
- **`PY0`** (pool output; component `risk-pooling`; allowed `collective-good|individual-indemnity|individual-draw`; applicability `.NA`)
  - expected value: `individual-draw`, poor fit flagged: the payout corresponds to no loss (marriage is not a misfortune), but nor is it allotted by rotation, lot or auction, which is how the vocabulary glosses the value.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: the sources frame the dowry as the father's burden which the fund relieves, and the payout as meeting it (→ `individual-indemnity`, as widows_fund_scotland is coded on a life-event trigger).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`PY1`** (payout trigger; component `risk-pooling`; allowed `realised-loss|life-event|rotation|need-assessed`; applicability `PY0`)
  - expected value: `life-event` (the girl's marriage, consummated).
  - confidence in this prior (high / medium / low): high.
  - what reading would falsify it: payment at the term regardless of marriage.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`PY2`** (allocation rule; component `risk-pooling`; allowed `rotation-lot|rotation-fixed|auction|indemnity|need-assessed`; applicability `PY0`)
  - expected value: `.NR`, no fitting value: the trigger determines the draw, no claimants compete, and the sum is fixed by deposit and term, which is none of the five.
  - confidence in this prior (high / medium / low): medium.
  - what reading would falsify it: a rationing rule in the payment crisis (e.g. payment by lot or by order of maturity) that the sources describe as allocating among eligible claimants.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): yes (no-fit rather than silence).
- **`PY3`** (payout cap; component `outcome-coupling`; allowed `1|P|0`; applicability `PY0`)
  - expected value: `1`: the sum is fixed by deposit and term, independent of what dowry the marriage required.
  - confidence in this prior (high / medium / low): medium.
  - what reading would falsify it: payout varying with the marriage (e.g. with the dowry agreed) (→ `0`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`LS1`** (loss-sharing rule; component `loss-sharing`; allowed `pro-rata|equal|capped|residual-on-fund`; applicability `.NA`)
  - expected value: `.NR` before the payment crisis; from the 1470s, if the sources describe a uniform rule for paying only part in cash and deferring or converting the rest, `pro-rata`. A split candidate.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: shortfall handled case by case or by the commune's ad hoc favour (→ `.NR`, no rule); or borne by the commune out of other revenue with beneficiaries paid in full (→ the question does not arise).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): partly.
- **`LS2`** (residual claim on fund; component `outcome-coupling`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `0`: depositors had no claim on the fund's surplus; the forfeits and the margin were the commune's.
  - confidence in this prior (high / medium / low): medium.
  - what reading would falsify it: forfeits redistributed to surviving depositors, or the rates on later deposits raised from surplus as of right (→ `1` or `P`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): possibly; the surplus may be described only as the commune's motive.
- **`LS3`** (liability beyond contribution; component `owner-shielding`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `.NR`; if anything, `0`.
  - confidence in this prior (high / medium / low): medium on `.NR`.
  - what reading would falsify it: a depositor or husband held liable to the Monte beyond the deposit (e.g. to restore a dowry paid on a marriage later annulled) (→ `1` or `P`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): yes.
- **`VF1`** (loss verification mode; component `none`; allowed `communal-attestation|official-adjudication|documentary|claimant-oath|none`; applicability `.NA`)
  - expected value: `documentary` (a notarial or parish instrument proving marriage and consummation, presented to the officials), with `official-adjudication` the close alternative.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: officials deciding entitlement on their own inquiry (→ `official-adjudication`); proof by witnesses' sworn statements (→ `communal-attestation`); the husband's oath (→ `claimant-oath`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no; Kirshner 2015 ch. 4 should ask it.
- **`VF2`** (verification object; component `none`; allowed `loss-occurrence|claimant-need|claimant-fault|conduct-compliance|mixed`; applicability `VF1`)
  - expected value: `loss-occurrence` (that the defined event happened: a marriage, consummated, of the enrolled girl), or `mixed` if the procedure also verified a condition such as the husband's guarantee to restore the dowry.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: verification of anything beyond the event itself.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`GV1`** (governance mode; component `none`; allowed `collective|elder-fixed|external-administered`; applicability `.NA`)
  - expected value: `external-administered` (communal officials of the Monte; depositors had no voice).
  - confidence in this prior (high / medium / low): high.
  - what reading would falsify it: any organ of depositors deciding over the fund.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`DR1`** (pool duration; component `none`; allowed `single-event|fixed-cycle|open-ended`; applicability `.NA`)
  - expected value: `open-ended`: a standing fund with continuous enrolment; each deposit has a term, but the pool does not complete a cycle.
  - confidence in this prior (high / medium / low): high.
  - what reading would falsify it: closed annual or periodic cohorts liquidated at the term (→ `fixed-cycle`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.
- **`DR2`** (terminal distribution; component `none`; allowed `on-completion|on-default|perpetual|none`; applicability `DR1`)
  - expected value: `.NA`, following `DR1 = open-ended`.
  - confidence in this prior (high / medium / low): high, conditional on DR1.
  - what reading would falsify it: DR1 not open-ended.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no (inapplicable).
- **`RB1`** (peril-risk bearer; component `loss-sharing`; allowed `capital-provider|labour-provider|third-party|shared|all-stakeholders`; applicability `.NA`)
  - expected value: a split. Before 1433, `capital-provider` (the depositor loses the whole deposit on the girl's death); after 1433, `shared` (the depositor loses the gain, the principal comes back). Flag that the locator presumes a capital/labour pair this form lacks; the depositor is read as the capital provider and the commune as obligor.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: the 1433 change absent or dated otherwise; or no forfeit at all on death in 1425.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no; but the value is analyst-imposed and possibly `.NR` on locator grounds.
- **`RB2`** (market-risk bearer; component `loss-sharing`; allowed `capital-provider|labour-provider|third-party|shared|all-stakeholders`; applicability `.NA`)
  - expected value: `.NR`; the nearest thing to market loss is payment in depreciated Monte credits in the crisis, borne by the beneficiaries, which I would put in notes rather than force into this cell.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: the sources treat the depreciation of Monte credits paid as dowries as a loss falling on depositors or husbands (→ `capital-provider`, possibly split by date).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): yes.
- **`RB3`** (security or pledge; component `owner-shielding`; allowed `vessel|goods|freight|real-estate|surety|personal|general-estate|mixed|none`; applicability `.NA`)
  - expected value: `.NR`. No advance is made to a member; the depositor's advance is to the commune, secured (if at all) on communal revenues, which no value names. A guarantee required of the husband for the restitution of the dowry, if the Monte demanded one, would be `surety` on a secondary obligation, and I would flag rather than code it.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: the Monte required guarantors of the husband as a condition of payment, securing an obligation owed to the fund or enforceable through it (→ `surety`).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): yes.
- **`RB4`** (discharge on total loss; component `owner-shielding`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `.NA` on the locator (`labour-party`: there is no labour-supplying party). If the locator is set aside, the commune's obligation is extinguished on the girl's death (`1`) before 1433 and only as to the gain (`P`) after, which would be a split; I expect to flag this, not code it.
  - confidence in this prior (high / medium / low): medium on `.NA`.
  - what reading would falsify it: a reading of the locator that admits the commune as obligor (MS ruling).
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no (inapplicable).
- **`PR1`** (peril priced ex ante; component `risk-pooling`; allowed `1|P|0`; applicability `.NA`)
  - expected value: `P`: the yield is fixed before the event and differentiated by term, and its level presupposes forfeits, but it is not graded by the girl's age or any assessment of the peril, and no mortality calculation is articulated.
  - confidence in this prior (high / medium / low): low.
  - what reading would falsify it: yields graded by the girl's age at deposit, or officials computing the yield from expected forfeits (→ `1`); a flat interest rate with no reference to forfeits (→ `0`). Per the vocabulary's coding rule, a price inferred from the yield is analyst-imposed.
  - expected to be `.NR` because the sources will not ask the question? (yes / no): no.

## 4. Row-level expectations

- **Period.** Yes. The 1433 reform (principal returned on the girl's death) should move `RB1` and, if coded, `RB4`, and may move `MC1` (how much of the hazard is mutualised) and `PR1`. The payment crisis of the 1470s–1480s (delay, part payment in cash, the rest in Monte credits or deferred, lower rates on new deposits) should move `LS1` and possibly `PY3` and `RB2`. Rules on girls entering convents (date unknown to me) may touch `PY1`. I expect at least one split proposal (1425–1433 / 1433–1530) and possibly a second at the crisis.
- **Value sets.** `PY2` (no value for a payout fixed by deposit and term with no competing claimants); `PY0` (neither indemnity nor a rotation/lot/auction draw); `RB4` and `RB1`/`RB2` (locators presuppose a capital/labour pair); `RB3` (no value for security on public revenues); `CN2` (no value for a contribution chosen by the member).
- **Coverage.** `owner-shielding` (`LS3`, `RB3`, `RB4`): all `.NR` or `.NA`.
- **Neighbours.** Expectation only, no computation: closest to `tontine_en_1693` and `tontine_fr_royal` on `MB3`, `CN1`, `PY1` and the survivorship element (forfeits funding survivors), and to `widows_fund_scotland` and `craft_widows_fund_edinburgh` on `PY1 = life-event` with a fixed payout; unlike all of them on `GV1 = external-administered` and on the trigger being a marriage rather than a death. Any likeness to the tontines is parallelism at most, and I expect no descent to be argued.
- **Sources.** Molho 1994 ch. 2 for most structural cells (founding, terms, 1433, administration, changes); Kirshner 2015 ch. 4 for `VF1`, `VF2`, `PY1`, `PY3` and the payment crisis; Kirshner & Molho 1978 for founding legislation and the 1433 reform; the two Morrison articles for `HZ1` only.

## 5. Hash

Printed after writing and given to MS in the coding chat's message.
