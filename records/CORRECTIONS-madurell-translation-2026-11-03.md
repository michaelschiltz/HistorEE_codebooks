# Corrections to the comanda primary records from the Madurell translation (2026-11-03)

**Applied by the assistant (`claude-opus-5-5`) on 2026-11-03 at MS's instruction ("Then the other corrections"; successor files; records plus recount report).** The source is the full image-based translation of Madurell Marimón & García Sanz 1973, docs 1–255 and Glosario, in chunks L01–L24 (Google Docs, `translations/Madurell-GarciaSanz-1973/`). The rulings applied are in `records/RULINGS-madurell-translation-2026-11-03.md`.

The 2026-10-27 files are untouched. The corrected records are successor files:

- `records/act-census-2026-11-03.csv` (255 rows)
- `records/instances-2026-11-03.csv` (118 rows: 115 + 3 split acts)
- `records/instance-chars-2026-11-03.csv` (1,116 rows)

**The full ledger is `records/CORRECTIONS-madurell-translation-2026-11-03.csv`: 1103 changes, one row per field changed, with old value, new value, rule and the L-chunk that found it.** This note summarises it.

**Conventions.**

- Notes are appended, never rewritten, and every appended note opens `[2026-11-03]`.
- A date in a census note is corrected in its leading token, and the correction is restated in the appended note.
- `instance-chars` rows derived for instances that move to `comanda` say so in their notes. They apply the 2026-10-27 coder's own field-to-cell mapping: CF2/RB1/RB2/RB4/LP2 from the loss rule; LR2/LR3/LR6/CF1 from the profit rule; RB3 from security; TS2 from duration; CI1/CF3 from `n_investors`; CI5 from the common fund. The mapping was tabulated over the 55 `comanda` instances of 2026-10-27, and it held without exception where the field was filled. The derived rows are not a fresh reading of each act. `CI3` is not derived.
- Files are written LF, as `.gitattributes` requires. The 2026-10-27 files are CRLF.

## Counts by file and rule

| file | rule | changes |
|---|---|---|
| census | D-207 | 2 |
| census | D-ABBR | 84 |
| census | D-ABBR+D-SALV | 2 |
| census | D-BELL | 18 |
| census | D-ERRAND | 2 |
| census | D-SALV | 12 |
| census | D-SIM | 7 |
| census | D105/D-ERRAND | 6 |
| census | acts | 6 |
| census | date | 21 |
| census | gloss | 2 |
| census | loss | 2 |
| census | open | 9 |
| census | parties | 6 |
| census | profit | 2 |
| census | security | 2 |
| instance-chars | D-ABBR | 18 |
| instance-chars | D-BELL | 2 |
| instance-chars | D105 | 10 |
| instance-chars | context | 2 |
| instance-chars | derived | 386 |
| instance-chars | derived-profit | 8 |
| instance-chars | quote | 98 |
| instances | D-207 | 4 |
| instances | D-ABBR | 60 |
| instances | D-ABBR+D-SALV | 3 |
| instances | D-BELL | 6 |
| instances | D-SALV | 6 |
| instances | D-SIM | 6 |
| instances | D105/D-ERRAND | 2 |
| instances | amount-truncated | 7 |
| instances | amount-wrong | 49 |
| instances | date | 54 |
| instances | destination | 29 |
| instances | loss | 2 |
| instances | note | 1 |
| instances | object | 1 |
| instances | ocr | 57 |
| instances | parties | 60 |
| instances | profit | 4 |
| instances | quote | 5 |
| instances | quote-witness | 18 |
| instances | rescope | 8 |
| instances | security | 2 |
| instances | split | 12 |

## Form assignments

**Census.** 60 acts move `neither` → `comanda`:

- D-ABBR 41;
- D-ABBR with D-SALV 1;
- D-BELL 9;
- D-SALV 6;
- D-SIM 3.

3 acts move `comanda` → `neither` (D105/D-ERRAND: 104, 105, 152). Totals: `comanda` 145 → 202, `neither` 108 → 51, `comanda_ad_societatem` 2.

| doc | rule | new form |
|---|---|---|
| 59 | D-BELL | comanda |
| 60 | D-BELL | comanda |
| 89 | D-SALV | comanda |
| 99 | D-ABBR | comanda |
| 100 | D-ABBR | comanda |
| 102 | D-ABBR | comanda |
| 103 | D-ABBR | comanda |
| 116 | D-ABBR | comanda |
| 117 | D-ABBR | comanda |
| 118 | D-ABBR | comanda |
| 123 | D-ABBR | comanda |
| 125 | D-ABBR | comanda |
| 128 | D-ABBR | comanda |
| 136 | D-ABBR | comanda |
| 138 | D-ABBR | comanda |
| 147 | D-ABBR | comanda |
| 149 | D-SALV | comanda |
| 153 | D-SALV | comanda |
| 164 | D-ABBR | comanda |
| 165 | D-ABBR | comanda |
| 167 | D-ABBR | comanda |
| 168 | D-ABBR+D-SALV | comanda |
| 170 | D-ABBR | comanda |
| 171 | D-ABBR | comanda |
| 172 | D-ABBR | comanda |
| 173 | D-ABBR | comanda |
| 174 | D-SIM | comanda |
| 175 | D-SALV | comanda |
| 176 | D-ABBR | comanda |
| 177 | D-ABBR | comanda |
| 178 | D-ABBR | comanda |
| 180 | D-ABBR | comanda |
| 181 | D-SIM | comanda |
| 182 | D-ABBR | comanda |
| 183 | D-ABBR | comanda |
| 187 | D-ABBR | comanda |
| 188 | D-ABBR | comanda |
| 189 | D-SALV | comanda |
| 192 | D-ABBR | comanda |
| 194 | D-ABBR | comanda |
| 195 | D-ABBR | comanda |
| 196 | D-SIM | comanda |
| 197 | D-ABBR | comanda |
| 203 | D-ABBR | comanda |
| 204 | D-ABBR | comanda |
| 205 | D-ABBR | comanda |
| 206 | D-ABBR | comanda |
| 209 | D-ABBR | comanda |
| 213 | D-ABBR | comanda |
| 215 | D-SALV | comanda |
| 217 | D-ABBR | comanda |
| 225 | D-ABBR | comanda |
| 233 | D-BELL | comanda |
| 237 | D-ABBR | comanda |
| 239 | D-BELL | comanda |
| 240 | D-BELL | comanda |
| 241 | D-BELL | comanda |
| 242 | D-BELL | comanda |
| 244 | D-BELL | comanda |
| 245 | D-BELL | comanda |
| 104 | D105/D-ERRAND | neither |
| 105 | D105/D-ERRAND | neither |
| 152 | D105/D-ERRAND | neither |

