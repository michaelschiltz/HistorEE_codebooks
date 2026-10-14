# Operator record, part 1: the Florentine *monte delle doti* — nothing held, parked on acquisition (2026-10-14)

- **Slug:** `monte-delle-doti-scheme`. Operator (Chat A), 2026-10-14, `claude-opus-5-5`. It is spent on this form and never codes it.
- **Status:** steps 1–4 of the operator's instruction were run as far as they can be without a source. **Step 5 — selection brief, priors template, coding prompt, `make_blind_bundle.py` command — is deferred by MS's decision (2026-10-14, in chat) until the literature is in Zotero.** A later operator session writes part 2. It must re-check the holdings and recompute the tables at that row count.
- **Not for the coding chat. Part 2 must keep this file out of the bundle.** It names comparator rows and the characteristics on which the 2026-09-10 entry set them, and that is an expectation about this form. `make_blind_bundle.py` copies every tracked file and has no per-file exclusion. So part 2 either deletes this file's copy from the built bundle and confirms it is absent by a term count before handing over, or builds a minimal bundle (the `commenda-pilot-operator` design of 2026-09-28). Today's logbook entries cite it by filename only, and are written to be shippable.

## 1. Inputs and the order of work

Read first, on MS's instruction: logbook 2, 2026-09-10, in full; logbook 4's standing table (the slug and session columns of every row, plus rows `italian-archives-survey` and `european-archives-survey` in full, because they matched a term sweep). **The 2026-09-10 entry was written by `italian-archives-survey`, whose standing row says it is spent on mechanism for this candidate.** This session therefore re-spent that mechanism; it did not spend it first.

The spend budget was declared to MS in chat before any reconnaissance, and §2 reconciles it. Then the following were done, in order: Zotero catalogue and full-text-cache counts; an Undermind sweep, at MS's request once nothing was found held; vault and repository counts; the matrix tables; the declarations.

## 2. Spend: the budget as declared, and the reconciliation

| question | planned | reached | what forced any excess |
|---|---|---|---|
| 1. holdings | 0; 2 for offsets; 1 for term counts | **0 and 1 only.** No offset could be measured, because nothing is held. Then **4–5 on external literature**: Undermind titles, plus the deep search's abstract-level summary | Nothing was held, and MS asked for an Undermind sweep. Titles (rung 4) were enough to answer *what to acquire*. **The summary was read because it is returned with the listing. It was not needed, and that is the excess.** It characterises what the literature covers, not values. No PDF was opened. |
| 2. dataset | 1; 2 if needed | 0 | nothing to count in |
| 3. scope and split | 2; contingent 5 | 0 | nothing to read; the split test is deferred (§5) |
| 4. tables and declarations | 5 on the matrix and named comparators | 5 as planned: the live `data.csv` of both censuses (795 and 948 rows); the cells of `tontine_fr_royal`, `tontine_en_1693`, `widows_fund_scotland` and `avariz_vakfi_kirkcesme`; the `tradition`, `period` and co-occurrence columns of both type vocabularies; the `key_source` of the rows citing Coudy, Kohn and Kuehn | — |
| 5. vault | 1 and 3 | 1 and 3: eight terms counted; `source-session` slugs extracted for the matching notes. **No title, no body.** | — |
| 6. repository residuals | 1; 5 on matching lines | as planned: logbook 4 lines 1088–1092, and one-line contexts in `Claude outputs/PILOT-DESIGN-commenda-primary-secondary-2026-09-27.md` and a `proposed-of/` candidate CSV | — |

Also seen, passively: the claude.ai Project's doc titles, which are listed in this chat's context.

## 3. Holdings (rungs 0–1)

**Neither Kirshner nor Molho is held, and no work treating the fund is held.** Method: a copy of `zotero.sqlite`. No title, container or bookTitle matches `dowr|dote|doti|monte|marriage market|dotal` except three irrelevant items. No creator is named Molho, Pezzarossa, Chabot, Klapisch-Zuber, Conti or Herlihy. The only Kirshner is Jonathan, reviewing *The Money Doctors from Japan* (`5JZAFB8C`); the only Marks is Andreas (`K3TH7ZGJ`).

**Full-text sweep** across the `.zotero-ft-cache` files, which cover **955 of 1,504** PDF attachments (698 of the 1,504 are linked files under the `attachments:` base directory):

