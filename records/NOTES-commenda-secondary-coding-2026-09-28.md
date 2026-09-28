# Coding notes — commenda-secondary-2026-09-28 (arm S, secondary sources only)

- Pass: `commenda-secondary-2026-09-28`. Coder: `ai`, `claude-opus-5-5`, effort `high`. Condition: `blind`. Date the values were fixed: 2026-09-28.
- Filename: the kickoff named this file `NOTES-commenda-secondary-coding-2026-09-28.md`. `proposed-of/` was empty when I wrote into it, so there was no collision to avoid.
- Deliverables in `proposed-of/`: `recodings-commenda-secondary-2026-09-28-organizational_forms.csv` (42 rows), `recodings-commenda-secondary-2026-09-28-loss_mitigation_forms.csv` (19 rows), this file, `LOGBOOK-DRAFT-commenda-secondary-2026-09-28.md`, `COMMIT-MSG-commenda-secondary-2026-09-28.txt`.

## Ordering, as it actually happened

1. I read the bundle's non-source files (README, all four doctrine files, both vocabularies in full, both schemas, scope, cells, templates) and loaded the `code-a-form` and `run-a-coding-batch` skills.
2. I wrote `PRIORS-commenda-secondary-2026-09-28.md` before opening any source. Its sha256 is `a2917ca57d266846a3204ec2210494dfd3768eb4db823d691c4e0fcc614c4b34`. MS committed it and confirmed that the committed copy (`git show HEAD:records/…`) has the same hash, and I opened no source until then. One disclosure: an earlier hash (`4b1c535d…`) was printed for a version whose "Finished at" line read 06:05Z. I corrected that line to 05:55Z before reporting; the committed hash is the corrected file's.
3. I read the six works in full, apart from van Doosselaere's bibliography and index, which I scanned for citations rather than read. The reading record is below.
4. I fixed all 61 cells and wrote the two CSVs, this file, the logbook draft and the commit message. I did this before computing anything about the matrix, and I have computed nothing since: no comparison with live values (I cannot see them), no similarity or distance measure, and no redundancy count over the dependence groups. The only checks I ran are schema validation on a scratch copy and a sweep of `value` against `allowed_values` (see Checks).
5. I did not run `git`, use the web, Zotero, Undermind or Elicit, or open the claude.ai Project or any memory file. Consequence: no DOI or citation below was checked against CrossRef, so every citation is **unverified** in the sense of `CLAUDE.md`. The one DOI printed on a source (Held 2025, `10.21857/yq32ohrvr9`) is copied from the PDF.
6. Deviation from the `run-a-coding-batch` skill: its final step, the session record in the claude.ai Project, was not written because the kickoff forbids opening the Project.

## Bundle status (code-a-form Step 0)

This is a blind bundle. It has no `data.csv`, vault or views, so the skills' steps that read comparative views or the vault did not apply, and I did not look outside the bundle. The known leaks and my exposure are listed in the priors under "Exposure", items B1–B13; nothing is added here. Reading the loaded skills against the forms under test: `code-a-form` names "commenda" only as an example (README leak 4). `run-a-coding-batch` contains no value for these forms, but it does name a vault title about "Harris 2020", which raises the citation ambiguity under answer 5. None of the six sources contained anything that looks like a census value.

## Reading record

Page offsets were measured against running heads and folios, not taken on trust.

| work | held file | pagination cited | offset measured |
|---|---|---|---|
| van Doosselaere, *Commercial Agreements and Social Dynamics in Medieval Genoa* (CUP 2009) | `vanDoosselaere2009.pdf`, 280 pp. | printed | printed = PDF − 18 (PDF 19 = p. 1; PDF 83 = p. 65; PDF 147 = p. 129). eBook reissue of the print typesetting ("First published in print format 2009"). |
| Harris, "The Institutional Dynamics of Early Modern Eurasian Trade: The Corporation and the Commenda", conference draft, USC, 23–24 Feb 2007 | `Harris2007_conference_draft.pdf`, 44 pp. | PDF page, as instructed | **The draft does carry page numbers.** Each page has a Word footer "Feb. 5, 07 … N", and N equals the PDF page on all 44 pages. So "PDF p. N" and the draft's own footer page N are the same number. The README's premise ("carries no printed page numbers") is false in the letter and harmless in effect. |
| Harris, "General Average and All the Rest: The Law and Economics of Early Modern Maritime Risk Mitigation" | `Harris2020.pdf`, 32 pp. | SSRN draft page | The file is the SSRN preprint (abstract 3799929; the footer reads "Electronic copy available at: https://ssrn.com/abstract=3799929"), with footer page numbers equal to the PDF page. It refers to other chapters "in this Volume" (forthcoming), so the published chapter's pagination is not in the bundle. Cited as "Harris 2020 (SSRN draft), p. N". |
| Held, "The Contract of Collegantia in the Late Medieval Law of Dubrovnik (Ragusa)", *Dubrovnik Annals* 29 (2025), 7–24 | `Held2025_ocr.pdf`, 19 pp. (1 cover + 18) | printed | printed = PDF + 5 (PDF 2 = p. 7; PDF 16 = p. 21). The prose OCR is clean. The figures' numbers are garbled, and none of them enters a cell. |
| Udovitch, "At the Origins of the Western Commenda: Islam, Israel, Byzantium?", *Speculum* 37 (1962), 198–207 | `Udovitch1962.pdf`, 11 pp. (JSTOR cover + 10) | printed | printed = PDF + 196 (PDF 2 = p. 198). |
| González de Lara, "Institutions for contract enforcement and risk-sharing: From the sea loan to the commenda in late medieval Venice", *European Review of Economic History* 6 (2002), 257–262 | `GonzalezdeLara2002.pdf`, 6 pp. | printed | printed = PDF + 256. The text layer drops every digit, so volume, pages and folios were read off rendered page images (pp. 257 and 259). It is a six-page **dissertation summary**, not an article. |

