# Blind re-coding: `deed_of_settlement_company`, five cells, 2026-09-07

Coding chat, working only inside `~/GitHub/_blind-deed-of-settlement-recode-2026-09-07`. Five cells re-coded de novo — `AP1`, `AP2`, `AP4`, `AP3`, `LR1`. The other 27 were not coded, not reviewed and not touched. No co-occurrence is proposed. No characteristic is proposed and no value set is widened. `git` was not run; `data.csv` was not edited; no generator was run without `--check`.

Filename note: `NOTES-<slug>-<date>.md` was left free in case a selection brief occupies it; this file takes the `-coding-` suffix.

## 0. Ordering, and the two disclosed leaks

**Every cell was fixed and written to `PROPOSED-ROWS-…csv` before anything about the matrix was computed.** The value-instance and signature counts in §7 were run afterwards, against a copy, and no value was changed after them. The file timestamps carry the ordering, as does `PRIORS-deed-of-settlement-recode-2026-09-07.md`, which was written before either source was opened.

**Leak 1, disclosed in the prompt and confirmed.** `vocabularies/organizational_form_characteristic.csv` survives in the bundle, and the `entity`-locator text repeated in the `AP1` and `AP2` definitions describes this form's trust arrangement and says where the arrangement's boundary was drawn for locator purposes. I read it, because `allowed_values` and `applicability_on` are unreadable without it. I kept it out of the coding in a specific way: **I re-derived the locator fact from the sources and cite only the sources for it** — Televantos printed 18, "as partners were equitable co-owners of the firm's property, no partner could claim any particular asset of the firm as his own", and printed 37, the trustees held "the circulating partnership assets". No cell cites that prose, agrees with it, or counts it as corroboration, and the `AP1` note says so.

**Leak 2, NOT disclosed to me, and I am reporting it rather than using it.** The `code-a-form` skill — my own instruction set, not part of the bundle — contains this sentence in its discussion of when a `.NR` is a result rather than an evasion: *"If no — because the attribute turns on the individual instrument at every date, as owner shielding did throughout 1720–1844 — say so, because that is what makes the `.NR` a claim about the form rather than an evasion."* Owner shielding across 1720–1844 is `AP3` of this form and this form only. That sentence appears to state one of the five withheld values. **I did not use it.** My prior for `AP3`, written before I opened either source, was `0`; I reached `0` from the evidence; and I therefore disagree with what that sentence implies. I have run the split test it demands and given my answer in §3 and in the cell note. **The bundle cannot scrub the skill files, and this is a hole in the blind that the prompt's channel-check does not cover.**

## 1. The independence check, run first, before any cell

Counted across Televantos 2020's full extracted text: **`Getzler` 19 hits, `Macnair` 10.** Every hit's context was read.

Four are substantive citations of Getzler & Macnair 2005:

- the introduction, n22, where the book's asset-partitioning frame is set up;
- **the partnership chapter's statement of the jingle rule, n51, citing "Getzler and Macnair … 267, 275–85"** — the rule `AP1` turns on;
- the trusts chapter on bona fide purchase, n7;
- the opening of the partnership-bankruptcy chapter, n2.

The remainder are the OUP series editorship, the acknowledgements (Getzler thanked as a reader), one unrelated Macnair article on Lord Chancellors, three citations of Getzler's own separate work on security over circulating capital and on *Morice v Bishop of Durham*, the appendix's note that Getzler is one of the few scholars to have used Eldon's notebooks, and bibliography and index entries.

**Result: they are not independent witnesses, and on `AP1` they are one claim and its echo.** Televantos cites Getzler & Macnair *for the jingle rule itself*. No cell treats them as two witnesses, and the `AP1` and `LR1` notes say so in terms.

Two further dependences bind and are written into the type row's prose:

- **Both sources sit inside the Hansmann–Kraakman(–Squire) framework in which `AP1` is worded.** Getzler & Macnair cite Hansmann & Kraakman 2000. Televantos states it himself: the book "seeks to combine the insights of the law and economics theorists Hansmann and Kraakman" (printed 8, nn 22–23), and he glosses the jingle rule as "'soft' entity shielding and asset partitioning, Hansmann, Kraakman, and Squire" (printed 146, n10). Agreement between either source and that framework is not corroboration of it.
- **Getzler & Macnair are not independent of Harris 2000**, a coded source elsewhere in this census, and the dependence falls exactly where this batch needs them: their n53 sources the assimilation of deed-of-settlement companies to partnership law to Harris.

