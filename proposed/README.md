# Proposed: the four allocation anchors — for review, not committed

Blind coding session, 2026-08-18. **Revision 2**, after MS supplied the van Doosselaere 2009 PDF
mid-session: `societas_maris` re-coded from `medium`/placement to `high` on the Genoese corpus,
corroboration added to the other three rows, two new logbook 4 findings ((v) and (vi)), and a fifth
vault note. Row IDs and the row count are unchanged (`LM-0527`–`LM-0563`). Nothing is committed; nothing was run against your working
copy. Both repos were cloned fresh into the session sandbox and every change lives here as a
patch or a CSV.

## What is in this folder

| File | Apply to | Contents |
|---|---|---|
| `loss_mitigation_forms-rows.csv` | — | the 37 proposed `data.csv` rows, `LM-0527`–`LM-0563`, standalone with header |
| `loss_mitigation_type-rows.csv` | — | the 4 replacement `vocabularies/loss_mitigation_type.csv` rows, standalone with header |
| `00-data-and-vocabulary.patch` | `HistorEE_codebooks` | the same two changes as a diff, plus the regenerated `codebook.md` |
| `01-logbook.patch` | `HistorEE_codebooks` | logbook 2, 4 and 5 entries dated 2026-08-18 |
| `02-vault.patch` | `myfoamrepo` | five new atomic notes and the `## Notes` additions to four MOCs |

Apply with `git apply <file>` from the relevant repo root.

## Checks run, on the patched tree

```
python3 scripts/check_vocabularies.py                                   ✓ 6 files, 150 codes
python3 scripts/check_dependence.py datasets/loss_mitigation_forms      ✓ 0 problems
python3 -m frictionless validate datasets/.../datapackage.json          ✓ VALID
python3 scripts/build_codebook.py                                       ✓ regenerated (526 → 563 rows)
python3 scripts/validate_vault.py            (myfoamrepo)               ✓ 175 notes, all wikilinks resolve
```

## Two things deliberately NOT done

1. **No datapackage `version` bump and no `CHANGELOG.md` entry.** `CLAUDE.md` requires both. The
   `[Unreleased]` blocks for 2026-08-16 and 2026-08-17 were withheld from this session, so it
   cannot see what version is already staged there. Left for you at merge. The codebook **was**
   regenerated, so the CI drift check will pass either way.
2. **`ortoq_alloc` untouched**, per the brief.

## Read the notes, not just the values

The `notes` column carries the reasoning, the rejected alternatives and the source limits. Three
cells in particular should not be read at face value without them: `qirad_alloc VF1` (`.NR`
because the library lacks Udovitch, **not** because the *qirāḍ* lacks verification); `isqa_alloc RB1`
(the source reaches theft and loss but not maritime peril); and the whole `commenda_alloc` /
`qirad_alloc` pair, which is identical by finding and must not be counted twice.

## One library-housekeeping item

`V4S222VJ` (van Doosselaere) is still tagged `priority-pdf-wanted` and is filed in `GQTSU7EA` only.
The tag is now false and the item belongs in `3CGGDGFW` too — it is the single most load-bearing
source for `societas_maris`.
