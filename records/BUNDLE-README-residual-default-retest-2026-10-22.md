# Blind bundle: `RD-test` re-test on nineteen rulebooks (built 2026-10-22)

You are coding a **test table**, not census rows. For each of nineteen rulebooks of rotating funds, from two government publications of 1915 and c. 1942, you code **six cells**: `RD-test`, a characteristic that is not yet in the vocabulary, and five that are (`RB3`, `LS1`, `LS3`, `CN3`, `GV1`). That is 114 cells. Nothing you produce goes into `data.csv`. Everything you may use is here or on the pages listed in `FRAMES.md`, and nothing else may be consulted. The kickoff prompt carries the order of work; this file says what is where.

## Contents

- `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `EDITING-CSV.md`: the doctrine. Read all four first. `CONTRIBUTING.md` §4 holds the missingness rules.
- `RD-TEST-DEFINITION.md`: the definition, values, coding rules and scope of `RD-test`. They are binding.
- `vocabularies/loss_mitigation_characteristic.csv` (the `exemplar` column has been removed) and `vocabularies/loss_mitigation_type.csv`. For the five existing characteristics, every `definition`, `allowed_values` and `locator` is binding, including the `CLARIFIED` sentences at the end of the `CN3` and `LS3` definitions.
- `datasets/loss_mitigation_forms/`: the live `data.csv`, `recodings.csv` and `datapackage.json`. None of the nineteen rulebooks has rows here. The other rows are house practice: read the notes of the existing `ko_*` rows on `RB3`, `LS1`, `LS3`, `CN3` and `GV1` to see how this census argues those cells for kō.
- `FRAMES.md`: the two sources, how to read them, the nineteen rulebooks with their pages and frames, and what you must not read.
- `PRIORS-residual-default-retest-2026-10-22.md`: the priors template.
- `TEST-TABLE-HEADER.csv`: the header your table must have.
- `scripts/check_test_table.py`: run it on your table before you stop.
- `proposed-of/`: empty. Everything you produce goes here.

## The table

One row per rulebook per characteristic, in `proposed-of/TEST-residual-default-retest-2026-10-22.csv`, with exactly the header in `TEST-TABLE-HEADER.csv` and LF line endings.

- `id`: the rulebook's id in `FRAMES.md` (`M01`–`M11`, `A03`–`A07`, `T01`–`T03`).
- `source`: `M` or `S`.
- `name_as_printed`: the rulebook's title as printed in its heading.
- `place_as_printed`: its place (村, 町 or 市, with 郡 and 縣 where printed), or `not printed`.
- `char_id`, `value`, `confidence`, `articulation`, `source_ref`, `source_lang`, `source_read` and `notes` have the meanings they have in `data.csv`. `source_ref` gives the source letter, printed pages and the rule's article numbers. `source_lang` is `ja`.
- `coder_model` and `coder_effort`: your model identifier and effort setting, on every row.

A note quotes the clause a cell rests on, in its original script, and says why the value follows. A `.NR` note says what was read and found silent. Personal names printed in the rulebooks are not repeated in notes.