**One thing counts the other way and is a gain.** Televantos's assimilation claim rests on a wider base than theirs — DuBois 1938 quoted at length, Gow's treatise of 1823, Ker's 1837 *Report on the Law of Partnership*, Wordsworth 1845, Ireland — and he names Cooke 1950 as asserting the contrary with no authority earlier than 1852. On the assimilation, Televantos is not merely relaying Harris.

## 2. Offset and citation limits, derived not inherited

**Televantos: `printed = PDF − 25`, derived here at eight points** on both rectos and versos before anything was cited — PDF 41/printed 16, 42/17, 43/18, 101/76, 102/77, 151/126, 152/127, 201/176 — and checked structurally against the table of contents (Ch. 1 opens at printed 15, ch. 2 §2 "The Deed of Settlement Company" runs printed 35–53, ch. 7 printed 143–170). It agrees with the offset the prompt gave, but it was measured, not taken.

**Getzler & Macnair: no printed page is cited by any cell.** The bundle's copy is the Oxford working-paper version, carries no folio marks, and no offset can be derived from it. Where the paper is cited it is cited by section heading and case name — its sections are ENTITIES AND CORPORATE FORM · PRIORITIES IN LAW AND EQUITY · CONVEYANCE AS PRESUMPTIVE FRAUD · BONA FIDE PURCHASE · REPUTED OWNERSHIP · GENERAL EQUITABLE ESTOPPEL AS AFFECTING PRIORITIES · TRUSTS AS IN PERSONAM · DISAGGREGATING THE EFFECTS OF COVERTURE · THE JINGLE RULE OF PARTNERSHIP INSOLVENCY · CORPORATIONS · CONCLUSION. The cell notes say that this was done and why.

## 3. The five cells

Scope was established before any cell took a value. Both sources treat out-of-scope material at length, and two exclusions did real work: the **testamentary trading trust** (Televantos printed 53–60), which is founder-endowed and where trusts *did* create limited liability, and the **ordinary Regency partnership of owner-managers**, which is where almost all of the jingle-rule material actually lives.

| cell | value | confidence | articulation |
|---|---|---|---|
| `AP1` | `1` | medium | analyst-imposed |
| `AP2` | `.NR` | `.NR` | `.NR` |
| `AP4` | `.NA` | `.NA` | `.NA` |
| `AP3` | `0` | medium | articulated |
| `LR1` | `unlimited-joint` | medium | analyst-imposed |

**`AP1` = `1`.** Televantos asks the column's own question of this form by name, at printed 51: "it was partnership law which meant that the company's assets were available to business creditors in priority to the separate creditors of shareholder-partners: the use of the trust made no difference." The mechanism is at printed 22–23 (partners' indemnity and lien; partnership creditors subrogated to them, *Ex p Ruffin* (1801)) and summarised at printed 167. Confidence is **medium and not high for a reason in the source**: no case applying the jingle rule to a deed of settlement company is reported, and Televantos records at printed 47 n125 that "creditors of deed of settlement companies did not sue out commissions of bankruptcy against them" — the machinery through which the priority operated. The priority is asserted for this form, not demonstrated on one.

**`AP2` = `.NR`, and this is the batch's main result.** `AP2` asks two things, and its whole increment over `CI2` is the second: members' *creditors* cannot force partition or withdrawal. The **members' limb is well evidenced** — deeds excluded the default partnership rules (printed 36), the trustee device "was designed to insulate the company from the effect of the rules effecting mandatory partnership dissolution upon any change of partners" (printed 38), and shareholders "could not easily use the courts to dissolve or withdraw their capital from such concerns" (printed 51), which "de facto acted as a capital lock-in mechanism" (printed 52). **The creditor limb is nowhere asked of this form.** Neither source asks whether a shareholder's private creditor could force partition or withdrawal of a deed of settlement company's assets. The nearest passage — printed 148, "where a separate creditor of a partner levied judgment against that partner's share of the partnership assets, he could only claim the partner's right to the residue of the partnership assets after the partnership creditors had been paid" — is about ordinary partnership *and* is about priority in the residue, which is `AP1`'s question. Filling `AP2` from it would make `AP2` report `AP1`, which is precisely the failure this batch was set up to avoid. The vocabulary's own rule then governs: one limb answered and one unevidenced is `.NR`, not `P`.

**`AP4` = `.NA`.** The characteristic applies only where the entity was constituted by endowment out of an identifiable founder's patrimony; with no founder the cell is `.NA` and not `0`. The no-founder fact is taken from the sources, not assumed: Televantos's own glossary at printed 183 defines the form as "a business which raised capital by issuing shares and/or bonds", "distinct from a typical partnership, where the partners who managed the business provided the capital", and the constitutive act is a private deed drafted by counsel with promoters (printed 36) with capital raised by subscription (printed 36–37, 39, 45). That is arising by subscription, which the definition names as one of the modes yielding `.NA`.

