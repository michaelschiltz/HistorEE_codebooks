# Coding notes — opus55-recode-mutual-pole-2026-09-26

Blind re-coding of `avariz_vakfi` and `bruderschaft_salzburg`, 32 characteristics each, 64 cells. Written by the coding chat (Chat B; configured model `claude-opus-5-5`; effort `high` per the kickoff, which I cannot observe from inside the session) inside `~/GitHub/_blind-opus55-mutual-pole-2026-09-26` only.

**Ordering held.** Priors were written to `records/PRIORS-opus55-recode-mutual-pole-2026-09-26.md` (finished 13:33 UTC) and MS reported the commit before any file in `sources/` was opened. All five sources were then read in full. All 64 cells were fixed in `recodings-opus55-recode-mutual-pole-2026-09-26.csv` and this file, with the six answers, was written (13:51 UTC onward) **before anything was computed about the rest of the matrix** — no value distribution, zero-instance set or signature has been computed from the bundle's `data.csv` at the time of writing. Anything computed afterwards is in a separate file, `NOTES-opus55-recode-mutual-pole-postfreeze-2026-09-26.md`, and changes no cell.

**Filename.** No collision: `proposed-of/` held nothing before this pass. The `-coding-` suffix is the kickoff's, on the precedent of selection-brief collisions.

**What I did not do.** No Zotero, Undermind, Elicit, web search or other source-finding tool. No file outside the bundle. No Project document, Project search or memory file opened (see exposure, item 6). No `git`. No edit to `data.csv`, the vocabularies, or anything outside `proposed-of/` and the priors file. No `data.csv` or type row minted. `value_at_recoding` and `agreement` left empty.

## 1. Reading record

Every source was extracted page by page with `pdftotext -layout` on the device, read end to end, and its printed folios checked against running heads on both sides of the spread. `source_ref` cites printed folios. `source_read=full` on every substantive and `.NR` cell, because every source was read in full.

