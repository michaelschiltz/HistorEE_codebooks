# Working on this repo

Coding datasets for *Clearing and Settling the Realm* / HistorEE. `CONTRIBUTING.md` is the coding protocol and `CHARACTER-CODING.md` is the methodological rationale with its literature. These rules govern any assistant work here and take precedence over general instincts about "helpfully" adding structure.

## The standing instruction

**The maintainer is a financial historian, not a specialist in classification theory or phylogenetic systematics.** He has said so explicitly. That places the burden on the assistant: do not make coding-ontology decisions silently and do not assume a methodological consequence will be noticed.

When a request or a coding decision has consequences in that literature, **say so before acting, in plain terms, with the specific failure named.** Examples of things to surface rather than quietly handle:

- a new characteristic that duplicates an existing one, or that is only meaningful conditional on another;
- a characteristic imported from one tradition and applied to others (the *waqf*-shaped `AP4`, `MG4`, `FP4`);
- a request that would license an unweighted similarity or clustering claim;
- a proposed value that conflates uncertainty with partial presence;
- a coding that would launder a source's silence into an asserted absence.

Being right and unhelpful is a failure. Being agreeable and wrong is a worse one. State the objection, give the recommendation, then do what is decided.

## Before adding a characteristic

Discriminating power is free: with enough characteristics **any** two forms separate, so "it lets us tell X from Y" is never a justification. Five tests, in `CHARACTER-CODING.md` with citations:

1. **Well-formedness.** Does an existing characteristic silently ask two questions? If yes, splitting is mandatory — that is a repair, not an embellishment. `LR2`/`LR6` is the worked case.
2. **Ontological dependence.** Is it meaningful only given another's state? Then record it in `applicability_on`; do not treat it as a free dimension.
3. **Comparative-concept hygiene.** Is it defined in terms available to *every* tradition, or borrowed from one? Borrowed categories get flagged in the vocabulary, not silently applied.
4. **Discriminant validity.** Does it ever take a value the existing characteristic does not predict? Unanswerable from the desk. Only forms answer it.
5. **Diversity budget.** Characteristics are paid for in forms.

**Default recommendation in almost every case: add forms, not features.** Two new forms in one session produced two falsifications; no amount of reasoning did.

## Claims, not columns

The matrix serves three purposes with three different constraints. Do not let a rule from one migrate to another — the assistant has already made this mistake once by importing a QCA threshold into a descriptive coding that has no outcome variable.

- **Description.** No budget. More characteristics is strictly better. This is most of what the matrix does.
- **Similarity and distance claims** — clustering, "convergence pair", "A is more like B than C". The ugly duckling theorem binds here and **adding forms does not help**; only a declared weighting does. Never run or endorse an unweighted distance computation over the full characteristic set.

  **The declared weighting already exists**: the `component` and `work_package` columns. WP2 carries the application's five (entity shielding, capital lock-in, transferable claims, legal personality, perpetual succession); WP1 carries four (owner shielding, outcome coupling, loss sharing, risk pooling). Eleven characteristics are `none` in both and are description only. **Any comparative claim must state which set it runs on, and must never run on all 32.** A characteristic marked `none` is `none` because the theory makes no prediction about it; promoting one into a set is a theoretical claim needing the same justification as adding a characteristic, and the set must be fixed before the coding it will be used on rather than assembled afterwards.
- **Configurational or causal inference.** The QCA case-to-condition budget binds here and binds hard. At present *n* this is not available; say so rather than producing it.

## Missing values

`.NR` not recorded · `.IL` illegible · `.NA` not applicable · `0` an observed absence. Conflating these is the fastest way to discredit the dataset.

- **A source that does not address a question yields `.NR`, never `0`.** `bazacle_mill AP1` and `asiento_averia AP1` are both `.NR` because neither source asks whether a member's private creditors could reach the fund. Coding `0` would assert an absence the evidence cannot support.
- **Inapplicability runs backwards.** If a child characteristic is `.NA`, that is evidence about the parent's value. `waqf_khayri LR4` was corrected from `P` to `0` on exactly this reasoning.
- When `value` is `.NA`, propagate `.NA` through `confidence`, `source_ref` and `source_lang`.

## `P` means half-present

`P` is a structural state, not a hedge. Uncertainty belongs in `confidence`; functional analogy belongs in `notes`. **A `P` sitting beside `low` confidence and a note arguing for `0` is almost always a `0`** — that is how the *waqf* pooling error survived.

## Dependence: two relations, never merged

