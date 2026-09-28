# Bundle: `commenda-primary-2026-09-28` (arm P: primary acts only)

**This is a prepared copy for one coding chat.** It is not the live repository. Do not look for the live repository, the vault, Zotero or the web. The kickoff prompt governs the procedure; this file says what is here and why.

## Sources (`sources/`): transactional documents only

| file | what it is | page map |
|---|---|---|
| `scriba_vol1_acts_pdfp66-501_errata.pdf` | *Il cartolare di Giovanni Scriba*, ed. Chiaudano & Moresco 1935, **vol. I**: acts I–DCCCII+, Genoa 1154–61 (Zotero QTEG4PM7, file DHLLKXEI) | extract page *k* = original PDF page *k*+65 for *k* = 1–436; extract p. 437 = original p. 504 (errata). The printed page is on each page. |
| `cassinese_vol1_acts_pdfp22-459.pdf` | *Guglielmo Cassinese (1190–1192)*, ed. Hall, Krueger & Reynolds 1938, **vol. I**: acts 1–c.1092, to September 1191 (Zotero G4TIJ2FM) | extract page *k* = original PDF page *k*+21; printed page on each page |
| `amalric1248_blancard_notulae_latin.txt` | Giraud Amalric, Marseille 1248: **the whole cartulary, nos. 1–1031**, as edited by Blancard 1884–85 (Zotero HF8ME3N7), **Latin only**, extracted by the operator. The Latin is printed for 561 acts; the rest are one-line stubs | each notula gives Blancard's volume and printed page; see the file's header |

**Removed from the sources:**

- both Genoese editors' prefaces and introductions;
- Blancard's French summary of every act, his date headings, his introduction, tables and index.

These are secondary literature, and this arm reads none.

**Editorial layers that remain:**

- the editors' Italian headings (*regesti*) above each Genoese act;
- the editors' footnotes;
- the bracketed restorations;
- Blancard's textual notes on the notary's corrections and erasures, marked `[Blancard's note: …]`.

**Use the regesti to find and sort acts, never as evidence.** Code from the Latin.

**The corpora are incomplete by construction:**

- The second volume of both Genoese cartularies is not held.
- **Amalric's cartulary is complete in numbering but not in text.** Blancard printed the Latin of 561 acts and summarised the other 413 in French (withheld here); 51 went to his appendix; nos. 276–280 are missing from the scan. Which acts got their Latin printed was the editor's choice, so frequencies over them describe the printed set.
- **Blancard abridges the standard formulae** (`renuncians etc.`, `obligans etc.`, `Factum fuit etc.`). A formula's absence from his text is never evidence of its absence from the notula.

**OCR:**

- Scriba's text layer is letter-spaced ("G ave sor or i s").
- Cassinese's plates are noise.
- Blancard's text layer is uneven and sometimes displaces a short fragment by a line; cite every Amalric quotation with its act number and printed page, so it can be checked against the page image at application.
- Check against the page image any quotation that carries a cell.

## Also here

`instances-header.csv` and `instance-chars-header.csv`: the document-level tables you fill. `cells-in-scope.csv`: the 61 cells, with the `recoding_id` pre-assigned for your stage-4 (`blind`) rows and your stage-5 (`open`) rows.

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