What each work bears on, with the cited pages:

- **van Doosselaere 2009.** Chapter 3 (pp. 61–117) is the core. It gives the contract's terms for both forms (p. 65), with the bilateral commenda "often called societas in Genoa" and "societas maris" listed as a distinct type (p. 14 n. 11). It shows the fixed payout rule (pp. 66–67) and counts single against multiple investors (p. 70 n. 11). It covers co-investor ties (p. 101), traveller autonomy and the breach exception (pp. 73–75), and failed ventures (p. 129). Chapters 4 and 5 contrast credit and insurance. The book is silent on legal personality, third-party liability, transferability, security and loss verification.
- **Harris 2007.** Pages 8–13 are a legal-economic anatomy of the "prototypical" commenda. It covers the investment, agency and risk terms (PDF 9–10) and the traveller's sole liability to third parties (PDF 10). PDF 11 is an asset-partition reading after Hansmann, Kraakman and Squire, with an "asymmetric entity shielding". PDF 12 gives the variants: the traveller investing a third, multilateral use, and sub-commendae. Also: voluntary contract (PDF 34), single venture (PDF 40). The rest is the corporation, the waqf and lineage estates, and migration.
- **Harris 2020.** The commenda is on pp. 25–27: bilateral, a 25–75 split, "the risks are split", a pricing reading of the shares that Harris himself calls under-determined, and the contract as a generator of information. Page 31 names the allocation/spreading/pooling triad without placing the commenda in it.
- **Held 2025.** This is Ragusan (Dubrovnik) law and practice, 1272–1301, so it falls **outside both rows' traditions** ("Italian (Latin)"; "Venetian / Genoese"). I used it only where it reports Venetian material: terminology (p. 9), the prevalence of the unilateral form (p. 10), Venetian profit shares (p. 11 n. 20), and the "ad periculum … maris et gentis clarefactum" formula as "common in Venetian documents" (p. 20). Otherwise it is cited as corroboration only.
- **Udovitch 1962.** Page 198 defines the Western commenda: no agent liability for sea or trade loss, no social capital, the investor not jointly liable with the agent towards third parties, and "an investor or group of investors". Pages 199–207 treat the analogues (ʿisqa, chreokoinōnia, qirāḍ); no Italian row is coded from them.
- **González de Lara 2002.** Venice. The commenda was enforced through state-generated verifiable information (pp. 258–259), and the "risk of sea and people" exemption applied "if this was clearly apparent" (p. 259). In this summary the "commenda" is the unilateral contract that prevailed by the 1220s.

## Non-independence found

- **Harris 2007 and Harris 2020 are one witness.** Harris 2020's commenda passage cites Harris, *Going the Distance* (2020), 130–70 (p. 25 n. 42), a third work by the same author.
- **Harris 2007 and Udovitch are not independent on legal features.** Harris names Udovitch (1970, *Partnership and Profit*) and Weber as "the most authoritative sources on the legal features" (PDF 8 n. 13). For origins he rests on Udovitch 1962 and 1970 and on Pryor 1977 (PDF 14 n. 19). Udovitch 1962 and 1970 are one scholar, hence one witness. So the AP3 evidence (Harris PDF 10–11; Udovitch 198) is at most one and a half witnesses.
- **Pryor 1977 (not held) is a shared upstream of three works.** van Doosselaere takes from it the equivalence of unilateral and bilateral (p. 65 n. 7), the parties as "socii" in the statutes (p. 66) and the traveller's limited liability in the qirāḍ comparison (p. 68). Harris 2007 uses it at PDF 14 n. 19, and Held on terminology at p. 7 n. 1 and p. 9 n. 10. The one statement founding societas_maris RB1/RB2/LR3 (van Doosselaere 65) therefore rests on Pryor.
- **Udovitch 1962 is cited by three of the others:** van Doosselaere 67–68, Harris 2007 PDF 14 n. 19, and Held p. 8 n. 3.
- **Held cites van Doosselaere 2009** (pp. 63–78; Held p. 8 n. 4) **and González de Lara.** Held cites González de Lara's 2000 dissertation (of which the bundle's 2002 piece is a summary), the 2008 *European Review of Economic History* article and a 2017 paper (Held pp. 7–8 nn. 2, 4; p. 10 n. 15; p. 12 n. 22; p. 20 n. 53). Held's statement that the "clarefactum" formula is "common in Venetian documents" cites González de Lara 2008, 252 (p. 20 n. 53). On the Venetian formula (RB1, VF1, VF2), Held and González de Lara are therefore partly one witness.
- **Shared data.** González de Lara (p. 259: "almost 1,000 notarial acts … transcribed … by Morozzo della Rocca and Lombardo, 1940 and 1953") and Held (p. 11 n. 20, counting Venetian profit shares in *Documenti* II) draw on the same Venetian edition.
- **Also cited:** Puga & Trefler 2014 (not held) by Held (p. 10 n. 14; p. 20 n. 52).
- **van Doosselaere's bibliography misdates Pryor 1977** as *Speculum* 51(4) with a garbled title ("commanda"). Harris 2007 gives *Speculum* 52(1), 5–37, and Held gives *Speculum* 52/1 (1977). Recorded, not resolved.

## Scope decisions

