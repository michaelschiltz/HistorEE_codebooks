# Reveal notes — commenda-primary-2026-09-28 (stages 5 and directed disconfirmation)

- Pass: `commenda-primary-2026-09-28`. Condition of the new rows: `open`. Coder: `ai`, `claude-opus-5-5`, effort `high`. Values fixed on 2026-09-28.
- Received: `reveal/REVEAL-commenda-2026-09-28.csv` (61 rows; sha256 `3014d5c54ee2c6a09dd72c87b0ba7fc019f82120cbc8d1a790194635aca367cb`), after MS verified the stage-4 freeze. It carries, for each cell, the live value with its confidence, articulation, `source_ref`, `source_read` and notes, and a second set of `secondary_*` columns from a secondary-literature pass. I read the whole file.
- Written, all in `proposed-of/`: `recodings-commenda-primary-open-2026-09-28-organizational_forms.csv` (42 rows) and `recodings-commenda-primary-open-2026-09-28-loss_mitigation_forms.csv` (19 rows), with the `recoding_id_open_stage5` ids; and this file. **No stage-4 file was edited**: the sha256 of all eight stage-4 files is unchanged.
- Evidence rule unchanged: every stage-5 value rests on the acts in `sources/`. The reveal's quotations from secondary works (Harris, van Doosselaere, Udovitch, Held, González de Lara, Pryor) were read as part of the reveal and used only to decide *where to search*; none of them supplies evidence for a stage-5 value. `value_at_recoding` and `agreement` are left empty, as the kickoff's fixed fields require; the live value, its confidence and the disposition are stated at the head of every row's `notes`.
- **Dispositions.** `keep`: the stage-5 value is the stage-4 value and the live value. `dispute`: the stage-5 value is the stage-4 value and differs from the live value. `revise`: the stage-5 value differs from the stage-4 value (the note says whether it now agrees with the live value). Result: 40 keep, 16 dispute, 5 revise. Stage 4 agreed with the live value in 40 of 61 cells; stage 5 agrees in 43.
- **Caution on the three revisions that converge on the live value** (`societas_maris CF2`, `commenda_alloc RB3`, `societas_maris RB3`). Each rests on acts found in the directed search, and the reason for each is stated in the acts' own words. But the search was prompted by the reveal, so these revisions are not independent of it, and they should be weighed as open, not blind, codings.

## 1. Dispositions, all 61 cells

