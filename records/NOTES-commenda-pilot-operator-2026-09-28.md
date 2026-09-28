# Operator brief: the commenda pilot, primary against secondary (2026-09-28)

**Maintainer only. Never place this file, the pilot design, or the Project doc of the same name in a coding chat's reach.**

- **The design:** `Claude outputs/PILOT-DESIGN-commenda-primary-secondary-2026-09-27.md`. Its §§9–10 are operator-only.
- **This brief:** records how the design was built into two bundles, and what MS does next.
- **The operator:** the chat of 2026-09-26 to 09-28. It is spent on these rows and never codes them; see its standing-table row in logbook 4.

## Passes and ids

| arm | pass slug | bundle | ids, organizational_forms | ids, loss_mitigation_forms | `condition` |
|---|---|---|---|---|---|
| S | `commenda-secondary-2026-09-28` | `~/GitHub/_blind-commenda-secondary-2026-09-28` | OF-R0065–R0106 | LM-R0001–R0019 | `blind` |
| P, stage 4 | `commenda-primary-2026-09-28` | `~/GitHub/_blind-commenda-primary-2026-09-28` | OF-R0107–R0148 | LM-R0020–R0038 | `blind` |
| P, stage 5 | `commenda-primary-2026-09-28` | same | OF-R0149–R0190 | LM-R0039–R0057 | `open` |

**Scope:** 61 cells, each arm and stage. `commenda` has 21 cells, `organizational_forms` `societas_maris` 21, `commenda_alloc` 10, and `loss_mitigation_forms` `societas_maris` 9. The per-cell assignment is in each bundle's `cells-in-scope.csv`. Rows carry `source_class` (logbook 1, 2026-09-27).

## What each bundle holds, and the departure from precedent

**Both bundles are minimal:**

- `doctrine/`: CLAUDE, CONTRIBUTING, CHARACTER-CODING, EDITING-CSV;
- `schema/`: both datapackages;
- `vocab/`: both characteristic vocabularies;
- `scope/types-in-scope.csv`: code, name, tradition and period only;
- the recodings headers and templates;
- `sources/`.

They carry **no `data.csv`, logbooks, CHANGELOG, codebooks, views, `records/`, vault or earlier bundles.** This departs from the full-repository bundles of 2026-08 to 2026-09-26. The reason: the commenda family runs through the logbooks, the neighbouring rows' notes and the vault from the census's first weeks, and scrubbing all of it would take a residual-mention pass larger than the pilot. Including less leaks less. The cost is that the coders lose house practice from other rows. The doctrine files carry the rules; the calibration of other rows' notes is gone.

**Arm P sources:** transactional only.

