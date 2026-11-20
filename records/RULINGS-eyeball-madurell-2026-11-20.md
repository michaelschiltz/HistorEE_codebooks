# Rulings: eyeball check of the Madurell instance record (2026-11-20)

**Ruled by MS on 2026-11-20, 18:46–19:03 JST, line by line, on the assistant's recommendations; every recommendation was accepted. Recorded by the assistant (`claude-opus-5-5`).** Protocol: `records/PROTOCOL-eyeball-madurell-2026-11-19.md`. Blank sheet, draw script and protocol pushed 2026-11-19 17:06 JST (research-ledger entry `20261119T080643Z-historee_codebooks-a1e038f77d3c`); filled sheet `records/SHEET-eyeball-madurell-2026-11-19-filled.md` (sha256 `65327df8a1469f8024db4bdad4ef3354f88a7c448761b213eca9d7a7926e3a5b`) pushed 2026-11-20 16:47 JST (`20261120T074718Z-historee_codebooks-d1701151eec8`) before anything was scored. The draw key, held outside the tree until scoring, matched its recorded sha256 and is now `records/DRAW-KEY-eyeball-madurell-2026-11-19.csv`. Line-level results: `records/SCORED-eyeball-madurell-2026-11-20.csv`.

## Result

| Class | Lines | Strata |
|---|---|---|
| Content error (the record) | 5 | date 4, parties 1 |
| Form error (the record) | 6 | parties 6 |
| Reader's slip (the record right) | 11 | parties 3, clause-absent 3, clause-present 2, destination 2, amount 1 |
| No error | 38 | 24 automatic matches, 14 flagged lines ruled no error or match |

- **Content-error rate of the record: 5 of 60, 8.3%**, 95% interval 3.7–18.1% (Beta(1 + k, 1 + n − k), flat prior). Weighted by stratum populations (118, 118, 118, 118, 168, 41 fields), 8.7%. In the mod3 subset, 3 of 39 lines.
- **By stratum:** date 4 of 10 (16.7–69.2%); parties 1 of 10; amount, destination, clause quotations and coded absences 0 of 10 each (0.2–28.5%).
- **The date errors are mechanical.** Three dating clauses are cut at the printed line break, before the year (docs. 15, 84, 162); one dated act is `.NR` (doc. 16). No date element was misread.
- **The parties error is an omission:** doc. 193 names the 55 investors' agents, Salavert and Geraldi; the record has `to: .NR`.
- **Escalation, under the protocol:** dates show two or more content errors in ten, so MS reads the dating clause of all 118 instances and the census replaces the sample for that field. The record is corrected in one successor after the census, together with doc. 193's parties.

## The reader's slips

Eleven of sixty, 18.3% (10.6–30.0%). Four are traced to the questions on the sheet, written by the assistant: the risk question did not list *redegum*, the word these notaries use (lines 1, 25); "who entrusts, who receives" invited the roles of the underlying comanda rather than the parties to a receipt (line 56); "binding a person … for performance" admitted a recital in a power of attorney (line 15). The other seven: act 1 read for act 2 or the reverse, in entries the edition does not or does number (lines 38, 45, 54); another document's parties (line 52); a destination missed (line 33); the editor's heading read for the act (line 44); and «Quod implicamentum etc.», the return promise, read as a risk clause (line 41).

**What this shows.** A single blind human reading is not a reference by itself: here it erred more often than the record. The rate above is the record's against the print, established only because every disagreement was ruled against the printed page. The next sheet (the Venetian acts) should name the act within an entry by its opening words, list each tradition's risk vocabulary, ask for the parties to the act, and define the obligation clause as a pledge of person or goods.

## The predictions (protocol, before the draw)

1. Dates and amounts each at least one content error: **dates hit (4), amounts missed (0).**
2. Parties none: **missed (1).**
3. Destination at most one: **hit (0).**
4. Clause quotations, no content error and several form errors: **content hit (0); no clause line was ruled a form error, so the second half missed.** The scorer's containment rule passes a shorter excerpt without flagging it, so form differences in quotations were not measured.
5. Coded absences at most one: **hit (0).**

