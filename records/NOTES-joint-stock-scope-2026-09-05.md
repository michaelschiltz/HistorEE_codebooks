# Forms selection — `joint_stock`, its source, and its scope, 2026-09-05

**Operator session. Slug `joint-stock-scope-scheme`.** Nothing coded, no row proposed, `data.csv` untouched, no `git` run. Written after the shielding-witness batch was applied and committed. Companion to `proposed-of/NOTES-shielding-witness-2026-09-05.md`, which this session read in full, and to `claude/shielding-witness-coding-2026-09-05.md`.

Census at the start of this session: `organizational_forms` **803 rows, 43 form codes, 33 coded forms, version 0.9.0**. Ten zero-instance values, seven one-instance values.

## 0. The decision, and it is not the one this session set out to make

**Next session: NOT a blind coding batch. A scope-and-verification pass on `joint_stock`, plus the sub-pool correction, both of which are open and neither of which needs a blind.**

The session began by working up the `AP4` batch that the shielding-witness pass recommended — the testamentary trading trust, founder-endowed, a live candidate for the value `AP4` has never taken. **Holdings killed it**, and then a vault sweep killed the replacement's blind. Both negatives are recorded in full below because each was reached by a measurement that can be repeated.

What is left is better than it sounds: three standing items converge on one held, unread, twenty-two-page article, and none of them requires an acquisition or a bundle.

## 1. Why the `AP4` batch is not available, measured rather than assumed

**Neither second witness is held.** `Ollikainen-Read` returns nothing in the library — the search falls through to semantic matches on Russian stock-exchange histories, which is what a miss looks like here. `Morley` returns two items and neither is *The Common Law Corporation* (2016): what is held is **Zhang & Morley 2022, "The Modern State and the Rise of the Business Corporation"** (`5TVI7GZZ`, preprint, tagged `Asset Partitioning` / `Entity Shielding` / `Limited Liability`), which is comparative theory, and a 2008 macroeconomics paper by a different Morley. **Harris 2000, *Industrializing English Law*, is not held either.**

**And no other founder-endowed form is held.** `chantry` returns nothing — the search falls through to Peruvian commerce bulletins and a graphic novel. `Stiftung` returns three items, all German and all from the maritime and cooperative-pole sweeps: Ebel's two-page Ruhwedel review, Haff on medieval transport cooperatives, Lohsse on the sea loan. `trust` returns Ottoman *waqf* material, Lamikiz on merchant networks, and Luhmann. **This reproduces Chat A's measurement of 2026-09-05 exactly**, and the hope that the shielding-witness reading had made the batch cheaper was wrong: it identified the form, it did not put a second witness in the library.

**Consequence.** Coding the testamentary trading trust now would give the census **a third English row from Televantos alone** — the single-author non-independence that the shielding-witness batch spent an entire logbook entry flagging on the Antwerp / `partenrederij` pair. It is available and it is a worse trade than it looked. **`AP4` remains an acquisition problem**, exactly as the shielding-witness brief's §11.4 said, and this is the fifth session to leave it standing.

## 2. What turned up instead, and why it is not what it first appeared

**`6FN9JG5S` — Harris, R., "A new understanding of the history of limited liability: an invitation for theoretical reframing", *Journal of Institutional Economics* 16:5 (2020), 643–664. DOI `10.1017/S1744137420000181`. Held, linked file, unread.**

**Offset measured and it is exact: `printed = PDF + 642`, verified at twenty-one consecutive points** — PDF 2 → 644 through PDF 22 → 664, with PDF 1 and 22 carrying the range 643–664. 22 PDF pages, clean text layer, 109,047 characters. The file name carries the range and the PDF `Title` field reads `S1744137420000181jra 643..664`.

Whole-file term counts:

| term | count | | term | count |
|---|---|---|---|---|
| `limited liability` | **189** | | `unincorporated` | 12 |
| `shareholder` | 93 | | `bankrupt` | 11 |
| `charter` | 47 | | `partnership` | 10 |
| `joint-stock` / `joint stock` | 36 / 7 | | `liquidat*` | 9 |
| `creditor` | 29 | | **`double liability`** | **9** |
| `unlimited liability` | 28 | | **`reserve liability`** | **15** |
| `legal personalit*` | 20 | | `hansmann` / `kraakman` / `squire` | 6 / 2 / 1 |
| `asset partitioning` | 5 | | `entity shielding` | 3 |
| | | | **`deed of settlement`** | **0** |

### 2.1 It is not a second witness on `deed_of_settlement_company`, and that was this session's first wrong guess

`deed of settlement` returns **0**. The article never names the form the English row scopes. It is a second witness on the **liability regime of chartered corporations**, not on the unincorporated company. The recruitment-bias corrective the shielding-witness brief asked for is still **Harris 2000**, and it is still not held.

