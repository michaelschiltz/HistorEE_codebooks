# Commenda pilot — applied (2026-09-28)

**Status: applied and committed; adjudication open.** Written by the application chat (standing slug `commenda-pilot-application`), which read every value and must never code these rows. This record points to the canonical files; where they and this page disagree, the files win. It follows `claude/commenda-pilot-design-2026-09-27.md`, whose decisions 2 (run arm S), 4 (instance table in `records/`) and 5 (`source_class`) are now implemented. Decision 6 (the eleven absent characteristics) was left as recommended, and decision 7 (Scriba II, Cassinese II) is still open.

## What landed

- **183 rows** in `recodings.csv`: OF-R0065–R0190 (126) and LM-R0001–R0057 (57), the loss census's first. Three row sets:
  - arm S, `commenda-secondary-2026-09-28`, `blind`;
  - arm P stage 4, `commenda-primary-2026-09-28`, `blind`;
  - arm P stage 5, the same pass, `open`.

  All `claude-opus-5-5` at `high`, all `adjudication=pending`. Only `value_at_recoding` and `agreement` were filled. `data.csv` is unchanged.
- **Before writing**, the application verified:
  - all 22 frozen hashes;
  - both manifests;
  - the filled priors and the reveal, found in the committed tree by reading `.git` objects;
  - the join to `data.csv`;
  - zero drift between `data.csv` and the reveal file.
- **Housekeeping, later the same day:**
  - five resolved patches moved from `proposed-of/` to `records/`, and ten citations repointed, two of them in `vocabularies/organizational_form_type.csv`;
  - the coders' own logbook drafts and commit messages copied into `records/`;
  - both bundles snapshotted into `records/BUNDLE-commenda-{secondary,primary}-2026-09-28/` without their PDF extracts (29 files, all hash-verified against the manifests, including the Amalric Latin extract), then deleted;
  - 40 spent drafts deleted from `proposed-of/`.
- **Commits (MS):** "coding on basis of primary and secondary sources successfully completed"; "note added to logbook"; "housekeeping spent and redundant files in the repository after the coding session". **Uncommitted as of 2026-09-29:** four marked corrections, in logbook 4 (3) and `CHANGELOG.md` (1), and the vault note's pointer to the bundle snapshots.

## Headline results, before adjudication

- **Values agreeing, of 61:** arm S with live 52 (the rater effect, Opus 5 → 5.5); stage 4 with arm S 40 (the evidence effect); stage 4 with live 40; stage 5 with live 43.
- **The four kinds, stage 4 against live:** 10 outrunning, 9 compression losses, 6 compression errors, 3 primary gains.
- **Anchoring:** 5 of 61 values revised at stage 5, none away from live. Three landed exactly on live, and chat P flagged all three as prompted by the reveal; without them, stage-5 agreement is 40, the stage-4 figure.
- **Observability:** 44 of 48 of the operator's withheld predictions held. The acts speak to the contract's internal terms and are silent on outside creditors, personhood and proof of loss.
- **Not a corroboration.** Primary and secondary share one evidence base; the effective n is three notaries; every coder is a Claude model.

## Where things are

- **Scores, dependence, falsified priors, standing rows:** logbook 4, 2026-09-28.
- **The coders' source findings:** logbook 5, 2026-09-28 (ii).
- **Housekeeping:** logbook 1, 2026-09-28.
- **Summary block:** `CHANGELOG.md`, 2026-09-28.
- **The coding record:** `records/`, including priors, prompts, manifests, reveal, both arms' notes, the frozen rows as `PROPOSED-RECODINGS-…`, the instance layer and the bundle snapshots.
- **Adjudication worksheet:** `proposed-of/ADJUDICATION-commenda-pilot-2026-09-28.md`: 24 entries, ordered disputes, then revisions, then S-only, with no decision filled.
- **Workflow note in the vault:** `Primary against secondary coding workflow - three arms, reveal, application`. Withhold slug `commenda-pilot-application` from any bundle that codes notarial acts.
- **Want-list:** Morozzo della Rocca & Lombardo, *Documenti* (1940, 2 vols; repr. 1971) and *Nuovi documenti* (1953), in `Source editions - Italian and Mediterranean commerce`.

## Open for MS, in order

1. **Adjudicate the 24 cells.** Four definitional questions come first, because their answers bind other rows:
   - is a formulary absence an observed `0`/`none` or `.NR`? (Both `RB3` revisions rest on it.)
   - can a minority clause make a cell `P`?
   - `commenda CI1`: `common` against `none`;
   - `commenda_alloc VF1`/`VF2` when no loss is ever claimed.
2. **Carried scoring notes:**
   - `RB3` on both loss rows: right value, unsupported basis;
   - the five `P` cells against the rule that a frequency never becomes `P` (all five are the modal state at the level of individual acts, not a blend);
   - eight arm-P `.NA` rows carrying `source_class=primary-transactional`.
3. **Flagged, not repaired:**
   - the loss `datapackage.json` names nonexistent vocabulary files (`cooperative_pooling_*`);
   - logbook 5, 2026-08-30, contradicts arm S on whether Harris 2007 has page numbers;
   - `records/README.md` says "currently one" priors file, where there are five;
   - `logbook/4-appendix-…csv` has CRLF endings in the working copy;
   - one live cell cites "Harris 2020" without a title.
4. **Vocabulary misfits reported by both arms:** `LR1` (extent and form); `LR3` (name against definition); `RB1` (labour at risk); `TS2` (multi-voyage); `RB3` (secures what, against what); `CI1` (common stock with separate side placements); the drafting-term frame, which mixes land and sea partnerships.
5. **Unaudited:** the older blind bundles in `~/GitHub` and `~/`. Check that their records reached `records/` before deleting any.
6. **Acquisitions, by the cell each would move:**
   - Morozzo & Lombardo: the Venetian half of `societas_maris`, and `VF1`/`VF2`;
   - Genoese notaries between 1161 and 1190 (*Notai liguri*): time against hand;
   - Pryor 1977: arm S's shared upstream;
   - González de Lara 2008: `VF1`;
   - Amalric's unprinted notulae: Blancard's selection bias.
7. **Next pilot:** the seven repairs are listed in the vault note. They include pre-registering the formulary-absence rule, fixing the frame (sea against land) in the design, and having stage 5 write its instance changes to a file.

## Corrections made after the fact (2026-09-29)

- Logbook 4 misattributed the `shared` variant of `commenda_alloc RB1`: it is Cassinese 362, not Amalric.
- `CHANGELOG.md` said git confirms the priors were committed "before the coding". It confirms only that they were committed before the freezes.
- The application chat's standing-table row now lists its later vault reads and web searches.
