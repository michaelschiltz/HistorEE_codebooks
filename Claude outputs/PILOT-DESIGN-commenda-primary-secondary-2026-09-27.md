# Pilot design: the commenda family, primary against secondary (2026-09-27)

**Status: draft for MS. Nothing has been coded. No data file has been touched.** This is the first test of the programme agreed on 2026-09-27: hold the rater fixed, vary the evidence, and read the secondary literature against the transactional record it compresses. **Sections marked OPERATOR ONLY must not reach the coding chat.**

## 1. What the pilot tests, and what it cannot

**The question.** When a form is coded from notarial acts rather than from the literature about them, which cells change, in which direction, and why? The pilot sorts every difference into one of four kinds:

- **Compression error.** The secondary value is not the modal state in the acts.
- **Compression loss.** The acts show a minority state that the secondary coding erased. This is heterogeneity turned into a type.
- **Outrunning.** The secondary coding asserts a value the acts cannot speak to. The primary arm returns `.NR` where the live row has a value.
- **Primary gain.** The acts answer a question the secondary coding left `.NR`.

**What it cannot test: independent corroboration.** The Genoese rows rest on van Doosselaere 2009 and on his dataset of "6,764 commenda ties" from 1154, which is built from the published Genoese cartularies. On its face that includes Giovanni Scriba (1154–64) and Cassinese (1190–92); verify against his source appendix. **Primary and secondary therefore share one evidence base.** Agreement between them corroborates nothing. Disagreement measures what the compression did, and that is exactly what this pilot is for.

**What it licenses: statements about notarial practice, not about "the commenda".** A notarial act is drafted from the notary's formulary, so the clause states within one cartulary measure that notary's drafting practice more than the parties' choices. See the vault note *The notarial security clause is boilerplate and cannot carry a typology*. At the level of the formulary the effective sample is the number of notaries, which is two in the Genoese core.

- A frequency within one cartulary describes one notary's practice.
- A difference between Scriba (1154–61) and Cassinese (1191) is a difference between two notaries, thirty years apart. It cannot separate time from hand.

The write-up must say this beside every figure.

## 2. Rows in scope

| census                | form             | rows                     | live coding (from `source_ref`)                  |
|-----------------------|------------------|--------------------------|--------------------------------------------------|
| organizational_forms  | `commenda`       | 21 of 32 characteristics | Harris 2007, van Doosselaere 2009, Pryor 1977    |
| organizational_forms  | `societas_maris` | 21 of 32 characteristics | van Doosselaere 2009, Harris 2007                |
| loss_mitigation_forms | `commenda_alloc` | 10                       | Held 2025, MHR I–IV (Ragusa, 1278–), Harris 2007 |
| loss_mitigation_forms | `societas_maris` | 9                        | van Doosselaere 2009, Held 2025                  |

All four were coded by `claude-opus-5` at `high`. `source_read` is `partial` or `unknown` throughout.

**Scope mismatch, declared in advance:**

- The `commenda` row is "Italian (Latin), 10–13c". The primary frame is **Genoa 1154–61 and 1191**, with Marseille 1248 optional.
- The Venetian half of `societas_maris` cannot be tested: Morozzo della Rocca & Lombardo 1940 and 1953 are not held.
- `commenda_alloc` is coded largely from Ragusan material, so the Genoese acts test it at one remove.

The comparison is reported per cell, restricted to the frame. It is not a verdict on the row.

**Eleven organizational characteristics have no row** for either form: TS1, TS3, TS4, MG1–MG4 and FP1–FP4. Coding them would mint `data.csv` rows. That is a data change, not a recoding, and it stays out of this pilot unless MS licenses a separate gap-fill arm.

## 3. Corpora and their state