| census | type_id          | char_id | stage 4           | live              | stage 5           | confidence | disposition | stage-5 id |
|--------|------------------|---------|-------------------|-------------------|-------------------|------------|-------------|------------|
| orga   | `commenda`       | `TS2`   | single-venture    | single-venture    | single-venture    | high       | keep        | OF-R0149   |
| orga   | `commenda`       | `AP3`   | .NR               | 0                 | .NR               | .NR        | dispute     | OF-R0150   |
| orga   | `commenda`       | `LR1`   | .NR               | unlimited-several | .NR               | .NR        | dispute     | OF-R0151   |
| orga   | `commenda`       | `LR2`   | coupled           | coupled           | coupled           | high       | keep        | OF-R0152   |
| orga   | `commenda`       | `LR3`   | P                 | 1                 | P                 | medium     | dispute     | OF-R0153   |
| orga   | `commenda`       | `LR4`   | .NR               | 0                 | .NR               | .NR        | dispute     | OF-R0154   |
| orga   | `commenda`       | `LR5`   | .NR               | .NA               | .NR               | .NR        | dispute     | OF-R0155   |
| orga   | `commenda`       | `CF1`   | 1                 | 1                 | 1                 | high       | keep        | OF-R0156   |
| orga   | `commenda`       | `CF2`   | 0                 | 0                 | 0                 | medium     | keep        | OF-R0157   |
| orga   | `commenda`       | `CF3`   | bilateral         | bilateral         | bilateral         | high       | keep        | OF-R0158   |
| orga   | `commenda`       | `LR6`   | upside-only       | upside-only       | upside-only       | low        | keep        | OF-R0159   |
| orga   | `societas_maris` | `TS2`   | single-venture    | single-venture    | single-venture    | medium     | keep        | OF-R0160   |
| orga   | `societas_maris` | `AP3`   | 0                 | 0                 | 0                 | low        | keep        | OF-R0161   |
| orga   | `societas_maris` | `LR1`   | unlimited-several | unlimited-several | unlimited-several | low        | keep        | OF-R0162   |
| orga   | `societas_maris` | `LR2`   | coupled           | coupled           | coupled           | high       | keep        | OF-R0163   |
| orga   | `societas_maris` | `LR3`   | P                 | 1                 | P                 | medium     | dispute     | OF-R0164   |
| orga   | `societas_maris` | `LR4`   | 1                 | 0                 | P                 | low        | revise      | OF-R0165   |
| orga   | `societas_maris` | `LR5`   | synchronising     | .NA               | synchronising     | low        | dispute     | OF-R0166   |
| orga   | `societas_maris` | `CF1`   | P                 | P                 | P                 | high       | keep        | OF-R0167   |
| orga   | `societas_maris` | `CF2`   | 1                 | 0                 | 0                 | medium     | revise      | OF-R0168   |
| orga   | `societas_maris` | `CF3`   | bilateral         | bilateral         | bilateral         | high       | keep        | OF-R0169   |
| orga   | `societas_maris` | `LR6`   | symmetric         | symmetric         | symmetric         | medium     | keep        | OF-R0170   |
| orga   | `commenda`       | `LP1`   | .NR               | 0                 | .NR               | .NR        | dispute     | OF-R0171   |
| orga   | `commenda`       | `LP2`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0172   |
| orga   | `commenda`       | `LP3`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0173   |
| orga   | `commenda`       | `AP1`   | .NR               | P                 | .NR               | .NR        | dispute     | OF-R0174   |
| orga   | `commenda`       | `AP2`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0175   |
| orga   | `commenda`       | `AP4`   | .NA               | .NA               | .NA               | .NA        | keep        | OF-R0176   |
| orga   | `commenda`       | `CI1`   | common            | common            | common            | low        | keep        | OF-R0177   |
| orga   | `commenda`       | `CI2`   | 0                 | .NR               | 0                 | low        | dispute     | OF-R0178   |
| orga   | `commenda`       | `CI3`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0179   |
| orga   | `commenda`       | `CI4`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0180   |
| orga   | `societas_maris` | `LP1`   | .NR               | 0                 | .NR               | .NR        | dispute     | OF-R0181   |
| orga   | `societas_maris` | `LP2`   | P                 | .NR               | P                 | medium     | dispute     | OF-R0182   |
| orga   | `societas_maris` | `LP3`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0183   |
| orga   | `societas_maris` | `AP1`   | .NR               | P                 | .NR               | .NR        | dispute     | OF-R0184   |
| orga   | `societas_maris` | `AP2`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0185   |
| orga   | `societas_maris` | `AP4`   | .NA               | .NA               | .NA               | .NA        | keep        | OF-R0186   |
| orga   | `societas_maris` | `CI1`   | common            | common            | common            | high       | keep        | OF-R0187   |
| orga   | `societas_maris` | `CI2`   | 0                 | .NR               | 0                 | low        | dispute     | OF-R0188   |
| orga   | `societas_maris` | `CI3`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0189   |
| orga   | `societas_maris` | `CI4`   | .NR               | .NR               | .NR               | .NR        | keep        | OF-R0190   |
| loss   | `commenda_alloc` | `MC1`   | allocation        | allocation        | allocation        | medium     | keep        | LM-R0039   |
| loss   | `commenda_alloc` | `MB3`   | voluntary         | voluntary         | voluntary         | high       | keep        | LM-R0040   |
| loss   | `commenda_alloc` | `RB1`   | capital-provider  | capital-provider  | capital-provider  | medium     | keep        | LM-R0041   |
| loss   | `commenda_alloc` | `RB2`   | .NR               | capital-provider  | .NR               | .NR        | dispute     | LM-R0042   |
| loss   | `commenda_alloc` | `RB3`   | surety            | none              | none              | medium     | revise      | LM-R0043   |
| loss   | `commenda_alloc` | `RB4`   | 1                 | 1                 | 1                 | medium     | keep        | LM-R0044   |
| loss   | `commenda_alloc` | `PR1`   | 0                 | 0                 | 0                 | medium     | keep        | LM-R0045   |
| loss   | `commenda_alloc` | `PY0`   | .NA               | .NA               | .NA               | .NA        | keep        | LM-R0046   |
| loss   | `commenda_alloc` | `VF1`   | .NR               | documentary       | .NR               | .NR        | dispute     | LM-R0047   |
| loss   | `commenda_alloc` | `VF2`   | .NR               | mixed             | claimant-fault    | low        | revise      | LM-R0048   |
| loss   | `societas_maris` | `MC1`   | allocation        | allocation        | allocation        | medium     | keep        | LM-R0049   |
| loss   | `societas_maris` | `MB3`   | voluntary         | voluntary         | voluntary         | high       | keep        | LM-R0050   |
| loss   | `societas_maris` | `RB1`   | shared            | shared            | shared            | medium     | keep        | LM-R0051   |
| loss   | `societas_maris` | `RB2`   | shared            | shared            | shared            | low        | keep        | LM-R0052   |
| loss   | `societas_maris` | `RB3`   | general-estate    | none              | none              | medium     | revise      | LM-R0053   |
| loss   | `societas_maris` | `RB4`   | 1                 | 1                 | 1                 | low        | keep        | LM-R0054   |
| loss   | `societas_maris` | `PR1`   | 0                 | 0                 | 0                 | medium     | keep        | LM-R0055   |
| loss   | `societas_maris` | `PY0`   | .NA               | .NA               | .NA               | .NA        | keep        | LM-R0056   |
| loss   | `societas_maris` | `VF1`   | .NR               | .NR               | .NR               | .NR        | keep        | LM-R0057   |

