# NOTES — what Morozzo della Rocca & Lombardo (1940) select: a measured pass over the 865 printed acts

**Operator-side record. Hold from any coder.** The measured direction below (what the edition over- and under-prints, and where the commenda evidence sits) would prime a blind coder. Nothing here goes into a bundle, a prompt or a PRIORS file for the Venetian pass. Written 2026-10-25 by `ai` (`claude-opus-5-5`), at MS's request ("Yes, go ahead"), as the first step of the Venetian pass. **No data change**: no `data.csv` or `recodings.csv` row is touched.

## 1. Why measure the edition first

The 32 pending commenda-arm rows (14 `commenda_alloc` and `societas_maris` cells) are carried into a pass that will confront them with the Venetian acts. An edition is a selection twice over: by what survived in the archives and by what the editors chose to print. Before any cell is read against these volumes, the selection has to be known, or the pass will mistake the shape of the archive for the shape of the institution.

## 2. Inputs

- Vol. I: Zotero attachment `HMZ7K7BQ` (item `GXRRAIUK`), file `Morozzo della Rocca and Lombardo - 1940 - Documenti del commercio veneziano nei secoli XI–XIII 1.pdf`, SHA-256 `a35ba9e45d31fcbc58a129125b1f48150feaa5bff2701f2beab823797d37c1a7`, 495 pages; printed page = PDF page − 33.
- Vol. II: attachment `L4VTQIKI`, file `… XI–XIII.pdf`, SHA-256 `a0e30104f7e7288aea347547d3ebee1bf3700bfb1695a0b76894284ea9ba7689`, 477 pages.
- Text layer: the OCR of 2026-10-24, extracted with `pdftotext` 22.02 in default mode (vol. I 1,194,181 characters, SHA-256 `23befe9f…2418772`; vol. II 1,168,960, `9900e261…a48b91`). The extracts are not committed: they contain the editors' regests and apparatus (`records/README.md`, "Source text taken from modern editions").
- Copy: BEIC digital reproduction, CC BY-NC-ND 3.0. The committed CSV carries no text of the edition, only act numbers, archival signatures reduced to their fondo, dates, places and this pass's own classifications.

## 3. What the editors say they did (vol. I, introduction, pp. v–xxx)

- **Provenance.** S. Zaccaria 506 parchments; other convents 25; Procuratori di S. Marco 151 (100 + 51); Cancelleria Inferiore (the 1812 deposit) 164; miscellanies 27; about 873 in all. Inside S. Zaccaria the family dossiers are Mairano 118, Stagnario 59, da Molin 54, Gradenigo 47, Serzi 41, Aimo 36.
- **Survival rule.** Charters were deposited with a convent or the Procuratori and normally handed back when the obligation was discharged, so what survives is a residue gathered around the tractators who received the money and later held the cancelled contract and the quittance. The Procuratori fonds hold forced executions and claims that could not be collected.
- **Inclusion (p. xx).** Acts showing an intent to gain by a temporary transfer of wealth; cut-off 1261.
- **Deliberate exclusion (p. xix).** The case files (*processi*) are left out.
- **Duplicates.** An exemplum is printed in full even where its mater is printed too.
- **Classification by opening formula (p. xxviii).** *Manifestus sum* (obligations), *plenam et irrevocabilem securitatem* (releases), *Testificor* (attestations).
- **Already published.** 60 documents (36 by Baracchi, 17 by Sacerdoti).

## 4. Method

**Segmentation.** The text layer was cut into the 865 numbered acts (vol. I 1–466, vol. II 467–865). 781 act headers were found as printed numbers in a monotone sequence; 78 more were recovered where the OCR misread the number (`89.` for 99, `188.` for 158, `$61.` for 661, `769.` for 760, `9551.` for 551 and the like) or lost it, by counting each act's archival line (condition and size, e.g. "Buona - 125x311") between two secure headers; 6 were placed by hand after reading the text. Acts 269, 271, 270 are printed in that order. The positions are in `SCRIPTS-…/positions.json`, with how each was found.

