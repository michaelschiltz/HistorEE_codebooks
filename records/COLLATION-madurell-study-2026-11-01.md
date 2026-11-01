# Collation: the editors' study in Madurell Marimón & García Sanz 1973 against the comanda coding of 2026-10-27

Written 2026-11-01 by ai (claude-opus-5-5, effort high), on licence from MS the same day to record the results as dated notes in eight `data.csv` cells, values untouched. Not a coding pass and not a blind test: the coder had the live matrix, the instance files and the act census open throughout.

## What was collated

- **The study.** Arcadi García Sanz's introduction to the edition, pp. 9-148 (Presentación by Raimundo Noguera, pp. 9-15; chapters I and II, pp. 17-148). Zotero `VPX7DFWD`, attachment `QQ427RZ4`; PDF page = printed page - 1.
- **How it was read.** Transcribed from the page images and translated into English page by page, as a translation test that doubled as an OCR check (MS, 2026-11-01). The transcription and translation are in Google Drive, folder `translations/Madurell-GarciaSanz-1973/`, Docs 01-14; they are not in this repository. Page numbers below are printed pages.
- **Against what.** `records/instances-2026-10-27.csv` (115 instances), `records/act-census-2026-10-27.csv` (255 entries), `records/NOTES-comanda-primary-coding-2026-10-27.md`, and the live `comanda` and `comanda_alloc` cells.

## Independence, declared before the results

- **On what the documents say, the study is not an independent witness.** García Sanz edited the documents the census was coded from. Where he and the census agree on a document's content, that is one reading checked twice, not two witnesses.
- **On what the documents look like, it is independent of the census's input.** The coding pass read the OCR text layer (`pdftotext -layout`; `records/NOTES-comanda-primary-operator-2026-10-27.md`); the editors read the originals. On dates, amounts and names, a disagreement between the study and the census is therefore a question for the page image of the document, and either side may be wrong: the study has misprints of its own (below).
- **On doctrine, the study is not independent of Martínez Gijón 1966.** García Sanz says he follows him in the account of the theories of the comanda's legal nature (pp. 74-76). Martínez Gijón 1966 is already cited in the cells concerned.

## 1. Dates

Every document the study dates was compared with the year the coding gives it: 48 documents against the act census, 25 of them also in the instance file. Decades (`1290s`) count as agreeing when the study's year falls inside them.

| doc | file              | coded              | study                     | page            | reading                                                                                                                                                       |
|-----|-------------------|--------------------|---------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 17  | instances         | 1252               | 20 Jan 1263               | p. 22, n. 8     | Conflict. The census row for the same act has `1260s`, and the instance's own note says `Census: 1260s`; docs 16 and 18 are coded 1261 and 1265. 1252 is out of sequence. |
| 55  | census            | 1280s/90s          | 5 Aug 1291                | p. 53, n. 158   | The census could not fix the year; the study does. Not in the sample.                                                                                         |
| 83  | census            | 1328               | 3 Mar 1329                | p. 39           | Probably not an error: a March date before 1351 in the Incarnation style, which the study modernises. Not in the sample.                                    |
| 178 | census            | 1409               | 23 Sep 1408               | p. 61           | Conflict, one year. Not in the sample.                                                                                                                        |
| 251 | census            | 1488               | 10 Dec 1489               | pp. 78, 135     | Conflict, one year; doc 250 is coded 1489, so 1488 is out of sequence. Not in the sample.                                                                     |
| 255 | census, instances | 15th c.            | second half of the 14th c. | p. 105          | Conflict. The act is undated; the editors date it by a party, Berenguer Martí, in docs 100 (1349) and 114 (1361), and by palaeography.                      |

**No sample instance moves between 25-year bins** (bins taken as starting in 1250): doc 17 stays in 1250-1274 either way, and doc 255 is assigned to neither row.

**Correction of an earlier claim.** A first pass at this collation, reported in chat on 2026-11-01 and in a project note of the same day, listed seven date conflicts in the instance file (docs 17, 66, 106, 111, 142, 220, 222). It was made without the comparison above. Five of the seven are not conflicts: the coded decade contains the study's year (66: 1290s against 1299; 106: 1340s against 22 May 1349), the study does not date the act (142, 220, 222, all consistent with their neighbours), or the study dates the voyage and not the act (111: voyage June-September 1358, act 10 September 1359 as the instance quotes it). Only doc 17 stands; doc 255 was not on the list.

