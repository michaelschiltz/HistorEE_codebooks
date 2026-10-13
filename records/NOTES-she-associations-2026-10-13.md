# Selection brief — coding the Dunhuang *she* association (2026-10-13)

**Status: drafted by the assistant (`claude-opus-5-5`, effort `high`) at MS's request and approved by MS in chat on 2026-10-13, with two decisions: the priors file is committed before any document is read for coding; an `organizational_forms` row is deferred. Pass slug `she-associations-2026-10-13`; open, not blind. The blind on the *she* was already spent by `silk-road-archives-survey` (2026-09-12) and `codable-forms-survey-2026-10-11` (logbook 4, standing table).**

## Read first

- The vault note "Dunhuang she associations - bylaws for a funeral fund"; logbook 2, 2026-09-12 (xi), with its three objections and its provenance warning; logbook 5, 2026-10-13 (ix), on the OCR and its limits.
- The cells and type rows of the neighbours: `guild_box_brabant`, `guild_relief_england`, `guild_box_dutch`, `confraternity_fund_it`, the `ko_*` rows, `averia_pool` (the precedent for the fund-or-levy question), `huiguan` and `shenhui_gu_alloc`.
- `loss_mitigation_characteristic.csv` whole.
- `.git/logs/HEAD` in both repos for the starting state.

## Sources

- **Primary:** Ning Ke and Hao Chunwen, *Dunhuang sheyi wenshu jijiao* (1997), Zotero `HTDVN55W`, read on the page images. The `(OCR)` file and the `(OCR text).txt` locate passages only; quotation from the images. Shelfmarks as S. / P. / BD; Chinese quoted in characters with a translation.
- **Secondary:** Teiser 2020 (`7DCXRHEX`; check the attachment opens); Hao Chunwen 2021, *Hualin International Journal of Buddhist Studies* 4.2 (check Zotero, then report open copies; no download without asking). Not held: Yamamoto and Dohi (eds), *Tun-huang and Turfan Documents* IV (Toyo Bunko 1988–89); report, do not acquire.
- **Non-independence, declared before the rows:** Ning and Hao and Teiser edit the same manuscripts, so they are one witness on the texts; Teiser's interpretation is a separate witness only where he argues beyond the text.

## Items, in order, each stopping for MS's ruling

1. **Scope and unit.** Recommended: one `loss_mitigation_forms` row for the *she*'s death mutual aid, coded from the death clauses of the practical bylaws, the 31 death circulars and the 29 death contribution registers; practical documents as evidence, models, drafts and students' copies as variants; Dunhuang, 9th–10th centuries, the Turfan bylaws of 658 comparison only. To rule: (a) whether the 義聚 loan stock (9 loan registers, 6 of member loans) is a second row or part of the first; (b) **decided: an `organizational_forms` row is deferred.**
2. **The corpus, counted by shelfmark** from the table of contents (page images): the practical bylaws, death circulars and contribution registers with dates, so the cells rest on counts, not samples. The preface counts recorded in the vault (pp. 7–21) re-checked.
3. **Priors per characteristic, before reading**, in `records/PRIORS-she-associations-2026-10-13.md`; **committed by MS before item 4.**
4. **Read and code**, characteristic by characteristic. Open questions first: `CN1` (a levy at the event, `ex-post-assessment`, against a standing stock; where the 義聚 matters); `PY0`–`PY2` (indemnity or draw on a life event; the guild rows are the precedent); `CN2`, `CN3` (the contribution rule and the fines 罰); `PY3` (whether fixed contributions cap the payout). Then `MB1`–`MB3`, `HZ1`–`HZ2`, `VF1`–`VF2`, `GV1` (社長 / 社官 / 錄事), `DR1`–`DR2`, and `LS1`–`LS3`, `RB1`–`RB4`, `PR1`. Each cell carries the documents it rests on (shelfmark, Ning and Hao page), a count where documents disagree, and confidence on the house scale.
5. **Co-occurrence declarations before the rows land:** `huiguan`, resemblance only, never descent, any likeness parallelism until descent is argued; the guild death-benefit rows, functional comparison only; in both directions where the column can carry it.
6. **Application:** type row minted with its scope note; rows into `data.csv` after a byte-identical round-trip check, ids from the live file; logbooks 2, 4 (results and the standing-table row) and 5; CHANGELOG block; no version bump unless the schema grows; full checks (sweep script rebuilt first); the vault note updated; a project doc.

## Hard rules

Never run git. No deletion or rename without MS's word; discards to `_to_delete/`. `records/` is verbatim. Commit messages in chat, hard-wrapped at 72. Reserved terms: convergence is not parallelism; hazard is not risk (death is a hazard); "genetic" only for biological heredity. Report counts, not samples.

## Out of scope

The `mudaraba` pass (after this batch); the irrigation (渠人) circulars except as a boundary note; the `huiguan` row itself.

## Flagged in passing, not repaired

The vault note cites the Ning and Hao attachment as `V5XHQ7EY` (image-only); that key is no longer among `HTDVN55W`'s children (now `VJ3VSQZJ` and `UE9ZV5MT`).
