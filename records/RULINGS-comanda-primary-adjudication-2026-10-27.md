# Rulings adjudicating the comanda primary pass (2026-10-27)

**Status: ruled by MS in chat on 2026-10-27 ("I follow your recommendations"; "go ahead"), on recommendations put by the assistant (`claude-opus-5-5`, effort `high`) and applied by the assistant the same day. Recorded here by the assistant.** Pass `comanda-primary-2026-10-27`: 43 cells of `comanda` (`organizational_forms`) and `comanda_alloc` (`loss_mitigation_forms`), coded blind from the Latin acts of Madurell Marimón & García Sanz 1973, docs 1–255. The coding was frozen and committed (`a73b140`) and applied as pending rows (`bdde89f`) before any cell was adjudicated, and the operator's withheld predictions were scored first (`5011328`; logbook 4, 2026-10-27 (ii)).

**One recommendation withdrawn before application.** The re-basing tranche as put in chat included `comanda_alloc MB3` (`voluntary`, analyst-imposed → articulated). On reading the coder's note at application, the articulation rests on the parties' notarial recognition (*concedo et recognosco tibi … me in tua comanda recepisse*), which shows that a contract exists, not that entering it was chosen. The Venetian adjudication carried exactly this question ("whether `MB3` is anything but definitional for a two-party contract", `records/RULINGS-venetian-pass-adjudication-2026-10-25.md`, tranche 2). `MB3` is therefore kept unchanged and left out of ruling 8.

## The queue as found

At `5011328`, 43 rows carried `adjudication = pending`, all of this pass: `OF-R0265`–`R0297` and `LM-R0098`–`R0107`. 34 agree with the live value and 9 disagree, all nine on blind-test cells and each a substantive value or `.NA` against a `.NR` or the reverse.

## How a change reaches `data.csv`

As in rulings 2–25 of `records/RULINGS-queue-clearance-2026-10-25.md` and the Venetian adjudication:

- **A blind value adopted as coded:** the blind row is `replaced` and no new row is made. The `data.csv` cell takes the blind row's value, confidence, articulation, `source_ref` and `source_lang`, and `coder_model`/`coder_effort` change with it. Its note opens with a `RE-CODED` line naming the row and this file, then the coder's reading, then the previous note.
- **A third value:** a new `open` row states the cell as ruled, `replaced`; the blind row is `overruled`.
- **Value unchanged, basis changed** (ruling 8): the blind row is `kept`; a new `open` row states the re-based cell, `replaced`. The `data.csv` note gains one bracketed addition naming the row, the ruling, the clause relied on and the counts. `coder_model` and `coder_effort` are unchanged, because the value is.
- **Value and basis unchanged, note only** (rulings 5, 6, 7, 9): the blind row is `kept` and the `data.csv` note gains one bracketed addition. No new row, as in rulings 14, 22 and 24 of the queue clearance.

`source_lang` moves to `la` only where the cell's value, articulation or confidence now rests on the Latin acts.

## 1. `comanda LP2` (OF-0837): `.NR` → `0`, medium, analyst-imposed

Blind row `OF-R0266` **replaced**. The acts are not silent on whose the capital is: 42 of 45 sample instances call it the investor's (*partem tibi pertinentem*, doc 6, p. 154; *comanda vestra*, doc 120, p. 250). So ruling 1 of 2026-10-07 (default law stays `.NR` on the acts' silence), which the live cell cited, does not apply. `commenda`, `societas_maris`, `qirad` and `mudaraba` are already `LP2 = 0` (analyst-imposed, medium) by later rulings, `societas_maris` by ruling 17 of `records/RULINGS-commenda-italian-recode-2026-10-12.md`; the two comanda rows were the only ones not revisited. `comanda_ad_societatem LP2` is not in scope and is not changed.

## 2. `comanda CI1` (OF-0847): `.NR` → `none`, medium, articulated

Blind row `OF-R0276` **replaced**. The `CI1` definition as narrowed on 2026-10-11 codes a single investor's capital entrusted to a single agent `none`; 42 of 45 sample instances have one investor. The live note recorded the modal state as unknown, "a gap Madurell & Garcia Sanz 1973 would fill, not a misfit". The three-of-45 multi-investor minority (docs 33, 105, 231; shares held apart in doc 14) is in the note, not the value (ruling 2 of 2026-10-07). Hancock 2025, 17 (a community of investments in shares, from the same edition at second hand) is kept in the previous note.

## 3. `comanda CI3` (OF-0849): `.NR` → `P`, low, analyst-imposed (a third value)

