# NOTES — venetian-pass-2026-10-25 (coding record)

Blind re-coding of 14 cells (five of `societas_maris` in `organizational_forms`; three of `commenda_alloc` and six of `societas_maris` in `loss_mitigation_forms`) from the Latin of the 865 acts printed by Morozzo della Rocca & Lombardo (1940), and nothing else. Coder: `ai`, model `claude-opus-5-5`, effort `high` (as launched). Written 2026-10-25 inside `~/GitHub/_blind-venetian-pass-2026-10-25/proposed-of/`. Suffixed `-coding-` because the bundle's README names no other NOTES file; none was overwritten.

## 0. Ordering, priors, and what this record can show

- The priors file `PRIORS-venetian-pass-filled-2026-10-25.md` was written before any file in `sources/` was opened. Its sha256 is `2733d8a01768e66f583d3c25b4a72100f0b96315c903f85178fff156cfe91b72`; MS reported the committed copy has the same hash and that it was pushed. **The commit id was not stated**: the confirming message read "Committed as <commit id>", with the placeholder unfilled, and named no ledger entry. The commit id and the `research-ledger` entry (`entries/<year>/<file>.txt`) should be filled in here when this record is carried into `records/`. The hash was re-checked at the end of the pass and is unchanged.
- Every one of the 14 values was fixed from the acts before anything was computed about the matrix. No `data.csv`, logbook, codebook, view or earlier coding was available or sought, so no agreement, new-value or neighbour computation was possible or attempted. No unweighted similarity was computed.
- Tools used: the shell and Python 3 (scripts in the session scratchpad, not in the bundle), and `frictionless` for validation. Not used: `git`, Zotero, Undermind, Elicit, web search, any Google or Claude Docs connector, any memory file, the claude.ai Project. Skills loaded: `code-a-form` and `run-a-coding-batch`, at the kickoff's instruction, before the priors.

## 1. Reading record

1. Before the source: `README.md`, `PRIORS-TEMPLATE.md`, `cells-in-scope.csv`, `scope/types-in-scope.csv`, both act-table headers, all four files in `doctrine/`, both files in `vocab/`, both `schema/` packages (fields, constraints, descriptions), both `templates/`. Declared non-content operations: a directory listing, and `wc -c` on `sources/`.
2. The source file was split on its `=== act N | vol. | p. ===` headings into 865 acts; the numbering is complete (1-865, no gaps). Vol. II begins at act 467.
3. **Type census, every act.** A script found each act's earliest dispositive formula and the terms it uses. Every act's opening (dating clause and dispositive) was then read on screen, and all doubtful acts in full; 88 script readings were overridden by hand (listed in the census `notes` where the type is unusual). Acknowledgments were then typed by the terms the act itself uses, from their operative clauses: profit-share, peril, salvum in terra, prestitum, mutuum, nabulum and so on. Year and place were read by script from the dating clause **as stated**, OCR errors included; they are not converted and should be checked against the page image where they matter. Twenty acts state no year (acts 1-7 state month and indiction only; others have a lost or garbled dating clause), and 34 have no readable place; both are recorded as `.NR`.
4. **Sampled acts**: all 121 read in full on screen (operative clauses, recital, release clause), and every clause quoted in the instance tables extracted from the source text by script, so that each quotation is verbatim. Whitespace is normalised; line breaks and the editors' brackets are kept as printed. A final check confirmed that every one of the 1,436 quotations in the two instance tables, and every «...» quotation in the recodings notes, occurs in the source.
5. **Further acts read outside the sample**, not entering any frequency, and why:
   - nos. 13, 106, 123, 234, 239, 270, 389, 426, 450, 451, 491, 862: the unsampled bilateral acknowledgments of stratum A, read because the sample drew only four bilateral contracts and the `societas_maris` loss cells (LR6, PR1, MB3, RB4) would otherwise rest on four acts alone;
   - nos. 556, 844 and 539, 702: read to settle their type (judgment, attestation, and two releases with lost openings);
   - nos. 380 and 418 were both drawn, and found to concern one contract.

## 2. Type census (`type-census-venetian-pass-2026-10-25.csv`)

The edition is one corpus and a selection: its editors chose these acts from the archives that kept them (largely ecclesiastical and family deposits). All counts describe the printed set, not Venetian practice.

