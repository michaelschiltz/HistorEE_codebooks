# Coding notes — comanda-primary-2026-10-27 (blind; Barcelona acts; 43 cells of `comanda` and `comanda_alloc`)

- Coder: `claude-opus-5-5`, effort recorded as `high` as the kickoff states. I cannot see a named effort level from inside the session and could not confirm `high` independently; this was disclosed in the priors and should be checked against the app setting before `coder_effort` is relied on.
- Priors: `PRIORS-comanda-primary-filled-2026-10-27.md`, sha256 `fac98fdcce8f37eeef7bf0e5f13e988cc6b7f6e338509cd92c5f16b961bdf75a`, finished 2026-10-27T08:47Z. MS reported the same hash after copying it into the live repository and reported a research-ledger anchor for commit `9b1a6a8da125cdc687f57517d6618111f6b53556`, `recorded_utc: 2026-10-27T08:52:48Z`. I took that commit to be the one adding the priors file on MS's word; I did not see the repository. Ledger entry: `entries/2026/20261027T085248Z-historee_codebooks-9b1a6a8da125.txt` (added by MS on 2026-10-27).
- Source opened after MS confirmed the hash at 08:56Z. Only file read in `sources/`: `madurell-garcia-sanz-1973_docs-1-255_acts.txt`.
- Exposure at start, as declared in the chat and the priors: a system-injected memory snapshot (profile, preferences, memory file names) with no comanda or commenda content, and one skill description naming "commenda" in a list. No memory file, Project, past chat, web page, Zotero item or other folder was opened. No skill was loaded.
- Method: every document read far enough to record act type, language, acts in entry and loss terms (`act-census-2026-10-27.csv`); every `mod3` document and every non-placement act read in full and coded (`instances-2026-10-27.csv`, `instance-chars-2026-10-27.csv`); directed searches as listed under (1). Quotations were taken from the OCR text with the subscription lines removed and line-end hyphens joined; every quotation in the recodings `notes` was checked by script as a substring of the cited document's text and against the printed page number in its heading. None has been checked against a page image.
- The edition is the editors' selection from the archives that kept the acts. Every count below describes the printed set, not Barcelona practice.

## (1) What was coded, and on what evidence

All 43 cells were coded, from the Latin acts of the edition only. Every value rests on `primary-transactional` passages in Latin (`source_lang` `la`); Catalan passages (docs 143, 186, 201, 220, 235, 248, 252, 255) appear only as minority or contextual evidence in notes.

