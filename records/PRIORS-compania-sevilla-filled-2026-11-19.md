# Priors — compania-sevilla-2026-11-19 (first coding of `compania_factoria_sevilla`)

Filled as a copy of `PRIORS-TEMPLATE.md` before anything in `sources/` was opened.

- Filled by (model identifier and effort): `claude-opus-5-5`, effort `high` as set by the operator's prompt. I cannot inspect the harness setting independently; the value is the one the prompt fixes.
- Finished at (UTC): 2026-11-19T05:58Z (shell clock read at 05:57:05Z while writing).
- Files read before writing this: in the bundle root, `README.md` and `PRIORS-TEMPLATE.md`. In `HistorEE_codebooks/`: `CLAUDE.md`, `CONTRIBUTING.md` (whole), `CHARACTER-CODING.md`, `EDITING-CSV.md`, `vocabularies/organizational_form_characteristic.csv` (all 33 rows, every definition in full), `vocabularies/organizational_form_type.csv` (printed to the first 700 characters of each line: 46 codes, scope notes of most rows truncated), `datasets/organizational_forms/datapackage.json` (first 20,000 characters: both resources' schemas), `datasets/organizational_forms/data.csv` (header, last three rows truncated, and by script the values only, not the notes, of `comanda`, `comanda_ad_societatem`, `commenda`, `societas_maris`; the row count, 948, and the highest `record_id`, OF-0950; a count of `source_lang`; the first five `comanda` rows' value, confidence, articulation and source_read), the matrix and character-state sections of all nine committed `views/organizational_forms--*.md` files (read as files; nothing run), `records/proposed-type-rows-comanda-2026-10-07-organizational_forms.csv` (first 1,500 characters) and the first data row of `records/proposed-rows-comanda-2026-10-07-organizational_forms.csv` (first 1,500 characters). Directory listings of `HistorEE_codebooks/`, `vocabularies/`, `datasets/`, `datasets/organizational_forms/`, `views/`, `records/`, `logbook/`. In `myfoamrepo/`: listings of `mocs/` and `notes/`, and three notes in full: `notes/Martinez Gijon on the comenda in Spanish law.md`, `notes/Archivo Historico Provincial de Sevilla - notarial protocols.md`, `notes/Source editions - Iberian Atlantic.md`. No logbook file was opened. **Directory listing of `sources/` declared:** `ls sources sources/*` returned the single file `Martinez-Gijon-1970-AHDE40-pp43-84.pdf`. Nothing in it was opened, rendered, or queried with `pdfinfo` or `pdftotext`.
- Skills loaded: `code-a-form` (anthropic-skills). `run-a-coding-batch` was not loaded.

## 1. Exposure, disclosed before any source is opened

### 1.1 Context at start

The chat began with: the system prompt; a memory snapshot (profile, preferences, and a memory-file listing whose one-line descriptions name HistorEE, the ERC application, the FHR special issue, *Porous Borders*, colleagues and students, and five claude.ai Projects by title, two of them "JapanFinHist" and one "Ergodicity economics and history"); and the descriptions of the available skills, including `code-a-form` and `run-a-coding-batch`. Nothing in that context concerned Seville companies for the Indies trade or this edition, and I said so before acting. I opened no memory file, no past chat, no claude.ai Project, no connector (Zotero, Drive, Gmail and others were offered as deferred tools and not loaded), and did not use the web. The chat is not inside a claude.ai Project (the session states that the user is outside any project). I requested access to the bundle folder only, by its exact path, without listing its parent `~/GitHub`.

Two attempts at a term sweep for leaks (`grep -rIl` for *sevill*, *gijón*, *carrera de indias* and similar, first across `HistorEE_codebooks/` and `myfoamrepo/`, then across `HistorEE_codebooks/` alone) were **refused by the permission layer** before they ran. I did not work around the refusal. The leak list in §1.4–1.5 therefore rests on the files named above, not on a sweep of the bundle, and a leak in a file I did not open would not be in it.

### 1.2 Training