## 2. How the directed disconfirmation was run

For each of the 21 cells where the stage-4 value differed from the live value, I asked which acts would overturn my own value, and searched for them in **all printed acts of the three corpora** (803 Scriba, 1,095 Cassinese, 561 Amalric), not only in the sample. The search ran over a letters-only, lower-case copy of each act's text layer, so that OCR spacing (`s u p e rflu u m`) does not hide a match; every hit was then read in context. Where a hit decided a revision, the act was read in full. The patterns searched, by question:

- Liability to third parties, creditors, entity shielding (`AP3`, `LR1`, `AP1`): `mutuare`, `mutuo accipere`, `possit mutuare`, `super societatem`, `accipere ad cambium`, `creditor`, and settlements and quittances that mention a societas or accomendatio.
- Personhood and property (`LP1`, `LP2`): `nomine societatis`, `ex parte societatis`, `pro societate`, and every act outside the two frames that names a societas, companhia or accomendatio (48 acts: quittances, debt acknowledgements, settlements, declarations, procurations).
- Pooling (`LR4`, `LR5`): `communes equis porcionibus`, `converti`, `reverti ad societatem`, `ponere in societate`, `in proficuum societatis`.
- Profit rule (`LR3`): `per medium`, `medietatem lucri/proficui` against `per libram`, `pro solido et libra`, `secundum racionem` applied to the main stock.
- Peril and capital (`CF2`): promises to pay or bring back the capital (`dare promittit ei capitale`, `totum capitale cum medietate lucri reducere`, `salvum erit`, `in omni casu`), crossed with peril clauses and with land and sea markers.
- Withdrawal (`CI2`): `dum placuerit`, `quando voluerit`, `ex quo petierit`, `ad voluntatem`, `non possit petere`, `donec redierit`.
- Market loss (`RB2`): `dampnum`, `si minus habuerit`, `perdita`, per-libram adjustment clauses.
- Security (`RB3`): `pignori`, `in suis bonis`, `debitor et pagator`, `fideiussor`, `obligans`, counted per instrument type in each cartulary.
- Proof of loss (`VF1`, `VF2`): `naufrag-`, `perdidi`, pirates, robbery, `clarefactum`, `probare`, `sacramentum`, `culpa`, `defectu`.

## 3. Cell by cell: the 21 cells where stage 4 differed from the live value

### `commenda` `AP3` — stage 4 `.NR`, live `0` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 10 and 11 (PDF pagination; the conference draft carries no printed page numbers) (confidence high, source_read partial).

Stage-4 .NR held against live 0. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Borrowing on the venture is licensed only in societas acts (Cassinese 218: possit mutuare super societatem et accomendationem si necesse fuerit pro carrico navis; 296; 335; 726; Amalric 774) and reported in one societas settlement (Scriba XLVIII: pro ipsa societate cepit mutuo bisancios .L.). No act of the 373 in the commenda frame speaks to the working party's liability to third parties. The live value rests on a characterisation in the secondary literature that these acts neither confirm nor contradict.

