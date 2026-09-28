# Logbook draft — commenda-secondary-2026-09-28 (for logbook 4, tests and results)

## 2026-09-28 — ai — blind re-coding of commenda and societas maris from secondary literature only (arm S)

Pass `commenda-secondary-2026-09-28`: 61 cells of `commenda` and `societas_maris` in `organizational_forms`, and of `commenda_alloc` and `societas_maris` in `loss_mitigation_forms`. Coded blind by `claude-opus-5-5` at effort `high` from six held works: van Doosselaere 2009; Harris 2007 (conference draft); Harris 2020 (SSRN draft of "General Average and All the Rest"); Held 2025; Udovitch 1962; González de Lara 2002. The bundle was minimal: no `data.csv`, vault or views. The priors (`PRIORS-commenda-secondary-2026-09-28.md`, sha256 `a2917ca5…4c34`) were committed by MS before any source was opened, and MS confirmed the committed copy by hash. All cells were fixed before any computation. Rows are in `recodings.csv` (OF-R0065–OF-R0106, LM-R0001–LM-R0019), all `adjudication=pending`; `value_at_recoding` and `agreement` are left for application.

Result: 35 substantive cells, 20 `.NR`, 6 `.NA`. On both rows, legal personality, capital lock-in and transferable claims learned nothing. Owner shielding was coded for the commenda only (`AP3`=0, `LR1`=unlimited-several low), on Harris 2007 PDF 10–11 and Udovitch 198, which are not independent of each other. Entity shielding has one cell (commenda `AP1`=P, low), on Harris's hedged Hansmann–Kraakman–Squire reading. The societas maris rests almost wholly on van Doosselaere 65–67, which rests on Pryor 1977 (not held). `MC1` is not blind on either loss row (README leak 1; a redaction inside the loss schema's list of allocation examples).

Flagged, not repaired:

- `LR1` asks extent and form together, and the form is undefined for one labour party.
- `LR3`'s name and definition ask different questions.
- `RB1` does not say whether an agent's labour at risk counts as loss.
- "Bilateral" in "bilateral commenda" means two-sided contribution, not `CF3`.
- "Harris 2020" names three works.
- The README's claim that Harris 2007 has no page numbers is false: the footer page numbers equal the PDF pages.
- The schema descriptions name vocabulary files that are not there.

Coding record: `records/NOTES-commenda-secondary-coding-2026-09-28.md` once copied from the bundle; until then `proposed-of/` is a pointer to open work only.
