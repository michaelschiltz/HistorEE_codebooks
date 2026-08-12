# Scoped view — component `risk-pooling`

Mechanism filter: `MC1 = None`. **32 forms × 9 characteristics.** This is NOT the full characteristic set: comparative claims run on a declared component set only (`CHARACTER-CODING.md`). At this *n* the matrix is a coverage map, not evidence.

## Matrix

| form | `CN1` | `HZ1` | `HZ2` | `MB3` | `MC1` | `PR1` | `PY0` | `PY1` | `PY2` |
|---|---|---|---|---|---|---|---|---|---|
| `averia_pool` | 0 | 1 | 1 | 1 | 2 | 0 | 0 | .NA | .NA |
| `bottomry` | -- | -- | -- | -- | 0 | 1 | -- | -- | -- |
| `craft_pension_edinburgh` | 0 | .NR | -- | 1 | 2 | 0 | 1 | 3 | 4 |
| `craft_widows_fund_edinburgh` | 0 | .NR | -- | 0 | 2 | P | 1 | 1 | .NR |
| `friendly_society_england` | 0 | .NR | P | 0 | 2 | 0 | 1 | 0 | 3 |
| `friendly_society_female_england` | 0 | .NR | P | 0 | 2 | P | 1 | 0 | 3 |
| `general_average` | 2 | 2 | P | 1 | 2 | 0 | 1 | 0 | 3 |
| `guild_box_brabant` | 0 | .NR | -- | 1 | 2 | 0 | 1 | 0 | 3 |
| `guild_box_dutch` | 0 | 2 | P | 1 | 2 | 0 | 1 | 0 | 3 |
| `guild_relief_england` | .NR | .NR | -- | 0 | 2 | 0 | 1 | 3 | 4 |
| `ko_daikokuya_1848` | 0 | .NR | -- | 1 | .NR | 0 | .NR | -- | -- |
| `ko_daimanin_1828` | -- | -- | -- | -- | 2 | -- | -- | -- | .NR |
| `ko_hokinosawa_1820` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | 0 |
| `ko_hokoin_1832` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | .NR |
| `ko_mitarai_gin_1805` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | .NR |
| `ko_mitarai_mujin_1773` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | 0 |
| `ko_mochiyori_yutsu_1876` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | 2 |
| `ko_shijunin_1829` | 0 | -- | -- | -- | 2 | -- | -- | -- | 0 |
| `ko_usui_bango_1822` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | .NR |
| `ko_yamakuni_1555` | 0 | .NR | -- | .NR | 2 | 0 | 2 | 2 | .NR |
| `life_annuity_priced` | -- | -- | -- | -- | 1 | 1 | .NA | -- | -- |
| `marine_insurance` | -- | -- | -- | -- | 1 | 1 | -- | -- | -- |
| `particular_average` | .NA | .NR | -- | .NA | .NR | 0 | .NA | .NA | .NA |
| `respondentia` | -- | -- | -- | -- | 0 | 1 | -- | -- | -- |
| `sea_loan` | -- | -- | -- | 0 | 0 | P | .NA | -- | -- |
| `shenhui_gu_alloc` | 1 | .NR | -- | 0 | .NR | 0 | 0 | .NA | .NA |
| `tontine` | -- | -- | -- | -- | 2 | .NR | -- | -- | -- |
| `tontine_en_1693` | 1 | 0 | -- | 0 | 2 | 0 | 2 | 1 | .NR |
| `tontine_fr_royal` | -- | 0 | -- | 0 | 2 | P | 2 | -- | -- |
| `torinoke_mujin` | 0 | .NR | -- | 0 | 2 | 0 | 2 | 2 | 0 |
| `warichi_iwade` | .NA | .NR | .NR | 1 | .NR | 0 | 2 | 2 | 0 |
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
| `bottomry` | 1 | -- |
| `craft_pension_edinburgh` | 0 | individual-indemnity |
| `craft_widows_fund_edinburgh` | P | individual-indemnity |
| `friendly_society_england` | 0 | individual-indemnity |
| `friendly_society_female_england` | P | individual-indemnity |
| `general_average` | 0 | individual-indemnity |
| `guild_box_brabant` | 0 | individual-indemnity |
| `guild_box_dutch` | 0 | individual-indemnity |
| `guild_relief_england` | 0 | individual-indemnity |
| `ko_daikokuya_1848` | 0 | .NR |
| `ko_daimanin_1828` | -- | -- |
| `ko_hokinosawa_1820` | 0 | individual-draw |
| `ko_hokoin_1832` | 0 | individual-draw |
| `ko_mitarai_gin_1805` | 0 | individual-draw |
| `ko_mitarai_mujin_1773` | 0 | individual-draw |
| `ko_mochiyori_yutsu_1876` | 0 | individual-draw |
| `ko_shijunin_1829` | -- | -- |
| `ko_usui_bango_1822` | 0 | individual-draw |
| `ko_yamakuni_1555` | 0 | individual-draw |
| `life_annuity_priced` | 1 | .NA |
| `marine_insurance` | 1 | -- |
| `particular_average` | 0 | .NA |
| `respondentia` | 1 | -- |
| `sea_loan` | P | .NA |
| `shenhui_gu_alloc` | 0 | collective-good |
| `tontine` | .NR | -- |
| `tontine_en_1693` | 0 | individual-draw |
| `tontine_fr_royal` | P | individual-draw |
| `torinoke_mujin` | 0 | individual-draw |
| `warichi_iwade` | 0 | individual-draw |
| `widows_fund_scotland` | 1 | individual-indemnity |