| source (file)                | pp. in PDF | printed folios | offset         | note |
|------------------------------|-----------:|----------------|----------------|------|
| Kars 2020 (`Kars2020_GAZN2XVN.pdf`)    | 28 | 160–187 | printed = PDF + 159 | Running head reads *TAD* C.40/S.69, **2021**; received 15.08.2020, accepted 03.10.2020. Cited "Kars 2020" as the kickoff names it; year flagged, not repaired. Istanbul, İstanbul Şer'iyye Sicilleri. |
| Kıvrım 2019 (`Kivrim2019_GSC5PEAH.pdf`) | 16 | 34–49   | printed = PDF + 33  | Ayntab (Gaziantep Şer'iyye Sicilleri); transcribed appendix (Ek) 43–49. |
| Gürsoy 2019 (`Gursoy2019_VM4K33C4.pdf`) | 32 | 95–126  | printed = PDF + 94  | Evkaf Muhasebeciliği Mahkemesi registers; the text layer also shows folios on odd pages. |
| Küçük 2025 (`Kucuk2025_NAQKKKN7.pdf`)   | 37 | 147–183 | printed = PDF + 146 | Kastamonu, Kırkçeşme mahallesi fund, 1834–1867; DOI 10.21021/osmed.1472954. |
| Klieber 2001 (`Klieber2001_SR4E4QM7.pdf`) | 37 | 34–70 | printed = PDF + 33  | Text layer readable throughout; footnotes on p. 58 slightly interleaved but legible. |

**The Klieber text layer is not "column-interleaved to the point of unreliability."** That characterisation (logbook 2, 2026-08-13, quoted in the priors' exposure item 4) does not describe this file. Either a different file was read then, or the layer was replaced. Flagged for logbook 5.

## 2. Non-independence

**Kars 2020 reproduces Kıvrım 2019's generalising text verbatim, with the city swapped.** A shingle comparison of the two text layers gives 317 shared 8-word sequences, in long runs: the definition of the levy; the list of uses; "mahalle halkının katkılarıyla kurulmuş ve çeşitli vesilelerle yapılan bağışlarla zenginleştirilmiştir"; the rule for mixed quarters; the cash-waqf lending methods; *muamele-i şer'iyye*; the paragraph on a debtor's death and the fund's lack of priority; and the conclusion. Kars cites Kıvrım once (fn. 53, p. 179, and the bibliography). **Consequence for coding:** wherever Kars and Kıvrım state the same general rule, they are one witness. Kars's independent evidence is its own Istanbul court entries (roughly 173–184). The cells where this bites are named in their notes: `TS4` (Kars 168 = Kıvrım 35), `MG2` (Kars 173 is Kıvrım's sentence), `CF3` (Kars 169 repeats Kıvrım 37), `AP1` (Kars 182 in Kıvrım's words).

**Shared upstream.** Kars, Kıvrım and Küçük all rest their general account on İpşirli's DİA entry "Avarız Vakfı", Akgündüz (228–229, on the debtor's death) and Ergin 1936. `TS4`'s general statement ("heyet kararıyla uygun yerlere sarf") is İpşirli's, relayed twice: one witness, coded `low`.

**Küçük 2025** lists Kıvrım 2019 and Gürsoy 2018 in its bibliography; its primary data (the Kırkçeşme ledgers and Evkaf defter) are its own. **Gürsoy 2019** cites only Kıvrım's 2016 Rize article and none of the other three; its data (EMM registers) are independent. So the independent witnesses for `avariz_vakfi` are: Kars's Istanbul entries, Kıvrım's Ayntab entries, Gürsoy's EMM registers, and Küçük's Kastamonu ledgers. The general framing is one witness.

**`bruderschaft_salzburg`** rests on one author. Nothing tests its independence.

## 3. Sub-pool

**By its sources' own enumeration, `avariz_vakfi` is a sub-pool form in Ayntab.** The Ammu mahalle fund is split into nine *bölük*/*hane* funds and the Alineccar fund into two. Each has its own mütevelli, its own ledger, and capital earmarked for that bölük's avarız (Kıvrım 39, 45–47). In Istanbul the opposite holds: several endowments for one quarter are aggregated "avarız sandıklarında toplanarak" (Gürsoy 105), and Kars 174 describes one budget per mahalle. Kırkçeşme's several mütevellis each held bonds for a group of borrowers (Küçük 156, 181), but they divided the administration of one capital, not the capital itself. Per the 2026-08-31 rule, the arrangement is the quarter's fund, and the partition is carried in notes (`LP2`, `CI1`) and not coded.

**`bruderschaft_salzburg` is not a sub-pool form.** There is one purse per fraternity. A Liebesbund's contribution rate reserved for Hausarme (57–58) is an earmark within that purse.

## 4. Coverage

`avariz_vakfi`: 19 substantive, 10 `.NR`, 3 `.NA`. `bruderschaft_salzburg`: 16 substantive, 14 `.NR`, 2 `.NA`. The counts below are by component. A characteristic in two components counts in both.

| component            | avariz_vakfi (subst / .NR / .NA) | bruderschaft_salzburg (subst / .NR / .NA) |
|----------------------|----------------------------------|-------------------------------------------|
| legal-personality    | 2 / 1 / 0                        | 1 / 2 / 0                                 |
| entity-shielding     | 1 / 2 / 0                        | **0** / 2 / 1                             |
| owner-shielding      | **0** / 2 / 0                    | **0** / 2 / 0                             |
| perpetual-succession | 3 / 1 / 0                        | 3 / 1 / 0                                 |
| capital-lock-in      | 1 / 0 / 0                        | **0** / 1 / 0                             |
| transferable-claims  | **0** / 2 / 0                    | **0** / 2 / 0                             |
| outcome-coupling     | 1 / 0 / 1                        | **0** / 2 / 0                             |
| loss-sharing         | 1 / 0 / 1                        | 1 / 0 / 1                                 |
| risk-pooling         | 2 / 0 / 0                        | 2 / 0 / 0                                 |
| none                 | 8 / 2 / 1                        | 9 / 2 / 0                                 |

**Components that learned nothing:** owner-shielding and transferable-claims on both forms, plus entity-shielding (its one non-`.NR` cell is a `.NA`), capital-lock-in and outcome-coupling on `bruderschaft_salzburg`. These sources are fiscal, social and church histories, and none asks the creditor questions.

## 5. Decision points and their alternatives

Every cell's note carries its evidence and, where one exists, the alternative reading. The contested cells are listed here.

### `avariz_vakfi`

| char  | coded | conf   | alternative(s) and why not |
|-------|-------|--------|----------------------------|
| `LP2` | P     | low    | **1**, if holding "avarız vakfına ait" is read as holding as an entity. Not taken: every act runs through the mütevelli, and the doctrine the sources relay withdraws the corpus from ownership. |
| `LP3` | P     | medium | **1**. Not taken: no record shows the fund suing apart from its officer. Articulated on "tevliyetim hasebiyle" (Kıvrım 38). |
| `AP1` | .NR   | —      | The one priority statement is the reverse question: the fund, as creditor, had no priority in a dead debtor's estate (Kıvrım 38; Kars 182 in Kıvrım's words). Carrying that across would have given `AP1` the wrong question. |
| `AP2` | .NR   | —      | The members' limb is partly evidenced (principal not to be spent). The creditor limb is silent. House rule: `.NR`. |
| `AP4` | 1     | medium | **.NA**, if the corpus is read as arising from collection. Not taken: identifiable donors endow out of their own property (Kars 175–176, 181; Kıvrım 37–38). Founders are plural and cumulative, so the locator is met donor by donor. Exposure item 1 applies. |
| `TS4` | P     | low    | **1**. The general statement is İpşirli, relayed twice. Founders' conditions barred alteration (Kars 175). |
| `CI1` | common | medium | **several-accounts** on the Ayntab bölük split. Not taken on the sub-pool rule (§3). |
| `CI3`/`CI4` | .NR | — | **0** was my prior. Not taken: no source addresses alienation of a resident's claim. A plot "avarıza bağlı" (Kars 178) is an obligation running with land, the reverse question. |
| `LR2` | veiled | low   | **.NR**, since no source asks whether the trustee bore losses. **coupled**, on the Burdur deed's fixed 75-of-375 akçe share (Kars 176). Taken on the stated salary (Küçük 154) and fault-based restoration (Küçük 151). |
| `LR4` | P     | low    | **1** (the reading that the poor-relief, funeral and fire lines are mutualisation), or **0** (the fund as charity allocated to residents). Taken as P because the main draw is a covariate common levy, while the contingent lines meet member-specific hazards. Both halves sit within one fund. Exposure items 3 and 5. |
| `LR5` | synchronising | low | Exists only because `LR4`≠0. |
| `LR6` | .NA   | —      | Follows `LR2=veiled`. If `LR2` falls to `.NR`, this becomes `.NR`. |
| `MG1` | beneficiary | medium | **membership**. Not taken: no admission and no roll; residence alone is not enrolment. |
| `MG2` | collective | medium | **founder-fixed** for uses. Not taken: residents appoint, inspect and reappoint (Kıvrım 38, 47–48; Küçük 160 n.56). Articulated on the transcriptions. |
| `MG4` | religious | medium | **customary**: Ebussuud defended cash waqfs on *örf* (Küçük 149–151). Taken on the kadı's confirmation of each deed ("Vakıf tasdik olunur", Kars 176), not on the `waqf_khayri` analogy. |
| `FP1` | mixed | medium | **mutual-provision**, if the levy line is taken as primary. The same deeds and accounts pay the imam, the recitation, the *suleha-yı fukara* and a school. |
| `CF1` | 0     | low    | **P**, reading the trustee's labour against donors' capital; or **.NA**, the `waqf_khayri` disposition. Taken 0: the trustee is salaried or holds a fixed share, and borrowers are debtors, not partners. |

