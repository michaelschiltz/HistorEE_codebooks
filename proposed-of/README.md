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

1. **`AP3=1` may be wrong on `commenda`, `qirad`, `ortoq_equity` and this row.** Harris 2007, 11
   calls the commenda's shielding *asymmetric* — the investor's private assets are unreachable, the
   traveller's are not, and he bears sole liability to third parties. On `AP3`'s own wording that is
   `P`. Not changed here, deliberately: recoding an old row in the batch that adds its comparison
   form confounds the two. Logbook 1, 2026-08-18.
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
