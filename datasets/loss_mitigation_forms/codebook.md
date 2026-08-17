# Codebook — Loss-mitigation forms — feature coding

> **Generated file.** Do not edit by hand. Produced by `scripts/build_codebook.py` from `datapackage.json`. Edit the schema and regenerate.

- **Dataset**: `loss_mitigation_forms`  
- **Version**: 0.6.0  
- **License**: CC-BY-4.0  
- **Contributors**: Michael Schiltz (maintainer)  
- **Rows**: 524  
- **Generated**: deterministically from `datapackage.json` (timestamps via Git history)


PROVISIONAL / PARTLY ASSISTANT-CODED seed dataset. A morphological coding of arrangements that mitigate loss WITHOUT an entity, sorted by Harris's (2023) three-way distinction: allocation (risk assigned to a named party by contract - sea loan, bottomry, respondentia, commenda), spreading (transferred to third parties for a premium - marine insurance), and pooling (mutualised among stakeholders - general average, averia, ko/mujin, confraternity funds). Harris's own open question - under which conditions risk was spread as opposed to pooled or allocated - is what MC1 is for. Stored long/tidy. Carries the same WP1 component vocabulary as organizational_forms, so the packages join at component level. RULE: a characteristic lives in exactly one dataset; forms suffixed _alloc are cross-references to organizational_forms entries, coded here only on loss-allocation characteristics and never on the entity characteristics coded there. Rows with coder 'ai' are provisional.


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

|  # | Field           | Type   | Required | Coded values                                                                              | Present |
|---:|-----------------|--------|:--------:|-------------------------------------------------------------------------------------------|--------:|
|  1 | `record_id`     | string |    ✓     |                                                                                           | 524/524 |
|  2 | `type_id`       | string |          |                                                                                           | 524/524 |
|  3 | `char_id`       | string |          |                                                                                           | 524/524 |
|  4 | `value`         | string |          |                                                                                           | 358/524 |
|  5 | `confidence`    | string |          | `high`, `medium`, `low`                                                                   | 358/524 |
|  6 | `articulation`  | string |          | `articulated`, `analyst-imposed`                                                          | 137/524 |
|  7 | `source_ref`    | string |          |                                                                                           | 469/524 |
|  8 | `source_lang`   | string |          | `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`, `tr`, `zh`, `pl`, `pt` | 439/524 |
|  9 | `coder`         | string |    ✓     |                                                                                           | 524/524 |
| 10 | `source_read`   | string |          | `full`, `partial`, `none`, `unknown`                                                      | 469/524 |
| 11 | `reviewed_by`   | string |    ✓     |                                                                                           | 524/524 |
| 12 | `review_status` | string |          | `unreviewed`, `source-checked`, `coding-checked`, `disputed`                              | 524/524 |
| 13 | `notes`         | string |          |                                                                                           | 524/524 |

## Variable definitions


### `record_id` — Record ID

Stable unique identifier for the coding. Never reused.

- **type** string · **required** · **unique** · **pattern** `^LM-[0-9]{4}$`


### `type_id` — Pooling form (coded)

Coded pooling arrangement. Controlled vocabulary: vocabularies/cooperative_pooling_type.csv. Not enum-constrained here because the census is still growing (CONTRIBUTING §5).

- **type** string


### `char_id` — Characteristic (coded)

Coded structural characteristic. Controlled vocabulary: vocabularies/cooperative_pooling_characteristic.csv, which also gives each characteristic's value type, allowed values, and WP1 component.

- **type** string


### `value` — Coded state

The characteristic's state for this form. Ternary characteristics: 1 present, P partial, 0 absent. Nominal characteristics: one of that characteristic's allowed categories. Absence (0) is a datum, kept distinct from .NA (inapplicable) and .NR (not yet coded).

- **type** string


### `confidence` — Record confidence

Confidence in the coding. Orthogonal to value.

- **type** string · **values** `high`, `medium`, `low`


### `articulation` — Articulation

Whether the coded function was articulated by the tradition's own advocates in their own idiom ('articulated'), or is visible only under the analyst's description ('analyst-imposed'). '.NR' where not yet assessed; propagates '.NA' with the value. 'articulated' must never rest on a placeholder citation.

- **type** string · **values** `articulated`, `analyst-imposed`


### `source_ref` — Source reference

Short citation supporting the coding, or '[verify]' where the value is asserted pending a pinned reference.

- **type** string


### `source_lang` — Source language

Language of source_ref. ISO 639-1 where a two-letter code exists, otherwise ISO 639-3.

- **type** string · **values** `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`, `tr`, `zh`, `pl`, `pt`


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