## Not ruled here, open

- **Doc. 174, act [2]:** whether «Hec igitur etc.» abbreviates the risk clause (written out elsewhere as «Hec igitur comanda vestra eat, maneat … ad vestri redegum»). The record codes the risk field `none` and the loss rule by incorporation.
- **`amount_as_read` in doc. 70:** the field holds the total of comandas carried under a partnership over commissions, not a sum entrusted in the act. A question about the field, not an error of reading.
- **The scorer** applies containment only to clause lines, so 14 lines where the reading merely ran longer than the field were flagged; harmless here, since all were ruled, but worth extending before the next run.

## The 36 flagged lines

Prepared by the assistant (`claude-opus-5-5`) after MS's filled sheet was pushed (commit `d170115`, research-ledger entry `20261120T074718Z-historee_codebooks-d1701151eec8`) and the draw key was checked against its hash. **Recommendations only; MS rules each line against the printed volume.** The print evidence quoted below is from the OCR text layer of the edition, read for this purpose after the freeze; check it against the book.

Classes (protocol): **content error** counts toward the record's rate; **form error** is counted apart; **reader's slip** means the record is right; **no error** / **match** means the scorer flagged a line on which the two agree.

## Recommended content errors (5)

### Line 6: doc. 193, p. 317, parties (parties, `CMD-193-1`)