**Fondo** is read from the archival line of each act (S. Zacc., Proc. di S. Marco, Canc. Inf. Busta …, S. Giorgio Magg., Museo di Paleografia with its provenance, and so on), falling back on the busta number where the OCR lost the fondo's name. **Date** is the first year in the editors' regest. **Place** is the place before that date. **Act type** is taken from the dispositive formula that opens the Latin text (*Plenam et irrevocabilem securitatem*, *Manifestus sum / Manifestum facio / Accepi ego*, *Testificor*, *Committens committo*, *Promittens promitto*, a sentence, a testament, a sale); where the formula is the general *Manifestus* or is unreadable, the type comes from the editors' regest (investment, loan, sea loan, freight, obligation for goods received), and acts the editors print as "Lo stesso da …" inherit the type of the act they continue. A series of flags is set from the archival line and endorsements: copy (*Copia*), incised charter (*Carta incisa*), previously edited (*Edita da …*), Mairano dossier, investment-related (the regest names a colleganza, compagnia, a sum "per commerciare", traffics or common dealings), written overseas.

This is description, not coding: no characteristic is coded and no cell is touched. The categories are the edition's own (formula and regest), not the matrix's.

## 5. Checked against the page images

Pages were read as images through the Zotero connector, not through the text layer.

- **First random sample** (20 acts, seed 1940) and **5 further acts** read while building. Fondo right in 24 of 25 (act 297: the script left it unresolved; the page has S. Zacc. B. 25). Four type errors, all from reading the regest verb "dichiara" as an attestation (303 a cession of a claim, 315 a release, 328 a promise of indemnity, 436 a sale), and two date errors from taking the earliest year in the head, which can be an endorsement's (52, 297). **The rules were changed in response**: type from the dispositive formula, date from the regest only. This sample therefore does not measure the final error rate.
- **Second random sample** (12 acts, seed 1261, drawn after the rules were fixed). Fondo 12 of 12; date 12 of 12; type 11 of 12. The error (690) was systematic: the "Lo stesso da …" series in Canc. Inf. had not inherited the type of the act it continues; fixed, which moved 21 acts into "investment contract". **Incision missed once** (811): the page has "Carta incisa", the text layer lost the line. Places were not extracted for 3 of the 37 acts checked.

What follows from the checks: fondo and date are reliable; act type is reliable for the large classes and should be read at ± a few acts for the small ones; **the incised count is a lower bound**; place is missing for 84 acts, so overseas counts are lower bounds too. Every act checked is marked in the CSV's `image_check` column.

## 6. Results

### 6.1 Fondi: the measurement against the editors' counts

| fondo                      | editors | measured |
| -------------------------- | ------- | -------- |
| S. Zaccaria                | 506     | 502      |
| Procuratori di S. Marco    | 151     | 153      |
| Cancelleria Inferiore      | 164     | 162      |
| other convents             | 25      | 25       |
| miscellanies               | 27      | 14       |
| unresolved                 | —       | 9        |
| total                      | c. 873  | 865      |

Agreement within a handful in each fondo. The editors count parchments, the measurement counts numbered acts; the shortfall in miscellanies sits mostly in the 9 unresolved.

### 6.2 Act type by fondo

| act type                        | S. Zaccaria | Procuratori | Canc. Inferiore | other convents | miscellanies | unresolved | all |
| ------------------------------- | ----------- | ----------- | --------------- | -------------- | ------------ | ---------- | --- |
| release (securitas)             | 250         | 47          | 40              | 9              | 4            | 4          | 354 |
| investment contract             | 44          | 64          | 45              | 6              | 4            | 1          | 164 |
| attestation                     | 51          | 13          | 13              | 0              | 0            | 2          | 79  |
| mandate (procura)               | 42          | 12          | 19              | 1              | 0            | 0          | 74  |
| loan / deposit                  | 38          | 8           | 12              | 3              | 3            | 0          | 64  |
| sea loan / exchange             | 19          | 1           | 5               | 0              | 0            | 2          | 27  |
| judgment / process              | 11          | 2           | 3               | 0              | 1            | 0          | 17  |
| obligation to pay (credit sale) | 7           | 1           | 2               | 3              | 0            | 0          | 13  |
| promise / guarantee             | 10          | 0           | 2               | 1              | 0            | 0          | 13  |
| freight / ship                  | 6           | 3           | 1               | 1              | 1            | 0          | 12  |
| cession of claim                | 7           | 2           | 3               | 0              | 0            | 0          | 12  |
| testament                       | 5           | 0           | 6               | 0              | 0            | 0          | 11  |
| property / sale / pledge        | 3           | 0           | 5               | 1              | 0            | 0          | 9   |
| other                           | 7           | 0           | 1               | 0              | 0            | 0          | 8   |
| ducal / authentication          | 1           | 0           | 5               | 0              | 1            | 0          | 7   |
| servile / labour                | 1           | 0           | 0               | 0              | 0            | 0          | 1   |
| total                           | 502         | 153         | 162             | 25             | 14           | 9          | 865 |

