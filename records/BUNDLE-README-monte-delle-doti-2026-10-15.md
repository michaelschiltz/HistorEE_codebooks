# Blind bundle: the Florentine *monte delle doti* (built 2026-10-15)

You are coding **one new form** into `loss_mitigation_forms`. This bundle is deliberately minimal. Everything you may use is here, and nothing outside it may be consulted. The kickoff prompt carries the full instructions; this file says what is where.

## Contents

- `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `EDITING-CSV.md`: the doctrine. Read all four before anything else. CONTRIBUTING §4 holds the missingness rules and the original-script convention.
- `PRIORS-monte-delle-doti-2026-10-15.md`: the priors template. Copy it to `PRIORS-monte-delle-doti-filled-<date>.md`, fill the copy **before opening `sources/`**, print its sha256, and stop.
- `datasets/loss_mitigation_forms/`: the live `data.csv`, `recodings.csv` and `datapackage.json`. The form you are coding has no rows here. The other rows are house practice: read their notes for how cells are argued and cited.
- `vocabularies/loss_mitigation_characteristic.csv` (the `exemplar` column has been removed) and `vocabularies/loss_mitigation_type.csv`. Every `definition`, `allowed_values`, `applicability_on` and `locator` is binding.
- `views/loss_mitigation_forms--risk-pooling.md`: the committed comparative view. Read its second line, which states its filter. There is no `build_views.py` in this bundle, on purpose.
- `scripts/`: `check_vocabularies.py`, `check_dependence.py` (pass it the dataset **directory**), `check_quotations.py`. Run them on a scratch copy, never on the bundle's own files.
- `sources/`: below.
- `proposed-of/`: empty. Everything you produce goes here.

## Sources, with page maps

Cite **printed** pages in `source_ref`. Each file's page map is exact; it was measured on page-edge numbers.

| file | what it is | file page → printed page |
|---|---|---|
| `kirshner-molho-1978_jmh50_pp403-438.pdf` | Julius Kirshner and Anthony Molho, "The Dowry Fund and the Marriage Market in Early Quattrocento Florence", *Journal of Modern History* 50, no. 3 (1978): 403–438, doi:10.1086/241732 | printed = file + 402 |
| `kirshner-molho-1978_p403_ocr.txt` | OCR of p. 403, which has **no text layer** in the PDF | p. 403 only |
| `molho-1994_frontmatter_title-cip-contents-dates.pdf` | Anthony Molho, *Marriage Alliance in Late Medieval Florence* (Cambridge, MA: Harvard University Press, 1994), Harvard Historical Studies 114: title, copyright/CIP, contents, Note on Dates | front matter |
| `molho-1994_ch2-3_pp27-127.pdf` | Molho 1994, ch. 2 "The Monte delle Doti" (27–79) and ch. 3 "Investors and Beneficiaries" (80–127) | printed = file + 26 |
| `molho-1994_app1-sources_pp351-360.pdf` | Molho 1994, Appendix 1, "Sources" | printed = file + 350 |
| `molho-1994_ms-sources-abbreviations_pp433-434.pdf` | Molho 1994, "Manuscript Sources and Their Abbreviations" | printed = file + 432 |
| `kirshner-2015_frontmatter_title-copyright-contents-origpub-abbrev.pdf` | Julius Kirshner, *Marriage, Dowry, and Citizenship in Late Medieval and Renaissance Italy* (Toronto: University of Toronto Press, 2015), doi:10.3138/9781442664517: title, copyright, contents (file 1–4), "Original Publication Information", p. 215 (file 5), Abbreviations, pp. 239–240 (file 6–7) | as stated |
| `kirshner-2015_ch4_pp94-113_app4_pp230-231_notes_pp292-309.pdf` | Kirshner 2015, ch. 4 "The Morning After: Collecting Monte Dowries in Renaissance Florence" (file 1–20 = pp. 94–113); Appendix 4 (file 21–22 = pp. 230–231); the chapter's endnotes (file 23–40 = pp. 292–309). **p. 309 also carries the first notes of ch. 5, which is out of scope.** | as stated |
| `morrison-kirshner-molho-1977_aje106_pp487-492.pdf` | Alan S. Morrison, Julius Kirshner and Anthony Molho, "Life Cycle Events in 15th Century Florence: Records of the Monte delle Doti", *American Journal of Epidemiology* 106, no. 6 (1977): 487–492, doi:10.1093/oxfordjournals.aje.a112496 | printed = file + 486 |
| `morrison-kirshner-molho-1985_ajph75_pp528-535.pdf` | Morrison, Kirshner and Molho, "Epidemics in Renaissance Florence", *American Journal of Public Health* 75, no. 5 (1985): 528–535, doi:10.2105/AJPH.75.5.528 | printed = file + 527 |

## Reading notes

- **Text layers.** Molho 1994 is a library scan with an OCR text layer of uneven quality. Kirshner & Molho 1978 and the two Morrison articles are scans with hidden text. **Read every figure that will enter a cell from the page image** (`pdftoppm -r 200 -png -f N -l N file.pdf out`), never from the text layer. Kirshner 2015 is a typeset PDF, so its text layer is reliable, but a table should still be checked against the page. **Check the OCR of p. 403 against its page image before any cell rests on it.**
- **Dates.** Florentine documents date the year from 25 March. A date written `1466/7` falls between 1 January and 24 March 1467, modern style. Molho's Note on Dates is in the front-matter file.
- **Abbreviations.** Archival citations in Molho's notes (e.g. `PR`) are expanded in the abbreviations file. Kirshner's are expanded in pp. 239–240.
- **More pages.** If a cell needs a passage that is not here, do not guess and do not code from memory. Name the work, the page range and the cell it would move, and ask. MS decides.
