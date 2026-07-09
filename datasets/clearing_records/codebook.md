# Codebook — Clearing and settlement records (illustrative)

> **Generated file.** Do not edit by hand. Produced by `scripts/build_codebook.py` from `datapackage.json`. Edit the schema and regenerate.

- **Dataset**: `clearing_records`  
- **Version**: 0.1.0  
- **License**: CC-BY-4.0  
- **Contributors**: Michael Schiltz (maintainer)  
- **Rows**: 8  
- **Generated**: deterministically from `datapackage.json` (timestamps via Git history)


ILLUSTRATIVE / SYNTHETIC worked example. Tokugawa-period money-changer and remittance settlements, structured to demonstrate the project's coding conventions: transparent unit normalisation across the sanka (gold/silver/copper) system, disaggregated missingness, explicit uncertainty, a source-language layer, and per-observation coder attribution. Not archival data.


## Provenance

Attribution and timestamps are supplied by Git (`git blame` for line-level history); releases are frozen and citable via a Zenodo DOI. Per-observation coder attribution is carried in the `coder` field.


## Missing-value conventions

Absence is coded, never blank. These tokens are treated as missing by the schema (`missingValues`):


| Token | Meaning |
|---|---|
| `.NR` | not recorded in the source |
| `.IL` | present but illegible / damaged |
| `.NA` | not applicable to this record type |

> `.ZERO` is **not** here: a source-recorded zero is the value `0`, a datum, not an absence (see the `missingness` field).


## Variables at a glance

| # | Field | Type | Required | Coded values | Present |
|---:|---|---|:---:|---|---:|
| 1 | `record_id` | string | ✓ |  | 8/8 |
| 2 | `date_wareki` | string |  |  | 8/8 |
| 3 | `date_iso` | string |  |  | 8/8 |
| 4 | `date_confidence` | string |  | `high`, `medium`, `low` | 8/8 |
| 5 | `instrument_wareki` | string |  |  | 8/8 |
| 6 | `instrument_romaji` | string |  |  | 8/8 |
| 7 | `instrument_type` | string |  | `bill_note`, `remittance_bill`, `book_transfer`, `money_exchange` | 8/8 |
| 8 | `amount_original` | number |  |  | 7/8 |
| 9 | `amount_unit` | string |  | `ryo`, `monme`, `kanme`, `mon` | 8/8 |
| 10 | `amount_monme_silver` | number |  |  | 7/8 |
| 11 | `normalization_method` | string |  |  | 7/8 |
| 12 | `missingness` | string |  | `observed`, `not_recorded`, `illegible`, `not_applicable`, `explicit_zero` | 8/8 |
| 13 | `payer` | string |  |  | 8/8 |
| 14 | `payee` | string |  |  | 6/8 |
| 15 | `place_romaji` | string |  |  | 8/8 |
| 16 | `source_ref` | string |  |  | 8/8 |
| 17 | `source_lang` | string |  | `ja`, `nl`, `de`, `fr`, `en` | 8/8 |
| 18 | `confidence` | string |  | `high`, `medium`, `low` | 8/8 |
| 19 | `coder` | string | ✓ |  | 8/8 |
| 20 | `notes` | string |  |  | 8/8 |

## Variable definitions


### `record_id` — Record ID

Stable unique identifier for the settlement record. Never reused.

- **type** string · **required** · **unique** · **pattern** `^CR-[0-9]{4}$`


### `date_wareki` — Date (Japanese era, original)

Date exactly as written in the source, in the Japanese era (wareki) calendar. Preserves the original, including markers of loss or inference (e.g. 欠 'missing', 推定 'inferred').

- **type** string


### `date_iso` — Date (ISO 8601, normalised)

Gregorian/ISO normalisation of date_wareki. Reduced precision (year, or year-month) is expressed by a truncated ISO string when the source does not license a full date.

- **type** string


### `date_confidence` — Date confidence

Confidence in the normalised date.

- **type** string · **values** `high`, `medium`, `low`


### `instrument_wareki` — Instrument (original term)

The instrument as named in the source, in the original script (e.g. 手形, 為替, 振替, 両替).

- **type** string


### `instrument_romaji` — Instrument (romanisation)

Hepburn romanisation of instrument_wareki.

- **type** string


### `instrument_type` — Instrument type (coded)

Controlled code mapping the source term to a project category. Vocabulary: vocabularies/instrument_type.csv. Where a term's referent shifts across periods, the shift is documented in the logbook rather than silently recoded.

- **type** string · **values** `bill_note`, `remittance_bill`, `book_transfer`, `money_exchange`


### `amount_original` — Amount (as written)

The figure as recorded in the source, in its original unit (amount_unit). Missing values use the disaggregated codes (see missingness and missingValues); an explicit source zero is the number 0, not a missing code.

- **type** number


### `amount_unit` — Original unit

Monetary unit of amount_original within the sanka three-currency system.

- **type** string · **values** `ryo`, `monme`, `kanme`, `mon`


### `amount_monme_silver` — Amount (normalised, silver monme)

amount_original normalised to a common unit — silver monme — to make cross-currency records comparable. The conversion applied is named in normalization_method; the choice of common unit and its assumptions are the project's, and are auditable per row.

- **type** number


### `normalization_method` — Normalisation method

The exact conversion applied to reach amount_monme_silver: 'identity_silver' (already silver), a named gold/copper conversion with its rate and source (e.g. 'ryo_to_monme@60_official1700'), or '.NA' where no amount exists to convert.

- **type** string


### `missingness` — Missingness (of amount)

Epistemic status of the amount. Four kinds of absence are never conflated: observed, not_recorded, illegible, not_applicable — plus explicit_zero for a source-recorded nil, which is a value, not an absence.

- **type** string · **values** `observed`, `not_recorded`, `illegible`, `not_applicable`, `explicit_zero`


### `payer` — Payer / remitter

Party debited, as named in the source (romanised). Missing coded per convention.

- **type** string


### `payee` — Payee / beneficiary

Party credited, as named in the source (romanised). Missing coded per convention.

- **type** string


### `place_romaji` — Place

Place of settlement (romanised).

- **type** string


### `source_ref` — Source reference

Archive/series call number and folio, keyed to logbook 5 (quality and nature of sources).

- **type** string


### `source_lang` — Source language

ISO 639-1 language of the source text.

- **type** string · **values** `ja`, `nl`, `de`, `fr`, `en`


### `confidence` — Record confidence

Overall confidence in the coded record. Uncertainty is made an explicit column, not laundered into prose.

- **type** string · **values** `high`, `medium`, `low`


### `coder` — Coder

Initials of the team member who entered the record. The backstop for attribution is git blame; contestable interpretive calls additionally carry an authority note in the logbook.

- **type** string · **required**


### `notes` — Notes

Free-text coder note: rationale, caveats, cross-references.

- **type** string