New row `OF-R0298` **replaced**; blind row `OF-R0278` (`1`, medium) **overruled**. `CI3`'s locator is `members`, both parties. The investor's interest is alienable: recorded cessions of an investor's rights, intimated to and accepted by the agent (doc 253, p. 376), and notes of recognition and cession (docs 213, 217), with restitution owed *et cui velis* in 8 of 45 sample instances (docs 42, 87). The agent's position is not: he may not hand the comanda to another without the investor's consent (Consolat cap. 213, already in the live note). One party's interest is alienable and the other's not, within every comanda: a structural half-presence, which is what `P` records, not variation across instances. The coder's `1` counts the investor's side only. **Low**: the cessions sit in acts the census assigns to neither row (their loss terms are abbreviated or cut; the coding notes' sensitivity check shows those acts carry the same clauses), and the order clause is a minority.

## 4. `comanda LR4` (OF-0854): `.NR` → `0`; `LR5` (OF-0855): `.NR` → `.NA`

Blind rows `OF-R0283` and `OF-R0284` **replaced**. `LR4` as clarified on 2026-10-12 (ruling 10 of `records/RULINGS-commenda-italian-recode-2026-10-12.md`) sends the division of one common venture's outcome by shares to `LR3` and codes it `0` here; the comanda placed in a *comune* divides its outcome pro rata (doc 108, p. 241), and a single comanda has one investor. `commenda LR4` moved `.NR` → `0` on that ground on 2026-10-12, and the whole commenda family is `0`; the live comanda cell still cited the superseded reasoning. `LR5` is `.NA` wherever `LR4` is `0` (definition; `check_dependence.py`).

## 5. `comanda TS1` (OF-0843): `.NR` stands

Blind row `OF-R0272` (`0`, medium, analyst-imposed) **kept**; note addition. What happens on a party's death is default law (ruling 1 of 2026-10-07), and the acts cut both ways: the investor's claim passes to his heirs, and *Risicum dictorum heredum* (doc 199, p. 323) can be read as the venture continuing at the heirs' risk, which is persistence, not an end; the agent's death winds the venture up (doc 97, p. 227, an act not assigned to this row). The coder's `0` rests on structure (doc 18: the venture ends on return and account). The *Costums de la mar* and *Costums de Tortosa* chapters are the read that would settle it.

## 6. `comanda FP4` (OF-0864): `.NR` stands

Blind row `OF-R0293` (`P`, low, analyst-imposed) **kept**; note addition. The live note already weighed the notaries' comanda books (Polonio 2014) and held that constitution by a public instrument is not registration legible to political authority. The coder's evidence (the notary's royal authority, doc 87; cancellation in the protocol, doc 60) is the same point, and the coder named `.NR` as the alternative. The family is `.NR` except `isqa` (`P`, low, a communal court).

## 7. `comanda_alloc VF1` (LM-0749) and `VF2` (LM-0750): live values stand

Blind rows `LM-R0106` and `LM-R0107` (`.NR`) **kept**; note additions. Ruling 4 of 2026-10-07: `VF1`/`VF2` are coded from the normative or judicial layer, and the acts' silence gives `.NR` only where nothing else is held. The live values rest on the Consolat (cap. 279 for the claimant's oath, caps. 209, 213, 220 for the object). One source's silence does not override another's statement (Venetian adjudication, tranche 4). The addition records that no comanda act among the 255 says how a loss is established; the credence clauses (docs 142, 154, 157, 158, 163) concern the investor's recovery costs.

## 8. The 34 agreeing rows: `kept`; fifteen cells re-based on the Barcelona acts

All 34 agreeing blind rows **kept**. Values unchanged. Following Venetian tranches 1–3, each cell below adds the Barcelona acts to its `source_ref` and its note, in a new `open` row `replaced`:

| cell           | record  | new row    | before                                    | after                                   |
|----------------|---------|------------|-------------------------------------------|-----------------------------------------|
| `TS2`          | OF-0844 | `OF-R0299` | single-venture high articulated `ca`      | evidence added                          |
| `LR2`          | OF-0852 | `OF-R0300` | coupled medium analyst-imposed `en`       | medium articulated `la`                 |
| `LR3`          | OF-0853 | `OF-R0301` | 1 high articulated `en`                   | evidence added                          |
| `MG1`          | OF-0857 | `OF-R0302` | contract high analyst-imposed `ca`        | high articulated `la`                   |
| `MG4`          | OF-0860 | `OF-R0303` | private-contract medium analyst-imposed `es` | high articulated `la`                |
| `FP1`          | OF-0861 | `OF-R0304` | commercial-profit high articulated `es`   | evidence added                          |
| `CF1`          | OF-0865 | `OF-R0305` | 1 high articulated `ca`                   | evidence added                          |
| `CF2`          | OF-0866 | `OF-R0306` | 0 high articulated `ca`                   | evidence added (not blind)              |
| `CF3`          | OF-0867 | `OF-R0307` | bilateral medium analyst-imposed `en`     | medium articulated `la`                 |
| `CI5`          | OF-0900 | `OF-R0308` | commingled low articulated `ca`           | high articulated `la`                   |
| `MC1`          | LM-0741 | `LM-R0108` | allocation high analyst-imposed `ca`      | high articulated `la` (not blind)       |
| `RB1`          | LM-0743 | `LM-R0109` | capital-provider high articulated `ca`    | evidence added (not blind)              |
| `RB3`          | LM-0745 | `LM-R0110` | general-estate medium articulated `es`    | high articulated `la`                   |
| `RB4`          | LM-0746 | `LM-R0111` | 1 high articulated `ca`                   | evidence added (not blind)              |
| `PR1`          | LM-0747 | `LM-R0112` | 0 high analyst-imposed `en`               | medium articulated `la`                 |

- **Articulated** where the Latin states the value in terms. **Confidence up** for `CI5` (23 of 45 instances commingle in terms, none segregates; a directed search found no segregation clause), `MG4` and `RB3`. **`CF3` stays medium**: three multi-investor acts are a recorded minority (ruling 2 of 2026-10-07). **`PR1` goes to medium**: a late comanda carries insurance bought by a separate contract, its premium deducted from profit (doc 250, p. 372), recorded as spreading layered on the comanda.
- **`RB3`**: the late notules' *obligo me personaliter et bona* add execution against the person to the general obligation of goods; no value in the set expresses that, and `mixed` is property with a surety. Recorded in the note; the value stays `general-estate`.
- **Not re-based**: `LR6`, `MG2` and `RB2`, which the coder could only impose by analysis from the acts where the Consolat states them; `MB3` (see the withdrawal above); and the `.NR` and `.NA` agreements, which the acts leave as they were (`TS3`, `CI2` take ruling 9).
- `CF2`, `MC1`, `RB1` and `RB4` are not blind tests (the type names and the assignment rule fix them) and take no weight on that account; the evidence is added because the acts state it.

## 9. `comanda TS3` (OF-0845) and `CI2` (OF-0848): `.NR` stands; sub-types recorded, no split

Blind rows `OF-R0274` and `OF-R0277` **kept**; note additions. The row aggregates three sub-types that answer differently: the voyage comanda (silent on recall), the open-trade comanda (recallable at the investor's will, doc 91 and docs 107, 110, 113, 220), and the comanda placed in an agent's *comune* (locked to the account, doc 108; docs 87, 90). No split, as Venetian ruling 1 declined one; the question reopens if the normative chapters rule differently by sub-type. The coder's observation that `TS3` and `CI2` rest here on the same clauses is recorded and no dependence is declared.

## 10. Carried, no change

- **`PY0` applicability.** The coder's proposal (applicable only where `MC1 = pooling`) is **not adopted**: it would make four existing cells violate the rule (`avariz_vakfi_kirkcesme`, `MC1 = allocation`, `PY0 = individual-indemnity`; `monte_doti_florence`, spreading, `individual-draw`; `warichi_iwade`, `MC1 = .NR`, `individual-draw`; `shenhui_gu_alloc`, `MC1 = .NR`, `collective-good`). The recommendation as put in chat said three; the count over the column is four. `comanda_alloc PY0 = .NA` stands on judgment, as on eight other allocation forms.
- **Doc 255.** Read by the operator as insurance and by the coder as carriage at the carrier's whole risk. No cell rests on it (it is context in the `VF1` note); both readings stand.
- **The pass's logbook 4 heading** gains the `— ai —` marker.

## Rows

- `kept` (38): the 34 agreeing rows, and `OF-R0272` (`TS1`), `OF-R0293` (`FP4`), `LM-R0106` (`VF1`), `LM-R0107` (`VF2`).
- `replaced` (4 blind): `OF-R0266` (`LP2`), `OF-R0276` (`CI1`), `OF-R0283` (`LR4`), `OF-R0284` (`LR5`).
- `overruled` (1): `OF-R0278` (`CI3`).
- New `open` rows, `replaced` (16): `OF-R0298`–`R0308`, `LM-R0108`–`R0112`.
- Pending after application: 0 in both packages.