### `commenda` `LR1` — stage 4 `.NR`, live `unlimited-several` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 10 and 11 (PDF pagination; the conference draft carries no printed page numbers) (confidence high, source_read partial).

Stage-4 .NR held against live unlimited-several, for the reason given at commenda AP3: no commenda act speaks to liability to third parties. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes).

### `commenda` `LR3` — stage 4 `P`, live `1` → stage 5 `P` (dispute)

Live basis: Pryor 1977 (confidence high, source_read unknown).

Stage-4 P held against live 1. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). No commenda act divides profit in proportion to a stake held by the working party (no per libram, pro solido et libra or secundum racionem rule applied to him); his share is always a fixed fraction (quartam proficui) of a profit in which he has no capital, and the only LR3=1 acts are the gratuitous ones. The disagreement is over the definition: 'shared proportionally to stake rather than as a fixed claim' has two limbs, and the acts meet the second (a share, not a fixed claim) and fail the first (the share tracks no stake). The live coding reads the second limb as the whole test. Needs a ruling on the definition.

### `commenda` `LR4` — stage 4 `.NR`, live `0` → stage 5 `.NR` (dispute)

Live basis: [verify] (confidence medium, source_read unknown).

Stage-4 .NR held against live 0 ('bilateral, not pooled', [verify]). Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Found: a pooling agreement among three travellers (Amalric 697, societas frame); the traveller's quarter from commendas carried beside a societas reverting to that societas (in the commenda frame Cassinese 50 and 1082: ad quartam proficui, que debet ponere in societate); commended goods reckoned per libram with the other goods the traveller carries (Cassinese 125, 175, 271, 383, 425, 438, 1009) and, the opposite, implicare separatim. All of these run between a commenda and other arrangements the traveller holds; none says whether members of one commenda share one another's own losses. An observed 0 needs a clause excluding such sharing, and none exists; the live 0 is an inference from bilateral form.

### `commenda` `LR5` — stage 4 `.NR`, live `.NA` → stage 5 `.NR` (dispute)

Live basis: .NA (confidence .NA, source_read .NA).

Stage-4 .NR held against live .NA. The live .NA propagates from LR4=0; with LR4 .NR its applicability is unknown, so .NR. Stands or falls with commenda LR4.

### `societas_maris` `LR3` — stage 4 `P`, live `1` → stage 5 `P` (dispute)

Live basis: van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence high, source_read partial).

Stage-4 P held against live 1 (high, articulated). Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Of the 334 acts in the societas frame, 260 divide profit per medium or by halves and 2 by per libram or pro rata. The live note states the structure itself: profit split equally, loss pro rata to capital, 'the two sides follow different rules'. That is the half-presence P records: a share, not a fixed claim; on the profit side, not in proportion to stake. Same definitional question as commenda LR3.

### `societas_maris` `LR4` — stage 4 `1`, live `0` → stage 5 `P` (revise)

Live basis: van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence medium, source_read partial).

Revised 1 -> P; live 0. The directed search showed that my stage-4 instance coding was inconsistent. Scriba DCCXXVII was coded P for a clause turning side-placement profit into the societas's profit, but the same clause, the quarter the traveller earns on accomendationes carried with the societas 'que debet reverti ad societatem', stands in 15 further sampled acts that were not coded (Cassinese 12, 38, 74, 106, 143, 337, 606, 1011, 1067, 1079, 1091; Scriba CXLI, CLXXXI, CCLXXV, CCCLXXXV) and in at least 24 acts of the full frame (Cassinese 19). Recounted over the sample: P 16 (Cassinese 11 of 60; Scriba 5 of 60), 1 in 1 (Amalric 697, three travellers pooling the profit of all their comandas). Variant 1: Amalric (1 of 1). Alternative reading, which would move the cell toward the live value: the reverting quarter is the fruit of the traveller's labour, which the societas has bought, not a mutualisation of outcomes; then the clause does not speak to LR4 and the cell rests on Amalric 697 alone. No act excludes sharing, so 0 is not observed on either reading.

### `societas_maris` `LR5` — stage 4 `synchronising`, live `.NA` → stage 5 `synchronising` (dispute)

Live basis: .NA (confidence .NA, source_read .NA).

Stage-4 synchronising held against live .NA. The live .NA propagates from LR4=0; with LR4 P (revised) LR5 applies. The side placements travel on the same voyage as the societas and are reckoned per libram with it (que debent lucrari et expendere per libram cum societate: Cassinese 38, 74, 143, 337), so the pooled outcomes are correlated. Now rests on 17 sampled acts, not one. Analyst-imposed.

