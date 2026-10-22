# Rulings: `RD-test` blind batch, 2026-10-22

Three rulings by MS on 2026-10-22, on the questions raised in `records/NOTES-residual-default-coding-2026-10-22.md` (answers 4–6). The test table as coded is `records/TEST-residual-default-2026-10-22.csv` and is not altered; the table with these rulings applied is `records/TEST-residual-default-adjudicated-2026-10-22.csv`. The census cells they move are entered in `datasets/loss_mitigation_forms/recodings.csv` as `LM-R0076`–`LM-R0079`, pass `residual-default-rulings-2026-10-22`, `adjudication = pending`; `data.csv` is unchanged until MS adjudicates them.

The rulings were argued by the coding assistant (`claude-opus-5-5`, `high`) and agreed by MS. Ruling 2 was agreed first on a ground the assistant then found to contradict the census (below), and was re-agreed on the corrected ground before anything was written.

## Ruling 1. `CN3`: a required bond or pledge with no stated consequence of default is `1`

A rule that requires the drawer to give a bond, a pledge or sureties for his repayment is `CN3 = 1`, at `medium` where no consequence of non-payment is stated in words and `high` where it is. The rule creates the instrument of compulsion; it need not restate the procedure by which the instrument is enforced.

**Grounds.** (i) The house rule as it stood was incoherent: `ko_mitarai_mujin_1773` read one pledge clause as exposure (`LS3 = 1`, LM-0258) and as no compulsion (`CN3 = .NR`, LM-0251). One instrument cannot do the first and not the second. (ii) Within the seventeen rulebooks, eight treat suit on the bond, sale of the pledge or calling the guarantors as the ordinary next step (第十四, 二十一, 二十五, 三十一, 三十三, 三十五, 三十七, 四十三講), and none suggests a bond was unenforceable; so the inference from a required bond to enforceability rests on the instruments' own usage, not on law supplied from outside. That usage comes from one editor's selection and is weighed as such. (iii) This is not `RD-test` rule 6 by another route: rule 6 forbids coding what the law would supply when the rules are silent; here the rules are not silent, they create the instrument.

**Not ruled.** Whether forfeiture of the draw alone is `1` or `P`: the census already holds both (`guild_box_brabant CN3 = 1` on forfeiture of entitlement; `ko_usui_bango_1822 CN3 = P` on forfeiture of the draw). Recorded, not resolved.

**Moves.** Test table: 第十八講 and 第二十七講 `.NR` → `1` (medium); 第七講 and 第十二講 stay `1`. Census: LM-0251 `ko_mitarai_mujin_1773 CN3` `.NR` → `1` (LM-R0076).

## Ruling 2. `LS3` for kō: two routes to `1`; a drawer's own pledge or surety alone is `.NR`

For a kō, `LS3 = 1` by either of two routes:

- **Association route.** A member answers for obligations that are not his own: guarantees he must give for other members' draws, クビリ advances, inheritance of an expelled member's share, a shortfall he must bear. Census precedents: `guild_box_dutch LS3 = P` (contributions raised on continuing members), the `avariz_fund` note (collective answerability).
- **Debtor route.** A drawer is expressly liable beyond his pledge, with his person or his whole estate. Census precedents: `sea_loan LS3 = 1` ('Der Schuldner haftete stets unbeschraenkt mit seinem gesamten Vermoegen'), `bodemerij_amsterdam LS3 = 1` ('zijn persoon ende alle sijne goederen'), against `bottomry LS3 = 0` (liability confined to the pledge).

A pledge or surety alone, securing the drawer's own agreed repayment, is `.NR` on the general question — not `1`, because it does not enlarge his obligation, and not `0`, because nothing confines his liability to the pledge (the `bodemerij_amsterdam` note: contracts naming only the special pledge are '.NR on the general question and NOT 0').

