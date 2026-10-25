# Bundle: `venetian-pass-2026-10-25` (Venetian acts, 14 cells)

**This is a prepared copy for one coding chat.** It is not the live repository. Do not look for the live repository, the vault, Zotero, the web, the claude.ai Project or any memory file. The kickoff prompt governs the procedure; this file says what is here and why.

## Sources (`sources/`): one edition, Latin only

| file | what it is |
| ---- | ---------- |
| `morozzo-lombardo-1940_acts-1-865_latin.txt` | R. Morozzo della Rocca & A. Lombardo (eds.), *Documenti del commercio veneziano nei secoli XI–XIII*, 2 vols. (Rome 1940): **all 865 acts, the Latin only**, extracted by the operator from the OCR text layer of the BEIC reproduction. Each act is headed `=== act N \| vol. I/II \| p. P ===`, P being the printed page on which its text begins. The file's own header states its provenance and its rights, which are outside this deposit's CC BY 4.0 grant. |

**Removed from the source:** the editors' regests (the Italian heading above each act), their archival and description lines (holding, condition, size, endorsements), their notes, introductions, errata and indexes. These are the editors' writing, and this pass reads none of it. Nothing else is supplied: no page images, no PDF.

**What remains:** the documents' text as the edition prints it, with the editors' bracketed restorations.

**The text is OCR, and it shows:**

- misread letters (`l` for `t`, `e` for `c`, `el` for `et`, `lu` for `tu`);
- words displaced where the scanner read a page out of order, most often in an act's dating clause;
- rarely, a lost line at an act's opening, or a stray fragment of the editors' apparatus the script did not remove. Ignore such fragments; they are not evidence.

Quote every passage that carries a cell with its act number and page. Every such quotation will be checked against the page image at adjudication.

**The edition is one corpus, and a selection.** It prints the acts its editors chose, from the archives that kept them. Frequencies over it describe the printed set, not Venetian practice. Say so wherever you report one.

## Also here

- `cells-in-scope.csv`: the 14 cells, with `record_id` and the `recoding_id_blind` pre-assigned.
- `scope/types-in-scope.csv`: name, tradition and period of the three rows in scope, and of `commenda`, which `commenda_alloc` cross-refers to and which is not in scope.
- `vocab/`: **only** the characteristics in scope, plus `LR2`, on which `LR6` depends. The loss vocabulary's `exemplar` column is dropped, as in every bundle.
- `schema/`: both `datapackage.json` files.
- `doctrine/`: `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md` (redacted), `EDITING-CSV.md`.
- `templates/`: the `recodings.csv` header of each census.
- `instances-header.csv` and `instance-chars-header.csv`: the act-level tables you fill.
- `PRIORS-TEMPLATE.md`: the priors you fill before reading.
- `proposed-of/`: where everything you write goes.

## What is deliberately NOT in this bundle

- No `data.csv` of either census, no logbooks, CHANGELOG, codebooks, views, `records/`, vault or earlier bundles.
- No characteristic outside the 14 cells' own, except `LR2`. **The vocabularies are cut down this time**, not only redacted: the definitions of several other characteristics now carry rulings that name the forms under test and their values, and a minimal bundle leaks less than a scrubbed one.

## Redactions

- **Where they are:** one worked case in `doctrine/CHARACTER-CODING.md` (test 1); one sentence in the `CI1` definition in `vocab/`; one word in the loss census's dataset description in `schema/`.
- **How to read the markers:** each is `[withheld 2026-10-25: names a form under re-coding]`. A marker says only that something was removed. Do not guess what.

## Known leaks that could not be removed (list them in your priors' exposure section)

1. **The type name of `societas_maris`: "Societas maris (the bilateral commenda; Venetian collegantia)".** It equates the Venetian *collegantia* with the bilateral form, and its "bilateral" collides with `CF3`'s value `bilateral`, which counts principals, not contributors of capital.
2. **The period of `societas_maris`: "c.1073-early 13c (Venice)".** It is the census's dating of the form in Venice, and it bears on any expectation about change over time.
3. **The type name of `commenda_alloc`: "Commenda (loss-allocation aspect)".** It states `MC1 = allocation` for that row. Treat `commenda_alloc MC1` as not blind; it is scored apart.
4. **The doctrine's reasoning about a class.** `doctrine/CHARACTER-CODING.md`, test 4, states why `AP3`, `LR1`, `CF2` and `LR6` were grouped as `agent-loss-exposure` "for bilateral capital-labour contracts". It names no form, but both forms under test belong to that class.
5. **The `LR6` definition** contrasts "a qirad agent holding a call" with "an isqa manager holding a debt". Neither is in scope, but general knowledge relates the *qirāḍ* to the commenda.
6. **General knowledge.** You know the historiography of the commenda and the *colleganza* from training. No bundle removes that. The priors template asks you to write it down, so that it can be kept apart from what the acts say.
7. **The `code-a-form` skill** names "commenda" in its description as an example. It states no value.
