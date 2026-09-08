# Shielding-witness batch — two forms, one source each, the Antwerp form split in two — 2026-09-05

Coded by `ai` from the blind bundle `_blind-shielding-witness-2026-09-05`. Unreviewed. **The deliverable is a proposal.** Nothing in `data.csv`, `codebook.md`, `datapackage.json` or the vocabularies was touched, no `git` was run, and no existing row was recoded.

**Three** proposed rows, **96 cells**: `deed_of_settlement_company` (23 substantive, 8 `.NR`, 1 `.NA`), `compagnie_antwerpen_1582` (21, 9, 2) and `compagnie_antwerpen_1608` (21, 9, 2). Eight cells carry `articulated`.

**The Antwerp row was split in two on 2026-09-05 at the maintainer's instruction, after the coding pass and after the checks.** The two phases separate on **AP2 and FP4 and on nothing else** — see §1(a) and §6.2, where what the split bought and what it cost are both stated. Sections written before the split have been revised in place; where a statement was true of the single unsplit row and remains true of both phases, it now names both.

---

## 0. Order of work, and what was looked at when

This is the disclosure the batch's value depends on, so it comes first and it is precise.

1. Read `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `EDITING-CSV.md`, the two organizational-forms vocabularies, the `datapackage.json` field descriptions, `check_dependence.py`, `check_vocabularies.py` and the logbook headings, plus logbook 1's 2026-08-31 entry in full (the `entity` locator rule).
2. Verified both page offsets before citing either source. `printed = PDF − 25` for Televantos, checked independently at printed 15, 35, 55, 75, 105, 143 and 175 — the constant holds. `printed = PDF + 234` for De ruysscher, checked at fourteen visible printed page numbers across all 31 PDF pages.
3. Read both sources. De ruysscher **in full** (31 pages). Televantos: Introduction, chapters 1, 2 and 7, the Conclusion and the Glossary **in full**; chapters 3–6 not read. `source_read` records this honestly as `full` and `partial` respectively.
4. Settled the four pre-coding decisions in §1 below and wrote them down.
5. Wrote all 64 cells of the two rows as first coded.
6. **Only then** appended the fragment to a scratch copy and ran the checks; **only then** generated the views; **only then** recomputed which allowed values have no instance in the census.

Nothing in `views/`, nothing in the coded neighbours of `data.csv`, and no computation over the matrix was consulted before step 6. The only pre-step-5 contact with `data.csv` was reading its header row for column order.

### The bundle's own withholdings

The bundle carries explicit `[section withheld]` headings and banner blocks in logbooks 2 and 4. They were read as banners and left alone: no attempt was made to reconstruct what they covered, and their absence was not treated as a hint. The vault in the bundle was searched for `Televantos`, `deed of settlement`, `unincorporated`, `trust deed`, `De Ruysscher`, `Costuymen` and `Antwerp`. Nothing on either form exists in it; the hits are on `natie` and the Fugger, which are different institutions. `notes/Entity-shielding.md` is a 2026-07-20 stub and was read; it names neither form and did not bear on any cell.

### The empty-value recompute, disclosed

The brief says the fact is computable in about a minute and that computing it must be disclosed. It was computed, **after all 64 cells of the original two rows were fixed** (and before the Antwerp split, which changed no cell's value except by assigning `AP2` and `FP4` to phases), from `vocabularies/organizational_form_characteristic.csv` and `data.csv` on the scratch copy. The disclosure is repeated in the cell note of every characteristic it touches (`AP4`, `LR2`, `LR3`, `LR4`, `MG3`, `TS1`, `TS4`).

Allowed values with **no instance** in the census after this batch: `AP4` {`0`, `P`} · `LR1` {`none`} · `LR2` {`attenuated`} · `LR3` {`P`} · `LR4` {`P`} · `LR5` {`na`} · `LR6` {`downside-only`} · `MG3` {`P`} · `TS4` {`1`}.

Two of these bear directly on cells in this batch and neither changed: `LR2=attenuated` is the value the alternative reading in the `deed_of_settlement_company LR2` note would take, and `TS4=1` is a value a coder minded to fill an empty cell could have reached for on printed 19. Both were declined before the recompute was run and stayed declined after it. **`TS1=P` is the one value this batch supplies that the census did not have, and it was written before the recompute** — the order is what makes it worth anything.

---

## 1. The four decisions, settled before a cell was opened

### (a) Scope

**`deed_of_settlement_company` — the deed-of-settlement company specifically, not the wider class of English associations constituted by trust deed.**

*Constitutive instrument:* the **deed of settlement** — the company's articles of association, a private partnership deed which excludes the default partnership rules and settles legal title to the circulating trade assets on a fixed body of trustees. No Royal Charter, patent, or Act of Parliament.

*Period claimed:* **c.1720–1844**, from the Bubble Act (which by criminalising the issue of transferable stock without Charter or Act drove counsel to invent the form, printed 35–36) to the Joint Stock Companies Act 1844 (which forced these partnerships to incorporate by registration, printed 52). **Every coded cell rests on 1790–1827 evidence**, the period Televantos's book covers, supplemented by his reading of DuBois 1938 and of Freeman, Pearson & Taylor 2012. That gap is the `partenrederij` weakness repeating and it is written into the type row.

*Why not the wider class, and the reason is evidential rather than tidy.* Televantos's chapter 2 treats **two** trust-using business forms and they take **opposite values on the census's owner-shielding question**:

- the deed-of-settlement company had none — shareholders were partners, personally liable without limit, and limited-liability clauses "were not fully effective" (44–46, 172);
- the **testamentary trading trust** did — on *Ex p Garland* (1804) the trustee's indemnity, and so the trade creditors' reach into the testamentary estate, was capped at the sum the will set aside, which Televantos calls in terms "an example of how trusts could create limited liability trading entities" (56–60).

A row spanning both would take both values on `AP3` and `LR1`. That is the condition under which `voc` was split on 2026-08-29 and under which `partenrederij` was held apart from the open rederij. The testamentary trading trust is also not an association — it has no members — so it belongs in the acquisition list (§7), not in this row.

**`compagnie_antwerpen_1582` and `compagnie_antwerpen_1608` — a form, on De ruysscher's own terms, not a doctrinal category, coded as two phases.**

The test the brief sets is whether the source refuses the unit in its own words. It does not:

- the 1554 official declaration names a **`societas generalis`** as a thing of which one is a *socius* (240–241);
- the **constitutive instrument** is the **`contrato de sociedad`**, which the 1608 compilation required be recorded before a notary on pain of nullity (255);
- the 1582 Impressae give it a chapter of its own (cap. 58, with caps. 51–52 on the fund) and the 1608 Compilatae give it part 4 cap. 9;
- it has a **named pool** — the *corpo*, the *capitale*, "los activos de la compañía" — with default rules attaching to it.

*Periods claimed:* **1582–1608** for the Impressae phase (on evidence reaching back to c.1540) and **1608–c.1700** for the Compilatae phase.

*The split, ordered 2026-09-05, and what it is and is not.* The original proposal was one row scoped on the Impressae, with the 1608 divergence recorded in the cell notes. The maintainer directed a split, on the `voc` precedent of 2026-08-29. **The two rows separate on exactly two cells of thirty-two — `AP2` and `FP4` — and on nothing else**, and most of the shared evidence sits in De ruysscher's section II.3, which is headed *Persistencia del carácter personal de la sociedad (1582–1608)* and spans both phases by its own title. Two things follow and are written into both type rows. First, **the phase boundary is textual, not practical**: the Compilatae "no tuvo mucha influencia y el de 1582 siguió siendo el más importante en la ciudad", was never printed, and its 3,643 articles obstructed copying — though the city government did order the court to apply its commercial chapters (255). The 1608 row therefore describes an enacted text of contested reach, and `FP4=P` records exactly that. Second, **the two rows are one source read once**: on the `fraterna`/`compagnia` model, they are not two independent cases, no agreement between them is a finding, and no similarity or difference claim may count them as two.

*A third separating cell was available and was declined.* Under the identity-masking reading of `FP3`, the 1608 phase is much the richer — secret societies became lawful, and the *participatio* gave ownership with limited liability and no voice (255–256, 260–261) — while the 1582 phase says nothing. `FP3` is left `.NR` on both rows so that a separation is not manufactured by a definitional choice made *after* the split was ordered. Fixing `FP3` is worth doing on its own terms; see §4.3.

But the row inherits the source's central finding, which is that these rules **did not form a system**: the 1582 compilation "impuso tanto un blindaje débil como fuerte para las compañías; de manera que el segundo hacía innecesario el primero. No obstante, esta incoherencia no fue detectada por los compiladores de la ley" (264). That is why `AP1=1` and `AP2=P` stand together on this row, and why the cells should not be read as describing a regime.

*What each phase carries.* `compagnie_antwerpen_1582` takes `AP2=P` — Paolo di Castro's strong shielding is in the Impressae (cap. 52 arts. 5–6), so members' creditors could not reach the company's assets, while a member could still force partition by an untimely *renuncia* — and `FP4=0`, the Impressae imposing no registration on the partnership contract. `compagnie_antwerpen_1608` takes `AP2=0` — strong shielding "ya no aparecía" in the Compilatae (255), so both limbs fail, what survives being the preferential-debt rule of part 4 cap. 9 art. 27, which is priority within the pool and not unseizability, and is coded at `AP1` — and `FP4=P`, the Compilatae requiring notarial registration on pain of nullity but circulating badly. **`AP1=1` on both**, and that continuity is the point: weak shielding survives the recompilation and strong shielding does not, which is De ruysscher's "regresión a posiciones anteriores" (264) recorded as a coding rather than as a note.

### (b) The `entity` locator, applied per the 2026-08-31 rule

**`deed_of_settlement_company`: the entity is the company as the deed of settlement scopes it — the joint stock the shareholder-partners are members of — and NOT the body of trustees.**

This is the load-bearing decision for the row. Televantos writes that the trustees "acted as the legal personality for the firm" (38). Read as the trustees, `LP1`–`LP3` would answer questions about three named natural persons and the row would show a personality it did not have. Read as the arrangement, the trust is a device *inside* the arrangement and `LP1=LP2=0` with `LP3=P`. **The trust fund is not a sub-pool**: the trustees held the whole of the circulating trade assets, so the sub-pool exclusion does not bite on this row and the rule returns the arrangement without a special case. The partners' "separate estates" are their own patrimonies, not sub-pools of the entity.

**Both Antwerp rows: the entity is the *societas* / *compagnie* as the `contrato de sociedad` scopes it, whose pool is the *corpo* or *capitale*.**

Here the sub-pool exclusion **does** bite, once. From the mid sixteenth century Antwerp contracts began to carry a **`fuori del corpo`** clause under which preferential withdrawals were paid "desde un fondo separado, dentro del fondo general de la compañía", composed of additional investments or accumulated profits (247). That is internal partitioning of exactly the kind the 2026-08-31 rule excludes. It has no column; it is carried in the `CI1` and `LP1` cell notes and **not** in `confidence`. Stracca's rule that each society's *capitale* is distinct even where the partners are the same (251) makes parallel companies separate *arrangements*, not sub-pools of one, so it does not engage the exclusion.

No cell on either row was carried over from sub-pool level. Where a source supported only a sub-pool answer the cell would be `.NR`; that case did not arise.

### (c) Non-independence — and one limb of it was not in the brief

**(i) The two authors are independent of each other.** Verified here rather than assumed: a term sweep of the full text of each source for the other's name, and for `Antwerp`/`Amberes` in Televantos and `England`/`inglés`/`deed of settlement` in De ruysscher, returns no citation in either direction. Subject to (ii) and (iii), agreement between the English row and either Antwerp row is two witnesses. **The two Antwerp rows are not two witnesses to each other** — they are one source read once, and the prohibition is in both type rows.

**(ii) Both authors take the CATEGORY from Hansmann, Kraakman & Squire 2006, which is itself a coded source in this census — and supplies `AP1`'s own wording.** Televantos frames chapter 1 around HKS's asset-partitioning argument (15) and chapter 7 around it (144, 146). De ruysscher's article is titled with HKS's term and its whole structure is HKS's three-way distinction (237). So when both rows read `AP1=1`, that agreement sits **inside a borrowed grid**. It is not independent of the census, whose `AP1` column and whose `compagnia` row descend from the same paper. Each cell note says which passage is the author's own evidence and which is his restatement of HKS, and two cells were *declined* on exactly this ground — see `FP2` on both Antwerp rows and the `AP1` note's refusal to code from paragraph 1.

**(iii) THE LIMB THAT WAS NOT IN THE BRIEF: both Antwerp rows share their author with `partenrederij`.** `partenrederij`'s type row records that it was coded from **one** source, `De ruysscher 2023`. Both Antwerp rows are coded from **De ruysscher 2020**. Worse, the two works overlap in substance: De ruysscher 2020 at printed 263 discusses the *reederij*'s *pro parte* liability and Grotius's right of abandonment, which is precisely what the `partenrederij` row is coded from. **These two rows are one scholar's reading of Low Countries commercial law and must not be treated as two independent witnesses to anything they agree on.** They currently share `AP1`? No — `partenrederij AP1=.NR`. They share nothing substantive on the entity-shielding component yet, but the prohibition should be recorded before they do.

**(iv) Each row rests on one witness.** Nothing internal to a row corroborates it. The four `agent-loss-exposure` cells on each row rest on a single liability rule, the three `capital-immobility`-adjacent cells on each row on a single procedural or dissolution fact. The cell notes say "one datum, N cells" wherever this holds. **Neither row may be treated as two cases against anything.**

### (d) Scope rule for the Antwerp row, as instructed

The Holland and VOC material concentrated at printed 257 and 261–263 supplied **no cell**. `voc_1602`, `voc_1612` and `voc_1623` are coded from other sources and this row does not touch them. Also excluded and coded from nowhere here: the *reederij* (a different form, already `partenrederij`), the *commenda*-type contract ("muy excepcionales" in Antwerp, 250), and the Antwerp *natie* (a different institution, already a row).

The *participatio* is **not** excluded as a separate form: a *particeps* was a *socius* (258), so it is a position within the society, and the 1608 exception it carried from the Genoese Statuta of 1588 is recorded in the `AP3` note rather than coded as a form.

De ruysscher's disagreement with HKS is **coded as a disagreement and not resolved**, per the maintainer's standing instruction. It runs through the type row and through `AP1`, `AP2`, `CI2` and `FP4`.

---

## 2. What was coded, and on what evidence

The six `articulated` cells, because the census rarely gets them and each should be checkable in a minute:

| cell | value | the tradition's own words, on the page |
|---|---|---|
| `deed_of_settlement_company AP1` | `1` | Lord Eldon in *Ex p Ruffin* (1801), quoted at printed 165: the joint creditors "had clearly no lien whatsoever upon the partnership effects … the equity is not that of the joint creditors, but that of the partners with regard to each other, that operates to the payment of the partnership debts" |
| `deed_of_settlement_company AP3` | `0` | Lord Ellenborough in *R v Dodd* (1808), quoted at 46: "as to the rest of the world it is clear that each partner is liable to the whole amount of the debts contracted by the partnership" |
| `deed_of_settlement_company LR1` | `unlimited-joint` | the same *R v Dodd* passage — **one datum, two cells**, and the note says so |
| `deed_of_settlement_company LR3` | `1` | Watson, *A Treatise of the Law of Partnership* (2nd edn 1807) 1, quoted at 17: "upon an agreement that the gain or loss shall be divided proportionally between them" |
| `compagnie_antwerpen_1582 AP3` and `_1608 AP3` | `0` | Costuymen Impressae 1582 cap. 58 art. 1, its own Latin terms *in solidum* and *pro toto*, at 251 — the rule persists into the Compilatae phase, so both rows rest on it |
| `compagnie_antwerpen_1582 LR1` and `_1608 LR1` | `unlimited-joint` | the same article — **one datum, two cells per row, and the same datum across both rows** |

`articulated` was **withheld** from `MG4` on both rows even though Lord Eldon's and the Costuymen's words are on the page, because the value set (`state-charter | customary | private-contract | religious`) is the analyst's comparative concept. The line held throughout: `articulated` goes where the tradition states the coded proposition in its own idiom, not where it merely uses a word the analyst also uses.

The other 38 substantive cells are `analyst-imposed` and each names its pages. The strongest of them:

- **`deed_of_settlement_company FP4=0`** — no shareholder register; Lord Eldon *proposed* one in June 1824 and never brought the bill in (45, 51); registration arrived only with the 1844 Act (52). The row's period ends where this cell would flip.
- **`deed_of_settlement_company MG4=private-contract`** — the absence of Charter or Act is the form's defining feature and the source of its criminality (35, 43, 50).
- **`LP1=0` on both Antwerp rows** — "no se desarrolló ningún concepto de velo corporativo" (239), with De ruysscher's own footnote that calling a company a *universitas* postdates the asset-separating rules (237 n 2).
- **`AP1=1` on both Antwerp rows** — Impressae cap. 52 art. 5 for the 1582 phase, Compilatae part 4 cap. 9 art. 27 for the 1608 phase, both probably on the Genoese Statuta 1588 model (book 4 cap. 12).
- **`compagnie_antwerpen_1608 AP2=0`** — the cell the split exists for: strong shielding "ya no aparecía en el compendio del derecho de Amberes de 1608" (255), which De ruysscher himself calls a regression (264).

---

## 3. What could not be coded, and why

Seventeen `.NR` and three `.NA`. Judged by the brief's standard — the `.NR` count, not the fill rate — the honest report is that **these are two rich sources and the rows are correspondingly dense**, and the density should be checked cell by cell rather than trusted.

**`.NA` — inapplicable, and why:**

- `AP4` on all three rows — no founder. Both forms arise by subscription or contract, and the 2026-08-30 rule returns `.NA`, not `0`, for a form whose corpus was arrived at by partitioning rather than constituted by endowment.
- `MG3` on both Antwerp rows — `MG1=contract`, which the vocabulary and `check_dependence.py` declare blocking.

**`.NR` — the source is silent, or the question is not the one the characteristic asks:**

- `TS2`, `TS4` (`deed_of_settlement_company`) — Televantos never asks the intended duration, and printed 19 on unanimous consent to change the scope of business is about binding partners to debts, not about a concern altering its own rules.
- `TS4` (both Antwerp rows) — De ruysscher's subject is assets and creditors, not the partners' power over their own contract.
- `CI3`, `CI4` (both Antwerp rows) — alienability of a *socius*'s share is never asked. The Genoese *particeps* and south German *Teilhaber* material at 258–259 is about **withdrawal**, not transfer, and is not Antwerp.
- `CF2` (both) — the 2026-08-18 `AP3` disposition applied in the mirror: both sources establish liability to the **venture's creditors** and neither asks whether a working party answered to a capital-supplying party for capital lost. `CF1=P` on both rows means the cell is applicable and empty, not inapplicable.
- `LR4`, `LR5` (both) — see §5.
- `FP2` (both Antwerp rows) — the one adjacent passage (237, on seventeenth-century state companies' sovereign monopoly) is De ruysscher's **restatement of HKS, citing their page 1378**, not his evidence about Antwerp. Coding `0` from it would launder a restatement into an observed absence. Contrast `deed_of_settlement_company FP2=0`, where Televantos puts the question himself.
- `FP3` (all three), `MG1` and `MG3` (`deed_of_settlement_company`), `CF3` (both Antwerp rows) — see §4; these are characteristic or vocabulary problems, not source silences.

**`MG3` on `deed_of_settlement_company` is deliberately `.NR` and not `.NA`.** `MG1` is `.NR`, so whether the cell applies is undetermined; `.NA` would assert that `MG1` takes a blocking value, which is exactly what is unknown, and `check_dependence.py` cannot tell the two apart.

---

## 4. Characteristics that did not fit the evidence — flagged, not repaired

Four, and none is proposed for repair. Per `CHARACTER-CODING.md` and the 2026-08-30 (ii) precedent, a repair must not be proposed inside the pass that motivates it.

### 4.1 `AP2` asks two questions, and this pair separates them

This is the batch's well-formedness finding in Sereno's sense, and the vocabulary already half-suspects it (`AP2`'s definition flags overlap with `CI2` and calls it "a candidate for merger rather than grouping"). The defect is different from the one flagged: **`AP2` bundles *can members force partition* with *can members' creditors force partition*.**

| row | members' creditors | members | column reads |
|---|---|---|---|
| `compagnie_antwerpen_1582` | **cannot** — 1582 Impressae cap. 52 arts. 5–6, company assets unseizable for a partner's personal debts | **can** — an untimely *renuncia* dissolves the society, at the cost of damages (253) | `P` |
| `compagnie_antwerpen_1608` | **can, subject to ranking** — strong shielding gone (255); what survives is priority within the pool, not unseizability | **can** — the *renuncia* rule is unchanged (253) | `0` |
| `deed_of_settlement_company` | **cannot** — a separate creditor reaches only the residue after partnership creditors (148) | **cannot in practice, can in law** — dissolution at will survives as a right (24) but Chancery would not hear the suit (51) | `P` |

Both rows read `P`. **The two `P`s are not the same state, and the column cannot say so.** A reader taking the column at face value would record an agreement between two unrelated traditions that does not exist. The evidence for the split is two codings that collide, which is what `CHARACTER-CODING` test 1 asks for; the repair is not proposed here.

There is a second axis on the Antwerp side that the column also cannot carry: the creditors' limb is a fact about the **1582** compilation and would fail on **1608**.

### 4.2 `LR4` does not distinguish one venture's outcome shared from members' separate baskets mutualised

`LR4` reads "mutualizes idiosyncratic risk across members versus unshielded". Both forms pool contributed capital into **one** venture whose outcome all members share — which is `LR3`'s question — and neither source asks whether members' **separate** risks were mutualised. The Antwerp *periculum communis* material (253) is loss-sharing inside one venture. Some deed-of-settlement companies were fire offices (36), but what a fire office pools is its **policyholders'** peril, not its members'.

Coded `.NR` on both rows rather than forced. Whether `LR4` is one question or two is a real matter, but it is not settled by two rows that both decline it, and no repair is proposed.

### 4.3 `FP3`'s definition is underdetermined between two readings, and the two sources fall on opposite sides

`FP3` reads "the form confers legal-status or access arbitrage for its principals". The census's worked instance is **identity-masking** (the *nación flamenca*; the vault's `Entity-shielding` stub calls the facet "identity-wrapper — the corporate form as a flag-of-convenience masking a foreign principal").

- Under the **identity-masking** reading, De ruysscher is rich and Televantos is silent: merchants invested while keeping their names out of the company name so creditors could not reach them (252–253); secret societies became lawful in 1608 (255–256); the *participatio* gave ownership with limited liability and no voice (260–261).
- Under a **status-arbitrage** reading, Televantos is rich and De ruysscher is silent: the whole form exists to obtain corporate-like advantages without the Crown's grant — and his finding is that it largely failed, eliciting no more than "bare tolerance" (52).

Which question `FP3` asks decides whether these rows are `.NR`/`.NR`, `P`/`.NR`, or `.NR`/`P`. Both are left `.NR` with the evidence recorded on both sides. **This is a definitional gap, not a source silence, and the distinction is in the cell notes.**

### 4.4 Two vocabulary gaps where no allowed value states a fact about the form

- **`MG1` on `deed_of_settlement_company`.** Allowed: `membership | contract | beneficiary`. The shareholder is **all three at once and by design** — a member of the company, a party to the deed and so in law a partner (44), and a beneficiary of the trust in which the assets are vested. Televantos's own term is "beneficiary-shareholders" (45). `.NR`, not the nearest wrong value.
- **`CF3` on both Antwerp rows.** Allowed: `bilateral | multilateral`. The Antwerp general partnership was routinely both — the worked problem is a "sociedad bipersonal" (245), and 242 has "sociedades de mayor tamaño con muchos miembros". Membership size is not fixed **by the form**, so neither value states a fact about it. `.NR`. This is the first `.NR` `CF3` has ever carried in the census; the previous values were `.NA`, `bilateral` and `multilateral`.

---

## 5. Dependence and well-formedness problems noticed and NOT repaired

Beyond §4:

1. **`check_dependence.py` still prints only ONE separation per unordered pair, and it is not always the strongest.** Logbook 1, 2026-08-18 recorded this and it has not been fixed. It matters here: the checker's report on this batch **hides two of the separations the batch produces**, including one that is strong on both sides. The full set is in §6, computed by hand. No change to the script is proposed.
2. **`build_views.py --check` without `--dataset` looks in the wrong vocabulary and exits 1** with "no characteristics with component 'entity-shielding' in `loss_mitigation_characteristic.csv`". A caller could easily read that non-zero exit as "the view is stale". It nearly produced a false finding in this session — the committed views for all six WP2 components are in fact **up to date** in the bundle. The same shape as the `check_dependence.py --dataset` trap the brief warns about. Reported, not repaired.
3. **`joint_stock` has no scope note. — CORRECTED 2026-09-05, and the correction changes the recommendation.** This item originally read "a type row with no scope note **and no cells at all**", and the second half was **false**. It rested on the `entity-shielding` view, where `joint_stock` shows `--` on `AP1`, `AP2` and `AP4` — three characteristics out of thirty-two. Counting by `type_id` in `data.csv` gives the real figure: **`joint_stock` carries two cells**, `OF-0032 LP1=1` (note: "chartered legal personhood") and `OF-0033 AP3=P` (`low`), both `coder=ai`, `source_ref=Harris 2020`, `source_read=unknown`, `articulation=.NR`. Ten of the census's forty type codes carry no cell at all; `joint_stock` is not one of them. **A `--` in a component view means "no row on this characteristic", and a component view covers three or four characteristics, so it cannot tell you whether a form is uncoded.** — What survives the correction: `LP1=1` with "chartered legal personhood" **already fixes the referent** as the chartered corporation, which excludes the proposed form (`LP1=0`), so the two rows differ on the first characteristic either touches and **this is not a blocker**. What remains is a documentation gap — the referent lives in a cell note no reader of the type vocabulary will find, while Televantos's glossary makes "joint stock company" a synonym for the *unincorporated* form (183). A draft scope note is at `proposed-of/PATCH-joint-stock-scope-2026-09-05.md`, for approval, to land **with** the batch rather than ahead of it. That file also raises the larger problem the correction exposed: on the chartered reading `joint_stock` is an **umbrella over `voc_1602`, `voc_1612` and `voc_1623`**, which are coded at full 32 — the defect logbook 2 records for `ie`, `piaohao` and `kabu_nakama`.
4. **Slug near-collision, and the split has reduced it.** `compagnie_antwerpen_1582` / `_1608` and the coded `compagnia` name unrelated institutions in different traditions; the year suffixes now separate them at a glance, where the bare `compagnie_antwerpen` did not. The hazard is recorded rather than repaired. `societas_generalis_antwerpen_1582` / `_1608` would be safer still.
5. **`AP4` still has no discriminating power**, exactly as its own definition warns: two coded forms, one value between them, and `0` and `P` both empty. This batch adds two more `.NA`s and does not help. §7 names the acquisition that would.

---

## 6. Verification — every command, in the form actually run, and what it printed

On a scratch copy (a `cp -R` of the bundle's `HistorEE_codebooks`), with the rows appended under **temporary** ids and the type rows appended to the type vocabulary. Run twice: first on the two rows as originally coded (`OF-0708`–`OF-0771`, two type rows), and again after the Antwerp split on the three rows (`OF-0708`–`OF-0803`, three type rows). Every result below is from the second, post-split run; the first run gave the same verdicts. A pristine copy at `~/scratch/base` served as the control. The bundle itself was not modified. **No `git` was run.**

**`frictionless` was not installed** on the machine and was installed for this batch: `python3 -m pip install frictionless` → **5.19.0**.

| # | command, exactly as run | exit | what it actually printed |
|---|---|---|---|
| A | `python3 scripts/check_dependence.py datasets/organizational_forms` | 0 | a full report: "no applicability problems", "no articulation problems", and six redundancy groups with their signatures — reproduced in part in §6.1 |
| B | `python3 scripts/check_vocabularies.py` | 0 | `✓ vocabularies valid — 6 files, 165 codes; no ragged rows, all references resolve, all values within allowed_values, enums agree, shared type rows agree` |
| C | `python3 scripts/check_dependence.py --dataset datasets/organizational_forms` | **0** | `no characteristic vocabulary registered for '--dataset'; nothing to check` — **the trap the brief names, confirmed: it exits 0 having checked nothing.** Not used for any claim here |
| D | `python3 -m frictionless validate datasets/organizational_forms/datapackage.json` (with the new rows) | 0 | a dataset table: `organizational_forms | table | data.csv | VALID` |
| E | the same on the pristine control | 0 | `VALID` — so D is not a vacuous pass |
| F | `python3 scripts/build_codebook.py --check` (with the new rows) | **1** | `datasets/organizational_forms/codebook.md: stale — regenerate with build_codebook.py`. **Expected**: `codebook.md` publishes row counts and per-field fill counts. On the pristine control the same command exits **0** and prints `current` for all three datasets. The maintainer regenerates on merge |
| G | `python3 scripts/build_views.py --dataset organizational_forms --component <c> --mechanism all --check` for all six WP2 components | 0 on the control, 1 with the new rows | the committed views are **current** in the bundle and go stale on merge, as expected. Note the invocation: **both** `--dataset` and `--mechanism all` are required or it fails for the wrong reason (§5.2) |
| H | hand sweep of `value` against `allowed_values`, with `.NA`/`.NR` propagation | 0 | `0 problems` over all 96 rows |

### The hand sweep, since "0 problems" is not self-explanatory

Written for this batch and run over the fragment before it was appended anywhere. For every row it checks: `value` ∈ that characteristic's `allowed_values` (split on `|`) ∪ {`.NR`, `.IL`, `.NA`}; where `value` is `.NA` or `.NR`, that `confidence`, `articulation`, `source_ref`, `source_lang` **and** `source_read` all carry the same token; where `value` is substantive, that `confidence`, `articulation`, `source_lang` and `source_read` are in their schema enums, and that no `articulated` cell sits beside `[verify]`, `.NR` or an empty `source_ref`; and that `record_id`, `coder` and `reviewed_by` are non-empty. Ninety-six rows, zero problems. `frictionless` sees none of this: it validates types, enums and keys, and cannot see the per-characteristic `allowed_values` at all.

### 6.1 What changed in the matrix — the finding

**One characteristic takes a value it had never taken.**

> **`TS1` = `P`** — `deed_of_settlement_company`. Before this batch the coded values of `TS1` were `1`, `0` and `.NR` only. The half is structural and is the form's whole point: settling the assets on a fixed body of trustees "insulate[d] the company from the effect of the rules effecting mandatory partnership dissolution upon any change of partners" (38), so the **pool** survives a member's exit while the **entity** does not — the courts treated these firms as partnerships throughout (43–46), and a single business in fact could be, in law, a succession of separate partnership estates (150).
>
> The value was written from the source before anything about the matrix was computed. That ordering is the only thing that makes it evidence rather than a fill.

**Two separations appear that the checker does not print** (see §5.1; the checker emits one line per unordered pair). Computed by hand over all ordered pairs, before-and-after:

- **`capital-immobility`: `AP2=P` occurs with `CI2` in {`1`, `P`} — strong on both sides.** `compagnie_antwerpen_1582` (`P`,`P`) against `asiento_averia` and `deed_of_settlement_company` (`P`,`1`). Before this batch the group's only substantive separation was `AP2=1` → `CI2` ∈ {`1`,`P`}. **`AP2=P` now fails to determine `CI2` as well**, and `AP2`/`CI2` are the pair the vocabulary calls a merger candidate. That is evidence against merging them.
- **`legal-personhood`: `LP3=P` occurs with `LP2` in {`0`, `1`, `P`} — strong on both sides.** Before, `LP3=P` occurred only with `LP2` ∈ {`1`,`P`}. `deed_of_settlement_company` supplies the census's **first form with no property capacity in the entity and partial standing to sue** — the trustees could sue at common law without joining the members while the company could not sue at all.

Three further widenings are weak (they run through a missing token) and are recorded without weight: `AP3=0`, `LR1=unlimited-joint` and `LR6=symmetric` each now occur with `CF2=.NR`; `TS2=.NR` now occurs with `TS1` ∈ {`1`,`P`}.

**Two new signatures, and one collision worth noting.**

- `entity-shielding` view: **`AP1=1` with `AP2=P` is a combination no form had.** Both new rows take it, from unrelated evidence in unrelated traditions. `AP2=P` goes from one form to three.
- `legal-personality` view: `deed_of_settlement_company` reads `0 · 0 · P`, a signature no form had. **Both Antwerp rows read `0 · 0 · 0`, which is exactly `isqa`'s** — a complete triple-zero on legal personality reached by a wholly different route, though the two Antwerp rows are one witness to it, not two.

### 6.2 What the split bought, and what it cost

**Bought.** One substantive contrast the unsplit row could not have produced: `compagnie_antwerpen_1608` is the census's **first form at `AP2=0` with `CI2=P`**, so `AP2=0` now occurs with `CI2` in {`.NR`, `0`, `P`} where before it occurred only with {`.NR`, `0`}. The added member is substantive, though the set as a whole still contains `.NR` (from `compagnia`), so `check_dependence.py`'s strictness rule reports the pair as separated *via a missing token* — that classification understates it, and the substantive contrast is `0` against `P`. The `AP2`/`CI2` grid now has ten occupied pairs across 33 coded forms, and the two Antwerp rows occupy two of them, `(P,P)` and `(0,P)`, both new to the census. Together with the `AP2=P` → {`1`,`P`} separation the unsplit row already gave, the capital-immobility group is now separated at two distinct `AP2` values, which is evidence against the merger with `CI2` that `AP2`'s own vocabulary definition contemplates.

**Cost.** The census gains a form count it has not earned: 33 coded forms where 32 would be the honest number, because two of them are one source read once and differ on two cells of thirty-two. Every other census-level result is unchanged by the split — `TS1=P` and `CF3=.NR` are still the new values, and the two strong separations (`AP2=P` → `CI2` in {`1`,`P`}; `LP3=P` → `LP2` in {`0`,`1`,`P`}) are exactly as they were. **The prohibition in both type rows is what keeps the cost from becoming a false *n*, and it should be read as binding rather than decorative.**

**The pooling facet gains nothing.** `LR4`/`LR5` = `.NR`/`.NR` now holds for four forms (`compagnia`, `fraterna`, and both of these). That is a fact about what commercial-partnership sources ask, not about the institutions.

**Both new rows land in the *same* `agent-loss-exposure` signature** — `AP3=0`, `CF2=.NR`, `LR1=unlimited-joint`, `LR6=symmetric`. That agreement is real and independent between the two authors, but on each row all four cells rest on **one** liability rule. It is two witnesses to one proposition, not eight.

---

## 7. What to acquire next, and which cell it would move

Ranked by how much the acquisition would move, not by how easy it is.

1. **A testamentary trading trust source — and it would move `AP4`.** `AP4` has two coded forms, one value between them, `0` and `P` both empty, and its own definition says in terms that it "has no discriminating power yet and must not enter a similarity or difference claim … until a founder-endowed form takes a value other than 1". The testamentary trading trust is founder-endowed *and* has a corpus that does **not** leave the founder's estate — it stays in the testamentary estate under a trust, with trade creditors' reach capped at the sum settled (*Ex p Garland* (1804), Televantos 56–60). That is a live candidate for `AP4=0` or `P`, which is the exact remedy the vocabulary names. It would also give `AP3` a second English value and test §4.1's split from the other side. **Start with Televantos chapter 2 §3, which is in hand, plus Alistair Owens, "Inheritance and the Life-Cycle of Family Firms in the Early Industrial Revolution", *Business History* 44 (2002) 21, and Aleksi Ollikainen-Read, "Creditors' Claims against Trustees and Trust Funds", *Trusts and Trustees* (2018) 177** — both cited by Televantos at 53 n 156 and neither, on the evidence of this bundle, held.
2. **DuBois, *The English Business Company after the Bubble Act 1720–1800* (1938), and Freeman, Pearson & Taylor, *Shareholder Democracies?* (2012).** Televantos's own eighteenth-century evidence is DuBois's, at second hand, and the 209-of-224 trust figure is FPT's. Holding them directly would close the period gap this row declares — `TS2` and `TS4` are `.NR` largely because Televantos does not go to the deeds themselves, and FPT chapter 3 examines the deeds. **They would move `TS2`, `TS4`, `CI3`'s confidence and possibly `MG2`.**
3. **The Costuymen themselves — de Longé's editions of the *Impressae* (1870) and the *Compilatae* (1872–74)**, which De ruysscher cites throughout by chapter and article. Every Antwerp cell here rests on his paraphrase, with only *in solidum* / *pro toto* and *fuori del corpo* surviving as the tradition's own words. **Holding the two editions would let four or five Antwerp cells move from `analyst-imposed` to `articulated`**, which is the scarcest thing in this census, and would let a coder settle the 1582/1608 scope question on the texts rather than on De ruysscher's assessment of their circulation. That last point matters: `AP2` and `FP4` both turn on it.
4. **A second, non-De-ruysscher source on Antwerp partnership law — Bram Van Hofstraeten** is the obvious one, cited a dozen times here ("Antwerp Company Law Around 1600 and its Italian Origins", 2016; "The Organization of Mercantile Capitalism in the Low Countries", 2016; "Limited Partnerships in Early Modern Antwerp", 2015). De ruysscher records that he **disagrees with Van Hofstraeten** on whether the 1608 compilation contained *contractus trinus* rules (256 n 85) and on the Genoese origin of the *deelhebber* article (259 n 109). That is a live scholarly dispute this row currently records only from one side, and it would break the author-level non-independence in §1(c)(iii).

**Not recommended now.** A second English joint-stock source (Harris, *Industrializing English Law*) — it is already Televantos's principal interlocutor and would corroborate rather than test. And nothing on the `pooling` facet: these are commercial partnerships and the facet is empty for a reason about the form, not about the library.

---

## 8. Housekeeping

- **Placeholder ids.** The fragment carries `OF-XXXX-01` … `OF-XXXX-96`. Real ids are the maintainer's at merge; the last id in the bundle's `data.csv` is `OF-0707`, so `OF-0708`–`OF-0803` is the obvious block and is what the scratch verification used.
- **ASCII.** Notes and type-row text are plain ASCII with straight quotes, matching the existing vocabulary rows (which write "Gonzalez de Lara", "voorcompagnieen", "societa in accomandita"). Spanish quotations are therefore transliterated without accents. Say the word and they can be restored as UTF-8; the files are already UTF-8 and the scripts read them as such.
- **Citations.** Televantos's book DOI `10.1093/oso/9780198870340.001.0001` was resolved through CrossRef on 2026-09-05 and returns *Capitalism Before Corporations*, Andreas Televantos, OUP, 2020. **De ruysscher 2020 has no DOI** — checked; the Tilburg University research portal record carries none and the article is open at the BOE's Biblioteca Jurídica Digital and at `revistas.mjusticia.gob.es`. Two flags travel with it: the volume is *tomo* XC / 2020 as printed on the article's own running feet, but the issue appeared in **2021** and Tilburg dates it so (received 28 September 2019, accepted 2 March 2020); and the article prints "D. de Ruysscher" while this census already cites the same author as "De ruysscher 2023" in the `partenrederij` row, whose spelling is followed here.
- **Not repaired, per the standing limits:** nothing in `data.csv`, `codebook.md`, `datapackage.json` or `vocabularies/`; no existing row recoded; no characteristic proposed; no script changed; no file deleted or renamed; no `git`.
