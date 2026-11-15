# Collation: the `she_death_aid` cells' register evidence against Yamamoto IV(A) (2026-11-15)

**Status: prepared by the assistant (`claude-opus-5-5`, effort `high`) at MS's request on 2026-11-15, after the adjudication of the Yamamoto ledgers pass (`records/RULINGS-yamamoto-ledgers-adjudication-2026-11-15.md`). One correction to a note is proposed below and not applied; no value moves.**

## What was collated

The 23 `she_death_aid` rows in `datasets/loss_mitigation_forms/data.csv` (LM-0763 to LM-0785) were coded from Ning and Hao 1997. Of the registers they cite, five are also in Yamamoto IV(A), Nos. 221–259, and so in the adjudicated text of 2026-11-15:

| N&H no. | Yamamoto no. | Rows citing it |
| --- | --- | --- |
| 219 (P. 2842/2) | 226 | LM-0782 |
| 220 (S. 4472v) | 230 | LM-0767, LM-0772 |
| 221 (P. 4975) | 233 | LM-0772 |
| 222 (S. 1845) | 231 | LM-0767, LM-0768 |
| 225 (S. 2472v) | 238 | LM-0767, LM-0768, LM-0772, LM-0778, LM-0781 |
| 228 (P. 2680v) | 241 | LM-0772 |

The other registers cited (N&H 214–218, 223, 224, 226, 227, 229–232) are either not in Yamamoto Nos. 221–259 or are cited for something no register line carries. The circulars, bylaws and petitions are outside Yamamoto's section IV and were not collated. The two editions read the same manuscripts, so agreement is a check on transcription, not a second witness.

## Results

| Row | Claim or quotation | Yamamoto (adjudicated) | Result |
| --- | --- | --- | --- |
| LM-0767, LM-0772 | 220: 見付凶家餅七百八十，又付凶家油三十合 | 230 l. 52: 見付凶家併七百八十「押」、又付凶家油三十合「押」 | Agrees in substance. The quotation silently takes N&H's emendation 併(餅) and drops the two (押) marks, which N&H also prints |
| LM-0767, LM-0772 | 225: 見付主人油三十一合，餅五百四十枚 | 238 l. 35: the same | Agrees |
| LM-0768, LM-0778, LM-0781 | 225: 眾社商量 … 自後長定; 每有納贈 … | 238 ll. 36, 38: 衆社商量 … 自後長定; 每有納贈之時 | Agrees. N&H prints 目(自); Yamamoto reads 自 |
| LM-0768 | 222: "bread and grain in all 62 entries, cloth in 23, 一丈一尺 to 三十五尺" | 231: 62 live entries (l. 42, 竹≀淸≀子≀, is cancelled); cloth in 23; 一丈一尺 (l. 36) to 三十五尺 (l. 3) | Partly false. Bread and grain in 55 of 62, not all: grain only in ll. 31, 32, 34 (its 幷 is cancelled), 35, 62; bread only in l. 25; nothing in l. 2. N&H's own text shows the same gaps, so the error is in the count, not in the edition |
| LM-0772 | 主人 among the givers in 221 and 228 | 233 verso l. 1 (主人 …); 241 l. 6 (主人 …) | Agrees |
| LM-0782 | 219 dated 949 | 226, 己酉年〔949〕 | Agrees |

## Proposed correction, not applied

LM-0768 (`she_death_aid` CN2 = `equal`, high). The value stands: the claim it supports is that registers vary in cloth above all, and the cloth count (23 of 62) is right. In the note, replace "bread and grain in all 62 entries, cloth in 23" with "bread and grain in 55 of 62 entries (grain alone in five, bread alone in one, one entry blank), cloth in 23". Applying it is a change to `data.csv` and waits for MS.

## Two observations for the next coding from these registers

- **Yamamoto's ≀ is a cancellation mark.** N&H omits every character Yamamoto marks with it (231 ll. 33, 34, 42, 50/51). A count of entries or items from Yamamoto must drop marked characters, as the count above does.
- **Quotations should mark emendations.** Where N&H prints an emendation in parentheses, a quotation should keep it in that form (併(餅)), or take the manuscript reading. It should not take the emended reading silently.

## Applied

**2026-11-15, 19:05 JST: MS, "yes, apply the new count."** The LM-0768 note in `datasets/loss_mitigation_forms/data.csv` now reads "bread and grain in 55 of 62 entries (grain alone in five, bread alone in one, one entry blank), cloth in 23", with a pointer to this file. The value is unchanged. `records/proposed-rows-she-associations-2026-10-13.csv` and `records/RULINGS-she-associations-2026-10-13.md` keep the original wording, as records.
