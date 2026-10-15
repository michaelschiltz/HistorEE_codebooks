# Coding notes — `monte_doti_florence`, `loss_mitigation_forms` (2026-10-15)

Blind bundle `~/GitHub/_blind-monte-delle-doti-2026-10-15`. Coder `ai`, `claude-opus-5-5`, effort `high` (the fixed field set in the brief; the committed priors file left effort for MS to fill because the setting was not visible inside the session, and that file has not been touched since its hash was confirmed). One row of 26 cells, tradition `Tuscan (Florentine)`, period `1425-1530`. A proposal, not a commit: nothing outside `proposed-of/` and the filled priors was written, and `git` was not run.

## 0. Ordering, priors and blindness

- Priors filled before any file in `sources/` was opened or listed; sha256 `b66aa269caf256b88e2ad834b1a9755441b14f1e4b06ee1a1c35e05cc28817ca`, confirmed by MS ("Hash matches") before the first source was opened.
- **Every one of the 26 cells was fixed before anything about the matrix was computed.** The only matrix computation made (value-instance counts per characteristic, §9) ran after `rows-monte-delle-doti-2026-10-15.csv` was written and committed to `proposed-of/`, and no cell was changed after it. No nearest-neighbour or similarity computation was run at any point.
- Leaks: none found. Before the priors, a regex sweep (`dot[ie]|dowr|florent|tuscan|kirshner|molho|marriage`, plus `monte` on non-data files) of every non-source bundle file returned nothing about this form; the 15 `data.csv` hits concern Ottoman marriage portions (`avariz_*`) and the 1345 Florentine guild *societas* in `confraternity_fund_it`. Both skills (`code-a-form`, `run-a-coding-batch`) were read in full and name neither the form nor its sources.
- Tools: no Zotero, Undermind, Elicit, web search, Project or memory file was used for this batch.

## 1. Reading record

All text extracted with `pdftotext -layout` and read in the order below; printed pages cited throughout. Page maps checked against running heads on the text layer and on every image rendered: all as the README states (Molho ch. 2-3 printed = file + 26; Appendix 1 = file + 350; KM 1978 = file + 402; Kirshner ch. 4 file 1-20 = 94-113, notes file 23-40 = 292-309; Morrison 1977 = file + 486; Morrison 1985 = file + 527).

| file                                                  | how far                                                                                                                            |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `molho-1994_frontmatter_title-cip-contents-dates.pdf` | in full (incl. Note on Dates)                                                                                                      |
| `molho-1994_ch2-3_pp27-127.pdf`                       | in full, pp. 27-127 (Table 3.1, p. 87, garbled on the text layer; not used)                                                        |
| `molho-1994_app1-sources_pp351-360.pdf`               | in full                                                                                                                            |
| `molho-1994_ms-sources-abbreviations_pp433-434.pdf`   | in full                                                                                                                            |
| `kirshner-molho-1978_jmh50_pp403-438.pdf`             | in full                                                                                                                            |
| `kirshner-molho-1978_p403_ocr.txt`                    | **0 bytes** (see defects)                                                                                                          |
| `kirshner-2015_frontmatter_…pdf`                      | in full                                                                                                                            |
| `kirshner-2015_ch4_…pdf`                              | in full: ch. 4, App. 4, notes 292-309; the ch. 5 notes on p. 309 read only for the date discrepancy in §8, nothing coded from them |
| `morrison-kirshner-molho-1977_aje106_pp487-492.pdf`   | in full                                                                                                                            |
| `morrison-kirshner-molho-1985_ajph75_pp528-535.pdf`   | in full                                                                                                                            |

**Page images checked** (rendered with `pdftoppm`, read by eye; every figure and every quotation in a cell was read from these, not from the text layer): Molho 30, 31, 32, 34, 35, 37, 38, 43, 45, 46, 47, 49, 52, 53, 55, 66, 68, 69, 70, 71, 77, 81, 82, 83, 111, 112, 356, 359; Kirshner and Molho 1978, 403, 406, 408, 409, 411, 419; Kirshner 2015, 94-95, 96, 101, 102, 112, 298, 306, 308, 309; Morrison, Kirshner and Molho 1985, 528, 529; Morrison, Kirshner and Molho 1977, 487 (rendered, not used).