### 6.3 Act type by period

| act type                        | <1150 | 1150-1199 | 1200-1229 | 1230-1261 | undated |
| ------------------------------- | ----- | --------- | --------- | --------- | ------- |
| release (securitas)             | 60    | 177       | 72        | 43        | 2       |
| investment contract             | 3     | 17        | 43        | 99        | 2       |
| attestation                     | 11    | 41        | 18        | 9         | 0       |
| mandate (procura)               | 0     | 26        | 29        | 19        | 0       |
| loan / deposit                  | 11    | 27        | 10        | 16        | 0       |
| sea loan / exchange             | 2     | 18        | 6         | 1         | 0       |
| judgment / process              | 1     | 6         | 7         | 3         | 0       |
| obligation to pay (credit sale) | 1     | 5         | 3         | 4         | 0       |
| promise / guarantee             | 2     | 9         | 1         | 1         | 0       |
| freight / ship                  | 3     | 4         | 1         | 4         | 0       |
| cession of claim                | 2     | 6         | 1         | 3         | 0       |
| testament                       | 0     | 4         | 3         | 4         | 0       |
| property / sale / pledge        | 2     | 1         | 3         | 2         | 1       |
| other                           | 0     | 1         | 3         | 4         | 0       |
| ducal / authentication          | 0     | 0         | 2         | 5         | 0       |
| servile / labour                | 0     | 1         | 0         | 0         | 0       |
| total                           | 98    | 343       | 202       | 217       | 5       |

### 6.4 Fondo by period

| fondo           | <1150 | 1150-1199 | 1200-1229 | 1230-1261 | undated | all |
| --------------- | ----- | --------- | --------- | --------- | ------- | --- |
| S. Zaccaria     | 86    | 280       | 100       | 34        | 2       | 502 |
| Procuratori     | 0     | 6         | 48        | 98        | 1       | 153 |
| Canc. Inferiore | 4     | 34        | 45        | 78        | 1       | 162 |
| other convents  | 7     | 14        | 2         | 2         | 0       | 25  |
| miscellanies    | 0     | 2         | 6         | 5         | 1       | 14  |
| unresolved      | 1     | 7         | 1         | 0         | 0       | 9   |

### 6.5 What the tables say

