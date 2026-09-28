# `OF-0744`'s `AP2` note is now false — flagged, not repaired, 2026-09-07

**Not applied.** The maintainer's licence for the 2026-09-07 (ii) batch lifted the `data.csv` prohibition for five rows — `OF-0711`, `OF-0712`, `OF-0713`, `OF-0714`, `OF-0723` — "and nothing else". `OF-0744` is not among them, so this is written down and left.

## The defect

`OF-0744` is `compagnie_antwerpen_1582 AP2 = P`. Its note ends:

> WELL-FORMEDNESS FLAG, RAISED AND NOT REPAIRED: AP2 asks two questions and this batch separates them; see proposed-of/PATCH-AP2-well-formedness-2026-09-05.md and the deed_of_settlement_company AP2 note. Both that row and this one read P and the two P's are not the same state, so they are not agreement.

**`deed_of_settlement_company AP2` no longer reads `P`.** It was re-coded `P` → `.NR` on 2026-09-07 (ii). The final sentence is therefore false in both halves: the two rows do not both read `P`, and there is no longer a collision to warn a consumer about.

The same sentence appears in the `CHANGELOG.md` block for 2026-09-05, where it **has** been corrected in place, that file being inside the batch's scope.

## What the repair should say, and what it must not

The **flag** is untouched by the re-coding and must survive it. `AP2`'s two limbs are still two questions in one column, and `compagnie_antwerpen_1582` is still the row that shows them coming apart — creditors could not force partition (cap. 52 art. 5–6), while a partner's untimely renunciation dissolved the society and so let a member force the partition his own creditors could not. That is the whole of the well-formedness argument and it never needed a second row.

What changes is only the **corroboration claim**. Suggested replacement for the final sentence:

> Both that row and this one read `P` when this note was written, and the two `P`s were not the same state, so they were never agreement. *(Updated 2026-09-07 (ii): `deed_of_settlement_company AP2` has since been re-coded `P` → `.NR`, the blind pass finding the creditor limb never asked of that form. The collision is gone and this row now carries the `P` alone; the well-formedness problem is unaffected, and if anything the re-coding strengthens it — a source can be rich on `AP2` and yield nothing on `AP2`'s increment.)*

**Do not delete the sentence.** It records what the 2026-09-05 batch found, and the census's practice is to correct in place with the correction marked rather than to rewrite history.

## Consequence for the signature tables

`deed_of_settlement_company` has left the entity-shielding signature `(AP1=1, AP2=P, AP4=.NA)` for `(1, .NR, .NA)`, which no form occupies. `compagnie_antwerpen_1582` now holds `(1, P, .NA)` alone. Any prose anywhere that treats those two rows as sharing an entity-shielding signature is stale; a grep for `compagnie_antwerpen_1582` across `logbook/` and `proposed-of/` should be run before the next batch that touches either row.
