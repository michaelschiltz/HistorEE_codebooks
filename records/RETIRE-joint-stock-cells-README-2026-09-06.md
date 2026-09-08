# Retiring `OF-0032` and `OF-0033` — the id-policy question this forces, which is MS's

> **APPLIED 2026-09-06.** MS chose option (a), gaps. `OF-0032` and `OF-0033` are removed; `data.csv` is 801 rows running `OF-0001`–`OF-0803`. See logbook 1, 2026-09-06 (ii) for the id policy and logbook 2, 2026-09-06 (ii) for the removal. This file is kept as the record of the choice.

Companion to `proposed-retire-joint-stock-cells-2026-09-06.csv`. Reasoning at logbook 2 and logbook 4, 2026-09-06.

**Why this is not applied.** Deleting rows the session did not create is reserved to the maintainer (`run-a-coding-batch`, "Yours, always"). MS licensed this session to **recode** the two cells; recoding is not the available repair, because neither cell has a correct value on this row — the defect is the row, not the values. So the licence was given and could not be exercised, and what the cells need instead is removal.

**The choice, and it is a first for this census.** `record_id` currently runs contiguously `OF-0001` to `OF-0803` with no gaps. Removing two rows means choosing one of:

**(a) Leave the gaps.** `data.csv` goes to 801 rows; `OF-0032` and `OF-0033` simply do not exist; the last id stays `OF-0803`. **Cost:** the sequence is no longer contiguous, and any future check that assumes contiguity would have to be relaxed. **Benefit:** every `record_id` ever quoted in a logbook, a CHANGELOG block or a proposal still points at the same cell. Nothing else in the repository moves.

**(b) Renumber.** `data.csv` goes to 801 rows numbered `OF-0001`–`OF-0801`. **Cost is large and mostly invisible: 771 rows change their id**, every generated file changes, and **every `record_id` quoted anywhere in the logbooks now points at a different cell than it did** — `OF-0158`, cited at logbook 1, 2026-08-31 (iv) as `nakai_fictive_household LP3`, would silently become something else. There is no mechanism in this repository for rewriting those references. **Benefit:** contiguity is preserved.

**The recommendation is (a)**, and the reason is the second cost of (b): this census's logbooks cite `record_id`s as evidence, so renumbering does not merely churn a file, it falsifies the record. Contiguity is a convenience; a citation that still resolves is not.

**Whichever is chosen**, the application must also: regenerate `codebook.md` and all nine views (the row count and the `owner-shielding` and `legal-personality` views all change); record in the CHANGELOG what the columns actually lose — ~~`AP3=P` falls from two instances to one (`bazacle_mill` alone)~~ **CORRECTED 2026-09-06 (iii): `AP3=P` has three instances (`bazacle_mill`, `partenrederij`, `joint_stock`) and falls to two, so it keeps its discriminating power; `LP1=1` falls ×6 → ×5 and the remainder is this row's own children plus `bazacle_mill`**; and remove the interim-state sentence from `joint_stock`'s `key_source`, which currently tells readers to treat both cells as withdrawn.