- **Scriba I:** acts only, PDF pp. 66–501 plus the errata on p. 504.
- **Cassinese I:** acts only, PDF pp. 22–459.
- Both editors' introductions are removed. Scriba's discusses the *accomendaciones* and the *socius stans*.
- **Amalric 1248:** all 104 notulae of Pryor 1981, Latin only, extracted by script:
  - chapter commentary, English headnote summaries, introduction, glossary and index removed;
  - each notula keeps its archival reference and marginalia;
  - the extraction was verified to be complete (1–104, none empty) and screened for English leakage (none above 1% of a notula's words).

**Arm S sources:** the works the live rows cite, as held:

- van Doosselaere 2009;
- Harris 2007 (conference draft, no printed pages);
- Held 2025 (OCR'd copy; the *MHR* contracts are reached through it);
- Udovitch 1962;
- Harris 2020;
- González de Lara 2002.

**Cited but not held:** Pryor 1977 (3 cells), Puga & Trefler 2014 (1), Merelo-Guervós & Molinari 2025 (1, file missing on disk). The coder is told to code from what is held or `.NR`, and to say so.

## Redactions, and leaks that could not be removed

**Redacted,** in both bundles' copies only, each marked `[withheld 2026-09-28: …]`:

- `CHARACTER-CODING.md`: the `LR2` worked case naming the commenda;
- the `AP3` definition: the commenda worked example quoting Harris 2007, 11, and two lists of named rows;
- the `LR1` definition: one list of named rows;
- the `LS3` definition: the list of rows it is not coded for;
- the loss datapackage description: "commenda" among its allocation examples.

Every replacement was asserted to match exactly once. The loss vocabulary's `exemplar` column is dropped. A re-scan of `doctrine/`, `schema/` and `vocab/` for 21 terms found no remaining mention outside the markers. The residual hits were false positives, plus one `LS3` sentence about the sea-loan family, which is out of scope.

**Disclosed to the coders, not removable:**

1. The code and name `commenda_alloc`, "loss-allocation aspect", imply its `MC1`. **Score `MC1` on that row apart.**
2. `societas_maris` is named "the bilateral commenda; Venetian collegantia". That is definitional.
3. Training knowledge. Arm P's priors must write the textbook commenda down clause by clause.
4. The `code-a-form` skill names the commenda as an example institution.

**Channel check.** Both prompts and READMEs were read against design §§9–10:

- No observability prediction appears in them.
- One sentence was removed from prompt P: it defined the sea loan by a coded trait (`RB4`).
- In the same edit, sea loans were taken out of the sample (they are still counted in the type census), since no sea-loan row is in scope.

## Findings made while building, which correct the design

- **Blancard 1884 vol. II is Amalric's cartulary** ("Les notules commerciales d'Amalric", per Pryor's abbreviations), not vol. I as the design guessed. The PDF held (HF8ME3N7) begins at printed p. 301 with nos. 1026–, so **only the tail of the unselected cartulary is held**. The bulk (Pryor's references run to no. 991 and below) is in the part not held. Blancard gives many acts only as French analyses. Acquisition: the first half of Blancard II.
- **Pryor 1981 needs no OCR:** Zotero's reader misreported its text layer.
- **QTEG4PM7's second file is not Scriba's acts.** It is probably Moresco & Bognetti's description of the registers, and is misfiled.

## What MS does next, in order

1. **Commit** this brief, both prompts, both manifests, the logbook 4 rows, and the `source_class` change (its commit message is in `proposed-of/`).
2. **Open chat S and chat P**, each fresh, on Opus 5.5 at high, **outside the claude.ai Project**, each granted only its own bundle. Paste the text of `records/PROMPT-commenda-secondary-2026-09-28.txt` and `records/PROMPT-commenda-primary-2026-09-28.txt` below the line.
3. **Priors, per chat.** When a coder prints its priors hash:
   - `cp ~/GitHub/_blind-commenda-<arm>-2026-09-28/PRIORS-commenda-<arm>-2026-09-28.md ~/GitHub/HistorEE_codebooks/records/`
   - `shasum -a 256` the copy, and check it equals the hash the coder printed;
   - commit;
   - reply "committed, hash matches".

   This is the step that failed on 2026-09-26: the template was committed instead of the filled file.
4. **When both S and P report their freeze hashes, bring them back to this operator chat** (or an application chat given this brief). It will:
   - verify both frozen records against the hashes;
   - prepare `reveal/REVEAL-commenda-2026-09-28.csv`, holding the live value and note, and arm S's value and note, per cell;
   - place it in the arm P bundle.

   Then tell chat P to continue with stages 5–6.
5. **Application,** after P's stages 5–6, by a fresh chat under the `run-a-coding-batch` pipeline:
   - append all three row sets to `recodings.csv`;
   - fill `value_at_recoding` and `agreement`;
   - copy the records;
   - score per the design §§1 and 8: the four difference classes, the anchoring measure, and the observability predictions of design §10.

## Bundle manifests

`records/MANIFEST-commenda-primary-2026-09-28.sha256` and `records/MANIFEST-commenda-secondary-2026-09-28.sha256` hold the sha256 of every file in each bundle as built. At application, `shasum -a 256 -c` against the bundle, excluding `proposed-of/`, `reveal/` and the filled priors, shows whether a coder changed anything outside its remit.
