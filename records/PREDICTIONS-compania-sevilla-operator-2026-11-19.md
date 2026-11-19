# Operator's predictions and withheld rulings — compania-sevilla-2026-11-19 (withheld from the coder)

**Withheld section of the Seville *compañía* batch.** Excluded from the bundle and from the coding prompt. Committed together with the coder's filled priors (sha256 `e384ba43…d53880`), before the coding chat opened any source, so that it can be scored in `logbook/4`. Written 2026-11-19 by `ai` (`claude-opus-5-5`) as operator. The assignment table and the `AP2` line were revised the same day, before any coding, after the bundle's README was written and `code-a-form` was read back against this file.

**Not blind, and saying so.** The operator has read all ten deeds in full against the page images and MS has ruled on one clause, so what follows are **readings**, not predictions made in ignorance of the evidence. The predictions are about **what the blind coder will return** from the same deeds; the falsification test that matters is the coder's own priors file. See `records/NOTES-compania-sevilla-operator-2026-11-19.md` §2 for what was spent.

## Withheld rulings (MS, 2026-11-19)

**R1. Doc. 8's loss clause.** "Ytem si pérdida hubiere en esta compañía, lo que Dios no quiera, cargue a todos los compañeros tal y como hereda en la ganancia" (p. 74). The labour-only factor, Gonzalo Fernández de Loya, is liable for one quarter of any loss, out of his own goods. Grounds: he is received "por factor y compañero" (p. 68), contracts above 100 pesos are made in the name of "todos cuatro compañeros" (p. 69), returns are registered to all four (p. 73), and he takes a quarter of profit "por la solicitud de su persona" (p. 74). "como a tal vuestro factor, y persona que no mete en esta dicha compañía caudal alguno" (pp. 74–75) describes his position and does not limit his share of loss. Doc. 9 is not evidence for the reading of doc. 8.

**R2. Contract-set loss allocation.** Where the deeds of one form place the loss of the principal's capital differently in terms, `CF2` takes a new value for contract-set allocation (working name `contractual`), and `LR6` likewise. Not `P`, which stays "a defined fraction … within each arrangement, never variation across instances" (ruling 7 of 2026-10-11); not `.NR`, because the deeds state their terms. Encoded at application, after the coding is frozen, and after a sweep of the existing `CF2` cells for the same situation. Version consequence: `organizational_forms` 0.13.0 → 0.14.0.

## The operator's reading of the three defining deeds

| Cell | Doc. 3 (1542) | Doc. 8 (1550) | Doc. 9 (1542) |
|---|---|---|---|
| `CF1` labour party | factor with 80 ducados against 3,000 | factor, labour only (p. 69) | factor, labour only (p. 77) |
| `CF2` agent bears capital loss | 0: loss "a la rata según el puesto de cada uno" (p. 50); he loses only on his own 80 ducados | P: ¼ (R1) | 0: "que ella corra contra vos … y no contra mí" (p. 79) |
| `LR6` coupling symmetry | symmetric (his quarter of profit; loss on his own stake) | symmetric | upside-only |
| `CF3` principal count | bilateral (one principal) | multilateral (three) | multilateral (two) |
| `TS2` venture horizon | fixed-term, six years | fixed-term, four years, extendable | fixed-term, four years, extendable |
| Death of a party | not provided for | heirs of factor and of principals excluded until the accounts are closed or the term ends (p. 73) | not provided for |
| Early ending by principals | recall at any time (p. 48) | at will, "sin declararlo" (p. 74) | recall at any time (p. 78) |

## Predictions on assignment

The bundle gives the coder MS's scope in words and all ten deeds; it does not say which deeds are instances.

| Deed | Operator's reading | Predicted assignment | Likeliest deviation |
|---|---|---|---|
| 3 | capital 3,000 v. 80 ducados, factor-partner for ¼ | in | in, with `CF1` P and a note on the 80 ducados |
| 8 | three principals, labour-only factor, ¾ – ¼ | in | — |
| 9 | two principals, labour-only factor, ¾ – ¼ | in | — |
| 2 | equal capital from both partners, one travels | out, or in with a note | **in**: the scope text says "one or more partners supply the capital and another partner travels", which doc. 2 also meets if the traveller's own half is read as a stake rather than as the capital |
| 6 | salaried factor with an embedded half-shares venture | out | in, on the venture |
| 7 | rubric *Compañía*, salaried factor | out | in, on the rubric, which would break the README's rule on rubrics |
| 4, 5 | commission sale (5%, 6%) | out | — |
| 1, 10 | powers of attorney | out | — |

## Predictions by cell

| Cell | Predicted coder value | Confidence | Basis | Likeliest deviation |
|---|---|---|---|---|
| `CF1` | 1 | high | the definition; docs. 8, 9 | P, citing doc. 3's 80 ducados |
| `CF2` | **misfit reported under answer 4**; cell coded `.NR` or P with the three deed values in notes | medium | three deeds, two values, no value for variation | **0, reading doc. 8's clause as limited to forfeiture of the factor's share (R1 rejected)**; or P with no misfit reported |
| `LR6` | misfit reported, as `CF2` | medium | symmetric in 3, 8; upside-only in 9 | upside-only, if doc. 8 is read as in the deviation above |
| `CF3` | multilateral, with doc. 3 noted; or misfit reported | low | two of three deeds | bilateral |
| `LR2` | coupled | high | quarter of profit in all three | attenuated |
| `LR3` | 1 | not a test | definition | — |
| `TS2` | fixed-term | high | 4–6 years stated | — |
| `TS3` | 1 | medium | principals may end or recall at will in all three | P, because the factor cannot |
| `CI1` | common | medium | "cuerpo de esta compañía" (8), "montón" (3, 9) | several-accounts, from doc. 8's thirds |
| `AP2` | `.NR`, with doc. 8's exclusion of heirs noted | medium | one deed of three, and `code-a-form` (line 164) requires the creditors' limb, which no deed addresses | P or 1 from doc. 8's exclusion of heirs |
| `LR1` | `.NR` | medium | the deeds bind the parties' goods to each other; no clause on outside creditors | unlimited-joint, from "contratos que suenen a todos cuatro compañeros" |
| `MG2` | single-principal | medium | principals direct, factor acts within instructions | collective, from doc. 8's three principals |
| `MG4` | private-contract | not a test | notarial deeds | — |
| `FP1` | commercial-profit | high | — | — |
| `LP1`–`LP3`, `AP1`, `AP3`, `AP4`, `TS1`, `CI3`, `CI4`, `FP2`–`FP4`, `MG1`, `MG3`, `LR4`, `LR5`, `CI2`, `CI5`, `TS4` | not predicted | — | not read for | — |

## Scoring rules, fixed before the coding

1. **R1 test.** The coder's reading of doc. 8's loss clause is scored against R1: agree (¼ on the factor, from his own goods), partial (¼ on the factor, extent unstated), or disagree (factor bears no loss beyond his labour or share). The coder's grounds are recorded verbatim.
2. **Misfit test.** `CF2` and `LR6` score as confirmed if the coder reports, unprompted, that the vocabulary has no value for what the deeds show. A value coded without the report scores as a miss, whatever the value.
3. A cell marked "not a test" is reported but not scored.
4. A deviation is scored in its direction: toward a stronger claim than the deeds bear, or a weaker one.