- **What "societas maris" refers to.** van Doosselaere lists "societas maris" as a contract type (p. 14 n. 11) and describes the bilateral commenda, "often called societas in Genoa" (p. 65). Held p. 9 (after Pryor) states that in Venetian documents *collegantia* designates the bilateral commenda exclusively. Together these support the type row's gloss. Harris 2007 treats the same contract as a "basic variant" of the commenda (PDF 12), and I coded it under societas_maris.
- **Ragusan evidence** (Held) does not found any cell on either row. Where it agrees, it is cited as corroboration and the note says so.
- **Harris 2007's "prototypical" commenda** is Eurasian, not specifically Italian. I used it for the Italian row because its legal terms are the Western commenda's as given by Udovitch 198 and van Doosselaere 65, and each note says whose.
- **source_class.** Every cited passage is a modern author's account. Where they quote clauses (van Doosselaere 70; González de Lara 259; Held 13, 20), the quotation sits inside the author's argument, which the schema classes as `secondary`. No passage I cite is an edited transcription printed as such, so no row is `mixed`. The kickoff's parenthesis ("`mixed`, if a passage you cite is an edited transcription of a document") and the schema's wording for a transcription in an appendix (`primary-transactional`) do not quite agree; nothing here tests the difference.

## Decision points (every cell, with the alternative reading)

The rationale for each value is in its row's `notes` field. This table gives the reading I rejected, so that an adjudicator can see the fork.

