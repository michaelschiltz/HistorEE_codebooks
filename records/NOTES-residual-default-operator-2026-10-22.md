# Operator brief: the `RD-test` blind test on the seventeen reserved kō (2026-10-22)

Slug `residual-default-operator`. Chat A of a two-chat test. Written before the coding chat exists. **This file is NOT in the bundle and must not be shown to the coding chat.** Its withheld section (§5) is what the coding is scored against.

## 1. What is being tested

The definition, values and coding rules of `RD-test`, the residual bearer of a drawn member's default, are fixed in logbook 6, 2026-10-22 (ii), and copied verbatim into the bundle as `RD-TEST-DEFINITION.md`. The question is discriminant validity (test 4 of `CLAUDE.md`). Does `RD-test` take values that the existing cells most likely to predict it do not predict? Those cells are `RB3`, `LS1`, `LS3`, `CN3` and `GV1`.

The question was found on the open half of 『賴母子講規約例』 (NDL pid 1074152; logbook 5, 2026-10-22; vault note `Who answers for a ko member's default was drafted not given`). The open half cannot test it. The reserve was fixed by seeded draw before any rulebook was opened (logbook 2, 2026-10-21 (ii)). It now has seventeen kō after three were spent by exposure.

## 2. The reserve, with pages and frames

Frames are NDL viewer frames (`https://dl.ndl.go.jp/pid/1074152/1/<frame>`). Frame *f* is a two-page spread, right page = printed page 2*f* − 14 and left page = 2*f* − 13; the formula was checked against the manifest's labels for all seventeen. End pages are the page before the next kō begins, so a kō's last page may be shared with the next.

| kō | name                   | prefecture | printed pages | frames |
|----|------------------------|------------|---------------|--------|
| 6  | 山野草平取建頼母子     | 山口       | 15–18         | 14–16  |
| 7  | 昭和講                 | 福岡       | 18–20         | 16–17  |
| 12 | 春山夏助長壽講         | 靜岡       | 29–31         | 21–22  |
| 14 | 深井朝右衞門發起頼母子 | 山口       | 32–35         | 23–24  |
| 15 | 權田太郎兵衞發起頼母子 | 山口       | 35–38         | 24–26  |
| 18 | 山坂昇講               | 福岡       | 51–52         | 32–33  |
| 21 | 共同信用講             | 靜岡       | 57–59         | 35–36  |
| 23 | 昭和御大典記念講       | 福岡       | 61–64         | 37–39  |
| 25 | 親睦講                 | 秋田       | 65–68         | 39–41  |
| 26 | 正利講親無金無盡       | 秋田       | 68–70         | 41–42  |
| 27 | 蒲團講                 | 靜岡       | 70–72         | 42–43  |
| 31 | 富士石碑講             | 靜岡       | 76–79         | 45–46  |
| 33 | 加茂川原昭和講         | 靜岡       | 81–83         | 47–48  |
| 35 | 吉武信用貯金講會       | 福岡       | 85–96         | 49–55  |
| 37 | 岡龍無盡               | 秋田       | 97–99         | 55–56  |
| 39 | 根津忠一郎企米無盡     | 秋田       | 105–107       | 59–60  |
| 43 | 愛宕社講               | 靜岡       | 117–119       | 65–66  |

Frames 2–6 (title, contents, 凡例) are given to the coder too. Frame 67 is the colophon.

## 3. The bundle

`~/GitHub/_blind-residual-default-2026-10-22`, minimal, on the 2026-10-15 precedent. It contains:

- the four doctrine files;
- `datasets/loss_mitigation_forms/` (data, recodings, datapackage) as at `143c950`;
- `vocabularies/loss_mitigation_characteristic.csv` with the `exemplar` column removed, and `loss_mitigation_type.csv`;
- `RD-TEST-DEFINITION.md`, a `FRAMES.md` reading guide, a priors template, a table header, a checker, and an empty `proposed-of/`.

**No logbook, no CHANGELOG, no vault, no `records/`, no views.** A term count over what the bundle carries found 0 hits for `1074152`, `規約例`, `Norinsho`, `農林省`, `default-bearer` and `residual bearer` in the data, recodings, vocabularies and doctrine files (2026-10-22).

