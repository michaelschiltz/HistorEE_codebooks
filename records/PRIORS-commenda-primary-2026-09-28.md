# Priors — commenda-primary-2026-09-28 (arm P, primary acts only)

- Filled by (model identifier as configured; effort as stated in the kickoff): `claude-opus-5-5`, effort `high`.
- Finished at (UTC): 2026-09-28T06:05Z (approximate; the sha256 printed after writing is the binding identifier, not this timestamp).
- Files read before writing this, listed: `README.md`; `doctrine/CLAUDE.md`; `doctrine/CONTRIBUTING.md`; `doctrine/CHARACTER-CODING.md`; `doctrine/EDITING-CSV.md`; `vocab/organizational_form_characteristic.csv` (all 32 rows, every column); `vocab/loss_mitigation_characteristic.csv` (all 26 rows, every column); `scope/types-in-scope.csv`; `cells-in-scope.csv`; `instances-header.csv`; `instance-chars-header.csv`; `templates/recodings-header-organizational_forms.csv`; `templates/recodings-header-loss_mitigation_forms.csv`; `schema/organizational_forms.datapackage.json` and `schema/loss_mitigation_forms.datapackage.json` (package metadata, resource descriptions, all field definitions of both `recodings` resources and of the `organizational_forms` data resource); this template. Skills loaded: `code-a-form`, `run-a-coding-batch`. **No file in `sources/` has been opened.** A directory listing of `sources/` (three filenames and sizes) was taken to confirm the bundle's layout; nothing else of it was read.

## Exposure, disclosed before any source is opened

**General knowledge (training).** I know the standard historiography of the commenda and the *societas maris* as it is compressed in textbooks and survey chapters: Weber's dissertation on the medieval trading companies; Lopez & Raymond's *Medieval Trade in the Mediterranean World* (which translates Genoese acts from Scriba and Cassinese among others); de Roover's chapter in the *Cambridge Economic History* III; Byrne and Krueger on Genoese notarial practice; Pryor's articles on the origins of the commenda and on the Marseille commenda (he worked on Amalric); Udovitch on the Islamic *qirāḍ* / *muḍāraba*; Greif, Williamson and the principal–agent literature; Harris's *Going the Distance* (2020) on the commenda as a migrating institution; Hansmann, Kraakman & Squire (2006) on entity shielding, where the commenda appears as a precursor. I also have a general recollection that Genoese acts use formulae such as *confiteor me accepisse a te … in accomendatione*, *portare laboratum*, *et inde quo voluero*, *quartum proficui*, *in potestate tua mittere*, and that Marseille acts of the mid-thirteenth century use *comanda*, *ad fortunam Dei, maris et gentium* and *ad usum maris*. I cannot recall specific act numbers or pages, and I do not know which acts the kickoff's example `source_ref` (Scriba CCCXII, CDXXXV; Cassinese 490; Amalric 91) refers to. None of this may found a cell.

**Known leaks listed by the README.**

1. The loss-census form code `commenda_alloc`, "Commenda (loss-allocation aspect)". It states `MC1=allocation` for that row. I treat `commenda_alloc MC1` as not blind.
2. The type name of `societas_maris`: "the bilateral commenda; Venetian collegantia". It asserts that the *societas maris* is a kind of commenda and equates it with the Venetian *collegantia*. **It also collides with `CF3`'s value `bilateral`**: in the historiography "bilateral commenda" means that both parties contribute capital, not that there are two principals. I will not read the type name as evidence for `CF3`, and I flag the collision now.
3. General knowledge, above.
4. The `code-a-form` skill names "commenda" in its description as an example. It states no value.

**Further leaks found in reading the bundle and the skills (not listed by the README).** None may be used; all are reported with their location.

