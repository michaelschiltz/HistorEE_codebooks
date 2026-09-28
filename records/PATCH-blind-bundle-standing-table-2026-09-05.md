# The standing-slug table is a structural leak and `--withhold-dates` cannot reach it

**Flagged 2026-09-05, deliberately NOT repaired**, on the standing rule against repairing a defect inside the batch that motivates it. This note is the patch; applying it is a separate commit.

## The defect

`make_blind_bundle.py` withholds two ways: `drop_sections()` deletes `## <date>` sections from the logbooks, and the vault scrub removes notes by `source-session`. **Neither can reach material that is not inside a dated section**, and the two worst leaks in the tracked tree are both of that kind.

**1. `logbook/4`'s standing spent-blind table sits above the first dated heading and is never withheld.** It is *designed* to record what each session read, so it necessarily discloses what there was to read. The `mutual-pole-scheme` row already says *"Computed and recorded the full zero-instance and one-instance value tables"* and names `AP4`, `LR1`, `LR2`, `LR6`, `MG4`, `TS4` and `FP1`. The row this session drafts is worse: it names `AP1`, `AP2`, `AP4`, `TS1` and `CI3` and states a finding about the matrix in terms. **The table grows monotonically, is never removed, and every row added to it enlarges the leak for every later batch.** This is a defect in the protocol, not an accident of one entry.

**2. `logbook/2`, `## 2026-08-30`, preserves the 2026-08-29 forms brief verbatim, and its §2 states the zero-instance table.** The 2026-09-04 session excised three passages from the bundle copy by hand and recorded the line numbers 149–168, 194–200 and (in logbook 4) 182–189. **Those numbers are already stale** — the file has changed since. **Excise by content, never by the recorded line numbers.**

## Excisions required for the 2026-09-05 bundle, by anchor rather than by line

In the **bundle copy only**, replacing each with a visible banner naming what was withheld and why, per the 2026-09-04 stopgap:

- `logbook/2` — the sentence beginning **"Status of the recommendations, which are NOT revised"** (it names the target list and the count of zero-instance values); the **§2 table rows for `LR2`, `LR6` and `FP1`** and the table's surrounding paragraph; the paragraph beginning **"`FP1=mutual-provision` is the finding"**; and the sentence beginning **"Nothing in the vocabulary can take `FP1=mutual-provision`"**.
- `logbook/4` — **the whole standing spent-blind table**, header row and all. Not selected rows: removing some and leaving others discloses which ones mattered.
- `logbook/4` — the paragraphs under **"`FP1=mutual-provision` is still empty, and that is the batch's negative result"**, inside the `2026-08-29 (iii)` entry, which `--withhold-dates 2026-08-29` would otherwise have to take wholesale along with three legitimate findings.

`--withhold-dates 2026-09-04,2026-09-05` handles `logbook/4`'s 2026-09-04 entry, `logbook/6`'s two, and today's views-padding entries without hand work.

## The two candidate repairs, for MS to choose between

1. **Move the "what it spent" column out of the tracked logbook** into an operator-held file outside both repositories, leaving only slug and date in `logbook/4`. This is what the 2026-08-29 brief's own appendix already did — it was *"cut from the file on 2026-08-30 and is held by the operator outside both repositories"* — and the standing table then reproduced the problem the appendix was cut to avoid.
2. **Teach `make_blind_bundle.py` to strip the table**, by anchor, and to fail loudly if the anchor is not found. Cheaper, and it keeps the record in one place; but it is one more thing that must be kept in step with the logbook's prose.

**Recommendation: (1).** A file that must be scrubbed on every use is the wrong place for the record, and the script has now failed to reach the same class of material three times — 2026-08-18, 2026-09-04 and today.

## What is honestly not fixable

`mutual-provision`, `attenuated` and `downside-only` remain allowed values in the vocabulary, and the views show what the matrix holds, **so any coder can recompute the zero-instance set in about a minute.** The excisions remove the *instruction*, not the computable fact. The 2026-09-04 brief said this and it remains true; the coding session should be told it plainly rather than left to assume more.