`applicability_on` records whether a cell *exists*. `dependence_group` plus `dependence_scope` record whether it *adds evidence*. Collapsing them into one column repeats the conflation the columns exist to catch.

A dependence asserted on logical grounds is a **hypothesis**. `agent-loss-exposure` was asserted as one degree of freedom and `asiento_averia` separated it on substantive values within a day.

## Coding practice

- **Code from the maintainer's own sources and vault notes where they exist**, not from general knowledge. `asiento_averia` was coded from his Hierro Anibarro notes; `bazacle_mill` from the supplied paper. Where a vault note flags a question as open, the coding inherits `low` confidence and says so.
- **Preserve the source's limits.** Carry `[verify]` flags through rather than resolving them by assertion. Where an author hedges — Le Bris, Goetzmann & Pouget call share standardisation "a preliminary for depersonalization" — the coding does not exceed the hedge.
- **Verify citations before entering them.** Resolve DOIs through CrossRef rather than from memory; mark anything unresolved as unverified in the note. Memory has been wrong in this repo's history.
- **Record disagreement as a coding, not a verdict.** `bazacle_mill FP1=mixed` holds the Harris versus Le Bris/Goetzmann/Pouget dispute open deliberately.

## Attribution

`coder=ai` marks provisional assistant codings pending human verification, and the datapackage description, the `coder` field description and the "PARTLY ASSISTANT-CODED" title all depend on it. **Do not bulk-convert `ai` to initials.** If adoption needs recording, propose an additive `verified_by` column, which preserves who entered a row against who checked it.

## Reserved terminology

Mirrors the vault's rules; the same words appear in `notes` fields.

- **`genetic` is reserved for biological heredity.** Never for the descent of institutions.
- **`convergence` means strict cladistic convergence** — independent arrival from *different* ancestral conditions. Where a shared ancestral condition is plausible, the word is **parallelism**. Le Bris, Goetzmann & Pouget's joint-stock case fails this test on their own evidence.
- **`hazard` and `risk` are not interchangeable, and the secondary literature treats them as if they were.** A **hazard** is a peril conceived as an event that may befall: no distribution over outcomes, not priceable, met by avoidance, sharing or propitiation. A **risk** is a peril conceived as a quantified distribution: priceable, and therefore transferable to a party with no stake in the venture. The movement from the first conception to the second is the semantic shift the project describes, and calling the earlier thing a "risk" makes that shift invisible by naming its endpoint as though it had always obtained. Harris (2023) writes of "maritime risks" and "risk mitigation" for institutions his own Knightian framework places under *uncertainty* — general average above all. **Do not inherit that usage.** Where a characteristic must be neutral as between the two conceptions, name it for the peril: `PR1` is "peril priced ex ante", not "risk priced ex ante".
- **Units are instruments, not populations.** Institutions are transmitted as texts and drafting practices. Never describe a legal tradition as a population with a heritable disposition, and object when a source does.

## Logbook prose style

The `logbook/*.md` files are **soft-wrapped**: one physical line per paragraph, list item and blockquote, with blank lines between blocks. Do not hard-wrap prose at a column width — let the editor wrap. Hard-wrapped entries have had to be re-flowed by hand after the fact. Headings, tables, `---` rules and fenced code are exempt. This is a house-style rule, not a data rule, but it applies to every entry an assistant writes.

## Checks before any PR

```sh
python -m frictionless validate datasets/<dataset>/datapackage.json
python scripts/check_dependence.py [datasets/<dataset>]
python scripts/check_vocabularies.py
python scripts/build_codebook.py --check
python scripts/build_views.py --component <component> --check
```

`frictionless` sees types, enums and keys. It cannot see the vocabulary's `allowed_values`, the dependence columns, or `.NA` propagation — `check_dependence.py` covers the second and third, and a `value`-against-`allowed_values` sweep should be run by hand when adding rows.

Regenerate `codebook.md` via `scripts/build_codebook.py` after any schema change; never hand-edit it. **It also goes stale on data change**, because it publishes row counts and per-field fill counts — it stood at 485 rows against an actual 579 on 2026-08-30. `--check` catches that without writing. The same is true of `views/`, which nothing in CI checks at all. Bump the datapackage `version` and record the decision in `CHANGELOG.md`, including what was *considered and rejected*.

## Safety

- Do not delete or rename files without explicit confirmation.
- Git commits and pushes are the maintainer's, in VSCode. **Do not run `git` from the sandbox** — it cannot write to `.git` and leaves `index.lock` files that block his client.
