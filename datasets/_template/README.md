# Dataset template

Scaffold for a new dataset. Not a dataset itself — `build_codebook.py` skips any folder without a `datapackage.json` it can resolve rows for, but this folder is still prefixed with `_` so it sorts away from real datasets and signals "not data" at a glance.

## Use it

```sh
cp -r datasets/_template datasets/<dataset_name>
```

Then, in the new `datapackage.json`:

1. Replace every `REPLACE_...` placeholder (name, title, description,contributors, `created`, the `record_id` pattern prefix).
2. Decide which `TEMPLATE —` fields apply and delete the rest:
   - **Amount normalisation** (`example_amount_*`) — keep only if this dataset records monetary amounts (CONTRIBUTING §4).
   - **Source-language triplet** (`example_term_*`) — keep only if the source is not in English.
   - Both patterns are optional and independent; a dataset may need neither, one, or both. Add more fields of either kind as needed (e.g. several amount columns) — schema growth is additive (CONTRIBUTING §5).
3. Rename the fields you keep to something meaningful (`example_amount_original`
   → e.g. `amount_original`) and update `data.csv`'s header to match.
4. Delete this README from the copy — it documents the template, not the dataset.
5. Run `python scripts/build_codebook.py datasets/<dataset_name>` and `frictionless validate datasets/<dataset_name>/datapackage.json`.

## Always kept

`record_id`, `source_ref`, `source_lang`, `confidence`, `coder`, `notes`, and the schema-level `missingValues` are not template patterns — they are the project's mandatory conventions (CONTRIBUTING §2 and §4) and every dataset carries them as-is.