5. `doctrine/CHARACTER-CODING.md`, test 1 worked case: "`LR2 outcome coupling` returned `coupled` for three forms alike [withheld 2026-09-28: names a form under re-coding]. It was bundling *is the decision-maker bound to outcomes?* with *in which direction?* — so an agent holding a call option bounded below at zero and a manager holding a debt read identically." The redaction marker sits exactly where a form under test is named, so the passage implies that at least one of `commenda` / `societas_maris` carries (or carried) live `LR2=coupled`, and that one of the three is "an agent holding a call option bounded below at zero" — i.e. implies a live `LR6=upside-only` somewhere among the forms under test.
6. `vocab/organizational_form_characteristic.csv`, `AP3` definition: "For a bilateral capital-labour contract it has two [answers], and they move in opposite directions: [withheld …]" and "several named rows [withheld …] reasoned about the principal's capital rather than about venture creditors, which is why the agent-loss-exposure group looked collinear"; and, in both `AP3` and `LR1`, "The conflation this repair undoes is only possible where the principal's claim is residual - [withheld …]". Together these imply that a form under test was once coded on `AP3` from the principal's claim, that its principal is a residual claimant, and that the investor's and the agent's shielding "move in opposite directions" for it.
7. `vocab/organizational_form_characteristic.csv`, `LR6` definition: "Without it a qirad agent holding a call and an isqa manager holding a debt both read as merely 'coupled'." Not a form under test, but general knowledge makes the *qirāḍ* the commenda's closest analogue, so this sentence plus training predicts `LR6=upside-only` for the commenda by analogy.
8. `doctrine/CHARACTER-CODING.md`, test 4: "`AP3`, `LR1`, `CF2` and `LR6` were grouped as `agent-loss-exposure` on the argument that for bilateral capital-labour contracts they all record one fact — the agent is a debtor." States the census's earlier reasoning about the class to which both forms under test belong.
9. `vocab/loss_mitigation_characteristic.csv`, `LS3` definition: "LS3 is NOT coded for several named rows [withheld …]" — implies the `_alloc` rows under test carry no `LS3` (consistent with `cells-in-scope.csv`).
10. `schema/loss_mitigation_forms.datapackage.json`, package description: "allocation (risk assigned to a named party by contract - sea loan, bottomry, respondentia, [withheld 2026-09-28: names a form under re-coding])". The redaction sits inside the *allocation* list, so it implies `MC1=allocation` for at least one of the two loss rows, possibly both. **I therefore treat `MC1` as not blind for `societas_maris` as well as for `commenda_alloc`**, which extends README leak 1. The same description says "forms suffixed _alloc are cross-references to organizational_forms entries, coded here only on loss-allocation characteristics".
11. `cells-in-scope.csv` reveals which characteristics the live census carries for each row: e.g. `societas_maris` has no `VF2` row in the loss census while `commenda_alloc` has one; `commenda` rows jump from `OF-0087` to `OF-0090` (two live rows, `OF-0088`/`OF-0089`, are out of scope); `LR5` exists for both organizational rows. The existence of a row states no value, but the missing `VF2` might reflect a live `VF1` state; I will not reason from it.
12. `instances-header.csv` names the clauses the operator expects to parse: `capital_stans`, `capital_tractator`, `destination`, `duration_clause`, `profit_rule`, `loss_rule`, `peril_clause`, `security`, `remittance_clause`, `separate_investment`, `side_amounts`, `penalty`. This is the operator's expectation of what the acts contain, not evidence.
13. The kickoff prompt lists the Latin drafting terms to classify by (*in accomendatione/accomendacio/comanda*, *in societate/societas/companhia*, *mutuum*, *foenus nauticum*, *cambium*) and gives an example `source_ref` naming four specific acts. The example acts may or may not be commenda/societas acts; I will not privilege them in sampling.
14. The session's system context carried a short standing profile of the maintainer's research programme (entity shielding, ergodicity economics). It states no value for these rows. No memory file and no claude.ai Project was opened.

## The textbook commenda, clause by clause, from general knowledge, before reading any act