### `bruderschaft_salzburg`

| char  | coded | conf   | alternative(s) and why not |
|-------|-------|--------|----------------------------|
| `LP2` | 1     | medium | **P**, on the *betreute* subtype, whose finances lay with abbots or superiors (52). Taken 1 on the fraternities' own holdings and dispositions, articulated in the 1774 Josefsbruderschaft resolution (58). |
| `AP4` | .NA   | —      | **1**, if a donor's endowment founded a given fraternity. Klieber shows erection and enrolment, with donors adding to an existing body (63). |
| `TS3` | .NR   | —      | Dissolution came from outside (53, 38, 46, 68). No party holds a power to dissolve at will. Individual exit is not dissolution. |
| `TS4` | P     | low    | **1** on the independent fraternities' own resolutions (58). Statutes needed approval (50), and foundations the consistory's consent (55). |
| `CI2` | .NR   | —      | **1** was my prior. Klieber never mentions refund; ceasing to pay meant exit (48). |
| `LR4` | 1     | medium | **P**, if spiritual provision is held to fall outside the characteristic. The definition does not restrict the currency. Klieber's own analysis is insurance-like: "versicherungsartig garantierter Dienst", "Umlagesystem bzw. Generationenvertrag" (42–43, 45, 62–63). Material relief is marginal (57; 58 n.37) and does not carry the value. |
| `LR5` | diversifying | low | Deaths fall at different times. The Liebesbünde's risk was demographic (45). No epidemic is discussed. |
| `LR6` | .NR   | —      | `LR2` is `.NR`. `.NA` would assert `LR2=veiled`. |
| `MG2` | collective | low | **single-principal**, for the *betreute* subtype (52) and for the period after c.1785, when the parish clergy took over (53). **Split proposed**: see §6. |
| `MG3` | 0     | medium | **P**, on the Liebesbünde's fixed contributions, which "schränkten das Prinzip des freien Zugangs ein" (48). That is a difference between subtypes, not a structural half. Articulated on the enrolment-slip formula (48). |
| `FP1` | mutual-provision | medium | **pious-charitable**: care for the dead as *Nächstenliebe* (59), and *Gottesdienstmehrung* as the 1917 Code's *Proprium* (35). **mixed** is the other alternative. Taken on Klieber's own finding that the purpose was the members' "Eigenvorsorge fürs Jenseits" (62–63), and on his rejection of the "religiös-karitativ" formula (57). |
| `FP3` | .NR   | —      | One clause: membership as proof of confessional reliability (47). No finding. |
| `FP4` | P     | medium | **1**, on the church–state coincidence in the prince-archbishopric. Not taken: no authority had a complete overview, and fraternities were exempted from a Kataster (68). |

