# Rulings for the Venetian pass: operator rules for adjudication (2026-10-25)

**Status: ruled by MS in chat on 2026-10-25 ("Everything accepted"), on six recommendations put by the assistant (`claude-opus-5-5`, effort `high`), two of them amended by the assistant before the ruling (1 and 3) and one widened (4). Recorded here by the assistant. Operator-side: these rules govern adjudication of the Venetian pass and are not given to the coder, who codes blind. No data change.**

Basis: the selection measured in `records/NOTES-morozzo-lombardo-selection-2026-10-25.md` (§6.5 for the findings, §7 for the recommendations as first written), over `records/CORPUS-morozzo-lombardo-2026-10-25.csv`. Logbook 5, 2026-10-25 (iii).

## Ruling 1 — Venetian contracts are assigned by their terms, not their date; no form split now

- Each Venetian contract is evidence for the type its own terms fit: the working party's own stake (*posui ibidem* and its variants) for `societas_maris`; the quarter share retained by the working party with the peril on the investor for `commenda` and `commenda_alloc`.
- The act's date and fondo are stated in the cell's note, because in this edition period and fondo are confounded (in 1230–1261, 91 of 99 contracts come from the Procuratori and the Cancelleria Inferiore).
- **Rejected:** a split at 1200 (the cut is the measurement's, not the sources'); a separate Venetian form now (it would turn a survival pattern into a form). The question reopens only if the two strata take different values on the same cells once coded.

## Ruling 2 — a release that does not recite the clause yields `.NR` for loss terms

- A release supports the existence of the venture, its parties, its capital, its route and its discharge.
- For a loss-allocation or outcome-coupling cell, a release counts only where it recites the clause. Where it does not, whether it abbreviates ("ut in ea legitur", 70 of the 166 investment-related releases) or recites other terms and stays silent on the peril (89 more), the cell takes `.NR` from it, never `0`.

## Ruling 3 — the settled-venture caveat binds ex-post claims only

- Cells coded from an ex-ante clause (the peril clause is in 158 of the 164 contracts) carry no survival caveat: the survival of a charter does not alter what its clause says.
- Where a cell or a claim rests on what happened after the fact (how losses fell, how often), the note names the attestation or judgment relied on and states that the surviving material is weighted toward settled ventures and toward contested losses.

## Ruling 4 — every family dossier counts as one cluster

- Applies to all dossiers the editors name (Mairano 118, Stagnario 59, da Molin 54, Gradenigo 47, Serzi 41, Aimo 36) and any found in reading. These are tractators' archives and over-represent the receiving side.
- Notes report the number of acts and the number of dossiers behind a value. Agreement among acts of one dossier does not raise confidence.

## Ruling 5 — mater and exemplum are one witness

- Use `copy_flag` and `regest_similarity_prev` in the CORPUS file to collapse duplicates before counting support. Where only the copy survives, it is the witness.

## Ruling 6 — the measurement stays out of the PRIORS and the bundle

- The Venetian PRIORS are written before the coder sees any act, without reference to the NOTES file. Rulings 1–5 are applied at adjudication, not passed to the coder.
