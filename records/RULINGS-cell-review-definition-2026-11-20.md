# Rulings: what a cell review requires (first use of `reviewed_by` / `review_status`)

**Ruled by MS in chat on 2026-11-20 (21:59 JST): "Recommendations accepted." Drafted by the assistant (`claude-opus-5-5`) the same day; every recommendation below was accepted as written. Recorded before the first review is written.** Until now all 981 `organizational_forms` cells (and every cell of the other censuses) read `none` / `unreviewed`; the schema defines the statuses in one line each (`datapackage.json`, `review_status`). The first use sets the precedent.

## 1. `source-checked` (recommended definition)

A reviewer has, for this cell:

- read every passage the cell's `source_ref` cites, in the printed source or its page image, not in a text layer or a translation;
- confirmed the value, `confidence` and `articulation` against those passages;
- checked every quotation in `notes` against the page;
- for a coded absence (`.NR`, `0` for a clause not written, `none`), read the whole of each instance the cell rests on, since an absence is a claim about the whole text.

The reviewer writes `confirm` on a review sheet. On application `reviewed_by` takes the reviewer's initials and `review_status` becomes `source-checked`.

## 2. `coding-checked`

As the schema has it: the reviewer accepts the reasoning but did not or could not check the source (for example, a language outside the reviewer's). **Recommended:** never used for a cell whose source the reviewer can read; partial checking is not `coding-checked` but unfinished `source-checked`.

## 3. `disputed`, and what follows

A reviewer who disagrees writes `dispute` with what the source shows. **Recommended:** the cell is marked `disputed` at application; the maintainer rules it with the coder's reasoning and the reviewer's beside it, as in the batch adjudications; a changed value is edited in place in `data.csv` with an `[REVIEWED <date> by <initials>: …]` note, and the status becomes `source-checked` once ruled. A dispute the maintainer rules against the reviewer also ends `source-checked`, with the dispute kept in the note.

## 4. What does not count as a review (recommended)

- An eyeball check: it measures a sample of record fields, not cells (ER-0025).
- A translation review, or a ruling on a single clause (R1 on doc. 8): evidence for a cell, not a review of it.
- A review by the coder of the same cell.

## 5. Corrections that leave the value standing

**Recommended:** `confirm, note: …` corrects `notes` or `source_ref` without a ruling (a page number, a quotation's wording, a count), appended as `[REVIEWED <date> by <initials>: …]`; the frozen text is not rewritten.

## 6. Independence, said in the record

The status records verification against the source, not independence. Where the reviewer also ruled on the batch (as MS did on the Seville scope and on doc. 8's loss clause), the logbook entry says so.

## 7. Mechanics

Review sheet in `proposed-of/` while in progress; the filled sheet frozen into `records/` (`REVIEW-<slug>-<date>-filled.md`); application sets the two columns and appends notes; logbook 4 entry and a CHANGELOG line; no version bump (process metadata). The views do not show the columns, so nothing is regenerated beyond the codebook if its counts change.
