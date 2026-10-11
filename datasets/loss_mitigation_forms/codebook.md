# Codebook — Loss-mitigation forms — feature coding

> **Generated file.** Do not edit by hand. Produced by `scripts/build_codebook.py` from `datapackage.json`. Edit the schema and regenerate.

- **Dataset**: `loss_mitigation_forms`  
- **Version**: 0.9.0  
- **License**: CC-BY-4.0  
- **Contributors**: Michael Schiltz (maintainer)  
- **Rows**: 761  
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

|  # | Field           | Type   | Required | Coded values                                                                                    | Present |
|---:|-----------------|--------|:--------:|-------------------------------------------------------------------------------------------------|--------:|
|  1 | `record_id`     | string |    ✓     |                                                                                                 | 761/761 |
|  2 | `type_id`       | string |          |                                                                                                 | 761/761 |
|  3 | `char_id`       | string |          |                                                                                                 | 761/761 |
|  4 | `value`         | string |          |                                                                                                 | 489/761 |
|  5 | `confidence`    | string |          | `high`, `medium`, `low`                                                                         | 489/761 |
|  6 | `articulation`  | string |          | `articulated`, `analyst-imposed`                                                                | 181/761 |
|  7 | `source_ref`    | string |          |                                                                                                 | 687/761 |
|  8 | `source_lang`   | string |          | `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`, `tr`, `zh`, `pl`, `pt`, `ca` | 657/761 |
|  9 | `coder`         | string |    ✓     |                                                                                                 | 761/761 |
| 10 | `source_read`   | string |          | `full`, `partial`, `none`, `unknown`                                                            | 687/761 |
| 11 | `reviewed_by`   | string |    ✓     |                                                                                                 | 761/761 |
| 12 | `review_status` | string |          | `unreviewed`, `source-checked`, `coding-checked`, `disputed`                                    | 761/761 |
| 13 | `notes`         | string |          |                                                                                                 | 761/761 |
| 14 | `coder_model`   | string |          |                                                                                                 | 761/761 |
| 15 | `coder_effort`  | string |          | `low`, `medium`, `high`, `xhigh`, `max`                                                         | 761/761 |

## Variable definitions


### `record_id` — Record ID

Stable unique identifier for the coding. Never reused.

- **type** string · **required** · **unique** · **pattern** `^LM-[0-9]{4}$`


### `type_id` — Loss-mitigation form (coded)

Coded loss-mitigation arrangement. Controlled vocabulary: vocabularies/loss_mitigation_type.csv. Not enum-constrained here because the census is still growing (CONTRIBUTING §5).

- **type** string


### `char_id` — Characteristic (coded)

Coded structural characteristic. Controlled vocabulary: vocabularies/loss_mitigation_characteristic.csv, which also gives each characteristic's value type, allowed values, and WP1 component.

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

Language of source_ref. ISO 639-1 where a two-letter code exists, otherwise ISO 639-3. 'ca' (Catalan) added 2026-10-11 for the Llibre del Consolat de Mar read in Catalan; the field records the language of the passage the coding rests on, so a cell resting on a Castilian study of a Catalan text stays 'es'. Scripts are not languages and are not recorded here.

- **type** string · **values** `ja`, `nl`, `de`, `fr`, `en`, `es`, `he`, `arc`, `ar`, `la`, `it`, `tr`, `zh`, `pl`, `pt`, `ca`


### `coder` — Coder

Initials of the team member who entered the record. 'ai' marks a provisional assistant-generated seed coding pending human verification. The model and effort setting of an 'ai' coding are carried in `coder_model` and `coder_effort`.

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


### `coder_model` — Coder model

Identifier of the AI model that produced the value currently in this row, where `coder` is 'ai' (e.g. `claude-opus-5`); `.NA` where the coder is a person; `.NR` where not recorded. Back-filled on 2026-09-26 for every row then in the census, on the maintainer's statement that all cells to that date were coded by Claude Opus 5 at effort 'high' (logbook 1, 2026-09-26). When an adjudicated re-coding replaces a value, this field changes with it; the superseded coding survives in `recodings.csv`.

- **type** string · **pattern** `^[a-z0-9][a-z0-9.-]*$`


### `coder_effort` — Coder effort

Named effort (reasoning-budget) setting under which `coder_model` produced this row's value; `.NA` where the coder is a person; `.NR` where not recorded. Named levels are not comparable across models: 'high' on one model is not the same budget as 'high' on another, so compare codings by the pair (`coder_model`, `coder_effort`), never by this field alone.

- **type** string · **values** `low`, `medium`, `high`, `xhigh`, `max`

