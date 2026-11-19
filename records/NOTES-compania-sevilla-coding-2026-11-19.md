# Coding notes — compania-sevilla-2026-11-19 (first coding of `compania_factoria_sevilla`)

- Coded by: `claude-opus-5-5`, effort `high` (as set by the operator's prompt; not independently verifiable from inside the chat).
- Bundle: `~/GitHub/_blind-compania-sevilla-2026-11-19`; only that folder was opened. Nothing outside `proposed-of/` was written in it. Checks ran on a scratch copy at `~/scratch-check/repo` on the same machine, outside the bundle.
- Priors: `proposed-of/PRIORS-compania-sevilla-2026-11-19.md`, sha256 `e384ba4319a9cb79deb4f9494e6928479086bfef46f433e5395ca42e43d53880`, committed by the maintainer before the source was opened (confirmed in chat at 15:03 JST, 2026-11-19). Its ledger entry is the maintainer's to name here: `entries/2026/<file>.txt` — not visible from the bundle.
- Source: Martínez Gijón 1970, *AHDE* 40, Apéndice documental, printed pp. 43–83; file `sources/Martinez-Gijon-1970-AHDE40-pp43-84.pdf`, sha256 `ed0864f6542113cd74d430fb9d897892fbe0fdbe8234750d01c0174cfc5a4288`, 41 pages, layer by OCRmyPDF 16.13.0 / Tesseract 4.1.1. Offset verified on every page: printed = PDF + 42.
- Deliverables: `INSTANCES-compania-sevilla-2026-11-19.csv` (10 rows), `proposed-rows-compania-sevilla-2026-11-19-organizational_forms.csv` (33 rows, placeholder IDs `OF-XXXX-01`…`33` per the maintainer's ruling of 15:03), `proposed-type-rows-compania-sevilla-2026-11-19-organizational_forms.csv`, this file, `LOGBOOK-DRAFT-compania-sevilla-2026-11-19.md`, `COMMIT-MSG-compania-sevilla-2026-11-19.txt`.

## Reading conventions applied (not ruled by the maintainer; put to him here)

1. **Assignment from the operative clauses, never the rubric.** The rubrics are the editor's small capitals. Doc 7's «COMPAÑÍA» is a salaried factor; doc 9's «FACTORÍA» is a compañía in its own words.
2. **A traveller who also contributes capital is still assigned**, as the priors §3 fixed before reading (doc 2: half; doc 3: 80 of 3,080 ducados). The asymmetry is recorded, not used to exclude.
3. **A later instrument that recites a company is not an instance.** Doc 10 is marked `recital` and used only as corroboration in a note (TS1).
4. **Heterogeneity across instances is coded by ruling 2 of 2026-10-07**: the modal state, with counts in the note and lowered confidence; a split is proposed, not a `P`. **Where the four deeds tie 2:2 there is no mode, and the cell is `.NR` with the tie stated.** That is a use of `.NR` for "answered, but no single value", which the token set does not distinguish; see (5).
5. **Formulary absence** (ruling 1 of 2026-10-07) was not needed: no cell is coded `0` for a clause one notary writes elsewhere and omits here.
6. **Image reading.** Every one of the 41 page images was read against the text layer, not only the pages a quotation or absence rests on. Every quotation in the cells and the instance file was taken from the image.

## Instances

| doc | date       | notary     | rubric         | assigned | why                                                   |
|-----|------------|------------|----------------|----------|-------------------------------------------------------|
| 1   | 1538-04-15 | Cazalla    | PODER          | no       | power of attorney to collect                          |
| 2   | 1516-01-24 | Vallecillo | COMPAÑÍA       | yes      | resident traveller, half the capital, halves; flagged |
| 3   | 1542-03-03 | Cazalla    | COMPAÑÍA HECHA | yes      | factor y compañero, 3,000 ducados v. 80, 3/4-1/4      |
| 4   | 1524-03-11 | Vallecillo | OBLIGACIÓN     | no       | commission, 5 % of sales                              |
| 5   | 1518-08-27 | Vallecillo | OBLIGACIÓN     | no       | commission, 6 %; owners take their own proceeds       |
| 6   | 1516-03-22 | Vallecillo | PACTO          | no       | salaried factor                                       |
| 7   | 1519-02-07 | Vallecillo | COMPAÑÍA       | no       | salaried factor; rubric not borne out                 |
| 8   | 1550-01-13 | Cazalla    | COMPAÑÍA       | yes      | three capital partners, factor puts nothing, 3/4-1/4  |
| 9   | 1542-01-25 | Cazalla    | FACTORÍA       | yes      | two brothers, factor puts nothing, 3/4-1/4            |
| 10  | 1549-08-16 | Cazalla    | —              | recital  | power reciting a company; corroboration only          |

Four assigned instances, which are not independent. Three are Alonso de Cazalla's (docs 3, 8, 9); two of those are in one book of 1542, five weeks apart. Doc 8 and doc 10 are one firm: Jorge and the two Pérez, whose «compañero» at Nombre de Dios in doc 8 (p. 71) is doc 10's factor. Doc 2 is the only Vallecillo instance and the only one from the 1510s.

## (1) What was coded, and on what evidence

Thirty-three cells: **13 substantive, 17 `.NR`, 3 `.NA`.** Every cell rests on the four assigned deeds (docs 2, 3, 8, 9), read in full from the page images, `source_class` primary-transactional, `source_lang` `es`, quoted in the editor's modernised text with deed and printed page. The substantive cells:

- `TS2=fixed-term` (high): terms of 2, 6, 4 and 4 years, extendable.
- `CI1=common` (high): several contributions merged in one stock in all four.
- `LR2=coupled` and `LR3=1` (high): the factor's reward is a quarter or a half of profit.
- `LR4=0` (high): one venture divided by shares; commissions sent into the stock are excluded by the 2026-10-12 clarification.
- `MG1=contract`, `MG4=private-contract`, `FP1=commercial-profit` (high).
- `TS3=P` (medium): revocable at the capital side's will, not the factor's.
- `CI5=segregated` (medium): exclusivity and separate account for goods on another's account; with a caution.
- `TS1=P` (low): doc 8 alone; survives a capital partner's death, liquidates on the factor's.
- `CI2=P` (low): one datum with `TS3`.
- `LP2=0` (low): title in the partners' names; against it, doc 8's «pertenecer a esta dicha compañía».
- `LR6=symmetric` (low) and `CF2=0` (low): modal states, 3:1 each, on ruling 2.

Per-component coverage:

| component (work package)   | characteristics             | substantive | values                                      |
|----------------------------|-----------------------------|-------------|---------------------------------------------|
| legal-personality (WP2)    | LP1 LP2 LP3                 | 1 of 3      | LP2=0                                       |
| entity-shielding (WP2)     | AP1 AP2 AP4                 | 0 of 3      | AP4=.NA                                     |
| capital-lock-in (WP2)      | CI2                         | 1 of 1      | CI2=P                                       |
| transferable-claims (WP2)  | CI3 CI4                     | 0 of 2      | —                                           |
| perpetual-succession (WP2) | TS1 TS2 TS3 TS4             | 3 of 4      | TS1=P, TS2=fixed-term, TS3=P                |
| owner-shielding (WP1)      | AP3 LR1                     | 0 of 2      | —                                           |
| outcome-coupling (WP1)     | LR2 LR6                     | 2 of 2      | LR2=coupled, LR6=symmetric (modal 3:1, low) |
| loss-sharing (WP1)         | CF2 LR3                     | 2 of 2      | CF2=0 (modal 3:1, low), LR3=1               |
| risk-pooling (WP1)         | LR4 LR5                     | 1 of 2      | LR4=0, LR5=.NA                              |
| none (description)         | CI1 CI5 MG1-4 FP1-4 CF1 CF3 | 5 of 12     | CI1, CI5, MG1, MG4, FP1                     |

**What the row adds to the matrix, computed only after every cell above was fixed in the fragment:** no new value-instance in any column. Every substantive value already occurs elsewhere: `CI5=segregated` has its second instance (with `mudaraba`), `TS1=P` its third (with `qirad`, `deed_of_settlement_company`). Against the neighbours, the row separates from `comanda` and `commenda` on `TS2` (fixed-term against single-venture), `CI1` (common against none), `CI5` (segregated against commingled) and `LR6` (symmetric against upside-only). From `comanda_ad_societatem` it separates on `CF2` (0 against P) only, where both are coded. On the WP2 entity-shielding and WP1 owner-shielding components it learns nothing, which is the finding there. **A new case, not a new state.**

**Ordering, declared.** While checking the format of `.NR` and `.NA` rows in `data.csv`, a script printed, beside those rows, the census counts of values for `CI1`, `CI2`, `CI5`, `LP2`, `TS1`, `TS3`. That was after every value had been decided and before the fragment was written. No value was changed after it, but that rests on my statement, not on a commit. All comparisons in the paragraph above were computed after the fragment was written.

## (2) What could not be coded, and why

Every `.NR` and `.NA` below rests on the four assigned deeds. **The page image was read for every page of each deed, and for every page of the edition**, so no absence is an absence of the text layer.

- **Silent (11):** `LP1`, `LP3`, `AP1`, `AP2`, `AP3`, `CI3`, `CI4`, `LR1`, `FP2`, `FP3`, `FP4`. Images read: pp. 45–51, 66–81 (and all others).
  - `LP1`, `LP3`, `AP1`, `AP3`, `LR1` ask default law about outsiders (creditors, standing), which the deeds do not address (ruling 1 of 2026-10-07).
  - `AP2`: the members' limb is answered (capital side may end at will; heirs barred), the creditor limb is not.
  - `CI3`, `CI4`: no clause on assigning an interest.
  - `FP2`, `FP3`: nothing.
  - `FP4`: the register records shipments in partners' names, not the company; whether a company register existed is normative.
- **Vocabulary does not fit (2):** `TS4` (variation by consent of all parties is not an entity's self-alteration), `MG2` (control divided by place, in terms, between a Seville administrator and a factor in the Indies).
- **Answered, but tied 2:2 across instances (2):** `CF1` (docs 8, 9 = 1; docs 2, 3 = P), `CF3` (docs 2, 3 bilateral; docs 8, 9 multilateral).
- **Inapplicable (3):** `AP4` (no founder), `LR5` (LR4 = 0), `MG3` (MG1 is contract).

## (3) Which of my own priors were falsified

Quoted verbatim from `PRIORS-compania-sevilla-2026-11-19.md` §2, §4 and §5.

| prior (verbatim from the priors file)                                                                                                                                | result                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `LP2`: `.NR`, medium. A clause holding goods in the company's name would move it; goods named as the partners' own would move it to 0.                               | FALSIFIED on the value; the condition it named is what fired (doc 8, p. 69). Coded 0, low.                             |
| `TS1`: `.NR`, medium; 0 if a clause ends the company on a partner's death or settles with heirs.                                                                     | FALSIFIED: doc 8 provides for both deaths, with opposite outcomes; P.                                                  |
| `TS3`: `.NR`, low; P or 1 if the capital partners may revoke or recall the factor at will.                                                                           | FALSIFIED on the value; the named condition fired in three deeds; P.                                                   |
| `CI2`: `.NR`, low-medium; 1 if a clause bars withdrawal during the term.                                                                                             | FALSIFIED: P (locked against heirs and factor, unlocked at the capital side's will).                                   |
| `LR6`: `upside-only`, low-medium, if the capital partners bear capital loss; `symmetric` if loss is shared in proportion to profit.                                  | FALSIFIED: modal symmetric (3:1); upside-only only in doc 9.                                                           |
| `MG2`: `single-principal`, low-medium (the factor manages in the Indies within a mandate); `collective` if decisions are reserved to the partners jointly.           | FALSIFIED: neither; control divided by place in terms; .NR, vocabulary misfit.                                         |
| `CF1`: 1, medium-high; P if the factor also contributes capital in most instances.                                                                                   | FALSIFIED: tied 2:2; .NR.                                                                                              |
| `CF2`: `.NR`, medium (silence on risk stays `.NR` under the evidence rule); 0 if the deeds say the goods travel at the capital partners' risk; P if loss is divided. | FALSIFIED: the deeds are not silent; all four state the loss rule; modal 0 (3:1), doc 8 = P.                           |
| `CF3`: `bilateral`, low-medium; `multilateral` if several capital partners are usual.                                                                                | FALSIFIED: tied 2:2; .NR.                                                                                              |
| I expect the destinations to be Santo Domingo, Tierra Firme / Nombre de Dios, New Spain and, late in the range, Peru.                                                | PARTLY FALSIFIED: no New Spain; Cuba appears (docs 1, 7), in deeds not assigned.                                       |
| from `comanda_ad_societatem` and `societas_maris` on `LR6`/`CF2` if the capital partners bear the capital loss.                                                      | FALSIFIED: modal LR6=symmetric and CF2=0 equal societas_maris; the row differs from comanda_ad_societatem on CF2 only. |
| I expect the entity and owner-shielding components (`AP1`, `AP2`, `AP3`, `LR1`, `LP1`–`LP3`) to learn nothing, all `.NR`, as on `comanda`.                           | FALSIFIED IN ONE CELL: LP2=0 (as on comanda); the rest held.                                                           |

Held: «`TS2`: `fixed-term`, medium (0.65).»; «`CI1`: ... my guess `common`, low.»; «`CI5`: `segregated`, low-medium, if the factor is barred from own-account or third-party trade.»; «my central estimate is **4 of 10 assigned** (range 3–6)»; «I expect the row to add no new value-instance in any column: a new case, not a new state.». The §1.2 recollections that the travelling partner was barred from trade on his own account or for others, that remittances went at the Seville partners' risk, and that commission ran at a few per cent all held in the deeds (4 %, 5 %, 6 %). The recollection of «a term of a few years (three to five)» held only roughly (2 to 6).

## (4) Characteristics that did not fit the evidence

- **The contractual-form cells do not fit a form that varies by deed.** The scoped form is heterogeneous across its four instances, and no single split resolves it:

| cell | doc 2     | doc 3      | doc 8        | doc 9        | coded                |
|------|-----------|------------|--------------|--------------|----------------------|
| CF1  | P         | P          | 1            | 1            | .NR (2:2)            |
| CF3  | bilateral | bilateral  | multilateral | multilateral | .NR (2:2)            |
| CF2  | 0         | 0          | P            | 0            | 0 (3:1, low)         |
| LR6  | symmetric | symmetric* | symmetric    | upside-only  | symmetric (3:1, low) |

`*` doc 3's factor bears loss only on his 80 ducados against a quarter of all profit; symmetric on the `societas_maris` precedent, upside-only on a stricter reading, which would make LR6 2:2.

Splitting on CF1 ({2, 3} against {8, 9}) also resolves CF3, but leaves {8, 9} split on CF2 and LR6, so doc 8 and doc 9 disagree on the loss rule. Splitting on the loss rule, the `comanda`/`comanda_ad_societatem` precedent ({8} against {2, 3, 9}), leaves CF1 and CF3 heterogeneous. Either split yields a singleton row. **Recommendation: do not split on four deeds; code the scoped form as above and acquire.** The split question is the maintainer's.
- `TS4` and `MG2`: entity-shaped questions put to a contract (above).
- `CI5`: for a factor who by covenant holds no other capital, "segregated" and "commingling foreclosed" are different states that the value set reads as one. A possible well-formedness defect (test 1), flagged and **not** repaired.
- `LP2`: the deeds speak of goods «pertenecer a esta dicha compañía» while registering title in the partners' names. The column asks about capacity; the deeds talk allocation and title. Coded 0 at low confidence, with the alternative `.NR` stated.

## (5) Dependence and well-formedness problems noticed and not repaired

1. **No `source_class` column in `data.csv`.** Carried at the head of every note, as ruled at 15:03.
2. **`.NR` is doing two jobs** in `CF1` and `CF3`: "not recorded" and "recorded, tied across instances". The token set cannot tell them apart; only the note can. Ruling 2's mode is also fragile at n = 4: one reading of doc 3 flips `LR6` from 3:1 to 2:2.
3. **One datum, two cells:** `TS3` and `CI2` both rest on the recall/termination clauses (docs 3, 8, 9). The capital-immobility group (`AP2`, `CI2`) is collinear on this row by construction, and `AP2` is `.NR`.
4. **`CF1=.NR` beside a coded `CF2`.** `CF2`, `AP3` and `LR1` take the labour-party locator from CF1 being present. CF1 is present (1 or P) in every instance; the `.NR` is a tie, not an absence. `check_dependence.py` does not flag it, and should not.
5. **Within-form evidence on `agent-loss-exposure` that the matrix cannot hold.** At instance level CF2 does not determine LR6: doc 3 is CF2 0 with LR6 symmetric, doc 9 is 0 with upside-only, doc 8 is P with symmetric. That bears on the group's dependence hypothesis but comes from deeds within one row, not from forms, so `check_dependence.py` cannot see it. Recorded here only.
6. **Instance non-independence:** three of four instances are one notary; docs 8 and 10 are one firm. No similarity claim may count the four as four witnesses.
7. **Asymmetric treatment of two similar drafting facts:** `LP2=0` (an ownership declaration) against `LP3=.NR` (an instruction on drafting instruments). The distinction is stated in both notes; the maintainer may prefer `.NR` for both.
8. **The edition's own inconsistencies**, recorded in the instance file and not resolved: doc 2's printed signatures («Juan Hernández» for the traveller); doc 4's penalty (cien mil / cincuenta mil); doc 5's shares not summing to the total; doc 9's heading printed without folios; doc 10's «fol. 450 v°» for 405 v°; doc 8's «Alonso Díaz de Herrera» / «de Llerena».
9. **Application prerequisites not in my remit:** `references/works.csv` has no row for Martínez Gijón 1970, so `check_citations.py` will fail until one is added. The instance file must be registered in `check_counts.py`'s scope if it goes to `records/`.
10. **Leak sweep incomplete:** two `grep` term sweeps of the bundle were refused by the permission layer (priors §1.1). The leak list rests on files opened.

## (6) What to acquire next, and which cell it would move

- **More printed deeds of the form**, full text, from the same and other Seville notaries, and ideally from Cazalla's 1542 book. Moves `CF1` and `CF3` off the tie; tests whether doc 8's loss clause (`CF2=P`) or doc 9's (`LR6=upside-only`) is a drafting variant or noise; firms up `TS1` (death clauses) and `CI2`. A regest or catalogue (the printed *Catálogo de los fondos americanos del Archivo de Protocolos de Sevilla*) would show only that such companies existed; it carries no clause cell.
- **The editor's study, pp. 5–42** (withheld). It is secondary, so it can carry present values only, never a coded absence. It would say how the ten deeds were chosen, which is what governs the weight of the 2:2 ties, and may quote clauses on a factor's debts (`AP3`, `LR1`).
- **Martínez Gijón 1966, section D (sixteenth-century Seville)**, unread per the vault. Same author: one witness with 1970, not two.
- **The normative layer**: the 1556 *Ordenanzas* of the Seville Consulado, Mercado's *Summa* (1569/1571), Hevia Bolaños's *Labyrintho de comercio* (1617). These are primary-normative and are entered with the conflict rule; they could move `AP1`, `AP3`, `LR1`, `LP3`, and `FP4` if they impose any registration of companies.
- **Litigation**: Casa de la Contratación or Consulado suits on a factor's debts (AGI, Justicia / Contratación). The only evidence that would move `AP1` and `AP3` from the practice side.

## Freeze

This file and the five others in `proposed-of/` were complete at writing; nothing in `proposed-of/` is changed after the freeze is declared in chat.
