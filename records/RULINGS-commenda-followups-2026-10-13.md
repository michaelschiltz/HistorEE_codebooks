# Rulings in the commenda follow-ups (2026-10-13)

**Status: ruled by MS in chat on 2026-10-13, item by item, each on a recommendation put by the assistant (`claude-opus-5-5`, effort `high`) and accepted as proposed. Recorded here by the assistant. Pass slug `commenda-followups-2026-10-13`; open, not blind. The brief takes up the "Open for MS" list of the Italian commenda re-code (`RULINGS-commenda-italian-recode-2026-10-12.md`).**

Sources read first-hand for these rulings, on page images: *Atti della Società ligure di storia patria* I (Zotero `SUJ2QXRU`), title page, pp. 93 n., 632, 636, 640, 642, 644 and the table of contents (700); Promis, *Statuti della colonia genovese di Pera*, in *Miscellanea di storia italiana* XI (`CTM27ZV8`), volume title page, its verso, and the section title (513); Pryor 1977, n. 13 (`G7U4P8T3`).

## 1. Edition dates in the cells — *Atti* I is cited as 1858; Promis stays 1871

*Atti della Società ligure di storia patria* I is cited by its title-page date, MDCCCLVIII (1858), in the 13 `organizational_forms` cells that cited it as "(1862)" (`OF-0079`, `0080`, `0284`, `0285`, `0550`–`0553`, `0560`–`0563`, `0902`), each with the inline bracket `[date CORRECTED 2026-10-13: title page reads 1858]`. Source reference only, after the precedent of `LM-0545` (2026-10-11 (v)): no value, confidence or articulation moves, so no recodings row and no version bump; the twelve recodings rows of 2026-10-12 keep "(1862)" as the record of what that pass wrote. The Datta fragment was issued in the volume's second fascicle (Rendiconto, p. 642), which cannot be dated from the copy held: no earlier than 1859, since Desimoni's report cites Datta's Nice edition of 1859 as *testé* published (p. 93 n.), and no later than the Rendiconto's approval on 9 March 1862. Pryor 1977, n. 13, gives "parte 2 (1859)" without a source. The cells cite the volume, not the fascicle; the fascicle evidence is in logbook 5.

Promis, *Statuti della colonia genovese di Pera*, stays "(1871)": the title page of *Miscellanea di storia italiana* XI, read at 400 dpi, prints MDCCCLXXI, and the pencilled "1871" beside it agrees. The flag of logbook 5, 2026-10-12 (viii), that the printed date is 1870, rested on a misreading of the imprint at low resolution; Zotero `CTM27ZV8` is returned to 1871. Pryor's "11 (1870)" is recorded as a divergence; no page held is printed 1870.

The vault note "Barcelona law kept the commendatary's creditors off the comanda goods" is corrected to *Atti* I, 1858.

## 2. The vault note on comanda capital is retitled for cap. 215

In `myfoamrepo`, "Comanda capital was kept apart unless the contract said otherwise" is renamed "Comanda capital was mixed with the agent's own unless the contract said otherwise". Ruling 29 of 2026-10-12 coded `comanda CI5 = commingled` on *Consolat* cap. 215 (mixing with the agent's own money, permitted unless the investor restricted it); the old title stated cap. 219 (no mixing into a company's common stock without consent) as the default. File, `title:` and H1 renamed; a RENAMED bracket carries the old title in the note; the wikilinks in six files (five notes and `MOC - Risk-sharing vs risk-pricing`) rewritten; `graph/` regenerated with `scripts/export_graph.py`. Precedent: the rename of the commenda-family note on 2026-10-12. The mention in `records/RULINGS-commenda-italian-recode-2026-10-12.md` stays verbatim.

## Flagged, not ruled

The `commenda` type row in `vocabularies/organizational_form_type.csv` cites "ASLSP I, 1862". Type rows are append-only, so it stands; a reader resolving it goes to `SUJ2QXRU`, which carries 1858.