### 2.2 It is the source of `joint_stock`'s cells, and the citation is ambiguous

`joint_stock` carries two cells, `OF-0032 LP1=1` (note: "chartered legal personhood") and `OF-0033 AP3=P` (note: **"limited liability a late and plural achievement, not an original feature"**). Both cite **`Harris 2020`**, both `source_read=unknown`, both `articulation=.NR`.

**There are two held Harris 2020s.** This article, and `8THJD26T` *Going the Distance: Eurasian Trade and the Rise of the Business Corporation 1400–1700* (Princeton; Zotero dates it 2019, the imprint is 2020). The `AP3` note is this article's abstract almost verbatim — *"limited liability … became a separate corporate attribute … only around 1800"*, *"a uniform attribute of all corporations only in the 20th century"*. **`joint_stock`'s `key_source` does not say which, and the two are different works with different periods** (1400–1700 for the book; 1600–1900 for the article). Nobody has noticed, and it sits directly under the scope note MS is holding for approval.

### 2.3 It may expose an `LR1` vocabulary gap, and that is the most interesting thing in it

`LR1 liability extent` allows `unlimited-joint | unlimited-several | limited | none`. Harris counts **`reserve liability` 15** and **`double liability` 9** — regimes in which a shareholder's exposure is capped at a multiple of the subscription rather than at the subscription or at everything. **None of the four allowed values states that.** `LR1=none` is already a zero-instance value the 08-30 record flags as suspect on its locator; this would be a second, independent problem with the same column.

**Flag, do not repair, and the reason is the standing rule**: a repair must not be proposed in the pass that motivates it. Read the article first, establish whether the census has or could have a form in such a regime, and only then decide.

## 3. The blind is badly spent for this material, and that decides the session's shape

Term counts over `~/GitHub/myfoamrepo`, counts only:

| term | files / hits | | term | files / hits |
|---|---|---|---|---|
| `Harris` | **53 / 127** | | `deed of settlement` | 0 / 0 |
| `lock-in` | 39 / 136 | | `double liability` | **0 / 0** |
| `limited liability` | 19 / 40 | | `reserve liability` | **0 / 0** |
| `entity shielding` | 17 / 27 | | `unlimited liability` | 1 / 1 |
| `asset partitioning` | 2 / 2 | | `Blair` | 2 / 2 |

**Twenty-seven notes across nine `source-session` slugs mention Harris together with a liability or shielding term.** Two slugs dominate: **`ron-harris-tradeoffs` (13 notes)** and **`harris-omega-naties` (2)**. And the decisive one — **`harris-omega-naties` holds a note titled *"Harris 2020 on the late plurality of limited liability"***.

Under the 2026-08-16 disclosure, in this vault **a filename is a claim**. That title *is* the article's thesis. The vault has argued this exact source. **A blind pass on Harris 2020 is not available at reasonable cost**: it would need 27 notes withheld across nine slugs, with `make_blind_bundle.py` scrubbing the MOC entries and wikilinks that point at the holes — a heavily holed vault for one twenty-two-page article.

**Against that, the specific things the article is about are genuinely unargued**: `double liability` **0 files**, `reserve liability` **0 files**, `unlimited liability` **1 file / 1 hit**. So the blind is not uniformly spent — it is spent on the frame and clean on the mechanism.

**The conclusion is not "code it blind anyway" and not "abandon it".** It is that the work `joint_stock` actually needs is **documentation and scope, which no blind protects**: which Harris 2020 the cells cite, what the row's referent is, and whether the row should exist. Those are decided by reading and by argument, not by a coding pass, and the `confraternita` precedent of 2026-09-04 shows an uncoded row with a reasoned refusal is a result.

## 4. The umbrella question, which must be settled before any cell is coded

`joint_stock` reads `Joint-stock corporation | European | 17c onward`. On the chartered reading its `LP1=1` cell note already fixes, **that scope contains `voc_1602`, `voc_1612` and `voc_1623` — coded at full 32 — and arguably `casa_san_giorgio` and the two `maone`.** That is the defect logbook 2 records for `ie`, `piaohao` and `kabu_nakama`: a parent row sitting above coded children.

**Three outcomes are live and the session must choose among them on evidence, not tidiness:**

1. **Narrow it** to a referent its children do not occupy — e.g. the English chartered corporation specifically, or the 17c form before the VOC phases.
2. **Retire it**, moving its two cells to whichever row the evidence supports, on the ground that the census codes forms and not families.
3. **Keep it as a declared umbrella**, uncoded beyond the two cells, with a scope note saying so and a prohibition against any similarity claim putting it on the same footing as its own children.

**Coding out its remaining thirty cells is NOT among them until this is settled**, because on outcomes 2 and 3 that work is wasted or wrong.

## 5. The sub-pool correction, which is independent and should go first