| item | key (attachment) | `Monte delle doti` (any case) | `dowry fund` | `Monte` | 1425 / 1433 | Kirshner / Molho |
|---|---|---|---|---|---|---|
| Kohn 1999, *Risk Instruments in the Medieval and Early Modern Economy* | `EX3ZNEHH` (`QHQG68E7`) | 4 | 1 | 6 | 1 / 1 | 2 / 2 |
| Miner 2020, *Profit and Patrimony* | `35F9Q8EX` (`LK8K5XL8`) | 3 | 0 | 5 | 0 / 0 | 6 / 8 |
| Coudy 1957, *La « Tontine Royalle »* | `WVR6A3RT` (`GL6PVPDD`) | 2 | 0 | 1 | 0 / 0 | 0 / 0 |
| Kuehn 2008, *Heirs, Kin, and Creditors* | `G5R7XCAK` (`JTSXTYCK`) | 0 | 1 | 5 | 1 / 1 | 9 / 8 |
| Sapori & Procacci 1978 | `3BCUQHDF` (`5DFQ2QE7`) | 1 | 0 | — | — | 0 / 0 |
| de Roover 1948, *The Medici Bank* | `BJ8TSRTA` (`W85KSCNJ`) | 1 | 0 | — | — | 0 / 0 |

**These six mention the fund; none treats it.** By the code-a-form rule, a form whose own terms appear at most four times in the best held source cannot carry a row. **None of them may found a cell**, and §8 explains why each would also be a dependent witness.

**Residual gap, stated rather than closed.** The 549 PDFs without a cache sit under parents whose titles do not match. A loose PDF with no Zotero item, in the linked-files base directory, cannot be excluded; that directory was not granted to this session.

## 4. Acquisition, in priority order

The Undermind deep search is *Florentine Monte delle doti dowry fund literature and sources*, in the workspace *HistorEE — cooperative pooling census*. **Verification state is given per item. Nothing here may enter a `source_ref` until the item is in Zotero and its metadata confirmed.**

1. Kirshner, Julius. *Pursuing Honor While Avoiding Sin: The Monte delle doti of Florence*. Quaderni di Studi Senesi 41. 1978 (publisher and place from general knowledge: Milan, Giuffrè). **The monograph, and the acquisition that decides whether there is a batch** (§§5–6). **Unverified**: Undermind holds only its reviews — Bowsky, *Speculum* 54 (1979): 594–595, doi:10.2307/2855802; Bergfeld, *ZRG Kan. Abt.* (1984): 429–431.
2. Kirshner, Julius, and Anthony Molho. "The Dowry Fund and the Marriage Market in Early Quattrocento Florence." *Journal of Modern History* 50, no. 3 (1978): 404–438. doi:10.1086/241732. **Verified through CrossRef** (pages as CrossRef gives them; confirm against the PDF).
3. Kirshner, Julius. *Marriage, Dowry, and Citizenship in Late Medieval and Renaissance Italy*. Toronto: University of Toronto Press, 2015. doi:10.3138/9781442664517 (**CrossRef**). Ch. 5, "The Seven Percent Fund of Renaissance Florence", 114–130, doi:10.3138/9781442664517-008 (**CrossRef**). The deep search names another chapter, "The Morning After: Collecting Monte Dowries" (**unverified**). This is a collection of essays, so check which are reprints of item 1 or 2 (§8, N1).
4. Carboni, Mauro. "Financing Marriage in Early Modern Italy: Innovative Dowry Funds in Florence and Bologna." *The History of the Family* 27 (2022): 221–242. doi:10.1080/1081602X.2022.2070521 (Undermind; **open access**).
5. Molho, Anthony. "Investimenti nel Monte delle doti di Firenze: un'analisi sociale e geografica." doi:10.1400/129692. Undermind gives 2006, pp. 1000–1021, which looks like a container record. **Year and venue unverified.**
6. Molho, Anthony. *Marriage Alliance in Late Medieval Florence*. Cambridge, MA: Harvard University Press, 1994. Undermind's doi:10.2307/2169909 is probably a review's. **Unverified.** A second CrossRef query for it was refused by the proxy (HTTP 429).
7. Morrison, Alan S., Julius Kirshner, and Anthony Molho. "Life Cycle Events in 15th Century Florence: Records of the Monte delle Doti." *American Journal of Epidemiology* 106 (1977): 487–492. doi:10.1093/oxfordjournals.aje.a112496. Also "Epidemics in Renaissance Florence", *American Journal of Public Health* 75 (1985): 528–535, doi:10.2105/AJPH.75.5.528 (open access). Demography from the registers; low expected yield for cells. Undermind metadata only.

