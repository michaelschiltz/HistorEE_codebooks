# Blind bundle: `RD-test` on seventeen kō rulebooks (built 2026-10-22)

You are coding a **test table**, not census rows. For each of seventeen 1930s *tanomoshi-kō* rulebooks you code **six cells**: `RD-test`, a characteristic that is not yet in the vocabulary, and five that are (`RB3`, `LS1`, `LS3`, `CN3`, `GV1`). That is 102 cells. Nothing you produce goes into `data.csv`. Everything you may use is here or on the pages listed in `FRAMES.md`, and nothing else may be consulted. The kickoff prompt carries the order of work; this file says what is where.

## Contents

- `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `EDITING-CSV.md`: the doctrine. Read all four first. `CONTRIBUTING.md` §4 holds the missingness rules.
- `RD-TEST-DEFINITION.md`: the definition, values and coding rules of `RD-test`. They are binding.
- `vocabularies/loss_mitigation_characteristic.csv` (the `exemplar` column has been removed) and `vocabularies/loss_mitigation_type.csv`. For the five existing characteristics, every `definition`, `allowed_values` and `locator` is binding.
- `datasets/loss_mitigation_forms/`: the live `data.csv`, `recodings.csv` and `datapackage.json`. **None of the seventeen kō has rows here.** The other rows are house practice: read the notes of the existing `ko_*` rows on `RB3`, `LS1`, `LS3`, `CN3` and `GV1` to see how this census argues those cells for kō.
- `FRAMES.md`: the source, how to read it, the seventeen kō with their pages and frames, and what you must not read.
- `PRIORS-residual-default-2026-10-22.md`: the priors template.
- `TEST-TABLE-HEADER.csv`: the header your table must have.
- `scripts/check_test_table.py`: run it on your table before you stop.
- `proposed-of/`: empty. Everything you produce goes here.

## The table

One row per kō per characteristic, in `proposed-of/TEST-residual-default-2026-10-22.csv`, with exactly the header in `TEST-TABLE-HEADER.csv` and LF line endings.

- `ko`: the kō's number in the volume (6, 7, 12, …).
- `name`: its name as in `FRAMES.md`.
- `place_as_printed`: its 郡 and 村 or 町, as printed.
- `char_id`, `value`, `confidence`, `articulation`, `source_ref`, `source_lang`, `source_read` and `notes` have the meanings they have in `data.csv`. `source_ref` gives printed pages and the rule's article numbers. `source_lang` is `ja`.
- `coder_model` and `coder_effort`: your model identifier and effort setting, on every row.

A note quotes the clause a cell rests on, in its original script, and says why the value follows. A `.NR` note says what was read and found silent.