**`AP3` = `0`, `articulated`.** Televantos gives the question a section of its own — printed 44–46, §2.2.1 "Unlimited Liability of Shareholders" — and the period says it in its own idiom about this form: *R v Dodd* (1808) 9 East 516, 527 concerned the shareholders of a large deed of settlement company, and Lord Ellenborough CJKB held that "as to the subscribers themselves, indeed, they may stipulate with each other for this contracted responsibility; but as to the rest of the world it is clear that each partner is liable to the whole amount of the debts contracted by the partnership" (Televantos printed 46).

**The split test, run and answered, because §0's leak turns on it.** Would a phase split give this cell a value in each phase? No — Televantos puts the change at 1855 and after, and nothing inside 1720–1844 moves. Does the attribute turn on the individual instrument at every date? **No, and that is his actual finding.** Deeds varied, and some purported to grant limited liability, but "such clauses were not fully effective" (printed 45): their effect was only that a shareholder could demand the company's property be exhausted first — a benefit of discussion, not a shield — and creditors could then sue shareholders personally unless that individual creditor had agreed otherwise. A single creditor's waiver is a contract with that creditor, not a feature of the form. The variation was in the drafting; **the legal position did not vary with it**, which is why this cell is an observed absence and not a silence.

**`LR1` = `unlimited-joint`.** *Extent* is articulated for this form in *R v Dodd*. *Form* — joint, not several — is the subject of a chapter section of its own (ch. 7 §4, "Rule IV: Joint Creditors Have Rights against the Partners' Jointly, not a Firm", printed 149; "creditors of the firm would acquire rights against partners jointly", printed 144), and it is carried to this form by two form-specific data rather than by assimilation alone: in *Van Sandau v Moore* (1826) a deed of settlement company could "frustrate Chancery suits brought against it by insisting that in such litigation each of the partner-shareholders be added as defendants" (printed 50), which is the joinder consequence of joint and not several liability; and Lord Eldon's 1824 proposal that creditors of such companies "should be able to recover the full amount of any debt by suing only some of the partner-shareholders" (printed 45 n108) presupposes that they could not. `limited` and `none` were both considered and rejected — `limited` because deeds purporting it were ineffective, `none` because liability plainly existed.

## 4. What could not be coded, and one dependency I could not resolve

`AP2` is the only cell that came back unrecorded, for the reason in §3: the column's second limb is never asked of this form by either source. That is a finding about the sources, not a gap in my reading, and the split test says it is not a period problem either.

**A dependency I flag rather than repair.** `AP3` and `LR1` both carry the 2026-08-18 locator fallback: `labour-party` where `CF1` is `1` or `P`, reverting to `members` otherwise. **`CF1`'s cell was withheld with the rest of this form's rows and could not be read** — the bundle's `data.csv` contains *no* `deed_of_settlement_company` rows at all. I resolved the antecedent from the sources instead: this form is not a bilateral capital–labour contract, the shareholder-partners subscribe capital and "would have no individual powers of management over the concern" (printed 37), and control lies with directors, a general court of proprietors and trustees. So there is no labour-supplying party and the locator is `members`, who are alike. The rule's own text ("where `CF1` is `0`, `.NA` or absent … the locator reverts to members") reaches the same place. **The maintainer must confirm against the live `CF1`: if it is `1` or `P`, both cells need re-examination on a different locator.**

## 5. Characteristics that did not fit the evidence

**`AP2` is the case, and it is a well-formedness problem I am flagging and not repairing.** Its own definition already carries the flag — "OVERLAPS CI2 and may be redundant with it … Flagged for review: candidate for merger rather than grouping" — and this form sharpens it rather than settling it. What this coding adds is that **the two limbs are not merely overlapping, they are differently evidenced**: the sources of this period treat members' withdrawal richly and members' creditors' power to force partition not at all, so a source can be rich on `AP2` and still yield nothing on `AP2`'s increment. A column whose evidential base splits that cleanly along its own conjunction is a candidate for the well-formedness test, but proposing the split in the batch whose coding motivates it would be retrospective selection. Flagged, not proposed.

**A second, smaller one.** `AP4`'s definition states that it "has no discriminating power yet" and must not enter a similarity claim until a founder-endowed form takes a value other than `1`. This coding does not help: `.NA` adds no instance, and `P` and `0` remain empty on that column. The remedy named in the definition — founder-endowed forms — is unaffected by anything in this batch.

## 6. Dependence and well-formedness problems noticed and NOT repaired

