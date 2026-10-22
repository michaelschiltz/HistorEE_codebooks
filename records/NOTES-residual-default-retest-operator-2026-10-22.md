# Operator brief: the `RD-test` re-test on nineteen rulebooks (2026-10-22)

Slug `residual-default-retest-operator`. Chat A of a two-chat re-test, run in the chat that coded and scored the first test (`residual-default-coding`) and wrote the shortlist (`residual-default-retest-scan`); MS chose this (2026-10-22). That chat does **not** code the re-test. **This file is not in the bundle and must not be shown to the coding chat.** Its §5 and §6 are what the coding is scored against.

## 1. Why a re-test, and what it tests

The first test (logbook 4, 2026-10-22) failed on rule 6's second limb: four eligible kō in three villages, no pair agreeing on all five predictors. Its weaknesses were too few eligible rulebooks, one selector (農林省經濟更生部) and the `LS1` `residual-on-fund` defect, which made any `fund` kō unscorable. This re-test asks the same question — does `RD-test` take values the existing columns do not predict (test 4 of `CLAUDE.md`) — on rulebooks chosen by two other selectors.

## 2. Population, decided by MS before any rulebook was read

**By structure, not by name** (MS, 2026-10-22): any rotating fund whose rules pay a member a pot he must then repay, whatever it is called (頼母子講, 無盡講, 模合, 和合講). 十錢講 and 信用會 rules are excluded. A savings-only 講 stays in and codes `RD-test = .NA`. The operator's earlier description of 模合 as "a different institution" (shortlist, and the question put to MS) was wrong: 模合 is a regional name for the same institution. Corrected here.

**Nineteen rulebooks, from two sources:**

- **M01–M11**: 大蔵大臣官房銀行課『無尽ニ関スル調査』 (1915), pid 944336, appendix 「附 無盡講會規約ノ數例」, pp. 257–276. Public domain.
- **A03–A07**: 司法省調査部『世態調査資料』第三十六號 (c. 1942), pid 1909099, Aomori report, appendix 二, 其ノ三–其ノ七, pp. 78–82. Transmission service.
- **T01–T03**: the same volume, Tokushima report, 附錄 (一) 講則 (イ)(ロ)(ハ), pp. 146–155. Transmission service.

The two sources are 27 years apart and come from two ministries; the 1915 set predates the 無尽業法. A pass on this population says nothing about Tokugawa instruments, and nothing about the 1936 volume's population beyond what the two tests show separately. **The two tests are not pooled.**

## 3. The bundle

`~/GitHub/_blind-residual-default-retest-2026-10-22`: the four doctrine files, `datasets/loss_mitigation_forms/` (data, recodings, datapackage) and both vocabularies as at the live tree after the 2026-10-22 rulings (characteristic vocabulary without `exemplar`), `RD-TEST-DEFINITION.md` (the definition of logbook 6, 2026-10-22 (ii), with ruling 3 as coding rule 7 and the population as a scope section), `FRAMES.md`, a priors template, a table header, a checker and an empty `proposed-of/`. **No logbook, no CHANGELOG, no vault, no `records/`, no views.** A term count over the doctrine, data and vocabularies found 0 hits for both pids, both titles, 青森, 徳島, 模合, 和合講, 十錢講 and `RD-test`; `residual-default` occurs only as the filename of the rulings record cited in the `CN3` and `LS3` `CLARIFIED` sentences and in the four recodings of 2026-10-22.

## 4. Spend, budgeted and reconciled

**Budget:** rung 2 on the nineteen rulebooks — headings and page positions only, to size the set and write `FRAMES.md`.

**Reconciled, and exceeded in one place.**

