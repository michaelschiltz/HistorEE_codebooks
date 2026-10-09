# HistorEE: the codebooks, the vault, and how coding sessions bind them

*A manual for researchers joining the project*

Maintainer: Michael Schiltz · State described: 7 October 2026 · Repositories: `michaelschiltz/HistorEE_codebooks` (branch `main`) and `michaelschiltz/myfoamrepo` (branch `master`)

<!-- House rule for this file: it is copied into every blind bundle. Never add a coded value, a form's result or a batch finding unless it already appears in CLAUDE.md or CONTRIBUTING.md. Prose is soft-wrapped; tables are padded (check_tables.py --fix). -->

> **Canonical copy:** `HistorEE_codebooks/ONBOARDING.md`. Any PDF or Drive copy is a dated snapshot of this file and may be out of date.
>
> This manual orients; it does not legislate. The binding rules live in the repositories themselves — `CLAUDE.md`, `CONTRIBUTING.md` and `CHARACTER-CODING.md` in the codebooks, `CLAUDE.md` and `tags.md` in the vault. Where this document and those files disagree, the files win, and the discrepancy should be reported so that this manual can be corrected.

---

## 1. The picture in one paragraph

HistorEE keeps its **evidence** and its **claims** in two separate Git repositories, governed by one discipline. `HistorEE_codebooks` holds the evidence: two feature-coded censuses of historical institutional forms (cooperative organisational forms; loss-mitigation forms), their schemas, their controlled vocabularies, and a narrative record of every coding decision. `myfoamrepo` holds the claims: some 540 atomic Markdown notes, each arguing one thing, cross-linked by wikilinks and organised through hub notes. A **coding session** is the procedure by which the vault's sources and arguments are turned into rows in the codebooks — and, in its blind variant, the procedure by which the vault is deliberately *hidden* from the coder so that a coding can falsify an expectation rather than merely restate it. Understanding that double relation — the vault as the coder's evidence on the one hand, as the coder's contaminant on the other — is the single most important thing in this manual.

---

## 2. The two repositories at a glance

|                         | `HistorEE_codebooks`                                                                  | `myfoamrepo` (the Foam vault)                                                    |
|-------------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Holds                   | Data, schemas, vocabularies, decision logs                                            | Arguments, distinctions, objections, source and archive notes                    |
| Unit                    | One row = one characteristic of one form (`type_id` × `char_id`)                      | One note = one claim                                                             |
| Canonical format        | UTF-8 CSV + Frictionless `datapackage.json`                                           | Markdown with YAML frontmatter and `[[wikilinks]]`                               |
| Generated, never edited | `codebook.md`, `views/*`                                                              | `graph/graph.html`                                                               |
| Enforcement             | CI (`validate.yml`) + local check scripts                                             | Pre-commit hook + CI (`vault.yml`) running `validate_vault.py`                   |
| Narrative record        | Six logbooks, `CHANGELOG.md`, `records/`                                              | `source-session` frontmatter + `git blame`                                       |
| Licence                 | Data and prose CC BY 4.0; code MIT                                                    | Note prose CC BY 4.0; code MIT                                                   |
| Citable as              | Zenodo concept DOI `10.5281/zenodo.21341360`; FigShare `10.6084/m9.figshare.32947250` | Zenodo DOI `10.5281/zenodo.21615890` [verify — cited in Part 2, not yet checked] |
| Editor                  | VS Code                                                                               | VS Code with the Foam extension                                                  |

Both repositories are **public**. Anything committed to either is published under CC BY 4.0 the moment it is pushed. Section 9.1 draws the consequences.

---

## 3. `HistorEE_codebooks` — the evidence

### 3.1 Layout

```
HistorEE_codebooks/
├── datasets/
│   ├── organizational_forms/     data.csv · recodings.csv · datapackage.json · codebook.md
│   ├── loss_mitigation_forms/    data.csv · recodings.csv · datapackage.json · codebook.md
│   ├── clearing_records/         synthetic worked example — not archival data
│   └── _template/                scaffold for a new dataset
├── vocabularies/                 one CSV per coded field (characteristics, form types, units)
├── views/                        reader-facing matrices, one per declared component — GENERATED
├── logbook/                      six running decision logs
├── records/                      tracked, verbatim evidence of completed batches
├── scripts/                      validators, generators, the blind-bundle builder
├── CONTRIBUTING.md               the coding manual
├── CHARACTER-CODING.md           when a new characteristic is warranted, and when it is a mistake
├── CLAUDE.md                     rules governing assistant sessions
├── EDITING-CSV.md                how to hand-edit data.csv in VS Code without breaking it
└── CHANGELOG.md                  dataset-level change record
```