| corpus                                                       | Zotero              | held                                                     | text layer                                                                                                                           | status                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------|---------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Cartolare di Giovanni Scriba*, ed. Chiaudano & Moresco 1935 | QTEG4PM7 → DHLLKXEI | vol. I only (BEIC scan, 509 pp; acts I–DCCCII+, 1154–61) | usable but letter-spaced OCR ("G ave sor or i s")                                                                                    | **core**                                                                                                                                                                                                                                                         |
| same item, second file                                       | QTEG4PM7 → 9PW8MDU5 | 139 pp, double-page spreads                              | none: image-only                                                                                                                     | **not Scriba's acts**: an OCR probe shows an introduction on the Genoese notarial archive and an inventory of registers ("Atti del notaio Jacobus de S. Savina"), probably Moresco & Bognetti's description of the twelfth-century cartularies; verify. Misfiled |
| *Guglielmo Cassinese*, ed. Hall, Krueger & Reynolds 1938     | G4TIJ2FM            | vol. I only (464 pp; acts 1–c.1092, 1190–Sept 1191)      | good on transcriptions; plates are noise                                                                                             | **core**                                                                                                                                                                                                                                                         |
| Pryor 1981, Giraud Amalric 1248                              | CQ4IPQ5Q            | 334 pp                                                   | **good** (Internet Archive layer; *corrected 2026-09-27*: Zotero's reader reports none, `pdftotext` reads Latin and English cleanly) | third notary, **editorially selected** (see below)                                                                                                                                                                                                               |
| Blancard 1884                                                | HF8ME3N7            | **vol. II only** (pp. 301–)                              | poor (tabular garble)                                                                                                                | not used; overlaps Pryor on Amalric, so one witness                                                                                                                                                                                                              |

**Pryor 1981 is an editorial selection with commentary, and both facts bind the design** (added 2026-09-27, after the text-layer correction):

- **It is not a sample.** The book gives about 100 notulae from Amalric's cartulary, chosen as exemplars of each contract type. The commenda-family chapters hold only a handful: VII *Comanda*, VIII *Companhia/societas*, IX *Comanda et companhia*, XXXI *Societas/companhia/comanda*. That is good for clause wording and useless for frequencies or minority states.
- **The unselected sample would be the full cartulary.** Blancard 1884 vol. II opens with acts nos. 1026–1027 of a numbered series, including a Ceuta comanda. That looks like the tail of the full 1248 cartulary, which would put the bulk in the vol. I we do not hold. Unverified.
- **The editor's commentary is secondary and shares an author with a live-row source.** Each chapter interleaves Pryor's essay (e.g. ch. VII's "basic features of the contract") with the notulae. The live `commenda` row cites Pryor 1977. **Arm P must receive an extract of the Latin notulae only**, cut out of the PDF by the operator, never the book.

The Genoese regesti (the editors' Italian headings) are a third layer: editorial classification. **Use them for sampling only, never as evidence.** Code from the Latin.

**Acquisitions this exposes:**

- Scriba vol. II;
- Cassinese vol. II;
- ~~OCR of Pryor 1981~~ (not needed: the text layer is good);
- Blancard vol. I (the Manduel commendas);
- Morozzo & Lombardo (hardcopy).

## 4. Design: three arms, one rater

The rater is held fixed: Claude Opus 5.5 at `high`, the same model in every arm, each arm in a fresh chat outside the claude.ai Project.

| arm               | reads                                                  | blind to                                     | purpose                                                                                                  |
|-------------------|--------------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **S** (secondary) | exactly the sources the live rows cite, no others      | live values                                  | a within-rater baseline; S against live also replicates the Opus 5 → 5.5 rater effect on a second family |
| **P** (primary)   | the Genoese acts only, in Latin                        | live values, all secondary literature, arm S | the evidence effect: P against S, same rater                                                             |
| **P→R** (reveal)  | the P chat continues after freezing its stage-1 coding | nothing                                      | reconciliation, and a direct measure of anchoring                                                        |

S and P must be separate chats. A chat that has read van Doosselaere cannot then read the acts "primary-only".

**Stage structure for arm P:**

1. **Priors**, including an exposure section, committed before any act is opened. Committed means the hash check at §7, not merely written.
2. **Type census.** Classify every act in the two volumes by contract type, using the regesto for sampling only: accomendatio, societas, mutuum, cambium or foenus nauticum, sale, dowry, other.
3. **Instance coding.** Draw the sample (§5) and code each act into the instance table (§6).
4. **Form-level summary.** Aggregate by the rule in §6, then **freeze**: files written and sha256 printed.
5. **Reveal.** The coder is shown the live cell and the arm-S cell with their notes. For each cell it records whether it keeps, revises or disputes its own value, and why. Stage-4 and stage-5 values are both kept.
6. **Directed disconfirmation.** For each cell where stage 4 and the live value differ, the coder searches the corpus for acts that would overturn **its own** value, and reports what it found. This is the "open search" half of the programme: severe, because it is aimed at the claim.

## 5. Sampling

- **Strata:** notary (Scriba, Cassinese) × type (accomendatio, societas). Add sea-loan instruments (foenus nauticum, "salvo eunte pignore") as a third type for the loss-census rows.
- **Size: all acts if a stratum has 60 or fewer; otherwise a systematic random sample of 60** (random start, fixed interval, over act numbers). **Why 60:** with n = 59, a clause variant present in at least 5% of a stratum's acts appears at least once with probability ≥ 0.95, since 1 − 0.95⁵⁹ ≥ 0.95. The pilot's main target is compression loss, so what matters is detecting minority states, not estimating proportions. A proportion to ±0.10 at 95% would need about 96, which is not warranted at this stage.
- **Clustering.** The same investors recur (e.g. Ogerio Galleta in Cassinese), as do the same days and the same travellers. Record party names so that cluster-robust summaries, or an effective n, can be computed. Report distributions with party-clustered intervals, or at minimum with the number of distinct investors.

## 6. The instance layer and the aggregation rule

**Where it lives.** For the pilot it is a CSV in `records/`, not a new `datapackage` resource. A schema change waits until the pilot shows the layer earns its place.

**Fields, one row per act:**

- **Identification:**
  - `instance_id`, `corpus` (Zotero key), `act_no`, `page_printed`, `date`, `place`, `notary`;
  - `editor_heading` (regesto, verbatim);
  - `act_type_latin` (the drafting term: *in accomendatione*, *in societate*, …).
- **Parties:** each party's name and role (stans / tractator / co-investor), and their count.
- **Capital:** `capital_stans`, `capital_tractator`, `currency`.
- **Venture:** `destination`, `duration_clause`.
- **Clause fields, each with a verbatim quote and a parsed value:**
  - `profit_rule`, e.g. "ad quartam proficui", "per medium";
  - `loss_rule`, e.g. "salvo capitali";
  - `peril_clause`;
  - `security`, e.g. "omnia bona sua pignori obligat";
  - `remittance_clause` ("possit mittere");
  - `separate_investment` ("implicare separatim");
  - `side_amounts` (e.g. "gratis" portions);
  - `penalty`.
- **Characteristic observations:** `char_obs`, a list of (char_id, state, quote, locator).
- **Quality:** `ocr_flag`, and `quote_checked_against_image` (y/n). Any quote that carries a form-level cell must be checked against the page image.

**Aggregation to a form-level cell:**

- Report the **modal state, its share, n, and the number of distinct investors**, per notary and pooled.
- **Frequency never becomes `P`.** `P` remains a structural half-state. Heterogeneity across instances is reported as a distribution, not collapsed into a value.
- **A state in at least 10% of acts in either notary counts as a variant.** Such a state is recorded as a compression-loss candidate if the secondary coding does not mention it.
- **A characteristic no act can address returns `.NR`**, even if the live row has a value. That is the "outrunning" class.

## 7. Governance, carried over from 2026-09-26 with its repairs

- **Priors.** The coder prints the sha256 of its filled priors, and MS commits them. Before any act is opened, the committed blob must match that hash. The application chat verifies it from `.git` objects, without running git.
- **Rows** go to `recodings.csv`:
  - pass slug `commenda-primary-2026-XX` (arm P) or `commenda-secondary-2026-XX` (arm S);
  - `condition=blind` for the stage-4 values;
  - the stage-5 values as separate rows with `condition=open`;
  - `source_ref` naming the corpus and act numbers.
- **`recodings.csv` has no `source_class` column.** Proposed: add `source_class` (primary-transactional / primary-normative / secondary). That is schema growth, so a version bump, and MS decides. Until then, the pass slug carries the class.
- **Freeze before reveal.** Anything computed after the freeze goes to a separate file.
- **No unweighted similarity over all characteristics.** Comparative statements run on a declared component set or not at all.
- **Standing-table rows** for every chat that spends the blind, including this one (§9).

## 8. What would count as a result

- **Primary gain.** At least one characteristic moves from `.NR` to a coded state from the acts. The cheapest candidates are loss-census RB1, RB3, RB4 and PR1, which acts state directly.
- **Compression loss.** At least one variant at 10% or more that the secondary coding does not record. Examples of the kind of clause at issue: the profit fraction, capital from the traveller, remittance rights.
- **A null is a result too.** If P and S agree on every act-addressable cell, the secondary coding is shown to be a faithful compression of these cartularies, for these characteristics. Say so.
- **Anchoring.** The share of stage-4 values revised at reveal, and the direction of revision (toward the live value or away from it). This is the first direct measurement of how far a revealed value pulls the model.

## 9. OPERATOR ONLY: exposure of this chat

**This chat is the operator and can never be a coder for this pilot.** It has read:

- the commenda-family rows' `source_ref`, `source_read` and missingness counts (not their values);
- the full characteristic vocabularies;
- Cassinese acts 490, 491 and 1090–1092;
- Scriba acts CDXXXIV–CDXXXV and DCCCI–DCCCII.

**Proposed standing row:**

- slug: `commenda-pilot-design`, 2026-09-27, operator;
- spent: the citation base and missingness of `commenda`, `societas_maris`, `commenda_alloc` and the loss-census `societas_maris`, plus the named acts;
- prejudices: any coding of those rows by this chat;
- does not reach cell values.

## 10. OPERATOR ONLY: observability predictions (withhold from the coder)

These are the operator's predictions of which characteristics notarial acts can address at all. They are to be scored after arm P. They are withheld because telling the coder which cells "cannot" be answered would steer it toward `.NR`.

- **Addressable from acts:**
  - organizational: TS2, CI1, CI2, CI3/CI4 (only if assignments occur), LR2, LR3, LR6, CF1, CF2, CF3, LR1 (via general-pledge clauses, with care);
  - loss census: MC1, RB1–RB4, PR1, MB3, and VF1/VF2 only if a loss is ever claimed.
- **Not addressable from acts, expected `.NR` in arm P:** LP1–LP3, AP1–AP3, AP4. These are creditor-priority and entity questions, which need litigation or statute.
- **Prediction:** the first list is where primary gain and compression loss will appear, and the second is where "outrunning" will appear if the live rows carry values there.

## 11. Decisions for MS

1. **Scope.** *Decided 2026-09-27: include Marseille.* Pryor needs no OCR, but its notulae are an editorial selection, so Marseille contributes clause wording, not frequencies, unless Blancard vol. I is acquired.
2. **Run arm S.** *Decided 2026-09-27: yes.*
3. **Sample size** of 60 per stratum, and the 10% variant threshold.
4. **The instance table in `records/` for the pilot** (recommended), versus a schema resource now.
5. **`source_class` in `recodings.csv`.** *Decided 2026-09-27: add it.* Specified in `proposed-of/PATCH-source-class-2026-09-27.md`, awaiting approval.
6. **The eleven absent organizational characteristics:** leave them (recommended), or license a separate gap-fill arm that mints rows.
7. **Identify QTEG4PM7's second file** (9PW8MDU5), and decide whether to acquire Scriba vol. II and Cassinese vol. II before or after the pilot.