## 6. Split proposal (not coded)

**`bruderschaft_salzburg` `MG2`.** The row's period, 1600–1950, spans two governance regimes, and the row also spans two subtypes. Independent (*selbständige*) fraternities elected their prefect, assistants and consilium and ran their affairs "weitgehend autonom" (52, 66). *Betreute* fraternities were run by abbots, superiors or rectors (52). After c.1785, administration was withdrawn and the fraternities were left to the parish clergy (53). A split, either by subtype or at c.1785, would give `MG2` a clean value in each part: collective, then single-principal. The split test also touches `LP2` (P on the *betreute* subtype) and `TS4`. I coded the independent type of 1600–c.1785, which Klieber says dominated the countryside (53), at `low` confidence. **For MS to decide; not coded.**

## 7. Exposure (leaks) — reported, not used

Each of these was disclosed in the priors before any source was opened. The quotations are from the bundle files named.

1. **`vocabularies/organizational_form_characteristic.csv`, `AP4` definition:** "(COUNT CORRECTED 2026-09-08. This read 'two coded forms' from 2026-08-30 until today. [withheld 2026-09-26: the count names a form under blind re-coding.] … a third form at the same value adds a case and not a state, and AP4 still has one value across the column." Together with "on present coding AP4 has THREE coded forms and one value between them", this implies one of the two forms carries `AP4=1` live. I coded `avariz_vakfi` 1 and `bruderschaft_salzburg` .NA, both from the sources. The notes on both cells carry EXPOSURE flags.
2. **Entity-locator definitions (`LP1`–`LP3`, `AP1`, `AP2`, `MG4`, `FP2`, `FP4`):** "Sub-pool: … and [withheld 2026-09-26: one further form, under blind re-coding]. Not sub-pool: [withheld 2026-09-26: one form under blind re-coding]". This implies exactly one form is a sub-pool form. My finding (§3) agrees with that shape, and I reached it from Kıvrım 39, 45–47.
3. **`logbook/4`, 2026-09-07 ("Four empty values were available and refused"), at 801 rows:** `TS4=1`, `MG3=P`, `LR2=attenuated`, `LR4=P` and `LR1=none` "had no instance". Also 2026-09-05 (ii), at 707 rows: `TS1=P` zero-instance; `LP3=0`, `AP2=P` and `FP4=0` were held by other forms. **This pass codes `avariz_vakfi` `LR4=P`, which the logbook implies differs from the live value.** Every other value is consistent with these statements. EXPOSURE flags are on `TS4`, `LR1`, `LR4` (both forms) and `MG3`.
4. **`vocabularies/loss_mitigation_type.csv`, line 9** (confraternity umbrella): "The regional limit added on 2026-08-13 from Klieber 2001 concluded: 'this cannot be one row for Latin Christendom. When coded it must be split regionally…'" and "with one coded child [withheld 2026-09-26: form under blind re-coding]". **`logbook/2`, 2026-08-13:** "a form whose relief is a tenth of outgoings in one house in one decade would carry `MC1` only by straining it", and "the PDF's text layer is column-interleaved to the point of unreliability". I agree on the relief finding (57; 58 n.37). The text-layer claim is false for this file (§1).
5. **`vocabularies/loss_mitigation_type.csv`, line 53:** "Bursa's own avarız-ı mahalle funds are in his dataset with capital figures across 1078-1239 AH". **`logbook/4`, 2026-08-19 (iii)/(iv) and the entry above them:** "The fund is allocation and the pooling sits behind it — in the residual tax the fund fails to cover. The pooled thing is the shortfall, not the fund"; "Residents electing the mütevelli and the mütevelli lending to himself are compatible facts"; "`RB3` gains a fifth attestation of the *rehn-i kavî / kefîl-i melî* formula, Ayntab now"; "The sentence `MC1`'s original `pooling` rested on appears **verbatim in both, with the city swapped**". **`logbook/5`, 2026-08-19:** "Kars `GAZN2XVN` — Zotero dates it 2020; the running head reads *TAD* C.40/S.69, **2021**, 160–187." **Effect:** I knew in advance that two Turkish sources shared text. I measured it myself (§2) and found it larger than one sentence. I knew a prior session had read the residents as electing the mütevelli, and `MG2` rests on the transcriptions I read. I knew a prior session placed the pooling in the residual tax, and `LR4` reads the same evidence as structurally half-present instead.
6. **The chat's Project attachment.** This chat is attached to the claude.ai Project for HistorEE. The platform supplied its document titles, including `claude/opus55-recode-mutual-pole-operator-2026-09-26.md`, `claude/recode-mutual-pole-operator-prompt-2026-09-26.md` and `claude/recode-plan-2026-09-26.md`. **I opened no Project document, did not use Project search, and read no memory file.** The titles state no value. The kickoff did not anticipate this channel, and MS should decide whether it matters.
7. **The loaded skills** (`code-a-form`, `run-a-coding-batch`), read back against both forms: `code-a-form` names "avarız" only as an example Zotero search term, and "confraternita" only as an example of an uncoded umbrella with a reasoned refusal. Neither states or implies a value for either form under test. No leak found in the skills.
8. **House practice read before the priors.** I read the full rows of `waqf_khayri`, `begijnhof` and `nacion_cofradia`, with notes truncated, as house practice. Cell notes that name `waqf_khayri` or `begijnhof` cite them as precedents for a disposition (`LP2`, `CF1`, `LR6`), not as evidence for a value.

