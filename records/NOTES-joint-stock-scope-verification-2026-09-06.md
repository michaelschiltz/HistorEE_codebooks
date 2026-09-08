# `joint_stock` scope and the sub-pool correction — verification pass, 2026-09-06

**Open pass. Slug `joint-stock-scope-verification`.** No blind, no bundle, and that was a decision taken in advance rather than an omission: the vault holds a note titled *"Harris 2020 on the late plurality of limited liability"*, in this vault a filename is a claim (logbook 4, 2026-08-16), so the blind on this source was already spent by `joint-stock-scope-scheme`. Withholding it would have meant excising 27 notes across nine session slugs for one 22-page article — and the work here is documentation and scope, which no blind protects. **The vault was never opened by this session.** `data.csv` not edited; `git` not run.

Companion to `NOTES-joint-stock-scope-2026-09-05.md`, which is the brief this session executed, and to `PATCH-joint-stock-scope-2026-09-05.md`, whose positive half is now written. **Neither is overwritten**; this file is suffixed `-verification-` for that reason.

## 0. The suite was green before the tree was dirty, and here is what each command actually printed

Run on the clean tree at 803 rows. **`frictionless` was not installed; installed for this session, 5.19.0.**

| command, in the form actually run | what it printed |
|---|---|
| `python3 -m frictionless validate datasets/organizational_forms/datapackage.json` | a one-row table, `organizational_forms / table / data.csv / **VALID**` |
| `python3 scripts/check_dependence.py datasets/organizational_forms` | applicability "no applicability problems", articulation "no articulation problems", six redundancy groups printed with their full value tables, all six **SEPARATED on substantive values**, then `dependence problems: 0` |
| `python3 scripts/check_vocabularies.py` | `✓ vocabularies valid — 6 files, 165 codes; no ragged rows, all references resolve, all values within allowed_values, enums agree, shared type rows agree` |
| `python3 scripts/check_softwrap.py` | `29 file(s) OK — no hard-wrapped prose.` |
| `python3 scripts/build_codebook.py --check` | three lines, `current` for each of `clearing_records`, `loss_mitigation_forms`, `organizational_forms` |
| `python3 scripts/build_views.py --dataset organizational_forms --component <c> --mechanism all --check`, nine times | nine lines, each naming its view file and `current` |

**The path form of `check_dependence.py` was used and the flag form was not**, per the standing warning that `--dataset <x>` prints "no characteristic vocabulary registered" and exits 0 having checked nothing. **`build_views.py` was given both `--dataset` and `--mechanism all` every time**, per the standing warning that without them it reads the wrong vocabulary, exits 1, and looks like staleness. **No cell was reconsidered after the tree was made dirty.**

## 1. The sub-pool correction

Full record at logbook 1, 2026-09-06. **40 `entity`-locator cells examined across the five forms added since 643 rows, 29 of them substantive. Three sub-pool forms confirmed, two not, no cell recoded.**

| form | sub-pool? | decided on | cells / substantive | recoded |
|---|---|---|---|---|
| `avariz_vakfi` | **yes**, against its own type row | Kıvrım 2019, printed 39–40, Tablo 1 and Tablo 2, re-read in the Turkish | 8 / 4 | 0 |
| `bruderschaft_salzburg` | no | Klieber: one association, one *Vermögen*, one annual balance; affiliation does not pool capital | 8 / 3 | 0 |
| `deed_of_settlement_company` | no | the trust splits **title**, not the pool | 8 / 8 | 0 |
| `compagnie_antwerpen_1582` | **yes** | *fuori del corpo*, "un fondo separado, dentro del fondo general de la compañía" (247) | 8 / 7 | 0 |
| `compagnie_antwerpen_1608` | **yes** | as its sibling | 8 / 7 | 0 |

**`avariz_vakfi` is the one that was genuinely contested and MS asked for it to be tested rather than assumed.** Its type row scopes the arrangement down to the *bölük* precisely to avoid being a sub-pool form, and its own `CI1` note flags that a reviewer scoping to the *mahalle* "GETS several-accounts AND A SUB-POOL FORM". **Kıvrım's own enumeration decides it against the row.** Tablo 1 is headed *Avârız Para vakfı olan mahalleler* and its `No.` column runs 1–9 **by quarter**, with all nine Ammu entries under the single number **6**; the prose names Ammu as the quarter with the most money, **857.5 kuruş**, which is the sum of its nine *hâne*; printed 40 says that while the *avârız hâne* is the unit of **assessment**, in **collection** the quarters are what is taken into account; and Tablo 2 lists **one** elected *vekil* per quarter, Ammu's included. One obligation, one representative, nine internal pools with nine trustees. That is the sub-pool structure.