**Defects in the bundle, flagged not repaired.** (a) `kirshner-molho-1978_p403_ocr.txt` is empty, though the README calls it the OCR of p. 403. (b) The README says p. 403 has no text layer; `pdftotext` extracted one. I OCR'd the page image with `tesseract`; it matches the layer. No cell rests on p. 403. (c) The ch. 5 note on p. 309 is out of scope and coded nothing.

**Scope exclusions applied.** Charitable dowry bequests and confraternity subsidies (Molho 104-109, incl. the Borromei bequest administered by the Monte) coded nothing. The Monte comune's own interest, prices and debt were used only where they price or pay this fund's claims (RB2, LS1). The special gabella of 16 January 1530/1 (1531 modern style) falls after the period's end and moved no cell.

## 2. The row

| char | value                 | conf.  | articulation    | lang |
|------|-----------------------|--------|-----------------|------|
| MC1  | spreading             | medium | analyst-imposed | en   |
| MB1  | territorial-subject   | medium | articulated     | la   |
| MB2  | 1                     | medium | articulated     | la   |
| MB3  | voluntary             | medium | articulated     | la   |
| CN1  | ex-ante-lump          | medium | articulated     | it   |
| CN2  | proportional-to-stake | medium | analyst-imposed | en   |
| CN3  | .NA                   | .NA    | .NA             | .NA  |
| HZ1  | mixed                 | medium | analyst-imposed | en   |
| HZ2  | P                     | low    | analyst-imposed | en   |
| PY0  | individual-draw       | low    | analyst-imposed | en   |
| PY1  | life-event            | medium | articulated     | la   |
| PY2  | .NR                   | .NR    | .NR             | en   |
| PY3  | 1                     | medium | articulated     | it   |
| LS1  | pro-rata              | low    | analyst-imposed | en   |
| LS2  | 0                     | medium | analyst-imposed | en   |
| LS3  | .NR                   | .NR    | .NR             | en   |
| VF1  | official-adjudication | medium | articulated     | la   |
| VF2  | mixed                 | medium | articulated     | la   |
| GV1  | external-administered | medium | articulated     | la   |
| DR1  | open-ended            | medium | analyst-imposed | en   |
| DR2  | .NA                   | .NA    | .NA             | .NA  |
| RB1  | capital-provider      | medium | analyst-imposed | en   |
| RB2  | shared                | low    | analyst-imposed | en   |
| RB3  | .NR                   | .NR    | .NR             | en   |
| RB4  | .NA                   | .NA    | .NA             | .NA  |
| PR1  | P                     | low    | analyst-imposed | en   |

No cell is `high` (cap `medium`). Every `articulated` cell quotes an enactment, a register entry, a certificate or a deliberation verbatim in Latin or Italian as Molho or Kirshner print it; the rest rest on authors' paraphrase and are `analyst-imposed`. `source_read` is `partial` throughout because every cell cites at least one book of which two chapters were supplied. **One witness:** every note citing more than one work says that the works are one witness; no agreement among them is counted as corroboration.

## 3. Decision points, with the alternative stated fairly