1. **Before 1200 the edition is a corpus of quittances.** Releases are 61% of the acts before 1150 and 52% in 1150–1199; investment contracts are 3% and 5%. For the twelfth century there are **20 investment contracts against 100 investment-related releases**. The twelfth-century colleganza is seen mainly through its discharge.
2. **The releases do not carry the terms.** Of the 166 investment-related releases, 70 abbreviate the contract they discharge ("et cetera ut in ea legitur" and its variants) and **7 mention the sea-and-people peril at all**. Of the 164 investment contracts, 158 carry a peril clause.
3. **What survives was settled.** At least 69 of the 164 investment contracts are incised charters, i.e. cancelled on discharge (act 389's endorsement: "nullius valoris quia omnes incisae sunt"); 3 of the 354 releases are. Ventures that ended in loss reach the edition by another road: attestations and judgments (96 acts, of which 18 name an investment), and attestations of the loss itself (a shipwreck off Rhodes, act 83; a crew taken by an imperial galley, act 336).
4. **The contract changes across 1200, and so does the fondo.** The bilateral marker (the working party's own stake, *posui ibidem*) is in 7 of the 17 contracts of 1150–1199, 3 of 43 in 1200–1229 and 0 of 99 in 1230–1261. The quarter-share formula (*capitaneam cum tribus partibus de toto prode … retenta michi quarta parte*, the investor bearing the peril) is in 2 of 17, 32 of 43 and 85 of 99. The word *colleganza/collegancia* is in 12 of 17, 3 of 43, 0 of 99. In 1230–1261, 91 of the 99 contracts come from the Procuratori and the Cancelleria Inferiore, whose investors include estates under administration, widows and wards. Period and fondo are confounded: the edition cannot by itself say whether the instrument changed or the archive that kept it did.
5. **One dossier weighs on the twelfth century.** 103 of the 343 acts of 1150–1199 (30%) belong to the Mairano dossier; 78 of its 106 acts are releases.
6. **Duplicates and earlier editions.** 91 acts are flagged as copies; 22 adjacent acts have near-identical regests (9 of them also flagged as copies); 52 were already edited before 1940 (the editors give 60).
7. **Written overseas.** At least 195 acts (23%) were drawn up overseas, 110 of the 343 of 1150–1199 (32%), mainly in Constantinople, Acre, Candia, Alexandria and Almyros (places on the Italian mainland not counted).

## 7. What this means for the Venetian pass (recommendations, for MS to decide)

1. **Two strata, never one modal instance.** Recommendation: read twelfth-century and thirteenth-century Venetian contracts separately, and say in the note of any cell which stratum it rests on. The 1150–1199 contracts include bilateral colleganze (relevant to `societas_maris`); the post-1200 contracts are overwhelmingly unilateral with the investor bearing the peril (relevant to `commenda` and `commenda_alloc`). Pooling them gives a modal instance that the edition's chronology and fondi have made, not the institution.
2. **A release is evidence of a venture and its discharge, not of its loss terms.** Recommendation: cite a release for a loss-allocation or outcome-coupling cell only where it recites the clause; where it abbreviates ("ut in ea legitur"), that cell takes nothing from it, and silence must not be read as an absence.
3. **The Venetian evidence is drawn from settled ventures.** Recommendation: on WP1 cells (outcome coupling, loss sharing), say in the note that the Venetian acts come overwhelmingly from ventures that were paid out, and that losses are seen only where they were attested or litigated. No frequency of loss can be read off this edition.
4. **Count the Mairano dossier as one cluster.** Recommendation: where a value rests on twelfth-century Venetian acts, report how many are Mairano's, so that one tractator's archive is not counted as many independent witnesses.
5. **Treat mater and exemplum as one witness.** Recommendation: use the copy flag and the regest similarity column to collapse duplicates before counting support.
6. **Keep this record out of the bundle.** Recommendation: write the Venetian PRIORS before the coder sees any act, as the protocol requires, and do not let §6.5 into them.

## 8. Limits

- Automated over an OCR text layer, checked on 37 acts against page images (§5). The small type classes carry a few acts of error each; incision and overseas counts are lower bounds.
- "Investment contract" groups colleganza, compagnia and "receives a sum to trade with" acts; the bilateral and quarter-share markers are pattern counts in the Latin, not readings, and should be checked at the page before any cell rests on them.
- Period cuts (1150, 1200, 1230) are this pass's, chosen before the tables were run; they are not the editors'.
- The measurement says what the edition prints. It does not say what the archives hold, which the editors themselves trimmed (*processi* out, p. xix).

## 9. Files

- `records/CORPUS-morozzo-lombardo-2026-10-25.csv`: one row per printed act (865), with fondo, date, place, formula, type and its basis, the flags, and the image check where one was made. No text of the edition.
- `records/SCRIPTS-morozzo-lombardo-selection-2026-10-25/`: the scripts as run (segmentation `seg3.py`–`seg7.py`, `blk.py`, `build.py`; classification `cls2.py`; tables `tab.py`, `final.py`, `out.py`), the act positions as finally fixed (`positions.json`) and the archival-line positions (`B.json`). They run against the two text extracts named in §2, which are not committed.