**And the result that matters: the scoping question changes no coded value.** Four of the eight cells are already `.NR`. `LP2=1` rests on Kars 174 and 181–182 — Mercan Ağa and Gülcamii, both undivided quarter funds. `LP3=1` rests on the Tovbe and Tarlayıatik trustees, Tarlayıatik being Tablo 1 no. 4, undivided. `MG4=religious` rests on Kars 175 and Küçük 149–151. `FP4=1` rests on registration, which happened at whichever level the fund sat. **The row is a sub-pool form and survives being one**, which is the first time the rule has been tested on a row whose scoping was chosen partly to avoid it.

**`deed_of_settlement_company`: MS asked for his own argument to be tested against him, and it holds.** Three grounds, and a falsification condition so it can be overturned rather than merely asserted — all at logbook 1, 2026-09-06. The strongest is that the partners' separate estates lie **outside** the arrangement and are the very thing `AP1` measures against, so reading them as sub-pools would make `AP1` predict itself: the same discriminant-validity failure the 2026-08-31 rule was written to avoid.

**One improvement noticed and not made.** The *fuori del corpo* fund is a second route by which an Antwerp partner takes value out of the pool, which bears on `AP2`'s member limb, and it appears only in the `CI1` notes. Adding it is recoding rows this session was not licensed to touch.

**The eight definitions now record both runs, and one rule is changed rather than restated: the test for a sub-pool form is the SOURCE'S OWN ENUMERATION, not the type row's scoping.**

## 2. The source, read in full

**Harris, R., 'A new understanding of the history of limited liability: an invitation for theoretical reframing', *Journal of Institutional Economics* 16:5 (2020), 643–664, DOI 10.1017/S1744137420000181, Zotero `6FN9JG5S`.** Read in full 2026-09-06.

**Offset re-derived rather than taken from the brief: `printed = PDF + 642`, verified at 22 consecutive points — every printed page** — from the even pages' `NNN Ron Harris` running heads, the odd pages' `Journal of Institutional Economics NNN` heads and page 1's masthead. **The brief said 21 points; the true figure is 22. And the PDF has 23 pages, not 22: the last is blank.** Both corrections are small and both are the kind of thing an offset gets wrong.

Term counts reproduce the brief's exactly — `limited liability` 189, `reserve liability` 15, `double liability` 9, `unlimited liability` 28, `deed of settlement` **0** — and add **`triple liability` 5**, which the brief did not count and which matters for §5.

## 3. Which Harris, and it was ambiguous three ways rather than two

Full reasoning at logbook 5, 2026-09-06. **The answer is the article, `6FN9JG5S`.**

- **A third held candidate the brief did not consider**, found by listing the store: `Harris - 2020 - General Average and All the Rest`. **Ruled out by measurement**: across 77,547 characters it contains `legal personalit*` **0** times and `chartered` **0** times, so it cannot be the source of "chartered legal personhood".
- **`OF-0033`'s note is the article's abstract almost verbatim**, and *Going the Distance* ends in 1700 and cannot carry a claim about 1800–1930.
- **`OF-0032` and `OF-0033` together are the article's central thesis**, which is the title of its own §2.4: *"Legal personality is not limited liability"*.
- **The row's period, "17c onward", matches the article and contradicts the book's 1400–1700** — which explains the discrepancy `PATCH-joint-stock-scope-2026-09-05` flagged as unexplained.
- **The evidence the other way, and it is why the string had to be disambiguated rather than simply read:** inside this very article Harris's reference list carries *Going the Distance* and **no entry for the article**, and he cites "Harris, 2020" in his own text at printed 646 and 650 to mean the book. **Read as its own author uses it, the bare string names the wrong work.**
- **Only one work is cited, so the one-author-twice problem does not arise — but it is one acquisition away**, and the `partenrederij` / `compagnie_antwerpen` precedent is written into the type row so that it binds whoever adds the book.

## 4. The umbrella question, settled

Full reasoning at logbook 2, 2026-09-06. **Outcome 3: keep as a declared umbrella, uncoded, with a standing prohibition.**