- **Your reading:** "Johannes Muner, Bernardus Vila, nomine meo proprio et ut procurator, ad hec et alia specialiter et legitime constitutus per Johannem Parers, mercatore cive Barchinone, prout constat instrumento publico inde facto in posse discreti Thome de Pulcromonte, XXª die mensis marcii anno a Nativitate Domini .Mº.CCCCº.XIIIIº.; Johannes Parers, Bertrandus Canyellas, Galcerandus de Fontelles, Franciscus Oliba, maior diebus, Franciscus ça Rovira, Michael Franch, Girardo de Doni, Caterina, uxor venerabilis Leonardi de Doni, mercatoris, Guillelmus Petrus ça Rovira. Narcisia, uxor Bartholomei de Manso, quondam mercatoris, Franciscus Novella, Bernardus Fornerii, Nicholaus Pujada, Petrus Riquerii, Petrus Sirvent, Leonardus de Doni, nomine meo proprio et ut procurator, prout assero, dicti Gerardi de Doni et domine Caterine, uxoris mee; Bernardus Muntaner, Petrus Mathes, Petrus Taraval, Anthonius Salavert, Anthonius Sirvent, maior diebus, Anthonius Salvador et Galcerandus Ferrarii, minor diebus, omnes mercatores; Franciscus Solerii, Johannes Solerii, Berengarius Bartholomei et Johannes de Junyent, omnes draperii; Thomas Castelli, patronus barche; Johannes de Belpuig, botigerius; Guillelmus Xanxo, civis; Jacobus Reig, blanquerius; Jacobus Molina, payerius; Johannes Mathes, formenterius; Franciscus Vilabella, textor panni lini; Anthonius Serra, magister domorum; Petrus Borrelli, parator panni lane; Jacobus Serradelli, ballistarius; Matheus d'en Hom, Laurencius Arters, lancerius; Guillelmus de Miranbello, parator panni lane; Petrus Ferrarii, payerius; Gabriell Goday, boterius, et Bernardus Soler, curritor auris, omnes cives Barchinone; Bartholomeus Aygabella, ville de Arlés; Guillelmus Januarii, de villa Oloti et Bernardus de Puigmijà, mercator ville Campirotundi, ac Berengarius Ollarii, draperius, civis Dertuse et Simon de Almanare, mercator, civis Terrachone."; "Franciscum Salavert et Guillelmum Geraldi, mercatores cives Barchinone", named as 'comanditarions'.
- **Record (`parties`):** declarant: 55 investors (named pp. 317-318) | to: .NR
- **Recommendation: content error.** The record has the 55 investors but `to: .NR`. The print names the agents: «vos Franciscum Salavert et Guillelmum Geraldi, mercatores cives Barchinone, confessos fuisse a nobis habuisse …». A party the act names is missing. (The editor's heading calls the two agents *comanditarios*.)
- **Ruling (MS):** content error. "agreed." (2026-11-20 18:49 JST). Side note put to MS: his list omitted the first five investors at the foot of p. 317 (Devesa to Figueret); not a ruling on the record.

### Line 19: doc. 16, p. 162, date (date, `CMD-016-1`)

- **Your reading:** "Actum est hoc .IXº. kalendas aprilis anno Domini .Mº.CCº.LXº. primo."
- **Record (`date_as_read`):** .NR
- **Recommendation: content error.** The print dates the act: «Actum est hoc .IX°. kalendas aprilis anno Domini .M°.CC°.LX°. primo.» The record has `.NR`.
- **Ruling (MS):** content error. "This act is dated." (2026-11-20 18:46 JST)

### Line 21: doc. 15, p. 161, date (date, `CMD-015-1`)

- **Your reading:** "Actum est hoc quarto kalendas januarii anno Domini millesimo .CCº.LXº."
- **Record (`date_as_read`):** Actum est hoc quarto kalendas januarii anno Domini millesimo 
- **Recommendation: content error.** The record stops at «millesimo»; the print continues «.CC°.LX°.» on the next line. Cut before the year.
- **Ruling (MS):** content error. "content error indeed." (2026-11-20 18:47 JST)

### Line 34: doc. 84, p. 215, date (date, `CMD-084-1`)

- **Your reading:** "Die jovis nonas decembris anno Domini millesimo .CCCº.XXXº. primo."
- **Record (`date_as_read`):** Die jovis nonas decembris anno Domini millesimo 
- **Recommendation: content error.** The record stops at «millesimo»; the print continues «.CCC°.XXX°. primo.» on the next line. Cut before the year.
- **Ruling (MS):** content error. "agreed." (2026-11-20 18:47 JST)

### Line 55: doc. 162, p. 291, date (date, `CMD-162-1`)

- **Your reading:** "Die sabbati .XVIIIª die mensis augusti anno a Nativitate Domini .Mº. .CCCº.XCº. septimo. "
- **Record (`date_as_read`):** Actum est hoc Barchinone octava decima die mensis augusti anno a Nativitate Domini 
- **Recommendation: content error.** The record takes the closing clause «Actum est hoc Barchinone octava decima die mensis augusti anno a Nativitate Domini» and stops before the year, which the print gives on the next line («.M°.CCC°.XC°. septimo.»). Your reading is the opening date line of the same act; both are in the print, and either would be right in full. The error is the cut year.
- **Ruling (MS):** content error. "agreed." (2026-11-20 18:48 JST)

## Recommended reader's slips (11)

### Line 1: doc. 72, p. 206, risk (clause-present, `CMD-072-1`)

- **Your reading:** "Et pro hiis complendis, obligo vobis et vestris me et omnia bona mea mobilia et inmobilia, habita et habenda."
- **Record (`peril_clause_quote`):** Hec autem comanda eat, maneat et redeat ad voluntatem Dei et vestri redegum et fortunam.
- **Recommendation: reader's slip (question wording).** The record's clause is in the print: «Hec autem comanda eat, maneat et redeat ad voluntatem Dei et vestri redegum et fortunam.» Your reading is the next sentence, the obligation clause. My question listed risicum, periculum, fortuna but not *redegum*, the Catalan-Latin word these notaries use.
- **Ruling (MS):** reader's slip, caused by the question wording (redegum not among the signal words; the obligation clause given instead). "agreed." (2026-11-20 18:53 JST)

### Line 15: doc. 221, p. 344, security (clause-absent, `CMD-221-1`)

- **Your reading:** "dictus Gabriel teneretur et obligatus esset tradere et deliberare tibi dictam comandam et totum lucrum cum ea factum et eodem casu vos dictus Guillelmus, filius meus, haberetis et teneremini cancellare eidem Gabrieli dictum comande instrumentum, et quod inde facerem vos presens procuracionis instrumentum. Idcirco constituo et ordino vos eundem Guillelmum Bertrandi, filium meum, presentem, procuratorem meum ad petendum et audiendum compotum et racionem ab eodem Gabriele de dicta comanda et de lucro eiusdem, et ipsum compotum laudandum et sive impugnandum, et ipsam comandam et sui lucrum et totum id quod michi debebitur pro ipsa comanda petere, exigere et recipere et apochas etc. de receptis etc."
- **Record (`security_quote`):** .NR
- **Recommendation: reader's slip (question wording).** Doc. 221 is a power of attorney. The passage you quote recites what the agent Gabriel had agreed to do («teneretur et obligatus esset tradere»); it binds no person or goods for this act's performance. The record's `none` holds. My question ('binding a person or goods for performance') was wide enough to admit the recital.
- **Ruling (MS):** reader's slip, caused by the question wording ("binding a person ... for performance" admitted a recital of the agent's duty in a power of attorney). "sure." (2026-11-20 18:54 JST)

