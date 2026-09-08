# `records/` — the batch record, tracked and preserved verbatim

**These files are evidence, not prose.** They are committed so that the claims the deposit makes *about how it was made* can be checked by someone who was not here, and they are preserved **verbatim**: nothing in this directory is reformatted, re-wrapped, re-aligned or tidied, ever. `check_softwrap.py` and `check_tables.py` both exclude it for that reason, on the same ground that excludes the verbatim `LICENSE-DATA.md` from the soft-wrap rule.

## Why this directory exists

Until 2026-09-08 every artefact here lived in `proposed-of/`, which `.gitignore` excludes as "working artefacts of one session, not part of the deposit: the rows themselves live in `data.csv` and the reasoning lives in the logbooks, both of which are tracked." **That description had stopped being true.** An audit on 2026-09-08 found the tracked record citing that ignored folder **47 times across 23 files** — including five times from `data.csv` cell notes — with **nine of those citations already broken** by an earlier tidy. The logbooks were not containing the reasoning at those points; they were delegating to a folder that was in no commit, had no history, and could be destroyed by a single `git clean -xdf`.

The contradiction had only two consistent resolutions: stop citing the folder, or track what is cited. This is the second.

## The line between here and `proposed-of/`

**`records/` holds the artefacts of a completed batch that the tracked record reasons from** — selection briefs, coding notes, the priors written before the sources were opened, the prompts handed to a blind coding chat, the rows as proposed (against which what actually landed can be diffed), and anything preserving content that was removed from the census.

**`proposed-of/` stays ignored and holds work in flight and drafts superseded by the thing they became** — open `PATCH-` proposals awaiting a decision, `COMMIT-MSG-` files whose text Git already holds, and `LOGBOOK-DRAFT-` files whose content is in the logbooks.

**The citation rule that follows:** the deposit may cite `records/` as *evidence*; it may cite `proposed-of/` only as a *pointer to open work*, and such a pointer must be resolved when the work is. A citation from a coded cell or a logbook entry to something that is not in the repository is a promise the repository cannot keep.

## What is here, and what each class is evidence of

- **`PRIORS-…md`** — expectations written down **before** a source was opened, quoted back verbatim when the coding is scored. *Evidence of ordering.* **There is currently one**, for the 2026-09-07 deed-of-settlement recode, against four blind coding batches run to date. The other three scored their falsifications from the coder's own narrative, written in the same session as the coding, which is a weaker thing and should be read as such.
- **`PROMPT-…txt`** — what a blind coding chat was actually given. *Evidence for the channel-check*: a selection brief that claims its withheld predictions were "checked absent from the prompt by term count" is checkable only while the prompt survives. One of these, the 2026-09-06 chartered-corporation prompt, exists in two versions because the first leaked two of its own predictions and was withdrawn — which is exactly the kind of thing a record is for.
- **`NOTES-…md`** — selection briefs (operator) and coding records (coder), including the coder's six answers, its declarations of non-independence, and what it refused to code and why.
- **`proposed-rows-…csv`, `proposed-type-rows-…csv`** — the rows as the coder proposed them, before application. *Evidence of the difference between what was proposed and what landed.*
- **`proposed-retire-joint-stock-cells-…csv`** and its README — the only surviving copy of `OF-0032` and `OF-0033`, deleted from the census on 2026-09-06 under the gaps policy.
- **`BUNDLE-EXCISIONS-…md`** — what a blind bundle removed and why, which is how a reader judges whether the blind was real.

## A standing weakness, stated here rather than buried

**An untracked priors file proved nothing.** A filesystem mtime is mutable and carries no commitment; a priors file written after the fact is indistinguishable from one written before. Committing these files gives them a place in the hash chain, which is far stronger — **but only if a priors file is committed *before* the coding commit that it is later scored against.** Tracking the folder does not by itself establish the ordering for anything already here; it makes the ordering establishable from now on. The batch procedure is where that has to be enforced, and this directory is not a substitute for it.