1. **MC1 = spreading (low).** For: the commune, an outside party, assumes the father's dotal burden for a price fixed ahead ("a father's material burden shifted to the polity", Molho 32; "the equivalent of a premium", 43; "primitive insurance policies", 34), keeps the forfeits as its own surplus (the 1452 law, Molho 49), and no depositor's payout depends on another's. Against, for **pooling**: the forfeits of girls who die finance the survivors' yield (Molho 45), the very cross-subsidy that makes tontines pooling in this census. Against, for **allocation**: the enactment assigns the peril of death to the depositor by rule. I take spreading because the residual and the shortfall both sit with the commune. **This call decides whether the form appears in the committed risk-pooling view at all** (its filter is `MC1 = pooling`); MS should rule on it before anything comparative is read off the row.
2. **MB1 = territorial-subject (medium, articulated)** on the 1425 *habilis* clause and the 1434 *quelibet puella … de quocumque loco in quo comune Florentie preheminentiam vel custodiam haberet* clause. Alternative: contract (joining is by deposit).
3. **PY0 = individual-draw (low).** Alternative individual-indemnity: the enactment pays *pro restitutione quantitatis solute pro dote*, and the husband had to show a dowry promised at least equal to the matured value. Rejected because a dowry is a chosen outlay at a life event, not a realised loss, and the sum is fixed by deposit and term. Neither value fits the vocabulary's glosses.
4. **HZ2 = P (low).** Peril indifferent, claim responsive (timing of marriage to maturity, false consummation claims, transfers of deposits from girls unfit for marriage). Alternatives: `.NR` (the sources never frame responsiveness) or `0` (the peril alone).
5. **VF1 = official-adjudication (medium, articulated)** on the officials' deliberation for Baldo della Tosa (*deliberaverunt quod Baldus … habeat dotem suam, recepta fide …*). Alternative: documentary.
6. **VF2 = mixed (medium, articulated)** on *in quantum fuerit consummatum matrimonium et dos confessata et soluta ghabella*.
7. **LS1 = pro-rata (low).** A uniform share of each claim was deferred or paid in credits. Qualified by Molho's own statement that dowries were "paid in full, more or less promptly" until 1478 (45).
8. **RB1 = capital-provider (medium).** The prior expected a split at 1433 to `shared`; the sources show the commune never shares a loss on a death, so 1433 changes the depositor's loss in magnitude only.
9. **RB2 = shared (low), split proposed.** Phase 1 (to August 1446) is `third-party` only on the MC1 reading of the commune as the outside party.
10. **RB3 = .NR.** The only security in the sources secures the husband's restitution to his wife (guarantors; the 1441 law), not anything owed to or by the pool. Alternative: `mixed` (surety and real estate), which I judge to be coding the wrong obligation.
11. **RB4 = .NA** on the `labour-party` locator; the would-be values, if MS admits the commune as obligor, are in the cell note and imply a split at 23 April 1433.
12. **PR1 = P (low).** Priced ex ante by term with death explicitly in view ("per cagione della morte", 1462/3), but not on the individual girl's exposure and "in the absence of actuarial tables".
13. **CN2 = proportional-to-stake (medium).** The vocabulary has no value for a member-chosen contribution; flagged.
14. **CN3 = .NA.** A lump is paid before the account exists; nothing is ever outstanding.

## 4. The split test, cell by cell