| act type             | dispositive formula                                       | acts | share |
| -------------------- | --------------------------------------------------------- | ---- | ----- |
| securitas            | Plenam et irrevocabilem securitatem facio/mitto           | 383  | 44.3% |
| manifestatio         | Manifestus sum / Manifestum facio ... quia recepi; Accepi | 274  | 31.7% |
| testificatio         | Testificor / Testificamur                                 | 74   | 8.6%  |
| commissio            | Committens committo                                       | 57   | 6.6%  |
| other                | various (see notes)                                       | 20   | 2.3%  |
| breve recordacionis  | Breve recordacionis facimus                               | 17   | 2.0%  |
| promissio            | Promittens promitto                                       | 15   | 1.7%  |
| testamentum          | testamentary disposition                                  | 12   | 1.4%  |
| sentencia / iudicium | judges or doge sitting                                    | 10   | 1.2%  |
| vendicio             | vendo / vendidi                                           | 3    | 0.3%  |
| total                |                                                           | 865  | 100%  |

Within acknowledgments (*manifestatio*, 274), by the terms the act itself uses:

| acknowledgment kind (terms the act uses)                          | acts |
| ----------------------------------------------------------------- | ---- |
| capital to trade for a share of profit                            | 170  |
| loan (prestitum, fixed return, safe on land)                      | 50   |
| sea loan / sea exchange (fixed sum, at the lender's peril at sea) | 33   |
| declaration of debt/obligation                                    | 6    |
| loan (mutuum, mainland form)                                      | 4    |
| anchor hire (ad nabulum)                                          | 3    |
| remittance at the giver's peril (sine prode)                      | 2    |
| grant/donation (manifestum facio ... do)                          | 2    |
| other acknowledgment                                              | 1    |
| deposit (sine ullo prode)                                         | 1    |
| agency (to invest for the giver, no profit share)                 | 1    |
| guardianship (tutela)                                             | 1    |

The 170 profit-share acknowledgments name the contract *collegantia* (or a spelling of it) in 16 cases: 13 of the 20 dated before 1200, and 3 of the 150 dated 1200 or later. Three call it *compagnia* instead (nos. 270, 533, 862). The 13th-century formula, «capitaneam cum tribus partibus de toto prode», names no contract at all. Releases (383) were sorted by their object: 83 discharge a contract placing capital with a trader (stratum R, below); the rest discharge loans and *cautiones*, pledges, estates, promises, or everything at once (*de omnibus*). Release objects outside stratum R were read by script from the release's opening words and are approximate. In the 13th century *caucionis cartula* also names colleganza deeds (e.g. no. 498), so some releases labelled "caucio/loan" may discharge colleganze whose recital is too short to show it.

## 3. Strata and the draw

**Strata**, as the census defines them:

- **A — acknowledgments that place capital with a party who trades with it, for a share of the profit** (N = 170). The receiver acknowledges capital and undertakes to trade with it and return the capital with a stated share of the profit (*capitanea salva, prode vero quod inde Dominus dederit ...*; *capitaneam cum tribus partibus de toto prode*; *cum medietate*; *cum illa parte de prode ...*). Named *collegantia*, *compagnia*, or nothing. It includes two guardians' acknowledgments that trade a ward's goods for a quarter of the profit (nos. 768, 784).
- **B — acknowledgments of capital to be invested for the giver's account, with no profit share** (agency; N = 1: no. 611, Messina 1224). The edition prints no acknowledgment *in rogadia* or *in commendacione*; those words occur only inside releases and general quittances.
- **R — releases of such contracts** (N = 83). A release qualifies where its recital shows a contract of kind A or B: colleganza markers (the contributions *iactavi/iactasti/posuisti/misisti*, *in collegancia*, a *memorialis cartula* carried on a voyage, a profit-share clause), or the trading formulas that in this edition occur only in profit-share acknowledgments (*portando, mandando ...*: 88 of 88 acknowledgments carrying it are profit-share; *negociandum et procertandum* 13 of 14; *laborare et procertare* 7 of 7). Plus three by hand: nos. 255, 581 and 787 (*compagnia* in which one party received the other's capital to trade), and no. 704 (*rogadia* with power to trade).
- Excluded from R and recorded in the census: general quittances listing *colleganciis, rogadiis, prestitis* in a general clause (23); releases of deposits *in commendacione* (10); releases of promises to return a deed (nos. 17, 421); releases of a *memorialis cartula* whose return terms are lost or not recited (nos. 99, 124, 150); joint *compagnie* of partners who travelled together (9); and releases reciting only *ad negociandum*, which in this edition also occurs in sea loans (nos. 128, 183, 321, 518).
- Counted but not sampled, as instructed: loans, sea loans and all other types.

**The draw.** Each stratum over 60 got a systematic random sample of 60 over act order: `random.seed(20261025)`; k = N/60; start u = `random.uniform(0, k)`; index_i = floor(u + i·k), i = 0..59. A was drawn first, then R, on one random stream.

- A: k = 2.833333, u = 1.201773. Acts: 71, 191, 235, 334, 377, 391, 444, 467, 469, 475, 479, 489, 496, 512, 523, 533, 573, 588, 602, 605, 618, 622, 654, 662, 668, 675, 677, 680, 683, 686, 689, 695, 701, 709, 715, 718, 721, 726, 741, 749, 752, 761, 764, 769, 772, 782, 786, 792, 801, 806, 808, 811, 814, 821, 828, 834, 839, 842, 849, 859.
- R: k = 1.383333, u = 1.079577. Acts: 18, 19, 31, 42, 45, 56, 59, 112, 118, 122, 136, 141, 142, 207, 209, 238, 337, 355, 380, 400, 401, 405, 409, 410, 414, 418, 424, 437, 459, 476, 498, 505, 507, 508, 538, 539, 555, 562, 564, 581, 632, 634, 647, 648, 650, 655, 665, 667, 692, 704, 739, 740, 757, 773, 787, 816, 817, 818, 855, 864.
- B: taken whole: 611.

**Frame defects, reported.** No. 207 was drawn into R although it releases a promise to deliver a *memorialis cartula*, not the colleganza; my own rule should have excluded it as it excluded nos. 17 and 421. It was kept in the sample and coded to no cell. Nos. 538 and 71 are one contract (the 1138 colleganza and its release in 1212), and nos. 380 and 418 are one contract (two releases for successive indemnities). Each pair is counted once in every frequency.

## 4. Instance coding

Files: `instances-venetian-pass-2026-10-25.csv` (121 rows) and `instance-chars-venetian-pass-2026-10-25.csv` (767 rows). Instance ids are `VP26-<stratum>-<act no.>`.

**Form assignment** (`form_assigned`), decided on the act's terms and never on its name:

- `societas_maris` where the traveller contributes capital beside the investor's (the contribution clause);
- `commenda_alloc` where one side supplies all the capital, the other trades it for a share of profit, and the act allocates the peril (profit and peril clauses);
- `neither` for agency, *rogadia*, land shop partnerships, releases of promises, and the 13th-century release recitals that state only the investor's sum and the trading formula, which do not say whether the traveller contributed;
- no act fitted both.

Two `commenda_alloc` contracts are land trade with the peril of thieves and fire (nos. 782, 821). The type is not restricted to sea ventures, so they stay. A bilateral land shop partnership (no. 855, recited) was not assigned to `societas_maris`, whose name restricts it to the sea.

**States** recorded per act are only those of the characteristics in scope that the act speaks to; the rule for each is in its row's `notes`. Release recitals speak to CF1, CF3 and CI1 when they state both contributions, to CF3 always, and to TS2 when they recite the voyage or term. They speak to RB1, RB4 and MC1 only where a loss event is recited: nos. 380 and 418 (the seizure of 1171), and 787 (seizure by Pisans).

## 5. Form-level summary (frozen)

n counts distinct contracts. "parties" counts distinct persons named as principals; OCR spellings were unified by hand where obvious, so the count is approximate. A frequency was never turned into `P`, and a state held by at least 10% of acts is named as a variant in the row note.

| recoding_id | census | type_id          | char_id | modal            | share | n  | parties | distribution                    | variants   | value            | confidence | articulation    |
| ----------- | ------ | ---------------- | ------- | ---------------- | ----- | -- | ------- | ------------------------------- | ---------- | ---------------- | ---------- | --------------- |
| OF-R0253    | orga   | `societas_maris` | `CF1`   | P                | 100%  | 30 | 53      | P 30                            | —          | P                | medium     | articulated     |
| OF-R0254    | orga   | `societas_maris` | `CF3`   | bilateral        | 97%   | 31 | 55      | bilateral 30, multilateral 1    | —          | bilateral        | high       | articulated     |
| OF-R0255    | orga   | `societas_maris` | `CI1`   | common           | 100%  | 30 | 53      | common 30                       | —          | common           | medium     | articulated     |
| OF-R0256    | orga   | `societas_maris` | `LR6`   | symmetric        | 100%  | 4  | 7       | symmetric 4                     | —          | symmetric        | medium     | analyst-imposed |
| OF-R0257    | orga   | `societas_maris` | `TS2`   | single-venture   | 88%   | 26 | 45      | single-venture 23, fixed-term 3 | fixed-term | single-venture   | medium     | articulated     |
| LM-R0080    | loss   | `commenda_alloc` | `MC1`   | allocation       | 100%  | 56 | 90      | allocation 56                   | —          | allocation       | high       | articulated     |
| LM-R0081    | loss   | `commenda_alloc` | `PR1`   | 0                | 100%  | 56 | 90      | 0 56                            | —          | 0                | medium     | analyst-imposed |
| LM-R0082    | loss   | `commenda_alloc` | `RB1`   | capital-provider | 100%  | 56 | 90      | capital-provider 56             | —          | capital-provider | high       | articulated     |
| LM-R0083    | loss   | `societas_maris` | `MB3`   | voluntary        | 100%  | 4  | 7       | voluntary 4                     | —          | voluntary        | low        | analyst-imposed |
| LM-R0084    | loss   | `societas_maris` | `MC1`   | allocation       | 100%  | 6  | 11      | allocation 6                    | —          | allocation       | medium     | analyst-imposed |
| LM-R0085    | loss   | `societas_maris` | `PR1`   | 0                | 100%  | 4  | 7       | 0 4                             | —          | 0                | medium     | analyst-imposed |
| LM-R0086    | loss   | `societas_maris` | `RB1`   | shared           | 100%  | 6  | 11      | shared 6                        | —          | shared           | high       | articulated     |
| LM-R0087    | loss   | `societas_maris` | `RB2`   | .NR              | —     | 0  | 0       | —                               | —          | .NR              | .NR        | .NR             |
| LM-R0088    | loss   | `societas_maris` | `RB4`   | 1                | 80%   | 5  | 9       | 1 4, 0 1                        | 0          | 1                | medium     | articulated     |

For `commenda_alloc` (56 contracts): 40 distinct travellers and about 51 distinct investors. Dominicus Gradonicus is the traveller in 8 sampled contracts (1205–1223), and Redolfus de Suligo in 5. His are all of August 1234: he took at least 15 colleganze that month, nos. 676–690, so a systematic draw over act order was bound to take several. For `societas_maris`: 30 contracts between 28 distinct pairs (nos. 18 and 19 are one pair; so are nos. 334 and 377).

## 6. Decision points, each with its alternative reading

1. **Strata by structure, not by name.** Profit-share acknowledgments form one stratum whether or not the act says *collegantia*. Alternative: separate strata by the act's name, which would have taken the 16 acts naming *collegantia* whole. That would have given `societas_maris` more contracts, but it would have stratified on a word that disappears c.1200. Rejected; reported.
2. **Release recitals count** for the cells they recite (CF1, CF3, CI1, TS2, and loss events). Alternative: contracts only, which would leave `societas_maris` CF1, CF3, CI1 and TS2 resting on 4 acts. Recitals were preferred because they are the same deeds' terms, restated by the party who held them.
3. **CF1 = P is partly circular**: the form is assigned on the same clause. Alternative: none that avoids it inside these two forms; reported in the cell.
4. **CI1 = common** over several-accounts for ship-share recitals (*sortes*) and for the 1211 compagnia profit rule (*pro quantitate tue suprascripte pecunie*).
5. **LR6 = symmetric** for a traveller who takes half the profit on a third of the capital and loses his own third; alternative: no state fits a disproportionate two-sided exposure (see answer 4). For the unilateral acts the instance state is `upside-only`, recorded but not in scope.
6. **TS2**: a convoy-bounded season (*a modo usque per totam muduam ...*) is read as `single-venture`; *muda ... et inde ad unum annum* and terms in years are read as `fixed-term`. Alternative: every convoy-bounded term read as fixed-term, which would make `fixed-term` the mode in the 13th century but changes nothing in the `societas_maris` cell, whose contracts are 12th century.
7. **PR1 = 0** (both forms) is read as an observed absence of a price in acts that state their full terms; alternative `.NR`.
8. **MB3 = voluntary**, low and analyst-imposed; alternative `.NR` (no clause asks). I recommend `.NR` if analyst-imposed values from contract form are not wanted.
9. **MC1 (`societas_maris`) = allocation** over pooling for two-party pro-rata loss sharing.
10. **RB2 = `.NR`** over a reading of *capitanea salva* as putting market loss on the traveller, or of the remainder clause as covering market loss.
11. **RB4**: no. 380's reservation (*in me remanel cum omni suo vigore et robore*) read as an obligation not extinguished (0, low confidence); alternative: it reserves only the claim to later indemnities.
12. **No. 787** (Pisan seizure) assigned to `societas_maris` at low confidence: the act shows both parties held shares and one carried the goods, but states no contributions. Alternative: `neither`, which would remove one MC1 and one RB1 datum from `societas_maris`.

## 7. Leaks

Disclosed in the priors (§1.4–1.5) and not used. One bears on a finding and must be read with it:

- **Period field of `societas_maris`** ("c.1073-early 13c (Venice)"). The acts independently show what this field states: the bilateral shape holds in the 12th-century deeds and almost vanishes after 1200 (section 8.1). My priors expected the shift earlier ("from the mid-12th c."), so the finding is not my expectation. But it is not independent of the field either, which I had read. **Treat the dating finding as non-blind.**
- **`commenda_alloc` type name**: states `MC1 = allocation`. The row is coded but scored apart.
- **Loss census description** (`schema/`): the withheld word sits in the list of *allocation* forms, and the `_alloc` rule repeats the implication for `commenda_alloc`. Bears on both MC1 cells.
- **`CHARACTER-CODING.md` test 1, and the `LR6` definition** (agent with a call; qirad): imply some commenda-like row is `LR6 = upside-only`. LR6 is in scope only for `societas_maris`, which came out `symmetric`; the unilateral instances read `upside-only`, consistent with the implication, but that is not in scope.
- **`CHARACTER-CODING.md` test 4** ("for bilateral capital-labour contracts ... the agent is a debtor"): the acts make the bilateral traveller a debtor for the investor's capital *except* for loss to the peril, which they discharge expressly (RB4 = 1). They neither confirm nor refute the doctrine's sentence as written.
- **`CI1` definition** ("a single investor's capital entrusted to a single agent is 'none'"): used as the vocabulary's own rule for the unilateral instance states, which are not in scope.
- **Kickoff prompt**: it lists *collegantia/colligancia, commendacio, rogadia, prestitum, mutuum*. It named no values. The acts contain no acknowledgment *in rogadia* or *in commendacione*, so the list over-predicted.

## 8. Findings beyond the cells (description only; no comparative claim)

1. **Change c.1200.** Before 1200, the colleganze the edition prints are mostly bilateral: 26 of the 28 distinct contracts whose release recitals state both contributions, and 3 of the 7 sampled acknowledgments; profit is divided by halves and the express clause discharges both parties on total loss. From 1200, the printed acknowledgments are unilateral: 52 of the 53 sampled, 48 of them three-quarters to the investor, with the investor bearing the peril *in tuo periculo maris et gentis clarefacto* and no name for the contract. This is a row whose values change over its own claimed period, so by the doctrine it should be **split, not averaged**. See answer 5, and the leak in section 7.
2. **Fixed-return finance dominates the printed 12th century.** Among acknowledgments dated before 1200 there are 31 land loans and 25 sea loans against 20 profit-share contracts; after 1200, 23 loans and 8 sea loans against 150 profit-share contracts.
3. **The peril clause is near universal** in the profit-share contracts (160 of 170; all 60 sampled), and always requires proof (*clarefactum*).
4. **Land and overland colleganze** exist: Venice and Rivoalto shops (nos. 782, 821, 846; peril of thieves and fire), Lombardy, France and Germany (no. 668, *aque et gentis*), Hungary (no. 715), Istria and Friuli (no. 808).
5. **One traveller, many investors**: Redolfus de Suligo took at least 15 colleganze in August 1234 (nos. 676–690; the fragment no. 804 lists his deeds). This is invisible to CI1 per arrangement (answer 4).
6. **Public indemnity**: in the 1171 seizure case (nos. 380, 418), the commune registered the seized goods (*catastico nostri communis*) and its examiners distributed imperial indemnities pro rata. That is a distinct public arrangement, outside these forms.

## 9. The six answers

**1. What was coded and on what evidence.** All 14 cells, from the census of all 865 acts and a coded sample of 121 (60 profit-share acknowledgments, 60 releases of such contracts, 1 agency act); `source_read = partial`. The values:

- `societas_maris` (organizational): CF1 `P`, CF3 `bilateral`, CI1 `common`, LR6 `symmetric`, TS2 `single-venture`.
- `commenda_alloc`: MC1 `allocation` (not blind), PR1 `0`, RB1 `capital-provider`.
- `societas_maris` (loss): MB3 `voluntary` (low), MC1 `allocation`, PR1 `0`, RB1 `shared`, RB2 `.NR`, RB4 `1`.

The evidence behind them:

- `societas_maris` CF1, CF3, CI1 and TS2 rest on 30 or 31 contracts (4 acknowledgments, 26 or 27 release recitals). LR6, PR1 and MB3 rest on 4 contracts; RB1 and MC1 on 6, adding two recited loss events; RB4 on 5. The twelve further bilateral acknowledgments listed in section 1 all agree, but are outside the frequencies.
- `commenda_alloc` rests on 56 sampled acknowledgments.

The evidence clauses are quoted in each row.

**2. What could not be coded, and why.**

- `societas_maris RB2` is `.NR`: no act distinguishes loss from price or failed sale from loss to the peril. *Capitanea salva* orders capital before profit and does not say who bears a shortfall.
- `MB3` is coded only weakly: no act addresses choice or compulsion.
- `LR6`'s existence could not be checked: it depends on `LR2`, which is not in the bundle.
- The `open` state of TS2 occurs in the edition (no. 13, 1073) but not in the sample.

**3. Which of my expectations were falsified** (quoted verbatim from `PRIORS-venetian-pass-filled-2026-10-25.md`):

- "releases or quittances **30**" (per 100 acts): 44.3% (383). "loans and sea loans **18** (of which sea loans ~6)": 10.1% (87; sea loans 3.8%). "attestations **5**": 8.6%. "anything else **17**": 10.9%. Near the mark: "contracts placing capital in a trader's hands (colleganza acknowledgments) **22**", actually 19.7%, and "mandates (*procurae*) **8**", actually 6.6%.
- "the unilateral (three-quarters/one-quarter) to dominate from the mid-12th c.": falsified. In the printed acts the bilateral shape holds through the 12th century and the three-quarter unilateral form dominates only from 1200 (section 8.1).
- "(d) sea loans and fixed-return loans to grow relative to colleganze in the 13th c.": falsified in the opposite direction (section 8.2).
- "colleganza contracts, as the condition of the traveller's discharge (I expect 50–70%)": falsified upward, 94% (160 of 170). "most sea loans (≥ 80%)": 76% (25 of 33), slightly below. Confirmed: "releases rarely (≤ 10%)" (2.3%) and "Overall perhaps 20–25% of all acts" (23.6%).
- "I expect among the 60 contracts ~15 (range 8–25) to be evidence for `societas_maris`": falsified, 4.
- "among the 60 releases, perhaps 15 that recite enough to speak to any cell, most of them only to `TS2` or `RB4`": falsified. 59 of 60 speak to at least one cell, 29 state both contributions, and only one speaks to RB4.
- "Repeated parties (Mairano above all)": partly falsified. Mairano recurs in the 12th-century recitals, but the most repeated principals in the sample are Dominicus Gradonicus (8) and Redolfus de Suligo (5).
- "In the whole edition I expect ~190 colleganza-type contracts and ~260 releases": 170 and 383.
- §4, `societas_maris RB2`: expected "shared | low", with ".NR (my main alternative)". The alternative came true: `.NR`.
- §4, `societas_maris MB3`: expected "voluntary | medium", with the falsifier "otherwise silence on choice might force .NR". The acts are silent on choice; I kept `voluntary`, lowered to low, and recommend `.NR` as the alternative.
- §4, `TS2`: the falsifier "acts stating a term in years or months ... in ≥ 10% (variant)" was met (fixed-term 12%); the mode held.
- "I expect *collegantia* to name both shapes": confirmed for the 12th century (no. 71 is unilateral and named), but the term nearly vanishes after 1200 (3 of 150), which I did not expect.

Not falsified: CF1 `P`, CF3 `bilateral`, CI1 `common`, LR6 `symmetric` (my "least sure" cell, held on n = 4), MC1 `allocation` (both forms), PR1 `0` (both), RB1 `capital-provider` and `shared`, RB4 `1` (with a `0` variant).

**4. Characteristics that did not fit the evidence.**

- RB2's split of market loss from peril loss has no counterpart clause in any act.
- TS2's value set has no state for a season bounded by the convoy calendar; the rule used is stated in the row.
- LR6 `symmetric` hides a disproportionate exposure: half the gain against a third of the capital at risk.
- CI1 is located on the arrangement, so a traveller who merges many investors' capitals in one venture (section 8.5) reads `none` contract by contract. That question belongs to `CI5`, which is not in the bundle.
- MB3 was built for pooling. For a two-party contract it is near definitional, which is why no act states it.
- CF3's `bilateral` collides with the type name's "bilateral".

**5. Dependence or well-formedness problems noticed and not repaired.**

- (a) `LR6` depends on `LR2` (`applicability_on`), which this bundle does not carry; applicability is unchecked.
- (b) The assignment of acts to `societas_maris` and the value `CF1 = P` rest on the same clause.
- (c) For `societas_maris`, RB1, RB4, MC1 and LR6 are all read from one clause: «nichil inde pars parti inquirere debeat, Si vero aliquid inde remanserit sicut iactavimus ita participemus» (no. 334 (I, 330)). They are not independent witnesses to each other; this matches the `agent-loss-exposure` grouping only in part, since RB1, RB4 and MC1 are not in that group.
- (d) **Phase split.** The `societas_maris` row's own period runs across the change c.1200 shown in section 8.1, and the `commenda_alloc` row's "10-13c" spans both shapes. Recommend that MS consider a phase split, not averaging (the split test of `code-a-form`). The split would give the 13th-century acts to `commenda_alloc` and leave `societas_maris` effectively 12th-century in Venice.
- (e) CF3 label collision (answer 4).
- (f) Frame defect in stratum R (no. 207, section 3).

No vocabulary or schema file was edited.

**6. What to acquire next, and which cell it would move.** These suggestions come from general knowledge and are unverified; none was used as evidence.

- Morozzo della Rocca & Lombardo, *Nuovi documenti del commercio veneto dei sec. XI–XIII* (1953). More 12th-century bilateral acknowledgments would raise n for `societas_maris` LR6, PR1, MB3 and RB4 (now 4–5 contracts each), and could put the `open` state of TS2 into a frequency.
- The BEIC page images for the OCR-flagged clauses (nos. 19, 141, 238, 377, 801 and the bracketed restorations in 769), to check the quoted text.
- A Venetian normative text on the colleganza: a statute, or the rules the doge's licences cite. It would move `RB2` (market loss) and `MB3` (whether participation was free) off `.NR`, or off an analyst-imposed value.
- For `CI5` (not in scope): a traveller's account book or the full deed series of Redolfus de Suligo (1234), to see whether many investors' capitals were kept apart.

## 10. Checks run

- Validation: the `recodings` resource of each `schema/` package was copied to a scratch directory outside `proposed-of/`, with its foreign key to `data.csv` removed and its path pointed at a copy of the CSV. `python3 -m frictionless validate organizational_forms.datapackage.json` printed `VALID` for `organizational_forms_recodings`, and the same for `loss_mitigation_forms` (frictionless 5.19.0).
- A hand sweep confirmed:
  - each value is in its characteristic's `allowed_values` in `vocab/`;
  - the `.NR` row carries `.NR` confidence and articulation;
  - the fixed fields are as instructed and the ids match `cells-in-scope.csv`;
  - the headers equal the templates, and the files use LF line ends.
- Quotation check: every quotation in the instance tables and recodings notes occurs in the source (1,436 instance-table quotations; 0 failures).
- Priors hash re-checked unchanged.
