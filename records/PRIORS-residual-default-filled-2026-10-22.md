# Priors: `RD-test` and five other characteristics on seventeen kō rulebooks

Filled 2026-10-22 (Asia/Tokyo) by `claude-opus-5-5`, before any page of the source was opened. Read before writing: `README.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CHARACTER-CODING.md`, `EDITING-CSV.md`, `RD-TEST-DEFINITION.md`, `FRAMES.md`, the vocabulary entries for `RB3`, `LS1`, `LS3`, `CN3`, `GV1`, and the notes of all 56 existing `ko_*` rows on those five characteristics in `data.csv`. No NDL page, no other website, no memory tool, no past chat, no connector.

## 1. Exposure

**Tanomoshi-kō / mujin in the 1920s–30s.** General textbook knowledge only. Rural kō were still widespread, especially in western Japan and the Tōhoku; the commonest 1930s pattern I expect is a fixed round of meetings, the pot taken by lot or by bid (入札), and a drawn member (取得者 / 落札者) obliged to keep paying an enhanced instalment (掛戻し) secured by one or two guarantors (保證人, often 連帶保證人) and, for larger pots, a mortgage (抵當) on land. I expect officers called 講元, 親, 發起人, 世話人 or 幹事, and penalty interest (延滯利息) for late payment. I have a general impression, not tied to any source I can name, that a 親 or 發起人 sometimes stood as guarantor of last resort, and that elsewhere the loss fell on the members not yet drawn. I hold that impression weakly and it may be wrong.

**This volume.** Nothing specific. I know that the 農林省 經濟更生部 existed from 1932 in connection with the 農山漁村經濟更生運動 and published survey material on rural credit, and that is all. I do not know the contents of 『農村金融資料 第4號』, its 凡例, its selection principle, or anything about any of the seventeen kō.

**Regulation.** The 1915 無盡業法 licensed mujin conducted as a business (營業) and left non-commercial, member-run kō largely outside it; my recollection is that a 1931 revision tightened the requirements on mujin companies. I believe some prefectures had 頼母子講 取締規則 or similar ordinances, but I cannot name one or date one, and I have nothing specific for 山口, 福岡, 靜岡 or 秋田. Treat all of this as unverified.

## 2. Expectations by characteristic, over the seventeen

- `RD-test`: `.NR` in about 11; `officers` in about 2–3; `all-members` in about 2; `deferred` in about 1; `standing-subgroup` 0–1; `fund` 0–1; `.NA` 0–1 (a purpose kō with no payout to members). Why: most rulebooks will stop at the guarantor, and rule 1 sends the guarantor to `RB3`; what lies beyond him is the kind of thing a village rulebook leaves to custom.
- `RB3`: `surety` in about 9; `mixed` in about 5; `real-estate` in about 1; `none` in about 0–1; `.NR` in about 1–2. Why: guarantors at drawing are, in my expectation, near universal in 1930s rules, and a mortgage is added where the pot is large.
- `LS1`: `.NR` in about 13; `pro-rata` in about 2; `equal` in about 1; `residual-on-fund` 0–1. Why: a rule that allocates an unmet loss across members is rarer than a rule that names who is liable, and only one existing `ko_*` row carries `LS1` at all.
- `LS3`: `1` in about 10; `.NR` in about 6; `0` in about 0–1; `P` 0–1. Why: house practice (`ko_mitarai_mujin_1773`, `ko_mitarai_hanei_1840`, `ko_mochiyori_yutsu_1876`) codes `1` where a drawn member's property or guarantor answers for the debt, and I expect most rulebooks to say that much.
- `CN3`: `1` in about 14; `P` in about 2 (forfeiture of the draw only); `.NR` in about 1; `0` none. Why: written rules for a running credit kō almost always sanction late payment, by penalty interest, guarantor, or exclusion.
- `GV1`: `collective` in about 7; `.NR` in about 8; `elder-fixed` in about 1; `external-administered` in about 1. Why: modern printed rules often name a 總會 or 講員協議, which may let `collective` be read where the earlier `ko_*` rows could not; but where a 講元 or 發起人 runs the kō the vocabulary has no cell and house practice is `.NR`.

## 3. Expectations by kō

- **6 山野草平取建頼母子.** 取建 suggests a kō raised for the relief of a named person (a 親頼母子). Expect the beneficiary-organiser problem on `GV1` (`.NR`, as `ko_mochiyori_yutsu_1876`), and possibly the 親 or 世話人 named for residual loss.
- **12 春山夏助長壽講.** A personal name and a celebratory name; possibly a 親講 for one person. No firm expectation.
- **14 深井朝右衞門發起頼母子, 15 權田太郎兵衞發起頼母子.** 發起 names a promoter; I expect the 發起人 to carry duties and possibly a guarantee, which could make `RD-test = officers`. The two are from one prefecture and may share a drafting pattern; that would not be corroboration.
- **21 共同信用講.** 共同信用 suggests joint liability; the likeliest kō in the set for `all-members` or `standing-subgroup` on `RD-test`, and for `LS1` to be coded.
- **23 昭和御大典記念講.** Commemorates the 1928 enthronement, so probably began c. 1928; possibly a savings purpose. No expectation on liability.
- **25 親睦講.** Fellowship framing; I expect lighter security and possibly `deferred` or `.NR` on `RD-test`.
- **26 正利講親無金無盡.** 親無金 may mean the 親 takes no pot of his own; I do not know. If so, the 親 is not a beneficiary and might be an officer with duties.
- **27 蒲團講.** Payout possibly in kind (bedding). A drawn member still owes later instalments, so `RD-test` is not `.NA` on the name alone; expect small sums and light security (`RB3 = surety` or `none`).
- **31 富士石碑講.** A kō for a stone monument; possibly no payout to members at all, in which case `RD-test`, `RB3` and perhaps `LS3` could be `.NA`. This is the likeliest `.NA` kō.
- **35 吉武信用貯金講會.** Twelve printed pages and a 信用・貯金 name: the most detailed rulebook, and the likeliest to have a reserve (積立金) and so `RD-test = fund` with `LS1 = residual-on-fund`, and the likeliest `GV1 = collective`.
- **37 岡龍無盡, 39 根津忠一郎企米無盡.** 秋田 usage of 無盡; 39 is perhaps reckoned in rice (企米). No expectation on liability beyond `RB3 = surety`.
- **43 愛宕社講.** A shrine kō; the shrine may be organiser or beneficiary, which would put `GV1` in the same gap as `ko_hokoin_1832`.

## 4. Row-level expectations

- **How many state who bears a drawn member's default beyond his own security?** About 5 of the 17.
- **Most often:** `officers` (a 講元, 親, 發起人 or 世話人 named as liable once the guarantors fail), narrowly ahead of `all-members`. **Not at all:** `standing-subgroup`, with `21 共同信用講` the one place I would not be surprised to see it.

## 5. Pre-reading concerns, recorded before the source

- `RD-test` is conditional on `RB3`: it asks what happens once security is exhausted, so it is ontologically dependent on there being a payout debt (its own `.NA` condition) and, in practice, informed by `RB3`. If it enters the vocabulary, its `applicability_on` should say so.
- `RD-test = fund` and `LS1 = residual-on-fund` are one fact in two columns, as `RD-TEST-DEFINITION.md` already says. I expect at most one kō to instantiate it, so the duplication will be visible in at most one place.
- `LS3`'s house practice codes `1` when a drawn member's property answers for his agreed repayments, although the definition says "beyond what he has … agreed to contribute". I will follow house practice and say so where it bites.
