# Rulings in the clearance of the pending recodings queue (2026-10-25)

**Status: ruled by MS in chat on 2026-10-25, each on a recommendation put by the assistant (`claude-opus-5-5`, effort `high`) and accepted as proposed. Recorded here by the assistant. Pass slug `queue-clearance-2026-10-25`; open, not blind. No source was re-read for ruling 1, which rules on the rows as they stand; the sources read for rulings 2–5 are listed before ruling 2.**

## The queue as found

At HEAD `82e6724`, 157 rows in the two `recodings.csv` files carried `adjudication = pending`: 36 in `loss_mitigation_forms`, 121 in `organizational_forms`. They come from three passes, none of them younger than 2026-09-28:

| pass                                   | `loss_mitigation_forms` | `organizational_forms` | rows |
|----------------------------------------|-------------------------|------------------------|------|
| `opus55-recode-mutual-pole-2026-09-26` | 0                       | 64                     | 64   |
| `commenda-primary-2026-09-28`          | 24                      | 38                     | 62   |
| `commenda-secondary-2026-09-28`        | 12                      | 19                     | 31   |
| all                                    | 36                      | 121                    | 157  |

No live cell under any of the 157 has been rewritten since the row was entered: no later `replaced` or `overruled` recoding sits on the same `record_id`. The two adjudication worksheets in `proposed-of/` (`ADJUDICATION-opus55-recode-mutual-pole-2026-09-26.md`, `ADJUDICATION-commenda-pilot-2026-09-28.md`) listed only the value disagreements; the rows left pending are, with eleven exceptions, the agreements those worksheets did not list.

Split by script against the live `data.csv`, into three tranches:

- **Tranche 1 — 98 rows.** `agreement = agree`, and the recoding's `confidence` equals the live cell's. 12 in `loss_mitigation_forms`, 86 in `organizational_forms`.
- **Tranche 2 — 48 rows on 26 cells.** `agree`, but the confidence differs.
- **Tranche 3 — 11 rows.** `disagree`, all from the mutual-pole pass (`avariz_vakfi` 7, `bruderschaft_salzburg` 4): the eleven entries of the mutual-pole worksheet.

## 1. Tranche 1 — the 98 agreeing rows are `kept`

`adjudication` `pending` → `kept`, `adjudicated_by` `none` → `MS`, on these rows and on no other field:

- `loss_mitigation_forms` (12): LM-R0001, LM-R0008, LM-R0018, LM-R0019, LM-R0027, LM-R0031, LM-R0037, LM-R0038, LM-R0046, LM-R0050, LM-R0056, LM-R0057. Commenda primary arm: `societas_maris` 6, `commenda_alloc` 2; secondary arm: `societas_maris` 2, `commenda_alloc` 2.
- `organizational_forms` (86): OF-R0001, OF-R0004–R0009, OF-R0011, OF-R0012, OF-R0014–R0016, OF-R0018, OF-R0021, OF-R0023–R0025, OF-R0027, OF-R0029, OF-R0031–R0033, OF-R0035–R0042, OF-R0044, OF-R0046–R0050, OF-R0053, OF-R0054, OF-R0057, OF-R0059, OF-R0061–R0065, OF-R0072, OF-R0074–R0076, OF-R0079, OF-R0086, OF-R0091, OF-R0092, OF-R0095, OF-R0096, OF-R0101–R0103, OF-R0105–R0107, OF-R0114, OF-R0121, OF-R0125, OF-R0127, OF-R0133, OF-R0134, OF-R0137, OF-R0138, OF-R0143, OF-R0144, OF-R0147–R0149, OF-R0156, OF-R0163, OF-R0167, OF-R0169, OF-R0175, OF-R0176, OF-R0179, OF-R0180, OF-R0185, OF-R0186, OF-R0189, OF-R0190. Mutual-pole pass: `bruderschaft_salzburg` 23, `avariz_vakfi` 21; commenda primary arm: `societas_maris` 14, `commenda` 12; secondary arm: `commenda` 8, `societas_maris` 8.

