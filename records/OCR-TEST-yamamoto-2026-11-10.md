*Verbatim copy, made 2026-11-15 under `records/RULINGS-count-audit-2026-11-15.md` (ruling 2), of the Claude project document `claude/yamamoto-she-ocr-pilot-2026-11-10.md` (project "Ergodicity economics and history"). Nothing below this line is changed.*

---

# Yamamoto, *She Associations* IV(A) — OCR pilot, 2026-11-10

**Edition.** Yamamoto Tatsurō, Dohi Yoshikazu and Ishida Yūsaku, eds., *Tun-huang and Turfan Documents concerning Social and Economic History*, IV: *She Associations and Related Documents* (A) Introduction & Texts (Tokyo: Tōyō Bunko, 1989). Zotero item 9XU6924V (mis-filed on the 1978 series record); transcriptions PDF = attachment DG452E53, 155 pp.

**OCR under test.** Tesseract `tessdata_best` `chi_tra_vert`, `--psm 5`, 400 dpi greyscale, `preserve_interword_spaces 1`. Output in `~/ocr/yam_texts/p-NNN.txt`.

**Reference.** Claude's transcription of the main text block of five pages from zoomed page images (`~/ocr/yam_pilot/ref_pNNN.txt`): headings and editorial glosses included, notes column and line numbers excluded. Characters Claude could not read with confidence are marked `[?]` and excluded from scoring (13 characters, all on p. 128).

## Pages

| PDF p. | Ed. p. | Documents | Type |
|---|---|---|---|
| 21 | 11 | Nos. 14 (end), 15 | *she* by-laws (立社條件) |
| 25 | 15 | Nos. 21 (end)–25 | petitions to join / leave (投社狀, 除名狀) |
| 38 | 28 | Nos. 56–59 | circulars (社司轉帖) |
| 105 | 95 | Nos. 230 (end), 231 | funeral-donation ledger (納贈曆) |
| 128 | 119 | No. 269, ll. 28–61 | banquet ledger, Pingkang (官齋籍) |

## Results

Recall = share of the printed Han characters that the OCR reproduces in sequence (difflib alignment; 爲/為, 衆/眾 and similar standard-form pairs normalised). Extra characters from the notes column do not count against the OCR on this measure.

| PDF p. | Ref. chars | Recall |
|---|---|---|
| 21 | 615 | 80.2% |
| 25 | 328 | 75.0% |
| 38 | 349 | 73.6% |
| 105 | 382 | 44.8% |
| 128 | 680 | 79.4% |
| **all** | **2,354** | **72.5%** |

Key-character recall across the five pages:

| Char. | Recall |
|---|---|
| 社 | 13/34 |
| 粟 | 0/26 |
| 褐 | 2/28 |
| 幷 | 0/23 |
| 併 | 6/14 |
| 麵 | 16/20 |

Recurrent substitutions (printed → OCR): 罰→器, 奴→叔, 粟→栗/林/村, 丈→支/媽, 社→及/竺, 如→加, 令→合, 牒→膩, 幷→反/知, 褐→福, 斜→錠/狡, 闍→閣, 己→已.

## Reading

- About a quarter of the printed text is lost or wrong overall. The loss is not random: it falls on exactly the terms that carry the institutional and quantitative content (社, 粟, 褐, 幷).
- The funeral-donation ledger (p. 105) is the worst page at under half. Its commodity columns are unusable. The banquet ledger (p. 128) scores well only because personal names are common characters; its role headings (餬餅頭, 䭔子 and the like) are rare characters and mostly wrong.
- The OCR layer will not support term counts, amounts, or quotation. It is adequate for locating a document by number, date or personal name.

## Caveat on the reference

Claude's reading is not a gold standard. A targeted re-check of p. 21 found two silent regularisations toward the expected wording (益 for printed 盆; 遠 for printed 遶). The OCR was also wrong at both points, so comparing against the OCR would not have caught them. Thirteen rare characters on p. 128 remain unresolved and need Michael's eye.

## Recommendation

1. **Working text from page images, not from the OCR layer.** Claude transcribes from the zoomed images, document by document.
2. **Independent second transcription, then diff.** A second blind transcription is made without sight of the first; disagreements and `[?]` characters go to Michael for adjudication. The OCR is used only as a third flag, never to clear a reading. This applies the 2026-11-03 rule on printed editions: a text layer can show that a reading is present, but never clears one.
3. **Order of work.** Ledgers (Nos. 221 ff.) first, since that is where the OCR fails worst and where the quantitative data sit.

## Addendum: English introduction (BTS84G8X, 56 pp.)

`ocrmypdf -l eng+chi_tra --tesseract-pagesegmode 3 --oversample 400`. Output: `~/ocr/yamamoto_IVA_intro_ocr.pdf` (3.7 MB) and sidecar `yamamoto_IVA_intro.txt`. Spot-checked against the page images on pp. 12 (ToC), 38 and 40 (two-column prose).

- **Prose.** Near-clean; the only errors on pp. 38 and 40 are stray quotation marks and one stray character.
- **Numerals in prose.** Mostly right, but not reliably: p. 40 has "Nos. 228–238" for the printed 223–238.
- **Inline characters.** About half are lost or garbled, worst on single characters:
  - lost or garbled: 粟→"38", 油→"YH", 麪→"$i", 餅→"8", 廿→"I"/"1", 卅→"#1", 納贈人某々→"EZ AF 4"; 布帛 → 布吊.
  - correct: 局席, 二月社, 麥, 十三, 八日, 五日 (with spaces inserted between characters).
- **Table of contents.** Structurally broken:
  - document numbers split off from their titles into a separate column (227–229 read as "997.–999.");
  - subscript sigla garbled (S. 3005₁ → "S.3005;", P. 2915 piece2-1 → "2915pgg");
  - dot leaders turned into junk;
  - page numbers survive.

**Verdict.** Fine as a searchable reading layer. Document numbers, sigla and inline characters used in coding are checked against the image (rule of 2026-11-03). The ToC should be rebuilt by hand as a concordance (No. → title → date → siglum → page), not corrected from the OCR.
