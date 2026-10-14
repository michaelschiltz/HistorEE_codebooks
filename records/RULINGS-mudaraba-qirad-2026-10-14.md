# Rulings in the *muḍāraba*–*qirāḍ* pass (2026-10-14)

**Status: scope rulings 1–6 given by MS in chat on 2026-10-14 (14:46 JST), all six accepted as recommended in `records/NOTES-mudaraba-sarakhsi-2026-10-14.md` §6 ("Absolutely, all recommendations accepted"). Recorded here by the assistant (`claude-opus-5-5`, effort `high`). Pass slug `mudaraba-qirad-2026-10-14`; open, not blind. These rulings precede the priors (`records/PRIORS-mudaraba-qirad-2026-10-14.md`) and any reading of the sources for coding. Cell rulings will follow below, block by block, as they are given.**

## Scope rulings (before the priors)

**1. The determination of 2026-08-18 is reopened in both datasets.** `mudaraba` is coded in `organizational_forms` from al-Sarakhsī, *al-Mabsūṭ* 22 (*Kitāb al-muḍāraba*), with vols. 11 and 19 only where vol. 22 refers to them. `qirad` is re-coded from Mālikī texts: the *Muwaṭṭaʾ*, *Kitāb al-qirāḍ*, and the *Mudawwana*, *Kitāb al-qirāḍ*. Every characteristic of the vocabulary (33) is attempted on both rows. The `mudaraba` type row's 2026-08-18 text stays in place, bracketed as superseded, append-only. Grounds, as briefed:
- the determination's premise has failed on `CI5` (rulings 1–3 of 2026-10-13);
- its falsification condition (`TS3`) can now be run;
- a single row fails the split test;
- carrying Ḥanafī evidence in a Mālikī row is the hygiene error refused at ruling 3 of 2026-10-07.

The strongest objection, one institution entered twice, is answered by treating `mudaraba` and `qirad` as **one Islamic datum** in any comparative claim, as Genoa, Pisa and Catalonia are one Latin datum.

**2. The loss side follows.**
- `qirad_alloc` is re-scoped to Mālikī law: name "Qirāḍ (loss-allocation aspect)", tradition "Islamic (Maliki)". It is re-coded from the same Mālikī texts.
- A new type code, `mudaraba_alloc`, is coded from al-Sarakhsī.

**3. Type-row fields.**
- `mudaraba` tradition "Islamic" → "Islamic (Hanafi)".
- Periods: `qirad` and `qirad_alloc` "8c-9c (Malik, Sahnun)"; `mudaraba` and `mudaraba_alloc` "8c-11c (al-Shaybani to al-Sarakhsi)". A row's period claims stability across it, and one text per school cannot show more.
- All `key_source` edits are append-only and dated.

**4. Loss-side cell set.**
- Both Islamic alloc rows take the family's ten cells: `MC1`, `MB3`, `RB1`–`RB4`, `PR1`, `PY0`, `VF1`, `VF2`.
- The other sixteen are read for. One is proposed as a cell only where a text addresses it substantively, then for both Islamic rows and flagged as having no Latin comparator. The rest are listed as declined, one line each.
- `LS3` stays uncoded on the family precedent: it would restate `AP3`.

**5. Latin links.**
- No co-occurrence is declared from `mudaraba` or `mudaraba_alloc` to any Latin row.
- The existing `commenda` ↔ `qirad` and `commenda_alloc` ↔ `qirad_alloc` links stand and are flagged in both `key_source`s, since they were declared when `qirad` stood for Islamic law in general.
- Whether the Latin link should name both Islamic rows, one, or neither is a theory call for MS, outside this pass.

**6. Slug `mudaraba-qirad-2026-10-14`.** The brief keeps its draft filename `NOTES-mudaraba-sarakhsi-2026-10-14.md`; a rename waits for MS's confirmation.

**Declarations adopted with the brief** (§5 there, before any row):
- **Non-independence.** One text per school: al-Sarakhsī is one Ḥanafī witness, and the *Muwaṭṭaʾ* with the *Mudawwana* is one Mālikī witness. Agreement on the contract core is shared origin and is not corroboration. Ramli 2018 is one witness with al-Sarakhsī. The family is the Latin rows as one datum and the Islamic rows as one datum; Latin–Islamic agreement is parallelism, not convergence.
- **Selection.** `CI5`'s separation is the reason the row was opened and carries no weight as a result. `TS3` is the only separation named in advance.
- **Co-occurrence.**
  - `mudaraba` ↔ `qirad` stands (same institution under two schools' law).
  - `mudaraba` ↔ `mudaraba_alloc` is new.
  - `mudaraba_alloc` ↔ `qirad_alloc` is new.
  - All are `same-institution`, both ways.
- **Boundary.** `boundary_basis` of `mudaraba_alloc` is `contemporary-legal-form`, with confidence after coding. `qirad_alloc` keeps its own value (its boundary with `commenda_alloc`), and its `key_source` states the second boundary in prose.

None of these rulings is a version bump.
