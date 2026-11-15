# Blind transcription: Yamamoto IV(A), Nos. 221–259 (納贈曆), 2026-11-15

**This is one of two identical bundles, A and B.** Two transcribers work from the same page images, independently and without sight of each other's output. Their disagreements go to MS for a ruling on the image. Nothing you transcribe is coded: the purpose is a working text, and a measured error rate for it.

## The edition

Yamamoto Tatsurō, Dohi Yoshikazu and Ishida Yūsaku, eds., *Tun-huang and Turfan Documents concerning Social and Economic History*, IV: *She Associations and Related Documents* (A) Introduction & Texts (Tokyo: Tōyō Bunko, 1989). Section IV, 納贈曆 (funeral-donation ledgers), Nos. 221–259. PDF pages 99–122; printed page = PDF page − 10 (the page number in brackets is the reverse pagination).

You transcribe **the printed edition**, not the manuscript. Where the editors print a misprint, a variant form or a character you think wrong, you transcribe what is printed and note your doubt in `out/LOG.md`. **Never correct toward the expected word.** In the pilot of 2026-11-10 the reference transcription silently regularised two readings (printed 盆 read as 益, printed 遶 as 遠). That is the error this pass exists to catch.

## What is in the bundle

- `pages/p-NNN.png`: the full page, 400 dpi greyscale, 4677 × 3307, landscape.
- `overview/p-NNN.png`: the same page at 1600 px wide, for layout only. Do not transcribe from it.
- `tiles/p-NNN-{top|bottom}-{1..4}.png`: each page cut into eight overlapping tiles. Strip 1 is the rightmost, strip 4 the leftmost; `top` and `bottom` overlap by about 8 per cent, as do neighbouring strips. **Transcribe from the tiles**, and go to `pages/` where a character falls on a tile edge.
- `MANIFEST.sha256`: hashes of every image. Do not modify any file outside `out/`.

The text runs in vertical columns, right to left. Each column carries its printed line number above it. Document numbers are printed in bold above the first column of each document, with the heading beside them and the shelfmark at the far left of the heading line (e.g. `S一八四五`).

## Orientation (verify on the page; the page is authoritative)

| PDF p. | Documents on the page |
|---|---|
| 99 | 221, 222, 223 (beg.) |
| 100 | 224, 225 |
| 101 | 226, 227 (beg.) |
| 102 | 227 (end), 228 |
| 103 | 229, 230 (beg.) |
| 104 | 230 (cont.) |
| 105 | 230 (end), 231 (beg.) |
| 106 | 231 (cont.) |
| 107 | 231 (end), 232 (beg.) |
| 108 | 232 (end), 233 (beg.) |
| 109 | 233 (end), 234, 235 (beg.) |
| 110 | 235 (end), 236 |
| 111 | 237, 238 (beg.) |
| 112 | 238 (end), 239 (beg.) |
| 113 | 239 (end), 240, 241 (beg.) |
| 114 | 241 (end), 242 |
| 115 | 243, 244, 245 (beg.) |
| 116 | 245 (end), 246 |
| 117 | 247, 248 (beg.) |
| 118 | 248 (end), 249 |
| 119 | 250, 251 (beg.) |
| 120 | 251 (end), 252 |
| 121 | 253, 254, 255, 256 |
| 122 | 257, 258, 259 |

## What to transcribe

For every document, 221 to 259: the document number, the heading as printed, the shelfmark as printed, and every numbered line of the main text, with its printed line number. Include the editors' parenthesised remarks that stand in the text column, such as `(中間11厘米空)`, `(後空)` and `(紙縫)`.

**Leave out** the editors' notes block (the paragraphs set apart lower on the page, opening with a circled sign and citing 釋錄 and other editions), the page numbers and the paper-size figures (e.g. `30.5×43`). Record in `LOG.md` that a page has such material, but do not transcribe it.

## How to write it

One UTF-8 file per document, `out/No-NNN.txt`:

```
# No. 231
# heading: 丙子年〔976〕四月十七日祝定德阿婆身故納贈曆
# shelfmark: S一八四五
# pages: 105-107
1	丙子年四月十七日祝定德阿婆身故納贈曆
2	社官氾
3	錄事李 幷粟 ⌜白細褐⌝三十五尺
```

- One printed line per row: the printed line number, a tab, the text. Sub-lines printed `a`, `b`, `c` under one number are written `1a`, `1b`, `1c`.
- A gap that the edition prints between the parts of a line (between a name and the goods) becomes a single space. Do not add punctuation the edition does not print; reproduce the punctuation it does print (、。).
- **Characters exactly as printed.** Keep variant and non-standard forms apart: 幷 / 并 / 併, 粟 / 栗, 己 / 已 / 巳, 斜, 褐, 麵 / 麪 / 麫, 爲 / 為, 衆 / 眾, 弘 / 紅, 疋 / 匹. If the printed form is not in Unicode, write the nearest code point and describe the form in `SIGNS.md`.
- **Your own uncertainty:** `[X?]` for a character you read as X but are not sure of; `[?]` for a character you cannot read at all, one per character. These are your marks, never the edition's.
- **The edition's own signs**, using these conventions so that A and B can be compared:

| Printed sign | Write |
|---|---|
| A rule beside a run of characters, with a tick at its head (e.g. beside 白細褐) | `⌜` before and `⌝` after exactly the characters the rule runs beside |
| A small character set beside the column (e.g. 小 beside 幷) | `{小}` immediately after the character it stands beside |
| An editorial reading in small parentheses beside a character (e.g. (紅) beside 弘) | `(紅)` immediately after that character |
| A date or reading in the heading in lens brackets (e.g. 〔976〕) | `〔976〕` |
| A printed question mark beside a character | `？` (full-width) immediately after the character |
| Corner quotes as printed (e.g. 「押」) | `「押」` |
| A square for a lost character | `□`, one per square |
| An open frame or rule standing for lost text of unstated length | `[lacuna]` |
| A vertical dotted line between columns | a row `⋮` with no line number, where it stands |
| Circled or parenthesised section numbers (㈠, (一)) | as printed |

Any sign not in this table: write the nearest Unicode character or a short `{sign: description}`, and record it in `SIGNS.md` with the page and the line the first time you use it.

## Order of work

1. Read this file. List `pages/`, `tiles/` and `overview/` and declare the counts in `LOG.md` (24, 192 and 24 expected).
2. Work page by page, PDF 99 to 122. For each page, read the overview for layout, then the tiles right to left, top then bottom. Write each document's file as you finish it; append to a file when a document runs onto the next page. Note in `LOG.md`, per page: the documents and line numbers on it, every `[?]` and `[X?]` with a word on why, and anything else you noticed.
3. When all 39 documents are written, check your own count: for each document, the last printed line number against the number of rows you wrote (sub-lines and `⋮` rows excepted). Record the check in `LOG.md`.
4. Write `out/SHA256SUMS` with the sha256 of every file in `out/`, and stop. Change nothing in `out/` after that.

**If your context runs low** before you finish, finish the document in hand, write `out/RESUME.md` stating the last page and line completed, and stop. A new session will continue from there with the same instructions.

## Rules

- Work only in this folder. Do not open the other bundle, any other folder, Zotero, the web, the claude.ai Project, past chats or any memory file. Do not use any OCR output or any other edition (Ning Ke and Hao Chunwen, 唐耕耦 釋錄 or others), even if you know them. If your context already holds a transcription of any of these documents, say so before starting, and stop.
- Do not normalise, complete or restore. A character the edition does not print is not in your transcription.
- Do not run `git`. Do not delete or rename anything.