**Instances.** The mod3 sample changes as follows:

- 25 instances move `neither` → `comanda`;
- 2 new mod3 acts are split out (`CMD-174-2`, `CMD-204-2`);
- `CMD-105-1` moves `comanda` → `neither`.

mod3 `comanda` goes from 45 to 71 instances, and mod3 `neither` from 42 to 18. The directed sample gains `CMD-217-1` (moved) and `CMD-217-2` (split).

| instance | rule | loss_rule (new) |
|---|---|---|
| CMD-060-1 | D-BELL | investor (abbreviated; city formula) |
| CMD-099-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-102-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-117-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-123-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-138-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-147-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-153-1 | D-SALV | investor (by the salvage clause; entry unfinished) |
| CMD-165-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-168-1 | D-ABBR+D-SALV | investor (abbreviated; house formula; salvage clause abbreviated) |
| CMD-171-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-174-1 | D-SIM | investor (incorporated by 'simile') |
| CMD-177-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-180-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-183-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-189-1 | D-SALV | investor (by the salvage clause; bounded to the coral chests, sailing… |
| CMD-192-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-195-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-204-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-213-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-217-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-225-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-237-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-240-1 | D-BELL | investor (abbreviated; city formula) |
| CMD-129-1 | D-ABBR | investor (abbreviated; house formula) |
| CMD-135-2 | D-ABBR | investor (abbreviated; house formula) |
| CMD-105-1 | D105/D-ERRAND | (unchanged) |
| CMD-174-2 (new) | D-SIM | (see row) |
| CMD-204-2 (new) | D-SIM | (see row) |
| CMD-217-2 (new) | D-SIM | (see row) |

## Structure

- **Merged acts split** (census `acts_in_entry` 2 against one instance):
  - `CMD-174-1` / `-174-2` (Francesc Sunyer's 420 lb);
  - `CMD-204-1` / `-204-2` (Isabel's 100 lb);
  - `CMD-217-1` / `-217-2` (535 lb 3 s 8 d).
- **Collapsed entries re-scoped to act [1].** Each 2026-10-27 instance counted the investors of a whole entry as one act's. Acts [2]–[n] are not instanced; that is deferred.
  - `CMD-081-1`: 4 investors counted;
  - `CMD-097-1`: 5;
  - `CMD-099-1`: 27;
  - `CMD-102-1`: 4.
- **Census `acts_in_entry`:** 238 1 → 2; 248 1 → 2 ([1] `neither` on its own, [2] `comanda`; the row stays `comanda`).

## Field corrections in `instances` (other than OCR)

**Amounts (wrong: leading number words lost in the text layer; truncated)** (56).

| instance | old | new | source |
|---|---|---|---|
| CMD-014-1 | sexaginta libras monete barchinonensis perpetue de terno | trecentas sexaginta libras monete barchinonensis perpetue de terno | L02 |
| CMD-015-1 | quatuor libras monete curribilis Barchinone perpetue de ter… | trecentas et octuaginta quatuor libras monete curribilis Barchinone perpetue de… | L02 |
| CMD-016-1 | duas libras de canyela | viginti duas libras de canyela | L02 |
| CMD-018-1 | septem libras et tres solidos et medium monete Barchinone d… | viginti septem libras et tres solidos et medium monete Barchinone de teerno | L02 |
| CMD-021-1 | octo libris et duodecim solidis monete Barchinone de terno | sexaginta octo libris et duodecim solidis monete Barchinone de terno | L02 |
| CMD-045-1 | quatuor solidos et septem denarios monete Barchinone de ter… | septuaginta quatuor solidos et septem denarios monete Barchinone de terno | L04 |
| CMD-048-1 | quinque libras monete Barchinone perpetue de terno | septuaginta quinque libras monete Barchinone perpetue de terno | L05 |
| CMD-060-1 | quinque libras Barchinone de terno | viginti quinque libras Barchinone de terno | L06 |
| CMD-069-1 | octo solidos monete Barchinone de terno | triginta octo solidos monete Barchinone de terno | L06 |
| CMD-070-1 | sexaginta libras Barchinone vel circa | trescentas sexaginta libras Barchinone vel circa | L06 |
| CMD-075-1 | duas libras et quinque solidos Barchinone de terno | triginta duas libras et quinque solidos Barchinone de terno | L07 |
| CMD-088-1 | quinquaginta libras barchinonenses de terno | centum et quinque libras monete predicte | L08 |
| CMD-090-1 | sani libras monete barchinonensium de terno | quingentas libras monete barchinonensium de terno | L08 |
| CMD-091-1 | tresdecim libras monete Barchinone de terno. Et ideo | tresdecim libras monete Barchinone de terno | L08 |
| CMD-092-1 | sex libras et decem solidos Barchinone | centum et triginta sex libras et decem solidos Barchinone | L08 |
| CMD-093-1 | triginta libras regalium Maiorice minutorum | trescentas triginta libras regalium Maiorice minutorum | L08 |
| CMD-094-1 | novem libras | nonagentas quadraginta novem libras, septem solidos et undecim denarios monete … | L08 |
| CMD-102-1 | septem libras | nonaginta septem libras, .IX. solidos et sex denarios Barchinone | L09 |
| CMD-107-1 | octuaginta libras et quatuor solidos et octo denarios monet… | octuaginta libras et quatuor solidos et octo denarios monete Barchinone de terno | L10 |
| CMD-108-1 | centum et quinquaginta libras et novem solidos et sex denar… | centum et quinquaginta libras et novem solidos et sex denarios monete Barchinon… | L10 |
| CMD-111-1 | novem libris Barchinone vel alterius cuiuscumque quantitatis | septuaginta novem libris Barchinone vel alterius cuiuscumque quantitatis | L10 |
| CMD-114-1 | octo libras] et portamus in viagio quod | [octo libras] | L10 |
| CMD-122-1 | centum et tres libras | centum et tres libras, sexdecim solidos et sex denarios monete Barchinone de te… | L11 |
| CMD-126-1 | tres libras | quadraginta tres libras, XIX solidos Barchinone | L11 |
| CMD-129-1 | septem libras et decem solidos Barchinone | viginti septem libras et decem solidos Barchinone | L11 |
| CMD-129-2 | quinque libris Barchinone | viginti quinque libris Barchinone | L11 |
| CMD-132-1 | septem libras .XV. solidos .IIII. denarios Barchinone | centum et decem septem libras .XV. solidos .IIII. denarios Barchinone | L12 |
| CMD-135-2 | quatuor libris Barchinone | viginti quatuor libris Barchinone | L12 |
| CMD-138-1 | septem libras et quatuordecim solidos | viginti septem libras et quatuordecim solidos | L12 |
| CMD-141-1 | quadraginta libras et decem solidos Barchinone | trescentas quadraginta libras et decem solidos Barchinone | L12 |
| CMD-147-1 | tres libras Barchinone | quadraginta tres libras Barchinone | L13 |
| CMD-150-1 | quinque libras Barchinone in peccunia Barchinone. Et ideo r… | quingentas quinquaginta quinque libras Barchinone in peccunia Barchinone | L13 |
| CMD-153-1 | quinque libras | viginti quinque libras, decem septem solidos et septem denarios monete Barchino… | L14 |
| CMD-154-1 | decem libras monete Barchinone de terno. Et ideo | centum decem libras monete Barchinone de terno | L14 |
| CMD-159-1 | .NR | XXVIm. quingentorum solidorum | L15 |
| CMD-165-1 | novem libras | septuaginta novem libras, tres solidos et duos denarios barchinonenses | L15 |
| CMD-171-1 | duas libras | centum septuaginta duas libras, unum solidum et quinque denarios barchinonenses… | L16 |
| CMD-174-1 | quatuordecim libris | quatuordecim libris, quatuordecim solidis et undecim denariis Barchinone | L16 |
| CMD-177-1 | quinque libris | trecentis sexaginta quinque libris, undecim solidis et octo denariis Barchinone | L16 |
| CMD-189-1 | duos bisancios | septuaginta duos bisancios, quatuor quiratos et medium monete Alexandrie | L17 |
| CMD-192-1 | tres libras Barchinone | triginta tres libras Barchinone | L17 |
| CMD-195-1 | tres libras et quinque solidos barchinonenses de terno | sexaginta tres libras et quinque solidos barchinonenses de terno | L18 |
| CMD-199-1 | novem libras | centum novem libras, tresdecim solidos et decem denarios barchinonenses | L18 |
| CMD-204-1 | una libras | octingentas quinquaginta una libras, undecim solidos et sex denarios Barchinone | L19 |
| CMD-213-1 | quinque libras barchinonenses de terno | centum octuaginta quinque libras barchinonenses de terno | L19 |
| CMD-216-1 | quatuor libras monete barchinonensium de terno | quadraginta quatuor libras monete barchinonensium de terno | L20 |
| CMD-217-1 | unam libras | quadrigentas tringa (sic) unam libras, decem solidos et decem denarios Barchino… | L20 |
| CMD-219-1 | septem libras | centum triginta septem libras | L20 |
| CMD-222-1 | duas libras | nonaginta duas libras, decem octo solidos et unum denarium barchinonenses | L20 |
| CMD-228-1 | duas libras | quadringentas viginti duas libras, decem novem solidos et sex denarios monete b… | L21 |
| CMD-231-1 | septem libras et quatuordecim solidos monete barchinonensiu… | septuaginta septem libras et quatuordecim solidos monete barchinonensium de ter… | L21 |
| CMD-234-1 | quatuor libras | ducentas viginti quatuor libras, decem septem solidos et sex denarios barchinon… | L21 |
| CMD-237-1 | tres libras | mille septingentas tres libras, decem novem solidos et sex denarios barchinonen… | L22 |
| CMD-246-1 | septingentas libras Barchinone | duas mille septingentas libras Barchinone | L22 |
| CMD-249-1 | quadraginta libras bar chinonenses | ducentas quadraginta libras barchinonenses | L23 |
| CMD-250-1 | quinquaginta libras barchinonenses | trescentas quinquaginta libras barchinonenses | L23 |

**Dates (`.NR` for a full date line, truncated, or OCR year)** (52).

| instance | old | new | source |
|---|---|---|---|
| CMD-070-1 | .NR | Die martis scilicet festum Beati Michaelis .IIIº. kalendas octobris anno predic… | L06 |
| CMD-099-1 | .NR | Die martis .III. nonas madi anno predicto [5 mayo 1349]. | L09 |
| CMD-120-1 | .NR | Die sabbati .XIX. die februarii anno a Nativitate Domini .Mº.CCCº.LXVIIIº. | L11 |
| CMD-135-1 | .NR | Die mercurii .XXXIª die madii anno a Nativitate Domini .MºCCCº.LXXº quarto. | L12 |
| CMD-135-2 | .NR | Die jovis XXI junii anno predicto. | L12 |
| CMD-147-1 | .NR | Die lune .VIIª. die mensis julii anno predicto [1382]. | L13 |
| CMD-150-1 | .NR | Die sabbati .XXVIIª die junii anno a Nativitate Domini .Mº.CCC.LXXX. tercio. | L13 |
| CMD-156-1 | .NR | Die jovis .XIIIIª mensis madii anno predicto [1394]. | L14 |
| CMD-189-1 | .NR | Die martis .XVII. die mensis aprilis anno predicto [1414]. | L17 |
| CMD-191-1 | .NR | Die sabbati .XXVIIª die mensis octobris anno predicto [1414]. | L17 |
| CMD-192-1 | .NR | Die mercurii .XXI. die mensis novembris anno predicto [1414]. | L17 |
| CMD-195-1 | .NR | Die lune .XIIIª die mensis madii anno a Nativitate Domini .MºCCCCº.XVº. | L18 |
| CMD-198-1 | .NR | Die sabati .XXXIª mensis augusti anno predicto millesimo .CCCCº.XVº. | L18 |
| CMD-204-1 | .NR | Die lune .XXVII. die dicti mensis jannuarii anno predicto [1421]. | L19 |
| CMD-207-1 | .NR | Die veneris .VIª die mensis novembris anno a Nativitate Domini .Mº.CCCCº.XXIIº. | L19 |
| CMD-213-1 | .NR | Die jovis .XXVII. mensis septembris anno predicto [1425]. | L19 |
| CMD-216-1 | .NR | Die Jovis .XIª. julii anno predicto [1426]. | L20 |
| CMD-217-1 | .NR | Die Jovis .XIª. die mensis decembris anno predicto [1427]. | L20 |
| CMD-219-1 | .NR | Die sabbati .XVª. die mensis octobris anno a Nativitate .MºCCCCº.XXº.IXº. | L20 |
| CMD-227-1 | .NR | Die lune .XIIII.ª mensis julii anno predicto [1449]. | L21 |
| CMD-228-1 | .NR | Die veneris .VIII.ª mensis augusti anno predicto [1449]. | L21 |
| CMD-231-1 | .NR | Die mercurii .XI.ª mensis augusti anno predicto a Nativitate Domini millesimo .… | L21 |
| CMD-234-1 | .NR | Die jovis .VI.ª mensis marcii anno predicto [1455]. | L21 |
| CMD-237-1 | .NR | Die mercurii .X.ª mensis octobris anno predicto [1459]. | L22 |
| CMD-243-1 | .NR | Die veneris .XI.ª mensis januarii anno predicto [1465]. | L22 |
| CMD-246-1 | .NR | Die sabbati .XVIIII.ª septembris anno predicto millesimo .CCCC.LX° septimo. | L22 |
| CMD-247-1 | .NR | Die veneris .XX.ª mensis augusti anno predicto [1473]. | L22 |
| CMD-249-1 | .NR | Die martis .XVII. mensis marcii anno a Nativitate Domini M.CCCC.LXXX nono. | L23 |
| CMD-250-1 | .NR | Die martis .XVII. mensis marcii anno a Nativitate Domini .M.CCCC.LXXX. nono. | L23 |
| CMD-253-1 | .NR | Die martis .XXVII.ª mensis julii anno a Nativitate Domini .M.D. primo. | L23 |
| CMD-129-1 | .NR | Die sabbati .XIIª die novembris anno a Nativitate Domini .Mº.CCCº.LXXº. tercio. | L11 |
| CMD-129-2 | .NR | Die sabbati .XIIª die novembris anno a Nativitate Domini .Mº.CCCº.LXXº. tercio. | L11 |
| CMD-141-1 | .NR | Die mercurii octava die octobris anno a Nativitate Domini .Mº.CCCº.LXXº.VI.º | L12 |
| CMD-141-2 | .NR | Die jovis .XVIª die octobris anno predicto [1376]. | L13 |
| CMD-165-1 | .NR | Die veneris .XVIIIª die mensis julii anno a Nativitate Domini .Mº.CCCº. .XCº. n… | L15 |
| CMD-199-1 | .NR | Die martis .Xª. die mensis marcii anno a Nativitate Domini Mº.CCCCº. .XVIº. | L18 |
| CMD-201-1 | .NR | Die sabbati .XXVIª. die augusti anno a Nativitate Domini .Mº.CCCCº. decimo nono… | L18 |
| CMD-210-1 | .NR | Die jovis .XXª. mensis madii anno predicto a Nativitate Domini millesimo .CCCCº… | L19 |
| CMD-225-1 | .NR | Die martis .XVIª mensis julii anno a Nativitate Domini .MºCCCCº.XXXº. septimo. | L20 |
| CMD-240-1 | .NR | Die mercurii .XXVIIII.ª mensis febroarii anno a Nativitate Domini .M°. .CCCC°.L… | L22 |
| CMD-102-1 | .NR | [1] .V. idus madii anno predicto [1349] [11 mayo 1349]. | L09 |
| CMD-097-1 | .NR | Die veneris intitulata .XV. kalendas madii anno Domini .M.CCC.XLIX. | L08 |
| CMD-098-1 | .NR | Die lune .XII. kalendas madii anno Domini .M.CCC.XLIX. | L08 |
| CMD-069-1 | .NR | Die sabbati, scilicet .VI. kalendas octobris [1299] | L06 |
| CMD-222-1 | .NR | Die martis .VIIIª die dictorum mensis et anni [junio 1434]. | L20 |
| CMD-142-1 | Actum est hoc Barchinone tricesima die mensis julii anno a … | Die sabbati .XXXª. die mensis julii anno a Nativitate Domini .Mº.CCCº.LXXº.IXº. | L13 |
| CMD-177-1 | Die vicesima tercia septembris anno  | Die vicesima tercia septembris anno .Mº.CCCCº. octavo. | L16 |
| CMD-180-1 | Die jovis octava dié augusti anno a Nativitate Domin i mill… | Die jovis octava die augusti anno a Nativitate Domini millesimo .CCCCº. nono. | L16 |
| CMD-183-1 | Die sabbati tricesima prima die augusti anno  | Die sabbati tricesima prima die augusti anno .Mº.CCCCº. nono. | L17 |
| CMD-186-1 | .NR | die jovis hora quinta post meridiem qua computabatur decima octava die febroari… | L17 |
| CMD-204-2 | .NR | Die lune .XXVII. die dicti mensis jannuarii anno predicto [1421]. (entry date; … | L19 |
| CMD-217-2 | .NR | Die Jovis .XIª. die mensis decembris anno predicto [1427]. (entry date; act [2]… | L20 |

**Destinations** (28).

| instance | old | new | source |
|---|---|---|---|
| CMD-066-1 | .NR | ad partes de Xipre | L06 |
| CMD-075-1 | ad partes Barchinone | ad partes Marsilie | L07 |
| CMD-099-1 | ad partes Xipri et de Rodes | ad partes Xipri et de Rodes o de Candia | L09 |
| CMD-105-1 | .NR | ad partes de Barut (payment at Damascus) | L10 |
| CMD-114-1 | .NR | ad partes Alexandrie | L10 |
| CMD-135-1 | .NR | ad partes de Rodes et de Xipro et de Barut | L12 |
| CMD-138-1 | .NR | ad dictas partes Alexandrie et de Barut | L12 |
| CMD-141-1 | .NR | ad partes de Rodes, Xipre et de Barut | L12 |
| CMD-141-2 | .NR | ad partes de Rodes, Xipre et de Barut | L13 |
| CMD-144-1 | .NR | ad partes de Barut | L13 |
| CMD-150-1 | .NR | ad partes regni Portugalensis | L13 |
| CMD-183-1 | .NR | ad dictas partes [Alaxandrie] (editorial supply) | L17 |
| CMD-186-1 | .NR | vers les parts de Rodes e de Barut | L17 |
| CMD-189-1 | .NR | ad dictas partes [Rodarum et Alexandrie] | L17 |
| CMD-198-1 | .NR | ad partes de Rodes, Cipri, Baruti et Damasci | L18 |
| CMD-199-1 | ad partes Sicilie | ad partes Sicilie, Rodarum, Sipri, Baruti, Damasci et Alexandrie | L18 |
| CMD-207-1 | .NR | ad partes ultramarinas | L19 |
| CMD-221-1 | ad partes Sicilie | ad partes Sicilie, Rodarum et de Levant et de Romania | L20 |
| CMD-222-1 | .NR | ad partes de Lavant | L20 |
| CMD-225-1 | .NR | ad partes de Levant; ad partes Sicilie e del Realme | L20 |
| CMD-231-1 | .NR | versus partes de Tunis | L21 |
| CMD-234-1 | .NR | ad partes de Tunis et de Alaxandria | L21 |
| CMD-237-1 | .NR | versus partes de Levant | L22 |
| CMD-240-1 | .NR | ad villam Aqualate et vel Cervarie et ad alias villas seu loca ad quas ... domi… | L22 |
| CMD-246-1 | .NR | versus partes de Levant | L22 |
| CMD-247-1 | .NR | ad partes regni Aragonum | L22 |
| CMD-249-1 | .NR | pro partibus de Levant | L23 |
| CMD-174-1 | .NR | ad dictas partes Alexandrie | L16 |

**Parties** (54).

| instance | old | new | source |
|---|---|---|---|
| CMD-048-1 | declarant: .NR / to: Marie | declarant: Petrus de Medalia et Philipus de Boscho, junior / to: Marie | L05 |
| CMD-060-1 | declarant: .NR / to: Jacobo de Malvino | declarant: Guillelmus Francisci de Podio et Bonanat de Turre, cives Barchinone … | L06 |
| CMD-066-1 | declarant: .NR / to: Nicholao de Samanis | declarant: Jacobus Laurenci et Berengarius Geraldi, cives Barchinone / to: Nich… | L06 |
| CMD-081-1 | declarant: .NR / to: Raymundo Regalis | declarant: Petrus de Episcopali et Bernardus de Sabateri, socii cives Barchinon… | L07 |
| CMD-087-1 | declarant: .NR / to: venerabili Bernardo de Burdillis | declarant: Petrus de Media Villa et Arnaldus Spaherii, cives Barchinone, et Ber… | L07 |
| CMD-088-1 | declarant: .NR / to: venerabili Petro de Mediavilla | declarant: Eymericus de Usallio / to: venerabili Petro de Mediavilla | L08 |
| CMD-091-1 | declarant: .NR / to: Bernardo Viaderii | declarant: Franciscus de Caldevol, mercator civis / to: Bernardo Viaderii | L08 |
| CMD-093-1 | declarant: .NR / to: Guillelmo Moratoni | declarant: Arnaldus Laurencii, mercator Barchinone, procurator Petri de Media V… | L08 |
| CMD-094-1 | declarant: .NR / to: Petro de Media Villa | declarant: Jacobus de Media Villa, mercator civis Barchinone / to: Petro de Med… | L08 |
| CMD-105-1 | declarant: .NR / to: Bernardo Durandi | declarant: Petrus de Croso et Petrus Pochasanch, cives Barchinone [patrones] co… | L10 |
| CMD-122-1 | declarant: Bernardus de Graells et Bernardus de Casis Albis… | declarant: Bernardus de Graells et Bernardus de Casis Albis, mercatores cives B… | L11 |
| CMD-129-2 | declarant: .NR / to: domine Isabeli | declarant: Franciscus Castilionis et Johannes Marqués, marinerii, cives Barchin… | L11 |
| CMD-135-2 | declarant: .NR / to: Jacobo Solà | declarant: Berengarius de Fabrica et Bernardus Felicis, mercatores cives Barchi… | L12 |
| CMD-141-1 | declarant: .NR / to: Durando Guarcia | declarant: Bernardus Guardiola, Petrus Ballistarii, Johannes Guardiola et Micha… | L12 |
| CMD-141-2 | declarant: .NR / to: Jacobo Raserio | declarant: Bernardus Guardiola, Petrus Ballistarii, Johannes Guardiola et Micha… | L13 |
| CMD-147-1 | declarant: .NR / to: Bartholomeo Paschalis | declarant: Johannes Martells, marinerius civis Barchinone / to: Bartholomeo Pas… | L13 |
| CMD-156-1 | declarant: .NR / to: venerabili Johanni de Dous | declarant: Michael Vila Nova, mercator habitator Barchinone / to: venerabili Jo… | L14 |
| CMD-159-1 | declarant: .NR / to: .NR | declarant: Anthonius de Fonte, civis Barchinone / to: Jacobo Ferrarii, mercatori | L15 |
| CMD-165-1 | declarant: .NR / to: Jacobo de Prexana | declarant: Jacobus Gilii, mercator habitator Valencie / to: Jacobo de Prexana | L15 |
| CMD-168-1 | declarant: .NR / to: Galcerando dez Serra Gallarde | declarant: Bartholomeus Arquimbau, mercator civis Barchinone / to: Galcerando d… | L15 |
| CMD-171-1 | declarant: .NR / to: venerabili Petro Tapioles | declarant: Periconus Saragossa, patronus navis, civis Barchinone, et Periconus … | L16 |
| CMD-174-1 | declarant: .NR / to: Bernardo Sent Martí | declarant: Ludovicus Cirvent / to: Bernardo Sent Martí | L16 |
| CMD-177-1 | declarant: .NR / to: Arnaldo Sent Just | declarant: Franciscus Brugal et Franciscus Miró / to: Arnaldo Sent Just | L16 |
| CMD-180-1 | declarant: .NR / to: venerabili Andree de Olivella | declarant: Guillelmus Pujades, botiguerius civis Barchinone / to: venerabili An… | L16 |
| CMD-183-1 | declarant: .NR / to: venerabili Ferrario Berengarii | declarant: Petrus de Olivella [mercator] / to: venerabili Ferrario Berengarii | L17 |
| CMD-189-1 | declarant: .NR / to: dicto Bernardo Fabre | declarant: Petrus Loreta, mercator civis Barchinone / to: dicto Bernardo Fabre | L17 |
| CMD-191-1 | declarant: .NR / to: venerabili domine Ysabeli | declarant: Petrus Toralles, mercator civis Barchinone / to: venerabili domine Y… | L17 |
| CMD-192-1 | declarant: .NR / to: venerabili Bernardo Fabre | declarant: Franciscus Costa, argenterius civis Barchinone / to: venerabili Bern… | L17 |
| CMD-193-1 | declarant: .NR / to: plenam damus et tribuimus potestatem | declarant: 55 investors (named pp. 317-318) / to: .NR | L17/L18 |
| CMD-195-1 | declarant: .NR / to: venerabili Bernardo Fabre | declarant: Petrus Miret, mercator civis Barchinone / to: venerabili Bernardo Fa… | L18 |
| CMD-199-1 | declarant: .NR / to: venerabili Guillelmo Perayerii | declarant: Bertrandus Porta et Johannes Scuderii, mercatores cives Barchinone /… | L18 |
| CMD-204-1 | declarant: .NR / to: Guillelmo de Fonolleto | declarant: Gabriel Cardona, mercator oriundus ville Morelle regni Valencie / to… | L19 |
| CMD-207-1 | declarant: .NR / to: Antonio Ledó | declarant: Petrus Muntsech, magister axie civis Barchinone / to: Antonio Ledó | L19 |
| CMD-213-1 | declarant: .NR / to: Francisco Arbolini | declarant: Miquael Homedes, mercator civis Dertuse / to: Francisco Arbolini | L19 |
| CMD-216-1 | declarant: .NR / to: Raymundo Pujolli | declarant: Petrus Folch, curritor auris civis Barchinone / to: Raymundo Pujolli | L20 |
| CMD-217-1 | declarant: .NR / to: Berengario de Junyent | declarant: Franciscus Riart, mercator civis Barchinone / to: Berengario de Juny… | L20 |
| CMD-219-1 | declarant: .NR / to: Leonardo de Doni | declarant: Franciscus Buada, mercator habitator Barchinone / to: Leonardo de Do… | L20 |
| CMD-221-1 | declarant: Petrus Bertrandi, mercator civis Dertuse / to: a… | declarant: Petrus Bertrandi, mercator civis Dertuse / to: Gabrielem Pujolli et … | L20 |
| CMD-225-1 | declarant: .NR / to: venerabili Johanni Jordà | declarant: Petrus Jacobi de Sancto Johanne, campsor monetarum civis Barchinone … | L20 |
| CMD-226-1 | declarant: Anthonius de Puigdangoles, mercator, et Geraldus… | declarant: Anthonius de Puigdangoles, mercator, et Geraldus Salvatoris, calafat… | L21 |
| CMD-227-1 | declarant: .NR / to: honorabili Guillelmo Martini | declarant: Bonanatus de Carcassona, mercator civis Barchinone / to: honorabili … | L21 |
| CMD-228-1 | declarant: .NR / to: honorabili Bartholomeo Sentjust | declarant: Petrus Arnaldus dez Carner, mercator civis Barchinone / to: honorabi… | L21 |
| CMD-231-1 | declarant: .NR / to: venerabilibus Michael Coscó et Luppo S… | declarant: Andreas Sucre, mercator civis Barchinone / to: venerabilibus Michael… | L21 |
| CMD-234-1 | declarant: .NR / to: venerabili Ludovico Guillelmo del Cast… | declarant: Gispertus dez Carner, mercator civis Barchinone, heir of Petrus Arna… | L21 |
| CMD-237-1 | declarant: .NR / to: honorabili Valentino Gibert | declarant: Franciscus Lobera, mercator habitator Barchinone / to: honorabili Va… | L22 |
| CMD-240-1 | declarant: .NR / to: Anthonio Maruny | declarant: Petrus Palau, flaçaderius civis Barchinone / to: Anthonio Maruny | L22 |
| CMD-243-1 | declarant: .NR / to: Raymundo Vitalis | declarant: Guillelmus Badorch, mercator civis Barchinone / to: Raymundo Vitalis | L22 |
| CMD-246-1 | declarant: .NR / to: venerabili Lehonardo de Corbera | declarant: Johannes de Corbera, mercator civis Barchinone / to: venerabili Leho… | L22 |
| CMD-247-1 | declarant: .NR / to: Anthonio Sadorní | declarant: Franciscus Portella, brodator habitator Barchinone / to: Anthonio Sa… | L22 |
| CMD-249-1 | declarant: .NR / to: honorabili Bernardo Mahull | declarant: Antichus Blanch, mercator civis Barchinone / to: honorabili Bernardo… | L23 |
| CMD-250-1 | declarant: .NR / to: dicto honorabili Bernardo Mahull | declarant: Anthicus Blanch / to: dicto honorabili Bernardo Mahull | L23 |
| CMD-252-1 | declarant: .NR / to: .NR | declarant: Lorenç Belloch, mercer (agent) / to: Anthoni Postomi (investor) | L23 |
| CMD-253-1 | declarant: .NR / to: venerabili Jacobo Bertran | declarant: Petrus Ubach, mercator civis Barchinone / to: venerabili Jacobo Bert… | L23 |
| CMD-045-1 | declarant: Filipus de Bosco, iunior, et Periconus de "Medal… | declarant: Filipus de Bosco, iunior, et Periconus de Medalia / to: Guillelmo de… | L04 |

**Investor counts** (8).

| instance | old | new | source |
|---|---|---|---|
| CMD-174-1 | 2 | 1 | L16 |
| CMD-204-1 | 2 | 1 | L19 |
| CMD-081-1 | 4 | 1 | L07 |
| CMD-097-1 | 5 | 1 | L08 |
| CMD-099-1 | 27 | 1 | L09 |
| CMD-102-1 | 4 | 1 | L09 |
| CMD-226-1 | 1 | 2 | L21 |
| CMD-193-1 | 60 | 55 | L17/L18 |

**Agent counts** (1).

| instance | old | new | source |
|---|---|---|---|
| CMD-226-1 | 2 | 1 | L21 |

**Profit rules** (2).

| instance | old | new | source |
|---|---|---|---|
| CMD-142-1 | .NR | agent-1/4 | L13 |
| CMD-199-1 | .NR | agent-1/4 | L18 |

**Profit-rule quotations** (3).

| instance | old | new | source |
|---|---|---|---|
| CMD-199-1 | .NR | Ad quartum lucri etc. | L18 |
| CMD-048-1 | cioni predictorum pannorum non receptorum et predicte coman… | De lucro vero quod Deus in hac comanda dederit, deducto prius tuo capitali, hab… | L05 |
| CMD-237-1 | In qua comanda unusquisque vestrum habet terciam partem. | Ad quartum lucri. | L22 |

**Loss-rule quotations** (13).

| instance | old | new | source |
|---|---|---|---|
| CMD-174-1 | .NR | Simile comande instrumentum facio ego dictus Ludovicus Cirvent | L16 |
| CMD-174-2 | .NR | Simile comande instrumentum facio ego dictus Ludovicus Cirvent | L16 |
| CMD-217-2 | .NR | facio aliud comande instrumentum vobis dicto Berengario de Junyent | L20 |
| CMD-250-1 | Predicta vero comanda et eius implicamenta eant et sint ad … | Predicta vero comanda et eius implicamenta eant et sint ad usum maris et genciu… | L23 |
| CMD-192-1 | Risicum etc. scriptor Barchinone. | Risicum etc. | L17 |
| CMD-195-1 | Risicum etc. estes Jacobus Ferrarii, mercator civis, Raymun… | Risicum etc. | L18 |
| CMD-204-1 | Risicum etc. mercator oriundus llerde, et Franciscus Erbolí… | Risicum etc. | L19 |
| CMD-213-1 | Et eadem comanda eat, maneat et sit ubique ad risicum. cive… | Et eadem comanda eat, maneat et sit ubique ad risicum. | L19 |
| CMD-228-1 | Et ipsa comanda vestra eat, maneat et sit ad vestri risicum… | Et ipsa comanda vestra eat, maneat et sit ad vestri risicum etc. | L21 |
| CMD-240-1 | Risicum etc. "estes discretus Bernardus Bastat, notarius ci… | Risicum etc. | L22 |
| CMD-246-1 | Intelligatur tamen quod dicta comanda eat, maneat et sit ub… | Intelligatur tamen quod dicta comanda eat, maneat et sit ubique ad vestri risic… | L22 |
| CMD-129-1 | Et ad risicum etc. chinone. | Et ad risicum etc. | L11 |
| CMD-147-1 | Risicum etc. I Barchinone. | Risicum etc. | L13 |

**Peril-clause quotations** (10).

| instance | old | new | source |
|---|---|---|---|
| CMD-250-1 | Predicta vero comanda et eius implicamenta eant et sint ad … | Predicta vero comanda et eius implicamenta eant et sint ad usum maris et genciu… | L23 |
| CMD-192-1 | Risicum etc. scriptor Barchinone. | Risicum etc. | L17 |
| CMD-195-1 | Risicum etc. estes Jacobus Ferrarii, mercator civis, Raymun… | Risicum etc. | L18 |
| CMD-204-1 | Risicum etc. mercator oriundus llerde, et Franciscus Erbolí… | Risicum etc. | L19 |
| CMD-213-1 | Et eadem comanda eat, maneat et sit ubique ad risicum. cive… | Et eadem comanda eat, maneat et sit ubique ad risicum. | L19 |
| CMD-228-1 | Et ipsa comanda vestra eat, maneat et sit ad vestri risicum… | Et ipsa comanda vestra eat, maneat et sit ad vestri risicum etc. | L21 |
| CMD-240-1 | Risicum etc. "estes discretus Bernardus Bastat, notarius ci… | Risicum etc. | L22 |
| CMD-246-1 | Intelligatur tamen quod dicta comanda eat, maneat et sit ub… | Intelligatur tamen quod dicta comanda eat, maneat et sit ubique ad vestri risic… | L22 |
| CMD-129-1 | Et ad risicum etc. chinone. | Et ad risicum etc. | L11 |
| CMD-147-1 | Risicum etc. I Barchinone. | Risicum etc. | L13 |

**Peril clause** (1).

| instance | old | new | source |
|---|---|---|---|
| CMD-207-1 | vestri dicti Petri | ad usum maris et gencium; salvage clause | L19 |

**Security** (1).

| instance | old | new | source |
|---|---|---|---|
| CMD-122-1 | surety (renunciation of principal-first rule) and general e… | general-estate, agents in solidum (renunciation of the benefit of excussion; no… | L11 |

**Act type** (1).

| instance | old | new | source |
|---|---|---|---|
| CMD-226-1 | apocha: agents receipt of returned pepper | apocha: investors' receipt of returned pepper from the agent's heir's tutors | L21 |

**Object** (1).

| instance | old | new | source |
|---|---|---|---|
| CMD-226-1 | .NR | unum pont de pebre, 1,033 Alexandrian rotols | L21 |

**OCR in quotations** (57 fields in `instances`; matching fixes in `instance-chars` quotes). The fixes are 'ete' → 'etc.', 'hee' → 'hec', 'huie' → 'huic', 'hine' → 'hinc', 'hoe' → 'hoc', 'hae' → 'hac', 'Lt pro' → 'Et pro', 'implieatas', 'nobiseum', 'seilicet', 'llerde', 'subseripto', 'de tores' → 'de tares', and the OCR years [1849], [1851] and [1863] → [1349], [1351], [1363]. All of these were carried with `ocr_flag` 'none'. Word-level and listed in full in the CSV.

## Census corrections other than form

| doc | field | new (excerpt) | rule | source |
|---|---|---|---|---|
| 43 | notes | 1280, Mallorca. Translatum. 'ad voluntatem Dei et tui redegum et fortunam'. 1/4. | date | L04 |
| 43 | notes | Date corrected 1270s -> 1280: deed of 10 May 1280 (VI id. Mai.; ".Mo.CCo. octuagesimo"). | date | L04 |
| 66 | notes | 1299, Cyprus. 'Ad quartum denarium de lucro et vestri fortunam'. | date | L06 |
| 66 | notes | Date corrected 1290s -> 1299: heading and manual give 1299. | date | L06 |
| 106 | notes | 1349, Cyprus. Promise to pay to heirs. | date | L10 |
| 106 | notes | Date corrected 1340s -> 1349: the year is 1349. | date | L10 |
| 110 | notes | 1359. 'ad vestri risicum, periculum et fortunam, prout Dominus Deus salvaverit dictum comune meum, ad libram … | date | L10 |
| 110 | notes | Date corrected 1350s -> 1359: deed of 6 September 1359. | date | L10 |
| 126 | notes | 1371, Sicily. 'Et hec comanda vestra sit ad vestrum risicum etc.': bearer stated. | date | L11 |
| 126 | notes | Date corrected 1370s -> 1371: editors' 25 September 1371 (fol. 38, with doc. 125). | date | L11 |
| 142 | notes | 1379. 'ad usum maris et gencium et ad vestri et vestrorum resicum, periculum et fortunam'. Investor a widow. | date | L13 |
| 142 | notes | Date corrected 1370s -> 1379: deed of 30 July 1379. | date | L13 |
| 222 | notes | 1434. 'ad vestri risicum, periculum et fortunam'. 1/4. | date | L20 |
| 222 | notes | Date corrected 1430s -> 1434: dated deed of 8 June 1434. | date | L20 |
| 235 | notes | 1456. Catalan. One agent is one of the four contributors; agents may insure goods and exchanges ('fase asegur… | date | L21 |
| 235 | notes | Date corrected 1450s -> 1456: Saturday 4 September 1456 (computed weekday agrees). | date | L21 |
| 251 | notes | 1489, Castile/Portugal. 'ad vestri risicum, periculum et fortunam ... per solidum et libram'. Catalan letter … | date | L23 |
| 251 | notes | Date corrected 1488 -> 1489: 10 December 1489, before the 25 December change of the Nativity year. | date | L23 |
| 178 | notes | D-ABBR: abbreviated risk clause read as Bernat Nadal's house formula, written out with the investor as bearer… | date | L16 |
| 255 | notes | undated; 2nd half 14th c. (editors, by party and hand) Catalan. Goods held 'en sa comanda' for carriage; carr… | date | L23 |
| 255 | notes | Date corrected '15th c.' -> editors' dating: heading 'mediados del siglo XIV'; study p. 105, 2nd half of the … | date | L23 |
| 238 | acts_in_entry | 2 | acts | L22 |
| 248 | acts_in_entry | 2 | acts | L23 |
| 248 | notes | acts_in_entry 1 -> 2: [1] is a jointly owned lot, the agent a third-owner, no loss term ('neither' on its own… | acts | L23 |
| 226 | act_type | apocha: investors' receipt of pepper from the agent's heir's tutors | parties | L21 |
| 226 | notes | Roles reversed in the 10-27 act_type (which followed the regest): the declarants had made two comandas to the… | parties | L21 |
| 220 | act_type | chapters of a companyia in the clothes-dealers' (peller) trade: investor's 400 l. held 'en pura comanda' at h… | gloss | L24 |
| 220 | notes | 'furriers' -> 'clothes-dealers' (peller), per the Glosario. | gloss | L24 |
| 171 | notes | D-ABBR: abbreviated risk clause read as Bernat Nadal's house formula, written out with the investor as bearer… | parties | L16 |
| 171 | notes | The consenting Franciscus is Francesc de Niubo, the father of the minor Perico de Niubo, not Francesc ca Rovi… | parties | L16 |
| 193 | notes | 1415. Fifty-five investors by count on pp. 317-318 (some with a procurator), permit the return to be sent via… | parties | L17/L18 |
| 193 | notes | 'Some twenty' undercounts (55 names, L17 count); 'several minors' misreads 'minor diebus' (the younger), pair… | parties | L17/L18 |
| 122 | act_type | comanda (two agents) | security | L11 |
| 122 | notes | No surety: the clause is the co-obligors' renunciation of the benefit of excussion (doc. 121 has it word for … | security | L11 |
| 191 | act_type | comanda in exchanges, agent answers for placing the money safe on land, investor the credit of the takers | loss | L17 |
| 191 | notes | 'agent bears the sea' removed: there is no sea in the deed; 'salve et secure in terra' is the agent's underta… | loss | L17 |
| 235 | notes | Agents take 1/4 of the net profit; the insurance clause ('fase asegurar') is a power of the agents. Recommend… | profit | L21 |
| 140 | notes | Five acts in the manual; the editors print three (two left out for faded ink: Francesc de Pedralbes after [2]… | acts | L12 |
| 149 | notes | The agent also executes an antipoca for the same 300 lb (a second instrument, not counted). | acts | L13 |
| 19 | notes | The flag 'Second act in entry: check' is answered by the image: one act (two investors, Fonts and Homo Dei). | acts | L02 |
| 207 | notes | D-207: stays neither (an errand to buy a slave for the investor, no profit allocation; D-ERRAND). The risk cl… | D-207 | L19 |
| 218 | notes | D-ERRAND: a trading comanda with all profit to the investor stays comanda. The profit rule is not otherwise r… | D-ERRAND | L20 |
| 233 | notes | D-ERRAND: a trading comanda without profit to the agent is comanda. | D-ERRAND | L22 |
| 214 | notes | Remuneration is a commission ('2 % + 2 %', entrada and exida), not a profit share. | profit | L19 |
| 75 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 76 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 77 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 78 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 79 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 80 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 81 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 84 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 85 | notes | Open theory call, not ruled: Pere de Torre's 'ad quartum lucri et usum maris' read as loss by custom only; no… | open | L07 |
| 207 | act_type | comanda to buy a slave (cancelled) (purchase errand: one female slave; no profit allocation; D105 rule) | D-207 | L19 |

## Recorded, not applied

The following corrections are recorded here but not applied:

- **Acts [2]–[n] of the collapsed entries.** These are 99 (26 acts), 102 (3), 81 (3) and 97 (4). Instancing them is a coding task, not a correction.
- **`.NR` dates in the early deeds.** Docs 1–66 carry the date in the eschatocol, not a head line, and are left `.NR`. Head-line dates were filled wherever the 2026-10-27 file had `.NR`.
- **Missing parties.** `CMD-186-1` (a Catalan protest), `CMD-201-1` and `CMD-220-1` (Catalan chapters) still lack parties; `CMD-220-1` also lacks a date. `CMD-255-1` parties stay `.NR`.
- **`CMD-154-1` `profit_rule_quote`.** It stays `.NR`; the rule is recorded in `profit_rule`.
- **Unrecorded clauses** listed in the L-chunks are not added as data. They include cancellations and their dates, licences, papal absolutions, insurance costs (docs 224, 250, 251), commission remuneration (214, 238), price ceilings and inter-agent rules. They are the material of a later pass.
- **Doc 193.** The investor count of 55 is the L17 count from the page images; the 2026-10-27 file had 60. Recount once more before any cell relies on it.
- **Torre's "usum maris" acts (75–85).** These are not ruled; see the RULINGS file.
