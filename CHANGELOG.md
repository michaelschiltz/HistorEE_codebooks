# Changelog

All notable, dataset-level changes are recorded here. This is the human-readable
companion to the Git history: Git records every line change, this records the
decisions that matter to a data *consumer*. Format follows
[Keep a Changelog](https://keepachangelog.com/); versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

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