- **Who supplies capital.** In the unilateral commenda (*accomendatio*, *commendacio*, Marseille *comanda*) the sedentary investor (*stans*, *commendator*) supplies all of it, in money or goods. The traveller (*tractator*) supplies none. In the *societas* (Genoese usage; Venetian *collegantia*) the *stans* supplies about two-thirds and the *tractator* about one-third.
- **Who travels.** The *tractator*, who acknowledges receipt (*confiteor me accepisse*, *portare laboratum*) and carries the capital overseas. The investor stays at home.
- **Profit shares.** Commenda: three-quarters to the investor, one-quarter to the traveller (*quartum proficui*). *Societas*: half each (*proficuum per medium*), so the traveller's share of profit exceeds his share of capital. Variants exist (a third, a fraction set per act).
- **Who bears loss of capital.** Commenda: the investor alone; the traveller loses only his labour and his expected quarter. *Societas*: each party bears loss in proportion to his capital contribution.
- **Who bears the peril of the sea.** The same as loss of capital: the capital travels at the investor's peril (Marseille: *ad fortunam Dei, maris et gentium*, *ad resicum*). I expect the Genoese acts of the 1150s to state the peril clause rarely or not at all, and the Marseille acts to state it often.
- **Remittance.** The traveller must return or send capital and profit into the investor's power (*in potestate tua mittere / reducere*), sometimes by named third parties, sometimes with licence to send by any ship or with witnesses.
- **Security.** Performance (not the peril) may be secured by a general pledge of the traveller's goods (*pro quibus omnia bona mea tibi pignori obligo*), with or without a penalty of double (*sub pena dupli*). In Marseille, a general obligation of goods behind Blancard's `obligans etc.`
- **Duration and destination.** A single voyage (*hoc viagio*, to a named port: Alexandria, Syria, Sicily, Ceuta, Bougie, Acre), often with *et inde quo voluero* / *quo Deus mihi melius administraverit*; the arrangement ends on the traveller's return and the division of profit. Not open-ended.
- **Number of parties.** Typically bilateral: one investor, one traveller. Several investors may join in a single act, and a traveller commonly takes commendas from many investors for the same voyage in separate acts (the traveller's book of commendas is then a portfolio, but each investor is a separate bilateral contract).
- **What distinguishes a *societas* from an *accomendatio*.** Whether the traveller contributes capital. In the *societas*, both contribute and share profit half-and-half; loss follows capital. In the *accomendatio*, only the investor contributes. A traveller may combine both in a single act (a *societas* plus an additional *accomendatio* from the same investor, at a quarter).

## What I expect the three corpora to answer, and not answer

(Giovanni Scriba vol. I, 1154–61; Guglielmo Cassinese vol. I, 1190–91; Giraud Amalric's cartulary of 1248 as edited by Blancard, Latin where printed.)

**Answer.** The acts should answer the bilateral, internal terms of the contract: who contributes capital and how much (`CF1`, and the traveller's capital share for the *societas*), the profit rule (`LR3`, `LR2`, `LR6`), the loss rule where stated, the peril clause where stated (`RB1`, `RB4`), the destination and voyage (`TS2`), the number of principals (`CF3`), security and penalty (`RB3`), and the voluntary character of entry (`MB3`). Remittance clauses bear on the traveller's obligation, not on any characteristic directly.

**Not answer.** Notarial acts are bilateral instruments between the parties; they address no third party. I expect silence on: liability to the venture's outside creditors (`AP3`, `LR1`); creditor priority in venture assets and partition by members' creditors (`AP1`, `AP2`); juridical personhood, property in the venture's own name, capacity to sue (`LP1`–`LP3`); transferability and depersonalisation of the investor's interest (`CI3`, `CI4`), except perhaps in isolated assignments of claims; withdrawal before return (`CI2`); verification of loss (`VF1`, `VF2`), unless an oath or an accounting clause appears. Market loss as distinct from peril (`RB2`) will be at best implicit in a general loss rule.

**Heterogeneity I expect.** Profit shares other than the textbook quarter/half; *societas* capital ratios other than 2:1; acts with several investors; mixed acts (commenda and *societas* in one); peril clauses frequent in Marseille, rare in Genoa; Genoese acts citing the pledge of goods and a double penalty; Marseille formulae hidden behind `etc.`, which yield `.NR` rather than `0`. I expect Amalric to contain many *cambium* acts and *comanda* acts; Scriba and Cassinese many sales, dowries, loans, quittances and procurations, with commenda and *societas* a minority.

## Per-cell expectations

| census | type_id | char_id | expected value | confidence | why |
|---|---|---|---|---|---|
| orga | `commenda` | `TS2` | single-venture | high | one voyage to a named destination, dissolved on return and division |
| orga | `commenda` | `AP3` | .NR | medium | locator is the traveller; the acts address no outside creditor. Textbook value would be 0 (traveller liable in his own person) but I expect no act to say so |
| orga | `commenda` | `LR1` | .NR | medium | same silence on third parties; textbook would be unlimited liability of the traveller |
| orga | `commenda` | `LR2` | coupled | medium | traveller's reward is a share of profit; alternative `attenuated` because he bears no capital loss (but that is `LR6`'s question) |
| orga | `commenda` | `LR3` | 1 | medium | profit divided by agreed fraction, not a fixed claim; ambiguity: "proportionally to stake" is not met literally, the traveller having no capital stake — may be P |
| orga | `commenda` | `LR4` | 0 | medium | bilateral contract, nothing mutualised among members; the traveller's portfolio of separate commendas is not a pool among members |
| orga | `commenda` | `LR5` | .NA | high | follows `LR4=0` |
| orga | `commenda` | `CF1` | 1 | high | investor supplies capital, traveller labour |
| orga | `commenda` | `CF2` | 0 | high | investor bears loss of capital |
| orga | `commenda` | `CF3` | bilateral | medium | modal one investor; multi-investor acts as a variant |
| orga | `commenda` | `LR6` | upside-only | medium | traveller shares gains, loses only labour |
| orga | `societas_maris` | `TS2` | single-venture | high | as commenda |
| orga | `societas_maris` | `AP3` | .NR | medium | silence on outside creditors |
| orga | `societas_maris` | `LR1` | .NR | medium | same |
| orga | `societas_maris` | `LR2` | coupled | medium | traveller shares profit and loses on his own capital |
| orga | `societas_maris` | `LR3` | 1 | medium | profit shared by fraction; half-and-half on 2:1 capital is not proportional to stake, so P is the alternative |
| orga | `societas_maris` | `LR4` | 0 | medium | no mutualisation beyond the two parties' joint stake |
| orga | `societas_maris` | `LR5` | .NA | high | follows `LR4=0` |
| orga | `societas_maris` | `CF1` | P | medium | both contribute capital, only one travels |
| orga | `societas_maris` | `CF2` | 0 | low | traveller loses his own third, not the investor's capital; P is the alternative if the acts make him share losses on the whole |
| orga | `societas_maris` | `CF3` | bilateral | medium | one *stans*, one *tractator* modal |
| orga | `societas_maris` | `LR6` | symmetric | medium | traveller exposed to gains and to losses on his own contribution |
| orga | `commenda` | `LP1` | .NR | medium | acts do not speak to personhood; literature would say 0 |
| orga | `commenda` | `LP2` | .NR | low | capital received by the traveller personally could be read as observed 0; I expect to hold .NR unless an act vests property somewhere explicit |
| orga | `commenda` | `LP3` | .NR | medium | silent |
| orga | `commenda` | `AP1` | .NR | high | silent on creditor priority |
| orga | `commenda` | `AP2` | .NR | high | creditor limb unanswerable from bilateral acts |
| orga | `commenda` | `AP4` | .NA | high | no founder endowment |
| orga | `commenda` | `CI1` | .NR | low | one investor's capital in the traveller's hands; `several-accounts` if acts keep separate investments apart, `common` if several investors' capital is merged |
| orga | `commenda` | `CI2` | .NR | low | no withdrawal clause expected; single-venture design suggests 1 but that would be inference |
| orga | `commenda` | `CI3` | .NR | medium | no assignment clause expected |
| orga | `commenda` | `CI4` | .NR | medium | no negotiability expected |
| orga | `societas_maris` | `LP1` | .NR | medium | silent |
| orga | `societas_maris` | `LP2` | .NR | low | as commenda |
| orga | `societas_maris` | `LP3` | .NR | medium | silent |
| orga | `societas_maris` | `AP1` | .NR | high | silent |
| orga | `societas_maris` | `AP2` | .NR | high | silent |
| orga | `societas_maris` | `AP4` | .NA | high | no founder |
| orga | `societas_maris` | `CI1` | common | medium | both contributions merged into one stock for the voyage |
| orga | `societas_maris` | `CI2` | .NR | low | as commenda |
| orga | `societas_maris` | `CI3` | .NR | medium | silent |
| orga | `societas_maris` | `CI4` | .NR | medium | silent |
| loss | `commenda_alloc` | `MC1` | allocation | high | NOT BLIND (README leak 1; schema leak 10) |
| loss | `commenda_alloc` | `MB3` | voluntary | high | entry by private contract |
| loss | `commenda_alloc` | `RB1` | capital-provider | medium | peril at the investor's charge; Marseille states it, Genoa may be silent |
| loss | `commenda_alloc` | `RB2` | capital-provider | low | loss on sale falls on the capital; rarely distinguished in the acts, so .NR is the likely alternative |
| loss | `commenda_alloc` | `RB3` | general-estate | low | general pledge of the traveller's goods for performance; `personal` or `none` alternatives; Blancard's `obligans etc.` hides the object |
| loss | `commenda_alloc` | `RB4` | 1 | medium | traveller owes nothing if the venture is lost to the peril |
| loss | `commenda_alloc` | `PR1` | 0 | medium | no premium; the profit share is not a price for bearing peril |
| loss | `commenda_alloc` | `PY0` | .NA | medium | no pool, nothing produced by a pool; the value set presupposes one |
| loss | `commenda_alloc` | `VF1` | .NR | low | acts unlikely to say how a loss is proved |
| loss | `commenda_alloc` | `VF2` | .NR | low | follows `VF1` silence (not .NA unless VF1 is `none`) |
| loss | `societas_maris` | `MC1` | allocation | medium | NOT BLIND (schema leak 10); alternative `pooling` because both parties' capital is merged and loss is shared |
| loss | `societas_maris` | `MB3` | voluntary | high | private contract |
| loss | `societas_maris` | `RB1` | shared | medium | loss follows capital, both contribute |
| loss | `societas_maris` | `RB2` | shared | low | same, if stated at all |
| loss | `societas_maris` | `RB3` | general-estate | low | as commenda |
| loss | `societas_maris` | `RB4` | 1 | low | traveller's obligation to return the investor's share extinguished on loss |
| loss | `societas_maris` | `PR1` | 0 | medium | no premium |
| loss | `societas_maris` | `PY0` | .NA | medium | no pool output |
| loss | `societas_maris` | `VF1` | .NR | low | silent |

## After writing

Print the sha256 of this file, give it to MS, and **do not open any source until MS confirms the commit.**