### Line 25: doc. 27, p. 170, risk (clause-present, `CMD-027-1`)

- **Your reading:** "Obligans tibi et tuis pro dicta comanda et etiam pro hiis omnibus firmiter complendis, attendendis et observandis, me et omnia bona mea mobilia et inmobilia presencia et futura, in quibus magis tu et tui habere et accipere volueritis sine vestro dampno. Renuncians scienter et consulte penitus de presenti omni juri, racioni et consuetudini, quibus me in hiis tueri possem, differre vel excusare, aut contra in aliquo venire."
- **Record (`peril_clause_quote`):** Hoc tamen expresso et declarato, quod de hac comanda tua possim simul cum mercibus et rebus meis transmitere per mare et terram ad tuum redegum et fortunam.
- **Recommendation: reader's slip (question wording).** As line 1: the clause is in the print, «Hoc tamen expresso et declarato, quod de hac comanda tua possim … transmitere per mare et terram ad tuum redegum et fortunam.» Your reading is the obligation clause (correctly given again at line 53).
- **Ruling (MS):** reader's slip, caused by the question wording (redegum not among the signal words). "agreed." (2026-11-20 18:54 JST)

### Line 33: doc. 138, p. 264, destination (destination, `CMD-138-1`)

- **Your reading:** none
- **Record (`destination`):** ad dictas partes Alexandrie et de Barut
- **Recommendation: reader's slip.** The print has the destination inside the act: «portamus in comanda vestra, cum dicta navi Jacobi Oliverii ad dictas partes Alexandrie et de Barut», as the record has.
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:53 JST). Cause: destination in the act's text, introduced by «dictas», missed.

### Line 38: doc. 174, p. 301, risk (clause-absent, `CMD-174-1`)

- **Your reading:** "Quod implicamentum etc." (this seems to be an abrreviated risk clause)
- **Record (`peril_clause_quote`):** .NR
- **Recommendation: reader's slip.** «Quod implicamentum etc.» is in act [2] of entry 174, not in act [1]. And it is not a risk clause: where this formula is written out it is the return promise, «Quod implicamentum promitto reducere et tornare in posse vestri …», with the risk clause following separately («Hec igitur comanda vestra eat, maneat … ad vestri redegum, periculum et fortunam»).
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:55 JST). Cause: a formula from act [2] given for act [1]; and «Quod implicamentum etc.» is the return promise, not a risk clause.

### Line 41: doc. 174 act 2, p. 301, risk (clause-absent, `CMD-174-2`)

- **Your reading:** "Quod implicamentum etc." (again, an abbreviated risk clause)
- **Record (`peril_clause_quote`):** .NR
- **Recommendation: reader's slip.** As line 38: «Quod implicamentum etc.» abbreviates the return promise, not a risk clause. The record's `none` holds; the row's loss rule comes from the incorporation «Simile comande instrumentum», which the record records separately.
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:56 JST). «Quod implicamentum etc.» is the return promise. Open, not ruled: whether «Hec igitur etc.» in act [2] abbreviates the risk clause (written out elsewhere as «Hec igitur comanda vestra eat, maneat ... ad vestri redegum»); the record codes the loss rule by incorporation («Cum posse primi instrumenti») and the risk field as none.