What I recall, with confidence:

- Sixteenth-century Seville merchants trading to the Indies used notarial *compañías* in which partners in Seville supplied goods or money and a partner or *factor* went to the Indies (Santo Domingo, Nombre de Dios / Panama, Veracruz and Mexico, later Peru) to sell, collect and remit gold and silver back. Medium confidence on the general pattern; low on any particular clause.
- Typical terms as I remember them from the secondary literature (Otte, Lorenzo Sanz, Bernal, Pike, Lohmann Villena): a term of a few years (three to five); the travelling partner taking a share of profit (a third, a quarter, sometimes half); a prohibition on the travelling partner trading on his own account or for others; remittances "a riesgo" of the Seville partners; accounts to be rendered on return. Low-to-medium confidence; I cannot attach any of these to a specific deed.
- *Encomienda* or *comisión*: sale of another's goods for a percentage (I recall figures of the order of a few per cent, low confidence) — the commission agent bearing no loss and taking no profit share.
- Castilian law: *Partidas* V.10 on *compañía*; the 1556 *Ordenanzas* of the Seville Consulado; Tomás de Mercado's *Summa de tratos y contratos* (1569/1571) on partnerships and factors; Hevia Bolaños later. Medium confidence on existence, low on content.
- José Martínez Gijón: legal historian at Seville; author of the *comenda* studies (AHDE 1964, 1966) and, I believe, of a later book on the *compañía mercantil* in Castile up to the Bilbao ordinances of 1737 (1979). Medium confidence on the book's existence. Of the 1970 article I knew no more than the title given in the bundle's README before reading it; I do not recall its contents or the deeds it prints. Low confidence that I recall anything specific about this edition — I have no recollection of any of the ten deeds, their parties, notaries or dates.

### 1.3 The bundle