## Forms

- `averia_pool` — Avería (compulsory convoy levy) · Spanish / Carrera de Indias · 1521-1681
- `bottomry` — Bottomry (sea loan secured on the ship) · Mediterranean / Latin West · 12c onward
- `craft_pension_edinburgh` — Craft pensions and supply, incorporation of Mary's Chapel · Scottish / Edinburgh · 1670-1768
- `craft_widows_fund_edinburgh` — Widows' fund annuity scheme, incorporation of Mary's Chapel · Scottish / Edinburgh · 1768-
- `friendly_society_england` — Friendly society / box club · English · 1870-1914 (this coding)
- `friendly_society_female_england` — Female friendly society · English · 1780-1830 (this coding)
- `general_average` — General average (jettison contribution) · Mediterranean / lex Rhodia · antiquity onward
- `guild_box_brabant` — Ambachtsbus / armenbus — craft guild sickness box · Low Countries / Brabant · 1250-1600
- `guild_box_dutch` — Gildebus — guild sickness, burial, old-age and widows fund · Dutch Republic · 1550-1800
- `guild_relief_england` — English religious gild relief · English · c.1350-1400
- `ko_daikokuya_1848` — 大黒屋善兵衛頼母子講 (a 領主的金融講 / 藩営頼母子, Iino domain) · Japanese / Settsu · 1848-1853
- `ko_daimanin_1828` — 大満院講 (広域講) · Japanese / Kawachi · 1828-1833+
- `ko_hokinosawa_1820` — 久左衛門始頼母子 (朴木沢新田, 中里村) · Japanese / Echigo · 1820-1838
- `ko_hokoin_1832` — 宝光院加入頼母子講 (the kō joined by Hōkō-in) · Japanese / Dewa-Yamagata · 1832-
- `ko_mitarai_gin_1805` — 「銀頼母子」(御手洗町) · Japanese / Aki · 1805-
- `ko_mitarai_mujin_1773` — 「無尽」(御手洗町, 竹原屋平三郎 宅で鬮取り) · Japanese / Aki · 1773-1785
- `ko_mochiyori_yutsu_1876` — 持寄融通社 (Mochiyori Yūtsū-sha) · Japanese / Kawachi-Settsu · 1876-1884
- `ko_shijunin_1829` — 四拾人講 (広域講) · Japanese / Kawachi · 1829-1843
- `ko_usui_bango_1822` — 碓井村伴吾講 (広域講) · Japanese / Kawachi · 1822-
- `ko_yamakuni_1555` — 二石頼母子 (丹波国山国庄, 親 井ノ本左近) · Japanese / Tanba · 1555-1563
- `life_annuity_priced` — Life annuity priced on a tabulated survival function · Dutch / English · 1671 onward
- `marine_insurance` — Premium-based marine insurance · Italian city-states · c.1300 onward
- `particular_average` — Particular average (avaria particolare) — accidental damage borne by its owner · Mediterranean / lex Rhodia and successors · antiquity onward
- `respondentia` — Respondentia (sea loan secured on the goods) · Mediterranean / Latin West · 12c onward
- `sea_loan` — Sea loan (foenus nauticum / nautikòn dáneion) · Greco-Roman / Mediterranean · 2nd millennium BCE onward
- `shenhui_gu_alloc` — 神會股 (corporate deity association — pooling aspect) · Chinese / Shanyin, Shanxi · mid-19c
- `tontine` — Tontine · European · 17c onward
- `tontine_en_1693` — Tontine — English (Million Act 5 & 6 Will. & Mar. c. 5) · English · 1693-1789
- `tontine_fr_royal` — Tontine — French royal series (fourteen age classes) · French · 1689-1759
- `torinoke_mujin` — 取退き無尽 (winner released from further contribution) · Japanese · 17c-1930s
- `warichi_iwade` — 割地 (warichi) — periodic reallocation of arable, Iwade village · Japanese / Echigo · 17c-1870s
- `widows_fund_scotland` — Scottish Ministers' Widows' Fund · Scottish · 1744 onward