**Census.** 255 documents; 230 are contracts placing capital or goods with a trading party, 25 are not (quittances, receipts, releases, a protest, a procuration, a royal licence, an agents' agreement, a collective instruction, a cession, two exchange or debt acknowledgments, deposits styled *comanda*, a carriage contract). Assignment by the loss rule for the investor's capital:

| loss terms of the act                                                                                                 | acts | row                     |
| --------------------------------------------------------------------------------------------------------------------- | ---- | ----------------------- |
| investor's risk stated (`ad tuum redegum et fortunam`, `ad vestri risicum, periculum et fortunam`, `vestri fortunam`) | 142  | `comanda`               |
| agent bears the capital wholly or in part (docs 3, 191, 220)                                                          | 3    | `comanda`               |
| loss shared (docs 201, 247)                                                                                           | 2    | `comanda_ad_societatem` |
| bearer abbreviated, cut or not named (`Et ad risicum etc.`)                                                           | 48   | neither                 |
| custom only (`ad quartum lucri et usum maris`, 1314-1331)                                                             | 9    | neither                 |
| no loss terms printed                                                                                                 | 22   | neither                 |
| illegible or contradictory (docs 62, 83, 95, 207)                                                                     | 4    | neither                 |
| not a placement of capital with a trading party                                                                       | 25   | neither                 |

Sensitivity, as promised in the priors: adding the nine custom-only acts to `comanda` gives 154; adding the 48 abbreviated acts as well gives 202. No coded value would change under either reading: the abbreviated and custom-only acts carry the same profit, security and commingling clauses as the assigned ones.

By period (contracts and non-placements together; years from each act's own dating clause, editors' heading dates having been removed):

| period    | docs | investor's risk stated | abbreviated or cut | custom only | no loss terms | other                                                      |
| --------- | ---- | ---------------------- | ------------------ | ----------- | ------------- | ---------------------------------------------------------- |
| 1236-1299 | 70   | 56                     | 2                  | 0           | 2             | 8 non-placements; 1 agent-bears; 1 illegible               |
| 1300-1349 | 36   | 11                     | 2                  | 9           | 5             | 7 non-placements; 2 illegible                              |
| 1350-1399 | 59   | 42                     | 11                 | 0           | 4             | 2 non-placements                                           |
| 1400-1449 | 64   | 21                     | 25                 | 0           | 9             | 5 non-placements; 2 agent-bears; 1 shared; 1 contradictory |
| 1450-1501 | 25   | 12                     | 8                  | 0           | 2             | 2 non-placements; 1 shared                                 |

**Sample.** 100 documents (85 `mod3`, 15 non-placement acts outside `mod3`), 103 instances (docs 129, 135 and 141 each give two acts with different loss terms). 45 instances are assigned to `comanda`, 1 to `comanda_ad_societatem` (doc 201), the rest to neither. The `comanda` cells rest on the 45.

**Directed searches** (all 255 documents, regular expressions on the OCR text):

- loss proof, for VF1/VF2: `prob(are|acio|atur)|testibus|sacrament|jurament|naufrag|amiss|perdut|perdidi|scriptura aut|fe del loch|certificar`. Found credence clauses believing the investor's plain word on his own recovery costs (docs 142, 154, 157, 158, 163), a credence clause in a deposit (doc 9) and in an agents' agreement (doc 70), an exemption of the investor from plea and oath in doc 3, and the only loss-proof clause in a carriage contract (doc 255). No comanda act says how a loss is established. Added instance: 142.
- surety or pledge, for RB3: `fideiuss|fermança|fianç|Velleyan|specialiter|ypothec|pignor`. Found the ship pledge in doc 93 (sample), sureties in docs 121 and 122, a wife's obligation in doc 154. Added: 122, 154.
- agent-bears clauses, for CF2/RB1/RB4: `salv\w+ (in terra|et secur)|sine (aliquo )?periculo|absque (aliquo )?(risico|periculo)|meo risico|risicum (meum|mei)|mon perill`. Found doc 3 (sample) and doc 191; docs 206, 209 and 210 use *salvis in terra* of the exchanges in which the return is to be invested, not of the comanda, which stays at the investor's risk (doc 210). Added: 191.
- cession, for CI3/CI4: `ced(o|imus)|cessio|recognicio|vendo|vendidi`. Found docs 213 and 217 (marginal notes of recognition and cession) and doc 253 (instrument of cession). Added: 217.
- segregation, for CI5: `separatim|separat|per se|a part|apart`. Nothing segregating found.
- creditors, for AP1: `creditor|prelaci|prioritat|primo solv|antequam alii`. Only doc 157, where the investors are called *creditores*. Nothing added.
- recall at will, for TS3/CI2: `quandocumque (vobis|tibi) placuerit|ad vestram voluntatem|qua hora velitis|plaurà|revoc`. Found open-trade comandas recallable at will (docs 15, 91, 107, 110, 113, 220). Added: 91, 107, 220.
- shared loss, for the boundary: `lucr\w* et (dampn|perd)|per maytat|risicum amborum|comuniter|pro rata ... (dampn|perd)|de lucro et perdita`. Found doc 201 (sample) and doc 247. Added: 247.
- also added as directed instances: 14 (two investors with stated shares, for CI1/CF3), 199 (investor's heirs, for TS1), 250 (insurance premium deducted from profit, for PR1/MC1).

No value rests only on directed instances. Directed instances are cited in notes as corroboration or as the minority against the value.

**Values coded** (full reasoning and quotations in each recodings row):

| cell           | value             | confidence | articulation    |
| -------------- | ----------------- | ---------- | --------------- |
| LP1            | .NR               |            |                 |
| LP2            | 0                 | medium     | analyst-imposed |
| LP3            | .NR               |            |                 |
| AP1, AP2, AP3  | .NR               |            |                 |
| AP4            | .NA               |            |                 |
| TS1            | 0                 | medium     | analyst-imposed |
| TS2            | single-venture    | high       | articulated     |
| TS3, TS4       | .NR               |            |                 |
| CI1            | none              | medium     | articulated     |
| CI2            | .NR               |            |                 |
| CI3            | 1                 | medium     | articulated     |
| CI4            | .NR               |            |                 |
| CI5            | commingled        | high       | articulated     |
| LR1            | .NR               |            |                 |
| LR2            | coupled           | medium     | articulated     |
| LR3            | 1                 | high       | articulated     |
| LR4            | 0                 | medium     | analyst-imposed |
| LR5            | .NA               |            |                 |
| LR6            | upside-only       | medium     | analyst-imposed |
| MG1            | contract          | high       | articulated     |
| MG2            | single-principal  | medium     | analyst-imposed |
| MG3            | .NA               |            |                 |
| MG4            | private-contract  | high       | articulated     |
| FP1            | commercial-profit | high       | articulated     |
| FP2, FP3       | .NR               |            |                 |
| FP4            | P                 | low        | analyst-imposed |
| CF1            | 1                 | high       | articulated     |
| CF2 (boundary) | 0                 | high       | articulated     |
| CF3            | bilateral         | high       | articulated     |
| MC1 (stated)   | allocation        | high       | articulated     |
| MB3            | voluntary         | high       | articulated     |
| RB1 (boundary) | capital-provider  | high       | articulated     |
| RB2 (boundary) | capital-provider  | medium     | analyst-imposed |
| RB3            | general-estate    | high       | articulated     |
| RB4 (boundary) | 1                 | high       | articulated     |
| PR1            | 0                 | medium     | articulated     |
| PY0            | .NA               |            |                 |
| VF1, VF2       | .NR               |            |                 |

The four boundary cells (CF2, RB1, RB2, RB4) and MC1 are not blind tests: the assignment rule and the type names fix them. CF2, RB1, RB4 and LR6 all rest on the same risk clause (see (5)).

## (2) What could not be coded, and why

Fourteen cells are `.NR` and four `.NA`.

- **LP1, LP3.** No act constitutes a body or shows the arrangement suing. The comanda is an obligation between named persons. That is silence on personhood, so `.NR`, not `0`. The 1412 protest (doc 186) is a personal claim in an act not assigned to this row.
- **AP1, AP2, AP3, LR1.** The acts address only the agent's duty to the investor: his goods obliged, co-agents bound in solidum. None addresses third parties who dealt with the venture, the ranking of creditors, or forced liquidation. By the AP3 and LR1 definitions, a source that addresses only the principal's claim gives `.NR`.
- **TS3, CI2.** The dominant voyage comanda is silent on recall and withdrawal. Where acts speak, they split by sub-type: open-trade comandas are recallable at will, comandas placed in an agent's comune are locked to the account. That is variation across instances, which may not be laundered into `P`, and the modal type gives no answer. See (4).
- **TS4.** No act lets a party alter the arrangement's purpose by internal decision. Destination and discretion clauses are mandate terms. The investors' collective variation of 1415 (doc 193) concerns comandas whose terms are not printed.
- **CI4.** Nothing states whether the interest is negotiable independent of the holder. The transfers recorded pass by named cession, intimated to the agent, in acts not assigned to this row. Not inferred to `0`.
- **FP2, FP3.** Licences attach to ships and patrons; investors include widows, clerics and Jews; no act states a franchise or an access arbitrage.
- **VF1, VF2.** No comanda act says how a claimed loss is established or what must be established. The credence clauses found concern the investor's recovery costs. VF2 follows VF1.
- **`.NA`.** AP4 (no founder); LR5 (LR4 is 0); MG3 (MG1 is contract); PY0 (no pool; see (4)).

## (3) Which of my priors were falsified

Quoted verbatim from the priors file; the cell rows are quoted by their expected value, confidence and evidence columns.

- **LP1.** Prior: "0" / "low" / "No act will name the comanda as a body; parties contract in their own names and the goods are described as the investor's (`res tuas`, `de bonis tuis`). The 0 rests on structure, not on a clause; if no clause bears on it at all I will code `.NR` rather than infer." Coded `.NR`: no clause bears on it, so the prior's own fallback applied. The phrases `res tuas` and `de bonis tuis` do not occur; the acts say `tua comanda`, `pars tua`, `partem tibi pertinentem`.
- **CI3.** Prior: "P" / "low" / "Payment clauses `tibi vel tuis aut cui volueris` and any cession of an investor's rights in a comanda among the non-contract acts." Coded `1`, medium: order clauses in assigned acts, and three recorded cessions of investors' rights (docs 213, 217, 253). The prior was too low.
- **CI5.** Prior: ".NR" / "low" / "Expect silence on whether the agent trades the goods apart from his own." Falsified: 23 of 45 sample instances commingle in terms (`simul cum mercibus meis`, `in comuni meo`, `per libram et solidum`), none segregates. Coded `commingled`, high.
- **Edition composition (§2.1).** Prior: "About 72 contracts placing capital or goods with a party who trades with them ...; 10 returns, releases or quittances ...". Falsified: 230 of 255 documents (90%) are such contracts; quittances, receipts, releases and acknowledgments are about 13 (5%).
- **Peril of sea and men (§2.3).** Prior: "About 50 of every 100 contracts, with the share rising through the fourteenth century as formulas lengthen." Falsified: about 30 of 230 contracts name the sea or men at all. The thirteenth-century clause allocates risk without naming any peril (`eat, maneat et redeat ad tuum redegum et fortunam`); *ad usum maris* first appears in 1293 (doc 58), *usum maris et gencium* in 1340 (doc 93), *periculum* in 1349 (docs 104, 105). My CF2 prior names the formula `ad risicum et fortunam tuam / Dei, maris et gentium`, which is not the form the early acts use.
- **Loss-sharing (§2.2).** Prior: "I expect loss-sharing acts to be concentrated before c. 1350." Falsified: the two loss-sharing acts are of 1419 (doc 201, Catalan chapters) and 1473 (doc 247). None is earlier. I also expected about 4 in the sample; there is 1.
- **Row counts (§5.1).** Prior: "about 60 are contracts placing capital with a trading party: about 40 assigned to `comanda`, about 4 to `comanda_ad_societatem`, and about 16 to neither (mostly *usus maris* only, plus a few deposits or loans)." Actual sample: 75 placement contracts, 44 documents assigned to `comanda`, 1 to `comanda_ad_societatem`, 30 to neither, and those 30 are mostly abbreviated notules (`Et ad risicum etc.`, `Hec tamen comanda etc.`), not *usus maris*: custom-only acts are 9 in the whole edition and 4 in the sample.
- **Least sure (§5.3).** Prior: "The share of acts that state a loss rule at all, and with it CF2, RB1 and RB4. If most acts give only *ad usum maris*, those three cells will rest on a minority of acts ...". Falsified in the safe direction: 147 of 230 contracts state the loss rule, and the three cells rest on 44 of 45 sample instances.
- **Confidence raised, value kept:** CF2, RB1, RB4, RB3, CF3 (medium to high); LR4, RB2 (low to medium). Values kept: all other cells. My priors' `.NR` count (about 15) and `.NA` count (three, PY0 a possible fourth) held: 14 and 4.

Leaks noted in the priors (§1.5) against my values, so that agreement can be discounted: my LR3 (`1`), AP1 (`.NR`), CI1 (`none`) and MG2 (`single-principal`) coincide with what the vocabulary implies; my LR4 (`0`, against an implied `.NR`), CF2 (`0`, against a possible `P`), VF1 (`.NR`, against an implied `claimant-oath`) and CI5 (coded, where the leak implied only that the question arose) do not.

## (4) Characteristics that did not fit the evidence

- **PY0.** An allocation contract has no pool and no payout. None of `collective-good`, `individual-indemnity` or `individual-draw` describes what happens on loss, which is that the investor bears it and the agent is discharged. The vocabulary gives PY0 no applicability rule, so `.NA` is my judgement, not a rule's consequence. Recommendation: give PY0 `applicability_on` MC1 (applicable only where MC1 is `pooling`), which would make every allocation form `.NA` by rule. This is test 2, ontological dependence.
- **TS3 and CI2.** The row aggregates at least three sub-types that answer differently: the voyage comanda (silent), the open-trade comanda (recallable at will) and the comanda placed in an agent's comune or societas (locked to the account). CF2's ruling forbids `P` for variation across instances, and the modal type is silent, so both are `.NR` while the edition plainly answers for two minority sub-types. The defect is in the type row's scoping, not the characteristic. Recommendation: no new characteristic; record the sub-types in the cell notes, or split the row if the census wants these answers.
- **CF2 on doc 191 (directed).** The agent bears the sea peril (*salve et secure in terra*), the investor the credit of the exchange takers. That is a split by category of loss, not a fraction or tranche, so neither `1` nor `P` as defined on 2026-10-11 fits the instance. It does not move the cell, but the characteristic cannot express it.
- **RB2.** The acts do not distinguish loss on sale from loss to the peril. Their risk clause is general ("risk and fortune"), and the early acts do not mention the sea at all. Coding RB2 separately from RB1 imposes the census's split on a source that does not draw it; hence analyst-imposed. The Catalan shop companyia (doc 220), which puts credit losses on the agent, is the only act that allocates a non-peril loss separately.
- **RB3.** Late notules read `Obligo me personaliter et bona`: the person (execution against the body) and the whole estate. I coded `general-estate`. Whether the personal obligation makes it `personal` or `mixed` under the 2026-08-09 value set is a vocabulary question I did not resolve.
- **FP4.** The comanda is legible as a notarial contract, registered and cancelled in the notary's protocol, not as an entity on a register kept by political authority. `P`/low is my reading; `.NR` is the alternative.
- **The word *comanda*.** In this edition it names at least five kinds of contract: the trading comanda; a deposit repayable on demand (docs 9, 17, 51); a ship loan with fixed repayment and a pledge of the cog (doc 93, assigned to `comanda` by its loss rule, the only fixed-claim instance against LR3); a carriage contract with risk on the carrier (doc 255); and shop companyias held *en pura comanda* (docs 143, 220, 252). Assignment by the loss rule alone puts doc 93 in `comanda` and leaves docs 9, 17 and 51 in neither only because they state no loss rule.

## (5) Dependence and well-formedness problems noticed and not repaired

- **One clause, four cells.** CF2, RB1, RB4 and LR6 (and RB2, analyst-imposed) all rest on the same risk clause. They are one datum here, not four or five. CF2 and LR6 are in `agent-loss-exposure`; RB1 and RB4 are in the other census with no dependence recorded. Any count of agreement across these cells should treat them as one.
- **CI2 and TS3 rest on the same clauses**, read from opposite sides: restitution on demand against no restitution before account. The vocabulary records CI2 in `capital-immobility` with AP2 and TS3 in no group. Not repaired: a dependence asserted on logical grounds is a hypothesis.
- **LP2 coded while LP1 and LP3 are `.NR`.** This is consistent with the legal-personhood group (`conditional`), but LP2 = 0 is not evidence for LP1 = 0, and I did not use it so.
- **Instances table.** Quote columns were extracted by script and checked only for the passages cited in the recodings. Some quote and parties fields run into witness or notary lines (e.g. doc 213), and some amount and destination fields are `.NR` where the extraction failed. The categorical columns are my readings. Not repaired.
- **Bundle text.** Several entries print more than one act without the `--- next act in the same entry ---` marker (docs 81, 97, 99, 101, 102, 124, 129, 135, 136, 139, 140, 146); I counted acts from my own reading. Doc 19's second act is empty in the file. Doc 114's risk clause is interleaved with the dating line. Doc 207's bearer reads *vestri dicti Petri*, which addresses the investor and names the agent. Doc 15's restitution clause is garbled by line order. All need the page image.
- **Model and effort.** `coder_effort = high` is as stated in the kickoff and not verified from inside the session.

## (6) What to acquire next, and which cell it would move

1. **The normative chapters on the comanda**: the *Costums de la mar* in the *Llibre del Consolat de Mar*, and the *Costums de Tortosa*. These are the most likely to move VF1 and VF2 (how a loss or the agent's account is proved: oath or otherwise), and possibly AP3 and LR1 (the agent's liability to those he dealt with) and TS3/CI2 (recall). They would be `primary-normative`, a second source class for this row.
2. **Litigation from the Consulate of the Sea of Barcelona** (sentences, inquests on comandas). These would move VF1/VF2 and LP3, and could move AP1 if an insolvent agent's creditors and investors were ranked.
3. **Page images of the cited documents**, above all docs 3, 18, 93, 108, 120, 191, 207 and 222, and the multi-act entries. These check the OCR of every quotation; a misreading in doc 3 or 191 would move the minority counts under CF2, RB1 and RB4.
4. **The editors' archival lines, stripped from this bundle.** These would tell whether the 48 abbreviated notules (`Et ad risicum etc.`) are register drafts whose extended instruments survive. That would move the census assignment, not the coded values.
5. **Vic and Mallorca registers of the 1230s-1300s**, where the type row places the form. These would test whether the loss-sharing comanda really is a fifteenth-century minority in Barcelona and absent earlier, which bears on the `comanda` / `comanda_ad_societatem` boundary. That boundary rests here on two acts.
