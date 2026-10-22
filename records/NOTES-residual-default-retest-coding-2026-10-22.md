# Coding notes: `RD-test` re-test on nineteen rulebooks (2026-10-22)

Coder: `claude-opus-5-5`, effort `high`, `coder=ai`. Blind bundle `_blind-residual-default-retest-2026-10-22`. Priors: `PRIORS-residual-default-retest-filled-2026-10-22.md`, sha256 `5d40e3c9c1875d957265bc9b1e69b29439a8e5c2037bb6dffecdf726abcdcce2`, filled before any page was opened; the maintainer reported it committed before reading began, and the bundle copy was re-hashed unchanged at 17:06 JST before the first page was opened.

**Ordering held.** Each rulebook's six cells were written to a working file before the next rulebook's rules were read; no rulebook was compared with another, or with any existing `ko_*` row, until all 114 cells were fixed. Everything in §4 onwards, and every comparison in the six answers, was written after that point. One reading correction was made after the 114 were fixed (a T01 `LS1` note that misdescribed art. 28; the value did not change), and place strings were shortened to the printed place only.

**What was not used.** No memory tool, past-chat search, Drive, connector, other website or other NDL page. No source other than the two items. No general knowledge in any cell.

**Selectors.** Source M's eleven rulebooks were chosen by the Finance Ministry's banking section; Source S's eight by the Justice Ministry's research department, for reports on local practice. Neither choice is random, and where rulebooks agree below, the agreement is not corroboration. Three in M (M08, M09, M10) share one drafting template (managers with 無限ノ責任 who pay each pot 講金ノ集否ニ拘ラス, approval by the 監督官署, the same dissolution and inspection clauses); two of them are model texts with blanks. The three Tokushima rules (T01-T03) share another (an 抵當預リ人 holding a mortgage for all members, the drawer's debt split into 小手形 to each undrawn member). Counted by drafting tradition rather than by rulebook, the four `officers` values in M rest on two drafting sources at most (the M08-M10 template, and M06), and the Tokushima `mixed` and `.NR` values rest on one.

## 1. Reading record

Source M was read through the IIIF image service on dl.ndl.go.jp in Chrome, in crops of one page at a time; Source S in the NDL viewer only, in the maintainer's Chrome, with the viewer's zoom. Frame-to-page arithmetic in `FRAMES.md` held throughout. True pages of each rulebook, as found:

- M01 pp. 257-260; M02 pp. 260-262; M03 pp. 262-263; M04 pp. 263-265; M05 pp. 265-266; M06 pp. 266-267; M07 pp. 267-268; M08 pp. 268-271; M09 pp. 271-272; M10 pp. 272-275; M11 pp. 275-276.
- A03 pp. 78-79; A04 pp. 79-80; A05 p. 80; A06 p. 81; A07 pp. 81-82.
- T01 pp. 146-149; T02 pp. 149-151; T03 pp. 151-154; forms (二) pp. 155-156, (三) p. 157, (四) p. 158.
- M08 and M09 are model texts (何々講, 何郡何村, 何某, blank dates); T01-T03 print every personal name as 何某 except one. They are coded as listed.

Frame by frame:

- Source M title: viewer frame 1 (cover) and IIIF frame 3 (the first printed leaf after the cover), viewed only to confirm the item; the 目次 was consulted for the appendix's pages. Nothing in them was used.
- Source S title: viewer frame 1 (cover) and the viewer's 目次 tab (table of contents of the three reports, read as headings only). The viewer's side panel also showed an unrelated recommended item (a 1999 book); not opened.
- ACCIDENTAL: IIIF full-frame view of frame 137 at low resolution shows the right page, p. 256 (end of the ministry's chapter on 無盡講, outside the list). Seen as a page image while locating p. 257; not read for content and not used. All later reading used crops of one page.
- M01: frame 137 left (p. 257), frame 138 right and left (pp. 258-259), frame 139 right (p. 260, top columns: M01 arts. 32-35 and closing formula). M02's heading and first articles on p. 260 were in the same crop and seen while finishing M01; M01's cells were fixed before M02 was read.
- Method for Source M: IIIF crops of one page at a time (left page ≈ x 13-48 %, right page ≈ x 49-84 % of the frame), in three horizontal bands at 735 px height, with narrower crops where two rulebooks share a page; a low-resolution full-frame view (700 px, illegible at that size) was taken of each frame only to locate the pages.
- M02: frames 139 left (p. 261), 139 right (p. 260, M02 columns), 140 right (p. 262, M02 columns only).
- M03: frame 140 right (p. 262, M03 columns), 140 left (p. 263, M03 columns). Checked the heading column for a prefecture tag: none.
- M04: frame 140 left (p. 263, M04 columns), 141 right (p. 264), 141 left (p. 265, first columns: end of M04 signatures).
- M05: frame 141 left (p. 265), 142 right (p. 266, M05 columns).
- M06: frame 142 right (p. 266, M06 columns), 142 left (p. 267, M06 columns).
- M07: frame 142 left (p. 267, M07 columns), 143 right (p. 268, M07 columns incl. signature line).
- M08: frame 143 right (p. 268, M08 columns), 143 left (p. 269), 144 right (p. 270), 144 left (p. 271, M08 columns).
- M09: frame 144 left (p. 271, M09 columns), 145 right (p. 272, M09 columns).
- M10: frame 145 right (p. 272, M10 heading and art. 1), 145 left (p. 273), 146 right (p. 274), 146 left (p. 275, first columns: signature heads).
- M11: frame 146 left (p. 275), 147 right (p. 276). Frame 147 left (p. 277, 第三章 無盡營業) appeared only in the 700-px locating view, illegible; not read.
- Every M rulebook's cells were written to the working file before the next rulebook's columns were read.
- On shared pages a full-width band sometimes showed the opening columns of the next rulebook (p. 262: M03 under M02; p. 263: M04 under M03; p. 266: M06 under M05; p. 268: M08 under M07; p. 272: M10 under M09). Those columns were transcribed only after the current rulebook's six cells were written.
- Source S, viewer only (side panel collapsed; viewer zoom 59-124 %, panned by dragging). A full-screen request did not engage.
- ACCIDENTAL: frame 45's right page (p. 78) opens with the end of 其ノ二 (信用會 rules, out of scope) in the upper tier: its last articles and an officers' block with a 弘前市 address were visible in the overview and partly in zoomed views while locating 其ノ三. Not read for content and not used.
- A03: frame 45 right page upper tier (其ノ三 heading, arts. 1-3), lower tier (arts. 4-16), left page upper tier (art. 16 end - 19 and closing formula).
- A04: frame 45 left page upper tier (其ノ四 heading, items 一-五) and lower tier (六-十四, closing formula, date).
- A05: frame 46 right page upper tier (其ノ五 heading, arts. 1-6) and lower tier (arts. 7-14, closing formula, signature heads 會主 / 保證人 / 同). The upper tier's first columns on p. 80 are A04's signature heads.
- A06: frame 46 left page upper tier (其ノ六, all items to 以上).
- A07: frame 46 left page lower tier (其ノ七 arts. 1-8), frame 47 right page upper tier (art. 8 end - 13).
- Forms 其ノ八-十 (frame 47, read after A03-A07 were fixed): 其ノ八 連帶借用書 (昭和四年, 'some 企頼母子', two joint co-borrowers), 其ノ九 金子預リ證 ('某企和合講', three joint depositaries, 昭和八年), 其ノ十 恩證 (大正十五年, a 企主's undertaking with 宿受保證人 taking over all his obligations). None names the association of any of A03-A07 (each says 某企 or 和合講 generically), so none was used for any cell, as FRAMES.md requires. The resemblances (其ノ八 to A03's 連帶借用人二名; 其ノ九 and 其ノ十 to A04's three 連帶證人, 企主 and 請宿) are recorded as decision points, not evidence.
- ACCIDENTAL: the left page of frame 47 carries the start of 三 統計表 (p. 83) in its lower tier/left edge; its title and column heads were visible in panned views. Not read and not used.
- T01: frame 81 right page (p. 146) upper and lower tiers, left page (p. 147) upper and lower tiers; frame 82 right page (p. 148) upper and lower tiers, left page (p. 149) first columns (T01's last signature line). T02's heading on p. 149 was in view at the same time; T01 was fixed first.
- T02: frame 82 left page (p. 149) upper and lower tiers; frame 83 right page (p. 150) upper and lower tiers; frame 83 left page (p. 151) upper tier (arts. 28-30, officers' list). T03's heading on p. 151 was in view; T02 was fixed first.
- Reading note: at 69 % some 扱/拔 and 債/償 pairs were ambiguous; a closer look at T02 art. 17 settled 取扱人 and 債權者, and quotations use those readings.
- T03: frame 83 left page (p. 151) lower tier (arts. 1-5); frame 84 right page (p. 152) upper tier (arts. 6-9 and the small-bill form), lower tier (arts. 10-13), a second look at the left edge of the lower tier for the end of art. 13; frame 84 left page (p. 153) upper tier (arts. 13 end-18) and lower tier (arts. 19-26); frame 85 right page (p. 154) upper tier (arts. 26 end-30) and lower tier (arts. 31-32, election record, signatures).
- Forms (二)-(四), read after T03's text and before T03's cells were written: (二) 講通帳 cover and pages, frame 85 left (p. 155) and frame 86 right (p. 156): titled 淨智寺第貳明照積立講通帳 - '第貳', so a second association of the same temple, not the one whose rules are T03 (its art. 1 names 淨智寺明照積立講 with no number); it records instalments and receipts and has no clause bearing on any cell. (三) 土地貳番抵當權設定講金借用證書, frame 86 left (p. 157): names 某殿發起頼母子講第壹號貳季積立講, a different association from T01-T03; it makes the 保證人 jointly liable (保證人ハ連帶債務ノ責任ヲ負擔ス). (四) 講金借用小手形, frame 87 right (p. 158): names the same 第壹號貳季積立講. Neither (三) nor (四) names any of T01-T03, so neither was used as evidence; (四) was used only to confirm the reading 糶賣 in T03's own art. 9 form.
- ACCIDENTAL: frame 87 right page lower tier carries the heading and first articles of (五) 講會取締規則 (p. 158), and the left page (p. 159) its continuation; visible in the overview and partly in panned views. Not read and not used.

## 2. The 114 cells at a glance

Values with confidence; every cell's quotation and argument is in its `notes` field in the CSV. There is no `.NA` anywhere (see §4).

| id  | name_as_printed      | place_as_printed                         | RD-test           | RB3                | LS1 | LS3        | CN3        | GV1                 |
|-----|----------------------|------------------------------------------|-------------------|--------------------|-----|------------|------------|---------------------|
| M01 | 金四拾圓模合規約書例 | 沖縄縣                                   | .NR               | mixed (high)       | .NR | .NR        | 1 (high)   | collective (high)   |
| M02 | 壹圓模合契約書例     | 沖縄縣                                   | .NR               | mixed (high)       | .NR | .NR        | 1 (high)   | .NR                 |
| M03 | 模合規約書例         | not printed                              | .NR               | surety (high)      | .NR | .NR        | 1 (high)   | collective (medium) |
| M04 | 永續講無盡規約       | 埼玉縣; 早稻田村 (signatures)            | .NR               | mixed (medium)     | .NR | 1 (medium) | 1 (medium) | .NR                 |
| M05 | 永續講法方           | 埼玉縣 北葛飾郡早稻田村                  | .NR               | mixed (high)       | .NR | .NR        | 1 (high)   | .NR                 |
| M06 | 頼母子永續講規約書   | 埼玉縣 北葛飾郡早稻田村                  | officers (low)    | real-estate (high) | .NR | .NR        | 1 (medium) | .NR                 |
| M07 | 規約書               | 埼玉縣; 中爪第二區 (no 村 printed)       | all-members (low) | surety (high)      | .NR | 1 (medium) | 1 (high)   | .NR                 |
| M08 | 何々講規約           | 鳥取縣 (model text: 何郡何村 left blank) | officers (medium) | mixed (medium)     | .NR | 1 (high)   | 1 (high)   | collective (medium) |
| M09 | 日掛講規約書         | 鳥取縣 (model text: 郡市町村 left blank) | officers (high)   | mixed (medium)     | .NR | 1 (high)   | 1 (high)   | collective (medium) |
| M10 | 規約書               | 島根縣                                   | officers (high)   | personal (medium)  | .NR | 1 (high)   | 1 (high)   | collective (medium) |
| M11 | 大正共益講規則       | 高知縣; 高知市 (art. 3)                  | .NR               | surety (high)      | .NR | 1 (high)   | 1 (high)   | .NR                 |
| A03 | 頼母子講規約         | not printed                              | .NR               | surety (high)      | .NR | 1 (high)   | 1 (high)   | collective (medium) |
| A04 | 和合講規約           | not printed                              | .NR               | surety (high)      | .NR | .NR        | 1 (high)   | collective (medium) |
| A05 | 和合講規約           | not printed                              | .NR               | surety (high)      | .NR | .NR        | 1 (high)   | collective (low)    |
| A06 | 龍川寺和合講規約     | 三戸町                                   | officers (medium) | .NR                | .NR | 1 (high)   | 1 (medium) | elder-fixed (low)   |
| A07 | ため講貯蓄規約       | 德下村                                   | .NR               | surety (high)      | .NR | .NR        | 1 (medium) | collective (high)   |
| T01 | 救濟頼母子講規約     | 德島市                                   | .NR               | mixed (medium)     | .NR | .NR        | 1 (high)   | collective (medium) |
| T02 | 積立講規約           | 德島市                                   | .NR               | mixed (medium)     | .NR | .NR        | 1 (high)   | collective (medium) |
| T03 | 淨智寺明照講規約     | 德島市                                   | .NR               | mixed (medium)     | .NR | 1 (medium) | 1 (high)   | collective (medium) |

## 3. Decision points, with the alternative stated

Each is argued in full in the cell's note; here is the choice and the reading not taken.

1. **M01 `RD-test` `.NR` vs `deferred`/`fund`.** Art. 12 sends pledge disposal to the 集會協議 and art. 35 sends unprovided matters to the meeting; art. 32 keeps a common emergency share. Taken: `.NR`, because the meeting decides only to start selling the pledge, art. 35 is the general clause rule 7 excludes, and nothing ties the emergency share to default. Not taken: `deferred` (art. 12) or `fund` (art. 32).
2. **M02 `RD-test` `.NR` vs `officers`.** Art. 9 makes the 發起者 answer for loans re-lent from a drawer's cash top-up deposit; art. 29 makes the 監督者 answer for a shortfall in the 共有金. Taken: `.NR`, since neither clause reaches a drawn member's default on his pot. Not taken: `officers`, which would join three clauses the rules do not join.
3. **M02 `LS3` and `GV1`.** Whether the 監督者 are members is not stated. If they are, `LS3` is 1 (or arguably `P`); `GV1` stays `.NR` either way (named officers in the first instance, meeting as appeal body).
4. **M03 `LS3` `.NR` vs 1.** 受取人ノ外株主中ノ承認ヲ得タル保證五人以上 read as sureties approved by the shareholders (taken) or as sureties drawn from the shareholders (1 by the association route).
5. **M04 `LS3` 1 (medium) vs `.NR`.** The 當寺世話人 who sign for the temple's draw (art. 3) are read as the same persons as the 世話人 who take the last draw (art. 4); the signature line 檀徒惣代人兼永續講世話人 supports this. If they are different persons, `.NR`.
6. **M05 `RD-test` `.NR` vs `deferred`.** 社中何人ヲ問ハス半途ニシテ苦情ヲ唱ヒ候者又ハ事故有テ掛繼キ不致者有之砌ハ社中一同協議ノ上取計ヒ could be read to cover drawn members, which would make it a clause about default itself. Taken: an unwon member's case (rule 5), because the consequence (return of what he paid out of a later pot) only fits a member who is owed money. Not taken: `deferred`.
7. **M06 `RD-test` `officers` (low) vs `.NR`.** 滿會ヲ告クル迄ノ期間講務ニ關スル一切ノ權利義務ハ引受世話人ノ責任トスル事: taken as putting the fund's obligations, and so a drawer's shortfall, on the 引受世話人. Not taken, and strong: 責任 as charge of administration, or the clause's scope confined to the convener's own instalments it opens with; then `.NR`.
8. **M07 `RD-test` `all-members` (low).** 本講員ニテ不納者ヲ生シタル場合ハ組合及證人引受必ス納入スヘキモノトス, with the kō constituted of the 中爪第二區衞生組合 (art. 2). Alternatives: `standing-subgroup` if the 衞生組合 is larger than the kō (but that value requires a group the rules set up, and these rules presuppose it); no value at all if 組合 means a treasury outside the fund. `LS3` 1 (medium) rests on the same reading.
9. **M08 `RD-test` `officers` (medium).** The joint effect of art. 3 (managers 債權債務ニ關シ無限ノ責任) and art. 15 (pots paid 講金ノ集否ニ拘ラス); no clause names the drawn defaulter. Not rule 3, because art. 22 treats the managers' fault separately. M09 art. 11 and M10 art. 16 (三) name the defaulter in terms and are coded high.
10. **M10 `LS3` 1 vs `P`.** The same clause that puts a drawn member's default on the managers shields everyone else (他ノ講員ニハ更ニ損失ヲ掛ケサルモノトス). Taken: 1 on the characteristic's wording. Not taken: `P`, for exposure confined to one class of member.
11. **M11 and A03: sureties who must be members.** M11's sureties are members unless the officers admit an outsider, and a drawing surety's pot is cut by his principal's arrears (art. 12); A03's two co-borrowers come from the remaining members. Under `RD-test` rule 1 they answer by signing, so they are `RB3` (surety) and `RD-test` is `.NR`; under the `LS3` ruling they are members answering for another, so `LS3` is 1. Both follow the definitions; see answer 4.
12. **A06 `RD-test` `officers` (medium) vs `.NR`.** 講長及世話人ハ懸金ノ遲怠者ノ有無ニ不拘糶取金支拂ヲ保證スル: taken as the officers bearing a default. Not taken: a guarantee of timely payment only (遲怠 is lateness), with their exposure capped at the share they hold back.
13. **A06 `GV1` `elder-fixed` (low) vs `.NR`.** Residual decisions vest in the temple's incumbent and the parish representatives by office (其ノ他ノ必要事項ニ就テハ講長及取締役世話人ニ於テ協議ノ上之ヲ決ス). The value is undefined in the vocabulary, and the same temple-convener pattern is `.NR` at M04 and M05; the difference is this express clause.
14. **A06 `RB3` `.NR`.** 擔保物件 required, its kind not named (as at `ko_meio_1498`).
15. **A07 scope.** A savings fund that lends to members (art. 8). The applicability clause (a payout that creates a debt owed to the fund) is met by a loan, so no cell is `.NA`; the population sentence (contribute in rounds, receive a pot) fits it only loosely.
16. **Aomori forms 其ノ八-十.** They resemble A03 (two joint co-borrowers) and A04 (three joint sureties, a 企主, a 宿受人), but name no association of A03-A07 and were not used.
17. **T01-T03 `RD-test` `.NR` vs `all-members`/`LS1` `pro-rata`.** The drawer's debt is split into 小手形, one to each undrawn member (T01 art. 10, T02 art. 20, T03 art. 9), so an unrecovered shortfall would by the form of the debt lie with whoever holds his bills. Not coded: that follows from the instrument's form, not from a clause about default, and rule 6 forbids supplying it.
18. **T03 `LS3` 1 (medium).** Debtor route: the printed small bill binds 抵當物件糶賣及拙者所有ノ財產. Taken as liability beyond the pledge with his own property; medium because 'whole estate' is not said in terms and the bond the 抵當預リ人 drafts is not printed. 糶 confirmed from form (四), which names another association and was used only as a reading aid.
19. **T03 `RB3` `mixed` vs `general-estate`.** The same small bill adds 拙者所有ノ財產 behind the mortgage. Taken: `mixed` (land or securities), the bill being an undertaking to pay, not a charge.
20. **Tokushima forms.** (二) is the passbook of 淨智寺第貳明照積立講, a second association of T03's temple, not T03's; (三) and (四) name 某殿發起頼母子講第壹號貳季積立講. None used as evidence.

## 4. Every `.NR` and `.NA`, argued

**`.NA`: none.** Every rulebook sets up a payout that leaves the receiver owing the fund or its members: deferred instalments on a drawn pot (all M, A03-A06, T01-T03), a bolt of cloth repaid by instalment (M10), rice repaid in rice (A05), or a loan from savings (A07). No cell's ground is absent, so `.NA` would be wrong in every row.

**`RD-test` `.NR` (13).** In each, the rules were read in full and name no bearer beyond the drawer's own security; the last named obligor is the drawer, his sureties or co-borrowers, or his pledge.

- M01: drawer, then 保證人, then 抵當 (art. 12); art. 35 is a general clause (rule 7).
- M02: drawer with 保證人, then 抵當 (art. 6); officer clauses do not reach the pot (decision 2).
- M03: 保證人ニテ辨償 (art. 11) and nothing after.
- M04: no default clause of any kind; the 世話人連署 is security for the temple's draw (rule 1).
- M05: drawer's three sureties (p. 265); the members' 協議 clause is an unwon member's case (decision 6).
- M11: sureties, sanctioned by loss of rights (art. 11), are security (rule 1).
- A03: two co-borrowers from the members, liable by signing (rule 1); the 宿受人 covers the convener's failure to hold the meeting, not a drawer's default.
- A04: three joint sureties; the 訴訟準備金 funds suits, it does not bear losses; 企主ヲ全體證人ニセサルコト allocates nothing.
- A05: sureties and a joint bond (arts. 7-8, 14); no bearer after them.
- A07: two sureties per loan (art. 8 (三)); no bearer after them.
- T01: pledge sold without notice, then acceleration of the drawer's own debt (arts. 31, 36: rule 4); art. 39 is a general clause (rule 7).
- T02: pledge enforced by the 抵當預リ人 (art. 23); no clause on a shortfall; small-bill structure not coded (decision 17).
- T03: 債務證書ニ依リ處分 (art. 21) and the small bill's own-property undertaking are the drawer's own liability (rule 4).

**`RB3` `.NR` (1).** A06: a pledge is required but its object is not named.

**`LS1` `.NR` (19).** No rulebook says how an unmet loss is divided. Where a bearer is named (M06-M10, A06) the clause says who, not how; where gains or costs are shared (M01 arts. 33-34; M08 art. 12 feast costs 講員平等ニ負擔; M09 art. 7; A04 item 十二; T01 art. 13; T03 art. 10) the sharing is of income, reserves or expenses, not of a default loss.

**`LS3` `.NR` (10).** No member answers for another by rule, and no clause binds the drawer's person or whole estate beyond his security; security for his own repayment is `.NR`, not 0, under the 2026-10-22 ruling, and no rulebook confines liability to the pledge.

- M01: three sureties of approved standing, not required to be members; art. 13 extends the drawer's own liability to costs and damages only.
- M02: officers' guarantees exist (arts. 9, 29) but the officers' membership is not stated (decision 3).
- M03: surety membership turns on parsing art. 10 (decision 4).
- M05: the drawer's sureties and the convener's guarantors are not said to be members.
- M06: both the 引受世話人's liability and their membership are uncertain.
- A04, A05: sureties need the members' consent, not membership.
- A07: sureties' membership not stated.
- T01, T02: pledge only; acceleration and damages concern the drawer's own debt.

**`GV1` `.NR` (6), each 'no fitting value' rather than silence.**

- M02: four 監督者 decide discipline in the first instance with the 總會 as appeal body.
- M04: temple as convener and principal beneficiary, 世話人 holding deeds, no meeting.
- M05: temple 會主, 引受世話人, and one referred decision to the members.
- M06: rules adopted by 株主一同ノ評決, conduct thereafter vested in the 引受世話人.
- M07: the sole officer holds office ex officio as deputy head of the sanitation association.
- M11: officers fixed for the life of the fund, removable by the 總會 only for misconduct.

**Articulation.** Every substantive cell is `articulated`: each rests on a clause of the rulebook quoted in its note. No cell rests on an analyst's description.

## 5. The six answers

### Answer 1: what was coded, and on what evidence

All 114 cells, from the rules and the forms printed with them, each quotation copied from the page image in its printed script with page and article.

- `RD-test`: 6 substantive of 19. `officers` 5 (M06 low, M08 medium, M09 high, M10 high, A06 medium); `all-members` 1 (M07 low). The two high values rest on clauses that name the drawn defaulter and put him on the managers: M09 art. 11 (本講管理人ハ講金ノ集否ニ不拘落札者ニ講金ヲ交付シ前條ノ者ニ對シテハ相當ノ處置ヲ爲スモノトス) and M10 art. 16 (三) (空掛人退講シ掛金ヲ爲サヽルトキハ管理人之ヲ負擔シ他ノ講員ニハ更ニ損失ヲ掛ケサルモノトス). No `fund`, `standing-subgroup` or `deferred`.
- `RB3`: 18 substantive. `mixed` 9, `surety` 7, `real-estate` 1 (M06), `personal` 1 (M10).
- `LS3`: 9 at 1. Association route in eight (M04, M07, M08, M09, M10, M11, A03, A06); debtor route in one (T03).
- `CN3`: 1 in all 19; eleven high, the rest medium where only a security requirement, and no stated consequence, carries the value.
- `GV1`: `collective` 12, `elder-fixed` 1 (A06).

By source. M: `RD-test` substantive in 5 of 11, all from rulebooks that make officers or the association pay pots regardless of collection; `LS3` 1 in 6. Aomori: `RD-test` substantive in 1 of 5 (A06); `RB3` surety in 4. Tokushima: `RD-test` `.NR` in all three; `RB3` `mixed` (mortgage on land or securities, no sureties) in all three; `GV1` `collective` in all three. The Tokushima uniformity is one drafting tradition and one ministry's choice, not three findings.

### Answer 2: what could not be coded, and why

- `LS1`: none of 19. No rulebook divides an unmet loss; where a bearer is named it is a single class (officers, or the 組合), and division among them is never stated.
- `RD-test`: 13 of 19. In all of them the instrument stops at the defaulter's own security. In the three Tokushima rules the drawer's debt is owed to the holders of his small bills, so where a shortfall falls is a consequence of the instrument's form that no clause states (decision 17).
- `LS3`: 10 of 19, because security for a member's own repayment is `.NR` under the 2026-10-22 ruling and, in four of the ten (M02, M03, M05, M06), because the membership of the persons who answer is not stated.
- `GV1`: 6 of 19, because the value set has no state for a temple as convener-beneficiary (M04, M05), officers deciding with a meeting as appeal body (M02, M11), adoption by the members followed by stewards' control (M06), or an office held ex officio in another body (M07).
- `RB3`: A06 only (pledge of unnamed kind).

### Answer 3: which of my priors were falsified

Quoted verbatim from the filled priors, then the outcome.

- "`RD-test`: `.NR` in about 11–13; `officers` in about 2–3; `all-members` in about 2; `deferred` in about 1–2; `fund` in about 1; `standing-subgroup` in 0; `.NA` in 0–2." Held on `.NR` (13), `standing-subgroup` (0) and `.NA` (0). Falsified on `officers` (5, above the range), `all-members` (1), `deferred` (0) and `fund` (0).
- "`RB3`: `surety` in about 7–8; `mixed` in about 5–6; `real-estate` in about 2; `.NR` in about 3; `none` 0; `.NA` 0–2." Held on `surety` (7) and `none` (0). Falsified on `mixed` (9), `real-estate` (1), `.NR` (1); `personal` (1) was not foreseen.
- "`LS1`: `.NR` in about 15–16; `residual-on-fund` in about 1; `pro-rata` in about 1–2 (shortfall borne per 口); `equal` 0–1; `capped` 0; `.NA` 0–2." Falsified: `.NR` in 19, no positive value.
- "`LS3`: `.NR` in about 12; `1` in about 5; `0` in about 0–1; `P` 0; `.NA` 0–2." Falsified on 1 (9) and `.NR` (10). The mechanism I gave ("require that 保證人 be 講員 or to make liability 連帶") is right for M11 and A03; most of the 1s came instead from officers' guarantees (M04, M08-M10, A06).
- "`CN3`: `1` in about 15–16; `P` in about 1–2 (forfeiture of the draw or 除名 only); `.NR` in about 1–2; `0` 0; `.NA` 0." Falsified at the edges: 1 in all 19.
- "`GV1`: `.NR` in about 10–11; `collective` in about 5–6 (a 總會 / 講員協議 deciding); `external-administered` in about 1–2 (a commercial 營業者 running the fund); `elder-fixed` in about 1." Falsified: `collective` 12, `.NR` 6, `external-administered` 0. Held on `elder-fixed` (1).
- "I expect it to over-represent formally drafted rules with numbered articles and to include one or more commercial 營業無盡 schemes run by a promoter or company, where the operator guarantees the members (`RD-test = officers`, `GV1 = external-administered`)." Falsified in its mechanism. The `officers` values in M come from managers elected from the members (M08-M10) or stewards (M06), not from a commercial operator, and there is no `external-administered`.
- "I expect shorter, rural, customary rules, more silence (`.NR`) across the board, possibly a savings-type 講 among the five (hence a chance of `.NA` on `RD-test` and `RB3`), and the bonds (其ノ八–十) to carry the security clauses the rules omit, if they name the same association." Partly falsified. A07 is savings-type but lends, so it took no `.NA`; none of the bonds names any of the five associations; and Aomori is not more silent than M on `RD-test` (4 of 5 `.NR` against 6 of 11).
- "I expect the most formalised security of the three sets (a 大手形 for the drawn member's whole remaining obligation signed by guarantors, 小手形 per instalment), therefore `RB3 = surety` or `mixed`, `CN3 = 1`, and the best chance of a `連帶` clause that makes `LS3 = 1`." Falsified in substance. The Tokushima rules take no sureties at all, only mortgages on land or securities (`mixed` in the property sense). No 連帶 clause appears in any of the three. The one `LS3` 1 comes by the debtor route (T03). The 小手形 is one bill per creditor member for the whole debt, not per instalment, and the 大手形 printed (三) belongs to another association.
- "About 6 of the 19 (range 4–8)." Held: 6.
- "Most frequent `RD-test` value: `officers` (convener or 世話人 answerable for the deficit). Not at all: `standing-subgroup`." Held on both counts, though the officers are mostly elected managers rather than conveners.

### Answer 4: characteristics that did not fit the evidence

**`RD-test`.** Values were not widened.

1. **The definition assumes the debt is owed to the fund.** In T01-T03 the drawer's debt is split into small bills held by each undrawn member (T03 art. 9: 第七條ノ規定ニヨリ債權ヲ設定シタル時ハ各掛込人ニ對シ左ノ小手形ヲ差シ入ルベキモノトス), so a residual default falls by the instrument's form on the bill-holders. The value set has no state for this. It is neither the fund, nor 'all members' (the drawn members hold no bills), nor a subgroup the rules set up by membership. Coded `.NR` by rule 6.
2. **Rule 1 meets a membership-restricted surety pool.** M11 and A03 require sureties or co-borrowers to come from the members. Liability attaches by signing, so it is `RB3`, but only members can sign. The 'signing or belonging' test sorts these correctly and still hides that the members, as a body, carry the default. `LS3` (association route) records it; `RD-test` cannot.
3. **Bearing vs advancing.** A06's officers guarantee payment 懸金ノ遲怠者ノ有無ニ不拘, and M08's managers pay pots 講金ノ集否ニ拘ラス. The definition asks who is made liable for what remains unpaid; these clauses say who pays first, and imply but do not state who keeps the loss. Coded `officers` at medium.
4. **Pre-existing bodies.** M07's 組合 is a sanitation association the rules presuppose. `standing-subgroup` requires a group 'the rules set up in advance', and `all-members` fits only if the kō and the 衞生組合 coincide. Coded `all-members` at low.
5. **Defaults the definition does not reach.** The convener's own failure is backed by guarantors pledging land (M05) or by the 宿受人 (A03), and M02's officers guarantee loans re-lent from a drawer's deposit. Each is a residual-loss rule the characteristic does not ask about. Recorded, not coded.
6. **Population vs applicability.** A07 lends from savings rather than rotating a pot. It meets the applicability clause and only loosely the population sentence.
7. **The `LS1` overlap is untested.** No rulebook took `fund`, so `LS1 = residual-on-fund` never co-occurs with it, and the known overlap neither showed nor failed to show.

**Existing characteristics.**

- **`RB3`.** No value holds securities (公債, 株券, 社債券, 有價證券: M01, M02, M04, T01-T03), and `mixed` is doing three jobs: property plus surety (M01, M02, M05), surety *or* property (M08, M09), and several kinds of property (M04 with a cash retention and a signing surety; T01-T03). The caution recorded at `ko_mitarai_gin_1805` now has seven more instances.
- **`GV1`.** Six of 19 had no fitting value, for four distinct structures (answer 2), and `elder-fixed` is undefined. The temple-convener gap of `ko_hokoin_1832` recurs at M04 and M05.
- **`CN3`.** Under ruling 1 every rulebook that requires security is 1, so the characteristic took no variance in 19 and is implied by any substantive `RB3` (see answer 5).
- **`LS3`.** M10's shield clause (他ノ講員ニハ更ニ損失ヲ掛ケサル) confines exposure to the managers. The ternary has no way to say 'exposed, but only one class', other than a `P` that the house rule reserves for structural half-presence.

### Answer 5: dependence and well-formedness problems noticed and not repaired

1. **`CN3` is collinear with `RB3` under ruling 1.** All 18 rulebooks with a substantive `RB3` are `CN3` = 1, and the nineteenth (A06, `RB3` `.NR` for want of a named object) is 1 on the same ground. The ruling makes `CN3` = 1 a function of 'security required'. On this population `CN3` adds no evidence beyond `RB3`, and a comparative claim counting both double-counts one clause.
2. **`RD-test` = `officers` and `LS3` = 1 rest on one clause in M08, M09, M10 and A06**, and `all-members` and `LS3` = 1 on one clause in M07. They should be declared a dependence group with scope over these rows if both characteristics are kept. Where the officers' membership is unknown (M06), the two separate (`officers` with `LS3` `.NR`), which is weak, not substantive, separation.
3. **The M08-M10 template and the Tokushima template are each one drafting source.** Any count over rulebooks (for instance 'officers in 4 of 11 in 1915') overweights them. That is a selection and dependence problem, not one of characteristic design, and it is not repaired here.
4. **`RB3` `mixed` is not well formed** (answer 4): one value records three different facts. Under `CHARACTER-CODING.md` test 1 this is a candidate for splitting. Per the protocol it is reported here with the colliding codings (M01, M08, T01) as evidence, not repaired in this batch.
5. **`LS1` and `RD-test`.** `LS1` was `.NR` in all 19, including the six rows where `RD-test` named a bearer. The 'how' question is not answered by any rulebook that answers the 'who', which is consistent with `RD-test` being a distinct construct. But with no instance of `fund`, the overlap `RD-TEST-DEFINITION.md` flags was not exercised.

### Answer 6: what to read next, and which cell it would move

1. **The Tokushima report's round-table on officers' liability and the 發起人** (S pp. 125, 144, `(三)發起人の地位` and `(八)講役員の責任其の他`, outside this test's list). It would show whether a shortfall on a drawer's small bills was borne by the bill-holders, the 抵當預リ人 or the organiser. As commentary it cannot itself fill a cell. But if it quotes a clause of any of T01-T03 it could move T01-T03 `RD-test` from `.NR`, and it would test decision 17.
2. **Any rule or record of the 中爪第二區衞生組合** (M07). Its size relative to the kō's 24 shares would move M07 `RD-test` between `all-members` and no fitting value, and M07 `LS3` with it.
3. **The membership of M02's 監督者 and M04's 世話人.** A member list printed with the rules elsewhere would move M02 `LS3` from `.NR` to 1 and settle M04 `LS3` at 1 or `.NR`.
4. **The Aomori report's 第三部 五 借用證書** (S p. 42, outside the list). It might print A05's referenced 連帶證書 or confirm the Aomori 借用證書 form. That would bear on A05 `RB3` (already surety) and could move A04/A05 `LS3` if it shows the sureties had to be members.
5. **The Okinawa report's 講元の責任** (S p. 183, outside the list). Relevant to M01-M03 (模合). If it quotes a 模合 rule naming the 講元 as bearer, it would bear on whether `officers` should have been expected there. It cannot move M01-M03, whose rules are silent.
6. **More rulebooks from outside both ministries' selections**, particularly ones with a reserve or a 積立金 expressly answering for defaults. That is the only way to get `RD-test` = `fund` or `deferred` an instance, and to exercise the `LS1` overlap.