**A standing prohibition has been discharged for five days and eight vocabulary definitions still assert it.** Logbook 1, **2026-08-31 (iii)** — *"the sub-pool recode audit is run: 32 cells examined, 2 recoded, and `begijnhof` loses the census's only complete legal personality"*. Yet all eight `entity`-locator characteristics (`LP1`, `LP2`, `LP3`, `AP1`, `AP2`, `MG4`, `FP2`, `FP4`) still carry **"THE RECODE AUDIT THIS RULE REQUIRES ON FORMS WITH SUB-POOLS HAS NOT BEEN RUN"**, and the shielding-witness brief of 2026-09-05 repeated it as live.

**It is not simply stale, which is why it needs a session and not a one-line edit.** The audit ran at **643 rows**. The census is at **803**. Five forms have been added since and at least two have sub-pools: `avariz_vakfi`, whose own CHANGELOG entry records nine *bölük* each with its own trustee and cash under a mahalle scoping, and the two `compagnie_antwerpen` rows, whose *fuori del corpo* fund is recorded as a sub-pool in their `CI1` and `LP1` notes. `bruderschaft_salzburg` and `deed_of_settlement_company` need checking; the English row's notes argue the trust fund is the whole arrangement and not a sub-pool, and that argument should be tested rather than accepted.

**The correction is therefore: re-run the audit on the five forms added since 643 rows, then rewrite the eight definitions to read what is true — run 2026-08-31 at 643 rows, re-run <date> at 803 — and add a forward pointer from logbook 1's earlier entries to the entry that discharged it.** Cheap, and it stops a false prohibition binding rows this project added yesterday.

## 6. Recommendation

**One session, open, no bundle, no acquisition, in this order:**

1. **The sub-pool correction** (§5). Independent of everything else and the fastest thing on the list.
2. **Read Harris `6FN9JG5S` in full.** 22 pages, offset `printed = PDF + 642` verified at 21 points, clean text.
3. **Disambiguate `joint_stock`'s `key_source`** between the article and `8THJD26T`, on the internal evidence of the two cell notes.
4. **Settle the umbrella question** (§4) among the three outcomes, and write the scope note MS is holding — `proposed-of/PATCH-joint-stock-scope-2026-09-05.md` is the draft, and its positive half was deliberately left blank pending exactly this reading.
5. **Flag the `LR1` gap** if the reading supports it. Flag only.

**Not now, and why.** The `AP4` batch, until an acquisition session runs — its spec is at the shielding-witness brief §11.4 and this session adds one candidate to it, the **testamentary trading trust**, with the caution that Televantos alone makes it single-witness. A blind Harris coding pass, on §3. And the `AP2` split, which needs deciding on its own merits before a form is coded to test it, and whose only current test-form was coded in the pass that found the defect.

## 7. Non-independence and co-occurrence

**No new form is proposed, so no co-occurrence declaration is required.** Two independence facts should nonetheless be recorded before any cell moves:

- **Harris `6FN9JG5S` and Harris `8THJD26T` are one author twice**, and both are candidates for the same `key_source` string. If `joint_stock` ends up citing both, they are **not two witnesses**, and the `partenrederij` / `compagnie_antwerpen` precedent of 2026-09-05 applies verbatim.
- **`joint_stock` and the three `voc` rows** would be non-independent in the other direction if the umbrella is kept: a parent and its children are one institution described twice. No similarity claim may put them on the same footing.

## 8. This session's row for the standing spent-blind table

| slug | session | what it spent |
|---|---|---|
| `joint-stock-scope-scheme` | 2026-09-05, operator | Read the live `organizational_forms` `data.csv` at 803 rows and recomputed the zero-instance and one-instance value tables on it; read the `joint_stock`, `natie` and `nacion_cofradia` cells in full; read `proposed-of/NOTES-shielding-witness-2026-09-05.md` whole, including its §11 addendum; read logbook 1's 2026-08-31 (iii) sub-pool audit entry in full and logbook 4's standing table. Ran Zotero metadata searches for Ollikainen-Read, Morley, Harris, chantry, Stiftung and trust, and read the metadata and abstract of `6FN9JG5S`, `8THJD26T` and `5TVI7GZZ`. Measured the `6FN9JG5S` offset at 21 points and ran whole-file term counts on it; **did not read its body.** Ran **term counts only** over the vault for ten terms and extracted the `source-session` slugs and **note titles** of the 27 notes matching Harris plus a liability term — **and in this vault a filename is a claim, so reading the title "Harris 2020 on the late plurality of limited liability" spent the blind on that article's thesis.** Prejudices any later blind coding of `joint_stock`, of `LR1`, and of the limited-liability chronology generally. Brief at `proposed-of/NOTES-joint-stock-scope-2026-09-05.md`. |