`data.csv` is unchanged: `kept` means the live value stands, and the live cell's `source_ref`, `confidence` and `articulation` stand with it.

**What these agreements are worth, which the ruling does not raise:**

- **Commenda primary arm.** The sampled acts carry the live value. But the live `societas_maris` and `commenda` cells rest on van Doosselaere 2009, whose dataset is built from the same Genoese cartularies, so primary and live are one evidence base and their agreement is one witness, not two (worksheet, "What the rows cannot tell you"). The effective n is the number of notaries: Scriba and Cassinese in Genoa, Amalric in Marseille.
- **Commenda secondary arm.** It re-read the literature the live cells were coded from. Its agreement shows the coding reproduces; it does not show the coding is right.
- **Mutual-pole pass.** Both coders are Claude models (`claude-opus-5` live, `claude-opus-5-5` re-code), so agreement is weak evidence of reliability; and the re-code's filled priors were not committed before coding (worksheet, third paragraph).

**Correction of the recommendation as put in chat.** The assistant described the primary-arm agreements as confirming the values on the Genoese and Marseille acts. That overstated them, for the reason in the first bullet. The ruling does not depend on it: `kept` follows from value equality alone.

**Left open by this ruling:**

- **The mutual-pole worksheet's definitional questions 3 and 4** — `AP4` with plural, cumulative founders, and `MG4` religious against customary. Their cells are among the 98 (OF-R0007 `avariz_vakfi AP4 = 1`; OF-R0025 and OF-R0057, `MG4 = religious` on both forms), and agreeing on a value answers neither question. Questions 1 (`LR4` and a spiritual hazard) and 2 (`CF1` on waqf-type forms) sit on Tranche 2 cells.
- **Articulation.** 31 of the 98 rows differ from the live cell in `articulation` (11 mutual-pole, 12 commenda primary, 8 commenda secondary); in the mutual-pole rows the re-code says `analyst-imposed` each time. Not adjudicated here.
- **Re-basing.** Where a primary-arm row supplies an act-level basis for a cell whose live `source_ref` is secondary, moving the cell onto it is a separate, cell-by-cell decision, made by a new recoding row as in the rulings of 2026-10-12.

## Tranche 2 — how it divides

Ruled in three parts, as recommended: (a) the 3 `commenda_alloc` and 11 `societas_maris` cells (6 in `loss_mitigation_forms`, 5 in `organizational_forms`; 32 rows) where the commenda arms differ from the live confidence are carried into the Venetian pass, which re-rules those cells with the Venetian half of the evidence, and their rows stay `pending` until then (the count was given in chat as 3 and 8; the script count is 3 and 11); (b) `commenda` `LR2`, `CF3` and `LR6`, rulings 2–4 below; (c) the 9 mutual-pole cells where the re-code is one step lower each time, to be read at the pages with Tranche 3.

**Sources read for rulings 2–5, on the page images through the Zotero connector on MS's machine:** *Il cartolare di Giovanni Scriba* I (`QTEG4PM7`, file `DHLLKXEI`), pp. 39 (LXXII, LXXIII), 48 (LXXXIX), 184–185 (CCCLIII–CCCLVI); *Guglielmo Cassinese* I (`G4TIJ2FM`, file `HFIT7SSW`), pp. 19 (41), 52 (124–126); Blancard I (`HF8ME3N7`, file `KAZIK3NZ`), pp. 274 (Amalric 27–29), 316 (Amalric 123–126); and, in the text layer, van Doosselaere 2009 (`V4S222VJ`, file `RHJHE7WQ`), 65–68 (printed = PDF − 18). Scriba's offset is not the logbook's: printed p. 39 = PDF 104 (− 65), p. 48 = PDF 113, p. 185 = PDF 254 (− 69).

## 2. `commenda LR2 = coupled` (OF-0081) — re-based, `medium` → `high`