### Line 44: doc. 75, p. 210, destination (destination, `CMD-075-1`)

- **Your reading:** "PARA LLEVAR A MARSELLA"
- **Record (`destination`):** ad partes Marsilie
- **Recommendation: reader's slip.** «PARA LLEVAR A MARSELLA» is the editor's heading. The act reads «in viatico quod facio ad partes Marsilie», as the record has.
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:53 JST). Cause: the editor's heading read instead of the act; same place.

### Line 45: doc. 204 act 2, p. 329, amount (amount, `CMD-204-2`)

- **Your reading:** "octingentas quinquaginta una libras, undecim solidos et sex denarios Barchinone, implicitas simul cum centum libris domine Isabelis, uxoris vestre, et ducentis libris meis propriis, in quodam comuni centum nonaginta sex pannorum lane diversorum colorum"
- **Record (`amount_as_read`):** de centum libris
- **Recommendation: reader's slip.** Line asks for act 2 of entry 204. The edition does not number the acts, but the second begins «Gabriel Cardona predictus facio aliud instrumentum comande vobis predicte domine Isabeli … de centum libris habitis per manus dicti viri vestri». The record's «de centum libris» is that act's sum; your reading is act 1's.
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:50 JST). Cause: act 2 of an entry the edition does not number.

### Line 52: doc. 9, p. 156, parties (parties, `CMD-009-1`)

- **Your reading:** Raimundus de Bagnariis (agent); Raimundus Ricardi (investor);
- **Record (`parties`):** declarant: Bernardus de Fontibus, civis Barchinone | to: Berengario Colomera
- **Recommendation: reader's slip.** Doc. 9 (bottom of p. 156) reads «ego Bernardus de Fontibus, civis Barchinone, confiteor et recognosco tibi Berengario Colomera, militi», as the record has. Your names (Raimundus de Bagnariis, Raimundus Ricardi) are doc. 6's, which you read for line 22.
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:50 JST). Cause: doc. 6's parties given for doc. 9.

### Line 54: doc. 174 act 2, p. 301, parties (parties, `CMD-174-2`)

- **Your reading:** Ludovicus Cirvent (agent); Bernardus Sent Martí (investor); [Miquel de Gualbes (consignee)]
- **Record (`parties`):** declarant: Ludovicus Cirvent | to: venerabili Francisco Sunyerii
- **Recommendation: reader's slip.** Line asks for act 2 of entry 174. Act [2] (22 August) is to «venerabili Francisco Sunyerii», as the record has; Bernardus Sent Martí is the investor of act [1]. Michael de Gualbis, whom you add, is in act [2], as consignee.
- **Ruling (MS):** reader's slip. "agreed." (2026-11-20 18:51 JST). Cause: act 1's investor given for act 2; consignee of act 2 added.

### Line 56: doc. 98, p. 228, parties (parties, `CMD-098-1`)

- **Your reading:** Arnaldus de Bastida (agent); Arnaldus de Conamines (investor)
- **Record (`parties`):** declarant: Arnaldus de Bastida, mercator civis Barchinone | to: domine Caterine
- **Recommendation: reader's slip (question wording).** The act's parties are Arnaldus de Bastida and «domine Caterine, uxori Arnaldi de Conomines … quondam, tutrici Francisci»; the record names them. Arnaldus de Conamines is the dead investor of the underlying comanda, not a party to this receipt. My question ('who entrusts, who receives') invited the comanda's roles rather than the act's parties.
- **Ruling (MS):** reader's slip, caused by the question wording ("who entrusts, who receives" invited the underlying comanda's roles, not the act's parties). "agreed." (2026-11-20 18:52 JST)

## Recommended form errors (6)

### Line 2: doc. 142, p. 269, parties (parties, `CMD-142-1`)