- `vocabularies/organizational_form_characteristic.csv`: 33 characteristics with their locators (`entity`, `labour-party`, `founder`, `arrangement`, `members`, `decision-maker`), the evidence rule on `CF2` (a promise to render or restore capital is a duty of performance, not evidence for `CF2`; silence on risk stays `.NR`), the clarifications of `LR3` (a share in the outcome against a fixed claim), `LR4` (dividing one venture's outcome by shares is 0), `CI1`/`CI5` (structure vs segregation), `MG2` (single-principal includes a managing agent within a mandate), `AP1` (entity creditors are third parties; a member's priority is not coded there), `AP4` (founder-locked; `.NA` without a founder).
- Views and data: the neighbouring rows `comanda` (unilateral Catalan: TS2 single-venture, CI1 none, CI5 commingled, LR6 upside-only, CF2 0, CF3 bilateral, CI3 P, MG2 single-principal), `comanda_ad_societatem` (TS2 fixed-term, LR6 symmetric, CF2 P), `commenda` (TS2 single-venture, CI2 1, CI5 commingled, LR6 upside-only, CF2 0), `societas_maris` (CF1 P, CI1 common, LR6 symmetric, CF2 0). `compagnia` (Florentine) is fixed-term with TS1=1. `asiento_averia` is the only other Spanish organizational row. No row resembling the new form exists.
- `CONTRIBUTING.md` §3 "Reading a printed primary edition" and "What each class of evidence can carry" (the class rules, the image-check rule, the quotation rule for an editor's modernised text).
- The vault notes in §1.5.

### 1.4 Leaks the operator knows of

- `CONTRIBUTING.md` §3 cites "ed. Martínez Gijón 1970, doc. 3 (APS, Oficio XV, Alonso de Cazalla, lib. 1.º de 1542, fols. 294r–295r)" and quotes the opening formula «Sepan cuantos esta carta vieren cómo». Read. It tells me one notary, one office, one year and one folio range for doc. 3, and that the deeds open with the standard formula.
- **The same paragraph also says that Martínez Gijón 1970 "prints ten Seville deeds of 1516–1550 in full".** That gives the date range of the whole appendix. I list it here because it is in the operator's known passage, though the operator's note quotes only the doc. 3 citation.
- The phrase "before the Carrera de Indias batch" in the same section: read.
- The first page of the excerpt carries the last lines of the editor's study: not seen; I have not opened the PDF.

### 1.5 Leaks you found

- `vocabularies/organizational_form_type.csv`, row `comanda`: its `key_source` cites "Martinez Gijon 1966, 386-388 and 404-405" for loss-sharing comandas, and the same author's 1974 paper. It tells me nothing about the Seville deeds, only that the author's comenda work is already in the census.
- `myfoamrepo/notes/Martinez Gijon on the comenda in Spanish law.md`: says the 1966 article (AHDE 36, 379–456) has a "section D on sixteenth-century Seville" that was **not read**; summarises his view that the comanda is a credit relation ("ex causa mutui, commandae seu depositi"); records that he finds no comanda in the Cantabrian and Atlantic sources. Bears on the author's framing, not on these deeds.
- `myfoamrepo/notes/Archivo Historico Provincial de Sevilla - notarial protocols.md`: says the Seville protocols hold "commendas and *companias*", "Genoese and Castilian *companias* and sea loans in one continuous series", and records De ruysscher's judgement (10 November 2026) that the Sevillian archives are unique in Europe for commenda material. Bears on the archive, not on these deeds.
- The README's own scoping of the form (capital partners in Seville, a travelling partner who resides and manages sale and reinvestment, a profit share; commission agency out) is the operator's, written before coding; it shapes my test in §3 and I have adopted it as the scope.
- I found nothing in what I read that names any party, date, amount, destination or clause of any of the ten deeds beyond doc. 3's archival line.

## 2. The edition as a whole, before you read it

Ten deeds chosen by a legal historian for a study of trade through intermediaries ("comercio por intermediario") will, I expect, be chosen to span the kinds of intermediary rather than to sample one: some *compañías* in which a partner travels and resides (the form), some commission or *encomienda* contracts for a percentage, perhaps a salaried factor, a power of attorney (*poder*) to a factor in the Indies, and perhaps a settlement of accounts (*finiquito*) or a dissolution. Given that the operator scoped the form before coding and chose this edition for it, I expect it to hold several instances: my central estimate is **4 of 10 assigned** (range 3–6), with 2–3 commission agencies and the rest powers, settlements or salaried factors. I expect at least one deed in which the travelling partner also contributes capital, and at least one with more than one capital partner. I expect the deeds to be dated 1516–1550 (from the leak) and the destinations to be Santo Domingo, Tierra Firme / Nombre de Dios, New Spain and, late in the range, Peru.

## 3. How you will assign a deed to the form

A deed is **assigned** when its operative clauses, not its rubric, show all of: (a) the parties constitute a partnership (they say *compañía* or *hacemos compañía*, or the operative terms are a share of profit — and of loss, if stated — rather than a fixed percentage of sales or a salary); (b) one or more parties supply the capital (money or goods) and another party is to go to the Indies, or is to reside there, and is to manage the sale of the goods and the employment or return of the proceeds; (c) it was executed before a Seville notary. The travelling party must be a party to the deed (his own or by proxy).

- **Commission** — remuneration as a percentage of sales or of returns, with no share of profit — is **not assigned** (out of scope by the operator's ruling).
- **Salaried factor**, a power of attorney alone, an agency without profit share, a sea loan or a bare deposit: **not assigned**.
- A partnership in which all partners stay in Seville and goods are consigned to an outside agent: **not assigned** (no travelling partner).
- **Partial features.** Where the travelling partner also contributes some capital, the deed is still assigned if the profit and management terms fit, and the capital asymmetry is recorded (it bears on `CF1`, `CI1`, `LR6`, `CF2`). Where the deed is a later instrument about an earlier company (an extension, a settlement, a dissolution) and its clauses recite the company's terms, it is assigned as evidence of the company only for what it recites, and flagged. Where the profit term is mixed (a percentage plus a share), it is assigned and flagged for `LR3`. Where a deed is ambiguous after reading the image, it is not assigned and the reason is stated, not resolved by the rubric.
- I will settle these conventions from the first reading of all ten before writing any instance row, and list them as rulings for the maintainer.

## 4. Per-cell expectations

Value, confidence in the prediction, and what would change it.

- `LP1`: `.NR`, high. A clause declaring the company a body, or suing in its name.
- `LP2`: `.NR`, medium. A clause holding goods in the company's name would move it; goods named as the partners' own would move it to 0.
- `LP3`: `.NR`, high. A clause on suing in the company's name.
- `AP1`: `.NR`, high. Any clause ranking company creditors against a partner's own creditors.
- `AP2`: `.NR`, high. A clause barring partners' creditors from the goods; the members' limb alone would leave it `.NR`.
- `AP3` (labour-party = the travelling partner): `.NR`, medium-high. A clause on the factor's liability to third parties for debts contracted for the company.
- `AP4`: `.NA`, high (no founder endowment).
- `TS1`: `.NR`, medium; 0 if a clause ends the company on a partner's death or settles with heirs.
- `TS2`: `fixed-term`, medium (0.65). `single-venture` if the deeds tie duration to one shipment and its return.
- `TS3`: `.NR`, low; P or 1 if the capital partners may revoke or recall the factor at will.
- `TS4`: `.NR`, high.
- `CI1`: `none` if one capital partner supplies all, `common` if several contributions (including the factor's) are merged; my guess `common`, low.
- `CI2`: `.NR`, low-medium; 1 if a clause bars withdrawal during the term.
- `CI3`: `.NR`, medium; 0 or P if the factor is forbidden to substitute another or assign his place.
- `CI4`: `.NR`, high.
- `CI5`: `segregated`, low-medium, if the factor is barred from own-account or third-party trade; `.NR` if silent.
- `LR1` (labour-party): `.NR`, medium-high.
- `LR2`: `coupled`, high.
- `LR3`: 1, high.
- `LR4`: 0, medium-high (one venture's outcome divided by shares).
- `LR5`: `.NA` if `LR4` is 0.
- `LR6`: `upside-only`, low-medium, if the capital partners bear capital loss; `symmetric` if loss is shared in proportion to profit.
- `MG1`: `contract`, high.
- `MG2`: `single-principal`, low-medium (the factor manages in the Indies within a mandate); `collective` if decisions are reserved to the partners jointly.
- `MG3`: `.NA` if `MG1` is `contract`.
- `MG4`: `private-contract`, high.
- `FP1`: `commercial-profit`, high.
- `FP2`: `.NR`, medium-high.
- `FP3`: `.NR`, medium; P if a foreign partner uses a Castilian factor to reach the Indies trade.
- `FP4`: `.NR`, medium. A notarial instrument is not a register; a clause requiring registration at the Casa de Contratación would move it.
- `CF1`: 1, medium-high; P if the factor also contributes capital in most instances.
- `CF2`: `.NR`, medium (silence on risk stays `.NR` under the evidence rule); 0 if the deeds say the goods travel at the capital partners' risk; P if loss is divided.
- `CF3`: `bilateral`, low-medium; `multilateral` if several capital partners are usual.

## 5. Row-level expectations

On the components where both are coded I expect the row to sit nearest `comanda` and `commenda` (bilateral capital-labour contract, coupled, LR3=1, LR4=0, MG1 contract, MG4 private-contract), and to separate from them on `TS2` (fixed-term against single-venture) and on `CI5` (segregated against commingled), and from `comanda_ad_societatem` and `societas_maris` on `LR6`/`CF2` if the capital partners bear the capital loss. I expect the entity and owner-shielding components (`AP1`, `AP2`, `AP3`, `LR1`, `LP1`–`LP3`) to learn nothing, all `.NR`, as on `comanda`. I expect the row to add no new value-instance in any column: a new case, not a new state.

## After writing

sha256 printed below by the shell, and the chat stops here until the maintainer confirms the commit.
