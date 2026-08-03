# Changelog

All notable, dataset-level changes are recorded here. This is the human-readable
companion to the Git history: Git records every line change, this records the
decisions that matter to a data *consumer*. Format follows
[Keep a Changelog](https://keepachangelog.com/); versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- `isqa` to `vocabularies/organizational_form_type.csv`, and a full 31-characteristic coding of it (`OF-0037`–`OF-0067`). The Jewish investment partnership of BT *Bava Metzia* 104b, whose *pelga milveh u-pelga pikkadon* (half loan, half bailment) structure makes it the **unshielded** member of the Mediterranean partnership triad: `CF2` (agent bears capital loss) is `1` and `AP3` (owner shielding) is `0`, inverting both cells relative to *qirād* and *commenda*. `CI1` codes `several-accounts`, which the bifurcated stake fits better than any other form yet in the matrix.
- Contrast codings for `qirad` (`OF-0068`–`OF-0077`) and `commenda` (`OF-0078`–`OF-0087`) across the contractual-form and liability facets. Added because a discriminating cell is unreadable without its comparators: `CF2 = 1` for the *ʿisqa* asserts nothing unless the forms it is being contrasted with are coded on the same characteristic. These rows exist to make the contrast legible in the data rather than only in prose.

- `LR6 coupling symmetry` to `vocabularies/organizational_form_characteristic.csv` (`symmetric|upside-only|downside-only`), coded for `isqa`, `qirad`, `commenda` and `waqf_khayri` (`OF-0088`–`OF-0091`). **`LR2` records whether the decision-maker is bound to outcomes; `LR6` records which way.** The gap surfaced during the *ʿisqa* coding: `LR2` returned `coupled` for all three partnership forms, flattening the difference between an agent holding a call option bounded below at zero (*qirād*, *commenda*) and one holding a debt that can carry him past it (*ʿisqa*). The distinction survived only by accident, in `CF2`. Since asymmetric exposure is what the project's ergodicity argument turns on, a feature space that cannot express it was under-specified rather than merely incomplete.

- `articulation` field on `organizational_forms` (v0.6.0), recording per cell whether the coded function was **articulated by the tradition's own advocates in their own idiom** (`articulated`) or is visible only under the analyst's description (`analyst-imposed`), with `.NR` where not yet assessed and `.NA` propagated with the value. This implements a methodological safeguard the application already promises — that functional coding be bounded by the sources' vocabulary — which until now lived only informally in `notes`. It is what makes *al-ghunm bi'l-ghurm* or *sekharo ke-poʿel batel* evidence rather than illustration.

  **Populating it caught an error in the first pass.** Twenty-two cells were initially marked `articulated`, six of which rested only on Udovitch — a modern secondary work. But `articulated` asserts that *the tradition said it*, not that a scholar reports it. `isqa AP3`, `isqa LR1`, `qirad AP3`, `qirad CF2`, `qirad LR3` and `commenda CF2` were downgraded to `.NR`. The sixteen retained each name a primary text (BT *Bava Metzia* 104b), a doctrinal term in the tradition's own vocabulary (*taʿbīd*, *shurūṭ al-wāqif*), or a secondary work quoting the clause verbatim (Hierro Anibarro on *"no han de estar obligados en mancomun"*). Current distribution: 16 `articulated`, 17 `.NA`, 122 `.NR`.

  **Recoverable:** the *qirāḍ* downgrades should return as `articulated` once re-coded with *al-ghunm bi'l-ghurm* as `source_ref` — the maxim is the tradition articulating loss-coupling in its own idiom, and would make `qirad` the worked demonstration that the safeguard operates.

- `check_articulation` in `scripts/check_dependence.py`, enforcing the weakest form of the rule: `articulated` cannot sit beside a `[verify]` citation, since a placeholder cannot evidence what a tradition said. Non-zero exit on violation, alongside the applicability check.

### Considered and rejected

- **Adding `articulation` to `clearing_records`.** Rejected: that dataset records transactions — dates, instruments, amounts, counterparties — not functional attributions, so the question "did the actors articulate this function?" does not arise for a coding that says a document is a *tegata*. Note also that `clearing_records` already implements the descriptive-category/comparative-concept distinction **by field design**, keeping `instrument_wareki` (the tradition's own term) beside `instrument_type` (the analyst's category). `organizational_forms` needed an explicit column precisely because its coding is functional attribution rather than term translation. The Methodology's phrasing — "the *functional* coding is constrained by the sources' own vocabulary" — is therefore correctly scoped as it stands and needs no widening.

### Added

- `component` and `work_package` columns on `vocabularies/organizational_form_characteristic.csv`, mapping each characteristic to the application's declared component framework. **WP2 / Objective 2** takes the five components as they stand in the application — entity shielding, capital lock-in, transferable claims, legal personality, perpetual succession — across 13 characteristics. **WP1 / Objective 1** is given a parallel four-component set *proposed here and not yet in the application*: owner shielding (`AP3`,`LR1`), outcome coupling (`LR2`,`LR6`), loss sharing (`LR3`,`CF2`), risk pooling (`LR4`,`LR5`). Eleven characteristics are `none` in both — description carrying no theoretical load.

  **Why WP1 needed its own set.** Mapping the five alone left 19 of 32 characteristics unassigned, including the whole liability-risk and contractual-form facets — that is, every result the matrix has produced. `AP3` owner shielding mapped to nothing, because the five define *what makes a corporation* (Hansmann–Kraakman–Squire) while the project's mechanism is *whether an agent's trajectory can reach zero*. Those come apart exactly at owner shielding: entity shielding protects the fund, owner shielding protects the member's path. The omission of owner shielding from the five is deliberate and defensible for the corporation definition (limited liability was late and plural, per Harris 2020) but leaves the ergodicity mechanism with no coded expression. Two component sets, one per work package, resolves it without disturbing the application's five.

  **The unifying formulation:** the two sets are one mechanism applied to two units. Owner shielding removes the absorbing barrier from the individual's trajectory; entity shielding, capital lock-in and perpetual succession remove it from the entity's. This predicts a trade-off — devices that protect the entity can trap the member — and `CI3` transferable claims is the hinge that resolves it, letting the member exit by sale where lock-in forbids withdrawal. `waqf_khayri` has maximal entity continuity with `CI3=0`; `bazacle_mill` has entity continuity *with* `CI3=1` from the twelfth century.

- `bazacle_mill` coded across all 32 characteristics (`OF-0124`–`OF-0155`), from Le Bris, Goetzmann & Pouget (NBER WP 31821) and Sicard (1953/2015). Coded specifically to convert the Harris versus Le Bris/Goetzmann/Pouget dispute from duelling prose lists into matrix facts. Three cells carry the argument: **`CI3=1`** — pariers could alienate without the consent of the others, and the 1182 Castel enfeoffment already schedules transaction tax on halves, thirds and quarters, so Harris's "shares were not traded in impersonal stock exchanges" concedes the structural question and objects to the venue; **`CI2=P`** — the mills invert the joint-stock pattern, accumulating capital by call with forfeiture rather than by locked-in subscription, which is a real structural difference and the strongest thing in Harris's favour; **`FP1=mixed`** — deliberately unresolved, because Harris reads community provision and the others read profit-seeking, and this single cell carries much of the disagreement. `LP1=1` records personality as *inherited* from `universitas` without state approbation, which is where the parallelism-not-convergence argument bites.
- `asiento_averia` coded across all 32 characteristics (`OF-0092`–`OF-0123`), from the vault reading of Hierro Anibarro 2005 rather than from general knowledge. Preserves that article's own limits: `AP1` is **`.NR`, not `0`** — Hierro Anibarro never asks whether a *partícipe*'s private creditors could reach the *arca* (the word *acreedor* does not occur in the text), so coding an absence would assert more than the source supports. `CI3` and `CI4` are `P` pending Sayous (1902) on the extent of *transmisión de las participaciones*. `LR5=synchronising` is coded `low` because the vault note flags where this sits on the determinate–contingent typology as an open question.
- `scripts/check_dependence.py`: validates the dependence columns against the codings. Enforces applicability (non-zero exit), reports redundancy without enforcing.

- Three columns to `vocabularies/organizational_form_characteristic.csv` recording **character dependence**, which the matrix previously left implicit:
  - `applicability_on` — the characteristic whose value gates whether this one applies at all (`LR5` on `LR4`, `LR6` on `LR2`, `CF2` on `CF1`, `MG3` on `MG1`).
  - `dependence_group` — characteristics encoding the *same underlying fact*: `agent-loss-exposure` (`AP3`,`LR1`,`CF2`,`LR6`), `legal-personhood`, `capital-immobility`, `duration`, `interest-alienability`, `pooling`.
  - `dependence_scope` — `always` where the members always collapse, `conditional` where they collapse only within a class of forms.

  These are two different relations and were deliberately not merged into one column: applicability is about whether a cell exists, redundancy is about whether it adds evidence. **The motivating problem:** the *ʿisqa*/*qirāḍ* contrast appears in four cells (`AP3=0`, `LR1=unlimited-several`, `CF2=1`, `LR6=symmetric`) but is one fact — the manager is a debtor on the loan half — recorded four times. Treating those as four independent characters quadruple-counts a single datum, the character-non-independence objection any referee with phylogenetic training will raise.

  **`agent-loss-exposure` was asserted with scope `conditional` and coding `asiento_averia` immediately tested it.** `LR1=limited` now occurs with `LR6=symmetric` (the *partícipe*, capped in both directions) *and* with `LR6=upside-only` (the *qirāḍ* agent, holding a call); `AP3=1` splits the same way. Both separations rest on substantive values, not on `.NA`. So limited liability does not determine the direction of exposure: the group collapses within bilateral capital-labour contracts, as claimed, and demonstrably not outside them. The *ʿisqa*/*qirāḍ* contrast still rests on one degree of freedom; the group as a whole does not.

### Changed

- `organizational_forms` to v0.4.0: characteristic vocabulary gains the three dependence columns. No `data.csv` row changes meaning; the 32-characteristic set is unchanged.
- `organizational_forms` to v0.3.0: characteristic set grown from 31 to 32 with `LR6`. Consumers computing per-form completeness should note the changed denominator; `waqf_khayri` and `isqa` remain fully coded at 32/32.
- `organizational_forms` schema to v0.2.0: `source_lang` enum extended from `ja|nl|de|fr|en|es` with `he`, `arc`, `ar`, `la`, `it`. The dataset codes Islamic, Jewish and Latin-Christian forms but could not cite any of them in their own language, forcing every primary locus through an English secondary work or through `.NR` — the precise conflation of "not recorded" with "not representable" that CONTRIBUTING §4 warns against. `arc` is used broadly for Aramaic; the Babylonian Talmud is strictly Jewish Babylonian Aramaic (ISO 639-3 `tmr`), and the field description records the distinction rather than multiplying codes. Additive, so no existing row changes meaning.

### Notes for verification

- **Inconsistency surfaced by the new dependence columns, now resolved — `waqf_khayri` `LR4` recoded `P` → `0` (`OF-0019`, confidence `low` → `medium`, `source_ref` `[verify]` → Kuran 2011).** The form has no members and mutualizes nothing: the corpus absorbs risk and transfers income to an indefinite beneficiary class that contributes nothing and bears no share of another's loss. That is third-party absorption, not pooling. The decisive evidence was `LR5` being inapplicable — if the waqf pooled even partially there would be baskets whose correlation `LR5` could report, and there are none, so **the child's inapplicability is evidence about the parent rather than an anomaly beside it.** The discarded `P` was carrying Kuran's claim that waqf provision substituted for what became social insurance elsewhere: a claim about function, now recorded in `notes` rather than in a structural value.
- **Coding discipline this establishes:** `P` means the characteristic is genuinely half-present. Uncertainty belongs in `confidence`, functional analogy in `notes`. A `P` sitting beside a `low` confidence and a note arguing for `0` is almost always a `0`.
- **Consequence to watch:** with `waqf_khayri` recoded, the `pooling` group now has **zero variance** across all four coded forms (`LR4=0`, `LR5=.NA` throughout) and carries no information. This is a property of which forms are coded, not a defect in the characteristics — `asiento_averia`, general average and `ko_mujin` are genuine pooling vehicles and would break it immediately. Until one is coded, no claim should rest on the pooling facet.
- Within the `agent-loss-exposure` group the four characteristics are **perfectly collinear across all four forms coded** — no form yet breaks the pattern, consistent with their being one degree of freedom. Other groups show apparent collinearity across only two forms, which is not evidence: any two characteristics look collinear at n=2. `interest-alienability` has zero variance so far (`CI3=CI4=0` for both coded forms) and carries no information until a form with tradable interests is coded.
- All 51 new rows carry `coder=ai` and are provisional. The cells most in need of a human check are `MG4` for the *ʿisqa* (coded `religious` for consistency with `waqf_khayri`, but `private-contract` is defensible and the two carry different claims), `TS3` (coded `P` because the schema's single ternary cannot represent the loan half and deposit half separately — a limitation of the characteristic, not a partial state of the form), and `FP4` (the characteristic's "political authority" does not map cleanly onto a corporate minority community).

- `organizational_forms` dataset (v0.1.0): a morphological (Zwicky) feature-coding of cooperative and risk-pooling organizational forms against a granular characteristic set, stored long/tidy (one row per form × characteristic). Provisional and partly assistant-coded (`coder=ai`, `source_ref=[verify]` where citations are unpinned), pending human verification. Seed content: `waqf_khayri` coded across all characteristics plus illustrative cells for `joint_stock`, `natie`, and `nacion_cofradia`.
- `vocabularies/organizational_form_type.csv` and `vocabularies/organizational_form_characteristic.csv`: controlled vocabularies for the two coded fields (`type_id`, `char_id`). Referenced in prose from the schema; `type_id`/`char_id` are deliberately not yet `enum`-enforced while the form census grows.

## [0.2.0] — 2026-07-23

### Added

- `variant_of` field on `clearing_records`: links an alternate-coding row (a second normalisation kept to show rate sensitivity) to the record it varies, with a self-referencing foreign key enforcing referential integrity. Makes the one-transaction/two-codings relation (CR-0003 → CR-0002) machine-readable rather than carried only in `notes` prose.

### Fixed

- De-padded `datasets/clearing_records/data.csv`. The committed file had been saved with column-alignment whitespace (a Rainbow CSV `Align` left on), which `frictionless validate` rejects: trailing spaces broke the `record_id` pattern and every `enum` constraint, so CI was failing on the illustrative dataset. Per `EDITING-CSV.md`, the committed CSV is unpadded; alignment is a view-time toggle only.

## [0.1.0] — 2026-07-08

### Added

- Initial repository scaffold and governance layer.
- `clearing_records` illustrative dataset (synthetic) demonstrating the schema.
- Provisional schema. Provenance apparatus established from commit one.

Snapshot minted to a FigShare and Zenodo DOI on this, the first tagged release: [Zenodo](https://doi.org/10.5281/zenodo.21341361) · [FigShare](https://doi.org/10.6084/m9.figshare.32947250).