**Grounds.** (i) Under the previous house reading `LS3 = 1` in all seventeen kō, wherever `RB3` was substantive: the mapping was a function and `LS3` added nothing (test 4), while both sit in the owner-shielding component, so a WP1 comparison counted the drawer's security twice. (ii) The definition ('beyond what he has contributed or agreed to contribute') excludes the drawer's own agreed repayments. (iii) Under this ruling `LS3` separates kō on the evidence: 8 at `1` (第七, 十四, 十五, 二十三, 二十五, 二十七, 三十三, 三十九講), 9 at `.NR`.

**Correction recorded.** As first argued and agreed, ruling 2 said that only liability for others' obligations counts. That contradicts `sea_loan LS3 = 1`, where the debtor's own unlimited liability is the coded fact, and the vocabulary's note that `LS3` is exact for the sea-loan family. The debtor route restores consistency. On the seventeen the outcome is the same, because no kō rulebook binds the drawer's person or whole estate in words; on the census it is not (see `ko_yamakuni_1555` below).

**Moves.** Test table: `LS3` `1` → `.NR` at 第六, 十二, 十八, 二十一, 二十六, 三十一, 三十五, 三十七, 四十三講. Census: LM-0258 `ko_mitarai_mujin_1773`, LM-0733 `ko_mitarai_hanei_1840`, LM-0276 `ko_mitarai_gin_1805`, each `1` → `.NR` (LM-R0077–LM-R0079).

**Not moved.** LM-0238 `ko_yamakuni_1555 LS3 = 1`: no pledge is recorded, and members' default reached 先祖相伝の地 sold to the 衆中, which is recourse against their own estates — the debtor route can hold it. Left at `1`; not recoded on this ruling. LM-0276 would move back to `1` on the association route if 加藤 1998, 147 shows that the 請合人 had to be members of the 連中.

## Ruling 3. `RD-test = deferred` only on a clause about default itself

A general amendment clause, or a clause putting 必要ノ事項 to the members, is not `deferred`. Only a clause that refers default to the members' decision can be.

**Grounds.** Counting general clauses would put `deferred` on roughly seven of the seventeen (第六, 十五, 二十三, 二十六, 三十五, 三十七, 四十三講), nearly all `GV1 = collective`: `RD-test` would record "has an amendment clause", which `GV1` already holds.

**Moves.** Test table: 第六講 and 第十五講 stay `.NR`. 第二十六講 stays `deferred` but drops from medium to low: 第十一 臨時會ヲ開キ協議ノ上決定スル says the meeting decides about the non-performer; that it decides who bears the residue is an added reading.

**Recorded, not repaired.** `deferred` names who decides the bearer, not a bearer. It is a governance fact in a loss-sharing column, and on test 1 (`CHARACTER-CODING.md`) `RD-test` asks two questions; 第二十六講 is the only cell in the set where they come apart. Per the rule against proposing a repair in the batch that motivates it, no change is proposed here. Likewise `RB3 = mixed` carrying four mixtures (several kinds of property; property and surety together; property or surety at the drawer's option; surety for one drawer and property for the others) is recorded in the coding notes and not repaired.

## The test table after the rulings

| characteristic | as coded                                     | after rulings                                |
|----------------|----------------------------------------------|----------------------------------------------|
| `RD-test`      | `.NR` 12; five values once each              | unchanged; 第二十六講 confidence low         |
| `RB3`          | `mixed` 9, `surety` 7, `real-estate` 1       | unchanged                                    |
| `LS1`          | `.NR` 16, `residual-on-fund` 1               | unchanged                                    |
| `LS3`          | `1` 17                                       | `1` 8, `.NR` 9                               |
| `CN3`          | `1` 15, `.NR` 2                              | `1` 17                                       |
| `GV1`          | `collective` 8, `.NR` 8, `external-adm.` 1   | unchanged                                    |

`CN3` now has no variance on the seventeen. That is a result about written kō rules of the 1930s — every rulebook binds the drawer by an instrument — and not a defect of the characteristic; its variance in the census comes from forms with no instrument (`ko_hokinosawa_1820`, `ko_kosaburo_1802`) and from forfeiture-only forms.