- The non-independence of Televantos and Getzler & Macnair on `AP1` (§1). Recorded in the cell note and the type row; nothing repaired.
- Both sources' position inside the HKS framework `AP1` is worded in (§1). Recorded; nothing repaired.
- Getzler & Macnair's dependence on Harris 2000 for the assimilation (§1), which matters because Harris 2000 is coded elsewhere in this census.
- **A qualification in Televantos that I deliberately did NOT carry across.** At printed 144 he argues Hansmann, Kraakman and Squire "overlook limitations on partnership law's ability to preserve business assets for business creditors" where a firm continued trading after a partner's death or retirement — the *Ex p Ruffin* problem, printed 163–66, under which a dissolution can strip the old joint creditors of their priority. **He never applies it to deed of settlement companies**, whose shares transferred by book entry and whose trustee device existed to absorb changes of membership. Applying it myself would have made `AP1` a `P` on an inference the source does not make. Recorded here as the thing that would move `AP1`; not used.
- The `check_vocabularies.py` failure in §8 is a bundle artefact, not a defect, and is not repaired.

## 7. What the matrix learned — computed only after all five cells were fixed

Against the bundle's scrubbed census, from which this form's own rows are entirely absent, so these figures describe the bundle and not the live matrix:

- **No new value-instance anywhere.** `AP1=1` (7 existing), `AP3=0` (10 existing), `LR1=unlimited-joint` (4 existing); `AP2=.NR` and `AP4=.NA` are missingness tokens. `AP4`'s `P` and `0` and `LR1`'s `none` remain without an instance, and this batch does nothing for them.
- **Entity shielding gains a signature.** `(AP1=1, AP2=.NR, AP4=.NA)` is held by no other form in the bundle's census; the nearest occupied cells are `(1, 0, .NA)` — `compagnia`, `compagnie_antwerpen_1608` — and `(1, 1, .NA)` — the three VOC phases.
- **Owner shielding learns nothing at all.** `(AP3=0, LR1=unlimited-joint)` is already occupied by `compagnia`, `compagnie_antwerpen_1582`, `compagnie_antwerpen_1608` and `nakai_fictive_household`. No new signature, no new value-instance, no gain in variance. **That is a result and belongs in the CHANGELOG**: the English unincorporated joint-stock company, on its two owner-shielding cells, is indistinguishable from a Florentine *compagnia* and an Antwerp general partnership — which is, in a way the census can now show, exactly what Televantos and the Regency courts said it was.

## 8. Verification, run on a copy; nothing in the bundle was written to except `proposed-of/`

- `frictionless validate datasets/organizational_forms/datapackage.json` → **VALID** (769 + 5 = 774 rows, ids `OF-0804`–`OF-0808` minted as `max(existing)+1 = 803+1`, asserted absent from the file; **note that row count and last id already disagree in this census**, so ids were taken from the file and not from arithmetic).
- `python3 scripts/check_dependence.py datasets/organizational_forms` — the **path** form, not the `--dataset` flag — → `dependence problems: 0`, and it printed its full separation tables, so it did run.
- `python3 scripts/check_vocabularies.py` → **5 errors, all of them the same bundle artefact**: `type_id 'deed_of_settlement_company' not in organizational_form_type.csv`, because the type row was withheld from the bundle. This will pass in the live tree, where the type row exists. **Not repaired, and the proposed type-rows CSV must not be used to create it** — its non-`key_source` fields are placeholders.
- Hand sweep of `value` against `allowed_values` for all five rows → pass. `.NA` propagated through `confidence`, `articulation`, `source_ref`, `source_lang`; `source_read=.NA` on the census's majority practice for `.NA` rows (47 of 66). `.NR` row carries `confidence=.NR` and `articulation=.NR`, which is **unanimous** house practice (162 of 162 `.NR` rows), and a real `source_ref` and `source_lang=en` with `source_read=full`, which is the **majority** practice (real `source_ref` on 144 of 162). Both figures are counts over the whole column, not samples. No `[verify]`; no `high` beside a partial read; `coder=ai`, `reviewed_by=none`, `review_status=unreviewed` throughout.
- `build_codebook.py --check` and `build_views.py --check` were run **on a separate untouched copy** to establish the baseline, never inside the bundle. Views: `entity-shielding` and `owner-shielding` both `current`. Codebook: reports `datasets/clearing_records/codebook.md: missing` — the generated codebooks were withheld from the bundle, as disclosed. Both artefacts will need regenerating when these rows are applied.
- `check_softwrap.py` → 16 files OK.

## 9. The bundle's vault, and why its silence is not evidence

