# Rulings: `compania-sevilla` blind first coding, 2026-11-19

Rulings by MS on 2026-11-19 (15:26 and 15:27 JST), on the questions raised in `records/NOTES-compania-sevilla-coding-2026-11-19.md` and on the operator's scoring against `records/PREDICTIONS-compania-sevilla-operator-2026-11-19.md`. The coded rows as frozen are `records/proposed-rows-compania-sevilla-2026-11-19-organizational_forms.csv` and are not altered; these rulings are applied at application. Each ruling was put by the operator with a recommendation and accepted as recommended.

## Ruling 1. Doc. 2 is not an instance of `compania_factoria_sevilla`

Doc. 2 (1516, González Vallecillo, fols. 82r–84v) is a two-sided partnership: each partner puts in 158,168 maravedís and one of them travels. It is outside the form, whose point is the asymmetry between capital and labour. This is a scope ruling made before the coding (operator brief, D2) and not a coding error: the scope text in the bundle's README ("one or more partners supply the capital and another partner travels") admits doc. 2, and the coder assigned it under the test written in its priors before the source was opened.

**Consequence.** The row rests on docs. 3, 8 and 9. The two ties the coder reported disappear, and the four disputed cells are coded under ruling 2 of 2026-10-07 (modal state, counts in `notes`, confidence lowered):

| Cell | Doc. 3 | Doc. 8 | Doc. 9 | Coded |
|---|---|---|---|---|
| `CF1` | P | 1 | 1 | 1 (2:1), low |
| `CF3` | bilateral | multilateral | multilateral | multilateral (2:1), low |
| `CF2` | 0 | P | 0 | 0 (2:1), low |
| `LR6` | symmetric | symmetric | upside-only | symmetric (2:1), low |

`LR6` for doc. 3 follows the coder's reading on the `societas_maris` precedent (the factor's exposure on his own 80 ducados). On the stricter reading the coder recorded, doc. 3 is upside-only and the modal state becomes upside-only (2:1). The note says so. Every other cell's notes and counts are revised at application to drop doc. 2.

## Ruling 2. Contract-set loss allocation: the operator's R2 is withdrawn; ruling 2 of 2026-10-07 governs

R2 (`PREDICTIONS-…`, 2026-11-19: a new `CF2`/`LR6` value for contract-set allocation, encoded at application) is withdrawn. It was made on operator advice that overlooked ruling 2 of 2026-10-07 (`RULINGS-commenda-pilot-definitional-2026-10-07.md`): "A clause present in a minority of acts does not make a cell `P`. Code the modal state, record the counts in `notes`, and lower `confidence`. Where the minority is a coherent drafting variant, propose a split rather than a `P`." That rule already meets MS's objection to `.NR` (the deeds are not silent): the cell states the modal state, and the notes give each deed's answer. No vocabulary change, no version bump, no `CF2` sweep.

**Left open, as a doctrine question:** ruling 2 has no answer for an exact tie, which forces `.NR` to mean "answered, but tied" as well as "not in the source" (coding notes, answer 5). It does not arise in this row after ruling 1.

R1 (doc. 8's factor bears one quarter of any loss, out of his own goods) stands. The blind coder reached the same reading independently (`CF2` note: "the factor, who puts in no capital, is charged a quarter of the loss").

## Ruling 3. No split now

The row is not split. On three deeds every sub-row would rest on a single deed. Doc. 8 is recorded as a split candidate in the `CF2` and `LR6` notes and in the type row.

## Ruling 4. A split criterion, fixed before any further evidence is read

**Dimension.** Loss allocation to a labour-only factor. Variant A: the capital partners bear the capital loss (`CF2` 0); docs. 3 and 9. Variant B: the factor bears a share of loss equal to his share of profit (`CF2` P); doc. 8.

**The row is split only when all three hold:**
1. each variant has at least three deeds in the row;
2. the minority variant occurs in deeds of more than one notary or office, or of more than one set of principals;
3. the variant goes with at least one other clause difference (for example a death clause, plural principals, or how the factor's share is computed), so that it is a coherent drafting variant and not a single bargain.

If the evidence never meets the threshold, the row stays unsplit and coded under ruling 2 of 2026-10-07. The likely sources of further deeds are the *Catálogo de los fondos americanos del Archivo de Protocolos de Sevilla* regesta (tomos XV and XVI held), read in full in the AHPS or from published transcriptions, and Gutiérrez García 1998 as a pointer.

## Ruling 5. Smaller items, the coder's values accepted

- `LP2` = 0, low: title is registered in the partners' names and declared theirs "por tercias partes"; the coder's alternative (`.NR`) stays in the note.
- `MG2` = `.NR`: control is divided by place (Seville and Lima), which the value set does not fit.
- `TS3` and `CI2` rest on the same recall clauses: declared in both notes as one piece of evidence.
- `references/works.csv` takes a row for Martínez Gijón 1970 at application, before `check_citations.py` is run.

## Ruling 6. The ordering disclosure is accepted

A script run by the coder printed census counts for six characteristics after every value was fixed and before the row file was written (coding notes, disclosures). It is accepted as disclosed and recorded in `logbook/4` with the scoring.
