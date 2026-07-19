# Editing `data.csv`

CONTRIBUTING.md §1 says the CSV is canonical and must be edited as text, never round-tripped through Excel. This file is the concrete "how" for that rule in VS Code: three ways to do it, in increasing order of hand-holding.

All three operate on the same plain-text file — none of them changes what `frictionless validate` or `build_codebook.py` see. Pick whichever gets you to a correct row fastest; there is no "proper" tier among them.

## 1. Plain text

Open `data.csv` like any other text file and edit it directly. This always works and requires no setup, but rows in this project routinely have 15–20 fields, so it's easy to miscount commas and shift a value into the wrong column — especially in fields that already contain a comma and rely on quoting:

```csv
record_id,...,confidence,coder,notes
CR-0003,...,low,YT,"Alternate normalization of CR-0002 at estimated market rate; retained to show sensitivity, flagged low confidence."
```

That comma inside `notes` only stays inside `notes` because the field is quoted. If you're hand-editing, don't strip quotes that are already there, and add them yourself if a value you're typing contains a comma.

Save as UTF-8. Several fields (`date_wareki`, `instrument_romaji`'s source term, etc.) carry non-Latin script, and a silent re-encode will corrupt them without any visible error.

## 2. Rainbow CSV — for reading and spot-edits

Install [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) (`mechatroner.rainbow-csv`).

It colors each column consistently down the file, so the field you're looking at lines up visually with its header even in a wide, comma-dense row — no extension changes the underlying text, so undo/diff/git blame all behave exactly as they do for any other text edit. Two features worth knowing:

- Hovering a cell shows its column name and index in the status bar — the fastest way to confirm "yes, this really is the `confidence` column" before you type.
- `Rainbow CSV: Align` (Command Palette) temporarily pads columns to line up, useful for eyeballing a block of rows; `Rainbow CSV: Align` again (or just re-save) removes the padding so the committed file stays unpadded.

Good for: verifying you're editing the right column, and small in-place edits — still ultimately typing into the raw CSV text, just with color as a guardrail.

## 3. Edit CSV — for a spreadsheet-like grid

Install [Edit CSV](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv) (`janisdd.vscode-edit-csv`).

Right-click `data.csv` (or use the editor's "Edit as CSV" button) to open it as an actual table — click a cell, type a value, tab to the next one. This is the easiest route for adding a new row or editing several cells without hand-counting commas, and is the option to reach for if you're new to editing raw CSV.

Before relying on it for this project's data, check on a throwaway copy that a save round-trips cleanly:
- non-Latin characters (e.g. `天保5.3.12`) come back unchanged, not mangled or escaped;
- a `notes` value containing a comma is still quoted correctly on save;
- the missingness tokens `.NR`, `.IL`, `.NA` are written back literally, not auto-converted to an empty cell.

Edit CSV writes the whole file back out on save, so it's worth confirming those three behave before trusting it on a real dataset — the underlying `frictionless validate` run (CONTRIBUTING §3) will catch a broken row, but it's cheaper to catch encoding drift here than in a PR review.

## Which one, when

| Task | Reach for |
|---|---|
| Fixing a typo, changing one or two values | Plain text, or Rainbow CSV if the row is wide |
| Scanning/verifying a block of rows | Rainbow CSV |
| Adding several new rows, or you're not comfortable hand-typing CSV | Edit CSV |
| Bulk transformation across many rows | A script (per CONTRIBUTING §1) — none of the above scale to that |

Whichever you use: no blank cells (use `.NR` / `.IL` / `.NA` per CONTRIBUTING §4), and run `frictionless validate datasets/<dataset>/datapackage.json` before opening a PR.