- **Your reading:** "Sit omnibus notum, quod ego Michael Buguera, mercator civis Barchinone, confiteor et recognosco vobis domine Francisce, uxori Petri Robioni, quondam mercatoris civis dicte civitatis, quod habui et recipi a vobis et teneo in vestra comanda ad mercandum, ducentas libras monete Barchinone de terno, quas de voluntate vestra posui et misi in comuni societatis quam noviter contraxi cum aliquibus sociis meis."
- **Record (`parties`):** declarant: Michael Buguera, mercator civis Barchinone | to: domine Francisce
- **Recommendation: form error.** Same persons in the same roles. The record shortens identifications or uses its `declarant | to` format; your reading gives fuller titles or role labels. No person, role or name differs.
- **Ruling (MS):** form error. "agreed." (2026-11-20 19:01 JST)

### Line 4: doc. 195, p. 320, parties (parties, `CMD-195-1`)

- **Your reading:** "Die lune .XIIIª die mensis madii anno a Nativitate Domini .MºCCCCº.XVº. Petrus Miret, mercator civis Barchinone, confiteor et recognosco vobis venerabili Bernardo Fabre, botigerio civi Barchinone, et Johanni Damiani, mercatori ville Montis Pesullani, quod habui et recepi a vobis et porto in vestra comanda ad partes Alexandrie et ad alias mundi partes, in quibus navis Petri Stephani, ville sancti Felicis Guixellensis, causa mercandi portum faciet, sexaginta tres libras et quinque solidos barchinonenses de terno, implicitas in duobus *sachs de violes boschanes* ponderis nitidarum *de tares* undecim quintalium et medii ad pondus Barchinone, solutis generalitate, uno denario de manifesto et aliis, dempto naulo."
- **Record (`parties`):** declarant: Petrus Miret, mercator civis Barchinone | to: venerabili Bernardo Fabre et Johanni Damiani
- **Recommendation: form error.** Same persons in the same roles. The record shortens identifications or uses its `declarant | to` format; your reading gives fuller titles or role labels. No person, role or name differs.
- **Ruling (MS):** form error. "agreed." (2026-11-20 19:01 JST)

### Line 10: doc. 91, p. 221, parties (parties, `CMD-091-1`)

- **Your reading:** "Ego Franciscus de Caldevol, mercator civis, filius Bernardi de Caldevol, lancerii civis Barchinone, confiteor et recognosco vobis Bernardo Viaderii, argentario Barchinone, quod habui et recepi a vobis et teneo in vestra comanda tresdecim libras monete Barchinone de terno."
- **Record (`parties`):** declarant: Franciscus de Caldevol, mercator civis | to: Bernardo Viaderii
- **Recommendation: form error.** Same persons in the same roles. The record shortens identifications or uses its `declarant | to` format; your reading gives fuller titles or role labels. No person, role or name differs.
- **Ruling (MS):** form error. "agreed." (2026-11-20 19:02 JST)

### Line 29: doc. 207, p. 331, parties (parties, `CMD-207-1`)

- **Your reading:** Petrus Muntsech (agent), Antonio Ledó (investor),
- **Record (`parties`):** declarant: Petrus Muntsech, magister axie civis Barchinone | to: Antonio Ledó
- **Recommendation: form error.** Same persons in the same roles. The record shortens identifications or uses its `declarant | to` format; your reading gives fuller titles or role labels. No person, role or name differs.
- **Ruling (MS):** form error. "agreed." (2026-11-20 19:02 JST)

### Line 36: doc. 141, p. 268, parties (parties, `CMD-141-1`)

- **Your reading:** Bernardus Guardiola, Petrus Ballistarii, Johannes Guardiola and Michael Marçal (obligors); Johannes Guardiola and Michael Marçal (travellers/agents); Durandus Guarcia (investor)
- **Record (`parties`):** declarant: Bernardus Guardiola, Petrus Ballistarii, Johannes Guardiola et Michael Marçal, cives Barchinone | to: Durando Guarcia
- **Recommendation: form error.** Same persons in the same roles. The record shortens identifications or uses its `declarant | to` format; your reading gives fuller titles or role labels. No person, role or name differs.
- **Ruling (MS):** form error. "agreed." (2026-11-20 19:03 JST). The reading adds that only two of the four declarants travel; the record's format does not hold that distinction.

