# Contributing — the coding manual

This is *not boilerplate*. It is the coding protocol for the project. In a multi-member team the codebook is only  as trustworthy as the discipline behind it, so every contributor reads this before touching data.

## 1. Golden rules

1. **The CSV is canonical.** Never edit data in Excel and paste back — you will silently mangle encodings, dates, and leading zeros. Edit `data.csv` as text, or through a script.
2. **Never hand-edit `codebook.md`.** It is generated. Edit `datapackage.json` and run `python scripts/build_codebook.py`.
3. **Each dataset is its own package.** Distinct corpora (different period, region, or source type — e.g. medieval Japanese registers vs. early modern Armenian ledgers) get their own folder under `datasets/`, each with its own `datapackage.json`, `data.csv`, and generated `codebook.md`. Do not merge unrelated corpora into one schema just because they share this repo; `build_codebook.py` regenerates every dataset folder it finds, so adding a new one is just adding a new folder. Start from `datasets/_template/` (§3) rather than copying an existing dataset — a real corpus carries fields specific to it that a new one should not inherit by accident.
4. **No blank cells.** Absence is coded, never empty. See §4.
5. **One decision, one commit.** Commit messages record *why*, not just *what*.
6. **Sign your commits** (`git commit -S`). Attribution must be cryptographic, not merely a name string.

## 2. Roles and attribution

Contributors and roles are declared in `CITATION.cff`. Every observation carries a `coder` field naming the person who entered it. Interpretive decisions that are contestable additionally carry an `authority` note in the codebook. `git blame` is the backstop: it shows who changed which line, when, in which commit.

| Role       | Responsibility                                                  |
|------------|-----------------------------------------------------------------|
| Maintainer | Owns the schema; approves merges to `main`; cuts releases.      |
| Coder      | Enters and normalises data; documents decisions in the logbook. |
| Reviewer   | Second pair of eyes on every PR touching data or schema.        |

## 3. The workflow

1. Branch from `main` (`git switch -c coding/<dataset>-<yourname>`).
2. **New dataset?** Scaffold it from the template rather than writing
   `datapackage.json` from scratch:

   ```sh
   cp -r datasets/_template datasets/<dataset_name>
   ```

   Fill in every `REPLACE_...` placeholder, and keep or delete each `TEMPLATE —` field depending on whether that pattern applies (full instructions in `datasets/_template/README.md`). The mandatory fields — `record_id`, `source_ref`, `source_lang`, `confidence`, `coder`,
   `notes` — are not optional patterns; every dataset carries them. For reference, here is an excerpt of the template showing the two kinds of field (the real, validated version lives at `datasets/_template/datapackage.json` — treat this as illustration, not the source of truth):

   ```jsonc
   {
     "schema": {
       "fields": [
         // mandatory — every dataset keeps this as-is
         { "name": "coder", "type": "string", "title": "Coder",
           "constraints": { "required": true } },

         // optional pattern — keep only if this dataset has monetary
         // amounts; rename example_amount_original -> amount_original, etc.
         { "name": "example_amount_original", "type": "number",
           "title": "TEMPLATE — Amount (as written)",
           "description": "OPTIONAL PATTERN, delete if not applicable — ..." }
       ]
     }
   }
   ```

3. Make changes. Regenerate the codebook if you touched the schema: `python scripts/build_codebook.py datasets/<dataset_name>`.
4. Run validation locally: `frictionless validate datasets/<dataset>/datapackage.json`.
5. Open a pull request using the template. CI re-runs validation.
6. A reviewer approves. Only then does it merge to `main`.
7. `main` is protected: no direct pushes, no unreviewed data.

## 4. Coding conventions (the parts referees test)

**Missingness is disaggregated.** Never leave a cell blank. Any field may carry one of three inline tokens, which the schema's `missingValues` treats as missing rather than as a value:

| Token | Meaning                            |
|-------|------------------------------------|
| `.NR` | not recorded in the source         |
| `.IL` | present but illegible / damaged    |
| `.NA` | not applicable to this record type |

Conflating these is the single most common way a historical dataset gets discredited. They are three different epistemic states, and a blank cell tells you none of them.

A fourth state — the source recording an actual zero — is **not** a fourth token. `0` is a datum, and writing a special string for it would make it indistinguishable from the other three. Where a field could plausibly be either a real zero or an unrecorded absence (typically amounts), pair the literal `0` with a companion `missingness` field (the `example_missingness` pattern in the template) coded `observed` / `not_recorded` / `illegible` / `not_applicable` / `explicit_zero`. `clearing_records` shows both mechanisms in the same two rows — inline tokens on `amount_original` and `payee`, and the field pair on a real zero:

```csv
record_id,amount_original,amount_unit,missingness,payee,notes
CR-0004,.IL,monme,illegible,.NR,Amount illegible (water damage); counterparty not recorded in source.
CR-0006,0,monme,explicit_zero,Kōnoike-ya,Source records a nil settlement (offsetting entry) — a real zero, not missing.
```

**Uncertainty is explicit.** The `confidence` field is coded `high` / `medium`/ `low`, defined in the codebook. Do not launder uncertainty into prose.

**Units are normalised transparently.** Any monetary amount carries both its original figure/unit *and* a normalised value, with the `normalization_method` naming the conversion applied. For Tokugawa material this means the *sanka* (三貨) gold/silver/copper problem is made auditable per row, not buried in a footnote:

```csv
record_id,amount_original,amount_unit,amount_monme_silver,normalization_method,confidence,notes
CR-0001,120,monme,120,identity_silver,high,Silver-denominated; no conversion needed.
CR-0002,15,ryo,900,ryo_to_monme@60_official1700,medium,Gold ryō remittance at the official 60-monme rate.
CR-0003,15,ryo,915,ryo_to_monme@61_market_est,low,Same transaction at an estimated market rate — retained to show sensitivity.
```

`normalization_method` names the exact rate and its vintage, so a reader can trace the number back to a decision rather than a black box. Where a rate is contested, keep both conversions as separate rows (as above) instead of silently picking a winner — the discarded alternative stays auditable, just flagged with lower `confidence`.

**Source language is preserved.** Original term, romanisation, and gloss are kept as separate fields. Where a term's referent shifts across periods, record the shift in the logbook rather than smoothing it over.

**Controlled vocabularies are documentation, not enforcement.** `vocabularies/*.csv` explains what each coded value means and where its definition or rate comes from; the `enum` constraint that `frictionless validate` actually checks against `data.csv` lives in `datapackage.json`, as a hand-maintained duplicate of the vocabulary's `code` column. Adding or renaming a code means editing both files — validation will not catch a vocabulary and schema that have drifted apart.

## 5. Extending the schema

Schema growth is **additive**. Add a field; do not repurpose an existing one.
Bump the data-package `version` (semantic versioning) and record the change in `CHANGELOG.md`. Additive change never breaks a downstream consumer.
