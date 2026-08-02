# Codebook — Cooperative organizational forms — feature coding

> **Generated file.** Do not edit by hand. Produced by `scripts/build_codebook.py` from `datapackage.json`. Edit the schema and regenerate.

- **Dataset**: `organizational_forms`  
- **Version**: 0.2.0  
- **License**: CC-BY-4.0  
- **Contributors**: Michael Schiltz (maintainer)  
- **Rows**: 87  
- **Generated**: deterministically from `datapackage.json` (timestamps via Git history)


PROVISIONAL / PARTLY ASSISTANT-CODED seed dataset. A morphological (Zwicky) coding of cooperative and risk-pooling organizational forms (waqf, ie, compagnia, joint-stock corporation, nación, natie, kabu-nakama, and forms to be added) against a granular set of structural characteristics. Stored long/tidy: one row per form × characteristic. Supports the comparative typology in Clearing and Settling the Realm / HistorEE. Codes for forms and characteristics live in vocabularies/organizational_form_type.csv and vocabularies/organizational_form_characteristic.csv. Rows with coder 'ai' are provisional seed codings pending human verification; source_ref '[verify]' marks a coded value whose citation is not yet pinned.


## Provenance

Attribution and timestamps are supplied by Git (`git blame` for line-level history); releases are frozen and citable via a FigShare and Zenodo DOI. Per-observation coder attribution is carried in the `coder` field.


## Missing-value conventions

Absence is coded, never blank. These tokens are treated as missing by the schema (`missingValues`):

| Token | Meaning                            |
|-------|------------------------------------|
| `.NR` | not recorded in the source         |
| `.IL` | present but illegible / damaged    |
| `.NA` | not applicable to this record type |

> `.ZERO` is **not** here: a source-recorded zero is the value `0`, a datum, not an absence (see the `missingness` field).


## Variables at a glance

| # | Field         | Type   | Required | Coded values                                                      | Present |
|--:|---------------|--------|:--------:|-------------------------------------------------------------------|--------:|
| 1 | `record_id`   | string |    ✓     |                                                                   |   87/87 |
| 2 | `type_id`     | string |          |                                                                   |   87/87 |
| 3 | `char_id`     | string |          |                                                                   |   87/87 |
| 4 | `value`       | string |          |                                                                   |   75/87 |
| 5 | `confidence`  | string |          | `high`, `medium`, `low`                                           |   75/87 |
| 6 | `source_ref`  | string |          |                                                                   |   75/87 |
| 7 | `source_lang` | string |          | `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it` |   40/87 |
| 8 | `coder`       | string |    ✓     |                                                                   |   87/87 |
| 9 | `notes`       | string |          |                                                                   |   87/87 |

## Variable definitions


### `record_id` — Record ID

Stable unique identifier for the coding. Never reused.

- **type** string · **required** · **unique** · **pattern** `^OF-[0-9]{4}$`


### `type_id` — Organizational form (coded)

Coded organizational form. Controlled vocabulary: vocabularies/organizational_form_type.csv. Not enum-constrained here because the form census is still growing (CONTRIBUTING §5); enforcement can be added once it stabilises.

- **type** string


### `char_id` — Characteristic (coded)

Coded structural characteristic. Controlled vocabulary: vocabularies/organizational_form_characteristic.csv, which also gives each characteristic's value type and allowed values.

- **type** string


### `value` — Coded state

The characteristic's state for this form. Ternary characteristics: 1 present, P partial, 0 absent. Nominal/ordinal characteristics: one of that characteristic's allowed categories (see vocabulary). Absence (0) is a datum, kept distinct from .NA (characteristic does not apply to this form) and .NR (not yet coded). Because admissible values are per-characteristic, this field is not enum-constrained.

- **type** string


### `confidence` — Record confidence

Confidence in the coding. Orthogonal to value: a contested coding is low even where value is 1 (present). Uncertainty is an explicit column, not prose.

- **type** string · **values** `high`, `medium`, `low`


### `source_ref` — Source reference

Short citation supporting the coding, or '[verify]' where the value is asserted pending a pinned reference.

- **type** string


### `source_lang` — Source language

Language of source_ref. ISO 639-1 where a two-letter code exists, otherwise ISO 639-3. 'arc' is used broadly for Aramaic; the Babylonian Talmud is strictly Jewish Babylonian Aramaic (ISO 639-3 'tmr'), and a row citing it carries 'arc' with the distinction noted rather than a separate code.

- **type** string · **values** `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`


### `coder` — Coder

Initials of the team member who entered the record. 'ai' marks a provisional assistant-generated seed coding pending human verification.

- **type** string · **required**


### `notes` — Notes

Free-text coder note: rationale, the school that dissents, caveats, cross-references.

- **type** string

