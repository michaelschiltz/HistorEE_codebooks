# Proposed: `societas_maris` into `organizational_forms`, and the `mudaraba` determination

2026-08-18, second batch of the day. Written straight into the working tree; these files are the
standalone copies for review.

| File | Contents |
|---|---|
| `organizational_forms-rows.csv` | the 11 proposed rows, `OF-0283`–`OF-0293` |
| `organizational_form_type-rows.csv` | 4 type-vocabulary rows: `societas_maris` (**new code**), `mudaraba`, `qirad`, `commenda` |
| `build_of.py`, `build_oftype.py` | the generators, for audit |

## Checks

```
python3 scripts/check_vocabularies.py                                  ✓ 6 files, 151 codes
python3 scripts/check_dependence.py datasets/organizational_forms      ✓ 0 problems
python3 scripts/check_dependence.py datasets/loss_mitigation_forms     ✓ 0 problems
python3 -m frictionless validate datasets/organizational_forms/…       ✓ VALID
python3 scripts/build_codebook.py                                      ✓ regenerated
python3 scripts/validate_vault.py          (myfoamrepo)                ✓ 176 notes
```

## The result, in one table

`societas_maris` is coded on exactly the eleven characteristics `commenda` carries, so the pair is
comparable cell for cell. **No cell of `commenda` was touched.**

| | TS2 | AP3 | LR1 | LR2 | LR3 | LR4 | LR5 | CF1 | CF2 | CF3 | LR6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `commenda` | single-venture | 1 | limited | coupled | 1 | 0 | .NA | **1** | 0 | bilateral | **upside-only** |
| `societas_maris` | single-venture | 1 | limited | coupled | 1 | 0 | .NA | **P** | 0 | bilateral | **symmetric** |

Two separations out of eleven, and the important one is `LR6`. It gives the `agent-loss-exposure`
group the signature `{AP3:1, CF2:0, LR1:limited, LR6:symmetric}`, which did not exist — **three of
four members held identical while the fourth moves**, on substantive values, inside one contract
family. `CF2` and `LR6` had previously separated only via `.NA`.

## Three things that need your decision

1. ~~**`AP3=1` may be wrong**~~ — **RESOLVED the same day, on your decision.** A `locator` column
   was added to both characteristic vocabularies (7 values, no new characteristics), `AP3` and `LR1`
   were relocated to the labour-supplying party and restricted to the venture's third-party
   creditors, and four cells moved: `commenda` and `societas_maris` `AP3` 1→0 and `LR1`
   limited→unlimited-several; `qirad` and `ortoq_equity` both to `.NR`. `isqa`, `ortoq_loan` and
   `nakai_fictive_household` held, on the ground that where the principal is a *creditor* rather
   than a residual claimant the two questions coincide.

   **Result: `AP3` has zero variance across the bilateral capital–labour family**, and
   `AP3=0` now occurs with `CF2` in `{0, 1, P}` where before the two inverted perfectly. The
   `agent-loss-exposure` group's apparent collinearity was substantially a coding artefact. The
   `societas_maris` result above survives unchanged — `AP3` and `LR1` moved together, so the pair
   still separates on `LR6` and `CF1` only. Logbook 1, 2026-08-18 (ii); logbook 4 postscript.
2. **`mudaraba` left uncoded**, as a determination on the `ortoq_alloc` model — it is the Ḥanafī name
   for `qirad` (Ramli 2018, 97). Falsification condition on the type row.
3. **`CF3=bilateral` means *two principals*** and collides with the literature's "bilateral commenda"
   (= both invest). Harmless today, not harmless the first time a multilateral commenda is coded.
   A sentence in `CF3`'s definition would fix it; not written, per the rule about characteristics.

## Also corrected on the way through

- `datasets/organizational_forms/codebook.md` in your working tree was a **stale uncommitted copy**,
  one line behind HEAD, while the other two codebooks were current. Regenerating fixed it.
- The vault note *Unilateral and bilateral commenda collapse on profit and separate on loss* claimed
  `organizational_forms` would merge the pair. It doesn't. Corrected in place, with the correction
  visible in the note.

## Still not done

`version` bump and `CHANGELOG.md` — both datapackages now, `loss_mitigation_forms` 0.6.0 and
`organizational_forms` 0.8.0.