**A separately sourced comparandum, recorded and not proposed:** the Bolognese *Monte del Matrimonio* (Carboni 1999, *Alle origini della previdenza*, doi:10.1410/9880, unverified; Carboni 2022 above) and the Monte di Pietà dowries of Bologna (Chabot and Fornasari 1997, no DOI). If acquired, it would be **its own row, never folded into the Florentine one** (§6).

**On arrival:** create each item, attach the file, measure offsets (rung 2), and count the form's own terms (rung 1) — including the terms of any premise the brief relies on — before part 2 is written.

## 5. Datasets

- **`loss_mitigation_forms`: yes.** This is the census the 2026-09-10 entry named. A new type code is minted in the coding batch, with its source, under that entry's own rule.
- **`organizational_forms`: not warranted on present evidence, and deferred rather than refused**, on the `she_death_aid` precedent (logbook 2, 2026-10-14). That census's characteristics ask about an entity: personality (`LP*`), shielding (`AP*`), succession (`TS*`), claims (`CI*`), governance and charter (`MG*`, `FP*`). A row is warranted only if the acquired sources treat the fund as an arrangement **with assets, administration or claims of its own, distinguishable from the commune's public debt in which it sat**. If they describe it only as an account or office of the *Monte comune*, an organizational row would code the public debt under the fund's name, and that is the umbrella defect. **The question is settled at rung 2 on item 1's contents and running heads**, and at rung 1 by counting the entity terms (`ufficiali`, `Monte comune`, `credit*`, `transfer*`, `heir*`), before part 2 is written.

## 6. Scope

- **`tradition`:** "Tuscan (Florentine)", following `compagnia`'s convention in the organizational census.
- **`period`:** **open.** The 2026-09-10 entry gives a founding date. It was written from finding aids with no source opened, and it says so. **Count the premise in item 1 before using it.**
- **The split test is mandatory, and it cannot be applied until the sources are held.** MS's instruction states that the fund's terms changed over its life. Under the standing rule, a row whose value changes across its own period is split, not coded `P` or `.NR`. To place a boundary, part 2 needs: (i) the dated legislative changes the sources record, at rung 2 (contents, section titles) and rung 1 (counts of the dated provisions); and (ii) for each candidate boundary, the characteristic it would move. **A boundary that moves no characteristic this census codes is not a split.** A change of rate or term that leaves every cell's value unchanged is a variant recorded in `notes`, on the Pisa land-partnership precedent (logbook 2, 2026-10-12 (iv)). The characteristics a boundary could move are listed in §7, but **which ones move is a coding question, and this file does not predict it.**
- **Out of scope:** the *Monte comune* itself (no row, and none proposed); charitable dowry endowments (*doti di carità*), which are a different instrument; and Bologna's funds, which are separate rows if ever acquired.

## 7. Value tables, as at 795 / 948 rows (rung 5 on the matrix)

Counts are **forms**, one cell per `(type_id, char_id)`; there are no duplicates in either census. "Zero-instance" means an allowed value with no form. "One-instance" names the single form holding a value. **A loss-census row could touch any of the 26 loss characteristics**; which ones it touches is a coding outcome. The organizational table is carried for §5 only.

