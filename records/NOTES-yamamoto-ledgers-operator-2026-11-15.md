# Operator notes: blind double transcription of Yamamoto IV(A), Nos. 221–259 (2026-11-15)

**Status: prepared by the assistant (`claude-opus-5-5`, effort `high`) at MS's request on 2026-11-15, after the OCR pilot of 2026-11-10 (`records/OCR-TEST-yamamoto-2026-11-10.md`). Pass slug `yamamoto-ledgers-2026-11-15`. Transcription and collation only; no cell is coded and no seeded sample is drawn in this pass (MS, 2026-11-15).**

## Why

The pilot measured the text layer of Yamamoto IV(A) at 72.5 per cent character recall over five pages and 44.8 per cent on the funeral-donation ledger, with 粟 at 0 of 26 and 幷 at 0 of 23. The layer cannot support term counts, amounts or quotation. The pilot also found that the assistant's own reading, used as its reference, had silently regularised two characters toward the expected wording. Hence two independent transcriptions from the page images, a diff, and MS's ruling on every disagreement.

`she_death_aid` was coded on 2026-10-13/14 from Ning Ke and Hao Chunwen 1997 (`records/NOTES-she-associations-2026-10-13.md`). Yamamoto edits the same manuscripts, so it is a second edition, not a second witness; the selection brief declared that non-independence before the rows.

## Design