## 2. Remuneration (`LR2`, `LR3`)

- **The quarter, and its decline.** The *quart diner* «se aplicó de modo inalterado hasta el año 1414»; afterwards *ad medium quartum lucri* and *ad sextum lucri* appear (docs 234, 241; p. 124, n. 209). In internal trade the split may be «a medias, dos tercios para el capitalista y uno para el gestor, 80 % para el primero» (docs 109, 154, 201, 220, 240, 247, 252; p. 126, n. 221). These agree with the ratios the `LR3` note already records from the census. The 80 per cent split is not located in any act yet. Doc 220 (a third, directed instance) is missing from that note's list of thirds.
- **A fixed fee on capital.** From 6 April 1426 (doc 214, 20 lb 18 s, almonds to Flanders) and again in 1462 (doc 238, Tunis and Barbary) the agent receives «el 2 ó 3 por 100 a la ida i el 2 por cien a la vuelta», which García Sanz takes to be of the capital and calls «una retribución fija, establecida como porcentaje del capital, y no una participación en los beneficios» (pp. 124-125, nn. 210-211, 213). It coexists with the *quart diner*; he finds it in the Flanders and Tunis trades and never on the eastern route. Neither act is in the sample; the act census records only their risk clauses. If the clauses read as he says, they are a second fixed claim besides doc 93 and evidence against `LR2` = coupled. **Not read: to read.**

## 3. Loss and risk (`CF2`, `RB1`, `RB2`, `RB4`)

- **The rule.** Where the agent's share is the *quart diner* or less, «la totalidad del riesgo recaía sobre el capitalista o comendante»; where it is larger, risk is divided in the proportion of profit, «muy señaladamente cuando era a medias» (docs 201, 247, 252); exceptions are internal-trade comandas and deposits (docs 109, 154, 240) (pp. 129-130). From the second half of the 13th century the first system «predominó francamente» (p. 130). This is the census's loss split, read by the editor from the same documents.
- **Two acts the census codes differently.** Doc 252 is coded `loss_rule = not-stated`; the study cites it for risk shared in proportion to profit. Doc 240 is coded `abbreviated` ('Risicum etc.'); the study counts it among acts with all risk on the investor, which is a reading of the notarial convention, not of the note. Both need the page image.
- **Risk is generic.** Not only the sea: «alzas o bajas de precios en el mercado, riesgos terrestres propiamente dichos, embargos o retenciones decretados por autoridades públicas, marcas, represalias» (pp. 126-127). It passes wholly to the agent if he «altere deliberada y substancialmente los términos» of his charge (LCM caps. 210-217; doc 186, a demand of 18 February 1412 for pepper owed under a comanda of 8 June 1409) (pp. 127-128). Supports `RB2` and its fault class.
- **The agent-bears acts, read as exchanges.** Doc 3 is the study's type of a money comanda «para ser devuelto en otra» city (p. 77) and a proto-exchange: 16 bezants *de cambio*, to be repaid at Tunis, with fallback repayment in Barcelona *salvos in terra* plus a profit-equivalent (pp. 36, 110-111). Doc 191 is trajectitious exchange *sine risico*: 600 florins to Pere Toralles to invest in exchanges *salve et secure in terra* (pp. 112-113; Toralles, a moneyer of Càller, also as an insurer, p. 38). Doc 93 is bottomry: a ship loan with a special hypothec, drafted with the comanda risk formula (pp. 112, 122, 127). If the reading is adopted, the agent-bears minority in `CF2` and the act against `RB4` are exchange drafting in comanda form, not comanda drafting.

## 4. Insurance (`MC1`, `PR1`)

