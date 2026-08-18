# Codebook — Cooperative organizational forms — feature coding

> **Generated file.** Do *not* edit by hand. Produced by `scripts/build_codebook.py` from `datapackage.json`. Edit the schema and regenerate.

- **Dataset**: `organizational_forms`  
- **Version**: 0.8.0  
- **License**: CC-BY-4.0  
- **Contributors**: Michael Schiltz (maintainer)  
- **Rows**: 282  
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

|  # | Field           | Type   | Required | Coded values                                                                  | Present |
|---:|-----------------|--------|:--------:|-------------------------------------------------------------------------------|--------:|
|  1 | `record_id`     | string |    ✓     |                                                                               | 282/282 |
|  2 | `type_id`       | string |          |                                                                               | 282/282 |
|  3 | `char_id`       | string |          |                                                                               | 282/282 |
|  4 | `value`         | string |          |                                                                               | 243/282 |
|  5 | `confidence`    | string |          | `high`, `medium`, `low`                                                       | 243/282 |
|  6 | `articulation`  | string |          | `articulated`, `analyst-imposed`                                              |  42/282 |
|  7 | `source_ref`    | string |          |                                                                               | 260/282 |
|  8 | `source_lang`   | string |          | `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`, `pl`, `pt` | 211/282 |
|  9 | `coder`         | string |    ✓     |                                                                               | 282/282 |
| 10 | `source_read`   | string |          | `full`, `partial`, `none`, `unknown`                                          | 260/282 |
| 11 | `reviewed_by`   | string |    ✓     |                                                                               | 282/282 |
| 12 | `review_status` | string |          | `unreviewed`, `source-checked`, `coding-checked`, `disputed`                  | 282/282 |
| 13 | `notes`         | string |          |                                                                               | 282/282 |

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


### `articulation` — Articulation

Whether the coded function was articulated by the tradition's own advocates in their own idiom ('articulated'), or is visible only under the analyst's description ('analyst-imposed'). '.NR' where not yet assessed; propagates '.NA' with the value. Implements the methodology's constraint that functional coding be bounded by the sources' vocabulary, so that the two kinds of claim are never aggregated.

- **type** string · **values** `articulated`, `analyst-imposed`


### `source_ref` — Source reference

Short citation supporting the coding, or '[verify]' where the value is asserted pending a pinned reference.

- **type** string


### `source_lang` — Source language

Language of source_ref. ISO 639-1 where a two-letter code exists, otherwise ISO 639-3. 'arc' is used broadly for Aramaic; the Babylonian Talmud is strictly Jewish Babylonian Aramaic (ISO 639-3 'tmr'), and a row citing it carries 'arc' with the distinction noted rather than a separate code.

- **type** string · **values** `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`, `pl`, `pt`


### `coder` — Coder

Initials of the team member who entered the record. 'ai' marks a provisional assistant-generated seed coding pending human verification.

- **type** string · **required**


### `source_read` — Source read

Whether the coder had read source_ref when the cell was entered, or has since. 'full' = read throughout; 'partial' = read the cited passages and their context; 'none' = coded from secondary description without opening the source; 'unknown' = not recorded at coding time. '.NA' where the row has no source. PROCESS METADATA, NOT A CLAIM ABOUT THE SOURCE.

- **type** string · **values** `full`, `partial`, `none`, `unknown`


### `reviewed_by` — Reviewed by

Initials of the team member who has checked this cell, or 'none'. Distinct from 'coder'. Multiple reviewers separated by ';'.

- **type** string · **required**


### `review_status` — Review status

'unreviewed' (default); 'source-checked' = a reviewer read source_ref and confirms the cell against it; 'coding-checked' = a reviewer accepts the reasoning but did not or could not verify against the source, which is the honest state where source_lang lies outside the reviewer's languages; 'disputed' = a reviewer disagrees and resolution is pending.

- **type** string · **values** `unreviewed`, `source-checked`, `coding-checked`, `disputed`


### `notes` — Notes

Free-text coder note: rationale, the school that dissents, caveats, cross-references.

- **type** string

