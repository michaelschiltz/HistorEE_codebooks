# Coding notes — commenda-primary-2026-09-28 (stage 4, blind)

- Pass: `commenda-primary-2026-09-28`. Condition: `blind`. Coder: `ai`, `claude-opus-5-5`, effort `high`. Values fixed on 2026-09-28.
- Scope: 61 cells, rows `commenda` and `societas_maris` in `organizational_forms`, rows `commenda_alloc` and `societas_maris` in `loss_mitigation_forms` (`cells-in-scope.csv`).
- Evidence: only the three files in `sources/`. No secondary literature, no web, no Zotero, Undermind or Elicit, no memory file, no claude.ai Project, no `git`. `reveal/` was neither listed nor opened.
- Priors: `PRIORS-commenda-primary-2026-09-28.md`, sha256 `5fcf23fc2cd2d961fefdc867fd1c76085212416847249c3993853972b01d182c`, committed and confirmed by MS before any source was opened.
- Files written, all in `proposed-of/`: `type-census-commenda-primary-2026-09-28.csv`; `instances-commenda-primary-2026-09-28.csv`; `instance-chars-commenda-primary-2026-09-28.csv`; `recodings-commenda-primary-2026-09-28-organizational_forms.csv` (42 rows); `recodings-commenda-primary-2026-09-28-loss_mitigation_forms.csv` (19 rows); this file; `LOGBOOK-DRAFT-commenda-primary-2026-09-28.md`; `COMMIT-MSG-commenda-primary-2026-09-28.txt`. Nothing outside `proposed-of/` was edited after the priors file.

## 1. Reading record

**What the sources are.** `scriba_vol1_acts_pdfp66-501_errata.pdf` (Chiaudano & Moresco's edition of Giovanni Scriba, vol. I: acts and errata); `cassinese_vol1_acts_pdfp22-459.pdf` (Hall, Krueger & Reynolds's edition of Guglielmo Cassinese, vol. I); `amalric1248_blancard_notulae_latin.txt` (Blancard's printing of Giraud Amalric's notulae of 1248, Latin where printed, as a text file with Blancard's page markers).

**How the text was obtained.** The two PDFs were read through their text layer (`pdftotext -layout`). The Amalric file was read as given. Acts were segmented by the editors' act numbers: Scriba 803 acts (nos. I–DCCCIII), Cassinese 1,095 acts (nos. 1–1097; nos. 996–997 are not in the edition's sequence), Amalric 1,031 numbers of which 561 are printed in Latin, 413 are stubs Blancard did not print, 51 are appendix stubs and 6 are missing from the scan (nos. 276–280, 879). The printed page of each act was mapped from the extract page: Scriba printed = extract for extract pp. 1–92, minus 2 for pp. 95–102, minus 4 from p. 105 (plates at extract pp. 93–94 and 103–104; extract p. 437 is the errata page); Cassinese printed = extract for pp. 1–12, minus 2 for pp. 15–128, minus 4 for pp. 131–405, minus 6 from p. 408 (plates at pp. 13–14 and 129–130; extract pp. 406–407 duplicate pp. 404–405 and were excluded).

**What was read, and how closely.** Every act of the three corpora was classified by its Latin drafting term (the type census). Every sampled act (268 acts, 272 act-by-stratum instances) was read in full in the Latin, act by act, to record every party's name and every clause parsed; the clause quotes in the instance files are copied from the text layer and checked by script to be verbatim substrings of it, so they carry the OCR's spacing and errors (e.g. `s u p e rflu u m ad fo rtu n am eorum`). Non-sampled acts were read only as far as the classification required.

**Page images.** For the 51 Genoese instances whose quotes carry a minority state (the states that decide whether a variant is named), the page images were rendered from the two PDFs (`pdftoppm -r 90 -gray`) and read: Scriba extract pp. 48, 56, 62, 110, 115, 116, 157, 158, 175, 189, 243, 248, 286, 343, 368, 378, 396, 403, 406, 414; Cassinese extract pp. 16, 25, 41, 46, 47, 49, 63, 124, 125, 127, 137, 147, 154, 156, 190, 194, 202, 216, 235, 236, 246, 263, 284, 291, 292, 302, 354, 355, 378, 379, 382, 404, 405, 430, 432, 434. Every checked quote matched the printed text except one: Scriba DCCLXIV had been coded `CI1=several-accounts` on `coniunctim et separatim`, which the image shows refers to the two travellers going together or apart, not to separate investment; the coding was removed. The images also showed two things the text layer had not given me: Cassinese 726 licenses the traveller to borrow for the ship's cargo (`Et Daniel possit mutuare et facere que opus fuerint pro carrico navis`, p. 288; noted, not coded), and Cassinese 29 carries the same promise to pay back the capital at term as the land-based societates (`et tunc dare promittit ei capitale`), so it was given `CF2=1` for consistency. These instances carry `quote_checked_against_image=yes`; the other Genoese instances carry `no`; Amalric instances carry `no (Blancard text file; no page images in sources/)`.

**Fields extracted by script, not by reading.** `capital_stans` is the first sum of money in the act, copied verbatim (OCR) by a pattern; it is `not extracted` where the pattern failed (33 of 272) and is not reliable enough to compute with. `capital_tractator` is the quoted clause stating the traveller's own contribution where one was found, `0` where the act is a commenda with no such clause, otherwise `not extracted`. `side_amounts` was not extracted. Genoese dates are ISO where the editor's heading parses; where the heading's year is OCR-damaged the day and month are taken from the heading and the year from the neighbouring acts, and the instance note says so; where the heading gives only a month (Scriba XII; Cassinese 20, 29, 41, 58) the date is `YYYY-MM`; four Scriba acts whose heading was not captured are `not parsed`, and three acts (Scriba DCCV; Cassinese 972, 984) keep `heading: …` with the unparsed OCR. Amalric dates are from the Roman dates, carried forward over `Eodem die`, 1248 new style.

## 2. Type census