| cell    | holds 1425-1530?                | dated changes examined                                                                                | outcome                                                       |
|---------|---------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| MC1     | yes                             | 23 Apr 1433; 24 May 1434; Jan 1435/6                                                                  | variant                                                       |
| MB1     | yes                             | 24 May 1434; 17 Jan 1461/2; 1463; 21 Mar 1451/2; 30 Apr 1477                                          | variant                                                       |
| MB2     | yes                             | ritratto from 1471/2                                                                                  | variant (adds a numerical limb)                               |
| MB3     | yes                             | Mar 1440/1 (medium of deposit); gabella 16 Jan 1530/1 out of period                                   | variant                                                       |
| CN1     | yes                             | Feb 1439/40, Mar 1440/1 deposits in credits                                                           | variant                                                       |
| CN2     | yes                             | rates 1428-1436; 1455/6 noncitizen premiums; 1458 pegging; 21 Mar 1451/2 ceilings                     | variant                                                       |
| CN3     | n/a                             | —                                                                                                     | .NA                                                           |
| HZ1     | yes                             | fiscal component sharpens after 1472                                                                  | variant                                                       |
| HZ2     | yes                             | —                                                                                                     | holds                                                         |
| PY0     | yes                             | refunds 23 Apr 1433, 15 May 1437                                                                      | variant                                                       |
| PY1     | yes                             | refunds 23 Apr 1433, 20 Nov 1436, 15 May 1437                                                         | variant                                                       |
| PY2     | n/a                             | ritratto 1471/2 (rations entry)                                                                       | .NR                                                           |
| PY3     | yes                             | ceilings from 21 Mar 1451/2; cash shares 1475, Nov 1478                                               | variant                                                       |
| LS1     | yes from 16 Aug 1441            | before 16 Aug 1441 no shortfall and no rule recorded                                                  | considered, not proposed: unrecorded is not a different value |
| LS2     | yes                             | Nov 1478 7 percent fund                                                                               | holds                                                         |
| LS3     | n/a                             | —                                                                                                     | .NR                                                           |
| VF1     | yes                             | contado attestation, earliest ref. Feb 1454                                                           | variant                                                       |
| VF2     | yes, so far as the sources show | 1425 clause names consummation only; law of 1441                                                      | considered, not proposed: no payment before 1433 is recorded  |
| GV1     | yes                             | 1458 reformers; Nov 1478                                                                              | variant                                                       |
| DR1     | yes                             | new accounts 1452, 1458; ritratto 1471/2                                                              | variant                                                       |
| DR2     | n/a                             | —                                                                                                     | .NA                                                           |
| RB1     | yes                             | 23 Apr 1433; 24 May 1434; Jan 1435/6; 20 Nov 1436; Apr 1446; 4 Feb 1455/6; 18 Jun 1463; 10 Jan 1471/2 | variant (magnitude)                                           |
| **RB2** | **no**                          | **18 Aug 1446 (first), 21 May 1472 (rule)**                                                           | **split proposed**                                            |
| RB3     | n/a                             | law of 1441 (wrong obligation)                                                                        | .NR                                                           |
| RB4     | n/a                             | 23 Apr 1433 if the locator were widened                                                               | contingent split, not proposed                                |
| PR1     | yes                             | 1455/6 noncitizen premiums; 1462/3 provision                                                          | holds                                                         |

**Split proposal (adjudication for MS).** Divide the row at **18 August 1446** into `monte_doti_florence` 1425-1446 (RB2 = third-party) and 1446-1530 (RB2 = shared). Alternative date **21 May 1472**, when paying part of every dowry in credits became the rule rather than an episode (Molho 47 calls the 1446 practice "repeated in subsequent years", but 45 says dowries were paid "in full, more or less promptly" until 1478). Every other cell holds across both phases. My recommendation is **not** to split on one cell resting on a locator defect: record the change in the note, as done, until a second cell separates the phases. If RB4's locator is widened, a split at 23 April 1433 would follow, and the two candidate splits do not coincide.

## 5. Cells declined

- **PY2 `.NR`**: no fitting value; the trigger fixes the payee and the deposit fixes the sum.
- **LS3 `.NR`**: not addressed; the fines in the sources punish misconduct and are not liability for the pool.
- **RB3 `.NR`**: no advance to a member; the security described secures another obligation (§3.10).
- **CN3 `.NA`**: a lump is paid before the account exists.
- **DR2 `.NA`**: DR1 is open-ended.
- **RB4 `.NA`**: `labour-party` locator, and there is no labour party.

## 6. Per-component coverage

| component              | characteristics                     | substantive | .NR / .NA |
|------------------------|-------------------------------------|-------------|-----------|
| risk-pooling (WP1)     | MC1 MB3 CN1 HZ1 HZ2 PY0 PY1 PY2 PR1 | 8           | PY2 .NR   |
| loss-sharing (WP1)     | CN2 CN3 LS1 RB1 RB2                 | 4           | CN3 .NA   |
| outcome-coupling (WP1) | PY3 LS2                             | 2           | —         |
| owner-shielding (WP1)  | LS3 RB3 RB4                         | **0**       | all three |
| none                   | MB1 MB2 VF1 VF2 GV1 DR1 DR2         | 6           | DR2 .NA   |

20 substantive of 26. **Owner-shielding learned nothing**, as the priors expected. Four of the eight substantive risk-pooling values were coded `low`; three remain `low` after MS raised MC1 to `medium`.

## 7. Vocabulary and well-formedness problems, flagged not repaired