### `societas_maris` `CF2` — stage 4 `1`, live `0` → stage 5 `0` (revise)

Live basis: van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence high, source_read partial).

Revised 1 -> 0; now agrees with the live value, for a reason found in the acts, not in the reveal's sources. The Amalric formula on which all five Amalric 1s rested (totum capitale cum medietate lucri reducere in posse tuo, or its dare et solvere and portare et solvere forms at a term) also stands in sea-going acts that expressly put the peril on both partners pro rata: Amalric 429, ad fortunam Dei et usum maris ... et tuum resegum et meum ... et totum capitale cum medietate lucri reducere in posse tui; Amalric 236 likewise. A promise to bring back the capital therefore does not assume the peril; it is a duty to render the capital and profit there are. The Cassinese land formula, tunc dare promittit ei capitale et medietatem proficui quod Deus dederit ... sub pena dupli, is the same duty at a term and is re-read the same way (the alternative given at stage-4 decision point 5). Those acts no longer speak to CF2. Recounted over the sample: 0 in 7 (Amalric 112, 236, 429, 442, 467, 774; Scriba DCCXXXIX); 1 in 2 (Scriba CCCLV, Capitale tuum super me salvum erit; Scriba DCLXXIV, the father promises the capital salvas futuras in omni casu). Variant 1: Scriba 2 of 3 (67%). Cassinese: no act speaks. The land/sea frame question (stage-4 decision point 4) no longer decides this cell.

### `commenda` `LP1` — stage 4 `.NR`, live `0` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 10-13 (PDF pagination; the conference draft carries no printed page numbers); van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence medium, source_read partial).

Stage-4 .NR held against live 0 (analyst-imposed). Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). No act makes a commenda or societas a party, a claimant or a principal: every constitution, quittance (Cassinese 234, 441, 893), settlement (Scriba XLVIII) and procuration (Amalric 518: quas michi debet ex causa companhie) is made by and in the names of natural persons, and claims arising from the arrangement are the partners' own. This pattern would support 0. I do not take it, because it is also what a formulary recording obligations between persons would show if the question of juridical status never arose, and LP1 asks about juridical status. Alternative: 0, analyst-imposed, on this primary pattern.

### `commenda` `AP1` — stage 4 `.NR`, live `P` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 11 (PDF pagination; the conference draft carries no printed page numbers) (confidence medium, source_read partial).

Stage-4 .NR held against live P (Harris 2007, 11, as quoted in the reveal). Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Commenda acts mention creditors only where the traveller is told to pay the investor's own creditor from the proceeds (Amalric 29, 187). Societas acts license borrowing super societatem (Cassinese 218, 296, 335), which gives a venture creditor recourse to the stock, but no act says whether a partner's personal creditor could reach it or ranks behind. One limb (venture creditors' recourse, attested for the societas only) without the other (priority over personal creditors) is .NR by the two-limb rule. Nearest clause found: in Cassinese 277 (a shop accomendatio, not sampled) the partners swear not to pledge the investor's goods (de rebus Idonis non ponent in pignore), a contractual bar on the working party's using the capital to secure his own debts; it states no rule binding his creditors.

### `commenda` `CI2` — stage 4 `0`, live `.NR` → stage 5 `0` (dispute)

Live basis: van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315); Harris 2007, 11 (PDF pagination; the conference draft carries no printed page numbers) (confidence .NR, source_read partial).

Stage-4 0 held against live .NR. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). No lock-in clause (non possit petere, donec redierit or the like) occurs anywhere in the 373-act commenda frame. Recall on demand or at will occurs in Cassinese 875 (deposit use; sampled) and Cassinese 277 (a shop: usque dum placuerit Idonii ... cum placuerit Idonii dare promittunt; not sampled). Both are land-based; the voyage acts do not speak. The 0 describes the land and deposit uses of the term and stands under the frame rule. Alternative: .NR if the frame is restricted to voyage commendas (decision point 4 of the stage-4 notes).

### `societas_maris` `LP1` — stage 4 `.NR`, live `0` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 10-13 (PDF pagination; the conference draft carries no printed page numbers); van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence low, source_read partial).

