# Venetian editions: regest years in the text layers against the page images (2026-11-05)

**Run by the assistant (`claude-opus-5-5`) on 2026-11-05 at MS's request ("edition-wide").** A check of the editions' current text layers, not of any record. Its consequences for the Venetian pass's records are in `CORRECTIONS-venetian-ocr-2026-11-05.md`.

Editions (Zotero attachment keys; layers as of 2026-11-05):

- Vol. I: Morozzo della Rocca & Lombardo 1940, `HMZ7K7BQ`, `Latin_best` layer of 2026-11-03 (printed page = PDF − 33).
- Vol. II: the same, `L4VTQIKI` (printed page = PDF − 7).
- *Nuovi*: Lombardo & Morozzo della Rocca 1953, `SFNBZ8D9`, `lat+ita` layer of 2026-11-02 (printed page = PDF − 13). Not used by any record in this repository.

## Method

A script compared each regest year in the text layer (`pdftotext -raw`) with the Latin dating clause of the same act, allowing *more veneto* (January–February one year later). Disagreements were read on the page image or, where the layer itself showed regest and Latin agreeing, triaged in the text as parser artefacts.

| edition | regest years found | agree (script) | flags checked | Latin clause not parsed |
|---------|--------------------|----------------|---------------|-------------------------|
| Vol. I  | 414                | 346            | 36            | 33                      |
| Vol. II | 364                | 319            | 15            | 30                      |
| *Nuovi* | 87                 | 69             | 14            | 4                       |

## A. Regest years wrong in the current text layer (14)

| ed. | doc. | PDF p. | printed (image) | text layer | note |
|-----|------|--------|-----------------|------------|------|
| I | 58 | 94 | 1130 | 1120 | damaged 3; same error in the 2026-10-24 layer |
| I | 73 | 109 | 1139 | 1159 | the 2026-10-24 layer had it right |
| I | 122 | 155 | 1156 | 1153 | damaged 6 |
| I | 156 | 187 | 116? (damaged); Latin 1162 | 1139 | see B |
| I | 213 | 244 | 1169 | 11693 | extra digit |
| II | 561 | 111 | 1215 | 1218 | |
| *Nuovi* | 5 | 19 | 1143 | 1149 | regest runs over to p. 6 |
| *Nuovi* | 13 | 28 | 1153 | 1158 | |
| *Nuovi* | 55 | 74 | 1203 | 1908 | |
| *Nuovi* | 70 | 90 | 1207 | 1907 | |
| *Nuovi* | 76 | 96 | 1213 | 1218 | document number also misread ("46") |
| *Nuovi* | 85 | 108 | 1223 | 1228 | the print itself disagrees with the Latin; see B |
| *Nuovi* | 95 | 125 | 1252 | 1952 | |
| *Nuovi* | 96 | 126 | 1253 | 1258 | |

In *Nuovi* every error is in the italic regest face: 3 read as 8, 2 or 0 as 9. 8 of 87 regest years (9%). In the 1940 volumes the errors are damaged roman digits: 6 of 778 found (under 1%).

## B. Discrepancies in the print itself

| ed. | doc. | regest | Latin | other evidence | reading |
|-----|------|--------|-------|----------------|---------|
| I | 133 | 1158 Sept. | 1159, ind. VII | endorsement 1159; no. 138 cites "1158 settembre Armiro" | the editors reckon ind. VII from September 1158; the regest is defensible |
| I | 156 | 116? (third digit damaged) | 1162, ind. X | endorsement (Att. XVII) 1172; nos. 155 and 158 are 1162 | 1162 |
| *Nuovi* | 85 | 1223 | 1233, ind. VI | ind. VI fits 1233 | the editors' misprint; 1233 |
| II | 495 | 1208 | «ducentesimo ducentesimo octavo» | — | doubled word in the edition; 1208 stands |

## C. Flags that were parser artefacts (regest correct in the layer)

- Vol. I: 8, 35, 52, 59, 61, 62, 93, 105, 106, 120, 124, 130, 138, 158, 237, 238, 252, 265, 301, 304, 309, 314, 317, 362, 363, 387, 395, 412, 413; "842" was a running head.
- Vol. II: 495, 579, 580, 612, 619, 633, 669, 687, 746, 767, 789, 804, 842; "3" was a running head.
- *Nuovi*: 44, 45, 61, 78, 87; "92" was a preface reference.

## D. Coverage

- **1940 volumes: superseded by the census sweep.** All 865 acts were checked through the census in `CORRECTIONS-venetian-ocr-2026-11-05.md`. 66 years there rest on the regest's numerals only; they are listed in that note.
- ***Nuovi*: not closed.** 4 acts with no Latin parse and 17 of 104 with no regest year read. No record depends on this edition.
