# Scoped view — component `risk-pooling`

Mechanism filter: `MC1 = pooling`. **12 forms × 9 characteristics.** This is NOT the full characteristic set: comparative claims run on a declared component set only (`CHARACTER-CODING.md`). At this *n* the matrix is a coverage map, not evidence.

## Matrix

| form | `CN1` | `HZ1` | `HZ2` | `MB3` | `MC1` | `PR1` | `PY0` | `PY1` | `PY2` |
|---|---|---|---|---|---|---|---|---|---|
| `averia_pool` | 0 | 1 | 1 | 1 | 2 | 0 | 0 | .NA | .NA |
| `general_average` | 2 | 2 | P | 1 | 2 | 0 | 1 | 0 | 3 |
| `ko_daimanin_1828` | -- | -- | -- | -- | 2 | -- | -- | -- | .NR |
| `ko_hokoin_1832` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | .NR |
| `ko_mochiyori_yutsu_1876` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | 2 |
| `ko_shijunin_1829` | 0 | -- | -- | -- | 2 | -- | -- | -- | 0 |
| `ko_usui_bango_1822` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | .NR |
| `tontine` | -- | -- | -- | -- | 2 | .NR | -- | -- | -- |
| `tontine_en_1693` | 1 | 0 | -- | 0 | 2 | 0 | 2 | 1 | .NR |
| `tontine_fr_royal` | -- | 0 | -- | 0 | 2 | 1 | 2 | -- | -- |
| `torinoke_mujin` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | 0 |
| `widows_fund_scotland` | -- | 0 | -- | 1 | 2 | 1 | 1 | 1 | -- |

**Missingness.** `--` no row entered · `.NR` not recorded in the source · `.IL` illegible · `.NA` inapplicable · `0` an observed absence. These are five different epistemic states and are never collapsed.

## Character states

- **`CN1` contribution timing** (nominal) — `0` = ex-ante-periodic; `1` = ex-ante-lump; `2` = ex-post-assessment
- **`HZ1` hazard correlation** (nominal) — `0` = idiosyncratic; `1` = covariate; `2` = mixed
- **`HZ2` hazard responsiveness** (ternary) — ternary: `1` present, `P` partial, `0` absent
- **`MB3` participation basis** (nominal) — `0` = voluntary; `1` = compulsory
- **`MC1` mitigation mechanism** (nominal) — `0` = allocation; `1` = spreading; `2` = pooling
- **`PR1` peril priced ex ante** (ternary) — ternary: `1` present, `P` partial, `0` absent
- **`PY0` pool output** (nominal) — `0` = collective-good; `1` = individual-indemnity; `2` = individual-draw
- **`PY1` payout trigger** (nominal) — `0` = realised-loss; `1` = life-event; `2` = rotation; `3` = need-assessed
- **`PY2` allocation rule** (nominal) — `0` = rotation-lot; `1` = rotation-fixed; `2` = auction; `3` = indemnity; `4` = need-assessed

## The claim

| form | `PR1` peril priced ex ante | `PY0` pool output |
|---|---|---|
| `averia_pool` | 0 | collective-good |
| `general_average` | 0 | individual-indemnity |
| `ko_daimanin_1828` | -- | -- |
| `ko_hokoin_1832` | 0 | individual-draw |
| `ko_mochiyori_yutsu_1876` | 0 | individual-draw |
| `ko_shijunin_1829` | -- | -- |
| `ko_usui_bango_1822` | 0 | individual-draw |
| `tontine` | .NR | -- |
| `tontine_en_1693` | 0 | individual-draw |
| `tontine_fr_royal` | 1 | individual-draw |
| `torinoke_mujin` | 0 | individual-draw |
| `widows_fund_scotland` | 1 | individual-indemnity |

## Forms

- `averia_pool` — Avería (compulsory convoy levy) · Spanish / Carrera de Indias · 1521-1681
- `general_average` — General average (jettison contribution) · Mediterranean / lex Rhodia · antiquity onward
- `ko_daimanin_1828` — 大満院講 (広域講) · Japanese / Kawachi · 1828-1833+
- `ko_hokoin_1832` — 宝光院加入頼母子講 (the kō joined by Hōkō-in) · Japanese / Dewa-Yamagata · 1832-
- `ko_mochiyori_yutsu_1876` — 持寄融通社 (Mochiyori Yūtsū-sha) · Japanese / Kawachi-Settsu · 1876-1884
- `ko_shijunin_1829` — 四拾人講 (広域講) · Japanese / Kawachi · 1829-1843
- `ko_usui_bango_1822` — 碓井村伴吾講 (広域講) · Japanese / Kawachi · 1822-
- `tontine` — Tontine · European · 17c onward
- `tontine_en_1693` — Tontine — English (Million Act 5 & 6 Will. & Mar. c. 5) · English · 1693-1789
- `tontine_fr_royal` — Tontine — French royal series (fourteen age classes) · French · 1689-1759
- `torinoke_mujin` — 取退き無尽 (winner released from further contribution) · Japanese · 17c-1930s
- `widows_fund_scotland` — Scottish Ministers' Widows' Fund · Scottish · 1744 onward