Every act was classified by the Latin term in which it is drafted, not by the editor's heading. Commenda type: `in accomendatione`, `accomendacio`, `commendacio`, `comanda`. Societas type: `in societate`, `societas`, `companhia`. An act drafted in both is `societas+accomendatio`; an act drafted in the alternative (`comanda vel societas`, `comanda seu societas`) is `accomendatio/societas-alt`. A continuation (`Et a …, similiter`; `Item a …`) takes the type of the act it refers to. Sea loan = a loan repayable `sana eunte nave` or at the lender's peril, including a `cambium` that carries such language; plain `cambium` otherwise. The file is `type-census-commenda-primary-2026-09-28.csv` (2,459 rows; the 470 Amalric stubs are counted apart and are not rows).

| type (drafting term)        | Scriba | Cassinese | Amalric (printed) | all  |
|-----------------------------|--------|-----------|-------------------|------|
| `accomendatio`              | 9      | 136       | 214               | 359  |
| `societas`                  | 173    | 132       | 15                | 320  |
| `societas+accomendatio`     | 1      | 6         | 4                 | 11   |
| `accomendatio/societas-alt` | 0      | 0         | 3                 | 3    |
| `sea_loan`                  | 43     | 14        | 30                | 87   |
| `cambium`                   | 12     | 5         | 74                | 91   |
| `mutuum`                    | 15     | 79        | 28                | 122  |
| `sale`                      | 191    | 75        | 30                | 296  |
| `dowry`                     | 75     | 55        | 23                | 153  |
| `other`                     | 284    | 593       | 140               | 1017 |
| **total**                   | 803    | 1095      | 561               | 2459 |

Amalric stubs, counted apart: 413 notulae not printed by Blancard, 51 appendix stubs, 6 missing from the scan (nos. 276–280, 879). **Every Marseille frequency in these files is a frequency over the 561 printed notulae, not over the cartulary.**

`other` includes 59 acts that commit trade capital without a drafting term (Scriba 33, Cassinese 26: `portare laboratum`, a share of profit, no `accomendatio` or `societas`), which the editors head as accomendationes; 19 acts that refer to an earlier accomendatio or societas without constituting one (quittances, assignments: Cassinese 15, Amalric 4); quittances (Scriba 36, Cassinese 98, Amalric 9); leases, testaments, procurations, obligations, declarations and others.

## 3. The draw

Strata are corpus × type, commenda type and societas type only. The commenda frame of a corpus is its `accomendatio`, `societas+accomendatio` and `accomendatio/societas-alt` acts; the societas frame is its `societas`, `societas+accomendatio` and `accomendatio/societas-alt` acts, so mixed and alternative acts sit in both frames and are coded once in each (4 acts in the samples: Scriba CCXLI; Cassinese 732; Amalric 41, 204). A stratum of 60 acts or fewer is taken whole. A larger one is sampled systematically: the frame is sorted by act number, `random.seed(20260928)` is set immediately before the stratum's draw, `k = N/60`, `r = random.random()*k`, and positions `floor(r + i*k)` for `i = 0..59` (0-based) are taken.

| corpus    | stratum  | frame N | n  | rule       | k        | r        |
|-----------|----------|---------|----|------------|----------|----------|
| Scriba    | commenda | 10      | 10 | all        | –        | –        |
| Scriba    | societas | 174     | 60 | systematic | 2.9      | 1.993444 |
| Cassinese | commenda | 142     | 60 | systematic | 2.366667 | 1.626834 |
| Cassinese | societas | 138     | 60 | systematic | 2.3      | 1.581007 |
| Amalric   | commenda | 221     | 60 | systematic | 3.683333 | 2.531903 |
| Amalric   | societas | 22      | 22 | all        | –        | –        |

Samples (act numbers):

- Scriba, commenda (all 10): LXVIII, LXXII, LXXIII, LXXXIX, CV, CXVIII, CLXXXVI, CCXLI, CCLXXXVII, DCCXLVII.
- Scriba, societas (60): XII, LIX, XCVII, CXV, CXXVI, CXXX, CXLI, CLXXXI, CCI, CCIX, CCXI, CCXX, CCXLI, CCLIV, CCLIX, CCLXXV, CCLXXXIII, CCXC, CCCXXIV, CCCXXXVII, CCCXLVII, CCCLV, CCCLXXVIII, CCCLXXXV, CCCXCIII, CDII, CDXX, CDXXXVII, CDXLIX, CDLX, CDLXIV, CDLXXX, CDLXXXVII, CDXCVIII, DIII, DXII, DXXVI, DLIX, DCIII, DCXII, DCXIX, DCXXV, DCXXXIX, DCXLIX, DCLIV, DCLVII, DCLXXIV, DCLXXX, DCXCII, DCCV, DCCXXVII, DCCXXXIX, DCCXLV, DCCLI, DCCLVII, DCCLXIV, DCCLXXI, DCCLXXIV, DCCLXXXI, DCCCIII.
- Cassinese, commenda (60): 29, 41, 50, 58, 103, 119, 125, 138, 175, 212, 271, 290, 306, 321, 332, 362, 375, 383, 417, 425, 430, 438, 468, 477, 483, 490, 500, 546, 573, 581, 604, 609, 662, 706, 716, 725, 732, 745, 750, 810, 866, 875, 917, 922, 956, 1005, 1009, 1013, 1017, 1021, 1028, 1040, 1046, 1061, 1063, 1078, 1082, 1087, 1089, 1093.
- Cassinese, societas (60): 12, 20, 32, 38, 53, 74, 93, 106, 112, 123, 143, 150, 184, 207, 218, 249, 263, 273, 289, 303, 310, 317, 327, 333, 337, 379, 382, 387, 407, 412, 445, 469, 493, 502, 529, 548, 583, 606, 655, 708, 726, 732, 751, 772, 777, 817, 832, 878, 905, 943, 952, 972, 984, 1004, 1011, 1031, 1059, 1067, 1079, 1091.
- Amalric, commenda (60): 7, 16, 29, 36, 41, 50, 61, 83, 87, 98, 125, 141, 161, 182, 194, 204, 212, 225, 228, 247, 260, 269, 273, 286, 291, 304, 314, 329, 342, 364, 371, 402, 412, 443, 451, 466, 473, 479, 492, 505, 519, 530, 538, 542, 559, 577, 582, 594, 603, 613, 623, 650, 671, 678, 687, 705, 718, 740, 810, 931.
- Amalric, societas (all 22): 41, 112, 164, 204, 236, 239, 348, 429, 442, 467, 486, 512, 611, 697, 755, 760, 774, 829, 838, 870, 948, 1015.