Stage-4 .NR held against live 0 (low, analyst-imposed). As at commenda LP1. In addition, 13 Cassinese acts outside the sample record a credit taken in one person's name and declare that part of it is 'de societate quam habet cum ...' (e.g. Cassinese 541, 544, 950): the societas's claims are held by persons. This supports 0 more directly than anything in the commenda acts, and the alternative (0, analyst-imposed) is stronger here. Held at .NR for the reason given at commenda LP1.

### `societas_maris` `LP2` — stage 4 `P`, live `.NR` → stage 5 `P` (dispute)

Live basis: Harris 2007, 11 (PDF pagination; the conference draft carries no printed page numbers); van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence .NR, source_read partial).

Stage-4 P held against live .NR; confidence raised from low to medium. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Beyond the idiom of Scriba CCXI and DCCXXXIX (res ipsius societatis; ad resicum et fortunam societatis), 13 Cassinese debt, sale and sea-loan acts (236, 241, 537, 541, 542, 544, 545, 584, 636, 787, 928, 950, 990; outside the sample) record a credit taken in one person's name and declare which part of it belongs to a societas (Et lib. .xl. sunt de societate quam habet cum Wilielmo Malfiliastro, et alie sunt sue, no. 541, spacing of the OCR normalised). Property identified as the societas's and held in a member's name: one limb present, one absent, which is what P records.

### `societas_maris` `AP1` — stage 4 `.NR`, live `P` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 11 (PDF pagination; the conference draft carries no printed page numbers) (confidence low, source_read partial).

Stage-4 .NR held against live P (low; the live note treats it as one datum with commenda AP1). As at commenda AP1: venture creditors are given recourse to the stock by licence to borrow super societatem (Cassinese 218, 296, 335), but no act ranks them against a partner's personal creditors.

### `societas_maris` `CI2` — stage 4 `0`, live `.NR` → stage 5 `0` (dispute)

Live basis: van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence .NR, source_read partial).

Stage-4 0 held against live .NR. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). No lock-in clause occurs in the 334-act societas frame. Withdrawal or division at will occurs in Scriba DXXVI (sampled) and Scriba DLIX (Baldezonus may take from the societas quando voluerit; not sampled); recall on demand or at the partners' pleasure in Cassinese 469, 878, 952 and Amalric 755. Three of the sampled five are land-based. Alternative: .NR if the frame is restricted to sea-going acts, where the evidence is Scriba DXXVI and Cassinese 878 only.

### `commenda_alloc` `RB2` — stage 4 `.NR`, live `capital-provider` → stage 5 `.NR` (dispute)

Live basis: Harris 2007, 9-13; Held 2025, 11-13 and 20-22 (Statute of Dubrovnik 1272, lib. VII, 50-51 and lib. III, 46; MHR I-IV, 53 contracts 1278-1301) (confidence high, source_read partial).

Stage-4 .NR held against live capital-provider (Harris 2007, 10, as quoted in the reveal). Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Clauses that separate the result of sale from the peril (si minus habuerit, per libram adjustment) occur only in societas acts (Scriba DCXXVI, DCXCII). In commenda acts the only dampnum clauses concern fault (Cassinese 201; the Amalric sureties). No commenda act says who bears a loss on sale.

### `commenda_alloc` `RB3` — stage 4 `surety`, live `none` → stage 5 `none` (revise)

Live basis: Harris 2007, 9-13 (confidence high, source_read partial).

Revised surety -> none; now agrees with the live value, for a reason found in the acts. The directed search compared the formularies: the same notaries write a pledge, a surety or an obligation of goods into 85% of Scriba's sales and 91% of his sea loans, 89% of Cassinese's sales, 64% of his sea loans and 75% of his mutua, but into 0 of Scriba's 10 commendas and 7 of Cassinese's 142, and none of those 7 secures the advance: three are accomendationes nomine pignoris, goods carried as a pledge for the carrier's own claim (300, 362, 378); three forbid lending the capital except to a merchant against a pledge (710, 1012, 1093); one has the partners swear not to pledge the investor's goods (277). Where a notary's formulary for comparable advances carries a security clause and his commenda formulary omits it, the omission is drafted, not silence: an observed none. This departs from my stage-4 rule (the absence of a clause is silence) for this characteristic only, and needs a ruling. Amalric's obligans etc. is abridged and not counted; his explicit sureties answer only for the son's culpa (in omni defectu quem invenires culpa dicti filii mei: Amalric 141, 194 in the sample; about ten of 221 printed commenda notulae). Recounted: Genoese sample none 69 of 70 (goods 1: Cassinese 362); Amalric surety 2 of 2 speaking. Variant surety (Amalric). Alternative: the stage-4 value, if drafted omission is not accepted as an observation.