- **1915 appendix.** Frames 137–147 viewed at 600 px, at which body text is illegible, to count the numbered headings 一–十一. One crop meant to read a heading was too wide: it showed the last articles of **M01** (第三十二條–第三十五條, ending 「本規約中ニ明文ナキ事ハ組合員中協議ノ上規定…」) and the first articles of **M02** (「壹圓模合」, 第一條–第九條, including a 第七條 on the drawer's 擔保 and his 保證人 and what follows 「若不行屆ノ場合」). **M01 and M02 are therefore not predicted in §6.** They stay in the coding set (MS, 2026-10-22); the coder has not seen them.
- **世態調査資料 36.** Frames 42–47 and 78–82 viewed in the logged-in viewer at a size where headings are legible and body text partly so; headings read (其ノ一–其ノ十, 講則 (イ)(ロ)), no clause read deliberately. Tables of contents of the whole volume read.
- Nothing else of either item was opened.

## 5. Scoring rules, fixed before the coding

1. **Agreement** on a predictor means the identical value string, `.NR` and `.NA` included.
2. **An eligible rulebook** has a substantive `RD-test` value (not `.NR` or `.NA`). No rulebook is excluded from scoring; M01 and M02 count.
3. **An eligible pair** is two eligible rulebooks from different places, the place taken from `place_as_printed` as the coder records it. Two rulebooks from one place count as one case. A rulebook whose place is `not printed` can pair only with a rulebook from the other source; two `not printed` rulebooks of one source cannot pair.
4. **The predictors for the pass test are `RB3`, `LS3`, `CN3` and `GV1`.** `LS1` is coded but **not** a pass predictor, because its value `residual-on-fund` restates `RD-test = fund` (logbook 4, 2026-10-22: with it, a `fund` rulebook can never pass). Fixed now, before the coding, on the first test's finding.
5. **Pass:** at least one eligible pair agrees on the four predictors and differs on `RD-test`.
6. **Weak pass, reported but not decisive:** an eligible pair agrees on `RB3` and `CN3` and differs on `RD-test`.
7. **Fail:** eligible pairs exist, but every pair agreeing on the four predictors also agrees on `RD-test` (first limb: the columns predict it), or no pair agrees on the four (second limb: they cannot be compared). Say which limb.
8. **Inconclusive:** no eligible pair.
9. **Also reported, not decisive:** the verdict with `LS1` added as a fifth predictor (the first test's rule), and the verdict with M01 and M02 removed (the operator's exposure).
10. **The scorer is not the coder.** This chat scores, from the coder's frozen table.

What a pass licenses: test 4 met on rotating-fund rulebooks of 1915 and c. 1942 chosen by two ministries. It does not justify WP1 membership, which was fixed by decision, and it does not reverse the first test's fail; the two results are reported side by side.

## 6. Withheld predictions (the operator's, written before the coding; M01 and M02 excluded)

- **Substantive `RD-test` in about 4 of the 17 predicted rulebooks** (the first test's rates were 8 of 21 and 5 of 17).
- **Tokushima (T01–T03): at least one `officers`.** The Tokushima round-table's contents list 「發起人の地位」 and 「講役員の責任其の他」, which suggests that the organiser's or officers' liability was a live question there. This rests on the table of contents only.
- **A07 (ため講貯蓄規約): `RD-test = .NA`** — a savings 講 with no payout debt.
- **Aomori A03–A06: `.NR` on `RD-test` in at least three of four.**
- **1915 (M03–M11): at most two substantive, and no `standing-subgroup`.** No 福岡 rulebooks are expected among the Finance Ministry's examples.
- **No `fund` anywhere.**
- **Predictors:** `CN3 = 1` in at least 15 of 19 (ruling 1 makes any required bond `1`); `RB3` `surety` or `mixed` in at least 14; `LS3 = 1` in about 6 (ruling 2: only where members must guarantee one another or answer for others); `LS1 = .NR` in at least 16; `GV1` split between `collective` and `.NR`, `external-administered` at most 1.
- **Overall: fail or inconclusive is more likely than pass** (the operator puts pass at about one in four). If it passes, the operator expects it on a Tokushima `officers` rulebook against a 1915 `all-members` or `deferred` one, both `RB3 = surety`, `CN3 = 1`, `LS3 = .NR`.

## 7. Order of work

1. MS commits this brief, the prompt, the bundle's `README.md`, `FRAMES.md`, `RD-TEST-DEFINITION.md` and priors template (as `BUNDLE-…-retest` copies), and logbook entries of 2026-10-22, into `records/`.
2. A new chat, **outside the Claude project**, opens on the bundle with the prompt, fills its priors, prints the sha256 and stops. MS commits the filled priors.
3. The chat reads and codes 114 cells into `proposed-of/`, writes its notes and six answers, runs the checker and stops.
4. MS copies the frozen record into `records/` and commits it. Then this chat scores it against §5, reconciles §6 in logbook 4, and MS decides.