- **Doc 255, the *comanda-seguro*.** The Florentine Ricardo de Avenzati receives four *aludes* of saffron in comanda from Berenguer Martí, to have them carried to Geneva, and takes on every risk and damage on the way; Martí pays carriage and taxes. The premium, García Sanz infers, stood in the lost part of the act. He reads it as insurance of overland carriage in Florentine form under the comanda's name (pp. 105-106). The census assigns the act to neither row.
- **Insurance among loading costs.** *Soluta securitate* in docs 224 and 245 (p. 106, n. 175), besides docs 246 and 250 already cited in `MC1` and `PR1`.
- **His explanation of the lateness.** Insurance came late to the comanda because the comanda already assigned the voyage risk to the investor (p. 106); and after 1414 the spread of risk cover, maritime exchange and insurance, «modalizaban en forma substancial» the comanda's risk element (p. 125).
- No price survives in doc 255, so it does not argue `PR1` = P under the coding rule.

## 5. Transfer (`CI3`)

The investor's cessions (doc 217, by marginal note of 24 January 1428, to the investor's father; docs 253-254, 27 July 1501, to the investor's father-in-law, with a renewed deed by the agent) are, for García Sanz, «más que de verdadera cesión, … un reconocimiento de propiedad», made «no como verdadera cesión, sino como novación», with the agent's consent and not on notice (C. 8.42.3), and only «en que mediaban vínculos personales estrechos, como lo es el parentesco»; «de ordinario, la comanda no era objeto de cesión» (pp. 85-86, 136). On that reading the investor's side, too, passes only with the agent's consent, which bears on the half-presence argued in the `CI3` note. The order clause of doc 87 is not discussed.

## 6. Open item 4 of the coding notes: the abbreviated acts

The 48 acts whose risk clause is abbreviated ('Et ad risicum etc.') are notarial register notes. The study explains the form (pp. 133-134): the AHPB documents of the edition are the notes in the notaries' *manuales*, drawn up «en forma muy sumaria, abreviándose las cláusulas de estilo con un simple *et cetera*»; the deed *in publicam formam* expanded them and was handed to the investor; the ACB parchments are such deeds, «con su auxilio el lector puede perfectamente completar las notas de los manuales». A chapter of the Corts of Perpinyà of 1351 forbade the practice and was «poco menos que letra muerta». The risk clause abbreviated in these notes is therefore a style clause whose expansion the notary took as known. Whether to assign the 48 acts by that convention is the maintainer's decision; the `CF2` note already records that adding them would not change the value.

## 7. Sample basis

«Los documentos contenidos en la presente colección, constituyen la totalidad de los que hemos encontrado en el ACB. En cambio, los procedentes del AHPB constituyen sólo una selección»: the selection criterion was representativeness of routes, products, document types and contract types; the Syrian comandas came «incluso con sobreabundancia», the Flanders trade with «serias dificultades» (p. 143). The printed set is a census of the cathedral parchments, mostly 13th-century, and a purposive selection from the notarial registers, from 1299. Frequencies across the collection mix the two.

## 8. Names

- **Doc 3.** The study names the lender Bernat de Banyeres (p. 36); the instance file, from the OCR of the Latin, Raimundo de Bagnariis. Not settled without the page image of doc 3.
- **Doc 193.** The second agent is Guillem Guerau on p. 29 and Guillem Giralt on p. 128. Not in the sample.

## 9. Misprints in the study, recorded so that they are not carried into cells

- The Espaser voyage to Alexandria yields 1,530 lb 16 s 3 d on 4,087 lb 13 s 7 d, which is 37.45 per cent, not «algo más del 27 por 100» (p. 121; computed in code).
- The 13th-century Alexandria comandas range 140-384 lb on p. 22 and 140-380 lb on p. 24.
- The partner is Espaser on pp. 82, 98, 120-121, and Espaer on pp. 26, 37.

## 10. A claim about the OCR layer, not yet tested

The translation logs class many lines of the text layer as truncated, scrambled or promoted to headings. Those observations were made through the Zotero connector's rendering of the layer, not through `pdftotext -layout`, which is what the coding pass used. The truncation may be an artefact of the rendering. The misread numerals (3 for 8, 2 for 9, 3 for 9) and characters are in the layer itself; they are the errors that threaten the coded years, amounts and document numbers.

## Page images to read first

Docs 17, 178, 251, 255 (dates); 3 (date, lender, risk clause); 93, 191 (classification); 240, 252 (risk clauses); 214, 238 (remuneration; not in the sample).