## 8. Flags (not repaired)

- **Kars year.** File and kickoff say 2020; the running head says 2021 (*TAD* C.40/S.69). `source_ref` uses "Kars 2020".
- **Klieber text layer** is fine (§1), contrary to logbook 2.
- **`MG4=religious` on a waqf-type form** has been criticised in this census as coded for consistency with `waqf_khayri`. Here it rests on per-deed kadı confirmation. The *örf* alternative is live.
- **`CF1` on waqf-type forms.** Is a salaried trustee's labour against donors' capital a capital–labour contract? The census seems to have two dispositions, 0 and .NA. I took 0 at `low`. MS may want one rule.
- **`FP4` vs `CI1` sub-pool.** In Ayntab, registration is per bölük fund (Kıvrım 39), so `FP4`'s entity locator is met at the partition level too. This is carried in notes.
- **`LR4` currency.** The definition does not say whether a spiritual hazard (post-mortem suffrage) counts. The `bruderschaft_salzburg` value depends on the reading that it does. That is a definitional question for MS, and I propose no repair.
- **Effort.** `coder_effort=high` rests on the kickoff. I cannot observe it.
- **Type rows absent from the bundle.** Neither `avariz_vakfi` nor `bruderschaft_salzburg` is in the bundle's `vocabularies/organizational_form_type.csv`, and OF-0644–0707 are absent from its `data.csv`. The `record_id` foreign key in `recodings` therefore fails inside the bundle by construction (§10).

