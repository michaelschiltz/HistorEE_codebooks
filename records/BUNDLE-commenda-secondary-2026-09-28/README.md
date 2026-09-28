# Bundle: `commenda-secondary-2026-09-28` (arm S: secondary sources only)

**This is a prepared copy for one coding chat.** It is not the live repository. Do not look for the live repository, the vault, Zotero or the web. The kickoff prompt governs the procedure; this file says what is here and why.

## Sources (`sources/`): the works the live rows cite, as far as they are held

| file | item |
|---|---|
| `vanDoosselaere2009.pdf` | van Doosselaere, *Commercial Agreements and Social Dynamics in Medieval Genoa* (2009) |
| `Harris2007_conference_draft.pdf` | Harris, "The Institutional Dynamics of Early Modern Eurasian Trade: The Corporation and the Commenda" (2007 conference draft; **it carries no printed page numbers**: cite PDF pages and say so) |
| `Held2025_ocr.pdf` | Held, "The Contract of Collegantia in the Late Medieval Law of Dubrovnik (Ragusa)" (2025), OCR'd copy. The Ragusan contracts (*MHR* I–IV) are reached only through this article. |
| `Udovitch1962.pdf` | Udovitch, "At the Origins of the Western Commenda: Islam, Israel, Byzantium?" (1962) |
| `Harris2020.pdf` | Harris, "General Average and All the Rest" (2020) |
| `GonzalezdeLara2002.pdf` | González de Lara, "Institutions for contract enforcement and risk-sharing" (2002) |

**Cited by the live rows but NOT held:**

- Pryor 1977, "The Origins of the Commenda Contract";
- Puga & Trefler 2014;
- Merelo-Guervós & Molinari 2025.

Do not reconstruct them from memory. If a cell can only be answered from them, code it from what is held, or `.NR`, and say so in the note.

## Also here

`cells-in-scope.csv`: the 61 cells, with the `recoding_id` pre-assigned.

## What is deliberately NOT in this bundle

- No `data.csv` of either census, and no logbooks, CHANGELOG, codebooks, views, `records/`, vault or earlier bundles.
- The re-coding must not see the census's reasoning about these forms, and **a minimal bundle leaks less than a scrubbed copy of the whole repository.** This departs from the full-repository bundles of 2026-08 to 2026-09-26 on purpose. The doctrine files carry the house rules; house practice from other rows is not needed.

## Redactions

- **Where they are:** passages naming a form under test were redacted in `doctrine/CHARACTER-CODING.md`, in the `AP3`, `LR1` and `LS3` definitions in `vocab/`, and in the loss census's dataset description in `schema/`.
- **How to read the markers:** each redaction is marked `[withheld 2026-09-28: …]`. A marker tells you only that a passage was removed, not what it said. Do not guess.
- **`exemplar`:** the loss vocabulary's `exemplar` column is dropped entirely, as in every bundle.

## Known leaks that could not be removed (list them in your priors' exposure section)

1. **The loss-census form code `commenda_alloc`, named "Commenda (loss-allocation aspect)".** The census's own name for the form states its loss-mitigation mechanism. Treat `MC1` for this row as not blind; it will be scored separately.
2. **The type name of `societas_maris`: "the bilateral commenda; Venetian collegantia".** It is the census's definition of the form's scope, so it stays.
3. **General knowledge.** You know the standard historiography of the commenda from training. No bundle can remove that. The priors template asks you to write it down, so that it can be separated from what the sources say.
4. **The `code-a-form` skill** names "commenda" in its description as an example institution. It states no value.

## Layout

| folder | contents |
|---|---|
| `doctrine/` | CLAUDE.md, CONTRIBUTING.md, CHARACTER-CODING.md (redacted), EDITING-CSV.md |
| `schema/` | both `datapackage.json` files (the `recodings` resource now has `source_class`) |
| `vocab/` | both characteristic vocabularies (redacted as above) |
| `scope/` | `types-in-scope.csv`: code, name, tradition and period of the four rows |
| `templates/` | the `recodings.csv` header of each census |
| `sources/` | the only sources you may read |
| `proposed-of/` | where everything you write goes |