### 3.2 Three layers, one source of truth

1. **Data** — `data.csv`, plain UTF-8 text, canonical. Never opened in Excel and pasted back: Excel silently mangles encodings, dates and leading zeros, and `.gitignore` refuses `*.xlsx` for that reason. `EDITING-CSV.md` describes three safe ways to edit in VS Code (plain text, Rainbow CSV, Edit CSV).
2. **Schema** — `datapackage.json`, Frictionless Table Schema: field names, types, enums, keys.
3. **Codebook** — `codebook.md`, **generated** from the schema by `scripts/build_codebook.py`. Editing it by hand is a mistake; it also goes stale on data change, because it publishes row counts.

### 3.3 The two censuses

**`organizational_forms`** (v0.11.0; 897 rows; 35 coded forms; 32 characteristics) codes institutional forms on the properties that make up the business corporation when bundled — legal personality, entity and owner shielding, capital lock-in, transferable claims, perpetual succession — and on the loss-management properties that sit beside them. **`loss_mitigation_forms`** (v0.8.0; 760 rows; 49 coded forms; 26 characteristics) codes the instruments by which perils were pooled, shared, shifted or priced. Each row records one characteristic of one form:

```
record_id, type_id, char_id, value, confidence, articulation, source_ref, source_lang,
coder, source_read, reviewed_by, review_status, notes, coder_model, coder_effort
```

The forms are defined in `vocabularies/<dataset>_type.csv`; the characteristics in `vocabularies/<dataset>_characteristic.csv`. **Read the characteristic vocabulary in full — `locator` and the whole `definition`, not just `allowed_values`.** Definitions carry standing rulings and prohibitions that bind every coding.

### 3.4 The declared component sets — the matrix's only licence for comparison

With enough characteristics any two forms separate; that is Watanabe's ugly duckling theorem, and it is why "this lets us tell X from Y" never justifies a new characteristic. The answer is a **weighting declared in advance**, recorded in the vocabulary's `component` and `work_package` columns:

- **WP2 — continuity of capital** (the entity's trajectory): entity shielding, capital lock-in, transferable claims, legal personality, perpetual succession. Thirteen characteristics.
- **WP1 — management of loss** (the individual's trajectory): owner shielding, outcome coupling, loss sharing, risk pooling. Eight characteristics.
- **Eleven characteristics are `none` in both**: description only, never part of a comparative claim.

Three rules follow and are not optional. No comparative claim runs on all 32 characteristics. The set a claim runs on is fixed before the coding it is tested on. And `none` is not a holding pen: promoting a characteristic into a set is a theoretical claim needing the same justification as adding one. Each component has its own generated view in `views/`; read the second line of any view, which states its filter, before trusting it.

### 3.5 Coding conventions a newcomer gets wrong first

**Missingness is disaggregated.** `.NR` not recorded in the source; `.IL` illegible; `.NA` not applicable; `0` an observed absence. A source that does not address a question yields `.NR`, never `0`. This is the commonest way to wreck the dataset. No cell is ever blank.

**Inapplicability runs backwards.** If a child characteristic is `.NA`, that is evidence about its parent (`waqf_khayri LR4` was corrected from `P` to `0` on exactly this reasoning). `.NA` propagates through `confidence`, `articulation`, `source_ref` and `source_lang`.

**`P` means structurally half-present**, within one arrangement. It is not a hedge (uncertainty goes in `confidence`), not functional analogy (that goes in `notes`), and not variation across instances or time (that is a row to be split). A `P` beside `low` confidence and a note arguing for `0` is almost always a `0`.

**`articulated` means the tradition said it**, in its own idiom, in a primary text or a verbatim quotation. A modern scholar's functional description is `analyst-imposed`. CI forbids `articulated` beside a `[verify]` citation.

**Two-limb characteristics.** Several characteristics ask a conjunction (`AP2`: members *and their creditors* cannot force partition). One limb present and one structurally absent is `P`; one limb answered and one unevidenced is `.NR`.

**Dependence.** `applicability_on` records whether a cell *exists*; `dependence_group` and `dependence_scope` record whether it *adds evidence*. They are never merged. A dependence asserted on logical grounds is a hypothesis, and forms have falsified several.

**Disagreement is coded, not resolved.** `bazacle_mill FP1 = mixed` holds a scholarly dispute open deliberately.

### 3.6 Attribution, re-codings and adjudication

`coder` names who entered a row. Assistant codings carry `coder=ai` plus `coder_model` and `coder_effort` (e.g. `claude-opus-5-5` / `high`); these are provisional pending human adjudication and must never be bulk-converted to initials. Human coders enter their initials.

**Re-codings never overwrite history.** A second reading of an existing cell goes to `recodings.csv`, one row per cell per pass, with `value_at_recoding`, `agreement`, `adjudication=pending` and `source_class` (the class of the cited *passage*: `secondary`, `primary-transactional`, `primary-normative`, `primary-institutional` or `mixed`). `data.csv` changes only when the maintainer adjudicates `replaced`.

### 3.7 `records/` versus `proposed-of/`

This line governs what the deposit may cite.

- **`records/` is tracked and preserved verbatim.** Selection briefs (`NOTES-…`), the priors written before a source was opened (`PRIORS-…`), the prompts handed to blind chats (`PROMPT-…`), proposed rows, bundle excisions, rulings. Nothing in it is ever reformatted, re-wrapped or tidied — it is evidence, and the style checkers exclude it.
- **`proposed*/` is gitignored.** Work in flight and superseded drafts: open patches, commit-message drafts, logbook drafts.

A logbook entry or cell note may cite `records/` as evidence; it may cite `proposed-of/` only as a pointer to open work, resolved when the work is. **Never cite a file that is not in the repository** — an audit on 2026-09-08 found 47 such citations, nine already broken.

### 3.8 Logbooks and CHANGELOG

Six running logs, newest entry at the top, headed `## YYYY-MM-DD — <initials or ai> — <what changed and why it matters>`:

1. database architecture · 2. inclusion and exclusion · 3. scripts and generators · 4. tests and results (including the **standing table of spent-blind session slugs**, §6.4) · 5. quality and nature of sources · 6. other.

Correct by adding a dated entry, never by erasing. `CHANGELOG.md` takes a block per dataset per batch, ending with the version decision. Version bumps follow schema growth only: new rows, new form codes and re-coded cells are not a bump; an enum gaining a code is.

### 3.9 Checks

```sh
python3 scripts/check_vocabularies.py
python3 scripts/check_softwrap.py
python3 scripts/check_tables.py                        # --fix aligns tables; records/ excluded
python3 scripts/check_dependence.py datasets/<dataset> # the DIRECTORY, not data.csv
python3 scripts/build_codebook.py --check
python3 scripts/build_views.py --dataset <ds> --component <c> [--mechanism all] --check
python3 -m frictionless validate datasets/<dataset>/datapackage.json
```

Several of these can pass on the wrong question. `check_dependence.py` pointed at `data.csv` prints a message and exits 0 having checked nothing. `--mechanism all` is mandatory on `organizational_forms` and meaning-changing on `loss_mitigation_forms`. `frictionless` cannot see `allowed_values`; sweep values against the vocabulary by hand when adding rows. **A check that printed nothing and exited 0 has not necessarily passed — say which form you ran and what it printed.** House style: every Markdown file is soft-wrapped (one line per paragraph), and every table is padded to equal column widths.

---

## 4. `myfoamrepo` — the claims

### 4.1 The note model

A note is atomic: one claim, argued. If it argues two things, split it. Titles are argument-shaped and readable (spaces allowed): *The sea loan is a contingent claim not a loan*; *Homoplasy is the finding not the noise*. Wikilinks resolve by basename, case-insensitively. Every atomic note links to at least one thematic MOC and one project MOC.

```yaml
---
title: <matches filename>
type: permanent        # permanent | moc | source | reference
tags: [concept, concept]
project: HistorEE      # or erc-synergy, infrastructure
source-session: <slug of originating session>
database: [organizational_forms]   # optional: codebooks dataset(s) the claim draws on
created: YYYY-MM-DD
status: seed           # stub | seed | developed
---
```

Of the current notes, roughly 210 are `permanent` (arguments), 300 `reference` (archives, editions, tooling) and 25 `source` (literature).

### 4.2 Tags and the quarantined layers

`tags.md` is the controlled vocabulary. **Tags name concepts only** — what a note is about — never provenance (that is `project:` and `source-session:`) and never navigation (that is the MOCs). Three tag families are quarantined because they label infrastructure, not ideas: tooling (`tooling`, `htr`, `ocr`, `kuzushiji`, `scanning-hardware`), acquisitions (`acquisitions`, `book-trade`) and `archives`. Never put a concept tag on an infrastructure note, and never an infrastructure tag on an argument note. The test at the boundary: a claim that digitisation funding conditions what survives into view is an *argument* and belongs under `provenance`, `selection` or `legibility`.

### 4.3 MOCs

Maps of Content live in `mocs/` (28 at present): project hubs (`MOC - HistorEE`, `MOC - ERC Synergy Grant`), thematic hubs (`MOC - Entity-shielding and corporate forms`, `MOC - Risk-sharing vs risk-pricing`, `MOC - Islamic contract doctrine`, …), and a family of regional archive hubs (`MOC - Geniza archives`, `MOC - Japanese archives`, …) plus `MOC - Source editions`.

### 4.4 Validation and the graph

`scripts/validate_vault.py` checks frontmatter, the blank line after every heading, link resolution and tag vocabulary. Install the pre-commit hook once per clone:

```sh
git config core.hooksPath .githooks
git config merge.ours.driver true
```

The hook normalises headings, validates, and regenerates `graph/graph.html` (colour-coded, colourblind-safe, Dark2 palette). `scripts/new_note.py` scaffolds a schema-correct note. A failing validator aborts the commit — by design.

### 4.5 In this vault, a filename is a claim

Because titles are theses, **reading a list of filenames discloses arguments**. This is not a stylistic remark; it is the fact on which the whole blind protocol turns (logbook 4, 2026-08-16). A directory listing that looks like cheap orientation can spend a blind as thoroughly as reading the notes.

### 4.6 Reserved terminology (shared with the codebooks)

- **`genetic`** is reserved for biological heredity, never for institutional descent.
- **`convergence`** means strict cladistic convergence — independent arrival from *different* ancestral conditions. Where a shared ancestor is plausible the word is **parallelism**.
- **`hazard` ≠ `risk`.** A hazard is a peril conceived as an event, unpriceable; a risk is a peril conceived as a distribution, priceable and transferable. Much of the secondary literature writes "risk" for both; do not inherit that usage.
- **Units are instruments, not populations.** Institutions are transmitted as texts and drafting practices.

Writing register throughout: forensic, argument-led, no hedging or throat-clearing, British spelling, Chicago author-date. Unverified citations carry `[verify]` rather than being laundered into confident claims.

---

## 5. How the two repositories interact

The relation runs in five channels.

**1. The vault is the coder's evidence.** The protocol is explicit: code from the maintainer's own sources and vault notes where they exist, not from general knowledge. Where a vault note flags a question as open, the coding inherits `low` confidence and says so. Source notes (`type: source`) and edition notes record page offsets, holdings and editorial problems that a coder needs before opening a PDF.

**2. The `database:` field links claims to data.** A note naming `database: [organizational_forms]` asserts that its argument is anchored in that census; the graph draws an edge from the note to the dataset. Sixty-odd notes carry it at present.

**3. `source-session` slugs are the quarantine handles.** Every non-MOC note records the session it came from. `make_blind_bundle.py --withhold-sessions <slug,slug>` removes every note with those slugs from a bundle and then scrubs the MOC entries, Foam link-reference definitions and inline wikilinks that pointed at them. The slug is what lets an operator withhold material without reading it.

**4. Batches write to both trees.** A typical batch adds source notes and claim notes to the vault (with the batch slug as `source-session`, and entries in the relevant MOCs) and rows, logbook entries and `records/` files to the codebooks. The 2026-10-07 comanda batch, for instance, added eleven vault notes, edited three MOCs, and added 84 rows across both censuses.

**5. One doctrine, two places.** Reserved terminology, the soft-wrap rule, the "no `git` from the sandbox" rule and the provenance stance are identical in both `CLAUDE.md` files. A rule changed in one must be checked against the other.

The tension inside channels 1 and 3 is the methodological centre of the project: a session that has read the vault cannot un-read it, so the same notes that *inform* an open coding *contaminate* a blind one.

---

## 6. Coding sessions

### 6.1 Kinds of session

| Kind                        | What it tests                                              | Where results land                  | Example                                         |
|-----------------------------|------------------------------------------------------------|-------------------------------------|-------------------------------------------------|
| **Open batch**              | Nothing beyond the coding itself; no blind to spend        | `data.csv`                          | Crown of Aragon *comanda*, 2026-10-07           |
| **Blind batch**             | Whether expectations survive contact with sources          | `data.csv`, scored against priors   | `shielding-witness`, 2026-09-05                 |
| **Blind re-code**           | The coder (model or person), not the evidence              | `recodings.csv`, adjudicated later  | Opus 5.5 re-code of the mutual pole, 2026-09-26 |
| **Primary/secondary pilot** | Whether secondary-literature codings survive the documents | `recodings.csv` with `source_class` | Commenda notarial pilot, 2026-09-28             |

The maintainer judged the 2026-09-26 blind re-code only moderately informative — it tested the model's interpretation, not the quality of the evidence — and the current emphasis has moved towards open sessions on new material and towards primary-versus-secondary contrasts. Newly acquired material that no session has read is the cheapest occasion for a genuine blind; material the project has already discussed rarely is.

### 6.2 Two chats, never one

A blind batch splits across separate sessions, and the split is the point.

```
 Chat A — OPERATOR                Hinge — MAINTAINER            Chat B — CODER
 reads vault & live matrix   →    commits PRIORS file      →    works ONLY in bundle
 chooses forms, checks Zotero     before any source opens       writes priors first
 measures page offsets            grants only bundle folder     reads sources, codes
 writes selection brief           opens fresh chat              freezes record (sha256)
   + withheld predictions                                       answers the six questions
 files budget row in logbook 4                                        │
 builds blind bundle                                                  ▼
                                  Grant — MAINTAINER        →   Chat B tail / Chat C — APPLICATION
                                  lifts data.csv prohibition    verifies destination tree
                                  "in so many words"            writes schema → vocab → rows
                                                                regenerates codebook & views
                                                                copies record into records/
                                                                logbooks, CHANGELOG, commit msgs
                                                                re-runs checks
                                  Maintainer commits.
```

**Chat A, the operator**, spends the blind: it reads the vault, chooses the forms, verifies holdings, computes which values have zero or one instance in the matrix, declares any co-occurrence before rows exist, and writes a selection brief to `records/` containing a **withheld-predictions** section for the maintainer only. It specifies the `make_blind_bundle.py` command. It never codes.

**The hinge** belongs to the maintainer. The coder writes its priors into the bundle; the maintainer copies that file to `records/PRIORS-<slug>-<date>.md` and **commits it before the coder opens a source**. A file's modification time proves nothing; a commit that precedes another commit is evidence. An audit on 2026-09-08 found one priors file against four blind batches — most earlier falsification claims rested on narrative written in the same session as the coding.

**Chat B, the coder**, works only inside the bundle (e.g. `~/GitHub/_blind-<slug>-<date>`). It does not look at the live repo or the real vault, and treats every hole in the bundle's vault as a hole the scrubber made, never as evidence. It fixes every cell before computing anything about the matrix, and freezes its record before the live tree is granted.

**The prompt is the one channel a bundle cannot scrub.** Read it back against the withheld section and delete every sentence that appears in both. The same applies to any loaded skill or procedure file: on 2026-09-07 a worked example in the coding skill was found to contain the answer to a cell under blind coding.

### 6.3 What every coding pass hands back

A proposed rows CSV with **placeholder** ids (`OF-XXXX-01`; the maintainer assigns real ids at merge), proposed form-type rows if the form is new, a `NOTES-…md` coding record, the priors, the prompt, a logbook draft and a commit message. And three explicit parts of the deliverable:

- **(a)** the row fragment, every row carrying a real short citation or `[verify]`;
- **(b)** cells declined, and why — silence (`.NR`), inapplicability (`.NA`), or no fitting value in the vocabulary;
- **(c)** adjudications for the maintainer — every point where a call was made, with the alternative reading stated fairly.

Plus six plain answers: what was coded and on what evidence; what could not be coded and why; which of one's own expectations were falsified; any characteristic that did not fit; any dependence or well-formedness problem noticed and not repaired; what to acquire next and which cell it would move.

### 6.4 The blind economy

Blind is a consumable, spent by reconnaissance at least as often as by reading. Climb no higher on this ladder than the question requires, and **write the question down before climbing**:

| Rung | Instrument                                         | Spends                                  |
|------|----------------------------------------------------|-----------------------------------------|
| 0    | Catalogue metadata (held? attachment? DOI?)        | Nothing about content                   |
| 1    | Counts (term hits, notes per slug, cells per form) | Almost nothing                          |
| 2    | Structure (page count, offset, table of contents)  | A source's shape, not its claims        |
| 3    | Field values (`source-session` slugs, tags, dates) | Metadata without rendering notes        |
| 4    | **Titles and filenames**                           | ⚠️ Looks like rung 1, costs like rung 5 |
| 5    | Bodies, abstracts, coded values                    | Everything on the topic                 |

Draft the standing-table row in logbook 4 before reconnaissance, as a budget; reconcile it after; a row that ends higher than budgeted must say what forced it. A count can prove a vault clean on a topic; only a title can prove it dirty — so accept "clean" and stop. Record spend per topic (frame versus mechanism, form versus characteristic), not as a binary. A spent blind never un-spends, and deleting a bundle does not un-spend it either. When the blind is already spent, say so and run an open pass with the spend disclosed: that is worth more than bundle theatre.

### 6.5 Application

Only after the maintainer lifts the `data.csv` prohibition explicitly, for a named tree. In order: verify the destination tree matches what the batch assumed (everything except the scrubbed `data.csv` and logbooks should be byte-identical to the bundle); schema fixes first if they unblock the batch; vocabulary rows; data rows (a re-coding edits in place and mints nothing; new ids come from the live file, never from arithmetic); regenerate `codebook.md` and the views; copy the batch record into `records/` and `cmp` each copy; logbook entries; CHANGELOG; commit messages hard-wrapped at 72; re-run every check. CSVs are written with LF line endings (`csv.writer(lineterminator='\n')`), since Python defaults to CRLF and CI rejects it.

### 6.6 What counts as a result

Judge a batch by what the matrix learned, not by cells filled. **A proposal that codes every cell is a failed proposal**: a densely filled row reports diligence, not structure. Count `.NR` per component, not only in total — a row can carry twenty-three substantive cells and leave three components empty, and the empty component is the finding. Report new value-instances and new component signatures separately. An uncoded row with a reasoned refusal is a result (`confraternita`, `joint_stock`). And **add forms, not features**: two new forms in one session produced two falsifications where no amount of reasoning produced any.

---

## 7. Who does what

**The maintainer, always:** every `git` operation (commits and pushes are made by hand in VS Code, signed); granting folders to sessions; lifting the `data.csv` prohibition; theory calls — promoting a characteristic into a component set, declaring a claim set, any comparative claim; adjudicating re-codings; deletions and renames of anything one did not create.

**Assistant sessions (Claude):** read granted folders; run scripts and read-only diagnostics; draft rows, notes, logbook entries, CHANGELOG blocks and commit messages; write to the live tree once told to. Never `git`, not even `git status` inside a bundle — the sandbox leaves `index.lock` files that block the maintainer's client. Every session ends by writing a session record (`claude/<slug>-<date>.md`) to the claude.ai project, which is what the next session reads.

**A collaborating researcher** may take any of four roles, and should know which one a given session puts them in:

- **Coder** — enters codings under their own initials, from sources they have read, following `CONTRIBUTING.md` and the `code-a-form` protocol.
- **Reviewer/adjudicator** — second pair of eyes on proposed rows; fills `reviewed_by` and `review_status`; proposes adjudications on `recodings.csv`.
- **Operator** — designs a batch, builds a bundle, writes the prompt, and thereby spends the blind on that material for themselves.
- **Source provider** — identifies, acquires, catalogues and makes readable the material a batch codes from; often the most consequential role of the four.

Formally, new contributors work on a branch (`coding/<dataset>-<name>`), open a pull request using the template, and merge only after review; `main` is protected and schema, data and vocabulary changes require CODEOWNERS approval.

---

## 8. Skills the collaborating researcher needs

### 8.1 Indispensable

**Source competence in at least one of the project's traditions.** The census is only as good as the reading of the passage cited in `source_ref`. For the Mediterranean and Islamic strand that now means documentary Arabic, Judaeo-Arabic or Hebrew (the Cairo Geniza above all); for the East Asian strand, classical Chinese and pre-modern Japanese, including *kuzushiji*; for the European strand, Latin, the Romance vernaculars and the relevant notarial formularies. The decisive skill is not translation but **knowing what a source does not say** — distinguishing silence (`.NR`) from absence (`0`) from a source that denies the question its determinacy.

**Legal-historical literacy.** Most characteristics are legal properties (who may force partition; whose creditors rank first; whether an entity sues in its own name). A researcher must be able to read a clause for its locator and its limbs, and to see when a modern scholar's functional gloss is being passed off as the tradition's own articulation.

**Source hygiene.** Locating material in Zotero by source-language terms and by author, not by collection; detecting duplicate records (the attachment is usually on the worse one); measuring printed-to-PDF page offsets oneself against running heads; distinguishing an electronic reissue's pagination from a reset edition's; recognising that a "scanned image" verdict often hides a usable OCR layer (`pdftotext` failing for a missing `poppler-data` language pack) and that recovered OCR corrupts numbers — any figure entering a cell is read from the page image. Citations are verified (DOIs through CrossRef, not memory) before entry.

**Methodological discipline.** Comfort with the four missingness states, with `P` as structure rather than hedge, and with the rule that discriminating power is free. One need not be a systematist, but one must read `CHARACTER-CODING.md` and be prepared to object when a request would license an unweighted similarity claim or launder silence into absence. The literature behind it (Sereno 2007; Vogt 2018; Haspelmath 2010; Rieppel 2002, 2007; Campbell and Fiske 1959; Marx and Duşa 2011) sits in the Zotero collection `method — typology and character coding`.

### 8.2 Technical, learnable in a week

- **Git and GitHub**: clone, branch, commit (signed), pull request, reading `git log` and `git blame`. No more is required.
- **VS Code** with the Foam extension and Rainbow CSV or Edit CSV.
- **Markdown** with YAML frontmatter; the soft-wrap and table-alignment house rules.
- **Plain-text CSV**: quoting, UTF-8, the danger of spreadsheet round-trips.
- **Running Python scripts** from the command line (`python3 scripts/…`) and `pip install frictionless`. Writing Python is useful, not required; the scripts are standard library and documented in their headers.
- **Zotero**, including linked-file attachments and the `Extra` field for container warnings and page offsets.
- **OCR and PDF tooling** at user level: `pdftotext`, `pdftoppm`, an HTR/OCR engine for the relevant script.

### 8.3 Working with assistant sessions

Most coding is currently done by Claude sessions under the maintainer's direction, and a researcher operating or reviewing them needs four habits. Treat every assistant coding as a proposal. Keep chats separated as §6.2 requires, and open the coding chat with only the bundle folder granted. Read prompts back against withheld predictions before sending them. And check claims by count rather than by sample — on 2026-09-08 a "house practice" flagged from three rows turned out to be the majority practice.

Three packaged procedures (Claude skills) encode the protocols and are worth reading as documents in their own right, whether or not one uses them:

| Skill                         | Use                                                                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `code-a-form`                 | Turn literature on one form into proposed rows: orientation, source checks, missingness, the three-part deliverable |
| `run-a-coding-batch`          | The envelope: blind bundle, separate chats, blind economy, application pipeline                                     |
| `bookmark-collection-to-foam` | Turn an online collection, finding aid or archive portal into a reference note in the vault, linked to its MOC      |

---

## 9. Tangential issues

### 9.1 Publicity and confidentiality

Both repositories are public and every push is publication. Withheld predictions, priors and prompts committed to `records/` are therefore public too — deliberately, since that is what makes the blind checkable — but it follows that **a coder who is to work blind must not browse the public GitHub repository or the claude.ai project files** any more than the live tree. Unpublished material from collaborators, restricted archival transcriptions and anything under a non-commercial licence must not be committed without resolving the licence first; a dataset folder may carry its own overriding `LICENSE`, and a vault note may narrow its terms with a `license:` field. Never write a personal cloud-storage path into `source_ref`: it resolves for nobody else.

### 9.2 Where things live

GitHub holds the data and the notes. Google Drive holds the grant application, the decision log, the bibliography, the deliverables register and this manual. Zotero holds the sources, and is the place a source must exist to be cited properly — a loose PDF in a cloud folder is the weaker arrangement, and a citation resting on one is treated as unverified until its metadata is confirmed. The claude.ai project holds the session records that give continuity between assistant sessions.

### 9.3 Known standing defects

Do not be surprised by them, and do not repair them inside an unrelated batch: 130 cells (101 organisational, 29 loss) carry nothing in `source_ref` but `[verify]`, none of them `articulated`; a handful of live notes still cite `proposed-of/`; several characteristics are flagged in the vocabulary as borrowed from one tradition (`AP4`, `MG4`, `FP4` are *waqf*-shaped). The rule is to flag, count and leave — a defect is repaired in its own commit, not inside the batch that discovered it, unless it blocks that batch.

### 9.4 Vocabulary gaps

When the allowed values have no cell that fits, the coding is `.NR` with a flag, never the nearest wrong value. New characteristics are proposed only to repair a conflation (one column silently asking two questions), never to add resolution, and never in the same batch as the coding that motivated them. Even `source_lang` has gaps (there is at present no code for Catalan); a new enum code is a minor version bump.

### 9.5 The open methodological question

The project has not settled what a re-code tests. A model re-coding from the same pages tests interpretation; a primary-source pass against secondary codings tests the evidence; neither tests the matrix's theory. The forthcoming Geniza work, and the new Zotero primary-source collections, are where this will be pushed next. A researcher who arrives with views on inter-coder reliability, on qualitative comparative analysis, or on how documentary corpora behave as samples has a real contribution to make here.

### 9.6 The grant context

The codebooks' DOI is cited in footnotes of Part 1 and Part 2 of the ERC Synergy application, and the vault's in Part 2. Releases freeze citable snapshots; the concept DOIs always resolve to the latest release. Anything a researcher adds may end up cited in a grant document within weeks, which is one more reason for the provenance discipline.

---

## 10. First-week checklist

1. Clone both repositories into `~/GitHub/`; install the vault's pre-commit hook; `pip install frictionless`; run the full check suite on both and confirm it is green.
2. Read, in this order: codebooks `README.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `CLAUDE.md`, `EDITING-CSV.md`, `records/README.md`; vault `readme.md`, `CLAUDE.md`, `tags.md`, `glossary.md`.
3. Read both characteristic vocabularies in full, definitions included.
4. Open three views in `views/` and one completed batch end to end: its `records/NOTES-…` files, its logbook 4 entry and its CHANGELOG block. The 2026-10-07 comanda batch is recent and open; the 2026-09-05 `shielding-witness` batch is the clearest blind one.
5. Read the vault note *Blind re-coding workflow - operator, coder, application* and logbook 4's standing table of spent-blind slugs.
6. **Before step 5, decide with the maintainer whether you will be asked to code blind on any material soon.** If so, skip what that material would spend and ask which slugs to avoid. Reading the vault is irreversible.
7. Code one form from one source in a scratch copy, as a proposal, and have it reviewed.

---

## 11. Short glossary

**Articulation** — whether a value is stated by the tradition (`articulated`) or imposed by the analyst. **Blind bundle** — a working copy built by `make_blind_bundle.py` from which withheld material is physically absent. **Component** — one of the nine declared subsets of characteristics licensed for comparison. **Form** — a coded institutional type (`type_id`). **MOC** — Map of Content, a hub note. **Operator** — the session that selects forms and builds the bundle, spending the blind. **Priors** — expectations written and committed before any source is opened. **`records/`** — the tracked, verbatim batch record. **Slug** — the `source-session` identifier on a vault note and the name of a batch. **Spent blind** — material a session has read and can no longer code blind. **Standing table** — the list in logbook 4 of slugs and what each spent. **View** — a generated matrix for one component.