### loss_mitigation_forms: 795 rows, 51 forms with cells, last id LM-0795
duplicate (type,char): 0
| char | component | coded forms | substantive | value: forms | zero-instance | one-instance |
| MC1 | risk-pooling | 51 | 45 | pooling 30, allocation 12, .NR 6, spreading 3 | — | — |
| MB1 | none | 30 | 22 | .NR 8, locality 7, occupation 5, territorial-subject 4, contract 3, confession 3 | kinship | — |
| MB2 | none | 32 | 23 | 1 22, .NR 9, 0 1 | P | 0=averia_pool |
| MB3 | risk-pooling | 43 | 35 | voluntary 26, compulsory 9, .NR 6, .NA 2 | — | — |
| CN1 | risk-pooling | 34 | 28 | ex-ante-periodic 24, .NA 3, .NR 3, ex-post-assessment 2, ex-ante-lump 2 | — | — |
| CN2 | loss-sharing | 33 | 19 | equal 16, .NR 11, proportional-to-stake 3, .NA 3 | proportional-to-capacity | — |
| CN3 | loss-sharing | 30 | 16 | 1 14, .NR 11, .NA 3, P 2 | 0 | — |
| HZ1 | risk-pooling | 36 | 10 | .NR 26, mixed 6, idiosyncratic 3, covariate 1 | — | covariate=averia_pool |
| HZ2 | risk-pooling | 11 | 7 | P 5, .NR 4, 1 2 | 0 | — |
| PY0 | risk-pooling | 44 | 30 | individual-draw 16, individual-indemnity 12, .NA 9, .NR 5, collective-good 2 | — | — |
| PY1 | risk-pooling | 31 | 27 | rotation 14, realised-loss 7, life-event 4, .NA 3, need-assessed 2, .NR 1 | — | — |
| PY2 | risk-pooling | 32 | 16 | .NR 13, indemnity 6, rotation-lot 5, .NA 3, need-assessed 3, auction 2 | rotation-fixed | — |
| PY3 | outcome-coupling | 23 | 16 | 1 11, .NR 5, P 3, .NA 2, 0 2 | — | — |
| LS1 | loss-sharing | 15 | 7 | .NR 7, pro-rata 4, residual-on-fund 2, .NA 1, capped 1 | equal | capped=avariz_vakfi_kirkcesme |
| LS2 | outcome-coupling | 25 | 9 | .NR 12, 1 6, .NA 4, 0 2, P 1 | — | P=ko_mochiyori_yutsu_1876 |
| LS3 | owner-shielding | 31 | 14 | .NR 16, 1 7, 0 6, .NA 1, P 1 | — | P=guild_box_dutch |
| VF1 | none | 33 | 16 | .NA 11, official-adjudication 8, .NR 6, claimant-oath 5, communal-attestation 2, documentary 1 | none | documentary=guild_box_dutch |
| VF2 | none | 32 | 13 | .NA 11, mixed 9, .NR 8, loss-occurrence 2, claimant-need 1, claimant-fault 1 | conduct-compliance | claimant-need=craft_pension_edinburgh; claimant-fault=confraternity_fund_it |
| GV1 | none | 32 | 15 | .NR 17, collective 11, external-administered 4 | elder-fixed | — |
| DR1 | none | 35 | 31 | open-ended 15, fixed-cycle 14, .NR 3, single-event 2, .NA 1 | — | — |
| DR2 | none | 26 | 6 | .NA 14, on-completion 6, .NR 6 | on-default, perpetual, none | — |
| RB1 | loss-sharing | 16 | 16 | capital-provider 9, shared 3, all-stakeholders 2, third-party 2 | labour-provider | — |
| RB2 | loss-sharing | 15 | 15 | capital-provider 9, labour-provider 3, shared 3 | third-party, all-stakeholders | — |
| RB3 | owner-shielding | 41 | 21 | .NR 19, none 11, mixed 4, real-estate 2, general-estate 2, vessel 1, goods 1, .NA 1 | freight, surety, personal | vessel=bottomry; goods=respondentia |
| RB4 | owner-shielding | 15 | 11 | 1 9, .NA 4, 0 2 | P | — |
| PR1 | risk-pooling | 49 | 47 | 0 37, 1 6, P 4, .NR 2 | — | — |
### organizational_forms: 948 rows, 36 forms with cells, last id OF-0950
duplicate (type,char): 0
| char | component | coded forms | substantive | value: forms | zero-instance | one-instance |
| LP1 | legal-personality | 27 | 19 | 0 11, .NR 8, 1 6, P 2 | — | — |
| LP2 | legal-personality | 27 | 21 | 1 9, 0 8, .NR 6, P 4 | — | — |
| LP3 | legal-personality | 27 | 15 | .NR 12, 0 7, P 5, 1 3 | — | — |
| AP1 | entity-shielding | 27 | 13 | .NR 14, 1 8, 0 4, P 1 | — | P=bazacle_mill |
| AP2 | entity-shielding | 27 | 12 | .NR 15, 1 6, 0 4, P 2 | — | — |
| AP3 | owner-shielding | 30 | 17 | 0 13, .NR 12, 1 2, P 2, .NA 1 | — | — |
| AP4 | entity-shielding | 27 | 3 | .NA 24, 1 3 | P, 0 | — |
| TS1 | perpetual-succession | 29 | 24 | 1 17, 0 5, .NR 5, P 2 | — | — |
| TS2 | perpetual-succession | 32 | 28 | open 18, fixed-term 7, .NR 4, single-venture 3 | — | — |
| TS3 | perpetual-succession | 25 | 16 | .NR 9, 0 7, 1 5, P 4 | — | — |
| TS4 | perpetual-succession | 25 | 11 | .NR 13, 0 7, P 4, .NA 1 | 1 | — |
| CI1 | none | 31 | 28 | common 20, none 5, several-accounts 3, .NR 3 | — | — |
| CI2 | capital-lock-in | 28 | 21 | 1 12, .NR 7, P 6, 0 3 | — | — |
| CI3 | transferable-claims | 33 | 20 | .NR 13, 1 12, 0 4, P 4 | — | — |
| CI4 | transferable-claims | 32 | 19 | .NR 13, P 9, 0 6, 1 4 | — | — |
| CI5 | none | 6 | 4 | commingled 3, .NR 2, segregated 1 | — | segregated=mudaraba |
| LR1 | owner-shielding | 30 | 17 | .NR 12, unlimited-several 8, unlimited-joint 5, limited 4, .NA 1 | none | — |
| LR2 | outcome-coupling | 29 | 26 | coupled 24, .NR 3, veiled 2 | attenuated | — |
| LR3 | loss-sharing | 32 | 32 | 1 27, 0 5 | P | — |
| LR4 | risk-pooling | 29 | 22 | 0 19, .NR 7, 1 3 | P | — |
| LR5 | risk-pooling | 29 | 3 | .NA 19, .NR 7, diversifying 3 | synchronising, na | — |
| LR6 | outcome-coupling | 29 | 21 | symmetric 16, .NR 6, upside-only 5, .NA 2 | downside-only | — |
| MG1 | none | 32 | 30 | contract 16, membership 12, beneficiary 2, .NR 2 | — | — |
| MG2 | none | 28 | 26 | collective 18, single-principal 7, .NR 2, founder-fixed 1 | — | founder-fixed=waqf_khayri |
| MG3 | none | 29 | 10 | .NA 16, 0 5, 1 5, .NR 3 | P | — |
| MG4 | none | 31 | 28 | state-charter 11, private-contract 10, religious 5, .NR 3, customary 2 | — | — |
| FP1 | none | 32 | 32 | commercial-profit 20, mixed 9, pious-charitable 2, mutual-provision 1 | — | mutual-provision=bruderschaft_salzburg |
| FP2 | none | 30 | 18 | .NR 12, 1 10, 0 5, P 3 | — | — |
| FP3 | none | 29 | 19 | 1 11, .NR 10, 0 4, P 4 | — | — |
| FP4 | none | 30 | 21 | 1 14, .NR 9, P 4, 0 3 | — | — |
| CF1 | none | 33 | 32 | 0 14, 1 10, P 8, .NA 1 | — | — |
| CF2 | loss-sharing | 30 | 13 | .NA 13, 0 9, .NR 4, P 3, 1 1 | — | 1=ortoq_loan |
| CF3 | none | 33 | 30 | multilateral 21, bilateral 9, .NR 2, .NA 1 | — | — |

