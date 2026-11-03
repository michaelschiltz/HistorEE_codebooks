# Rulings from the Madurell translation test (2026-11-02 to 2026-11-03)

**Status: ruled by MS in chat on 2026-11-02 and 2026-11-03, on recommendations put by the assistant (`claude-opus-5-5`) in the course of the full translation of Madurell Marimón & García Sanz 1973, docs 1–255 and the Glosario (Google Docs `translations/Madurell-GarciaSanz-1973/`, chunks L01–L24). Recorded here by the assistant on 2026-11-03 and applied the same day to the successor records `act-census-2026-11-03.csv`, `instances-2026-11-03.csv` and `instance-chars-2026-11-03.csv`. The 2026-10-27 records are not changed.**

The translation read every act from the page image. The 2026-10-27 coding read the PDF text layer. The rulings below settle how a form is assigned where the act's own loss term is abbreviated, implied or incorporated, a question the 2026-10-27 coding answered one way throughout ("bearer not written, so `neither`"). Every change they cause is in `records/CORRECTIONS-madurell-translation-2026-11-03.csv`, tagged with the ruling's code.

No `data.csv` cell is changed by these rulings. The sample statistics that the `comanda` and `comanda_alloc` cells quote are recounted against the corrected records in `proposed-of/RECOUNT-comanda-madurell-2026-11-03.md`, for MS to rule.

## D105 (2026-11-02): a remittance with no profit allocation is `neither`

Docs 104 and 105 are carriage and sale for the principal: the whole price, profit included, goes to him, the carrier has no share, and the principal's risk ends at unloading. Form `comanda` → `neither`. Census note: "remittance of value by carriage and sale; whole price incl. profit to the principal; no profit allocation to the carrier". `CMD-105-1` leaves the mod3 `comanda` sample. Its cells are kept, marked contextual.

## D-ERRAND (2026-11-03): the boundary of D105

An errand is an act in which the agent carries, sells or buys a specified thing, has no discretion to trade the capital onward, and has no profit allocated to him: `neither` (docs 104, 105, 152, 207). A comanda is an act in which the agent trades the capital for the investor, with or without a profit share: `comanda` (docs 218 and 233 stay `comanda`). Doc 152 (13,200 s to buy sheep and drive them to the principal at his expense) moves `comanda` → `neither`.

## D-ABBR (2026-11-02): an abbreviated risk clause is the notary's house clause

Where a notary's written-out risk clauses all put the risk on the investor, his abbreviated clause ("Et ad risicum etc.", "Risicum etc.", "Hec igitur etc. risicum", "Et hec comanda etc.") is read as that clause. Form `comanda`; `loss_rule` "investor (abbreviated; house formula)"; `abbreviated_entry` stays "yes", so the reading can be switched off by filtering on it.

The notaries are listed below, each with the written-out clauses that ground the reading.

| Notary | Abbreviated acts read | Written out with the investor as bearer |
|---|---|---|
| Jaume Ferrer | 99, 100, 102, 103 | 104, 105, 107, 108, 110 |
| Jaume Just | 116, 117, 118, 123, 125, 128, 129 [1], 135 [2], 136, 138 | 119–121, 126, 127, 129 [2], 130, 131 |
| Felip Gombau | 147 | 142 |
| Bernat Nadal | 164, 165, 167, 171, 172, 173, 178 | 161–163, 166 |
| Tomàs de Bellmunt | 170, 188, 192, 194, 195, 197 | 190, 191 |
| Arnau Lledó | 176, 177, 180, 182, 183, 187 | 179, 184, 185, 200 |
| Joan Nadal | 203, 204, 205, 206, 209, 213, 217 [1] | 202, 208, 210–212, 214 |
| Francesc Cerdà | 225 | 223, 224 |
| Esteve Mir | 232 [2], 237 | 230, 231, 236, 246 |

Doc 179 is the strongest single support: Lledó's abbreviated text (fol. 19) and full text (fol. 52) of one comanda, the full one naming the investor.

## D-BELL (2026-11-02): the city formula where the notary writes none

Where the notary never writes the clause out in the edition, the abbreviated clause is read on the city formula. The ground: all 34 written-out "eat, maneat …" clauses in L01–L15 name the investor, two of them pro rata with a *societas* or common. `loss_rule` "investor (abbreviated; city formula)", kept distinct from "house formula". This applies to Bernat de Vilarrubia (docs 59, 60) and Pere Bastat (docs 233, 239–242, 244, 245). The ruling was framed on Bellmunt; his written clauses in docs 190 and 191 (L17) moved him to D-ABBR.

## D-SALV (2026-11-02): a salvage clause is a loss rule

"restituam … prout Deus salvaverit" and "implicamenta, prout Dominus Deus ea salvaverit, … reducere" limit restitution to what survives, so the loss falls on the investor. The 2026-10-27 coding already read the clause so for `CMD-122-1` `RB4`. Form `comanda`; `loss_rule` "investor (by the salvage clause)". This applies to docs 89, 149, 153 (entry unfinished), 175 and 189 (both bounded to numbered coral chests), and 215.

Doc 168 rests on two abbreviations only, "Que implicamenta etc." and "Predictam autem comandam etc.". It is coded "investor (abbreviated; house formula; salvage clause abbreviated)" and marked as such.

## D-SIM (2026-11-02; general form 2026-11-03): incorporation by "simile"

A "simile" or "fiat in omnibus ut in proxime instrumento" entry with no risk clause of its own takes over the notary's earlier instrument. Where that notary's written-out clauses name the investor, the entry is coded `comanda`, `loss_rule` "investor (incorporated …)", with `abbreviated_entry` "yes". This applies to docs 174 [1] and [2], 181, 196, 204 [2], 217 [2] and 238 [2]. The general form supersedes the Lledó-only scope of 2026-11-02.

## D-207 (2026-11-03): doc 207 stays `neither`

Doc 207 is a purchase errand (one female slave) with no profit allocation, so it is `neither` under D-ERRAND. Its risk clause, "ad risicum … vestri dicti Petri", is confirmed in the image. "vestri" is the investor and "dicti Petri" is a scribal slip. `CMD-207-1` `loss_rule` "contradictory as printed" → "investor [sic: dicti Petri, scribal slip for the investor]"; `peril_clause` "ad usum maris et gencium; salvage clause". It stays in mod3 as `neither`.

## Not ruled: Pere de Torre's "ad quartum lucri et usum maris" (docs 75–85)

The census reads the formula as loss by custom only and codes `neither`. No D-ABBR reading is applied, because Torre has no written-out clause naming a bearer in the edition. The census rows carry a note that this is an open theory call. If D-BELL's city formula were extended to the custom of the sea, nine more acts would move.

## The 2026-10-27 sensitivity claim

The coding notes said that adding the 9 custom-only acts and the 48 abbreviated acts would give 202 `comanda` acts. The corrected census also has 202, but by a different route: 145 + 60 (D-ABBR 41, D-ABBR with D-SALV 1, D-BELL 9, D-SALV 6, D-SIM 3) − 3 (D105/D-ERRAND), with the custom-only acts not added. The equality is a coincidence of counts, not a confirmation.