- **PY0**: individual-draw is glossed "by rotation, lot or auction"; a draw by event (marriage) has no value. Second instance of the problem after the survivorship forms.
- **PY1 locus**: the trigger is the enrolled girl's own event and the payee is her husband; the logbook-6 locus defect bites differently here than on `tontine_en_1693`.
- **RB1/RB2/RB4 locators** presuppose a capital/labour pair. A commune that takes deposits and owes a contingent sum is a counterparty-obligor with no value; RB2 phase 1 can only be written `third-party` by borrowing MC1's reading.
- **CN2** has no value for a contribution the member chooses.
- **RB3** is defined on "the advance"; a pool whose members advance to the institution, with security attaching only to a downstream private obligation, has no clean reading.
- **MC1**: Harris's three values separate poorly for a contingent claim sold by a polity; the row is a candidate test of whether `spreading` and `pooling` can share a survivorship cross-subsidy.
- No new characteristic or value is proposed.

## 8. Disagreements inside the one witness

- Law of PR 132, ff. 6v-9r (deposits in credits; security under Kirshner's reading): 24 March 1440/1 (Molho 37 n. 37) = March 24, 1441 (Kirshner and Molho 1978, 411) against 24 Mar. 1441/2 (Kirshner 2015, 308 n. 117), a year later in modern style.
- Seven Percent Fund enactment, PR 169, ff. 84v-86v: 14 November 1478 (Molho 70 n. 145) against 14 Oct. 1478 (Kirshner 2015, 309 n. 11).
- Oral declarations of consummation made to the Monte officials (Kirshner 2015, 96) or to the officials of the gabella dei contratti (Molho 358).
- Molho 45 ("until 1478 … paid in full, more or less promptly") sits uneasily with Molho 47 (discounted payment in credits from 1446). Both are recorded in LS1 and RB2.

## 9. What the matrix learned (computed after every cell was fixed)

- **No new value-instance.** Every substantive value in the row already occurs in the census for its characteristic.
- The row adds a fourth `MC1 = spreading` form, and therefore does not enter the committed risk-pooling view.
- A split at 18 August 1446 would give `RB2 = third-party` its first instance; a widened RB4 locator would give `RB4 = P` its first instance. Both observations came after the cells were fixed and moved no cell; they are reported because they would make a split or a locator ruling look attractive for the wrong reason.
- Zero-instance values left untouched include `CN2 = proportional-to-capacity`, `VF2 = conduct-compliance` and `GV1 = elder-fixed`.

## 10. The six answers

**1. What was coded, and on what evidence.** One row, `monte_doti_florence`, 26 cells: 20 substantive, 3 `.NR`, 3 `.NA`. The evidence is Molho 1994 chs. 2-3 and App. 1, Kirshner and Molho 1978, Kirshner 2015 ch. 4 with its notes, and Morrison, Kirshner and Molho 1985, treated as one witness. Nine cells are `articulated` on Latin or Italian clauses printed in those works: the founding enactment PR 114 of 23 February 1424/5; the eligibility clause of 24 May 1434; the 1437 *tamquam vere mortua* clause; a 1477 tax-standing certificate and the Cento law of 30 April 1477; and two deliberations of the Monte officials. Eleven are `analyst-imposed`. No cell is `high`.

**2. What could not be coded, and why.** PY2 has no fitting value. LS3 is not addressed by the sources. RB3 is `.NR` because the only security in the sources secures a different obligation. CN3, DR2 and RB4 are inapplicable: a lump is paid before the account exists, the pool is open-ended, and there is no labour party. The whole owner-shielding component is empty.

**3. Which of my expectations were falsified.** Quoted verbatim from the committed priors:

- MC1, "expected value: `pooling`, flagged as a hard call." **Falsified** toward spreading, at low confidence.
- MB1, "expected value: `contract` (membership by making a deposit), with `territorial-subject` the alternative if eligibility was limited to citizens or subjects of the Florentine state." **Falsified**: the 1434 clause makes eligibility a matter of the dominion.
- MB2, "expected value: `1` (closed to a defined class: girls, possibly of a stated age or status), not numerically restricted." **The value held; the clause "not numerically restricted" is falsified** from 1471/2 (ritratto).
- HZ2, "expected value: `.NR`; if the sources speak, `P` on the census's reading (the claim responding to the cover: marriages timed to maturity, contested consummation)." **The primary expectation (.NR) is falsified and the conditional held**: the sources speak, and on exactly those two points.
- VF1, "expected value: `documentary` (a notarial or parish instrument proving marriage and consummation, presented to the officials), with `official-adjudication` the close alternative." **Falsified** toward the alternative.
- RB1, "expected value: a split. Before 1433, `capital-provider` (the depositor loses the whole deposit on the girl's death); after 1433, `shared` (the depositor loses the gain, the principal comes back)." **Falsified**: no split, because the commune never bears a loss on a death.
- RB2, "expected value: `.NR`; the nearest thing to market loss is payment in depreciated Monte credits in the crisis, borne by the beneficiaries, which I would put in notes rather than force into this cell." **Falsified**: the sources state the burden's location in two dated phases.
- Period, "The 1433 reform (principal returned on the girl's death) should move `RB1` and, if coded, `RB4`, and may move `MC1` (how much of the hazard is mutualised) and `PR1`." **Falsified for RB1, MC1 and PR1**, which take variants only; RB4 is contingent. "I expect at least one split proposal (1425–1433 / 1433–1530)". **Falsified**: the one split proposed is at 1446 (or 1472), on RB2.
- Period, "The payment crisis of the 1470s–1480s … should move `LS1` and possibly `PY3` and `RB2`." **Falsified on timing**: the first crisis is 16 August 1441 and the first discounted payment is 18 August 1446. PY3 does not move.
- Textbook account, "From the 1470s, and acute in the late 1470s and 1480s, the commune could not pay maturing dowries in full or on time". **Falsified on its start date** (1441); held on the acute phase.
- Textbook account, "A girl who entered a convent: by some later provision a portion was paid as a monastic dowry, otherwise the deposit was lost." **Falsified**: from 15 May 1437 the capital was refunded to the nunnery.
- Textbook account, "I do not know whether the Monte itself required such a guarantee before paying." **Answered**: under a law of 1441 it required security where its officials acted in place of the bride's father (Kirshner 2015, 112).
- Held: MB3, CN1, CN2, CN3, HZ1, PY0, PY1, PY2, PY3, LS1 (in substance), LS2, LS3, VF2 (on its second limb), GV1, DR1, DR2, RB3 (its falsifier, "securing an obligation owed to the fund or enforceable through it", is not met), RB4, PR1, the value-set expectations, and the coverage expectation for owner-shielding.

**4. Any characteristic that did not fit the evidence.** PY0 (no value for a draw by event), PY2 (no value at all), CN2 (no value for a member-chosen contribution), RB1/RB2/RB4 (locators presuppose a capital/labour pair and have no counterparty-obligor), RB3 (security attaches to a non-pool obligation), and MC1 (Harris's trichotomy fits a commune's contingent claim badly).

**5. Dependence or well-formedness problems noticed and not repaired.** PY1's locus (girl's event, husband's payment). RB2 needs MC1's reading to be codable in phase 1, an undeclared dependence between a loss-sharing cell and the mechanism cell. RB4 would split the row only if its locator were widened, so a locator ruling would create a period split, which is a reason to rule on the locator before any batch relies on it. The definitions of PY0's two values each assert one limb this form fails. None repaired.

**6. What to acquire next, and which cell it would move.**

- A witness independent of Kirshner and Molho on the fund's terms. Ideally the edited text of PR 114 (Kirshner, "Pursuing Honor While Avoiding Sin", edition at pp. 234-239 per Kirshner and Molho 1978, 406 n. 9), which would allow articulated cells to rest on the enactment rather than on Molho's ellipses. It would move **MC1, PY0, PY3 and LS1** (whether the 1425 text says anything about insufficiency).
- [CORRECTED 2026-10-15, after MS's note: this chapter is ch. 5 of Kirshner 2015 and already held; it needs adding to the bundle, not acquiring. Original wording kept below.] Kirshner and Klerman, "The Seven Percent Fund" (Kirshner 2015, ch. 5, pp. 114-130), would move **RB2** (whether the post-1478 credits carried market loss as a rule) and settle the **14 October / 14 November 1478** date.
- The page of the 1441 law (PR 132, ff. 6v-9r) as printed anywhere would settle **VF2** and the **1441/1442** date.
- Nothing in the bundle bears on **RB3** or **LS3**; a juristic consilium on the Monte (Angelo da Chivasso's *consilium*, edited in Kirshner's "Pursuing Honor", per Kirshner and Molho 1978, 434 n. 52) might move LS3.

## 11. Checks

Run on a scratch copy outside the bundle (`$HOME/scratch/check` on the device VM: `scripts/`, `datasets/`, `vocabularies/`, `views/` copied). The 26 rows were appended to `data.csv` with temporary ids LM-0796 to LM-0821 (the last live id is LM-0795, and the minted ids were asserted absent), and the type row was appended to `loss_mitigation_type.csv`. Both proposed CSVs have exactly the target files' headers and no CR.

- `python3 scripts/check_vocabularies.py` → "✓ vocabularies valid — 2 files, 87 codes; no ragged rows, all references resolve, all values within allowed_values, enums agree, shared type rows agree"; exit 0.
- `python3 scripts/check_dependence.py datasets/loss_mitigation_forms` (the directory) → "no applicability problems", "no articulation problems", "dependence problems: 0"; the redundancy report places the row at `VF1 = official-adjudication`, `VF2 = mixed`, a pair already present; exit 0.
- `python3 scripts/check_quotations.py` → "0 error(s), 0 coverage gap(s)"; exit 0.
- `python3 -m frictionless validate datasets/loss_mitigation_forms/datapackage.json` (frictionless 5.20.0, installed `--user`) → `data.csv` VALID, `recodings.csv` VALID; exit 0.
- Hand sweep of the proposed file: 26 distinct `char_id`, equal to the vocabulary's set; every substantive value within `allowed_values`; `.NA` propagated through confidence, articulation, source_ref, source_lang and source_read; `.NR` carries `.NR` confidence and articulation; no `high`; no `[verify]`; `coder`, `reviewed_by`, `review_status`, `coder_model` and `coder_effort` uniform; no reserved term outside a quotation; applicability consistent (PY0 is not collective-good, so PY1-PY3 exist; VF1 is not none, so VF2 exists; DR1 is open-ended, so DR2 is `.NA`).
- Nothing in the bundle outside `proposed-of/` was written after the filled priors (their mtime is unchanged since the hash was confirmed).

## 12. MS rulings, 2026-10-15 (recorded after the coding; no value changed)

All nine recommendations put to MS were accepted.

- **MC1**: `spreading` kept. The row sits outside the risk-pooling view by design. **Confidence raised from `low` to `medium` by a further MS ruling the same day**; it was coded `low` (§3.1), and the §2 table now shows `medium`.
- **RB2**: no split. The change at 18 August 1446 / 21 May 1472 stays in the cell note, and both phases are recorded.
- **RB4**: `.NA` kept and the `labour-party` locator not widened. The missing obligor locator is recorded as a vocabulary defect, to wait for a second form that needs it.
- **RB3**: `.NR` kept.
- **Chapter 5** (Kirshner and Klerman, "The Seven Percent Fund", Kirshner 2015, ch. 5): the blind row is applied first; the chapter is then read as an open recoding pass in `recodings.csv` (`condition = open`, `adjudication = pending`), limited to RB2, LS1, LS2, PY3 and the 1478 date.
- **§10.6 wording**: corrected visibly (above), not rewritten.
- **Dating disagreements**: logged in logbook/5; no action.
- **Bundle defects** (empty p. 403 OCR file; the README's claim about p. 403): for the operator to repair in the bundle-building step before the next batch.
- **Effort field**: no action.

Edits made after the rulings, all to notes only: the cell notes of MC1, RB2 and RB4 each gain one sentence recording the ruling; the type row's `key_source` replaces its split sentence with the rulings; the logbook draft and commit message are updated to match. No `value` or `articulation` changed; one `confidence` changed, MC1 from `low` to `medium`, by MS ruling. All checks re-run (§11) after these edits.