## 9. The six answers

**1. What was coded and on what evidence.** All 64 cells were coded or declined.
- `avariz_vakfi` rests on four Turkish studies: Kars 2020 (Istanbul court records), Kıvrım 2019 (Ayntab court records with transcribed appendix), Gürsoy 2019 (Evkaf Muhasebeciliği registers) and Küçük 2025 (the Kastamonu Kırkçeşme ledgers, 1834–1867). It has 19 substantive cells. The best-evidenced are `TS1`, `TS2` and `FP4` (high), then `AP4`, `CI1`, `CI2`, `MG1`, `MG2`, `MG4`, `FP1` and `CF3` (medium). Articulated cells: `LP3`, on "tevliyetim hasebiyle" (Kıvrım 38); `MG2`, on the Ayntab transcriptions (Kıvrım 47–48) and Küçük 160 n.56.
- `bruderschaft_salzburg` rests on Klieber 2001 alone. It has 16 substantive cells, the best-evidenced being `TS1`, `TS2`, `MG1`, `MG4` and `CF3` (high). Articulated cells: `LP2`, on the 1774 Josefsbruderschaft resolution (58); `MG3`, on the enrolment-slip formula (48). Klieber's own "versicherungsartig" analysis of the Totendienst carries `LR4=1` and `FP1=mutual-provision` (42–45, 62–63).