Swept by term count rather than by filename, since in this vault a filename is a claim. Across 285 markdown files: `deed of settlement` 0 files, `Televantos` 0, `Getzler` 0, `Macnair` 0, `jingle` 0, `unincorporated` 0, `joint stock` 1 (not this form's own term — `joint_stock` is a separate census code).

**These zeros are read as absence and nothing more.** Vault notes were withheld from this bundle by design and its MOC entries and wikilinks were scrubbed, so a zero here is a hole the scrubber made. It is not evidence that no note exists, it was not counted toward anything, and no cell rests on it. **No cell in this batch was coded from a vault note**, and every cell rests on the two sources under `sources/` alone.

## 10. What to acquire next, and which cell it moves

1. **Getzler & Macnair 2005 in the Four Courts printing** (*Adventures of the Law*, 267–288). Moves nothing substantively, but lifts the standing bar on citing it by page, so `AP1` and `LR1` could carry a resolvable citation to the second source instead of a section heading. Cheapest item on this list.
2. **DuBois, *The English Business Company after the Bubble Act 1720–1800* (1938), 213–345 and 373–75.** This is the one that would move **`AP2`**, which is the cell that came back unrecorded. Televantos relies on DuBois for the drafting of actual deeds of settlement and cites him for the very question `AP2`'s second limb asks — printed 47 n125 sends the reader to DuBois 373–75 for what companies did instead of bankruptcy, including compromises with creditors and Acts of Parliament for formal dissolution. If any source records what happened when a shareholder's private creditor came against a named company's stock, it is DuBois's company archives. **`AP2` is the acquisition target of this batch.**
3. **Freeman, Pearson & Taylor, *Shareholder Democracies?*, 190–202 and 52–57.** Televantos cites them at printed 45 n106 for how limited-liability clauses varied by sector and at printed 51 n149 for shareholders' inability to withdraw capital. They would test whether `AP3=0` should be `P` for particular sectors — and if the variation turns out to be a phase or sector split rather than a uniform rule, that is a **row-splitting** question for the maintainer, not a recode.
4. **Morley, 'The Common Law Corporation' (2016) 116 Colum L Rev 2145, 2172–87.** The contrary reading on `AP3` and on capital lock-in, met by Televantos but not read here. Reading it would tell us whether `AP3=0` at `medium` is the right confidence, or whether the dispute should be recorded as it is at `bazacle_mill FP1`. It would also bear on `AP2`'s members' limb, though not on the creditor limb that actually blocks the cell.
5. **A reported case of execution or bankruptcy against an individual shareholder of a named deed of settlement company.** The direct evidence `AP2` needs. Televantos's own sampling of Chancery and Bankruptcy order books found none, which is itself a reason to think the acquisition may fail — and a failed acquisition returning silence would leave `AP2=.NR` standing as a claim about the period rather than about our reading of it.

## 11. CORRECTION to §10, added 2026-09-07 after the coding record was frozen

**This section post-dates the freeze and is not part of the blind record.** No cell was reconsidered; §§1–10 stand as written, and this corrects §10 item 2 in place rather than leaving it standing.

The maintainer reports that **DuBois 1938 cannot be located as a PDF**, and that **Harris 2000 itself rests on DuBois**. Both bear on the recommendation and it needs two amendments.

**First, the dependence.** If Harris rests on DuBois, then the chain already declared in §1 runs one link further: Getzler & Macnair → Harris 2000 → DuBois 1938, and Televantos cites DuBois directly and heavily besides. **So acquiring DuBois would corroborate nothing.** On `AP1` he would be the upstream of a witness this census already codes, and agreement between him and Harris, Getzler & Macnair or Televantos would be one claim and its ancestor. §10 item 2 did not say this and should have.

**Second, what survives of the recommendation.** The reason DuBois was named was `AP2`'s creditor limb, and that reason is untouched by the dependence point, because **no witness in this census has testified on that limb at all** — not Televantos, not Getzler & Macnair, and, on the measurement recorded elsewhere in this census, not Harris. DuBois would not be a corroborating witness there; he would be the first one. That is why he was named, and it remains the only route to a value.

**But the acquisition is unavailable, and a hazard is discharged by evidence, never by an acquisition.** `AP2 = .NR` therefore stands, and stands as a claim about the period's own sources rather than about the reach of this batch's reading. If DuBois is never acquired, the correct outcome is not a weaker value on thinner evidence — it is this `.NR`, with the reason recorded. §10 items 1, 3, 4 and 5 are unaffected; **item 3, Freeman, Pearson & Taylor 190–202, is now the most useful acquisition on the list**, because it bears on `AP3` and is a question of sector variation that no other listed work asks.