Loss-census notes for part 2: `PR1` has 6 forms at `1` and 4 at `P` (`1`: `bodemerij_amsterdam`, `bottomry`, `life_annuity_priced`, `marine_insurance`, `respondentia`, `widows_fund_scotland`; `P`: `craft_widows_fund_edinburgh`, `friendly_society_female_england`, `sea_loan`, `tontine_fr_royal`). `PY1=life-event` has four forms: `craft_widows_fund_edinburgh`, `she_death_aid`, `tontine_en_1693`, `widows_fund_scotland`. `CN1=ex-ante-lump` has two: `shenhui_gu_alloc`, `tontine_en_1693`. The comparator rows the 2026-09-10 entry names are thinly coded: `tontine_fr_royal` has 5 cells, `widows_fund_scotland` 6, `tontine_en_1693` 10, and `avariz_vakfi_kirkcesme` 23. Any comparison part 2 sets up on a cell that a comparator does not carry is not available, and part 2 must count before it predicts. The umbrella `tontine` carries no cells, as an umbrella should.

## 8. Declarations, made before any row exists

### Non-independence

- **N1. The Florentine literature is one witness.** Items 1–3 and 5–7 of §4 are by Kirshner, by Molho, or by the two together, and they work from the same registers of the fund. Agreement among them is not corroboration. Item 3 is a collection that may reprint items 1–2, and any chapter that does is the same text twice.
- **N2. Carboni 2022 is presumed dependent on N1 for Florence** until measured. On arrival, count its citations of Kirshner and Molho and read the contexts. It is independent only for Bologna.
- **N3. Coudy 1957 is `tontine_fr_royal`'s source** (its `key_source` and one cell), and it mentions this fund twice. **No cell of this form may be coded from Coudy.** If one were, any comparison between this row and `tontine_fr_royal` on that cell would rest on one author.
- **N4. Kohn 1999 and Kuehn 2008 are in `compagnia`'s `key_source`; Miner 2020 is cited by `casa_san_giorgio`, the three `voc` rows and `friendly_society_england`.** All three mention this fund and cite Kirshner and Molho. Coding from them would be N1 at one remove **and** would share a source with those rows. They may be used only to locate the primary literature.
- **N5. The census's own record is not a witness.** The 2026-09-10 logbook entry and the vault notes of `italian-archives-survey` were written from finding aids and general knowledge, with no source opened (that entry says so). Nothing in them may found a cell, and both are quarantined for any coding chat (§9).

