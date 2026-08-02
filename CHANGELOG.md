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

### Changed

- `organizational_forms` to v0.3.0: characteristic set grown from 31 to 32 with `LR6`. Consumers computing per-form completeness should note the changed denominator; `waqf_khayri` and `isqa` remain fully coded at 32/32.
- `organizational_forms` schema to v0.2.0: `source_lang` enum extended from `ja|nl|de|fr|en|es` with `he`, `arc`, `ar`, `la`, `it`. The dataset codes Islamic, Jewish and Latin-Christian forms but could not cite any of them in their own language, forcing every primary locus through an English secondary work or through `.NR` — the precise conflation of "not recorded" with "not representable" that CONTRIBUTING §4 warns against. `arc` is used broadly for Aramaic; the Babylonian Talmud is strictly Jewish Babylonian Aramaic (ISO 639-3 `tmr`), and the field description records the distinction rather than multiplying codes. Additive, so no existing row changes meaning.

### Notes for verification

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