**The count that decided it.** Ten of the census's 43 type codes carry no cells, and **every one of them is an umbrella or a parent** — `confraternita`, `ie`, `piaohao`, `kabu_nakama`, `waqf_ahli`, `mudaraba`, `ortoq`, `ton_ya`, `hegu_gangu`, `gugu_death_share`. **In this census an umbrella carries zero cells. `joint_stock` carrying two was the anomaly**, and `confraternita` of 2026-09-04 is the worked precedent for what to do about it.

**Narrowing rejected**, and not because it is a bad idea: it does not save this row, it creates a different one under this row's code — the `voc` mistake in reverse, `voc` having been **split and its parent retired**, not renamed. The narrowed row is the right thing to want and is §6's recommendation.

**Retiring and moving the cells rejected**: `LP1=1` would collide with three `voc` rows coded from a source Harris expressly disputes, and `AP3=P` has no home at all, the `voc` rows coding `AP3` as `0`, `0` and `1`.

**A sharper reason than the umbrella, found by the reading.** This row's source and its children's sources are on **opposite sides of a direct dispute about the same institution**: Harris at printed 646–647 names Dari-Mattiacci et al. and Gelderblom, de Jong & Jonker and rejects them — *"I think that this interpretation of historical facts is misjudged"* — and holds there is no evidence a passive-shareholder liability regime was defined "in 1602, in 1623 or at any later stage". **`voc_1623 LR1=limited` and `AP3=1` rest on the reading he rejects. NOT TOUCHED**, per instruction and on the `bazacle_mill FP1=mixed` disposition. **The wrong is the silence, not the value.**

**`name` gains "(umbrella)"**, on `confraternita`'s convention — flagged twice before and left standing twice, which is the reason for doing it rather than flagging a third time.

## 5. `LR1`, flagged and refused

`PATCH-LR1-multiple-of-subscription-2026-09-06.md`, which names **no value, no code and no locator**. The gap: no allowed value states **exposure capped at a multiple of the subscription**. It is not marginal — 62 reserve-liability banks against 40 limited in England and Wales in 1889, and US double liability not fully repealed until 1959. **Refused for three reasons**: the standing rule against repairing inside the motivating pass; **no census form would take the value**, and `LR1=none` is already `×0`, so a second empty value repeats the `AP4` mistake; and MS's explicit instruction. What would license it, with two named acquisitions, is in the patch.

## 6. What to acquire next, and which cell it moves

**Harris 2000, *Industrializing English Law: Entrepreneurship and Business Organization, 1720–1844* (CUP). Not held. Wanted for a third and stronger reason than the two already on file** — the shielding-witness brief wanted it as the HKS-sceptic corrective and §11.2 as the independent voice against Morley. **This pass wants it because it is the book that would let the English chartered corporation be coded as a form**, which is what `joint_stock` should have been.

**The cell it would move: `LP1` on a new `chartered_corporation_england` row**, c.1600–1844, with `AP3` and `LR1` following. That row is the natural counterpart to `deed_of_settlement_company`, which already holds the English *unincorporated* form; the two would differ on `LP1` by construction and would carry the chartered/unchartered contrast the English literature turns on. ~~**It is also where the `LR1` gap first becomes testable rather than hypothetical**, since the chartered banks are in it.~~ **CORRECTED 2026-09-06 (ii): WRONG, and the acquired file disproves it.** `reserve liability` 0, `double liability` 0, `uncalled` 0 across 331 pages — reserve liability was created in 1879 and US double liability spread after 1863, both outside the book's 1720–1844 period. The `LR1` multiple-of-subscription gap still needs Acheson, Hickson & Turner 2010 or Macey & Miller 1992, as the patch says. Harris 2000 does supply a *different* `LR1` problem at printed 129. See logbook 5, 2026-09-06 (ii).

Second priority, unchanged from §11.2: **Morley 2016**, open access, a download rather than a purchase. `AP4` remains an acquisition problem and this is the sixth session to leave it standing.

## 7. What was not done, and on whose instruction

`git` not run. The AP4 batch not started. `voc_1602`, `voc_1612`, `voc_1623`, `casa_san_giorgio`, `maona_chios` and `maona_corsica` not touched. **`data.csv` not edited at all** — including the two `joint_stock` cells, whose removal is proposed rather than applied because deleting rows this session did not create is reserved and because it forces an id-policy choice the census has never faced. See `RETIRE-joint-stock-cells-README-2026-09-06.md`. **No version bump.**
