# Priors — venetian-pass-2026-10-25 (Venetian acts, 14 cells of `societas_maris` and `commenda_alloc`)

**Copy this file to `PRIORS-venetian-pass-filled-<date>.md` and fill the copy before you open any file in `sources/`.** Write what you expect, not what you hope: a prior that turns out wrong is the useful kind. Then print the copy's sha256, give it to MS, and stop. **Do not open any source until MS confirms that the filled copy is committed.**

This chat must not be inside the claude.ai Project of this research programme, and must not read any memory file, vault note or project document. If your context contains any of these, say so in §1 before writing anything else.

- Filled by (model identifier as configured; effort as stated in the kickoff):
- Finished at (UTC):
- Files read before writing this, listed (state explicitly that no file in `sources/` has been opened; a directory listing is allowed and must be declared):
- Skills loaded:

## 1. Exposure, disclosed before any source is opened

1. **Training.** What do you know about the Venetian *colleganza* (*collegantia*) and the commenda in Venice, eleventh to thirteenth century: its terms, its historiography, and any quantitative study? Name the works you recall and what you recall them as finding. Say plainly where the answer is "nothing specific".
2. **This edition.** What do you know about Morozzo della Rocca & Lombardo, *Documenti del commercio veneziano nei secoli XI–XIII* (1940): its contents, its sources, its editorial choices, and any study that has used it and what it found? Do you recall any act of it by number?
3. **Earlier passes.** Do you know anything about earlier codings of these two forms in this census, or about the passes of September 2026 on Genoese and Marseille acts? (You should not. If you do, say from where.)
4. **Leaks the operator knows of.** Disclose how each bears on you:
   - the type name `societas_maris` is "Societas maris (the bilateral commenda; Venetian collegantia)". It equates the Venetian *collegantia* with the bilateral form, and its word "bilateral" collides with `CF3`'s value `bilateral`, which counts principals, not contributors of capital;
   - the type name `commenda_alloc` is "Commenda (loss-allocation aspect)", which states `MC1 = allocation` for that row. Treat `commenda_alloc MC1` as not blind;
   - the census's descriptions of `MC1` and of the loss census may name the commenda among allocation forms. Check what you were given and say whether they do.
5. **Leaks you find.** List any further statement, in the bundle or in a loaded skill, that names or implies a value for a cell in scope. Give its location. Do not use it.

## 2. The edition as a whole, before you read it

You will be given the Latin text of the acts with the editors' regests, archival descriptions and notes removed.

1. Of every 100 acts, how many do you expect to be: contracts placing capital in the hands of a party who trades with it; releases or quittances; loans and sea loans; mandates (*procurae*); attestations; anything else? One sentence on why.
2. Do you expect the terms of the contracts placing capital in a trader's hands to be uniform across the period the edition covers? If not, say what you expect to change, and when.
3. In which kinds of act do you expect the peril of sea and men to be stated, and how often?
4. Do you expect releases to recite the terms of the contract they discharge? Fully, in part, or not at all?

## 3. How you will assign an act to a form

1. Which words, clauses or terms in a Venetian act will make you treat it as evidence for `societas_maris`, and which for `commenda_alloc` (the commenda's loss-allocation aspect)?
2. Do you expect the Venetian word *collegantia* to coincide with the bilateral form? What will you do with an act called *collegantia* that does not fit the bilateral form, and with an act that fits both forms or neither?
3. Will a release be evidence for any of the cells in §4? For which, and on what condition?

## 4. Per-cell expectations

Fill every row. *Evidence* names the kind of act and the clause you expect to carry the value. *Falsifier* names what you would have to read to change your expectation.

| census | type_id          | char_id | allowed values                                                               | expected value | confidence | evidence | falsifier |
| ------ | ---------------- | ------- | ---------------------------------------------------------------------------- | -------------- | ---------- | -------- | --------- |
| orga   | `societas_maris` | `CF1`   | 1 · P · 0                                                                    |                |            |          |           |
| orga   | `societas_maris` | `CF3`   | bilateral · multilateral                                                     |                |            |          |           |
| orga   | `societas_maris` | `CI1`   | common · several-accounts · none                                             |                |            |          |           |
| orga   | `societas_maris` | `LR6`   | symmetric · upside-only · downside-only                                      |                |            |          |           |
| orga   | `societas_maris` | `TS2`   | open · fixed-term · single-venture                                           |                |            |          |           |
| loss   | `commenda_alloc` | `MC1`   | allocation · spreading · pooling                                             |                |            |          |           |
| loss   | `commenda_alloc` | `PR1`   | 1 · P · 0                                                                    |                |            |          |           |
| loss   | `commenda_alloc` | `RB1`   | capital-provider · labour-provider · third-party · shared · all-stakeholders |                |            |          |           |
| loss   | `societas_maris` | `MB3`   | voluntary · compulsory                                                       |                |            |          |           |
| loss   | `societas_maris` | `MC1`   | allocation · spreading · pooling                                             |                |            |          |           |
| loss   | `societas_maris` | `PR1`   | 1 · P · 0                                                                    |                |            |          |           |
| loss   | `societas_maris` | `RB1`   | capital-provider · labour-provider · third-party · shared · all-stakeholders |                |            |          |           |
| loss   | `societas_maris` | `RB2`   | capital-provider · labour-provider · third-party · shared · all-stakeholders |                |            |          |           |
| loss   | `societas_maris` | `RB4`   | 1 · P · 0                                                                    |                |            |          |           |

Missing values are part of the answer: `.NR` (the sources do not address it), `.NA` (not applicable), `.IL` (illegible). Expect `.NR` wherever you expect silence, and say so.

## 5. Row-level expectations

1. How many acts do you expect to code from for each form, and how many of them contracts?
2. Which cells do you expect to come back `.NR`, and why?
3. Which single expectation in §4 are you least sure of?

## After writing

Print the sha256 of the filled copy, give it to MS, and **do not open any source until MS confirms the commit.**