- **Scope:** section IV of the edition, 納贈曆, Nos. 221–259, PDF pp. 99–122 of Zotero attachment DG452E53 (item 9XU6924V). Section V (計會, Nos. 260–278, PDF pp. 123–138) is out of scope for this pass.
- **Two bundles,** identical: `~/ocr/_blind-yamamoto-ledgers-A-2026-11-15` and `-B-`. Each holds 24 page images (400 dpi greyscale, from the pilot's renders in `~/ocr/yam_texts/`), 24 overviews and 192 overlapping tiles (eight per page), the README with the transcription conventions, and `MANIFEST.sha256` over the 240 images. Hashes at issue: README.md 1d7b1f08ae787d618fc65c064278598b3c2963a0b517d5e163a46df610f7052f; MANIFEST.sha256 9d89d2b64f89a859262468bb4a80220eb72db67ead7dbeef328c8c700776ab45. The bundles sit under `~/ocr`, not beside the earlier `_blind-*` folders in `~/GitHub`, because this session could not be given access to `~/GitHub`.
- **Blindness:** each transcriber sees only its own bundle. Neither sees the OCR, Ning and Hao, 唐耕耦's 釋錄, the cells of `she_death_aid`, or the other transcriber's output. The operator (this session) has seen five pilot pages and the top strips of pp. 97–140 for orientation, and has not transcribed any of the 39 documents.
- **Transcribers:** recommended A = `claude-opus-5-5`, B = a different model where available (`claude-fable-5-2`), because two sessions of one model share blind spots and their agreement then clears less. The model actually used goes on the first line of each `LOG.md`. As run (MS, 2026-11-15): A `claude-opus-5-5`, effort `high`; B `claude-fable-5-2`, started at effort `medium` and switched to `high` before transcription began.
- **Prompt:** `records/PROMPT-yamamoto-ledgers-transcription-2026-11-15.md`.

## Predictions, before any transcription exists

1. Disagreement concentrates in the characters the pilot found the OCR losing: 幷/并/併, 粟/栗, 褐, 斜, and the numerals with 丈 and 尺, and in personal names with rare characters.
2. Disagreement on the editorial signs (side rules, small inserted characters, parenthesised readings) exceeds disagreement on characters, because the signs need judgement about extent.
3. Agreement does not clear a reading. Where A and B agree on a regularised form, the diff cannot see it; only the collation against Ning and Hao, or MS's reading, can.

## After both bundles are frozen

1. **Count audit.** `scripts/audit_text_layer.py` cannot run on per-document files; instead, for each transcriber, the 39 files exist, and each file's last line number matches the page. Recorded in `logbook/4-appendix-error-rates.csv` only if a document is missing or short.
2. **Diff.** Line-aligned, then character-aligned within each line. Sign-only differences (the same reading written in two notations) are normalised after reading both `SIGNS.md` files, and counted separately.
3. **Adjudication sheet for MS.** Every disagreement and every `[?]` or `[X?]`, with page, tile and line, the two readings, and the assistant's recommendation read on the image. MS rules on the image.
4. **Register rows.** Disagreement rate between A and B; each transcriber's error rate against the adjudicated text, at adjudicated positions. Both are lower bounds: an error A and B share is invisible to the diff. Labelled `sample` all-units and `reference_type` maintainer-image-read for the adjudicated positions.
5. **Collation.** Every passage of Nos. 221–259 that a `she_death_aid` cell quotes from Ning and Hao is set against the adjudicated Yamamoto text. A difference goes back to the image of both editions before any cell note changes.
6. **Records.** The transcriptions are not committed. The edition dates from 1989 and the repository is public, so on the `records/` rule its text stays out (as in ruling 2 of `records/RULINGS-count-audit-2026-11-15.md`). The frozen `out/` folders stay in `~/ocr`, with a copy in Drive. The repository gets this file, the prompt, the bundle README, the hashes of both frozen `SHA256SUMS` files, the diff counts, the adjudication rulings (citing single characters and short readings only) and the register rows. Logbooks 4 and 5, CHANGELOG, and the vault.

## Incident, 2026-11-15, 15:35–15:46 JST: a second B session started while the first was still running

**What happened.** The first B session (`claude-fable-5-2`) had not stopped and had written no `RESUME.md`; a second B session was opened in the belief that it had, with the continuation prompt. Finding no `RESUME.md`, it took its stop point from `LOG.md` (No. 239 l. 4, p. 113), and wrote into `out/` while the first session was still writing there. It noticed, stopped and withdrew at 15:43, having transcribed nothing that remains.

**What it changed and undid, by its own account.** (1) `No-239.txt`: a duplicate l. 4 and `(後空)` appended, then removed; the file is back to 10 rows, 387 bytes. (2) `No-240.txt`, the first session's file: 馬步 → 馬歩 (twice) and 尙 → 尚 (twice), then put back. Checked by the operator at 15:46: `No-239.txt` 10 rows, 387 bytes; `No-240.txt` holds 步 ×2, 尙 ×2, no 歩 or 尚; the first session's own page log for p. 113 records 尙 at ll. 6 and 11. A change the second session did not report cannot be excluded by these checks, since no hash of `No-240.txt` was taken before 15:38.

**What remains of it.** Two blocks in B's `LOG.md`: a "Session 2 (continuation)" heading block between the first session's p. 112 and p. 113 entries, now void, and a withdrawal note. They stay where they are: `LOG.md` is append-only, and rewriting it while the first session appends would risk its entries. They will fall inside B's `SHA256SUMS`.

**Blindness.** The second session read the first session's p. 113 log entry and `No-240.txt`; it is closed and takes no further part. The first B session and A are unaffected: neither saw the other's text. The second session's readings of No. 240 (歩 at ll. 10 and 16, 尚 at ll. 6 and 11, at 6×) go on the adjudication sheet as flags, marked not independent.

**Lesson, applied from here on.** A continuation prompt is given only after the transcriber has itself reported a stop and written `RESUME.md`; the operator checks the folder before issuing one.

## Incident, 2026-11-15, 15:26–15:51 JST: A's continuation ran under two models and two branches

**What the folder shows.** A's continuation session opened at 15:26 under `claude-fable-5-2`, B's model, and wrote only its session header. At 15:32 it was switched to `claude-opus-5-5`; under Opus it wrote `No-237.txt` (15:39), `No-238.txt` and `No-239.txt` ll. 1–3 (15:44), the `SIGNS.md` additions (15:45) and the page notes for pp. 111–112. A second switch at 15:48 restarted the conversation on a branch that did not hold that work in its context; that branch found the files, appended a second model-change note (15:50) and stopped. Nothing was written in A's folder between 15:45 and 15:50, so the first branch is not running.

**Assessment.** Nos. 237–239 ll. 1–3 are A's work under `claude-opus-5-5`, by its own log, in A's conventions; A never saw B. The Fable interval wrote no transcription. The duplicated model-change notes stay in `LOG.md` (append-only). The continuing branch takes over from No. 239 l. 4 (p. 113) after reading A's own files 237–239 and the new `SIGNS.md` entries.

**Lesson.** A transcriber's model is not changed mid-session; a change of model is a new session with a continuation prompt after a clean stop.

## B frozen, 2026-11-15 15:54 JST

B (`claude-fable-5-2`, one session throughout, apart from the withdrawn second session above) froze at 15:54. Checked by the operator at 15:59: 39 files `No-221.txt` to `No-259.txt`, no `RESUME.md`, `SHA256SUMS` verifies against every file in `out/`; its own hash is 31d579f44a3734ae4c32da65be927768ada982c24b3be51285caa777926ca43d. `No-240.txt` still holds 步 ×2 and 尙 ×2. B verified the bundle images against `MANIFEST.sha256` (240 of 240) before freezing.

## A frozen, 2026-11-15 16:33 JST

A (`claude-opus-5-5` for every transcribed document; see the incident above for the Fable interval, which wrote no transcription) froze at 16:33. Checked by the operator at 16:34: 39 files `No-221.txt` to `No-259.txt`; `RESUME.md` remains in `out/`, updated by A to state that the pass is complete, and falls inside the hashes; `SHA256SUMS` verifies against every file in `out/`; its own hash is 098df8cbafb10ea8d1e8b41313088b08712100f5667bda771ac6d64b8af8ce57.

## Diff of A against B, 2026-11-15

Document level, after normalising notation (uncertainty brackets, print marks, sign and component notation, whitespace): A 9,962 characters, B 9,975. Disagreements: 73 content operations (214 characters), 55 form operations (56 characters; 清/淸, 青/靑 and the like), 42 placement operations (side notes, overflow, sub-columns). Uncertainty marks: A 28, B 14. Row structure differs in No. 233 (B gives names their own rows) and wherever A writes side notes as separate rows.

The adjudication sheet (56 decision rows, 8 convention questions, recommendations read from the page images) is in `~/ocr/_adjudication-yamamoto-ledgers-2026-11-15/`, outside the repository, because it carries crops of the edition. Recommendation tally: A 22, B 30, combine 2, neither 1 (歩 at No. 240 ll. 10 and 16, which both transcribers wrote as 步), check on tile 1. The maintainer rules on the image; rulings go into a `records/` file citing single characters and short readings only.
