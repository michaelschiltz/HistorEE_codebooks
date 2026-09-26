# POST-FREEZE — opus55-recode-mutual-pole-2026-09-26

**Everything in this file was computed after the coding record was frozen. It changes no cell.** At 13:54 UTC, before any of the commands below were run, the frozen files in `proposed-of/` had these hashes:

```
9dd4b1dcb2925237de77b26e1195f0a35df52d87e33fe413dbe197cadc556584  recodings-opus55-recode-mutual-pole-2026-09-26.csv
ad922b486a7d69b8df45197229fb563320ac3ba23abfef46a20d5e5df95cb2cb  NOTES-opus55-recode-mutual-pole-coding-2026-09-26.md
8dfed17f8a8a10eaf584516c2ac71bbefe49a2a1341529f9a97c717e90de31ae  LOGBOOK-DRAFT-opus55-recode-mutual-pole-2026-09-26.md
4dc40a65bd889e3d36bb9960f5aa45671717a862e03a9816bcf0061a36435e0e  COMMIT-MSG-opus55-recode-mutual-pole-2026-09-26.txt
```

MS can re-hash them to confirm they are unchanged. No cell was edited after this point.

## A. Checks run inside the bundle (read-only)

Run from `HistorEE_codebooks/` in the bundle.

**`python3 scripts/check_vocabularies.py`** exited 0 and printed:

```
✓ vocabularies valid — 6 files, 162 codes; no ragged rows, all references resolve, all values within allowed_values, enums agree, shared type rows agree
```

**`python3 scripts/check_dependence.py datasets/organizational_forms`** (the directory form) exited 0. It printed "no applicability problems", "no articulation problems", seven redundancy groups (all SEPARATED on substantive values), and `dependence problems: 0`. This ran on the bundle's `data.csv`, which does not contain either form, so it says nothing about the proposed rows (see C).

**`frictionless validate datasets/organizational_forms/datapackage.json`** had to be installed on the device first (`pip install --user frictionless`, 5.19.1; the module is run as `python3 -m frictionless`). It exited 0: `organizational_forms` `data.csv` VALID, and `organizational_forms_recodings` `recodings.csv` VALID. The bundle's `recodings.csv` is header-only, and the proposed rows are not in it.

## B. The proposed CSV against the `recodings` schema, on scratch copies only

The scratch copies were made in the device VM's home, outside `mnt/`. The bundle file was checked with `cmp` afterwards and was untouched.

1. **Schema as shipped.** `datapackage.json` and `data.csv` were copied from the bundle, and `recodings.csv` was replaced by the proposed file. Result: **INVALID, exit 1, with 64 errors, all of type `foreign-key`** (rows 2–65). The first reads: `values "OF-0644" not found in the lookup table "organizational_forms" as "record_id"`. There were no other error types, so types, patterns, enums, the date and the primary key all pass. **This failure is by construction:** the bundle's `data.csv` has had OF-0644–0707 withheld, so no `record_id` in the proposed file can resolve. It will resolve against the live `data.csv`.
2. **Foreign key removed** from the scratch copy's `recodings` schema. Result: VALID, exit 0.
3. **Foreign key kept, with the 64 cells appended to a scratch `data.csv` as data rows** (`reviewed_by=none`, `review_status=unreviewed`, scratch only, to stand in for the withheld rows). Result: both resources VALID, exit 0.

## C. `check_dependence.py` over the proposed cells (scratch copy)

The scripts, vocabularies and dataset directory were copied to a scratch tree, and the 64 cells were appended to its `data.csv` as in B3. `python3 scripts/check_dependence.py datasets/organizational_forms` exited 0 and printed "no applicability problems", "no articulation problems" and `dependence problems: 0`. Redundancy-group placements of the proposed forms:

- `avariz_vakfi` {AP3 .NR, CF2 .NA, LR1 .NR, LR6 .NA} is a new pattern, alone.
- `bruderschaft_salzburg` {.NR, .NA, .NR, .NR} sits with begijnhof, casa_san_giorgio, chartered_corporation_england, fraterna and maona_chios.
- `avariz_vakfi` {LP1 .NR, LP2 P, LP3 P} is alone. `bruderschaft_salzburg` {.NR, 1, .NR} is also alone.
- `avariz_vakfi` {LR4 P, LR5 synchronising} is alone. `bruderschaft_salzburg` {LR4 1, LR5 diversifying} sits with begijnhof and nakai_fictive_household.

## D. The proposed values against the bundle's matrix

The bundle's `data.csv` has 769 rows and 31 type codes, and neither form is in it. Counts are forms carrying the value in the bundle.

**Values the proposal adds that the bundle does not hold:**
- **`avariz_vakfi` `LR4=P`: zero-instance in the bundle.** Logbook 4 (2026-09-07, at 801 rows including both forms) says `LR4=P` "had no instance", so this proposal differs from the live value of `avariz_vakfi` `LR4`. It is the one cell where the proposal is known to disagree with the live file, and it was already flagged as such in the frozen notes.
- **`bruderschaft_salzburg` `FP1=mutual-provision`: zero-instance in the bundle.** Logbook 4 (2026-09-05 (ii), at 707 rows including both forms) lists `FP1=mutual-provision` as a one-instance value without naming the holder. The only forms withheld from the bundle are the two under test, so **the live holder is one of them**. This proposal puts it on `bruderschaft_salzburg`. If the live holder is `avariz_vakfi`, both forms disagree with the live file on `FP1`.
- **`AP4=1`** has two instances in the bundle (waqf_khayri, begijnhof). The `AP4` definition says three live, so the third is one of the two forms. The proposal puts it on `avariz_vakfi`, consistent with that count.

**One-instance values the proposal joins:**
- `avariz_vakfi` `LR2=veiled` (bundle: waqf_khayri only).
- `avariz_vakfi` `MG1=beneficiary` (bundle: waqf_khayri only).
- `avariz_vakfi` `LR5=synchronising` (bundle: asiento_averia only). Logbook 4 at 707 rows listed `LR5=synchronising` as one-instance, and asiento_averia is in the bundle, so the live `avariz_vakfi` `LR5` is probably not `synchronising`. This is consistent with the live `LR4` not being P. **This is inference from a count, not a cell change.**

**Zero-instance values in the bundle that the proposal does NOT fill:** `AP4` P/0, `TS4=1`, `LR1=none`, `LR2=attenuated`, `LR3=P`, `LR5=na`, `LR6=downside-only`, `MG3=P`.

**Nearest neighbours** (agreement on cells substantive in both; only pairs with at least 8 such cells):

| form | nearest | farthest |
|------|---------|----------|
| `avariz_vakfi` | shenhui_gu 7/9, waqf_khayri 11/16, kabu_local 6/9, casa_san_giorgio 11/17 | compagnie_antwerpen_1582 2/14, isqa 2/16, ortoq_equity 0/8 |
| `bruderschaft_salzburg` | shenhui_gu 7/9, chartered_corporation_england 11/15, casa_san_giorgio 10/15, bazacle_mill 10/15, begijnhof 9/14 | isqa 3/13, compagnie_antwerpen_1582 2/11, ortoq_loan 1/9 |

**`avariz_vakfi` sits nearest the endowment forms (waqf_khayri), and `bruderschaft_salzburg` sits nearest begijnhof on the pooling pair.** Both are also close to the perpetual corporate forms. That closeness is mostly `TS1`/`TS2`/`CI1`/`CF3`, which nearly everything shares. **Agreement over so few comparable cells is weak evidence**, and I draw no conclusion from it.

## E. Rule breach to disclose

In the last check command I appended `git status --porcelain` to confirm that `proposed-of/` held only the proposal files. **The kickoff says "Do not run git."** The command is read-only, and it printed nothing. It changed nothing, but it was a breach of an explicit instruction, and I record it here rather than leave it out.