### `commenda_alloc` `VF1` — stage 4 `.NR`, live `documentary` → stage 5 `.NR` (dispute)

Live basis: Held 2025, 11-13 and 20-22 (Statute of Dubrovnik 1272, lib. VII, 50-51 and lib. III, 46; MHR I-IV, 53 contracts 1278-1301); Gonzalez de Lara 2002, 259 (confidence high, source_read full).

Stage-4 .NR held against live documentary (high, articulated). The live value rests on Held 2025 (Dubrovnik) and Gonzalez de Lara 2002 (Venice); the clarefactum formula it quotes does not occur in these corpora. Directed disconfirmation run over all printed acts of the three corpora, not only the sample (section 3 of the reveal notes). Searched for loss events and proof (naufrag-, perdidi, pirates, robbery, clarefactum, probare, sacramentum). Found only Scriba XLIV, a holder's notarial declaration that he lost another's goods (quas perdidi), which is a record rather than a procedure the traveller must pass to be discharged, and Scriba XLVIII, a settlement in which the traveller swears to his borrowings. No commenda act says how a loss is to be established.

### `commenda_alloc` `VF2` — stage 4 `.NR`, live `mixed` → stage 5 `claimant-fault` (revise)

Live basis: Held 2025, 11-13 and 20-22 (Statute of Dubrovnik 1272, lib. VII, 50-51 and lib. III, 46; MHR I-IV, 53 contracts 1278-1301) (confidence high, source_read full).

Revised .NR -> claimant-fault; live mixed. The directed search found that the acts do state what separates the working party's discharge from his liability: fault. Amalric's sureties bind themselves in omni defectu quem invenires culpa dicti filii mei (141, 194 in the sample; also 32, 84, 88, 162, 283, 302, 341, 410 in the frame); Cassinese 201 (outside the sample) binds the father si ita non attenderit vel in sua culpa devastaverit, which is fault together with failure to keep the terms (mixed), as do the societates Cassinese 333 and 731. Sample: claimant-fault 2 of 2 speaking. Variant mixed (Cassinese, frame only). Dependence flagged: VF1 stays .NR (the acts say what must be found, not how), and VF2 is coded because a stated object of verification implies that verification occurs. Alternative: .NR, following VF1.

### `societas_maris` `RB3` — stage 4 `general-estate`, live `none` → stage 5 `none` (revise)

Live basis: van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315) (confidence high, source_read partial).

Revised general-estate -> none; now agrees with the live value, for the formulary reason given at commenda_alloc RB3: Scriba's societates carry a security clause in 1 of 174 acts and Cassinese's in 11 of 138, against 64-91% of the same notaries' loans and sales. Recounted over the Genoese sample: none 114 of 120; general-estate 5 (Scriba CCCLV; Cassinese 53, 150, 529, 726), pledges securing a land partner's promise to pay at a term or a traveller's performance; surety 1 (Cassinese 333, two friends for the traveller's culpa). Amalric: surety 1 of 1 speaking (760, a father). Variant surety (Amalric); general-estate is below 10% in both Genoese corpora (Cassinese 4 of 60, Scriba 1 of 60). Alternative: the stage-4 value, if drafted omission is not accepted as an observation.


## 4. Instance readings changed by the directed search (stage-4 instance files not edited)

The stage-4 instance files stand as written. The stage-5 cells rest on these changed readings:

- **`CF2` no longer read from a promise to render the capital.** Dropped as `CF2=1`: Cassinese 29, 875 (commenda); Cassinese 53, 93, 150, 310, 469, 529, 943, 952 and Amalric 41, 164, 755, 760, 1015 (societas). Reason: Amalric 429 and 236 carry the same promise (`totum capitale cum medietate lucri reducere`) together with an express shared-peril clause. Kept as `1`: Scriba CCCLV (`Capitale tuum super me salvum erit`) and DCLXXIV (the father's guarantee `in omni casu`).
- **`LR6`**: Amalric 41 (commenda) no longer `symmetric`, since its `CF2=1` falls.
- **`LR4=P` added** to 15 sampled societas instances carrying `que debet reverti ad societatem` or its Scriba equivalents: Cassinese 12, 38, 74, 106, 143, 337, 606, 1011, 1067, 1079, 1091; Scriba CXLI, CLXXXI, CCLXXV, CCCLXXXV. This corrects an omission at stage 4: I had coded the clause in Scriba DCCXXVII and missed it elsewhere.
- **`RB3=none`** for Genoese instances without a security clause (commenda 69 of 70; societas 114 of 120), on the formulary contrast (section 5).
- **`VF2=claimant-fault`** for Amalric 141 and 194 (`in omni defectu quem invenires culpa dicti filii mei`).

## 5. Methodological moves that need MS's ruling

1. **Drafted omission as an observation (`RB3`).** Stage 4 treated the absence of a security clause as silence. The directed search showed that the same notaries put security into 85–89% of sales, 64–91% of sea loans and 67–75% of mutua, and into almost no commenda or societas. I now read the omission as drafted, and so as an observed `none`. I apply this only where a notary's own formulary for comparable instruments shows he wrote the clause when it was intended. I have not extended it to `CF2`, `VF1` or `LP1`, where no comparable instrument supplies the contrast. If MS rejects the move, both `RB3` cells revert to their stage-4 values.
2. **A promise to render the capital is not an assumption of peril (`CF2`).** This was the stage-4 alternative at decision point 5. It is now adopted because an act in the corpus carries the promise and the shared-peril clause side by side (Amalric 429). With it, the frame question (land against sea, stage-4 decision point 4) no longer decides `societas_maris CF2`.
3. **What `LR4` counts.** Side-profit reversion into the societas is coded `P`, for consistency with Scriba DCCXXVII. The alternative, that it is labour income the societas has bought and not a mutualisation, would leave `LR4` on Amalric 697 alone. Neither reading yields the live `0`, because no act excludes sharing.
4. **`VF2` coded while `VF1` is `.NR`.** The acts state what must be found (fault) but not how. The vocabulary makes `VF2` depend on `VF1` without saying what `VF2` is when `VF1` is unobserved.
5. **The `LR3` definition.** Both `LR3` disputes turn on whether "proportionally to stake" is a limb of the test or a gloss on "rather than as a fixed claim".
6. **Land and deposit uses in the frames (`CI2`).** The `0` in both `CI2` cells comes mostly from land-based and deposit uses of the drafting terms. The disputes stand under the frame rule, and fall if the frames are restricted to voyages.

## 6. Observations on the live evidence (for adjudication, not coding)

- Several live values rest on sources outside the three corpora and outside the two cities: `commenda_alloc VF1` and `VF2` rest on Held 2025 (Dubrovnik) and González de Lara 2002 (Venice), and `RB4` on the Statute of Dubrovnik. The `clarefactum` formula the live note quotes does not occur in Scriba, Cassinese or the printed Amalric.
- The live `commenda AP3`, `LR1` and `AP1` rest on Harris 2007 as a characterisation of the form. The primary acts confirm the premise behind them for the societas only (licences to borrow `super societatem`) and are silent for the commenda.
- The live note at `societas_maris CF3` flags the same `bilateral` collision that the priors file reported as leak 2.
- The live `societas_maris LR3` note describes profit halved and loss pro rata to capital, which is the structure the stage-5 `P` records.

## 7. Checks

- Both stage-5 files validated with `~/.local/bin/frictionless validate res-<census>.json` (frictionless 5.19.1) on scratch copies outside `proposed-of/`, each against its census's `recodings` resource with the foreign key removed. Output: `organizational_forms_recodings … VALID`; `loss_mitigation_forms_recodings … VALID`.
- By script: the 61 ids, `record_id`s, `char_id`s and censuses match `cells-in-scope.csv` (`recoding_id_open_stage5`); every value is in `allowed_values` or is `.NR`/`.NA`; `.NA` and `.NR` propagate; `condition=open` on every row; LF line endings; the eight stage-4 files have unchanged sha256.
- Dependence at stage 5: `commenda` `LR4=.NR`/`LR5=.NR`; `societas_maris` `LR4=P`/`LR5=synchronising`, `CF1=P`/`CF2=0`; `commenda_alloc` `VF1=.NR`/`VF2=claimant-fault` (flagged, section 5 item 4).
- The sha256 of the new files is printed in the chat; this file cannot carry its own.
