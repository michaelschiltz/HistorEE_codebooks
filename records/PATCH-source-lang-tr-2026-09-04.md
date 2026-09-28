# `source_lang` has no `tr` in `organizational_forms` — flagged, not applied

**Status: NOT APPLIED.** `datasets/organizational_forms/datapackage.json` was not modified in the bundle. This file records the defect, its diagnosis and the one-line fix, per the standing rule that a schema defect is not repaired inside the batch that exposed it.

## The defect

`datasets/organizational_forms/datapackage.json` constrains `source_lang` to

```
["ja","nl","de","fr","en","es","he","arc","ar","la","it","pl","pt"]
```

`datasets/loss_mitigation_forms/datapackage.json` constrains the same field to

```
["ja","nl","de","fr","en","es","he","arc","ar","la","it","tr","zh","pl","pt"]
```

The two lists differ by exactly `tr` and `zh`. Nothing in either schema, in `CONTRIBUTING.md` or in the codebook says the entity census excludes Turkish and Chinese sources; the field's own description says "ISO 639-1 where a two-letter code exists". The divergence looks like drift rather than a decision: `tr` was added on the loss side when the Ottoman rows were coded in August and never mirrored, and the entity census had until now never cited a Turkish source (`source_lang` there runs `en` 464, `it` 38, `es` 24, `arc` 7, `nl` 5, and nothing else).

## Why it blocks this batch

`avariz_vakfi` is coded from four Turkish-language sources. Twenty-eight of its thirty-two rows carry `source_lang=tr`; the other four are `.NA` and are exempt as missing values.

Measured on a scratch copy with the proposed rows spliced in:

```
python3 -m frictionless validate datasets/organizational_forms/datapackage.json
  -> 28 constraint-errors, every one of them:
     The cell "tr" ... does not conform to a constraint: constraint "enum" is [...]
```

Adding `tr` to that one enum and re-running gives `VALID`, and the error count falls from 28 to 0. `datasets/clearing_records` and `datasets/loss_mitigation_forms` are VALID either way.

**This is the one flagged defect in the batch that must be merged BEFORE the rows rather than merely recorded.** Everything else here can wait; this cannot, because CI runs `frictionless validate` on every push and the rows will fail it.

## The fix

In `datasets/organizational_forms/datapackage.json`, in the `source_lang` field's `constraints.enum`, insert `"tr"` after `"it"`:

```diff
-        "enum": ["ja","nl","de","fr","en","es","he","arc","ar","la","it","pl","pt"]
+        "enum": ["ja","nl","de","fr","en","es","he","arc","ar","la","it","tr","pl","pt"]
```

Additive; no coded value changes. `build_codebook.py` must then be re-run, because the codebook prints the enum.

## Two questions the fix does not settle, and they are the maintainer's

1. **Should `zh` go in at the same time?** The entity census already holds five Chinese forms (`hegu_yingu`, `hegu_shengu`, `kabu_local`… `shenhui_gu`), all coded `source_lang=en` from Zelin 2019 and Wu 2025. Nothing is broken today. But the next Chinese-language source will hit exactly this wall, and mirroring the loss-side list in full closes both holes in one commit rather than two.
2. **Should the two enums be registered as a deliberate duplicate?** `CONTRIBUTING.md` §4 has `ENUM_VOCAB` in `check_vocabularies.py` for fields duplicated on purpose, and says "an unregistered duplicate is precisely what drifts unnoticed". `source_lang` is duplicated across two datapackages with no vocabulary file and no agreement check, and it has now drifted. The cheap guard is a check that every dataset's `source_lang` enum is the same set — a few lines, no new dependency, and it would have caught this in August.

Neither is proposed here. Both belong to the commit that makes the fix.