### Co-occurrence

- **C1. Within `loss_mitigation_forms`: none, by assessment.** No row in that census is Florentine or Tuscan. `confraternity_fund_it` is "Latin Christendom / Italian, 11c–15c", which is not a polity. Assessed, and not declared.
- **C2. `compagnia@organizational_forms`, basis `same-polity`: proposed, and MS's call.** `compagnia` is "Tuscan (Florentine), 13–15c" and overlaps this form's opening decades. **There is no precedent for a cross-dataset `same-polity` declaration**: the census's three `same-polity` links are all within the loss census, among kō rows, and its cross-dataset links are `same-institution`. The reverse declaration would change `compagnia`'s row, which now reads `.NR`/`.NR`. Both make this a theory call under `run-a-coding-batch`. Recommendation: declare it, in both directions, in the batch that mints the type code, and only if MS agrees.
- **C3. If an organizational row is ever minted (§5),** it and the loss row are declared `same-institution` in both directions, on the `avariz_vakfi_kirkcesme` ↔ `avariz_vakfi` precedent.
- **C4. The *Monte comune* has no row,** so no declaration can be made to it. Any comparative statement involving the public debt the fund sat in is not available from this census, and part 2 must not imply that it is.
- **C5. The tontine rows: no co-occurrence** (different polity and period). There is also a possible relation of **descent** — a borrowing of design from Italian *monti* into the tontine. That is known here only from general knowledge, which is not evidence, and `cooccurrence_basis` cannot express it. It is recorded in prose as a hypothesis to assess from the acquired literature and from Coudy's two mentions, and **N3 applies to the second**. If it holds, any likeness between this row and the tontine rows is **parallelism by transmission**, not convergence, under the reserved terminology.

## 9. What the coding chat must eventually be kept from (for part 2's bundle)

The material each item withholds is named here; its content is not described.

- `--withhold-sessions italian-archives-survey,european-archives-survey,monte-delle-doti-scheme`. These are the only two vault slugs whose notes match `monte delle dot|dowry fund|Kirshner|Molho` (one note each; counts and slugs only, rung 3). Add the third so that this session's own standing row is removed. **`dowry` alone also matches one note each in `source-editions-survey` and `stoic-cooperation-loci`.** Part 2 must decide those two at rung 3–4, by asking whether the note is about this fund. Neither slug is withheld from here.
- **This file**, `records/NOTES-monte-delle-doti-scheme-2026-10-14.md`, and part 2's own brief: delete them from the built bundle, or use a minimal bundle (see the header).
- `--withhold-dates 2026-09-10`. This removes the logbook 2 entry that parked the candidate, together with every other section of that date in every logbook. Today's logbook entries (2026-10-14) are written to be shippable: they name the fund and cite this file, and state no comparator and no characteristic.
- Residual named mention that survives the scrub: logbook 4, the 2026-09-26 entry, lists this fund by name among the parked candidates. It names the fund and states no value. Hand review: acceptable.
- Outside the repository: the claude.ai Project's doc list and memory, and the Undermind workspace. **The coding chat is opened outside the Project**, on the 2026-09-28 precedent, and is never pointed at Undermind.

## 10. What part 2 does, in order

1. Confirm the acquisitions are in Zotero. Measure offsets and count the form's own terms (rungs 0–2). Recompute the holdings table.
2. Settle §5 (the organizational row) and §6 (period and split boundaries) at rungs 1–2, writing each question down before climbing.
3. Recompute §7 at the live row count, and re-check §8 against the sources actually held: N2's count, and the reprints in item 3.
4. Write the selection brief with its withheld section, the priors template, and the prompt. Read the prompt and both skills back against the withheld section, and delete every leak.
5. Write the bundle command, or a minimal bundle if the full copy cannot be made safe. File part 2's standing row.

## 11. This session's standing-table row (filed in logbook 4)

See logbook 4, slug `monte-delle-doti-scheme`.
