# Rulings in the Italian commenda re-code (2026-10-12)

**Status: ruled by MS in chat on 2026-10-12, item by item, each on a recommendation put by the assistant (`claude-opus-5-5`, effort `high`) and accepted as proposed. Recorded here by the assistant. Pass slug `commenda-italian-recode-2026-10-12`; open, not blind. The worksheet is `proposed-of/ADJUDICATION-commenda-pilot-2026-09-28.md`.**

Sources read first-hand for these rulings: Besta & Predelli, "Gli statuti civili di Venezia anteriori al 1242", *Nuovo archivio veneto* n.s. 1 (1901), preface 47–48 and statutes 221–223, 273, 281, from page images (Zotero `AYNZLYBP`, OCR copy `GIP29ID7`); González de Lara 2011, "Litigation Plus Regulation", 101–122 (`P7T4459J`); Held 2025, 20–23 (`L83IPLNP`); Pryor 1981, section II "Account (Rendering of)", unnumbered page between 95 and 97 (`CQ4IPQ5Q`).

## 1. Scope of `commenda_alloc`

`commenda_alloc` codes the law and practice of the Italian maritime cities: Venice, Genoa, Pisa. Evidence from Dubrovnik (Held 2025) and Marseille (Amalric; Pryor) may corroborate a cell or record a variant in its notes and may not be a cell's sole basis. The 2026-08-18 decision filing the Ragusan *collegantia* under this row stands for the allocation cells. `MB3` and `RB4` cite Held alone and are listed for re-pointing, values unchanged.

## 2. Worksheet entry 16 — `commenda_alloc VF1`

`documentary` → `official-adjudication`, medium, articulated, `la` (`LM-0535`; new recoding `LM-R0061`, replaced). Venice proves a peril loss by lawful witnesses, confirmed by the debtor's oath, rebuttable by the creditor's witnesses and weighed by the judges (Dandolo c. 32 with the Querinian gloss to St. Nov. III, 2; Tiepolo 1229 c. 16, excepting shipwreck and robbery from the account oath; Tiepolo 1233 c. 2, notoriety). *Clarefactum* and *si manifestum fuerit* are a standard, not a mode. The witness clause of c. 32 is an editorial restoration (om. MS M).

## 3. Adjudication state `overruled`

Added to `adjudication` in both recodings schemas: neither this value nor the existing one stands, because a third value was written. `loss_mitigation_forms` 0.9.0 → 0.10.0; `organizational_forms` 0.12.0 → 0.13.0. Entry 16 rows: `LM-R0009` replaced; `LM-R0028`, `LM-R0047` overruled.

## 4. Worksheet entry 20 — `commenda_alloc VF2`

Live `mixed` stands, basis moved from Held to the Venetian statutes: loss-occurrence (Dandolo c. 32 and the gloss; Tiepolo 1233 c. 2) and conduct-compliance (cc. 30–31). Medium, articulated, `la` (`LM-0536`; new recoding `LM-R0062`, replaced). Fault is attested only in Genoese acts (Cassinese 201) and recorded in notes. `LM-R0010`, `LM-R0029`, `LM-R0048` kept.

## 5. Worksheet entries 9 and 13 — `commenda` and `societas_maris` `AP1`

Acquired and read from page images: the Breve of the consuls of the *placita* of Genoa (the Datta fragment), *Atti della Società ligure di storia patria* I (1862), 81–84, dated 1207–1217 by Desimoni (99); *Statuti della colonia genovese di Pera*, ed. Promis (1871), c. CCXI, 739–740; Bonaini, *Statuti inediti della città di Pisa* II (1870), 839 and 885. Live `P` stands on both rows, basis replaced (`OF-0553`, `OF-0563`; new recodings `OF-R0197`, `OF-R0198`, replaced; the six pilot rows kept): in Genoa the *accomendator* or *socius* is preferred to all other creditors and the wife in the movables traced to the money, and shares equally with creditors in later-acquired immovables; an unpaid seller ranks first. `medium`, `articulated`, `la`. Harris 2007, 11 (via Hansmann, Kraakman & Squire 2006) is contradicted on the traveller's half. Pisa's 1248 revision of the *Constitutum usus* and Venice's silence are recorded as comparison. Licensed by MS in the same ruling: `comanda AP1` (`OF-0839`) note corrected in place where it repeated Martínez Gijón's claim that Genoa reached the rule only in its 1490/1588 printing.

## Flagged, not ruled

`comanda_alloc VF1` rests on *Consolat* cap. 279, an accounting rule; Venice shows the account oath and the proof of a peril loss as separate rules. Until caps. 209–210 and 220 are read for a peril-specific rule, the family's separation on `VF1` may not be like for like.