### Line 60: doc. 60, p. 199, parties (parties, `CMD-060-1`)

- **Your reading:** Guillelmus Francesci de Podio and Bonanat de Torre (agents); Jacobus de Malvino (investor)
- **Record (`parties`):** declarant: Guillelmus Francisci de Podio et Bonanat de Turre, cives Barchinone | to: Jacobo de Malvino
- **Recommendation: form error.** Same persons in the same roles. The record shortens identifications or uses its `declarant | to` format; your reading gives fuller titles or role labels. No person, role or name differs.
- **Ruling (MS):** form error. "agreed." (2026-11-20 19:03 JST). Spelling checked after the ruling: the act prints «Guillelmus Francisci de Podio et Bonanat de Turre», as the record has; «Francesc» and «Torre» are the editor's Catalan heading.

## Recommended no error (14)

### Line 3: doc. 70, p. 204, destination (destination, `CMD-070-1`)

- **Your reading:** "ad partes Candie et Xipri in navi Raimundi Laurencii et sociorum, vel ad quecumque alia loca dicta navis portum faciat causa mercandi"
- **Record (`destination`):** ad partes Candie et Xipri
- **Recommendation: no error.** The record's destination is in your reading; your reading gives the surrounding phrase (ship, voyage, return leg).
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:59 JST)

### Line 8: doc. 237, p. 360, amount (amount, `CMD-237-1`)

- **Your reading:** "porto in vestra comanda in viagio quod, volente Domino, facere debeo versus partes de Levant cum navi venerabilis Melchioris Mates, mille septingentas tres libras, decem novem solidos et sex denarios barchinonenses, implicitas in XVIII."
- **Record (`amount_as_read`):** mille septingentas tres libras, decem novem solidos et sex denarios barchinonenses
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:57 JST)

### Line 13: doc. 70, p. 204, amount (amount, `CMD-070-1`)

- **Your reading:** "[...] quequidem comande ascendunt ad trescentas sexaginta libras Barchinone vel circa, in quibus sunt centum octuaginta libre vestre proprie"
- **Record (`amount_as_read`):** trescentas sexaginta libras Barchinone vel circa
- **Recommendation: no error, with a note.** The record's value is in your reading. Note: doc. 70 is a partnership between two Jewish merchants on their commissions; «trescentas sexaginta libras … vel circa» is the total of comandas they carry, not a sum entrusted in this act. The record transcribes it faithfully; whether `amount_as_read` should hold it is a question about the field, not an error of reading.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:56 JST). Noted, not ruled: doc. 70 is a partnership over commissions; the 360 lb is the total of comandas carried, not a sum entrusted in this act, which bears on what amount_as_read should hold.

### Line 16: doc. 16, p. 162, destination (destination, `CMD-016-1`)

- **Your reading:** none (the document concerns the settlement of a venture described in another document)
- **Record (`destination`):** .NR
- **Recommendation: match.** Your reading is 'none' with a note after it; the scorer read the note as part of the answer. 'none' agrees with the record's `.NR`.
- **Ruling (MS):** match. "agreed." (2026-11-20 19:00 JST). Flagged only because the scorer read the bracketed note as part of the answer.

### Line 22: doc. 6, p. 154, amount (amount, `CMD-006-1`)

- **Your reading:** "Sit notum omnibus, quod ego Raimundus de Bagnariis confiteor et recognosco tibi Raimundo Ricardi et tuis, quod recepi in tua comanda quingentos bizancios argenti [...]".
- **Record (`amount_as_read`):** quingentos bizancios argenti
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:57 JST)

### Line 30: doc. 204, p. 329, amount (amount, `CMD-204-1`)

- **Your reading:** "octingentas quinquaginta una libras, undecim solidos et sex denarios Barchinone, implicitas simul cum centum libris domine Isabelis, uxoris vestre, et ducentis libris meis propriis, in quodam comuni centum nonaginta sex pannorum lane diversorum colorum"
- **Record (`amount_as_read`):** octingentas quinquaginta una libras, undecim solidos et sex denarios Barchinone
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:58 JST)

