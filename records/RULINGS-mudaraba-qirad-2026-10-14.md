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

## Cell rulings

Sources, as read for coding:

- al-Sarakhsī, *al-Mabsūṭ* 22: Arabic Wikisource, revids 281306 and 281305.
- *al-Muwaṭṭaʾ*, *Kitāb al-qirāḍ*: Wikisource, revid 22122.
- *al-Mudawwana*: shamela.ws book 587, pages 1730–1765.

The three were saved by permission (MS, 2026-10-14) as untracked text files in `proposed-of/mudaraba-qirad-2026-10-14/` and read there. **H** = `mudaraba` / `mudaraba_alloc`; **M** = `qirad` / `qirad_alloc`.

### Block O1, contract core: ruled by MS 2026-10-14 (15:03 JST) as recommended

All sixteen priors held.

| char | H | M | evidence |
| --- | --- | --- | --- |
| `CF1` | 1, high, articulated | 1, high, articulated | H 18–19; M Muw 2026, *Mudawwana* 647 (stipulating the agent's own capital barred; unstipulated mixing at 641 a variant) |
| `CF2` | 0, high, articulated | 0, high, articulated | H 28 (loss stipulated on both void, loss on the capital, contract stands), 19–20 (*amāna*); M Muw 2026 and 2029 (*sharṭ al-ḍamān fī al-qirāḍ bāṭil*), *Mudawwana* 647 |
| `CF3` | bilateral, high | bilateral, high | base case one investor and one agent; two agents (H, 9 pages; *Mudawwana* 632) and two investors (H, 3 pages; *Mudawwana* 645) recorded as variants |
| `LR2` | coupled, high, articulated | coupled, high, articulated | H 22–23 (a fixed sum turns the contract into a hire; no profit, nothing); M Muw 2026 (*ṣāra ijāra*) |
| `LR3` | 1, high, articulated | 1, high, articulated | H 22; M Muw 2025; *Mudawwana* 632 (all profit to the agent) a variant |
| `LR4` | 0, medium, analyst-imposed | 0, medium, articulated | H 157–158 (a second fund mixed after profit is liability for mixing his own property; before profit, one *muḍāraba*); M *Mudawwana* 650 (barred as *khaṭar bayyin*: one fund's loss made good from the other's profit), 645 (two investors' funds mixed: `LR3`'s question under the 2026-10-12 clarification) |
| `LR5` | .NA | .NA | follows `LR4` = 0 |
| `LR6` | upside-only, high, articulated | upside-only, high, articulated | H 20, 28, 33; M Muw 2026, 2022 |

**The schools agree on all eight cells**, which is one witness on what they share (declaration 2). M changes no value on the live row; seven cells are re-pointed to Mālikī texts with articulation filled (recodings rows), and `LR5` is unchanged. Muw 2027, which bears on O2, was read here after the priors were committed.

### Block O2, term and exit: ruled by MS 2026-10-14 (15:06 JST) as recommended

All ten priors held.

| char | H | M | evidence |
| --- | --- | --- | --- |
| `TS3` | 1, medium, articulated | P, high, articulated | H: either party may dissolve at will (19; 91 *matā shāʾa*); the investor's prohibition is void once goods are bought (53), but he can compel the agent to sell, or to hand over the capital and his profit share in kind, because delay "*ḥaylūla bayna rabb al-māl wa-bayna mālihi*" (72). M: recall free while the capital is cash; barred once the agent has bought or equipped himself for a journey, even on the road; the investor cannot compel sale, the ruler holding the goods to their market season; taking them at valuation is the agent's choice (*Mudawwana* 662–663; Muw 2027) |
| `CI2` | 0, medium, articulated | 1, high, articulated | as `TS3`; M has the shape of `commenda CI2 = 1` |
| `TS2` | open, high, articulated | open, high, articulated | H: no term required (19, 150), a time limit admitted as a binding restriction (40); M: a term barred (Muw 2027; *Mudawwana* 647, a stipulated year → *qirāḍ mithl*). The difference over a term is recorded in notes. M changes from the live `single-venture` |
| `TS1` | 0, medium, articulated | P, high, articulated | H: the investor's death ends the contract as a *wakīl*'s dismissal; realisation only (53, 69, 87); the agent's death not treated in what was read. M: the agent's trustworthy heirs (or a trustworthy substitute) collect and sell on his share; the investor's heirs may continue (*Mudawwana* 663–664) |
| `TS4` | .NR | .NR | contract variation, not an entity's internal decision: H, the investor may restrict while the capital is cash (53, 68); M, the parties may vary the ratio mid-contract (*Mudawwana* 632, Ibn al-Qāsim). `comanda .NR` followed; the family is split (`isqa .NA`) |

**The pre-named test (2026-08-18) separates the schools**, on the investor's power to force liquidation, not on revocability after commencement as the vault note framed it: both schools void the investor's recall once goods are bought. The alternative coding, `TS3` P / P with the separation carried by `CI2` alone, was put to MS and not taken. `TS3` and `CI2` are WP2, so the rows part on a component characteristic.

### Block O3, creditors and entity: ruled by MS 2026-10-14 (15:08 JST) as recommended

Priors: 13 held. Changed: `AP1` on both rows (.NR → 0). Falsified: H `AP2` (0 → .NR).

| char | H | M | evidence |
| --- | --- | --- | --- |
| `AP3` | 0, medium, articulated | 0, medium, articulated | H: the agent carries the *ʿuhda*, with recourse against the investor (19, 76); it falls on the investor only where the agent cannot bear it (minor, slave: 59). M: capital lost before payment, the investor declining, the agent pays the price and the goods are his, sold against him if he has nothing (*Mudawwana* 641) |
| `LR1` | unlimited-several, medium, articulated | unlimited-several, medium, articulated | as `AP3`: the agent alone answers to the seller |
| `AP1` | 0, medium, analyst-imposed | 0, medium, analyst-imposed | H: at death creditors attach to the agent's own property "except what was a trust in his hands"; identified capital to the owner, unidentified ranks with debts (19); after mixing pro rata (143). M: deposits, *qirāḍ* and debts share pro rata (Mālik); identified capital first (Yaḥyā b. Saʿīd); the *qirāḍ* never shares (ʿAṭāʾ, al-Layth) (*Mudawwana* 664). 0 under the 2026-10-13 clarification; the investor's priority goes in the notes as a member's claim |
| `AP2` | .NR | .NR | two-limb rule: the members' half is answered (H, either party may force liquidation, 72; M, neither once goods are bought, 662) and carried by `TS3` and `CI2`; the creditors' half is unaddressed |
| `AP4` | .NA | .NA | no founder |
| `LP1` | 0, medium, analyst-imposed | 0, medium, analyst-imposed | H 19 (*aḥkām shattā min ʿuqūd mukhtalifa*: trustee, agent, partner, hireling); M the same relations between two persons. M changes from `.NR` |
| `LP2` | 0, medium, analyst-imposed | 0, medium, analyst-imposed | H 110, 122, 168 (goods the investor's; the agent's profit share co-owned once a surplus appears); M Muw 2035, *Mudawwana* 664. M re-pointed from Ramli, low → medium |
| `LP3` | 0, medium, analyst-imposed | 0, medium, analyst-imposed | H 19, 76, 89, 163; M *Mudawwana* 661. M changes from `.NR` |

**A contrast no column holds, ruled to be recorded in both rows' `AP3` notes and in the adjudications.** When the capital is lost after a purchase and before the price is paid:
- the Ḥanafī agent recovers the price from the investor, repeatedly if need be, so that the investor is exposed beyond his capital for purchases within the mandate (al-Sarakhsī 22, 76; 172–175, at 175 a recovery of 4,500);
- the Mālikī investor may pay or decline, and if he declines "nothing is owed by you": the price falls on the agent and the goods are his (*Mudawwana* 641).

This is the capital provider's owner shielding. `AP3` and `LR1` are located on the labour party (2026-08-18), so no column carries it. It is reported, not proposed as a characteristic: retrospective selection rules out repairing the vocabulary in the batch that found the gap.

### Block O4, capital: ruled by MS 2026-10-14 (15:09 JST) as recommended

Priors: 5 held. Falsified: H `CI3` and H `CI4` (0 → .NR).

| char | H | M | evidence |
| --- | --- | --- | --- |
| `CI1` | none, high | none, high | base case one investor's capital. Variants, in effect `common`: H, the agent's own money mixed in with authority (131–136) and two funds of one investor (157–158); M, the agent's own money mixed in unstipulated (*Mudawwana* 641) and two investors' funds (645) |
| `CI3` | .NR | .NR | no alienation of either party's interest in either text (0 hits); handing the capital to a second agent needs authority, without it liability (H 98–100; M 642–643), which is delegation, the first agent remaining a party |
| `CI4` | .NR | .NR | follows `CI3` |
| `CI5` | segregated, high, articulated (new cell) | commingled (`OF-0903`, stands) | H 48, 132–133, 157–158; a single purchase with both funds lawful (48, 133–134). The motivating datum (declaration 5), not a result |

M is re-pointed from Ramli to Mālikī texts on `CI3` and `CI4`, values unchanged, and on `CI1`, **which changes `.NR` → `none`** *[corrected 2026-10-14 at application: the chat put to MS said all three were unchanged; the ruled value `none` stands]*.

### Block O5, governance and frame: ruled by MS 2026-10-14 (15:11 JST) as recommended

All sixteen priors held (H `MG2` K).

| char | H | M | evidence |
| --- | --- | --- | --- |
| `MG1` | contract, high, analyst-imposed | contract, high, analyst-imposed | H 22–23; M Muw 2025 |
| `MG2` | single-principal, high, articulated | single-principal, high, articulated | H 83–84 (a stipulation that the investor work with the agent voids the contract: *takhliya* is a condition of validity); M *Mudawwana* 648 (that stipulation → a fair wage; the investor's sale of *qirāḍ* goods void unless the agent ratifies). M `OF-0907` re-pointed from al-Sarakhsī, closing the 2026-10-13 flag |
| `MG3` | .NA | .NA | `MG1` ≠ membership |
| `MG4` | private-contract, medium, analyst-imposed | private-contract, medium, analyst-imposed | H 18 (lawful "by the *sunna* and the consensus"); M Muw 2029–2030 (*sunnat al-muslimīn*). The jurists' warrant validates a contract type; `religious` refused on the `isqa` hygiene warning |
| `FP1` | commercial-profit, high, articulated | commercial-profit, high, articulated | H 18–20; M Muw 2030 |
| `FP2` | .NR | .NR | — |
| `FP3` | .NR | .NR | H 125 (capital given to a Christian agent: disliked, valid at law) and 131 (a fixed sum valid with a foreign enemy national in enemy territory, the general exception for every contract there); M *Mudawwana* 645 (disliked). In notes, not a property of the form |
| `FP4` | .NR | .NR | H *bāb al-shahāda* (185): witnesses for disputes, no register |

**Organizational side complete.** H and M separate on `TS3`, `CI2` (WP2, the pre-named test), `TS1` (WP2) and `CI5` (description; the motivating datum), and agree on every other cell. The capital provider's exposure (O3) separates them in no column.

### Blocks L1 and L2, loss allocation: ruled by MS 2026-10-14 (15:13 JST) as recommended

All 52 priors held (H `VF1` and `VF2` K).

| char | H (`mudaraba_alloc`) | M (`qirad_alloc`) | evidence |
| --- | --- | --- | --- |
| `MC1` | allocation, high | allocation, high | H 28, 33; M Muw 2026 |
| `MB3` | voluntary, high | voluntary, high | contract |
| `RB1` | capital-provider, high, articulated | capital-provider, high, articulated | H 99, 19–20; 18 (the ʿAbbās report: three named perils as limits of the mandate); M Muw 2029, *Mudawwana* 641 (highway robbery) |
| `RB2` | capital-provider, high, articulated | capital-provider, high, articulated | H 28, 33 (*waḍīʿa* on the capital); M Muw 2026. M changes analyst-imposed → articulated: both texts name trading loss apart from destruction of the capital |
| `RB3` | none, medium, analyst-imposed | none, high, articulated | H: no surety or pledge for the capital (0 hits; *rahn* at 123 is the agent pledging venture goods); M Muw 2029, 0 hits for *ḥamīl*, *kafīl*, *rahn* |
| `RB4` | 1, high, articulated | 1, high, articulated | H 99, 20; M Muw 2029 |
| `PR1` | 0, high, articulated | 0, high, articulated | H 22; M Muw 2026 |
| `PY0` | .NA | .NA | — |
| `VF1` | claimant-oath, medium, articulated | claimant-oath, medium | H 27, 51; M *Mudawwana* 661 (the agent's word as trustee), Muw 2054 (oath on the share), 2053 (corroboration needed after a prior admission). No oath stated for a loss claim in the Mālikī texts read |
| `VF2` | mixed, medium, articulated | mixed, medium | H 108 (loss-occurrence and claimant-fault); M Muw 2053, *Mudawwana* 661 (loss-occurrence and conduct-compliance) |

**L2, declined on both rows:**
- `MB1`, `MB2`: restate `MG1` and `CF3`.
- `CN1`–`CN3`: no pool.
- `HZ1`, `HZ2`: not addressed; the ʿAbbās perils are mandate limits.
- `PY1`–`PY3`: follow `PY0`.
- `LS1`, `LS2`: carried by `LR6` and `RB2` (H 20; M Muw 2022).
- `LS3`: ruling 4.
- `GV1`: restates `MG2`.
- `DR1`, `DR2`: restate `TS2` and the division (H 105; M Muw 2046–2050).

**Corroboration found in L1 reading, no ruling changed:**
- Muw 2052 gives Mālik's own rule for O2: in a dispute over selling, neither party's word governs, and men of expertise decide whether to sell or wait.
- Muw 2055 gives Mālik's own rule for the O3 contrast: money stolen before the price is paid leaves the agent owing the seller, and the investor may pay in or "be quit of the goods".

**Coding complete: 118 cells ruled.** Priors, counted at application: 108 held (`CF1` partly K on both rows), 5 K (H `CI5`, `MG2`, `VF1`, `VF2`; M `CI5`), 2 changed (`AP1` on both rows, .NR → 0), 3 falsified (H `AP2`, `CI3`, `CI4`). `TS3`'s prior values held, but the vault seed's framing was corrected (O2).
