You are the coding chat of a blind re-coding pass, `comanda-primary-2026-10-27`, for the HistorEE_codebooks census. You code 43 cells of two rows, `comanda` (organizational_forms) and `comanda_alloc` (loss_mitigation_forms), from one printed edition of Barcelona notarial acts, and from nothing else.

**Your working folder is `~/GitHub/_blind-comanda-primary-2026-10-27` on my computer, and only that folder.** Read its `README.md` first. Do not open, list or search any other folder: not the live repository `~/GitHub/HistorEE_codebooks`, not the vault `~/GitHub/myfoamrepo`, not the other `_blind-*` or `_work-*` folders beside it. Do not use Zotero, the web, the claude.ai Project, past-chat search, or any memory file. If your context already holds material from any of these about the comanda or the commenda, say so before doing anything else, and stop.

**Order of work, which is the point of the pass:**

1. Read `README.md`, the four files in `doctrine/`, `cells-in-scope.csv`, `scope/types-in-scope.csv`, both files in `vocab/` and both in `schema/`. Do not open anything in `sources/`; a directory listing is allowed and must be declared.
2. Fill `PRIORS-TEMPLATE.md` as a copy in `proposed-of/`, print its sha256, and stop. I will commit it and tell you so. **Do not open the source before I confirm the commit.**
3. Census, sample and directed search, exactly as `README.md` fixes them. Record every act you assign to `comanda_ad_societatem` as well, but code no cell of that row.
4. Code the 43 cells into the two recodings files, from your instances and their quotations. Follow `doctrine/CLAUDE.md` on missing values without exception: a document that does not address a question yields `.NR`, never `0`; `P` is a structural state, not a hedge; uncertainty goes in `confidence`. Quote every passage a cell rests on, with doc number and page, in the language of the act, and give the reading you take from it; the OCR will be checked against the page images at adjudication. `source_lang` is the language of the quoted passage. `source_class` is the class of the cited passage, not of the edition.
5. Write `NOTES-comanda-primary-coding-<date>.md` and answer these six, plainly and unprompted: (1) what was coded and on what evidence; (2) what could not be coded and why; (3) which of your own priors were falsified, quoting the priors file verbatim; (4) any characteristic that did not fit the evidence; (5) any dependence or well-formedness problem noticed and not repaired; (6) what to acquire next, and which cell it would move. Then the logbook draft and the commit message, both in `proposed-of/`.

Everything you write goes in `proposed-of/`. Do not edit any other file in the bundle. Do not run `git`. Freeze the record when you are done: once `proposed-of/` is complete, say so, and change nothing in it afterwards.

Record your model identifier and effort setting in `coder_model` and `coder_effort` on every recodings row. Work at effort `high`.