| recoding_id | census | type_id        | char_id | value                 | confidence | alternative reading                                                                                                                   |
|-------------|--------|----------------|---------|-----------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------|
| OF-R0065    | orga   | commenda       | TS2     | single-venture        | high       | none material; local time-bound commendae (vD 66 n.8) outside scope                                                                   |
| OF-R0066    | orga   | commenda       | AP3     | 0                     | medium     | .NR if Harris's HKS framing is discounted and Udovitch's implication is not read as a statement about the agent                       |
| OF-R0067    | orga   | commenda       | LR1     | unlimited-several     | low        | .NR with vocabulary flag ('sole' has no cell)                                                                                         |
| OF-R0068    | orga   | commenda       | LR2     | coupled               | high       | none                                                                                                                                  |
| OF-R0069    | orga   | commenda       | LR3     | 1                     | medium     | P, if 'proportionally to stake' is read strictly                                                                                      |
| OF-R0070    | orga   | commenda       | LR4     | 0                     | low        | .NR (no work puts the question)                                                                                                       |
| OF-R0071    | orga   | commenda       | LR5     | .NA                   | .NA        | follows LR4; .NR if LR4 is .NR                                                                                                        |
| OF-R0072    | orga   | commenda       | CF1     | 1                     | high       | none                                                                                                                                  |
| OF-R0073    | orga   | commenda       | CF2     | 0                     | high       | none (breach exception is conduct, not allocation)                                                                                    |
| OF-R0074    | orga   | commenda       | CF3     | bilateral             | medium     | multilateral (vD 70 n.11 minority; Udovitch 'group of investors')                                                                     |
| OF-R0075    | orga   | commenda       | LR6     | upside-only           | high       | none                                                                                                                                  |
| OF-R0076    | orga   | societas_maris | TS2     | single-venture        | high       | none                                                                                                                                  |
| OF-R0077    | orga   | societas_maris | AP3     | .NR                   | .NR        | 0 carried from commenda via vD's 'essentially the same agreement' (rejected)                                                          |
| OF-R0078    | orga   | societas_maris | LR1     | .NR                   | .NR        | unlimited-several carried from commenda (rejected)                                                                                    |
| OF-R0079    | orga   | societas_maris | LR2     | coupled               | high       | none                                                                                                                                  |
| OF-R0080    | orga   | societas_maris | LR3     | 1                     | high       | none                                                                                                                                  |
| OF-R0081    | orga   | societas_maris | LR4     | 0                     | low        | .NR; or P if pro-rata co-investment is read as pooling                                                                                |
| OF-R0082    | orga   | societas_maris | LR5     | .NA                   | .NA        | follows LR4                                                                                                                           |
| OF-R0083    | orga   | societas_maris | CF1     | P                     | medium     | 1 (labour one-sided)                                                                                                                  |
| OF-R0084    | orga   | societas_maris | CF2     | 0                     | medium     | P (traveller bears part of the venture's capital loss)                                                                                |
| OF-R0085    | orga   | societas_maris | CF3     | bilateral             | low        | .NR; the type-row gloss 'bilateral commenda' is not evidence of principal count                                                       |
| OF-R0086    | orga   | societas_maris | LR6     | symmetric             | high       | none                                                                                                                                  |
| OF-R0087    | orga   | commenda       | LP1     | .NR                   | .NR        | 0 by inference from 'nexus of contracts' (not made)                                                                                   |
| OF-R0088    | orga   | commenda       | LP2     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0089    | orga   | commenda       | LP3     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0090    | orga   | commenda       | AP1     | P                     | low        | .NR (Harris hedges; limb unstated) or 0/.NA on Udovitch's 'no social capital'                                                         |
| OF-R0091    | orga   | commenda       | AP2     | .NR                   | .NR        | P on the creditor limb alone (rejected: one limb unevidenced)                                                                         |
| OF-R0092    | orga   | commenda       | AP4     | .NA                   | .NA        | none                                                                                                                                  |
| OF-R0093    | orga   | commenda       | CI1     | none                  | low        | common (Harris 2007) or several-accounts (vD 103) or .NR                                                                              |
| OF-R0094    | orga   | commenda       | CI2     | .NR                   | .NR        | 1 by inference from voyage-bound duration (not made)                                                                                  |
| OF-R0095    | orga   | commenda       | CI3     | .NR                   | .NR        | 0 by inference (not made)                                                                                                             |
| OF-R0096    | orga   | commenda       | CI4     | .NR                   | .NR        | 0 by inference (not made)                                                                                                             |
| OF-R0097    | orga   | societas_maris | LP1     | .NR                   | .NR        | 0 by inference (not made)                                                                                                             |
| OF-R0098    | orga   | societas_maris | LP2     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0099    | orga   | societas_maris | LP3     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0100    | orga   | societas_maris | AP1     | .NR                   | .NR        | P carried from commenda (rejected)                                                                                                    |
| OF-R0101    | orga   | societas_maris | AP2     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0102    | orga   | societas_maris | AP4     | .NA                   | .NA        | none                                                                                                                                  |
| OF-R0103    | orga   | societas_maris | CI1     | common                | medium     | .NR                                                                                                                                   |
| OF-R0104    | orga   | societas_maris | CI2     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0105    | orga   | societas_maris | CI3     | .NR                   | .NR        | none                                                                                                                                  |
| OF-R0106    | orga   | societas_maris | CI4     | .NR                   | .NR        | none                                                                                                                                  |
| LM-R0001    | loss   | commenda_alloc | MC1     | allocation            | high       | none on the evidence; not blind                                                                                                       |
| LM-R0002    | loss   | commenda_alloc | MB3     | voluntary             | high       | none                                                                                                                                  |
| LM-R0003    | loss   | commenda_alloc | RB1     | capital-provider      | medium     | shared (Udovitch 198; Harris 2020, 26 count the agent's labour at risk)                                                               |
| LM-R0004    | loss   | commenda_alloc | RB2     | capital-provider      | medium     | shared, as RB1                                                                                                                        |
| LM-R0005    | loss   | commenda_alloc | RB3     | .NR                   | .NR        | none (priors' general knowledge) or personal/general-estate (no passage)                                                              |
| LM-R0006    | loss   | commenda_alloc | RB4     | 1                     | high       | none                                                                                                                                  |
| LM-R0007    | loss   | commenda_alloc | PR1     | 0                     | medium     | P or 1 on Harris 2020's Knightian reading (analyst-imposed by rule)                                                                   |
| LM-R0008    | loss   | commenda_alloc | PY0     | .NA                   | .NA        | .NR                                                                                                                                   |
| LM-R0009    | loss   | commenda_alloc | VF1     | official-adjudication | low        | documentary (Harris 2020, 26-27); or .NR                                                                                              |
| LM-R0010    | loss   | commenda_alloc | VF2     | mixed                 | medium     | loss-occurrence only, if the Ragusan fault clause is set aside and Harris's breach standard read as conduct outside loss verification |
| LM-R0011    | loss   | societas_maris | MC1     | allocation            | low        | pooling (pro-rata sharing among stakeholders with no outsider)                                                                        |
| LM-R0012    | loss   | societas_maris | MB3     | voluntary             | medium     | none                                                                                                                                  |
| LM-R0013    | loss   | societas_maris | RB1     | shared                | medium     | none; 'all-stakeholders' is equivalent for two parties                                                                                |
| LM-R0014    | loss   | societas_maris | RB2     | shared                | medium     | as RB1                                                                                                                                |
| LM-R0015    | loss   | societas_maris | RB3     | .NR                   | .NR        | none                                                                                                                                  |
| LM-R0016    | loss   | societas_maris | RB4     | 1                     | medium     | .NR (no passage on total loss of a societas as such)                                                                                  |
| LM-R0017    | loss   | societas_maris | PR1     | 0                     | medium     | none                                                                                                                                  |
| LM-R0018    | loss   | societas_maris | PY0     | .NA                   | .NA        | .NR                                                                                                                                   |
| LM-R0019    | loss   | societas_maris | VF1     | .NR                   | .NR        | official-adjudication carried from commenda_alloc (rejected)                                                                          |

## Coverage by component

| census | type_id        | component            | substantive | .NR | .NA | cells           |
|--------|----------------|----------------------|-------------|-----|-----|-----------------|
| loss   | commenda_alloc | loss-sharing         | 2           | 0   | 0   | RB1 RB2         |
| loss   | commenda_alloc | none                 | 2           | 0   | 0   | VF1 VF2         |
| loss   | commenda_alloc | owner-shielding      | 1           | 1   | 0   | RB3 RB4         |
| loss   | commenda_alloc | risk-pooling         | 3           | 0   | 1   | MC1 MB3 PR1 PY0 |
| loss   | societas_maris | loss-sharing         | 2           | 0   | 0   | RB1 RB2         |
| loss   | societas_maris | none                 | 0           | 1   | 0   | VF1             |
| loss   | societas_maris | owner-shielding      | 1           | 1   | 0   | RB3 RB4         |
| loss   | societas_maris | risk-pooling         | 3           | 0   | 1   | MC1 MB3 PR1 PY0 |
| orga   | commenda       | capital-lock-in      | 0           | 1   | 0   | CI2             |
| orga   | commenda       | entity-shielding     | 1           | 1   | 1   | AP1 AP2 AP4     |
| orga   | commenda       | legal-personality    | 0           | 3   | 0   | LP1 LP2 LP3     |
| orga   | commenda       | loss-sharing         | 2           | 0   | 0   | LR3 CF2         |
| orga   | commenda       | none                 | 3           | 0   | 0   | CF1 CF3 CI1     |
| orga   | commenda       | outcome-coupling     | 2           | 0   | 0   | LR2 LR6         |
| orga   | commenda       | owner-shielding      | 2           | 0   | 0   | AP3 LR1         |
| orga   | commenda       | perpetual-succession | 1           | 0   | 0   | TS2             |
| orga   | commenda       | risk-pooling         | 1           | 0   | 1   | LR4 LR5         |
| orga   | commenda       | transferable-claims  | 0           | 2   | 0   | CI3 CI4         |
| orga   | societas_maris | capital-lock-in      | 0           | 1   | 0   | CI2             |
| orga   | societas_maris | entity-shielding     | 0           | 2   | 1   | AP1 AP2 AP4     |
| orga   | societas_maris | legal-personality    | 0           | 3   | 0   | LP1 LP2 LP3     |
| orga   | societas_maris | loss-sharing         | 2           | 0   | 0   | LR3 CF2         |
| orga   | societas_maris | none                 | 3           | 0   | 0   | CF1 CF3 CI1     |
| orga   | societas_maris | outcome-coupling     | 2           | 0   | 0   | LR2 LR6         |
| orga   | societas_maris | owner-shielding      | 0           | 2   | 0   | AP3 LR1         |
| orga   | societas_maris | perpetual-succession | 1           | 0   | 0   | TS2             |
| orga   | societas_maris | risk-pooling         | 1           | 0   | 1   | LR4 LR5         |
| orga   | societas_maris | transferable-claims  | 0           | 2   | 0   | CI3 CI4         |

Totals: 35 substantive, 20 `.NR`, 6 `.NA` (61 cells).

- **Components that learned nothing, on either row:** legal-personality (LP1–LP3), capital-lock-in (CI2) and transferable-claims (CI3–CI4).
- **Entity-shielding** has one substantive cell (commenda AP1 = P, low), resting on one hedged witness.
- **Owner-shielding** is coded for the commenda (AP3, LR1) and not for societas_maris.

## Six answers

### 1. What was coded, and on what evidence

- **Overall:** 35 substantive cells, 20 `.NR` and 6 `.NA` out of 61. The per-component count is in the coverage table above. Every substantive cell rests on a modern author's account (`source_class` = `secondary`). Two are `articulated`: commenda `CF1`, on the receipt clause quoted by van Doosselaere 70, and commenda_alloc `RB1`, on the "ad periculum … maris et gentis" formula (Held 20; González de Lara 259).
- **commenda (organizational_forms), from van Doosselaere, Harris 2007 and Udovitch:**
  - The contract: `TS2` single-venture, `CF1` 1, `CF2` 0, `LR2` coupled, `LR6` upside-only, `LR3` 1.
  - `CF3` bilateral, on the modal instance.
  - `LR4` 0, with `LR5` .NA following from it.
  - The owner-shielding pair: `AP3` 0 and `LR1` unlimited-several (low). This rests on Harris PDF 10–11 and Udovitch 198, which are not independent of each other.
  - `AP1` P (low), on Harris's hedged Hansmann–Kraakman–Squire reading alone.
  - `CI1` none (low), on Udovitch against Harris.
- **societas_maris (organizational_forms), almost wholly on one page of van Doosselaere (65, 66–67):** `TS2`, `LR2` coupled, `LR3` 1, `LR6` symmetric, `CF1` P, `CF2` 0, `CI1` common and `LR4` 0, plus `CF3` bilateral (low).
- **commenda_alloc:**
  - `MC1` allocation. Not blind.
  - `MB3` voluntary (Harris PDF 34).
  - `RB1` and `RB2` capital-provider, `RB4` 1 (Harris, van Doosselaere, Udovitch, González de Lara).
  - `PR1` 0, on van Doosselaere's fixed-payout evidence, with Harris 2020 dissenting.
  - `VF1` official-adjudication (low) and `VF2` mixed, on González de Lara and Held.
- **societas_maris (loss_mitigation_forms):** `MC1` allocation (low), `MB3` voluntary, `RB1` and `RB2` shared, `RB4` 1 and `PR1` 0, all from van Doosselaere 65–67 and 129.

### 2. What could not be coded, and why

- **Legal personality (LP1–LP3), both rows: `.NR`.** No work states the arrangement's legal status. Harris 2007 discusses legal personality only for the corporation and the waqf. The inference to 0 that general knowledge supplies was not made.
- **Entity shielding.**
  - commenda `AP2`: `.NR`. The members' limb is unevidenced for the Italian contract, and the creditor limb points against.
  - societas_maris `AP1` and `AP2`: `.NR`. Harris's pool analysis covers the basic commenda only.
- **Capital lock-in and transferability (CI2–CI4), both rows: `.NR`.** No passage on recall before return or on alienating an interest.
- **societas_maris `AP3` and `LR1`: `.NR`.** No work states third-party liability in the bilateral contract. van Doosselaere's "essentially the same agreement" (65 n. 7, after Pryor) is not a statement about venture creditors.
- **`RB3`, both loss rows: `.NR`.** No work names any security for the invested capital.
- **societas_maris `VF1`: `.NR`.** González de Lara's verification evidence concerns the unilateral Venetian contract.
- **`.NA` (applicability or locator):** `LR5` on both rows (LR4 = 0), `AP4` on both rows (no founder), and `PY0` on both loss rows (no pool).
- **Three cited works are not held:** Pryor 1977, Puga & Trefler 2014, and Merelo-Guervós & Molinari 2025. Nothing was reconstructed from them. Pryor is the upstream of the societas_maris statements, so its absence caps confidence there.

### 3. Expectations of mine that the sources falsified (priors quoted verbatim)

- `commenda` `AP3` — prior:

  > | orga   | `commenda`       | `AP3`   | .NR              | medium     | Locator is the traveller and venture creditors; I expect sources to speak of the investor's limited liability only, which the definition makes .NR. GK: 0 (traveller personally liable to those he dealt with). |

  value: expected `.NR`; coded `0` (medium). Harris 2007 PDF 10-11 and Udovitch 198 address the traveller's liability to venture creditors. Falsified towards a stronger claim.

- `commenda` `LR1` — prior:

  > | orga   | `commenda`       | `LR1`   | .NR              | medium     | As AP3. GK: traveller's liability unlimited; the value set's joint/several split is moot for one agent.                                                                                                         |

  value: expected `.NR`; coded `unlimited-several` (low). Same pages.

- `commenda` `AP1` — prior:

  > | orga   | `commenda`       | `AP1`   | .NR              | high       | No source I expect asks creditor priority in commenda assets.                                                                                                                                                   |

  value and confidence: expected `.NR`, high ("No source I expect asks creditor priority"); Harris 2007 PDF 11 asks it, and I coded `P` (low).

- `commenda` `CI1` — prior:

  > | orga   | `commenda`       | `CI1`   | .NR              | low        | GK: none or common; the value set fits a one-sided capital advance badly. Possible vocabulary misfit.                                                                                                           |

  value: expected `.NR`; the sources answer it, and conflict (Udovitch 198 against Harris PDF 11-12). Coded `none` (low).

- `commenda` `LP1` — prior:

  > | orga   | `commenda`       | `LP1`   | .NR              | low        | Harris 2007 may deny personality in terms (then 0). GK: 0.                                                                                                                                                      |

  value confirmed (`.NR`), rationale falsified: Harris 2007 does not deny personality in terms.

- `societas_maris` `CI1` — prior:

  > | orga   | `societas_maris` | `CI1`   | .NR              | low        | GK: common (capital of both parties combined in one venture); a source stating the combination would give common.                                                                                               |

  value: expected `.NR`; van Doosselaere 65 states the joined capital. Coded `common` (medium).

- `societas_maris` `CF3` — prior:

  > | orga   | `societas_maris` | `CF3`   | bilateral        | high       | Type row name; leak B2.                                                                                                                                                                                         |

  confidence: expected `bilateral`, high "Type row name; leak B2". Coded `bilateral`, low: the name refers to two-sided contribution, not principal count.

- `commenda_alloc` `MB3` — prior:

  > | loss   | `commenda_alloc` | `MB3`   | voluntary        | medium     | A private contract; but no source may say so in terms, in which case it is analyst-imposed.                                                                                                                     |

  confidence: expected medium ("no source may say so in terms"); Harris 2007 PDF 34 says so in terms. Coded high.

- `commenda_alloc` `RB1` — prior:

  > | loss   | `commenda_alloc` | `RB1`   | capital-provider | high       | Capital at the investor's risk of sea and people.                                                                                                                                                               |

  confidence: expected high; coded medium (Udovitch 198 and Harris 2020, 26 describe the risks as shared).

- `commenda_alloc` `RB3` — prior:

  > | loss   | `commenda_alloc` | `RB3`   | none             | low        | The capital is entrusted, not advanced against security. Alternative .NR if no source addresses security, or personal if the traveller's estate answers for the capital.                                        |

  value: expected `none`; no work addresses security. Coded `.NR`. My "none" was general knowledge.

- `commenda_alloc` `RB4` — prior:

  > | loss   | `commenda_alloc` | `RB4`   | 1                | medium     | Traveller owes nothing if goods lost at sea without fault. Could be .NR if not stated for the Italian contract.                                                                                                 |

  confidence: expected medium ("Could be .NR if not stated for the Italian contract"); it is stated four times. Coded high.

- `commenda_alloc` `VF1` — prior:

  > | loss   | `commenda_alloc` | `VF1`   | .NR              | low        | Held may give the Ragusan rule (oath / witnesses / documents); scope then disputed. GK: unknown.                                                                                                                |

  value: expected `.NR`; González de Lara 258-259 (not Held, as I predicted) gives a mode. Coded `official-adjudication` (low).

- `commenda_alloc` `VF2` — prior:

  > | loss   | `commenda_alloc` | `VF2`   | .NR              | low        | If VF1 is coded, claimant-fault or mixed (loss occurred and without the traveller's fault).                                                                                                                     |

  value: expected `.NR`; coded `mixed` (medium).

- `societas_maris` `MC1` — prior:

  > | loss   | `societas_maris` | `MC1`   | allocation       | medium     | Leak B5 possibly names this row. GK is less sure here: pro-rata sharing between two stakeholders could be read as pooling. Alternative pooling.                                                                 |

  confidence: expected medium; coded low (no work classifies the contract).

- `societas_maris` `RB1` — prior:

  > | loss   | `societas_maris` | `RB1`   | shared           | high       | Loss pro rata to capital contributed.                                                                                                                                                                           |

  confidence: expected high; coded medium (one statement, resting on Pryor, not held).

- `societas_maris` `RB2` — prior:

  > | loss   | `societas_maris` | `RB2`   | shared           | high       | As RB1.                                                                                                                                                                                                         |

  confidence: expected high; coded medium (as RB1).

- `societas_maris` `RB3` — prior:

  > | loss   | `societas_maris` | `RB3`   | none             | low        | As commenda_alloc.                                                                                                                                                                                              |

  value: expected `none`; coded `.NR`.

- `societas_maris` `RB4` — prior:

  > | loss   | `societas_maris` | `RB4`   | 1                | low        | Traveller's obligation to return the investor's two-thirds extinguished by total loss without fault. Could be .NR.                                                                                              |

  confidence: expected low; coded medium.

- Expectation about the works:

  > - **Harris 2020** ("General Average and All the Rest"). Should place the commenda in a typology of maritime loss devices: `MC1`, `RB1`, `PR1`, maybe `RB4`. Same author as Harris 2007: one witness where they overlap.

  Falsified: Harris 2020 does not place the commenda in the triad (p. 31), and MC1 got nothing from it. It did bear on PR1, as a dissent, and on RB1.

- Expectation about the works:

  > - **González de Lara 2002.** The file is 41 kB, which suggests an abstract or a very short text. If it is substantial it bears on Venetian enforcement and on the *colleganza*'s risk-sharing (`RB1`, `RB2`, `LR3`, maybe `VF1`). I expect little.

  Falsified: it is a 6-page dissertation summary, and it carried commenda_alloc VF1, RB1 and RB4 and part of VF2.

- Expectation about the works:

  > - **Held 2025** (Ragusa, *collegantia*). Likely to state the statute's rules on loss, proof and accounting: the one source I expect to reach `VF1`/`VF2` and perhaps `RB3`/`RB4`. Scope risk: Ragusan law is neither Genoese nor Venetian, and the type rows' tradition fields say Italian / Venetian / Genoese. Whether a Ragusan rule may code a Venetian row is an adjudication I will have to put to MS. Its quoted statute and contract clauses are primary texts reached through a secondary work, so `source_class` may be `mixed` there.

  Partly falsified: Held reached VF2 (the culpa clause) and supports VF1, but only for Ragusa. Its Venetian formula rests on González de Lara 2008.

- Expectation about the works:

  > - **Harris 2007 draft** (corporation v. commenda, Eurasia). The one work most likely to put the commenda against entity characteristics (legal personality, perpetuity, transferability, lock-in, limited liability). Could answer `LP1`–`LP3`, `CI3`, `TS2`, perhaps `AP1`/`CI2`. May speak of limited liability only for the investor, which the `AP3`/`LR1` locator makes `.NR`.

  Falsified on AP3/LR1: Harris states the traveller's sole liability to third parties (PDF 10-11). Falsified on LP1-LP3: Harris gives legal-personality statements only for the corporation and the waqf.

- Expectation about the works:

  > - **Venice.** González de Lara's work (the 2008 *JEH* article and earlier working papers) argues that the Venetian state's enforcement and administered convoy system made the *colleganza* work across large social distance. Puga and Trefler (2014) use the *colleganza* as a channel of social mobility closed off by the *Serrata*. I know nothing specific of Merelo-Guervós and Molinari (2025) or of Held (2025).

  Falsified in a detail of general knowledge: Held p. 8 n. 4 and p. 20 n. 53 cite González de Lara 2008 as *European Review of Economic History* 12/3, not the *JEH*. (Held p. 8 n. 4 also mentions a summary in *JEH* 61/2, 2001.)

- Expectation about the works:

  > - **Expected silences across all six:** `AP1`, `AP2`, `AP3`, `LR1` (at the labour-party locator), `CI1`, `CI2`, `CI4`, `LR5` beyond `.NA`, `RB3`, `PY0` beyond `.NA`, `MB3` stated in terms. **Expected non-independence:** Harris 2007 and Harris 2020 are one witness; Harris and van Doosselaere probably rely on Udovitch and on Pryor 1977 for the contract's terms; Held probably cites Pryor and Udovitch too.

  Falsified for AP1 (Harris PDF 11), AP3 and LR1 (Harris PDF 10-11; Udovitch 198), CI1 (Udovitch 198; Harris PDF 11-12) and MB3 stated in terms (Harris PDF 34). Confirmed for AP2, CI2, CI4, RB3 and PY0 (for RB3 the silence was confirmed, against my own cell prior of "none"). Confirmed on non-independence: Harris and van Doosselaere rely on Udovitch and Pryor, and so does Held.

Beyond single cells, three patterns:

- My priors expected silence on owner shielding at the labour-party locator. Harris 2007 and Udovitch speak to it directly, so the owner-shielding component moved from "expected empty" to coded, at modest confidence, for the commenda.
- I expected Harris 2007 to be the source for legal personality. It is not: it answers asset partitioning instead.
- I expected Held to carry loss verification. González de Lara's six-page summary carried more of it for Italy than Held did.

### 4. Characteristics that did not fit the evidence

- **`LR1` (liability extent) joins two questions: extent and form.** At the labour-party locator only one party is liable. The sources give an unlimited extent and a "sole" form (Harris PDF 10; Udovitch 198: the investor is not "jointly liable"), and the value set has no cell for "sole". I coded `unlimited-several` (low), reading "several" as "individually, not jointly". A reviewer could fairly prefer `.NR` with a flag.
- **`CI1` (capital structure).** The unilateral commenda's one-sided entrusted capital fits no value cleanly. The sources disagree: Udovitch 198 has "no social capital formed" (→ none), Harris PDF 11–12 has a separate commenda pool (→ common), and van Doosselaere 103 has several investors' shares in separate contracts (→ several-accounts). I coded `none` (low) and recorded the dissent.
- **`LR3` (profit-and-loss sharing).** The name says "profit-and-loss", but the definition says "returns shared proportionally to stake rather than as a fixed claim". The traveller's quarter is a share without a stake. I coded 1 (medium) on the share-versus-fixed-claim limb.
- **`RB1` and `RB2` (risk bearers).** Whether the traveller's forgone labour and expected share count as "loss" decides between `capital-provider` and `shared`. Udovitch 198 and Harris 2020, 26 describe the risks as "shared" or "split" while placing all capital loss on the investor.
- **`CF3` (principal count) and the type-row gloss "bilateral commenda".** In this literature "bilateral" means that both parties contribute capital (van Doosselaere 65; Held 7), not that there are two principals. A coder or reader can take the gloss as evidence for `CF3` = bilateral, and it is not. Principal count also varies across instances: van Doosselaere 70 n. 11.
- **`MC1` for societas_maris.** Pro-rata co-investment in one venture sits on the boundary between allocation and pooling as the vocabulary defines them. Harris 2020, 19 describes pooling as proportional sharing among stakeholders with no outsider. No work classifies the contract.
- **`PY0` has no cell for an arrangement without a pool.** I coded `.NA` on both loss rows, on the reasoning that the characteristic presupposes a pool.

### 5. Dependence and well-formedness problems noticed and not repaired

- **Sereno-type conflations (flagged, not split):**
  - `LR1`: extent plus form.
  - `LR3`: the name's "profit-and-loss" against the definition's "proportionally to stake … rather than as a fixed claim".
  - `RB1`: whether labour at risk counts.
- **The `agent-loss-exposure` group, commenda row.** `AP3` = 0, `LR1` = unlimited-several, `CF2` = 0, `LR6` = upside-only. `AP3` and `LR1` rest on Harris PDF 10–11 and Udovitch 198, which are not independent of each other (see Non-independence). As instructed, I computed nothing about collinearity. I note only that these cells share a source base.
- **The locator depends on CF1 inside the same form** (`AP3` and `LR1` use labour-party only where `CF1` is 1 or P). Because `CF1` was coded in this pass, the dependence was resolved from my own coding (commenda 1; societas_maris P), not guessed.
- **Schema and README defects (not repaired):**
  - (a) Both schemas' `type_id` and `char_id` descriptions name vocabulary files that do not match: `vocabularies/organizational_form_type.csv` is not in the bundle, and the loss schema names `cooperative_pooling_type.csv` and `cooperative_pooling_characteristic.csv` while the bundle's vocabulary is `loss_mitigation_characteristic.csv`.
  - (b) `source_lang` includes `zh` in the loss schema but not in the organizational one.
  - (c) The README says Harris 2007 "carries no printed page numbers", but it carries footer page numbers equal to the PDF pages.
  - (d) `Harris2020.pdf` is an SSRN preprint whose pagination is not the published chapter's.
- **The short citation "Harris 2020" is ambiguous.** Harris published *Going the Distance* (Princeton 2020), cited in Harris2020.pdf itself at p. 23 n. 40, pp. 25 n. 42, 28 n. 46, 29 n. 48, and "General Average and All the Rest" (2020). The `run-a-coding-batch` skill mentions a vault note "Harris 2020 on the late plurality of limited liability", which fits neither title. Harris2020.pdf p. 28 n. 44 cites a third Harris 2020, "A New Understanding of the History of Limited Liability", *Journal of Institutional Economics* (forthcoming 2020), and that is probably what the vault title refers to. If the live rows cite "Harris 2020" without a title, the defect code-a-form describes ("a short citation that names more than one held work") may apply. Not resolved.
- **Held's Ragusan *collegantia* is a unilateral-commenda variant** (Held 23), whereas the Venetian *collegantia* is bilateral (Held 9). A row glossed "Venetian collegantia" is right for Venice, but the same word means the other contract a hundred miles down the coast.

### 6. What to acquire next, and which cell it would move

- **Pryor 1977, "The Origins of the Commenda Contract"** (cited, not held). It is the shared upstream of van Doosselaere, Harris 2007 and Held. It would test societas_maris `RB1`, `RB2`, `LR3` and `CF3` (founded on a statement of van Doosselaere's that rests on Pryor), and could move societas_maris `AP3` and `LR1` from `.NR`.
- **A primary-normative text on the Venetian contract:** the statutes of Jacopo Tiepolo, 1242, III.I–III, cited by Held p. 9 n. 9 and p. 11 n. 20. It would move commenda and societas_maris `CI2`, `AP2` and `LP3`, and it is the only route to an `articulated` `VF1`. (The Genoese statutes that van Doosselaere 66 cites via Pryor would do the same for Genoa.)
- **Lopez & Raymond, *Medieval Trade in the Mediterranean World*, docs 85–87 and 174–184** (cited by Udovitch 198 n. 3 and Harris 2007 PDF 8 n. 13). These are contract translations. They would make societas_maris `CF1`, `CF3` and `RB1` `articulated`, and test `CF3` directly.
- **González de Lara 2008, "The Secret of Venetian Success" (*European Review of Economic History* 12), esp. p. 252.** It would raise commenda_alloc `VF1` from low and test societas_maris `VF1` (`.NR`).
- **Puga & Trefler 2014** (cited, not held). It could move societas_maris `PR1` (profit shares responsive to capital supply; Held p. 20 n. 52) and `VF1`.
- **Hansmann, Kraakman & Squire 2006.** The frame of Harris 2007 PDF 11; it would test commenda `AP1` (P, low) against its own source. Note that it is not independent of Harris's reading.
- **Merelo-Guervós & Molinari 2025** (cited, not held). I know nothing of its content; I cannot say which cell it would move.

## Checks

Run on a scratch copy outside the bundle (`$HOME/scratch/validate/`, on the device VM), after all cells were fixed. The copy holds each census's `recodings` resource alone, taken from `schema/<census>.datapackage.json`, with `foreignKeys` removed (the key to `data.csv` cannot resolve in this bundle) and `path` pointed at a copy of the proposed CSV. Nothing inside the bundle was written by any check.

- `pip install --user frictionless`, which printed `Successfully installed … frictionless-5.19.1 …`. It had not been installed: `python3 -m frictionless --version` printed `No module named frictionless`.
- `python3 -m frictionless validate organizational_forms.recodings-only.datapackage.json` printed `organizational_forms_recodings … table … VALID`.
- `python3 -m frictionless validate loss_mitigation_forms.recodings-only.datapackage.json` printed `loss_mitigation_forms_recodings … table … VALID`.
- A hand sweep by script over the 61 rows (Frictionless cannot see the vocabulary) printed `rows swept: 61 problems: []`. It checked:
  - `value` against each characteristic's `allowed_values`;
  - `.NA` propagating through `confidence`, `articulation`, `source_ref`, `source_lang`, `source_read` and `source_class`;
  - `.NR` carrying `confidence=.NR` and `articulation=.NR`;
  - every fixed field (`pass`, `recoded_on`, `condition`, `coder`, `coder_model`, `coder_effort`, `adjudication`, `adjudicated_by`), and `value_at_recoding` and `agreement` left empty;
  - no `[verify]`, and no `articulated` on a missing value;
  - LF line endings only.
- The same script listed every `applicability_on` pair, and each is consistent:
  - commenda: LR5=.NA with LR4=0; CF2=0 with CF1=1; LR6=upside-only with LR2=coupled;
  - societas_maris: LR5=.NA with LR4=0; CF2=0 with CF1=P; LR6=symmetric with LR2=coupled;
  - commenda_alloc: VF2=mixed with VF1=official-adjudication.
- **Not run:** `check_dependence.py`, `check_vocabularies.py`, `build_codebook.py` and `build_views.py`. The bundle has no `scripts/` and no `data.csv`. No similarity, distance or redundancy computation was run, by instruction.