New row `OF-R0245` **replaced**: `coupled`, `high`, `articulated`, `la`. The working party takes an agreed share of profit in terms — Scriba LXXII (1156, p. 39), *proficui quod in eis Deus dederit quartam habere debet*; Cassinese 41 (1191, p. 19), *ad terciam proficui*; Cassinese 125 (1191, p. 52), *ad quartam proficui*; Amalric 29 and 125 (Blancard I, 274, 316), *ad quartam partem lucri* — and van Doosselaere 2009, 66–67 finds only a handful of 4,860 commenda ties of 1154–1265 departing from the fixed quarter. Arm P: coupled in 52 of 59 speaking acts. The previous `source_ref` was `[verify]`. Arm rows `OF-R0068`, `OF-R0110`, `OF-R0152` **kept**. The gratuitous minority is handled by ruling 5.

## 3. `commenda CF3 = bilateral` (OF-0087) — re-based, `medium` → `high`

New row `OF-R0246` **replaced**: `bilateral`, `high`, `articulated`, `la`. One investor in the modal act (Scriba LXXII; Cassinese 41; Amalric 29, 125); arm P 96 of 130 (Scriba 10 of 10, Cassinese 38 of 60, Amalric 48 of 60); van Doosselaere 2009, 70 n. 11, 2,705 single- against 504 multiple-investor commendas, 1210–1300. Multilateral is variation across instances, recorded by count (Cassinese 125, two investors *de societate quam habent insimul*; Cassinese 22 of 60). `CF3` is nominal, so no `P`. **Objection put and answered:** Cassinese's 37% multilateral is a minority in every notary and in van Doosselaere's later sample, so the modal value is not in doubt, which is what `medium` would have to express. The previous `source_ref` was `[verify]`. Arm rows `OF-R0116`, `OF-R0158` **kept** (the secondary arm's `OF-R0074` was kept in ruling 1).

## 4. `commenda LR6 = upside-only` (OF-0090) — re-based, `high` → `medium`

New row `OF-R0247` **replaced**: `upside-only`, `medium`, `analyst-imposed`, `la`. Basis: van Doosselaere 2009, 65 (the investor "bore all liability for loss", the traveller "bore no capital risk") and 68 (his loss "was limited to the value of his labor"); Amalric 29 and 125, where *ad fortunam Dei et usum maris et tuum resegum* stands with *ad quartam partem lucri* in one act; Amalric 364 and 931 as read by arm P, not re-read. The previous `source_ref`, "Harris 2020", carried no page and was never verified. **Grounds for `medium`:** (i) `LR6` shares the `agent-loss-exposure` group with `CF2`; upside-only is `CF2 = 0` plus a share of profit, so it cannot be more certain than `commenda CF2 = 0` at `medium` (OF-0086); (ii) the direction is stated in terms only at Marseille, and in the Genoese acts sampled the peril is unstated, a question of default law (ruling 1 of 2026-10-07). `analyst-imposed`: no act states the direction; it is composed from two clauses. Variant symmetric: Scriba CCCLV (14 February 1158, p. 185), *Capitale tuum super me salvum erit*, profit halved — drafted *in societatem*, a commenda by structure (ruling 9 of 2026-10-12). Arm rows `OF-R0117`, `OF-R0159` **kept** (the secondary arm's `OF-R0075` was kept in ruling 1; its `high` is not adopted).

## 5. Scope: the gratuitous commenda is outside `commenda`

Ruling 13 of 2026-10-12 assigns acts to `commenda` by structure: the working party trades capital he did not contribute *for a share of profit*. **A gratuitous commenda — no share of profit to the working party (*gratis*; *capitale et proficuum tuum*, Scriba LXXXIX, 30 June 1156, p. 48) — fails that structure and is outside the row.** It is recorded in the cells' notes as a neighbouring arrangement, not as a variant. Van Doosselaere 2009, 67 n. 8 counts it among the rare exceptions to the standard payout (*gratis et amore*, perhaps an exchange of favour). Arm P's seven: Scriba LXXXIX, CCLXXXVII, DCCXLVII; Cassinese 383, 500, 750, 1087. Recorded in the `commenda` type row (`vocabularies/organizational_form_type.csv`, `key_source`).

**Consequence, carried:** `commenda CF2 = 0` (OF-0086) cites four Scriba acts, and two of them are gratuitous — LXXXIX (*Hoc debeo portare ad tuum resicum … capitale et proficuum tuum*) and CCLXXXVII (*quicquid enim sunt vel erunt tibi esse debent*). The cell is to be re-pointed to the acts that remain (Scriba CV, CXVIII; Amalric 29, 125, 364). The value is not expected to move.

## The mutual-pole sitting — rulings 6–25

The 20 remaining rows of pass `opus55-recode-mutual-pole-2026-09-26`: the 11 value disagreements (Tranche 3) and the 9 confidence differences (Tranche 2(c)), ruled item by item in the order of `proposed-of/ADJUDICATION-opus55-recode-mutual-pole-2026-09-26.md`, each on a stated recommendation accepted as proposed.

**Read for these rulings**, through the Zotero connector on MS's machine, text layers (clean in all five works): Kars 2020 (`GAZN2XVN`, file `CQ4L4NHZ`; printed = PDF + 159), pp. 160–169, 174–177, 179–185; Kıvrım 2019 (`GSC5PEAH`, file `7WXXB6CH`; printed = PDF + 33), pp. 34, 36–39; Küçük 2025 (`NAQKKKN7`, file `JNZHR9BT`; printed = PDF + 146), pp. 147–148, 150–154, 161; Gürsoy 2019 (`VM4K33C4`, file `R4QC5ZL3`; printed = PDF + 94), pp. 104–106, 110, 112–113; Klieber 2001 (`SR4E4QM7`, file `VEUB2IG2`; printed = PDF + 33), pp. 35, 42–45, 47–59, 61–67.

**A finding that runs through items 1, 2 and 7.** The live cells' premise that donor and beneficiary are disjoint (OF-0662, OF-0669) is contradicted on the page they cite: Kıvrım 37 names the donors by their own quarter (*Zincirlikuyu Mahallesi'nden Hacı Arab 50 kuruş …*, giving to *mahallelerinin avârız vakıflarına*), and two of them, Yakub and Seyyid Halil of Kanalıcı, gave *kendi evlerinden avârız alınmamak şartı ile*. Kars's abstract says the funds were made by notables of the same settlement. The premise is withdrawn from every cell that rested on it.

**A pattern through items 4–6.** The live `avariz_vakfi` entity and term cells took stronger values than `waqf_khayri` on the same Ḥanafī-Ottoman law, on the ground that their sources are working registers rather than doctrine; read closely, the registers show what the `waqf_khayri` values describe.

| item | ruling | cell                                  | live                    | re-code                 | ruled                                       | rows                                  |
|------|--------|---------------------------------------|-------------------------|-------------------------|---------------------------------------------|---------------------------------------|
| 1    | 6      | `avariz_vakfi FP1` (OF-0669)          | pious-charitable medium | mixed medium            | **mixed** medium analyst-imposed            | OF-R0026 replaced                     |
| 2    | 7      | `avariz_vakfi LR4` (OF-0662)          | 0 medium                | P low                   | **0 low**, basis rewritten                  | OF-R0248 replaced; OF-R0019 kept      |
| 3    | 8      | `avariz_vakfi LR5` (OF-0663)          | .NA                     | synchronising low       | **.NA** (follows item 2)                    | OF-R0020 kept                         |
| 4    | 9      | `avariz_vakfi LP2` (OF-0645)          | 1 medium                | P low                   | **P medium** articulated                    | OF-R0249 replaced; OF-R0002 replaced  |
| 5    | 10     | `avariz_vakfi LP3` (OF-0646)          | 1 medium                | P medium                | **P medium** articulated                    | OF-R0003 replaced                     |
| 6    | 11     | `avariz_vakfi TS3` (OF-0653)          | P medium                | .NR                     | **0 low** (a third value)                   | OF-R0250 replaced; OF-R0010 overruled |
| 7    | 12     | `avariz_vakfi FP3` (OF-0671)          | P low                   | .NR                     | **.NR**                                     | OF-R0028 replaced                     |
| 8    | 13     | `avariz_vakfi CI2` (OF-0656)          | 1 high                  | 1 medium                | **1 medium** articulated                    | OF-R0251 replaced; OF-R0013 kept      |
| 9    | 14     | `avariz_vakfi LR2` (OF-0660)          | veiled medium           | veiled low              | **veiled medium** (live stands)             | OF-R0017 kept; note addition          |
| 10   | 15     | `avariz_vakfi MG1` (OF-0665)          | beneficiary high        | beneficiary medium      | **beneficiary medium** articulated          | OF-R0252 replaced; OF-R0022 kept      |
| 11   | 16     | `avariz_vakfi CF1` (OF-0673)          | 0 medium                | 0 low                   | **0 medium** (live stands)                  | OF-R0030 kept; note correction        |
| 12   | 17     | `bruderschaft_salzburg TS4` (OF-0686) | 0 medium                | P low                   | **0 medium** (live stands)                  | OF-R0043 kept                         |
| 13   | 18     | `bruderschaft_salzburg CI2` (OF-0688) | 1 medium                | .NR                     | **.NR**                                     | OF-R0045 replaced                     |
| 14   | 19     | `bruderschaft_salzburg MG2` (OF-0698) | .NR                     | collective low          | **collective low**                          | OF-R0055 replaced                     |
| 15   | 20     | `bruderschaft_salzburg FP3` (OF-0703) | P medium                | .NR                     | **.NR**                                     | OF-R0060 replaced                     |
| 16   | 21     | `bruderschaft_salzburg LP2` (OF-0677) | 1 high                  | 1 medium                | **1 medium** articulated                    | OF-R0034 replaced                     |
| 17   | 22     | `bruderschaft_salzburg LR4` (OF-0694) | 1 high                  | 1 medium                | **1 high** (live stands)                    | OF-R0051 kept; note addition          |
| 18   | 23     | `bruderschaft_salzburg LR5` (OF-0695) | diversifying medium     | diversifying low        | **diversifying low**                        | OF-R0052 replaced                     |
| 19   | 24     | `bruderschaft_salzburg MG3` (OF-0699) | 0 high                  | 0 medium                | **0 high** (live stands)                    | OF-R0056 kept; note addition          |
| 20   | 25     | `bruderschaft_salzburg FP1` (OF-0701) | mutual-provision high   | mutual-provision medium | **mutual-provision medium** analyst-imposed | OF-R0058 replaced                     |

**Grounds, in brief, numbered by ruling** (the full reasoning is in each `data.csv` cell's note, which keeps the previous note after it):

- **6, FP1.** The deeds and accounts declare both the quarter's common obligations (Küçük 148, 153) and pious heads (imam, school, *suleha-yı fukara*, recitation: Kars 175–177; Küçük 154). Read with ruling 7: joint provision for a common levy is mutual provision; pooling member-specific hazards is another thing.
- **7, LR4.** The main draw is a common levy (Kars 167); the member-specific draws are grants to the poor (Kars 175–176; Küçük 154, 161) — allocation to a class from an endowment, not mutualisation, the `waqf_khayri` line. Kars 184 is a repayable loan to the tenant of a fund-owned house. Low: disaster relief appears only in general statements (Kars 168; Küçük 152). The re-code's `P` at `low`, beside a note offering `0`, is the pattern `CLAUDE.md` names.
- **8, LR5.** `.NA` while `LR4 = 0`.
- **9, LP2.** Held in the fund's name (*vakfına ait*, *vakıf adına*: Kars 180–183) and owned by no one (*temlik ve temellükten ebediyen alıkoymak*, Kars 164). Medium because both halves are in the tradition's own words.
- **10, LP3.** Standing through the office (*tevliyetim hasebiyle*, Kıvrım 38). *Mütevelli de diğer alacaklılar gibi bir alacaklıdır* concerns priority, not standing. **Flag, not ruled:** `begijnhof LP3 = 1` (`high`) carries the same caveat.
- **11, TS3.** `P` mixes modes of founding (variation across deeds; ruling 7 of 2026-10-11) and pre-binding revocation (Gürsoy 113); `.NR` ignores the positive normative statement of perpetuity (Kars 164). `0`, low, as `waqf_khayri`.
- **12, FP3.** The conditional gifts are a bargain inside the apportionment, not a status conferred against outsiders. The live `P` was a frequency.
- **13, CI2.** The deeds bar spending principal (Küçük 151; Kars 167, 179; Gürsoy 110), which is preservation against the administrator; contributors' withdrawal is barred by irrevocability, now `TS3 = 0` low. High rested on a neighbouring question.
- **14, LR2.** Defaults fall on the fund (Kıvrım 38; Kars 182–183), which answers the question the re-code called unasked.
- **15, MG1.** Membership is a real alternative (residents elect the trustee, Kıvrım 38; donors are residents; one class is "the residents"), but no admission or roll is described.
- **16, CF1.** The census treats office as not `CF1`'s labour (`maona_chios`, `maona_corsica`, `casa_san_giorgio`), which answers the worksheet's definitional question 2 in practice. The live note's "borrowers are outsiders" is withdrawn (Küçük 153).
- **17, TS4.** Statutes needed approbation (Klieber 50, 66); the re-code's examples are spending within the statutes (49, 58), not amendment.
- **18, CI2.** Klieber 48 is silent on refunds; 56–57 concerns debtors. Silence stays `.NR`.
- **19, MG2.** `.NR` "for no fitting value" is not what `.NR` means. Coded on the modal instance (Klieber 52–53, 66); the *betreute* subtype and the post-1785 position recorded as variation. No split; the worksheet's split proposal is closed. Type row updated.
- **20, FP3.** No instance of membership obtaining status or access (Klieber 47, 61). The definition at Klieber 35 is Remling's, not Klieber's; corrected.
- **21, LP2.** Owned and disposed of as fraternities (42, 55–59); silent on ownership for the *betreute* subtype (52).
- **22, LR4.** Does not depend on whether a spiritual hazard counts (worksheet definitional question 1): the pooled outlay is material (mass stipends, bearers, bier, pall, shroud: 43–45). That question stays open for a spiritual-only case.
- **23, LR5.** Klieber never discusses correlated mortality; the value rests on general knowledge.
- **24, MG3.** True by the row's scoping (free access defines the type, 47–48), so certain and without comparative weight.
- **25, FP1.** The declared idiom is pious (*Nächstenliebe*, 59; CIC 1917, 35); the mutual reading is Klieber's (43, 50, 62–63). Consistent with ruling 6: there two declared heads, here one, in pious language.

**Worksheet questions after the sitting.** Definitional question 1 (`LR4` and a spiritual hazard): open, not needed by any cell. Question 2 (`CF1` on waqf-type forms): answered in practice by census usage; `waqf_khayri CF1 = .NA` carried. Questions 3 (`AP4`, plural founders) and 4 (`MG4`, religious or customary): open, as recorded under ruling 1. Split proposal (`MG2`): closed by ruling 19.

## Carried

- **Tranche 2(a)** — 14 cells, 32 rows, into the Venetian pass (above).
- **`commenda CF2` re-pointing** (ruling 5).
- **`CF3`'s definition says "number of principals", but the cells apply it to the number of parties.** One investor and one working party is `bilateral` on `qirad` and `mudaraba` ("two parties in the base case"), on `comanda` (an investor bound to one commendatary) and now on `commenda`; the `isqa` and `societas_maris` notes say "two principals". On the definition's words a single-investor commenda has one principal. A wording question for the vocabulary, not ruled here.
- **`waqf_khayri CF1 = .NA`** against the census's `0` for office-holding forms (ruling 16).
- **`begijnhof LP3 = 1`** (`high`) against the standing-through-the-office reading of ruling 10.
- **Mutual-pole definitional questions 1, 3 and 4** (above).