**No page images.** Downloading them through MS's Chrome was approved, but Chrome blocked every download after the first, so the coding chat reads the frames in the NDL viewer through the IIIF image API. This is a weaker blind than files: the coder has a browser, so its instructions are the only fence. The one image that did download (`ndl1074152_f02.jpg`, the title page) is in MS's `~/Downloads` and is not used.

## 4. Scoring rules, fixed before the coding

1. **Agreement on a predictor** means the identical value string, `.NR` and `.NA` included, because identical codings are what the matrix cannot tell apart.
2. **An eligible kō** has a substantive `RD-test` value (not `.NR` or `.NA`). **Kō 7 is coded but excluded from scoring**: the ministry's glosses to kō 19 and 28, in the open half, refer to kō 7's 解説 for クビリ, so its value is half-known to the operator. The coder is not told this.
3. **An eligible pair** is two eligible kō from different villages, the village taken from each kō's heading and 解説 as the coder records it. Kō from one village count as one case.
4. **Pass:** at least one eligible pair agrees on all five predictors and differs on `RD-test`.
5. **Weak pass, reported but not decisive:** an eligible pair agrees on `RB3` and `CN3` only and differs on `RD-test`.
6. **Fail:** eligible kō exist, but every pair that agrees on all five predictors also agrees on `RD-test`, or no pair agrees on all five. On this evidence, the existing columns either predict `RD-test` or cannot be compared with it. Do not adopt.
7. **Inconclusive:** fewer than two eligible kō from different villages. The reserve is too silent to test, and that is a result, not a fail.

What a pass licenses is limited. It meets test 4 on Shōwa rulebooks chosen by a regulator. It does not justify WP1 membership, which was fixed by decision, and it says nothing about Tokugawa instruments.

## 5. Withheld predictions (the operator's, written before the coding)

- **Substantive `RD-test` in about 6 of 17.** Under the fixed rules the open half gives 8 of 21: 11 `all-members`; 19, 28, 29 and 36 `standing-subgroup`; 30 and 34 `officers`; 42 `deferred`. Kō 41 drops to `RB3` under rule 1, and kō 8 to `.NR` under rule 3.
- **Kō 7: `standing-subgroup`** (known, excluded).
- **Kō 35 (吉武, 福岡): `standing-subgroup`.** It is likely the same village as the open half's kō 19, which uses 部落 liability. If so, it is one case with kō 19 and not independent of it.
- **Kō 18 and 23 (福岡): `standing-subgroup` or `.NR`.**
- **At least one Akita kō `all-members`**, on kō 11's pattern and on 第一講's 相互不可分連帯. Of the four Akita kō, 37 (rice, relief) or 39 (rice, the 親's business) is the more likely.
- **Kō 33 (Shizuoka, an organisation kō): `officers`**, on kō 34's pattern.
- **Predictors:** `LS1` `.NR` in at least 14 of 17; `CN3` = `1` in at least 12; `RB3` `mixed` or `surety` in at least 12; `LS3` = `1` in most; `GV1` mostly `collective`.
- **Overall: pass**, most likely on a Fukuoka `standing-subgroup` kō against an Akita `all-members` kō, both coded `RB3 mixed`, `CN3 1`, `LS3 1`, `GV1 collective`, `LS1 .NR`.

## 6. Spend, budgeted and reconciled

This chat is the continuation of `tanomoshi-ko-retrieval` and carries everything it spent: the whole open half read, and three reserved kō in part (2, 9, 40). **For this step the budget was rung 2 only on the reserve**: names, prefectures and pages from the manifest, plus an illegible 400-pixel overview of frames 67–68 to find where kō 43 ends. Reconciled: that is all that was read of the reserve. The 43-frame download fetched the reserve images into Chrome's memory without displaying them, so it read nothing, and none was saved except the title page.

## 7. Order of work

1. MS commits logbook 6, 2026-10-22 (ii), this brief, the prompt and the bundle README into `records/`.
2. The coding chat opens on the bundle, fills its priors, prints the sha256 and stops. MS commits the filled priors.
3. The chat codes 102 cells into `proposed-of/TEST-residual-default-2026-10-22.csv`, writes its notes and answers, and stops.
4. A scoring chat, or this one, scores the table against §4 and reconciles §5 in logbook 4. Then MS decides whether to adopt.