### Line 32: doc. 222, p. 345, amount (amount, `CMD-222-1`)

- **Your reading:** "nonaginta duas libras, decem octo solidos et unum denarium barchinonenses, smerciatas in rebus sequentibus: [...]"
- **Record (`amount_as_read`):** nonaginta duas libras, decem octo solidos et unum denarium barchinonenses
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:58 JST)

### Line 40: doc. 93, p. 223, destination (destination, `CMD-093-1`)

- **Your reading:** "nunc existentis in portu Maioricarum, que nunc, dante Domino, est itura apud Cadis a Maioricis recedendo, redeundo Maioricis, [...]"
- **Record (`destination`):** apud Cadis
- **Recommendation: no error.** The record's destination is in your reading; your reading gives the surrounding phrase (ship, voyage, return leg).
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:59 JST)

### Line 42: doc. 72, p. 206, destination (destination, `CMD-072-1`)

- **Your reading:** "in viatico quod nunc facturus sum ad partes Valencie"
- **Record (`destination`):** ad partes Valencie
- **Recommendation: no error.** The record's destination is in your reading; your reading gives the surrounding phrase (ship, voyage, return leg).
- **Ruling (MS):** no error. "agreed." (2026-11-20 19:00 JST)

### Line 50: doc. 226, p. 349, destination (destination, `CMD-226-1`)

- **Your reading:** none. This is a receipt, not a venture to be undertaken
- **Record (`destination`):** .NR
- **Recommendation: match.** Your reading is 'none' with a note after it; the scorer read the note as part of the answer. 'none' agrees with the record's `.NR`.
- **Ruling (MS):** match. "agreed." (2026-11-20 19:00 JST). Flagged only because the scorer read the note after "none" as part of the answer.

### Line 51: doc. 147, p. 274, amount (amount, `CMD-147-1`)

- **Your reading:** "quadraginta tres libras Barchinone, implicitas in tres balas de cuyram de recamudes"
- **Record (`amount_as_read`):** quadraginta tres libras Barchinone
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:58 JST)

### Line 57: doc. 177, p. 304, amount (amount, `CMD-177-1`)

- **Your reading:** "trecentis sexaginta quinque libris, undecim solidis et octo denariis Barchinone, implicitis, videlicet, ducente libre simul cum rebus et mercibus comunis mei dicti Francisci Brugal, et residue centum sexaginta quinque libre, undecim solidi et octo denarii in una bala septem pannorum lane de Villa Francha de Conflent et in duabus caxiis de ferret ponderis nitidi viginti unius rovarum et octo librarum ad pondus et quintale Barchinone, et in quadam aluda de saffrà ponderis nitidi viginti quatuor librarum, et eciam in duobus caxetes plenis de ulleres vitri sive de vidre, solutis generalitate, pariatico et aliis missionibus, excepto naulo."
- **Record (`amount_as_read`):** trecentis sexaginta quinque libris, undecim solidis et octo denariis Barchinone
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:58 JST)

### Line 58: doc. 219, p. 342, amount (amount, `CMD-219-1`)

- **Your reading:** "centum triginta septem libras, implicitas in duabus balis pannorum lane de la terra, in quarum altera sunt octo, scilicet, sex burelli mesclats et due palmelle de Gerunda, et in altera sunt octo panni burelli de Oloti, soluti[s] generalitate et aliis averiis, et missis in dicta navi, dempto naulo."
- **Record (`amount_as_read`):** centum triginta septem libras
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:59 JST)

### Line 59: doc. 138, p. 264, amount (amount, `CMD-138-1`)

- **Your reading:** "viginti septem libras et quatuordecim solidos, implicitas in quindecim libris de safrano, soluto nauleo, quirato, generalitat et aliis missionibus, oneratis in navi."
- **Record (`amount_as_read`):** viginti septem libras et quatuordecim solidos
- **Recommendation: no error.** The record's value (the sum and the money) is in your reading word for word; your reading adds the surrounding words (what the sum is invested in). The scorer applies containment only to clause lines, so it flagged these.
- **Ruling (MS):** no error. "agreed." (2026-11-20 18:59 JST)
