# Priors — opus55-recode-mutual-pole-2026-09-26

**Written by the coding chat (Claude Opus 5.5, effort high) BEFORE any file in `sources/` was opened.** MS commits this file after it is filled and before the coder opens a source; the commit, not the file's mtime, is the evidence of ordering. The coder quotes this file verbatim in answer 3.

- Filled by: Claude, coding chat (Chat B), in a Cowork session. Model identifier as configured for the session: `claude-opus-5-5`. Effort: the kickoff specifies `high`; I cannot confirm the session's effort setting from inside the session, so `coder_effort=high` rests on the kickoff and not on anything I can observe.
- Finished at (UTC): 2026-09-26 13:33 UTC
- Files read before writing this (list them): `HistorEE_codebooks/CLAUDE.md`; `CONTRIBUTING.md`; `CHARACTER-CODING.md`; `EDITING-CSV.md`; `logbook/README.md` and logbooks 1–6 in full (whitespace-squeezed copies, read end to end); `vocabularies/organizational_form_characteristic.csv` in full (every field of all 32 rows); `vocabularies/organizational_form_type.csv` (code, name, tradition, period of all 42 rows; `key_source` not read except where a term grep surfaced a fragment, below); `datasets/organizational_forms/datapackage.json` (both resources' schemas); `datasets/organizational_forms/recodings.csv` (header only; empty); `datasets/organizational_forms/data.csv` — field distributions over the whole file, and the full rows of `waqf_khayri`, `begijnhof` and `nacion_cofradia` with notes truncated to 160 characters, as house practice; this priors template. Also the `code-a-form` and `run-a-coding-batch` skills (loaded in the session). Also a whole-bundle term-count grep, excluding `sources/`, for: avarız/avariz, Bruderschaft, Salzburg, Klieber, Liebesbund, Kars 20, Küçük, Kastamonu, Ayntab, Gürsoy, Kıvrım, mahalle, fraternit, withheld — which printed some 200-character contexts from `vocabularies/loss_mitigation_type.csv` (see exposure section). `myfoamrepo/` was NOT opened: no note, no filename beyond the top-level directory listing the first `find` printed (it listed file paths under `myfoamrepo/`, including note titles under `notes/` up to the alphabetical point "Flows make the dynamic affine…" — none of the titles printed names either form or Salzburg, avarız, confraternity or waqf). No source file opened; `ls -la sources/` only (file names and sizes).

## Exposure disclosed before any source was opened

This is recorded here, and not only in the coding notes, because it is information I held when writing the priors below and the priors cannot be read fairly without it. None of it is a source and none of it will found a cell.

1. **`AP4` definition, `organizational_form_characteristic.csv`:** "(COUNT CORRECTED 2026-09-08. This read 'two coded forms' from 2026-08-30 until today. [withheld 2026-09-26: the count names a form under blind re-coding.] … a third form at the same value adds a case and not a state, and AP4 still has one value across the column." Read with the definition's opening ("on present coding AP4 has THREE coded forms and one value between them"), this implies that **one of the two forms under test carries `AP4=1` in the live file.** I cannot tell which.
2. **Entity-locator definitions (`LP1`–`LP3`, `AP1`, `AP2`, `MG4`, `FP2`, `FP4`):** the 2026-09-06 sub-pool re-run at 803 rows lists "Sub-pool: … and [withheld 2026-09-26: one further form, under blind re-coding]. Not sub-pool: [withheld 2026-09-26: one form under blind re-coding]". Logbook 1, 2026-09-06, says five forms were added between 643 and 803 rows; three are named (`deed_of_settlement_company`, both `compagnie_antwerpen`). **So the operator's audit found exactly one of the two forms under test to be a sub-pool form and the other not.** I cannot tell which.
3. **Logbook 4, 2026-09-07 entry ("Four empty values were available and refused"), written at 801 rows, which include both forms:** `TS4=1`, `MG3=P`, `LR2=attenuated`, `LR4=P` and `LR1=none` "had no instance". **So neither form carries `LR4=P`, `TS4=1`, `MG3=P`, `LR2=attenuated` or `LR1=none` in the live file.** Logbook 4, 2026-09-05 (ii), at 707 rows (including both forms): `TS1=P` was zero-instance, and `LP3=0`, `AP2=P` and `FP4=0` were one-instance values held by other named forms — so neither form carries those either. The same entry lists `AP1=0`, `CI1=none`, `LR5=synchronising`, `MG2=founder-fixed`, `FP1=mutual-provision` and `CF2=P` as one-instance values without naming the holder; I have NOT checked the bundle's `data.csv` to see which of these vanish from it, and will not before coding.
4. **`loss_mitigation_type.csv`, confraternity umbrella row (line 9), by grep context:** "The regional limit added on 2026-08-13 from Klieber 2001 concluded: 'this cannot be one row for Latin Christendom. When coded it must be split regionally…'" and "the entity census now carries the parallel umbrella confraternita, uncoded …, with one coded child [withheld 2026-09-26: form under blind re-coding]". Logbook 2, 2026-08-13, beside withheld passages: "a form whose relief is a tenth of outgoings in one house in one decade would carry `MC1` only by straining it", and "the PDF's text layer is column-interleaved to the point of unreliability — the passages above were legible, the *Beitragssätze* and *Armenklauseln* discussions were not". **I read this as a prior session's characterisation of Klieber 2001: relief a small share of outgoings, and a hard text layer.** The kickoff says every file has a working text layer; I will test that rather than assume either.
5. **`loss_mitigation_type.csv` line 53 (a parked cash-waqf row), by grep context:** "Bursa's own avarız-ı mahalle funds are in his dataset with capital figures across 1078-1239 AH". **Logbook 4, 2026-08-19 (iii)/(iv) and the untitled entry above it**, around withheld passages about an Ottoman fund row in the loss census: "The fund is allocation and the pooling sits behind it — in the residual tax the fund fails to cover. The pooled thing is the shortfall, not the fund"; "Residents electing the mütevelli and the mütevelli lending to himself are compatible facts"; "`RB3` gains a fifth attestation of the *rehn-i kavî / kefîl-i melî* formula, Ayntab now"; "`PR1` … Ayntab's own endowments let at twenty"; "Kars's clause is not discarded — it is unsourced to any deed"; "The sentence `MC1`'s original `pooling` rested on appears **verbatim in both, with the city swapped**" followed by "Before counting two sources as agreeing, check whether the later one cites the earlier." **So a prior session read at least Kars and Kıvrım for a loss-census sibling of `avariz_vakfi`, found election of the mütevelli by residents, found the fund lending on pledge and surety, and found that two of the Turkish sources share a sentence.** Logbook 5, 2026-08-19: "Kars `GAZN2XVN` — Zotero dates it 2020; the running head reads *TAD* C.40/S.69, **2021**, 160–187."
6. **The chat itself.** This coding chat is attached to the claude.ai Project for HistorEE, whose document list (titles only, supplied by the platform) includes `claude/opus55-recode-mutual-pole-operator-2026-09-26.md`, `claude/recode-mutual-pole-operator-prompt-2026-09-26.md` and `claude/recode-plan-2026-09-26.md`. **I have not opened any Project document, the Project knowledge search, or any memory file other than the platform-supplied profile/preferences summary**, which says nothing about either form. The titles state no value. But the kickoff asked for a fresh chat with one folder, and a Project attachment is a channel the kickoff did not anticipate; MS should decide whether that matters.

## General expectations

**`avariz_vakfi`.** Four Turkish local and archival studies of *avarız akçesi vakıfları* / *avarız vakıfları*: Istanbul court records (Kars), Kastamonu (Küçük), Ayntab (Kıvrım), and the Evkaf Muhasebeciliği registers (Gürsoy). I expect them to answer, richly: who endowed (residents, individually and collectively, in cash and some real property), the declared purposes (paying the *avarız-ı divaniye* and *tekâlif-i örfiye* on behalf of the quarter's households, often with pious and communal lines — imam, müezzin, water, lamps, the poor, funerals), the capital and its lending (*muamele-i şer'iyye*, *istiğlal*, stipulated rates around 10–15 per cent, *rehin* and *kefil*), the *mütevelli* and how he was chosen, accounting and audit before the *kadı* or the Evkaf muhasebe, and the fund's decline. I expect them NOT to answer legal personality as doctrine, creditor priority in the fund, liability of residents to the fund's creditors, or transferability — they are fiscal and social histories, and the fund is a lender, not a debtor. So I expect the WP2 entity-shielding and owner-shielding components to come back almost entirely `.NR`, perpetual-succession and capital-lock-in to be coded, and the none-component governance cells to be the richest. I expect `FP4` to be the best-evidenced cell of the row, because three of the four sources are built out of registration and audit records. Sub-pool: I expect the arrangement to be the quarter's fund, possibly assembled from several donors' endowments that were sometimes accounted separately; I put roughly even odds on the sources' own enumeration making it a sub-pool form. Non-independence: I expect Küçük 2025 to cite Kars and/or Kıvrım, and at least two of the three local studies to share an upstream (Barkan, Çizakça, Yediyıldız, Özcan, or Bulut on avarız vakıfları); Gürsoy is a different record type and the likeliest independent witness.

**`bruderschaft_salzburg`.** One German source, Klieber 2001, a church historian on post-Tridentine confraternities in the archdiocese of Salzburg. I expect it to answer: numbers and growth of confraternities to a mass phenomenon; devotional types; membership open and very large, entry fees and dues; the spiritual benefits (indulgences, masses and prayers for deceased members — the *Liebesbund* as a bond of suffrage); finances (endowed masses, capital lent at interest), officers and clerical supervision; Josephinist/Bavarian-era suppression or amalgamation and nineteenth-century revival. I expect it NOT to answer any legal-personality, creditor or liability question. I expect relief of living members to be marginal against spiritual provision, which bears on `LR4` and `FP1`. Single witness throughout; nothing to test independence against.

**Across both.** The mutual-pole selection presumably chose these forms for `FP1=mutual-provision`; I expect at most one of them to take it, and `avariz_vakfi` to be the likelier. I expect `LR4` to be the hardest cell on both rows, because both funds meet a peril that is either covariate (a levy that falls on every household at once) or spiritual (the timing of one's death), and neither is clean mutualisation of an idiosyncratic hazard.

## `avariz_vakfi`

| char | expected value | confidence in that expectation | why |
|---|---|---|---|
| `LP1` | .NR | medium | Local fiscal histories rarely put the personhood question; if they do, waqf doctrine gives 0 (the `waqf_khayri` precedent). |
| `LP2` | P | low | Corpus held as waqf, ownership suspended, lent "from the vakıf" through the mütevelli — half-present on the `waqf_khayri` pattern; real chance of .NR. |
| `LP3` | P | low | Court-record studies should show the mütevelli suing defaulting borrowers on the fund's behalf: standing mediated by an officer. Could be .NR if only debt registrations appear. |
| `AP1` | .NR | medium | Creditor ranking in the fund is not a question these sources ask; the fund is a creditor, not a debtor. If asked, 1. |
| `AP2` | .NR | medium | Members' limb likely answered (residents cannot divide or withdraw the corpus), creditor limb not; one limb unevidenced gives .NR on the house rule. |
| `AP3` | .NR | high | Whether residents' estates answer to the fund's creditors will not be addressed. |
| `AP4` | 1 | medium | Funds constituted by endowment of identifiable donors' cash or property. Alternative .NA if the sources show the corpus arising by a levy or collection rather than endowment. (Exposure item 1 applies.) |
| `TS1` | 1 | high | Waqf perpetuity; funds outlive donors and residents. |
| `TS2` | open | high | Perpetual endowment. |
| `TS3` | .NR | medium | Revocability at will is unlikely to be discussed; if it is, 0 (waqf irrevocable). |
| `TS4` | P | low | Residents petitioning the kadı to redirect surplus to other communal needs; a change by internal decision needing external sanction. (Exposure item 3: live value is not 1.) |
| `CI1` | common | medium | One fund per quarter. Alternatives: none (the `waqf_khayri` reading of an endowed corpus) or several-accounts if donors' endowments were kept apart. |
| `CI2` | 1 | medium | Corpus inalienable; no resident or donor may withdraw. |
| `CI3` | 0 | low | Benefit tied to residence, not an alienable interest. Alternatives .NR, or P if the benefit is shown to run with the house. |
| `CI4` | 0 | low | As `CI3`; likely .NR in practice. |
| `LR1` | .NR | high | Residents' liability for the fund's third-party obligations will not be addressed. (Exposure item 3: live value is not none.) |
| `LR2` | .NR | medium | The mütevelli's exposure to outcomes is probably not discussed; if it is, veiled (salaried) or coupled through liability for negligent loss. |
| `LR3` | 0 | medium | No return proportional to any stake; relief is by household assessment, not by contribution. |
| `LR4` | P | low | The fund pays a levy that falls on every household at once (covariate) and partly relieves those who cannot pay; neither 0 nor clean mutualisation. (Exposure items 3 and 5: the live value is not P, and a prior session read the pooling as sitting in the residual tax rather than the fund.) |
| `LR5` | synchronising | low | If `LR4` is not 0: the levy strikes all households together. |
| `LR6` | .NR | medium | Follows `LR2` .NR. |
| `MG1` | beneficiary | medium | Residents' claim rests on the deed's designation of the quarter's households, on the `waqf_khayri` pattern. Alternative: membership, if residence is treated as membership. |
| `MG2` | collective | medium | Residents (ahali) choose or propose the mütevelli and account before the kadı. Alternative: founder-fixed. (Exposure item 5.) |
| `MG3` | .NA | medium | Follows `MG1=beneficiary`; if `MG1=membership`, then 0 or 1 on residence. |
| `MG4` | religious | medium | Constituted as waqf under fiqh before the kadı, on the `waqf_khayri` precedent. Alternative: customary. |
| `FP1` | mutual-provision | medium | A fund whose declared purpose is to meet the residents' own common obligations. Alternative: mixed, if the deeds carry pious lines alongside. |
| `FP2` | 0 | medium | No franchise; likely .NR if sources are silent. |
| `FP3` | 0 | low | No status or access arbitrage expected; .NR likely. |
| `FP4` | 1 | high | Registered in the şer'iyye sicilleri and audited in the Evkaf registers. |
| `CF1` | 0 | medium | Donors, residents and a salaried trustee; no capital–labour contract. Alternative .NA. |
| `CF2` | .NA | medium | Follows `CF1=0`. |
| `CF3` | multilateral | medium | Many donors and beneficiaries. Alternative .NA on the `waqf_khayri` precedent. |

## `bruderschaft_salzburg`

| char | expected value | confidence in that expectation | why |
|---|---|---|---|
| `LP1` | .NR | medium | A church historian is unlikely to put the personhood question; if he does, P (canonical erection, a *corpus* recognised by the ordinary). |
| `LP2` | P | low | Confraternities held and lent capital, but under parish or diocesan administration; 1 if Klieber has them owning in their own name, .NR if silent. |
| `LP3` | .NR | high | Litigation not expected. |
| `AP1` | .NR | high | Not asked. |
| `AP2` | .NR | high | Not asked; members may leave but take nothing, which is the members' limb only. |
| `AP3` | .NR | high | Members' liability for confraternity debts will not be addressed. |
| `AP4` | .NA | medium | No founder's patrimony: arises by erection and enrolment. Alternative 1 if particular confraternities are shown founded on a donor's endowment. (Exposure item 1 applies.) |
| `TS1` | 1 | high | Persists across members' deaths; centuries-long. |
| `TS2` | open | high | No term. |
| `TS3` | .NR | medium | Suppression by the ordinary or the state is a power of an outside party, not revocation "by a party" at will; likely .NR. |
| `TS4` | P | low | Statutes remodelled and confraternities converted (Liebesbund) with episcopal sanction. (Exposure item 3: live value is not 1.) |
| `CI1` | common | medium | One confraternity purse; several-accounts if endowed masses were accounted apart. |
| `CI2` | 1 | low | Dues and gifts not returnable; .NR if not addressed. |
| `CI3` | 0 | medium | Membership personal, not alienable. |
| `CI4` | 0 | medium | As `CI3`. |
| `LR1` | .NR | medium | Not addressed. (Exposure item 3: live value is not none.) |
| `LR2` | .NR | medium | Officers' exposure not addressed. |
| `LR3` | 0 | medium | Benefits (suffrages, indulgences) equal per member, not proportional to stake. |
| `LR4` | P | low | Masses and prayers for deceased members and funeral attendance mutualise a death-timing hazard in spiritual currency; material relief marginal. (Exposure items 3 and 4: live value is not P; a prior session read relief as a tenth of outgoings.) |
| `LR5` | diversifying | low | If `LR4` is not 0: deaths fall on members at different times (epidemics excepted). |
| `LR6` | .NR | medium | Follows `LR2`. |
| `MG1` | membership | high | Enrolment is the claim. |
| `MG2` | collective | low | Elected lay officers under a clerical *Präses*; alternative single-principal (priest-directed). |
| `MG3` | 0 | medium | Open enrolment is what makes a mass phenomenon. (Exposure item 3: live value is not P.) |
| `MG4` | religious | high | Canonical erection, episcopal approval, papal indulgences. |
| `FP1` | pious-charitable | medium | Devotional and suffrage purpose. Live alternatives: mutual-provision (suffrages for fellow members) and mixed. |
| `FP2` | 0 | medium | No franchise; .NR if silent. |
| `FP3` | 0 | low | .NR likely. |
| `FP4` | P | low | Legible through episcopal approval, visitations and state inventories rather than a register. |
| `CF1` | 0 | medium | Members alike. |
| `CF2` | .NA | medium | Follows `CF1=0`. |
| `CF3` | multilateral | high | Many members. |
