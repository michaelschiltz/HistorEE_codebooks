# Ruling: the comanda cells recounted on the image-read records (2026-11-05)

**Status: ruled by MS in chat on 2026-11-05.** He asked whether the profit-share keys had been entered correctly. The answer was that the note on `comanda LR3` still said "all one quarter", and the recount tranche (`proposed-of/RECOUNT-comanda-madurell-2026-11-03.md`) was put to him. He ruled: "Absolutely; also check whether there are other stale notes/cells". Applied by the assistant (`claude-opus-5-5`) the same day.

**What changes.** The notes of 21 cells in `datasets/organizational_forms/data.csv` (15) and `datasets/loss_mitigation_forms/data.csv` (6) change. **No value, confidence, articulation, `source_ref`, `coder_model` or `coder_effort` changes.** Each note gains one bracketed addition opening `[2026-11-05, recount on the image-read records …]`. Where a quotation in a note carried an OCR form, the quotation is corrected in place and the addition says so. The `recodings.csv` rows of the 2026-10-27 blind pass are the record of that pass and are not touched.

**The convention** is that of ruling 8 of `records/RULINGS-comanda-primary-adjudication-2026-10-27.md` for a note-only change: value and basis unchanged, no new recodings row, one bracketed addition per cell.

## The counts

These are recomputed from `records/instances-2026-11-03.csv` and `records/instance-chars-2026-11-03.csv`. The rulings that changed the sample are in `records/RULINGS-madurell-translation-2026-11-03.md`, and the corrections in `records/CORRECTIONS-madurell-translation-2026-11-03.md`.

The sample (mod3 `comanda` instances) goes from 45 to 71:

- **26 enter.** 25 move from `neither` by ruling, and 2 are split acts (`CMD-174-2`, `CMD-204-2`), less `CMD-105-1`, which moves to `neither` by D105.
- **27 rest on a ruling** (abbreviated, salvage or incorporated loss terms).
- **26 carry cells derived** from the instance fields by the 2026-10-27 coder's own mapping, not reread.

| cell | record | 2026-10-27 | 2026-11-05 |
|---|---|---|---|
| `comanda` CF2 | OF-0866 | 44 of 45; census 142 of 145 | 70 of 71; census 199 of 202 (exceptions docs 3, 191, 220) |
| `comanda_alloc` RB1, RB4 | LM-0743, LM-0746 | 44 of 45 | 70 of 71 |
| `comanda_alloc` RB3 | LM-0745 | 41 of 45 | 66 of 71 (1 mixed, 4 silent) |
| `comanda` LP2 | OF-0837 | 42 of 45 | 69 of 71 by cell (26 derived) |
| `comanda` CI1, CF3 | OF-0847, OF-0867 | 42 of 45 | 67 of 71 |
| `comanda` CI3 | OF-0849 | 8 of 45 | at least 8 of 71 (not derived) |
| `comanda` LR2 | OF-0852 | 41 of 45 | 68 of 71 |
| `comanda` LR3 | OF-0853 | 41 shares, all ¼ | 68 shares: 66 ¼, 1 ⅛ (doc 189), 1 ⅓ (doc 240) |
| `comanda` CF1 | OF-0865 | 41 of 45 | 68 of 71 |
| `comanda` CI5 | OF-0900 | 23 of 45 | 33 of 71 |
| `comanda` TS2 | OF-0844 | 40 / 2 / 3 | 65 single-venture / 2 fixed-term / 4 open |

## What else was found stale, and corrected

The search ran over every `comanda`, `comanda_alloc`, `comanda_ad_societatem` and `comanda_ad_societatem_alloc` cell and every cell citing Madurell. It used a pattern sweep for counts, superseded conventions, the docs whose reading or form changed on 2026-11-03, and OCR forms. Separately, the 56 quotations that cite a document were checked against the image-read transcriptions of the translation.

- **Quotations carrying OCR forms**, corrected in place:
  - OF-0843 (*ete* → *etc.*);
  - OF-0844 (*hine* → *hinc*);
  - OF-0857 and OF-0860 (*J acobo* → *Jacobo*);
  - OF-0860 (*hee* → *hec*);
  - LM-0743 (*ad Dei vestrum* → *ad voluntatem Dei et ad vestrum*);
  - LM-0749 (*süper* → *super*).

  One flagged quotation, on OF-0853, is from the editor's study, not from an act, and is correct.
- **The assignment convention.** OF-0866 described abbreviated acts as assigned to the neither row and recorded ruling D1 of 2026-11-01. Both are superseded by D-ABBR, D-BELL, D-SALV and D-SIM.
- **Doc 105** was cited in LM-0743 as the time-limited form of a comanda risk clause. It is now `neither` (D105). Doc 189 is named as the within-row instance, and "periculum" first enters a sample clause in 1351 (doc 108), not 1349.
- **Doc 191's "sea"** (LM-0743) and **doc 122's "surety"** (LM-0745) are withdrawn.
- **The commissions of docs 214 and 238**, reported but unread in LR2 and LR3, are now read: 2 + 2 and 2 + 3 per cent, on goods out and goods back. Docs 218 and 233 give the agent no share. They are recorded in OF-0852, OF-0853 and LM-0747.
- **OF-0849 CI3.** Its reason for LOW was that the cessions sit in acts assigned to the neither row. That no longer holds for docs 213 and 217, which are `comanda` by D-ABBR. LOW is kept on the order clause's minority status, and the confidence is left for MS to revisit.
- **LM-0741 MC1.** The note quoted the census's "15th c." for doc 255; the census now carries the editors' dating.

## Not changed

- The values. Every recount confirms the modal state already coded. **Ruling-dependence:** 27 of the 71 sample instances enter by ruling, so the higher counts are not independent evidence for the boundary cells.
- `recodings.csv`, the vocabularies and the type rows. No type-row `key_source` carried a stale count.