268 distinct acts, 272 instances.

## 4. Instance coding

Each sampled act is one row in `instances-commenda-primary-2026-09-28.csv` (instance id `SCR|CAS|AMA-nnnn-C|S`, the suffix naming the stratum) with every party's name as printed (`stans:` the capital provider or providers, `tractator:` the working party or parties), the clauses parsed with their Latin quoted verbatim, and a note. Each characteristic the act speaks to is one row in `instance-chars-commenda-primary-2026-09-28.csv` with the state, the verbatim quote that carries it and a note; a characteristic the act does not speak to has no row. 272 instances, 1,826 characteristic rows.

How an act speaks to each characteristic (instance level):

- `TS2`: the duration clause. One voyage out and back (`portare laboratum … et inde Ianuam`, `in proximo viagio`) is `single-venture`; a stated term (`usque ad annum`, `usque .v. annos`, `usque ad kalendas augusti`) is `fixed-term`; `usque dum placuerit eis` or repayment on demand is `open`; two or more stated voyages is `.NR` (no value fits).
- `CF1`: `1` where only the capital provider contributes; `P` where both sides contribute and one side travels or works; `0` where all contribute and all travel or work.
- `CF2`: `0` where a peril clause puts the capital at the provider's peril (`ad tuum resicum`; `tuum resegum`), including the shared form in which the working party bears only his own portion; `1` where the working party promises the capital unconditionally (`Capitale tuum super me salvum erit`; `tunc dare promittit ei capitale … sub pena dupli`); `P` for Cassinese 362 (pledged goods at the holder's fortune up to the debt, the surplus at the owners'). Not coded where the act says neither.
- `CF3`: `bilateral` for one named capital provider, `multilateral` for two or more, or for goods of several owners carried under one act. Not coded where all partners work (then there is no principal).
- `LR2`, `LR3`, `LR6`: from the profit clause. A share to the working party is `LR2=coupled`; `gratis` or all profit to the investor is `LR2=veiled` with `LR3=1`. A fraction (a quarter, a third, a half) is `LR3=P`; profit per libram or halves on equal contributions is `LR3=1`. `LR6=upside-only` where the working party shares gains and the peril clause lays the capital on the investor; `symmetric` where he also has capital of his own in the stock or guarantees the capital.
- `CI1`: `several-accounts` for `implicare separatim`; `common` for expenses and profit reckoned per libram with other goods the agent carries (`expensas per libram cum aliis`), `implicatas in comunibus implicitis meis`, or a societas stock of merged contributions.
- `CI2`: `0` where the capital can be recalled at will or on demand. Not coded otherwise.
- `LR4`, `LR5`: only where members expressly share one another's outcomes (Amalric 697; Scriba DCCXXVII).
- `AP3`, `LR1`: only where an act speaks to borrowing from third parties on the venture (Amalric 774).
- `LP2`: `P` where goods are spoken of as the societas's own (`res ipsius societatis`; `ad resicum et fortunam societatis`).
- `RB1`, `RB4`, `PR1`, `MC1`: from the peril clause only.
- `RB2`: only where the act separates the result of sale from the peril (Scriba DCXCII).
- `RB3`: `general-estate` for `bona pignori` or a double penalty `in suis bonis`; `surety` for a third party bound as `debitor et pagator`; `goods` for goods pledged. Amalric's `obligans etc.` is abridged and not coded.
- `MB3`: `voluntary` for every act (entry by private contract).

Blancard's `etc.` hides formulae. Where an Amalric notula abridges the peril, profit or security clause, nothing is coded for it: never `0`.

## 5. From instances to cells

