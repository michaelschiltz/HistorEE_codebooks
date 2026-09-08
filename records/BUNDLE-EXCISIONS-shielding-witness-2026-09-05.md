# Hand-excisions applied to `_blind-shielding-witness-2026-09-05`, 2026-09-05

**Maintainer's record. Not in the bundle.** The script's own manifest sits at `~/GitHub/_blind-shielding-witness-2026-09-05.manifest.md` and does not know about any of this; `make_blind_bundle.py` cannot reach material that is not inside a `## <date>` section. See `PATCH-blind-bundle-standing-table-2026-09-05.md` for the defect and the two candidate repairs.

**Applied to the bundle copy only. The tracked tree was verified untouched afterwards** — neither logbook carries the banner string, `data.csv` is at 708 lines ending `OF-0707`, and `logbook/2` is 764 lines live against 727 in the bundle.

Each excision leaves the surrounding heading and a visible banner naming what was removed and why, so the document's six internal cross-references still resolve. **Located by content, not by the 2026-09-04 line numbers, which were already stale.**

## `logbook/2. data inclusion and exclusion.md` — six

1. **Section 2 entire** — *"Thirteen values in `organizational_forms` have no instance"*: the table of every zero-instance characteristic value with its interpretation, the note on the five unused `P` values, the `LR5=na` sentinel defect, and the paragraph drawing the finding out of them. Heading replaced by `#### 2. [section withheld]`.
2. **The closing clause of the "Status of the recommendations" paragraph**, which characterised section 2's contents.
3. **The lead sentence of "Third — the cooperative pole"**, which named a characteristic value and its state in the census.
4. **The zero-cells clause of the `begijnhof` bullet**, which listed characteristics and predicted the form's relation to them.
5. **The `waqf_ahli` clause in "Not now"**, which named the characteristic value that form was expected to supply. The sibling-of-a-coded-row point is preserved.
6. **Item 2 of "Three reasons it is the right partner"** — *"It buys the zero cells."* — which named `LP3=1`, `TS1=1`, `CI3=1`, `CI4=1`, `AP2`, `MG4=state-charter`, `FP2=1` and `LR1`. **This one was not on the pre-run list and was caught only by the post-excision sweep.** It matters more than the others: `CI3=1` and `TS1` are the two characteristics carrying this batch's principal withheld structural expectation, and the item states them as empty in terms.

## `logbook/4. tests done and results used or discarded.md` — two

7. **The standing spent-blind session-slug table, entire, header row included.** Removing selected rows would disclose which ones mattered. The explanatory paragraph above it and the two paragraphs below, which name slugs but not content, are left standing.
8. **The "`FP1=mutual-provision` is still empty" subsection** of the `2026-08-29 (iii)` entry — the value, its state, the two forms selected to fill it and what they were coded as instead. `--withhold-dates 2026-08-29` would have taken three legitimate findings with it.

## Not excised, and why

- **`logbook/1`, line ~466** — the `LR2`/`LR6` split rationale, which lists `symmetric|upside-only|downside-only` as `LR6`'s allowed values. That is vocabulary design, identical to what the CSV carries, and it does not say the value is empty. Cutting it would leave the coder unable to understand what `LR6` asks.
- **Two surviving uses of "zero cells"** in `logbook/2` (lines ~157 and ~176) mean *type rows carrying no data rows*, not characteristic values with no instances. The coder needs to know the census has uncoded type rows.
- **The vocabulary CSVs keep every `allowed_values` entry**, and the views keep everything the matrix holds, **so the zero-instance set remains computable in about a minute.** The excisions remove the instruction, not the computable fact. The coding prompt says this outright rather than inviting the coder to assume the removal was more complete than it is.

## Verification after excision

Leak sweep over all bundle prose (`logbook/`, `views/`, root `*.md`) for statements that a characteristic value is empty: **clean.**

Check suite run inside the bundle:

- `check_vocabularies.py` — valid, 6 files, 162 codes.
- `check_dependence.py datasets/organizational_forms` and `datasets/loss_mitigation_forms` — **the path form, not `--dataset`** — 0 problems each.
- `check_softwrap.py` — 16 files OK, no hard-wrapped prose. **The banners are soft-wrapped and pass.**
- `build_codebook.py --check` — all three current.
- `build_views.py --dataset organizational_forms --component <c> --mechanism all --check` — **all nine current**, swept one component at a time. Bare `--check` (the loss risk-pooling view) also current.
- `frictionless validate` — **VALID** on all three datapackages. `frictionless` was not installed in this device session and was installed for these checks (5.19.0); **an earlier loop reported nothing and exited 0, which is a silent pass and not a pass** — the same defect class as `check_dependence.py --dataset`.
- `validate_vault.py` — vault valid, **216 notes**, all wikilinks resolve; the session scrub dereferenced cleanly. Same count as the 2026-09-04 bundle.

Bundle contains no `CHANGELOG.md` and no `proposed*/`; the `exemplar` column is dropped from the vocabularies; `--withhold-types` was correctly not used, so `data.csv` is complete at 707 rows and `codebook.md` survives — this is a first coding of two new forms, not a recoding.

## Addition to the bundle: `sources/`

The bundle as built contained the two repositories and nothing to read. The two source PDFs live in the ZotMoov store, outside it, so the coding session would either have been blocked at once or have needed the whole 412-file library granted — and a coder loose in the library is a coder redoing phase A's holdings work with a blind it is supposed to be spending on cells.

**Copied in, whole and unclipped**, and verified byte-identical to the ZotMoov originals with `cmp`:

- `sources/Televantos 2020 - Capitalism Before Corporations (OUP).pdf`
- `sources/De Ruysscher 2020 - Entity shielding y los inicios del patrimonio de las sociedades (AHDE XC).pdf`

Offsets re-verified **in the copies**, not assumed from the originals: Televantos PDF 61 → printed 36 and PDF 171 → printed 146, both `printed = PDF − 25`; De Ruysscher PDF 2 → printed 236, `printed = PDF + 234`.

Neither file is clipped to the chapters in scope. Clipping would stop the coder verifying the offset for itself and would amount to the operator pre-selecting the evidence.

**Consequence: the coding session needs exactly one folder granted — the bundle — and no Zotero access at all.** That is the point: `make_blind_bundle.py`'s principle is that what is absent cannot be identified, and confining the readable sources to two files enforces "code only from these" physically rather than by instruction.
