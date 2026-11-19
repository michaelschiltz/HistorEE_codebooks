# Ruling: a tie across a form's instances (2026-11-19)

**Ruled by MS in chat on 2026-11-19, on the operator's recommendation, choosing the first of four options put to him. Recorded by the assistant (`claude-opus-5-5`). No schema, vocabulary or data change: no cell in either census is tied.**

## The question

Ruling 2 of 2026-10-07 (`records/RULINGS-commenda-pilot-definitional-2026-10-07.md`) codes heterogeneity across a form's instances at the modal state, with the counts in `notes`, confidence lowered, and a split proposed where the minority is a coherent drafting variant. It has no answer where there is no modal state. The blind coder of `compania_factoria_sevilla` met two such cells (`CF1` and `CF3`, 2:2 across four deeds) and coded them `.NR`, stating the tie (`records/NOTES-compania-sevilla-coding-2026-11-19.md`, conventions 4 and answer 5). `.NR` means "not recorded in the source" (`CONTRIBUTING.md` §4); deeds that state their terms and disagree are the opposite of silence. Both ties dissolved when doc. 2 was ruled out of scope (`records/RULINGS-compania-sevilla-2026-11-19.md`, ruling 1), so the question has no live instance. A sweep of the notes of `organizational_forms` and `loss_mitigation_forms` on 2026-11-19 found no other tied cell.

## The options put

1. A new missing token for a tie, ruled now and added to the schema with the first batch that meets one (recommended).
2. The same token added now, before any instance: `missingValues` in every datapackage, `CONTRIBUTING.md` §4 and seven scripts, with a version bump.
3. `.NR` kept, with a mandatory `TIED k:k` prefix in `notes`, checkable by script; `.NR` would keep two meanings.
4. A fixed tie-break (for example the state that claims less); arbitrary on unordered value sets.

**Grounds for the recommendation.** It meets the objection to `.NR` for deeds that answer, and it follows the precedent that no value enters a vocabulary until a form gives it an instance (ruling 3 of 2026-10-07 on `CI1`; the `AP4` lesson).

## The ruling

1. **A tie is answered, not silent.** Where the instances of a form that answer a cell have no single modal state (2:2, 2:2:1, 1:1), the cell takes a new missing token, `.TI` (tied across instances). Its `confidence` and `articulation` carry `.TI` as `.NR` and `.NA` do, and `notes` give each instance's state with its locator.
2. **Before a tie is coded, the split criterion is tested.** A tie is the strongest sign that a row aggregates two drafting variants. Where a split criterion has been fixed for the row, or the tied states co-vary with another clause across the same instances, the split is proposed in place of `.TI`, under ruling 2 of 2026-10-07.
3. **The token enters the schema with the first batch that needs it**, schema first: the batch adds `.TI` to `missingValues` in every datapackage, to the table in `CONTRIBUTING.md` §4 and to the scripts that read the missing tokens (`apply-fragment.py`, `build_codebook.py`, `build_views.py`, `check_citations.py`, `check_counts.py`, `check_dependence.py`, `check_vocabularies.py`), ahead of its rows, with a version bump. Until then a blind coder who meets a tie writes `.TI` in the proposed rows and reports it under answer 4.

## Two points of wording, the operator's, for MS to confirm

- **What is counted.** The tally runs over the instances that answer the cell. An instance silent on it is not a state and does not count toward a tie; if no instance answers, the cell is `.NR`.
- **Dependent cells.** A cell whose applicability turns on a tied antecedent is coded where every tied state gives it the same applicability, as the Seville coder reasoned for `CF1` (both 1 and `P` place a labour-supplying party, so the locator of `AP3`, `LR1` and `CF2` holds). Where the tied states give different applicability, the dependent cell is `.TI` too.