- **Modal state.** The cell takes the modal state among the sampled acts that speak to the characteristic, pooled across the three corpora (the form's sample, not a corpus, is the unit). Counts, shares and distinct investors are given per corpus and pooled in every cell's `notes`.
- **Variants.** A state held by at least 10% of the speaking acts in any one corpus is a variant and is named in the note. The denominator is the speaking acts, not all sampled acts (decision point 16).
- **A frequency never becomes `P`.** `P` appears at cell level only where the modal instance state is itself `P` (structural half-presence in the act).
- **Ties** are broken by the number of distinct investors among the acts holding each state (decision point 17). One tie occurred (`societas_maris LR4`).
- **`.NR`** where no sampled act speaks. `confidence` and `articulation` are then `.NR`, `source_ref` names the sample, `source_lang=la`.
- **`.NA`** where the characteristic does not apply to the form (`AP4`: no founder; `PY0`: no pool). `.NA` propagates to `confidence`, `articulation`, `source_ref` and `source_lang`.
- **Dependants of an `.NR` parent** are `.NR`, not `.NA` (`commenda LR5`, `commenda_alloc VF2`): `.NA` would assert that the parent is `0` or `none`.
- `source_read=partial` in every row, with the sample stated in the note. `source_class=primary-transactional`. `source_ref` cites up to three acts per corpus carrying the modal state and up to two carrying each named variant; the full list is in the instance files.

| census | type_id          | char_id | value             | confidence | articulation    | speaking/sampled | modal share | variants named   |
|--------|------------------|---------|-------------------|------------|-----------------|------------------|-------------|------------------|
| orga   | `commenda`       | `TS2`   | single-venture    | high       | articulated     | 120/130          | 97%         | –                |
| orga   | `commenda`       | `AP3`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `LR1`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `LR2`   | coupled           | high       | articulated     | 59/130           | 88%         | veiled           |
| orga   | `commenda`       | `LR3`   | P                 | medium     | analyst-imposed | 59/130           | 88%         | 1                |
| orga   | `commenda`       | `LR4`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `LR5`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `CF1`   | 1                 | high       | articulated     | 129/130          | 99%         | –                |
| orga   | `commenda`       | `CF2`   | 0                 | medium     | articulated     | 13/130           | 69%         | 1, P             |
| orga   | `commenda`       | `CF3`   | bilateral         | high       | articulated     | 130/130          | 74%         | multilateral     |
| orga   | `commenda`       | `LR6`   | upside-only       | low        | analyst-imposed | 5/130            | 80%         | symmetric        |
| orga   | `societas_maris` | `TS2`   | single-venture    | medium     | articulated     | 131/142          | 82%         | fixed-term       |
| orga   | `societas_maris` | `AP3`   | 0                 | low        | analyst-imposed | 1/142            | 100%        | –                |
| orga   | `societas_maris` | `LR1`   | unlimited-several | low        | analyst-imposed | 1/142            | 100%        | –                |
| orga   | `societas_maris` | `LR2`   | coupled           | high       | articulated     | 131/142          | 100%        | –                |
| orga   | `societas_maris` | `LR3`   | P                 | medium     | analyst-imposed | 131/142          | 96%         | 1                |
| orga   | `societas_maris` | `LR4`   | 1                 | low        | articulated     | 2/142            | 50%         | P                |
| orga   | `societas_maris` | `LR5`   | synchronising     | low        | analyst-imposed | 1/142            | 100%        | –                |
| orga   | `societas_maris` | `CF1`   | P                 | high       | articulated     | 136/142          | 83%         | 1                |
| orga   | `societas_maris` | `CF2`   | 1                 | low        | analyst-imposed | 22/142           | 68%         | 0                |
| orga   | `societas_maris` | `CF3`   | bilateral         | high       | articulated     | 138/142          | 68%         | multilateral     |
| orga   | `societas_maris` | `LR6`   | symmetric         | medium     | analyst-imposed | 119/142          | 100%        | –                |
| orga   | `commenda`       | `LP1`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `LP2`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `LP3`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `AP1`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `AP2`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `AP4`   | .NA               | .NA        | .NA             | 0/130            | –           | –                |
| orga   | `commenda`       | `CI1`   | common            | low        | articulated     | 24/130           | 67%         | several-accounts |
| orga   | `commenda`       | `CI2`   | 0                 | low        | articulated     | 1/130            | 100%        | –                |
| orga   | `commenda`       | `CI3`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `commenda`       | `CI4`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| orga   | `societas_maris` | `LP1`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |
| orga   | `societas_maris` | `LP2`   | P                 | low        | articulated     | 2/142            | 100%        | –                |
| orga   | `societas_maris` | `LP3`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |
| orga   | `societas_maris` | `AP1`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |
| orga   | `societas_maris` | `AP2`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |
| orga   | `societas_maris` | `AP4`   | .NA               | .NA        | .NA             | 0/142            | –           | –                |
| orga   | `societas_maris` | `CI1`   | common            | high       | articulated     | 113/142          | 98%         | –                |
| orga   | `societas_maris` | `CI2`   | 0                 | low        | articulated     | 5/142            | 100%        | –                |
| orga   | `societas_maris` | `CI3`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |
| orga   | `societas_maris` | `CI4`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |
| loss   | `commenda_alloc` | `MC1`   | allocation        | medium     | articulated     | 10/130           | 100%        | –                |
| loss   | `commenda_alloc` | `MB3`   | voluntary         | high       | analyst-imposed | 130/130          | 100%        | –                |
| loss   | `commenda_alloc` | `RB1`   | capital-provider  | medium     | articulated     | 10/130           | 90%         | shared           |
| loss   | `commenda_alloc` | `RB2`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| loss   | `commenda_alloc` | `RB3`   | surety            | low        | articulated     | 3/130            | 67%         | goods            |
| loss   | `commenda_alloc` | `RB4`   | 1                 | medium     | analyst-imposed | 9/130            | 100%        | –                |
| loss   | `commenda_alloc` | `PR1`   | 0                 | medium     | analyst-imposed | 10/130           | 100%        | –                |
| loss   | `commenda_alloc` | `PY0`   | .NA               | .NA        | .NA             | 0/130            | –           | –                |
| loss   | `commenda_alloc` | `VF1`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| loss   | `commenda_alloc` | `VF2`   | .NR               | .NR        | .NR             | 0/130            | –           | –                |
| loss   | `societas_maris` | `MC1`   | allocation        | medium     | articulated     | 10/142           | 100%        | –                |
| loss   | `societas_maris` | `MB3`   | voluntary         | high       | analyst-imposed | 142/142          | 100%        | –                |
| loss   | `societas_maris` | `RB1`   | shared            | medium     | articulated     | 10/142           | 90%         | capital-provider |
| loss   | `societas_maris` | `RB2`   | shared            | low        | articulated     | 1/142            | 100%        | –                |
| loss   | `societas_maris` | `RB3`   | general-estate    | low        | articulated     | 7/142            | 71%         | surety           |
| loss   | `societas_maris` | `RB4`   | 1                 | low        | analyst-imposed | 1/142            | 100%        | –                |
| loss   | `societas_maris` | `PR1`   | 0                 | medium     | analyst-imposed | 10/142           | 100%        | –                |
| loss   | `societas_maris` | `PY0`   | .NA               | .NA        | .NA             | 0/142            | –           | –                |
| loss   | `societas_maris` | `VF1`   | .NR               | .NR        | .NR             | 0/142            | –           | –                |

## 6. Decision points, each with its alternative reading

1. **The frame is the drafting term.** 59 Genoese acts commit trade capital with no drafting term (`portare laboratum`, a quarter of profit), and the editors head them as accomendationes; they are outside the frames. *Alternative:* take the editors' headings; the Scriba commenda frame would grow from 10 acts to about 43 and its cells would rest on more Genoese evidence of the 1150s.
2. **Continuations count.** An act drafted `Et a …, similiter` or `Item a …` under a constituting act is typed and coded by reference to it (e.g. Cassinese 477→475, 1040→1038), because the notary's `similiter` incorporates the terms. *Alternative:* count only acts that state their own terms; a few Cassinese instances would drop.
3. **Mixed and alternative drafting go in both frames.** *Alternative:* assign a mixed act to one frame by its dominant capital; four instances would move.
4. **Land-based societates stay in the societas frame.** 20 of the 142 societas instances are shops, workshops, a money-changer's table, or trade `in terra` (Cassinese 9, Amalric 8, Scriba 3); 5 of the 130 commenda instances are land-based. They share the drafting term, and the frame was fixed by drafting term before any act was coded. They drive `societas_maris` `CF2` (14 of the 15 `1`s), most of the `fixed-term` variant of `TS2` (15 of 19), three of the five `CI2` acts and four of the five `general-estate` acts of `RB3`. *Alternative:* restrict the `societas_maris` frame to acts that go by sea; then `CF2=0` (7 of 8 speaking acts), `TS2=single-venture` in 107 of 113 speaking acts, `RB3` 1 `general-estate` against 1 `surety` (a tie) and `CI2` on 2 acts. This is the most consequential decision in the pass (see answer 4).
5. **A promise to pay back the capital at term is `CF2=1`.** `tunc dare promittit ei capitale et medietatem proficui … sub pena dupli in suis bonis` is read as the working party answering for the capital. Scriba CCCLV is explicit (`Capitale tuum super me salvum erit`). *Alternative:* a performance duty (render account and pay what there is) that says nothing of peril; then these acts do not speak to `CF2`, and `societas_maris CF2` is `0`. The sea acts' `reducere … in potestate … cum capitali` is not read as `CF2=1` on either reading, since it is a duty to bring back, and `quod Deus dederit` marks the outcome as fortuitous.
6. **Multi-voyage horizons are `TS2=.NR`** (Cassinese 112, 1078), because none of `open`, `fixed-term`, `single-venture` fits. *Alternative:* `fixed-term`. Neither changes a cell.
7. **Atypical uses of `accomendatio` stay in the frame.** Cassinese 875 is a deposit repayable 15 days after demand; Cassinese 362 carries goods `nomine pignoris`; Cassinese 469 converts an earlier debt into a societas (`innovationem facit`). They are drafted in the terms and the rule is the drafting term. *Alternative:* exclude them; `commenda CI2` would become `.NR` and the `commenda CF2` variants would shrink to one act.
8. **Gratuitous commendas are `LR2=veiled` and `LR3=1`.** Scriba LXXXIX, CCLXXXVII, DCCXLVII; Cassinese 383, 500, 750, 1087. *Alternative for `LR3`:* the working party has no stake, so proportionality to stake is not in question and `LR3` should be `.NR` for these acts; `commenda LR3=P` either way.
9. **A fixed fraction is `LR3=P`.** The quarter or the half is a share of outcome (not a fixed claim) that does not track the capital stake: one limb present, one absent. *Alternative:* `1`, reading "proportionally to stake" loosely as "a share, not a fixed claim"; this was my prior.
10. **`LR4` is coded only for express mutualisation.** *Alternative for the commenda:* `0` by structure (a bilateral contract cannot pool). Not taken: that is an inference from form, not an observation, and 34 of 130 commenda instances are multilateral without saying how the co-investors share outcomes.
11. **`AP3` and `LR1` rest on one act** (Amalric 774: the ship-buying partner may borrow for the ship and is repaid half by the other). Cassinese 218 (borrowing on the societas), 382 and 1093 (a ban on lending to others), and 726 (licence to borrow for the ship's cargo) are noted, not coded, because none says who answers to the lender. *Alternative:* code Cassinese 726 as `AP3=0` as well (the traveller borrows in his own name); this would not change the cell.
12. **`LP2=P` is an idiom, not title.** `de rebus ipsius societatis` (Scriba CCXI) and `ad resicum et fortunam societatis` (Scriba DCCXXXIX) speak of the stock as the societas's own. *Alternative:* a manner of speaking about a common stock owned by the partners; `.NR`.
13. **`MC1` is not blind** for either loss row (priors leaks 1 and 10). It is coded from the acts, and the note says so.
14. **Blancard's abridgements are never `0`.** `ad fortunam Dei etc.`, `obligans etc.`, `renuncians etc.` are not coded. The Marseille peril clause, profit clause and security are therefore under-observed, and the Marseille frame is itself the printed notulae only.
15. **Marseille frequencies are over the printed notulae.** Every note that reports an Amalric frequency says so.
16. **The variant threshold uses the speaking acts as denominator.** *Alternative:* all sampled acts in the corpus; then only the frequent states would qualify (for instance `commenda LR2=veiled` would fall to 3 of 10 in Scriba, still a variant, and to 4 of 60 in Cassinese, not one; `commenda CF2=1` would not be a variant anywhere).
17. **Ties go to the state with more distinct investors.** Only `societas_maris LR4` tied (Amalric 697 `1`, three investors; Scriba DCCXXVII `P`, two). *Alternative:* report the tie as `.NR`; not taken, because acts do speak.
18. **`RB4=1` is inferred** from a clause that puts the capital at the investor's peril; no act states the discharge in words. Hence `analyst-imposed`.
19. **`PR1=0` is read as observed** in acts that allocate the peril and state the parties' shares with no charge for bearing it. *Alternative:* the silence of a clause is not an observed absence; `.NR`. I took the complete statement of terms as the observation.
20. **`CI1=common` on expense and profit reckoning.** `expensas per libram cum aliis` is read as the commended capital traded together with the agent's other goods. *Alternative:* it is a rule for charging expenses, not capital structure; then `commenda CI1` would rest on Amalric's `implicatas in comunibus implicitis meis` (common) and Cassinese's `implicare separatim` (several-accounts) and the per-corpus modes would still differ.
21. **Distinct investors are counted by name string as recorded.** Spelling variants of one person in different acts (e.g. `Bonus Iohannes Malfiliaster`, `Bonus Johannes Malfiliaster`) inflate the count slightly.
22. **Not coded for ambiguity:** Scriba CCI (Lucca money; `Et ego Tortus ad resicum meum accipio predictas lb. .xx. …`, an allocation of 20 lb. whose direction I could not settle); Amalric 371 (`totum capitale et lucrum tibi reddere`, which may be a gratuitous commenda or only a remittance clause).
23. **`MB3=voluntary` includes agents acting `iussu patris`** (e.g. Cassinese 655): the compulsion, if any, is the father's, not the arrangement's.

## 7. Leaks

All leaks found before coding are listed with their locations in the priors file (items 1–14 there): the `commenda_alloc` code name; the `societas_maris` type name and its collision with `CF3=bilateral`; general knowledge; the `code-a-form` skill's example; the redacted `LR2` worked case in `CHARACTER-CODING.md` test 1; the redacted `AP3`/`LR1` passages in the organizational vocabulary; the `LR6` *qirāḍ* sentence; `CHARACTER-CODING.md` test 4 ("the agent is a debtor"); the `LS3` redaction; the loss schema's package description placing a withheld form under *allocation*; the row pattern of `cells-in-scope.csv` (no `VF2` row for `societas_maris`); the clause columns of `instances-header.csv`; the kickoff's term list and example `source_ref`; the system profile. None was used. **No further leak was found during coding.** One discrepancy, not a leak: the kickoff's example `source_ref` gives Scriba CCCXII at p. 172, but CCCXII begins on printed p. 165 (extract p. 169); I treated the example as a format only.

## 8. Vocabulary and schema defects noticed and not repaired

- **`TS2` cannot hold a multi-voyage horizon** (Cassinese 112: Sardinia, then Bugia, then `uno alio viatico`; 1078: Constantinople, then `duobus aliis viaticis`). Neither `single-venture` nor `fixed-term` nor `open` describes it.
- **The `societas_maris` row and the drafting term do not coincide.** `societas` in Genoa and Marseille covers shops, workshops and credit at a term as well as sea ventures, and no row in scope holds the land partnership. Coding the row from acts selected by drafting term mixes two arrangements (decision point 4). The type name also names the Venetian *collegantia*, and no Venetian act is in `sources/`.
- **`CF2` conflates two questions for fixed-term acts:** whether the working party bears the *peril* to the capital, and whether he owes the capital as a debt at term. The land acts answer the second and are silent on the first.
- **`RB3` records what secures the advance but not against what.** Every surety in the sample (Cassinese 333; Amalric 141, 194, 760) answers for the working party's fault (`in sua culpa`; `in omni defectu quem invenires culpa`), not for loss to the peril. `surety` reads as security for the capital itself.
- **`LR3` is undefined where the working party has no stake** (gratuitous commendas): only the investor has a stake, so "proportionally to stake" is either trivially met or undefined.
- **`CI1` cannot hold "a common stock with side placements kept in separate accounts"** (Cassinese 1011: the societas stock is common; the accomendationes carried with it must be invested `separatim`).
- **`LR6` is not observable for the Genoese commenda** where no peril clause is written, although `LR2=coupled` is; the dependence is on a clause that Cassinese never drafts.
- **`AP2` overlaps `CI2`**, as the vocabulary itself flags. `CI2=0` evidences the partners' limb of `AP2`; the creditors' limb is unevidenced, so `AP2` stays `.NR` by the two-limb rule.
- **`instances-header.csv` has no column for the sea/land distinction or for continuation by reference**, both of which decided codings; they are in `notes`.
- **Frictionless cannot check the dependence rules** (`LR5` on `LR4`, `VF2` on `VF1`, `LR6` on `LR2`, `CF2` on `CF1`, `.NA` propagation). I checked them by script (section 11).

## 9. The six answers

### 1. What was coded, and on what evidence

All 61 cells, from 272 instances drawn from the printed acts of three notarial corpora: Giovanni Scriba vol. I (Genoa 1154–61; 70 instances), Guglielmo Cassinese vol. I (Genoa 1190–91; 120 instances) and Giraud Amalric's cartulary of 1248 as printed by Blancard (Marseille; 82 instances, over the printed notulae only). 36 cells carry an observed state, 21 are `.NR` and 4 are `.NA` (see answer 2). The values with broad support (at least 100 speaking acts pooled) are: `commenda` `TS2=single-venture`, `CF1=1`, `CF3=bilateral`, and `commenda_alloc MB3=voluntary`; `societas_maris` `TS2=single-venture`, `CF1=P`, `CF3=bilateral`, `LR2=coupled`, `LR3=P`, `LR6=symmetric`, `CI1=common`, `MB3=voluntary`. `commenda` `LR2=coupled` and `LR3=P` rest on 59 acts, almost all Genoese, because Blancard's notulae rarely print the profit clause. Everything that turns on the peril clause (`commenda CF2=0`, `LR6=upside-only`, the `commenda_alloc` `MC1`, `RB1`, `RB4`, `PR1` cells and their `societas_maris` counterparts) rests on 5 to 13 commenda acts and 1 to 22 societas acts, because Cassinese never writes a peril clause and Blancard usually abridges or omits it. Fourteen observed cells are `low`, most of them resting on seven acts or fewer.

### 2. What could not be coded, and why

`.NR` (the acts were read and are silent): `commenda` `AP3`, `LR1`, `LR4`, `LR5`, `LP1`, `LP2`, `LP3`, `AP1`, `AP2`, `CI3`, `CI4`; `commenda_alloc` `RB2`, `VF1`, `VF2`; `societas_maris` `LP1`, `LP3`, `AP1`, `AP2`, `CI3`, `CI4`, and the loss row's `VF1`. The reason is the same throughout: a notarial act binds its parties and addresses no one else, so it says nothing of the venture's outside creditors (`AP1`, `AP2`'s creditor limb, `AP3`, `LR1`), of personhood or standing (`LP1`, `LP3`), of alienating an interest (`CI3`, `CI4`), or of how a loss claimed at the end of a voyage is proved (`VF1`, `VF2`). No commenda separates the result of sale from the peril (`RB2`). `commenda LR5` and `commenda_alloc VF2` are `.NR` because their parents are. `.NA`: `AP4` for both rows (no founder; both forms arise by contract) and `PY0` for both loss rows (no pool with an output).

### 3. Which of my expectations were falsified

Per-cell expectations, quoted verbatim from the priors file, with the blind value:

```text
| orga | `commenda` | `LR3` | 1 | medium | profit divided by agreed fraction, not a fixed claim; ambiguity: "proportionally to stake" is not met literally, the traveller having no capital stake — may be P |
| orga | `commenda` | `LR4` | 0 | medium | bilateral contract, nothing mutualised among members; the traveller's portfolio of separate commendas is not a pool among members |
| orga | `commenda` | `LR5` | .NA | high | follows `LR4=0` |
| orga | `societas_maris` | `AP3` | .NR | medium | silence on outside creditors |
| orga | `societas_maris` | `LR1` | .NR | medium | same |
| orga | `societas_maris` | `LR3` | 1 | medium | profit shared by fraction; half-and-half on 2:1 capital is not proportional to stake, so P is the alternative |
| orga | `societas_maris` | `LR4` | 0 | medium | no mutualisation beyond the two parties' joint stake |
| orga | `societas_maris` | `LR5` | .NA | high | follows `LR4=0` |
| orga | `societas_maris` | `CF2` | 0 | low | traveller loses his own third, not the investor's capital; P is the alternative if the acts make him share losses on the whole |
| orga | `commenda` | `CI1` | .NR | low | one investor's capital in the traveller's hands; `several-accounts` if acts keep separate investments apart, `common` if several investors' capital is merged |
| orga | `commenda` | `CI2` | .NR | low | no withdrawal clause expected; single-venture design suggests 1 but that would be inference |
| orga | `societas_maris` | `LP2` | .NR | low | as commenda |
| orga | `societas_maris` | `CI2` | .NR | low | as commenda |
| loss | `commenda_alloc` | `RB2` | capital-provider | low | loss on sale falls on the capital; rarely distinguished in the acts, so .NR is the likely alternative |
| loss | `commenda_alloc` | `RB3` | general-estate | low | general pledge of the traveller's goods for performance; `personal` or `none` alternatives; Blancard's `obligans etc.` hides the object |
```

Blind values for the same cells:

| census | type_id          | char_id | prior            | blind value       |
|--------|------------------|---------|------------------|-------------------|
| orga   | `commenda`       | `LR3`   | 1                | P                 |
| orga   | `commenda`       | `LR4`   | 0                | .NR               |
| orga   | `commenda`       | `LR5`   | .NA              | .NR               |
| orga   | `societas_maris` | `AP3`   | .NR              | 0                 |
| orga   | `societas_maris` | `LR1`   | .NR              | unlimited-several |
| orga   | `societas_maris` | `LR3`   | 1                | P                 |
| orga   | `societas_maris` | `LR4`   | 0                | 1                 |
| orga   | `societas_maris` | `LR5`   | .NA              | synchronising     |
| orga   | `societas_maris` | `CF2`   | 0                | 1                 |
| orga   | `commenda`       | `CI1`   | .NR              | common            |
| orga   | `commenda`       | `CI2`   | .NR              | 0                 |
| orga   | `societas_maris` | `LP2`   | .NR              | P                 |
| orga   | `societas_maris` | `CI2`   | .NR              | 0                 |
| loss   | `commenda_alloc` | `RB2`   | capital-provider | .NR               |
| loss   | `commenda_alloc` | `RB3`   | general-estate   | surety            |

Expectations in the priors' prose, quoted verbatim:

- "I expect the Genoese acts of the 1150s to state the peril clause rarely or not at all, and the Marseille acts to state it often." Half falsified. Scriba's commendas state it in 4 of 10 acts (`ad tuum resicum`), its societates in 1 of 60. In Marseille a peril clause, whole or abridged, appears in 11 of 60 sampled commenda notulae and 9 of 22 societas notulae as Blancard prints them: not often. It is Cassinese (1190–91) that almost never states it: 2 acts of 120, a pledge (no. 362) and `ad fortunam utriusque` (no. 382).
- "Marseille acts of the mid-thirteenth century use *comanda*, *ad fortunam Dei, maris et gentium* and *ad usum maris*." `gentium` does not occur in the 80 sampled notulae; the clause is `ad fortunam Dei et usum maris` (sometimes `et terre`) followed by the bearer (`et tuum resegum`).
- "Performance (not the peril) may be secured by a general pledge of the traveller's goods (*pro quibus omnia bona mea tibi pignori obligo*), with or without a penalty of double (*sub pena dupli*)." Falsified for the commenda: none of the 70 sampled Genoese commendas pledges the working party's goods for the commended capital; the double penalty appears only in the deposit use (Cassinese 875) and on a debt recorded in the same act as an accomendatio (Cassinese 332), and Cassinese 362 pledges the carried goods themselves. Among societates the pledge and the penalty `in suis bonis` appear in 5 acts, four of them land-based.
- "Duration and destination. … the arrangement ends on the traveller's return and the division of profit. Not open-ended." Falsified for part of the societas frame: 19 of 131 speaking acts are fixed-term (up to five years) and 4 are open (`usque dum placuerit eis`), almost all land-based.
- "I expect silence on: liability to the venture's outside creditors (`AP3`, `LR1`); … juridical personhood, property in the venture's own name, capacity to sue (`LP1`–`LP3`); … withdrawal before return (`CI2`) …". Falsified in part: six acts speak to withdrawal (all `0`), two Scriba acts speak of the societas's own goods, and one Amalric act speaks to borrowing from third parties.
- "Heterogeneity I expect. … Genoese acts citing the pledge of goods and a double penalty; Marseille formulae hidden behind `etc.`" The second held (the security clause is `obligans etc.` in 25 of the 82 Amalric instances); the first did not, for the commenda.

Expectations that held: `TS2`, `CF1`, `CF3`, `LR2`, `LR6`, `AP4`, `MC1`, `MB3`, `RB1`, `RB4`, `PR1`, `PY0`, `VF1`, `VF2` and the silence on `LP1`, `LP3`, `AP1`, `AP2`, `CI3`, `CI4` held for both rows. So did `commenda CF2=0`, and `societas_maris` `CI1`, `RB2` and `RB3`.

### 4. Characteristics that did not fit the evidence

- **`CF2` for `societas_maris`.** The pooled mode (`1`) comes from land-based societates whose partner owes the capital at a term; the sea-going societates that speak put the peril on the partners pro rata (`0`, 7 of 8). The cell reports the frame's mode as the protocol requires, at `low`, and the note gives the sea-only reading. Whichever is right, the characteristic is answering "does the working party owe the capital as a debt?" in the land acts and "who bears the peril?" in the sea acts.
- **`TS2`** could not hold two multi-voyage acts.
- **`RB3`** could not say that every surety in the sample answers for the working party's fault, not for the peril.
- **`LR3`** has no clear state for the gratuitous commenda.
- **`CI1` for the commenda** splits by corpus: Cassinese 1190–91 drafts `implicare separatim` (several accounts) about as often as it drafts per-libram reckoning with other goods (common), while Scriba and Amalric only show common. A single cell hides a drafting change.
- **`LR4` and `LR5` for `societas_maris`** rest on two side agreements (Amalric 697, Scriba DCCXXVII), not on the ordinary societas, which says nothing of pooling beyond its own stock.
- **`LR6` for the commenda** is observed only in Marseille; in Genoa it depends on a peril clause that Cassinese never writes.

### 5. Dependence and well-formedness problems noticed and not repaired

- `commenda LR5` and `commenda_alloc VF2` are `.NR` because their parents (`LR4`, `VF1`) are `.NR`; the vocabulary says only when the dependant is `.NA` (parent `0` or `none`), not what it is when the parent is unobserved.
- The `agent-loss-exposure` group (`AP3`, `LR1`, `CF2`, `LR6`) is not observed jointly for `societas_maris`: `AP3` and `LR1` come from one act (Amalric 774), `CF2` from 22 acts (mostly land-based), `LR6` from 119. The four cells are not a joint observation of any act, and the group's collinearity cannot be tested on them.
- For `commenda`, `CF2=0` and `LR6=upside-only` are consistent at instance level wherever both are coded (Amalric 29, 125, 364, 931); Amalric 41 is `CF2=1` and `LR6=symmetric`, also consistent.
- `AP2` overlaps `CI2` (section 8).
- `CF2` applies only where `CF1` is present. Instances with `CF1=0` (4 societas acts) carry no `CF2`; at cell level `CF1` is `1` and `P`, so `CF2` applies.
- `LR6` applies only where `LR2` is not `veiled`: the seven gratuitous commendas carry no `LR6`.
- The type census's `other` class hides 59 undrafted trade-capital acts that a reader of the editors' headings would count as commendas (decision point 1).
- The instance files carry OCR text: quotes are verbatim to the text layer, not to the print, except where `quote_checked_against_image=yes`.

### 6. What to acquire next, and which cell it would move

1. **A larger, stratified sample of sea-going Genoese societates of 1190–91**, or the rest of the Cassinese societas frame (78 unsampled acts), read against the page images, with land and sea recorded as a field. It would settle `societas_maris CF2` (now `1`, `low`) and the `fixed-term` variant of `TS2`.
2. **The Amalric notulae that Blancard did not print (413) and the full text behind his `etc.`**, from the manuscript or a complete transcription. It would move every Marseille cell that turns on the peril, profit and security clauses: `commenda LR2`, `LR3`, `LR6`, `CF2`; `commenda_alloc` `RB1`, `RB3`, `RB4`, `PR1`; `societas_maris` `RB1`, `RB3`, `CF2`. It would also remove the printed-notulae caveat from every Marseille frequency.
3. **Genoese cartularies between 1161 and 1190 and after 1191** (primary editions). They would show whether Cassinese's silence on peril and its `implicare separatim` are a drafting change or a notary's habit, and so move `commenda CI1` and `commenda CF2`.
4. **Acts of dispute over lost or unaccounted commendas** (consular sentences, arbitrations, quittances after loss). They are the only acts likely to say how a loss was proved and who answered to outside creditors: `VF1`, `VF2`, `RB4` (discharge in words), `AP3`, `LR1`, `AP1`, `AP2` for both rows.
5. **Venetian *collegantia* acts.** The row's type name includes the Venetian form, and no Venetian act is in `sources/`. They would test every `societas_maris` cell outside Genoa and Marseille, above all `CF1`, `CF2`, `RB1` and `TS2`.

## 10. Validation

Scratch copies of the two recodings files were validated outside `proposed-of/`, each against its census's `recodings` resource with the foreign key removed (the bundle holds no `data.csv` to resolve `record_id` against).

```sh
pip install --user frictionless                     # frictionless 5.19.1
mkdir -p ~/w/val && cd ~/w/val
cp <bundle>/proposed-of/recodings-commenda-primary-2026-09-28-<census>.csv rec-<census>.csv
# res-<census>.json = the <census>_recodings resource from schema/<census>.datapackage.json,
# with path set to rec-<census>.csv and schema.foreignKeys removed
~/.local/bin/frictionless validate res-organizational_forms.json
~/.local/bin/frictionless validate res-loss_mitigation_forms.json
```

Output: `organizational_forms_recodings  table  rec-organizational_forms.csv  VALID`; `loss_mitigation_forms_recodings  table  rec-loss_mitigation_forms.csv  VALID`.

## 11. Checks run by script

- Every recodings `value` is in its characteristic's `allowed_values` or is `.NR`/`.NA` (0 failures); every instance `state` likewise (0 failures).
- `.NA` propagates to `confidence`, `articulation`, `source_ref`, `source_lang`; `.NR` carries `.NR` confidence and articulation (0 failures).
- The 61 `recoding_id`s, `record_id`s, `char_id`s and censuses match `cells-in-scope.csv` exactly; the headers match `templates/`.
- Every instance quote is a verbatim substring of the act's text layer (0 not found).
- Dependence at cell level: `commenda` `LR4=.NR`/`LR5=.NR`, `LR2=coupled`/`LR6=upside-only`, `CF1=1`/`CF2=0`; `societas_maris` `LR4=1`/`LR5=synchronising`, `LR2=coupled`/`LR6=symmetric`, `CF1=P`/`CF2=1`; `commenda_alloc` `VF1=.NR`/`VF2=.NR`. `CI3` and `CI4` are both `.NR`.
- All CSVs have LF line endings (0 `\r`).
- Reserved terms: the prose of these notes and of the `notes` fields uses "peril" for the event that may befall, not "risk"; "risk" survives only in the sources' own words (`resicum`, `resegum`) and in vocabulary names quoted as such. "convergence" and "genetic" do not appear.

The sha256 of every file in `proposed-of/` is printed in the chat at the end of this stage; this file cannot carry its own hash.
