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

## 6. Worksheet entry 24 and the `CI1` split — `CI1` and `CI5`

`commenda CI1` `common` → `none`, medium, analyst-imposed (`OF-0556`; `OF-R0199` replaced; `OF-R0093` replaced; `OF-R0135`, `OF-R0177` overruled): the modal commenda carries one investor's capital (van Doosselaere 2009, 70 n. 11; arm P's two-party counts). New cells: `commenda CI5 = commingled`, low, articulated (`OF-0902`; Genoese acts, segregation an express clause; Pisa, *Constitutum usus*, Bonaini II, 885); `qirad CI5 = segregated`, medium, articulated (`OF-0903`; al-Sarakhsī, *al-Mabsūṭ* 22, 48); `societas_maris CI5 = .NR` (`OF-0904`; 2 against 2). `societas_maris CI1 = common` and `qirad CI1 = .NR` re-read and stand. The hypothesis of ruling 6 of 2026-10-11 (commingling linked to `LR4`) is tested and reported in logbook 4, not encoded. Flag: for principal–agent forms `CI1 = none` nearly follows from `CF3 = bilateral`.

## 7. `MG2` for `commenda`, `societas_maris` and `qirad`

Three new cells, all `single-principal`, medium, articulated (`OF-0905`, `OF-0906`, `OF-0907`): the traveller, the travelling partner and the *muḍārib* hold residual control as managing agents within a mandate, under the definition clarified on 2026-10-11 (ruling 3). Read from page images or first-hand: *Il cartolare di Giovanni Scriba* I, nos. LXVIII–LXIX (p. 37; *exinde quo voluero*; and the ship's majority on route, *si maior pars hominum de navi … concordati fuerunt ire Alexandria, ibo*); González de Lara 2011, 111 (Venice); al-Sarakhsī, *al-Mabsūṭ* 22, 41 and 48. The ship's company's decisions on route are recorded in notes, not as `collective`, because the company is not a party to the arrangement. Objection put and answered: `MG2` now separates none of the principal–agent forms; ruling 3 accepted that.

## 8. D1 — the `LR3` definition (worksheet entries 3 and 6)

`LR3` is clarified on existing usage, value names kept: the test is a share in the outcome against a fixed claim; "proportionally to stake" is a gloss in which labour counts as a stake, so a negotiated ratio that does not follow capital is `1`; `P` is reserved for an arrangement partly fixed and partly shared. Ground: all 16 forms with a labour partner (`CF1` = `1` or `P`) carried `LR3 = 1`; reading the ratio's departure from capital as `P` would duplicate `CF1`. Live `commenda LR3 = 1` and `societas_maris LR3 = 1` stand; `OF-R0069`, `R0111`, `R0153`, `R0080`, `R0122`, `R0164` kept. No version bump: a definition, not a declared constraint.

## 9. D2 — a promise to render the capital is not an assumption of peril (`CF2`)

An evidence rule is added to `CF2`'s definition: a promise to render, restore or bring back the capital, with or without a term or penalty, is a duty of performance and not by itself evidence for `CF2`; `1` or `P` requires that the act or the law place the loss of the principal's capital on the working party in terms, or keep the obligation alive on total loss. Read first-hand: Amalric 429 (Blancard II, 35–36; page images), where "et tuum resegum et meum" and "totum capitale … reducere" stand in one act; Scriba CCCLV (1158, 185; "capitale tuum super me salvum erit"), an explicit assumption; Scriba DCLXXIV (1160, 364), a father's guarantee, recorded as not the working party's exposure. Worksheet entry 18 is ruled after D4.

## 10. D3 — what `LR4` counts

`LR4` is clarified on existing usage, value names kept: it counts the pooling of members' separate, member-specific outcomes or hazards, so that one member's own loss is borne in part by the others. Dividing one common venture's outcome by shares is `LR3`'s question and is `0` here; so is a clause sending a member's earnings on a separate stake into the common stock (Scriba CLXXXI, 1157, p. 96, read in context: the investor's extra £31, *quarum totum proficuum debet esse suum preter quartam que debet reverti in societatem ipsam*). An agreement pooling the profits of several separate ventures counts, on the arrangement it creates: Amalric 697 (1248; Blancard II, 153–154, read in context), three Jewish travellers to Valencia on the *Leopardus* making the profit of *omnium comandarum … sint eis communes equis porcionibus*, own money taking profit *pro solido & libra*. Ground: of 28 `LR4` cells, the 17 `0`s include every common-stock venture in the census (the three VOC rows, both *maone*, `partenrederij`, `bazacle_mill`, `casa_san_giorgio`, `chartered_corporation_england`), each coded `0` in its notes on one common exposure with nothing member-specific pooled; three of the four `1`s (`nakai_fictive_household`, across stores; `begijnhof`; `bruderschaft_salzburg`) rest on pooling members' separate fortunes. **The fourth, `asiento_averia` (`OF-0110`), is coded `1` "for the vehicle", whose *participes* "pool capital and share loss proportionally" — the ground this clarification excludes; its note says the levy limb would also carry `1`, "but the members differ". Found while applying, not raised when D3 was put; flagged below, not repaired.** The strongest objection — that this infers `0` from form rather than evidence — is answered by that house practice; whether commingling (`CI5`) makes a venture pool is left open (logbook 4, 2026-10-12 (iii)). No value moves by the clarification itself; entries 4, 5, 7 and 17 are ruled separately. No version bump: a definition, not a declared constraint.

## Flagged, not ruled

`asiento_averia LR4` (`OF-0110`, `1`, medium, `.NR`, Hierro Anibarro 2005): its stated ground, the vehicle's *participes* pooling capital and sharing loss proportionally, is excluded by ruling 10; whether the averia levy — a compulsory ad valorem charge spreading the cost of convoy protection across all shippers — carries `1` for this row turns on the row's unit, which the note leaves deliberately ambiguous. `OF-0111` (`LR5`) depends on it.

`comanda_alloc VF1` rests on *Consolat* cap. 279, an accounting rule; Venice shows the account oath and the proof of a peril loss as separate rules. Until caps. 209–210 and 220 are read for a peril-specific rule, the family's separation on `VF1` may not be like for like.
