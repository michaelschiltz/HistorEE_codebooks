# Scoped view — component `risk-pooling`

No mechanism filter (this dataset has no mechanism characteristic). **33 forms × 2 characteristics.** This is NOT the full characteristic set: comparative claims run on a declared component set only (`CHARACTER-CODING.md`). At this *n* the matrix is a coverage map, not evidence.

## Matrix

| form                         | `LR4` | `LR5` |
|------------------------------|-------|-------|
| `asiento_averia`             | 1     | 1     |
| `avariz_vakfi`               | 0     | .NA   |
| `bazacle_mill`               | 0     | .NA   |
| `begijnhof`                  | 1     | 0     |
| `bruderschaft_salzburg`      | 1     | 0     |
| `casa_san_giorgio`           | 0     | .NA   |
| `commenda`                   | 0     | .NA   |
| `compagnia`                  | .NR   | .NR   |
| `compagnie_antwerpen_1582`   | .NR   | .NR   |
| `compagnie_antwerpen_1608`   | .NR   | .NR   |
| `deed_of_settlement_company` | .NR   | .NR   |
| `fraterna`                   | .NR   | .NR   |
| `hegu_shengu`                | --    | --    |
| `hegu_yingu`                 | --    | --    |
| `isqa`                       | 0     | .NA   |
| `joint_stock`                | --    | --    |
| `kabu_edo_export`            | --    | --    |
| `kabu_local`                 | --    | --    |
| `maona_chios`                | 0     | .NA   |
| `maona_corsica`              | 0     | .NA   |
| `nacion_cofradia`            | --    | --    |
| `nakai_fictive_household`    | 1     | 0     |
| `natie`                      | --    | --    |
| `ortoq_equity`               | 0     | .NA   |
| `ortoq_loan`                 | 0     | .NA   |
| `partenrederij`              | 0     | .NA   |
| `qirad`                      | 0     | .NA   |
| `shenhui_gu`                 | --    | --    |
| `societas_maris`             | 0     | .NA   |
| `voc_1602`                   | 0     | .NA   |
| `voc_1612`                   | 0     | .NA   |
| `voc_1623`                   | 0     | .NA   |
| `waqf_khayri`                | 0     | .NA   |

**Missingness.** `--` no row entered · `.NR` not recorded in the source · `.IL` illegible · `.NA` inapplicable · `0` an observed absence. These are five different epistemic states and are never collapsed.

## Character states

- **`LR4` risk pooling** (ternary) — ternary: `1` present, `P` partial, `0` absent
- **`LR5` pooling correlation** (nominal) — `0` = diversifying; `1` = synchronising; `2` = na

## Forms

- `asiento_averia` — Asiento de avería company · Spanish · 17c
- `avariz_vakfi` — Avarız akçesi vakfı (mahalle/köy extraordinary-levy endowment) · Ottoman · 17c-19c; coded 1618-1867
- `bazacle_mill` — Bazacle milling company (pariage) · Occitan / Toulouse · 12c-1946
- `begijnhof` — Begijnhof / court beguinage (curtis beguinarum) · Low Countries (Southern Netherlands; also Lille, Valenciennes, Breda, Amsterdam) · 13c-19c; entity-level cells evidenced post-1585
- `bruderschaft_salzburg` — Bruderschaft / Liebesbund (post-Tridentine Salzburg 'Fraternität') · Latin Christendom / German-speaking (Salzburg) · 1600-1950
- `casa_san_giorgio` — Casa di San Giorgio (Genoa) · Genoese · 1407-1805
- `commenda` — Commenda · Italian (Latin) · 10-13c
- `compagnia` — Compagnia · Tuscan (Florentine) · 13-15c
- `compagnie_antwerpen_1582` — Antwerp general commercial partnership (societas generalis / compagnie), Costuymen Impressae phase · Low Countries (Antwerp, duchy of Brabant) · 1582-1608 as enacted law, on evidence reaching back to c.1540; the Impressae remained the operative compilation in Antwerp after 1608, so the phase boundary is TEXTUAL rather than practical
- `compagnie_antwerpen_1608` — Antwerp general commercial partnership (societas generalis / compagnie), Costuymen Compilatae phase · Low Countries (Antwerp, duchy of Brabant) · 1608-c.1700 as enacted text; NEVER DISPLACED THE 1582 IMPRESSAE IN PRACTICE, which is why FP4 is P and not 1
- `deed_of_settlement_company` — Deed of settlement company (English unincorporated joint-stock company) · English (common law and equity) · c.1720-1844 (Bubble Act 1720 to the Joint Stock Companies Act 1844); ALL CODED CELLS REST ON 1790-1827 EVIDENCE
- `fraterna` — Fraterna · Venetian · 12-15c
- `hegu_shengu` — 身股 — body share (labour share, non-inheritable) · Chinese · 18c-20c
- `hegu_yingu` — 合股 — silver share 銀股 (capital share in a Chinese partnership) · Chinese · 16c-1949
- `isqa` — ʿIsqa · Jewish (Babylonian rabbinic) · 4c onward
- `joint_stock` — Joint-stock corporation · European · 17c onward
- `kabu_edo_export` — 株 — Edo export share (sake shipped to the Edo market) · Japanese · 17c-19c
- `kabu_local` — 株 — local-market share (kabu nakama stock society) · Japanese · 1660-1841
- `maona_chios` — Maona di Chio (New Maona) · Genoese · 1362-1566
- `maona_corsica` — Maona di Corsica · Genoese · 1378-1407
- `nacion_cofradia` — Nación (cofradía) · Spanish (Habsburg) · 16-18c
- `nakai_fictive_household` — Fictive household entity (Nakai Genzaemon) · Japanese / Tokugawa · 1749-1868
- `natie` — Antwerp natie · Low Countries · 15c onward
- `ortoq_equity` — Ortoq — equity regime (capital entrusted) · Mongol / Inner Asian · 13c (not periodised)
- `ortoq_loan` — Ortoq — loan regime (capital advanced at interest) · Mongol / Yuan and Il-khanid · 13c-14c, prevalent from late 13c
- `partenrederij` — Partenrederij / Partenreederei (fractional ship co-ownership) · Low Countries (Holland); the term reder migrated into German · 15c onward; coded on Hollandic law c.1619-1625
- `qirad` — Qirad · Islamic (Maliki) · 7c onward
- `shenhui_gu` — 神會股 — share in a corporate deity association · Chinese / Shanyin, Shanxi · mid-19c
- `societas_maris` — Societas maris (the bilateral commenda; Venetian collegantia) · Venetian / Genoese · c.1073-early 13c (Venice); 1154-13c (Genoa)
- `voc_1602` — VOC (first charter form) · Dutch · 1602-1611
- `voc_1612` — VOC (permanent capital) · Dutch · 1612-1622
- `voc_1623` — VOC (mature chartered form) · Dutch · 1623-1799
- `waqf_khayri` — Waqf (charitable) · Islamic · 8c onward