**2. What could not be coded and why.** There are 24 `.NR` cells: 10 on `avariz_vakfi` and 14 on `bruderschaft_salzburg`. Almost all are the creditor-facing questions (`AP1`–`AP3`, `LR1`) and the transferability questions (`CI3`, `CI4`), which no source asks. Neither form is a debtor in its sources; both appear only as lenders. On both forms, `LP1` goes unasked. `TS3` is `.NR` on both because the sources show dissolution or constraint from outside, not a party's power to dissolve at will. `FP2` and `FP3` are `.NR` on both.
- On `avariz_vakfi`, the `AP2` members' limb is partly evidenced but the creditor limb is silent.
- On `bruderschaft_salzburg`: `LP3` (no litigation), `CI2` (refund never mentioned), `LR2` (officers' exposure unaddressed) and hence `LR6`.
- Five `.NA`: `avariz_vakfi` `LR6` (`LR2=veiled`), `MG3` (`MG1=beneficiary`) and `CF2` (`CF1=0`); `bruderschaft_salzburg` `AP4` (no founder) and `CF2` (`CF1=0`).
- Owner-shielding and transferable-claims learned nothing on either form (§4).

**3. Which of my own expectations were falsified.** These are quoted verbatim from `records/PRIORS-opus55-recode-mutual-pole-2026-09-26.md`.

`avariz_vakfi`:

> | `CI3` | 0 | low | Benefit tied to residence, not an alienable interest. Alternatives .NR, or P if the benefit is shown to run with the house. |

Falsified: `.NR`. No source addresses alienation.

> | `CI4` | 0 | low | As `CI3`; likely .NR in practice. |

Falsified: `.NR` (the stated fallback).

> | `LR2` | .NR | medium | The mütevelli's exposure to outcomes is probably not discussed; if it is, veiled (salaried) or coupled through liability for negligent loss. |

Falsified: `veiled`, low. Küçük 154 states the salary.

> | `LR6` | .NR | medium | Follows `LR2` .NR. |

Falsified: `.NA`, because `LR2` was coded.

> | `FP1` | mutual-provision | medium | A fund whose declared purpose is to meet the residents' own common obligations. Alternative: mixed, if the deeds carry pious lines alongside. |

Falsified: `mixed`. The deeds do carry the pious lines.

> | `FP2` | 0 | medium | No franchise; likely .NR if sources are silent. |

> | `FP3` | 0 | low | No status or access arbitrage expected; .NR likely. |

Both falsified: `.NR`. The sources are silent.

`bruderschaft_salzburg`:

> | `LP2` | P | low | Confraternities held and lent capital, but under parish or diocesan administration; 1 if Klieber has them owning in their own name, .NR if silent. |

Falsified: `1`, articulated (58).

> | `CI2` | 1 | low | Dues and gifts not returnable; .NR if not addressed. |

Falsified: `.NR`.

> | `CI3` | 0 | medium | Membership personal, not alienable. |

> | `CI4` | 0 | medium | As `CI3`. |

Both falsified: `.NR`. Transfer is never discussed.

> | `LR4` | P | low | Masses and prayers for deceased members and funeral attendance mutualise a death-timing hazard in spiritual currency; material relief marginal. (Exposure items 3 and 4: live value is not P; a prior session read relief as a tenth of outgoings.) |

Falsified: `1`, medium. I had expected spiritual currency to halve the value. Klieber's own analysis is of an insurance-like *Umlagesystem* in that currency, and the definition does not restrict the currency.

> | `FP1` | pious-charitable | medium | Devotional and suffrage purpose. Live alternatives: mutual-provision (suffrages for fellow members) and mixed. |

Falsified: `mutual-provision`. Klieber rejects the "religiös-karitativ" formula (57).

> | `FP2` | 0 | medium | No franchise; .NR if silent. |

> | `FP3` | 0 | low | .NR likely. |

Both falsified: `.NR`.

General expectations:

> "Across both. The mutual-pole selection presumably chose these forms for `FP1=mutual-provision`; I expect at most one of them to take it, and `avariz_vakfi` to be the likelier."

Half falsified. One takes it, but it is `bruderschaft_salzburg`.

> "I expect `LR4` to be the hardest cell on both rows"

Falsified for `bruderschaft_salzburg`, where the author's own analysis settles it. It held for `avariz_vakfi`.

> "Non-independence: I expect Küçük 2025 to cite Kars and/or Kıvrım, and at least two of the three local studies to share an upstream (Barkan, Çizakça, Yediyıldız, Özcan, or Bulut on avarız vakıfları); Gürsoy is a different record type and the likeliest independent witness."

Partly falsified. Küçük cites Kıvrım, but not Kars. The shared upstream is İpşirli's DİA entry, Akgündüz and Ergin, not the names I guessed. The real dependence is stronger than I expected: Kars copies Kıvrım's text wholesale. Gürsoy is independent, as expected, and so is Küçük's primary data.

> "Sub-pool: … I put roughly even odds on the sources' own enumeration making it a sub-pool form."

Resolved: it is a sub-pool form in Ayntab (Kıvrım 39, 45–47).

**The pattern across the falsifications:** my priors put `0` on characteristics the sources never address: `CI3`, `CI4`, `FP2` and `FP3` on both forms, and `CI2` on the Bruderschaft. Every one came back `.NR`. My priors converted expected silence into absence, which is the error the missingness rule exists to prevent. The priors named the fallback in most cases. Confirmed expectations include every entity-shielding and owner-shielding `.NR`, `AP4`, `TS1`, `TS2`, `FP4` (best-evidenced, as predicted) and `MG1`–`MG3` on both forms.

**4. Characteristics that did not fit the evidence.**
- `LR4` on `avariz_vakfi`: the fund's main draw is a common levy, a covariate burden on every household at once. Its secondary lines, the poor's levy, poor funerals and a fire loan, meet member-specific hazards. The value set asks one question of a fund doing both. `P` is coded as a structural half; it is not a hedge.
- `LR4` on `bruderschaft_salzburg`: the definition is silent on whether a spiritual hazard counts.
- `MG2` on `bruderschaft_salzburg`: the row spans two subtypes and a c.1785 break. A split is proposed (§6).
- `MG4` on `avariz_vakfi`: the value set forces fiqh against custom, while the source says the fiqh authorisation itself rested on *örf* (Küçük 149–151).
- `AP4`: the locator reads as one founder, but the avarız corpus is built by many founders cumulatively. I applied it donor by donor.
- `CI1`: cannot record the Ayntab bölük partition. On the sub-pool rule this is carried in notes.

**5. Dependence or well-formedness problems noticed and not repaired.**
- Kars copies Kıvrım (§2). Cells citing both carry one witness, and their notes say so.
- The three local studies share the İpşirli, Akgündüz and Ergin upstream.
- Kars's year (2020 vs 2021) is not repaired.
- Dependence chains that rest on low-confidence antecedents: `avariz_vakfi` `LR6=.NA` rests on `LR2=veiled` (low); `AP3` and `LR1` take the members locator from `CF1=0` (low), though both are `.NR` under either locator; `LR5` on both forms rests on `LR4`≠0.
- The type rows and the OF-0644–0707 data rows are absent from the bundle, so the `recodings` foreign key fails there by construction (§10).
- The `recodings` schema does not constrain `(record_id, type_id, char_id)` to agree with `data.csv`, so a mismatched triple would pass. I cannot test it in the bundle.
- The Project-attachment channel (§7 item 6).
- The unobservable effort setting.
- The Klieber text-layer claim in logbook 2 is false for this file.

**6. What to acquire next, and which cell it would move.**
- **For `bruderschaft_salzburg`, an independent second author on Salzburg or South-German fraternities.** This matters most, because every cell rests on one witness. It would test `LR4=1` and `FP1=mutual-provision`, which carry the row's mutual-pole claim.
- **Klieber's 1999 monograph**, the Habilitationsschrift that the 2001 article distils: *Bruderschaften und Liebesbünde nach Trient. Ihr Totendienst, Zuspruch und Stellenwert im kirchlichen und gesellschaftlichen Leben am Beispiel Salzburg (1600–1950)*, Frankfurt am Main: Peter Lang, 1999, 634 pp. The citation is as Klieber 2001 gives it in its first note. It is the same author, so it deepens and does not add a witness. It could move `LP1`, `LP3`, `AP1`–`AP3`, `CI2`, `LR2`/`LR6` and `TS3` off `.NR`, and settle the `MG2` split.
- **For `avariz_vakfi`, İpşirli's DİA entry "Avarız Vakfı"**, the shared upstream. It would let `TS4`'s general claim be judged at source, and could lift it from low or move it to 1.
- **Akgündüz's treatment of the dead debtor (228–229)**, which bears on the `AP1`-adjacent priority question.
- **A study of avarız fund accounts.** Candidates:
  - Çiftçi, "Osmanlı'da Mahalle Avarız Vakıfları: Bursa Örneği (1749–1784)", cited by Kars and by Küçük. It is an avarız-specific study from a fourth city.
  - Koyunoğlu 2008, "Para Vakıfları: Muhasebe Defterlerine Göre 17. yy İstanbul Uygulaması", *Din Bilimleri Akademik Araştırma Dergisi* 8/1, 253–303, cited by Gürsoy. This is on cash waqfs generally.
  - Özdemir 1998, on Ankara, cited by Kars.

  These would move `LR2`, and with it `LR6`, if trustees are shown to bear losses. They would also address `TS3` and `AP2`'s creditor limb, if a fund is ever shown indebted. The citations are as the sources give them; none has been checked against a catalogue, since no source-finding tool was allowed.

## 10. Checks

The commands run and their output are recorded in `NOTES-opus55-recode-mutual-pole-postfreeze-2026-09-26.md`. They were run after this file was written.
