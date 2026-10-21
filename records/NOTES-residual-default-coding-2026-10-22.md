# Coding notes: `RD-test` and five characteristics on seventeen kō rulebooks

Test-table batch of 2026-10-22, coded by `claude-opus-5-5` at effort `high`, in the blind bundle `~/GitHub/_blind-residual-default-2026-10-22`. The priors were filled before any page was opened (`PRIORS-residual-default-filled-2026-10-22.md`, sha256 `0af1a13a9294615b9fd411ebf312b3697d3389881902f5505dd0cfed450ffe9a`) and committed by the maintainer as `d50331a` (reported to me as the push range `cca7bf6..d50331a`; I had no access to the live repository to check it). Nothing here enters `data.csv`.

**Ordering.** Every cell of a kō was fixed before the next kō was opened, in the order 6, 7, 12, 14, 15, 18, 21, 23, 25, 26, 27, 31, 33, 35, 37, 39, 43. No kō was compared with another, or with the existing `ko_*` rows, until all 102 cells were fixed, with **one exception, recorded in full in §1.4**: while coding 第十八講 I edited two already-fixed `CN3` cells and then reverted both to the values first fixed. The tables and the answers in §3–§4 were computed only after the last cell (第四十三講 `GV1`) was fixed. Cross-references inside cell notes to house practice (`ko_mitarai_mujin_1773`, `ko_mochiyori_yutsu_1876` and others) cite the definitions and the existing notes read before the source was opened, not comparisons of values.

**What I did not use.** No other website, no other NDL page or item, no search, no memory tool, no past-chat search, no Google Drive or connector. The source was read in Chrome through the two URL forms in `FRAMES.md` only (viewer and IIIF image service; in practice the IIIF service throughout).

**One editor.** All seventeen rulebooks were chosen, transcribed, annotated and anonymised by one ministry office (農林省經濟更生部), which also wrote every 解說 and footnote. Agreement between kō is therefore never treated as corroboration in this file. Several pairs come from one village or town: 第十四講 and 第十五講 (吉敷郡嘉川村), 第二十五講 and 第二十六講 (仙北郡千屋村), 第二十一講 and 第三十三講 (磐田郡富岡村), 第三十一講 and 第四十三講 (富士郡富士町), and 第七講 and 第三十五講 (宗像郡吉武村).

## 1. Reading record

### 1.1 Front matter (frames 2–6)

- **Frame 2.** Cover: 『頼母子講規約例』, 昭和十一年三月, 農林省經濟更生部, (農村金融資料第四號). Read at page resolution. The volume is dated March 1936 on its cover; `FRAMES.md` gives 昭和11–13 for the series entry.
- **Frame 3.** 凡例, six items, read before any rulebook and **re-read after all 102 cells were fixed** to transcribe it here, because my first-pass view of it was not retained verbatim. Transcribed as printed:
  - 一 本書は各地各風なる頼母子講の仕組に付其の事例の一班を示さんが爲め、秋田、靜岡、山口、福岡の四縣下より適當と認め得るもの四十三講を選び、其の規約（又は講則、規則、會則等）を收錄したるものなり。
  - 二 收錄の順序は大別して金錢出資講と米穀出資講に分ち夫々講の目的別に配列せり。
  - 三 規約の條文は判讀に難からざる限り原文を其の儘採錄し、特殊なる方言若しくは難解と認めらるる用語に付ては末尾に註を附して說明し、尙全文の意味を補足する爲め冒頭に解說を加へたり。
  - 四 若干のものに付ては規約末尾に借用證書、借入申込書等の書式例を添付せり。
  - 五 規約其の他に記載しありたる講親、世話人、其の他の姓名は凡て之を抹殺若しくは秘匿したり。
  - 六 本書に收錄したる頼母子講は二三のものを除き孰れも昭和十一年三月現に營講を續けつつあり。
- **What the 凡例 means for the coding.** (i) Selection is 適當と認め得るもの with no criterion stated: the seventeen are a sample of a sample, chosen by one office for reasons not given. (ii) Transcription is verbatim only 判讀に難からざる限り: where the original was hard to read, the printed text may be the editor's reading, and nothing marks where. (iii) Names are 抹殺若しくは秘匿: the personal names in headings and signatories (山野草平, 根津忠一郎, 甲野丙吉 and so on) are the editor's and are never evidence. (iv) The 解說 is the editor's 補足, which is why no cell rests on it. (v) The arrangement by 金錢出資講 / 米穀出資講 and by purpose is the ministry's class and was not used.
- **Frames 4–6.** Table of contents, read at page resolution for orientation. It lists all forty-three kō by number and name, including those not on the list; I used it for nothing beyond locating pages.

### 1.2 The seventeen kō, frame by frame

### 第六講 山野草平取建頼母子 (山口縣吉敷郡仁保村), printed pp. 15–18

- **Frame 14, left page (p. 15).** Read only the leftmost columns: heading 第六講, place (山口縣吉敷郡仁保村) and the first part of the 解說. The right two-thirds of p. 15 carry the end of 第五講 (a form headed 賴母子講金借用證書 or similar, and footnotes 1)–9)); I saw its layout at overview resolution only and did not read it. Right page of frame 14 (p. 14) not read: it is 第五講.
- **Frame 15, both pages (pp. 16–17).** Whole: rest of the 解說, 賴母子規約 第一條–第十九條 (to …除名ノ上掛金捨ノ).
- **Frame 16, right page (p. 18), right-hand columns only.** End of 第十九條, 第二十條, 以上, 追加 (昭和六年 resolution), and footnotes 1)–7). I stopped at the heading 第七講, which is on the list. Left page of frame 16 not read for this kō.
- **解說 facts used:** 講親 山野草平 a schoolteacher farming a few 反 with debts; kō 發起 by villagers in 明治四十四年 for 負債償還; running twenty-odd years with a few years to 滿會; one meeting skipped. The 解說 dates the skipped meeting 昭和七年十一月, the rules' 追加 heads the resolution 昭和六年十一年協議 (sic, presumably 十一月). The two do not agree on the year; recorded, not resolved.
- **Footnotes used:** 1) 子方は親に對する一般講員; 3) 發起人は講親に同じ; 5) 惣會員は總會員で講員一同のこと; 6) 後取は未取者; 7) 前取者は既取者. Footnote 4) refers to 第五講 (p. 13), which I did not follow.

### 第七講 昭和講 (福岡縣宗像郡吉武村), printed pp. 18–20

- **Frame 16, right page (p. 18), left-hand columns.** Heading 第七講 昭和講, place, and the first part of the 解說. The right-hand columns are the end of 第六講, already read for that kō.
- **Frame 16, left page (p. 19), whole.** End of the 解說, the 講則 (fifteen unnumbered 一、 items, cited below as 講則 item 1–15 in printed order), and footnote 1).
- **Frame 17, right page (p. 20), right-hand columns only.** Footnotes 2)–5). I stopped at the heading 第八講 大正合名賴母子講, which is **not on the list**; at overview resolution I saw that its heading, its 解說 and its 第一條 begin on the same page, and I did not read them. Left page of frame 17 (p. 21) not read; it belongs to 第八講.
- **解說 facts used:** organised 昭和三年の暮 for a 小作人 after a house fire and the death of the household head (the 講則 item 11 gives 昭和三年十二月二十五日); 掛金五圓 × 三十六口, so the 親's pot was 百八十圓; drawing by lot (抽籤法), which the 解說 calls rare for a credit kō.
- **解說 interpretation NOT used as evidence:** the 解說 says that 講クビリ means 連帶保證 or 部落保證, that the three 部落 猿田・高六上組・高六下組 are each one クビリ, and that 若し既取者にして返掛を怠り講事に云々を生ずる如き場合には各クビリの講員は、連帶してその責に任ずるものである, adding 講クビリの制度は福岡縣の賴母子講に於て、隨所に散見される. The rule itself is narrower (see `RD-test`). I code from the rule and record the 解說's reading as the ministry's.
- **Footnotes used:** 1) 支配人は世話人のこと; 2) 坐會 is held by day for members living far off in a kō spanning several 部落; 3) 「クビリ」に就ては解說を參照; 4) 子は未取者; 5) 「坐觸レ」は坐會の通知.

### 第十二講 春山夏助長壽講 (靜岡縣引佐郡井伊谷村), printed pp. 29–31

- **Frame 21, left page (p. 29), leftmost columns only.** Heading 第十二講 and place. The rest of p. 29 and all of p. 28 belong to 第十一講, which is **not on the list**; at overview resolution I saw that they hold numbered 條 and a 以上, and did not read them.
- **Frame 22, right page (p. 30), whole.** 解說, 總則 preamble, 第一條–第五條.
- **Frame 22, left page (p. 31), right-hand columns.** 第六條–第八條, 右講則依而如件, 昭和四年六月, the signatories (講主 春山夏助, 引受人 何某 and three 同, 講事世話人 何某 and further 同 何某, names suppressed per 凡例 五), and footnotes 1)–7). I stopped at the heading 第十三講 秋田實取建賴母子 (山口縣阿武郡佐々並村), **not on the list**, and read nothing of it beyond the heading and place, which fell inside my crop.
- **解說 facts used:** the 講親 春山夏助 is a 商業者, not poor, raising 一千圓 to build a house; 二十口 including the 親. The 解說's long passage on 親子割 (the bid discount returned to drawn and undrawn alike) concerns surplus, not loss.
- **Footnotes used:** 1) 講主は講親のこと; 2) 親掛とは既取者の返掛金にして子掛とは未取者の掛金; 3) 講主引受人は講親の保證人; 4) 立會 is the meeting; 5) 鬮出金は入札差金; 6) 親子割 returns the 入札差金 without distinction between drawn and undrawn; 7) 座料は講員懇親の席料.

### 第十四講 深井朝右衞門發起頼母子 (山口縣吉敷郡嘉川村), printed pp. 32–34 (FRAMES.md says 32–35)

- **Frame 23, right page (p. 32), leftmost columns only.** Heading 第十四講 and place. The rest of p. 32 is the end of 第十三講 秋田實取建賴母子, **not on the list**. A sliver of its last column fell inside my crop and I could not avoid reading it: 及有價證券其ノ他ハ規例ニヨリ總代會員ニ… (truncated). Nothing else of 第十三講 was read; not used.
- **Frame 23, left page (p. 33), whole.** 解說; 深井朝右衞門賴母子規約 第一條–第拾三條 (first sentence).
- **Frame 24, right page (p. 34), whole.** Rest of 第拾三條, 第拾四條, 第拾五條, the form 賴母子金借用證書 (signed 債務者 何某 to 賴母子惣代 何某殿), and footnotes 1)–10).
- **Frame 24, left page (p. 35).** Viewed at page resolution to find the end of 第十四講: the whole page belongs to 第十五講 (heading at the top right), so 第十四講 ends on p. 34. The 第十五講 columns were read for that kō, not this one.
- **解說 facts used:** 本講も親講ではあるにしても、講そのものゝ主たる目的は一般講員の金融と貯蓄に存する; the 講親 received 高金二百圓 at the first meeting and alone pays 一圓五十錢 interest per meeting on his return, which goes to the drawer of that round. No date of foundation is given in what I read; the form leaves 昭和 年 blank.
- **Footnotes used:** 1) 高金は給付金; 2) 取建親(とりたておや)は救濟を受くる講親のことで、既取人を次親(じおや)と呼ぶに對し…取建親は又發起親とも呼ばれる; 3) 入組者は講員、加入者のこと; 8) 既取者の掛增金なく、掛金二十圓だけを返掛する意; 9) 前取者は既取者即ち次親、後取者は未取者; 10) 棄金(すてきん)は入札差金に同じ.

### 第十五講 權田太郎兵衞發起頼母子 (山口縣吉敷郡嘉川村), printed pp. 35–38

- **Frame 24, left page (p. 35), whole.** Heading, place, 解說, 權田太郎兵衞發起賴母子規約書 第一條–第四條 (first sentence).
- **Frame 25, both pages (pp. 36–37), whole.** 第四條 (rest)–第二十二條, the subscription line (以下入組人氏名調印), the form 賴母子返掛借用證書 (債務者 and two 連帶保證人, 擔保物件, addressed to the 惣代人), footnote 1).
- **Frame 26, right page (p. 38), right-hand columns only.** Footnotes 2)–9). I stopped at the heading 第十六講 大島長次郎發起共榮講 (山口縣佐波郡…), **not on the list**; its heading, place and the first words of its 解說 were visible at overview resolution and were not read. Left page of frame 26 not read.
- **解說 facts used:** two pots per meeting from the second meeting; at the first the 講親 alone receives two 口 (一千九百二十圓); 一般講員は返掛無利息なるに對し講親は一割の利息を附せられてゐる. The 解說 cross-refers to 第六講 (かゝる仕組は第六講にも記した如く), and footnote 2) to 第十四講. **Same village as 第十四講** (嘉川村; the rules restrict pledged land to 嘉川村、井關村 and transfers to 嘉川村ノ在住ノモノ). Two kō from one village, chosen and annotated by one editor, are not independent witnesses to anything they share.
- **Footnotes used:** 2) 取建親は講親のこと; 3) 次親は既取者のこと; 4) 入組全員は加入者全員; 6) 地價は法定地價 (refers to 第五講, not followed); 7) 既取未取を論ぜずの意; 8) 持口の讓渡をいふ; 9) 子方はここでは講員の意.

### 第十八講 山坂昇講 (福岡縣糸島郡深江村), printed pp. 51–52

- **Frame 32, left page (p. 51), left-hand columns.** Heading, place, 解說, 山坂昇講々則 items 1–6. The right-hand columns of p. 51 and all of p. 50 belong to 第十七講, **not on the list**; at overview resolution I saw that they hold footnotes and two registration-type documents (登記濟 stamps, 抵當權者 何某 lines), and did not read them.
- **Frame 33, right page (p. 52), right-hand columns.** 講則 items 7–8, the schedule of deductions, footnotes 1)–6). I stopped at the heading 第十九講 紀念講, **not on the list**; its heading and place were visible at overview resolution and nothing of it was read. Left page of frame 33 not read.
- **解說 facts used:** 十圓掛、六十口, pot 六百圓; the 講親 is a 漁業者 raising money for nets, but 主目的は講員相互の金融; the 親's 返掛金及び抵當物件は一般講員と同然の取扱ひをうけてゐる; founded 大正十五年; **深江村の賴母子講整理の折整理されて現在は營まれてゐない** — one of the 凡例's 二三 exceptions: not running in 1936.
- **Footnotes used:** 1) 株數は口數; 2) 銀座(ぎんざ)とは世話人或は役員のこと; 3) 割取は奬勵金; 4) 取當金は落札金; 5) 掛戾金は返掛金即ち償還金; 6) 盛料は席料.
- Items are unnumbered 一、; cited as 講則 item 1–8 in printed order (item 8 is the deduction schedule).

### 第二十一講 共同信用講 (靜岡縣磐田郡富岡村), printed pp. 57–59

- **Frame 35, left page (p. 57), left-hand columns.** Heading, place, 解說 (first part). The right-hand columns of p. 57 and all of p. 56 belong to 第二十講, **not on the list**; at overview resolution I saw numbered 條, a 會計 heading, signatory lines (保證人 何某) and footnotes, and did not read them.
- **Frame 36, right page (p. 58), whole.** End of the 解說, 富岡村共同信用講事會則 (seven 一、 items, each with a heading word: 名稱, 立會, 掛金, 立會ノ座料, 鬮取方法, 落札金預リ方法, 花割方法), 右會則如件, and the form 講金預リ證書.
- **Frame 36, left page (p. 59).** My crop was too wide: besides 第二十一講's footnotes 1)–4) it took in the heading, place and 解說 of **第二十二講 無願主講 (山口縣玖珂郡日積村), not on the list**, and the first item of its rules. **Read by accident:** its 解說 says it is a 親無講, 延滯者の處置、抵當差入等仲々嚴重を極めてをり, opened 大正十四年, and that 親無講 are rare in 山口縣; its first rule fixes the drawer by lowest bid. Not used for anything.
- **解說 facts used:** a 親のない金融講 whose members include 農業者, 商業者, 公務業者; it has 親子割 and a 花割 prize-lottery; 昭和七年以來本講も年回數三回を二回に減じ、從つて滿會までの期限が延長した (the 會則 still says three meetings a year). The form's term runs to 昭和拾壹年拾月. No foundation date is stated.
- **Footnotes used:** 1) 立會 is holding the meeting; 2) 親子割 returns the bid discount to drawn and undrawn alike — 第十二講解說(三〇頁)を見よ — here by dividing the 手取金 by heads from the outset; 3) 花割は花籤とか奬勵金に同じ; 4) the 花籤金 is collected outside the 講金.

### 第二十三講 昭和御大典記念講 (福岡縣築上郡東吉富村), printed pp. 61–64

- **Frame 37, left page (p. 61), left-hand columns.** Heading, place, 解說 (first part). The right-hand columns of p. 61 and all of p. 60 belong to 第二十二講, **not on the list** (already glimpsed by accident at p. 59, see 第二十一講); at overview resolution I saw that they hold its numbered 條, a form and signatories, and did not read them.
- **Frame 38, both pages (pp. 62–63), whole.** End of the 解說; 昭和御大典記念講規程 第一條–第二十一條; 昭和三年九月二十日決定.
- **Frame 39, right page (p. 64), right-hand columns only.** Footnotes 1)–4). I stopped at the heading 第二十四講 農友親睦講 (秋田縣…), **not on the list**; its heading, 解說 and first 條 were visible at overview resolution and were not read.
- **解說 facts used:** set up at the 御大典 (the 規程 is dated 昭和三年九月二十日決定); recruitment began in 大字直江 and widened to neighbouring 部落; 講員數六十名、講口數八十口; pot 千六百圓; meetings in the 直江公會堂.
- **Footnotes used:** 1) 掛金は未取者の掛金、掛戾金は既取者の返掛金; 2) 間際金 is the excess of a re-auction's proceeds over the first auction's (cross-reference to 第八講, not followed); 3) members who lose their 花籤 right through 掛金不掛 etc.; 4) 未取者がその持口を讓り若しくは落札者がその講金取得權を讓ること.

### 第二十五講 親睦講 (秋田縣仙北郡千屋村), printed pp. 65–68

- **Frame 39, left page (p. 65), left-hand columns.** Heading 第二十五講 親睦講 and place only; the page carries nothing else of this kō. Its right-hand columns are the end of 第二十四講 農友親睦講, **not on the list**; one line fell inside my crop and was read: 第拾壹條 會場ハ取主ノ家宅トス, and a footnote 6) 入札權もしくは落札權の讓渡. Not used. Right page of frame 39 (p. 64) was read only for 第二十三講's footnotes; the middle of that page is 第二十四講 and was seen only at overview resolution.
- **Frame 40, both pages (pp. 66–67), whole.** 解說; 親睦講規約 (unnumbered 一、 items, cited below as 規約 item 1–8 in printed order; the 藏元ノ任務 that follow item 8 are cited as 藏元ノ任務 (1)–(4)); footnotes 1)–3).
- **Frame 41, right page (p. 68), right-hand columns only.** Footnote 4). I stopped at the heading 第二十六講 正利講親無金無盡, which is on the list and is read under that kō.
- **The kō's word for the draw is 諍** (諍下, 諍引, 諍取者), checked at higher magnification on p. 67; quoted as printed.
- **解說 facts used:** 親無講にして金融と親睦を兼ねたる無盡講; 世話人 paid 五十錢 a 口; draws are bid orally in 五十錢 steps; 本講は昭和十年既に滿會すべき筈の講であつたが、どういふ理由か二回休會せることあり、從つて滿會は昭和十二年の豫定 — still running. The rules date the kō 大正四年二月十日創立.
- **Footnotes used:** 1) 一株は一口; 2) 藏元は世話人又は講元; 3) 地價は法定地價 (refers to 第五講, not followed); 4) 既取者返掛を怠り訴訟沙汰となつた場合、これに要する費用は該既取者の負擔であるは勿論だが、裁判終了まで諸費用は一時講員一同が立替へる.

### 第二十六講 正利講親無金無盡 (秋田縣仙北郡千屋村), printed pp. 68–70

- **Frame 41, right page (p. 68), left-hand columns.** Heading, place, 解說, 正利講親無金無盡總則, 規約 第一–第三. (The right-hand columns are 第二十五講's footnote 4), read for that kō.)
- **Frame 41, left page (p. 69), whole.** 規約 第四–第十四; the form 正利講金借用證書 (寫), beginning.
- **Frame 42, right page (p. 70), right-hand columns.** End of the form (dated 大正 年十二月二十五日, 千屋村浪花 借主 何某, 連帶保證人 何某, addressed to 藏元 何某殿) and footnotes 1)–7). The left-hand columns of p. 70 begin 第二十七講, which is on the list and is read under that kō.
- **Same village as 第二十五講** (千屋村). Two rulebooks from one village, chosen by one editor: not independent witnesses to anything they share.
- **解說 facts used:** a kō for buying 家財什器: the drawer must spend the pot, 世話人と相談の上, on some memorable object, so that 實質に於て物品給付無盡に近い形; 親無講; draws by oral bidding; 昭和十一年末滿會の豫定 — running in 1936. The payout is money, so it creates a debt; the in-kind purpose does not make RD-test inapplicable.
- **Footnotes used:** 1) 藏元は講元の義で役員又は世話人; 2) 連中は加入者のこと; 3) 壹期は開講一回; 4) 前取主(まへどりぬし)は既取人; 5) 末(すゑ)は未取人; 6) 連中開濟の保證人は、加入者その人物を知り、これならばといふ保證人; 7) 講中は連中と同じく加入者.
- 規約 articles are printed 第一、第二 … 第十四 without 條; cited as printed.

### 第二十七講 蒲團講 (靜岡縣庵原郡小島村), printed pp. 70–72

- **Frame 42, right page (p. 70), left-hand columns.** Heading, place, first part of the 解說. The right-hand columns are 第二十六講 (read for that kō).
- **Frame 42, left page (p. 71), whole.** Rest of the 解說; 蒲團講々則 第一–第八; footnotes 1)–2).
- **Frame 43, right page (p. 72), right-hand columns.** Footnotes 3)–4). **Read by accident:** my crop of p. 72 rendered the whole page, which carries the heading and 解說 of **第二十八講 直江共同馬講 (福岡縣築上郡東吉富村), not on the list**. Before I recognised the heading I had taken in that its 解說 describes a 親無講 of 二十七名、三十一口 for buying 役馬, with draws by lot and payment also on a horse's death. I read no rule of it. Not used. Left page of frame 43 (p. 73) not read for this kō; at overview resolution it carries the end of 第二十八講 and the heading of 第二十九講, neither on the list.
- **解說 facts used:** a kō of women (村の主婦や處女會員) for buying bedding; pot 六十三圓; 會員二十四名で口數二十一口, six holding half-shares; drawn members pay 一圓 interest a meeting thereafter (大掛四圓); the 親 takes the first pot but is 所謂救濟される親ではなく、むしろ會員の世話役. Whether the pot must be spent on bedding is, says the 解說, left to the member. No date of foundation and no statement whether it was still running.
- **Footnotes used:** 1) 會主は講親; 2) 小掛(こがけ)は未取人の掛金、大掛(だいがけ)は既取人の返掛金; 3) 抽籤に依りて當籤者即ち取得者を定むる意; 4) 未取人既取人を問はず平均割とす、親子割に就ては第十二講解說(三〇頁)參照 (cross-reference not followed).

### 第三十一講 富士石碑講 (靜岡縣富士郡富士町), printed pp. 76–79

- **Frame 45, right page (p. 76), left-hand columns.** Heading, place, 解說 (first part). **Read by accident:** my crop began a few columns too far right and took in the last lines of **第三十講 (not on the list)**: the close of a 連帶借用證 (…壹回ニ付金五圓也拂込ノ約定但シ年利息 / 右前記約定ヲ以テ借用候處實正也然ル上ハ本講則ニ準據シ毛頭違背不仕萬一聊タリトモ不履行ノ場合ハ該講則ニ依リ御處理相成候共毛頭異議無之候依而連帶借用證一札如件) and its footnotes 1)–3) (講步 = 花籤; 盛月/盛方; 掛戾し = 既取人の返掛). Not used. The rest of p. 76 and p. 75 belong to 第三十講 and were seen only at overview resolution.
- **Frame 45, left page (p. 77), whole.** Rest of the 解說; 講則 第一條–第七條 (first sentence).
- **Frame 46, right page (p. 78), whole.** 第七條 (rest)–第十七條, 右條項嚴守スルコト.
- **Frame 46, left page (p. 79), right-hand columns.** The form 割濟金連帶借用之證 (連帶借用主 and two 同, addressed to 何某殿) and footnotes 1)–6). I stopped at the heading 第三十二講 觀音堂修繕講 (靜岡縣富士郡富士町), **not on the list**, and read nothing of it beyond heading and place.
- **解說 facts used:** a 物品給付無盡: the drawer receives not cash but a stone monument for his family grave, built by the 會主, a 石屋 (stonemason), to whom the 世話人 pay the pot; the 會主 hosts and runs the meetings but, says the 解說, holds no share (講に一つの持口を有するでもなく) and is 一種の講管理者; 出金花 for the first three meetings is 事ある場合の訴訟費用として積立て. The rules date the kō 自昭和九年十月至昭和十三年五月迄 (第五條), so it was running in 1936.
- **Footnotes used:** 1) 會主に就ては解說參照; 2) 豫め集金せずその場掛け; 3) 未取人の入札權、落札人の落札權等の賣買讓渡; 4) 大掛(だいがけ)は既取人の返掛; 5) 掛戾金は返掛金; 6) 未取者の持口を他に賣ること、小掛者は未取者で大掛者に對する語.
- My prior expected this kō to be the likeliest `.NA` (a purpose kō with no payout to members). It is not: the stele is a payout in kind, and the drawer owes 掛戾金 for it.

### 第三十三講 加茂川原昭和講 (靜岡縣磐田郡富岡村), printed pp. 81–82 (FRAMES.md says 81–83)

- **Frame 47, left page (p. 81), left half.** Heading, place, 解說, 加茂川原昭和講會則 items 1–5. **Read by accident:** my first crop took in the last lines of **第三十二講 觀音堂修繕講, not on the list**: the end of a footnote (…ただ親の掛金は觀音堂がなすのでなく、毎回の落札者が受持つといふのである) and footnotes 3) 大掛は既取人の返掛、大掛者は既取人 and 4) 立會は講の會同. Not used. The right half of p. 81 and all of p. 80 belong to 第三十二講 and were seen only at overview resolution.
- **Frame 48, right page (p. 82), whole.** 會則 items 6–11 and the closing line 以上各自承諾ノ上加盟セルモノトス; the form 年賦金借用證書; footnotes 1)–4).
- **Frame 48, left page (p. 83).** I looked for the form's signatories and found none: the page opens with the heading of **第三十四講 中央實行組合共同作業場講 (靜岡縣引佐郡井伊谷村), not on the list**, so 第三十三講 ends on p. 82. **Read by accident** in that crop: the first lines of its 解說 (a kō of 七十餘名 of the 井伊谷中央實行組合, 六十口 split into three 組 of 二十口, 半口持四十名). Not used.
- **Same village as 第二十一講** (富岡村). Not independent of it as evidence of anything they share.
- **解說 facts used:** a kō for building 納屋、物置 run under the 加茂川原煙草耕作組合; members are 組合員 of the district; no 講親, no pay for the 世話人; 掛金十五圓、口數二十口, pot 三百圓; 設立は昭和二年で年二回の開會. The 會則 run it 昭和貳年貳月ヨリ昭和拾壹年拾壹月迄, so it was in its last year in 1936.
- **Footnotes used:** 1) 本講は目下のところ一組しかない (cross-references to 第三十四講 and 第四十一講, not followed); 2) 立會(りつくわい)は講の會同; 3) 參回糶 is three successive rounds of bidding; 4) 糶金(せりきん)は入札差金.
- 會則 items are unnumbered 一、; cited as 會則 item 1–11 in printed order.

### 第三十五講 吉武信用貯金講會 (福岡縣宗像郡吉武村), printed pp. 85–95 (FRAMES.md says 85–96)

- **Frame 49, left page (p. 85).** Heading, place, 解說 (first part). **Read by accident:** my crop's right edge took in the last two lines of **第三十四講 (not on the list)**: an addressee line 講事世話人 殿 and its footnote 3) 座料は講會々座の諸費用. Not used. The right page of frame 49 (p. 84) belongs to 第三十四講 and was seen only at overview resolution (a 年賦金借用證書 with signatory lines).
- **Frame 50, right page (p. 86).** End of the 解說.
- **Frame 50, left page (p. 87).** Cover of the 吉武信用貯金講會通帳 (form, 表); 吉武信用貯金講會規則 第一條–第二條.
- **Frame 51, right page (p. 88).** 規則 第三條–第十一條.
- **Frame 51, left page (p. 89).** 規則 第十二條–第十四條; the passbook grid begins (會番 / 第一小會 … 第六本會).
- **Frames 52 and 53 right (pp. 90–92).** Passbook grids only, read at page resolution; they carry no clause.
- **Frame 53, left page (p. 93).** 吉武信用貯金講會規則左記各條ヲ變更訂正ス: amended 第二條, 第三條, 第四條, 第五條, 第九條; 以上變更條項ハ昭和九年二月八日ヨリ實施.
- **Frame 54, both pages (pp. 94–95).** 吉武信用講借入並ニ使途申込書 (with a box 査定委員認印); 金借用證書 items 一–九, signatories (借主 and six 連帶保證人); footnotes 1)–5).
- **Frame 55, right page (p. 96).** Seen at overview resolution only, to find where 第三十五講 ends: the page opens with the heading of **第三十六講 相互救濟講**, not on the list, so 第三十五講 ends on p. 95. Nothing of 第三十六講 was read.
- **Which text governs.** The 規則 of pp. 87–89 as amended on p. 93. The 解說 says it describes the amended text (この解說は變更後現に行はれつゝあるものに就いての解說). Where an article was amended I cite the amended text and say so; 第六條–第八條 and 第十條–第十四條 are unamended.
- **解說 facts used:** a kō 吉武信用組合と緊密な關係に置かれる, but 獨立の全く別個のもの; open to 組合員 and their families and other village residents; members are mostly indebted to the 組合 and the kō's purpose is the 回收 of the 組合's 固定貸付; the 組合 grants 年額五十圓 for expenses; 豫定年限昭和八年九月より昭和十六年十二月まで; 講員數は百五十八人、全部持口は一口; 實際には概ね部落保證を徵してゐる (an interpretive statement about practice, **not** used as evidence for any cell).
- **Footnotes used:** 1) 掛込金 is the undrawn member's instalment, 掛戻金 the drawn member's repayment; 2) 取親(とりおや)は又單に親とも云ひ、既取者の意; 3) 地價は法定地價 (cross-reference to 第五講, not followed); 5) 滿座は滿會.

### 第三十七講 岡龍無盡 (秋田縣由利郡平澤町), printed pp. 97–99

- **Frame 55, right page (p. 96).** Not read: it is 第三十六講 相互救濟講, not on the list (heading and 解說 seen at overview resolution only, while locating the end of 第三十五講).
- **Frame 55, left page (p. 97), whole.** Heading, place, 解說, 無盡會則 第一條.
- **Frame 56, right page (p. 98), whole.** 第二條–第十四條.
- **Frame 56, left page (p. 99), right-hand columns.** 第十五條–第十七條; the form 玄米借用證 (落取主, 保證人, 同); footnotes 1)–10). I stopped at the heading 第三十八講 桝尾源太取建賴母子 (山口縣吉敷郡仁保村), **not on the list**, which fell inside my crop; nothing of it beyond heading and place was read.
- **解說 facts used:** a 米無盡 raised 昭和三年 for the relief of the 講親 岡村龍藏, a 小作農 with a large family whose household head had died; 六十六名, mostly village residents with some ten relatives from outside; 口數六十八口; contributions are 粳玄米三等四斗入一俵 a head, lodged in the 平澤農業倉庫 and brought to the meeting as 入庫票; bids are in rice. No statement whether it was still running in 1936; at one meeting a year (第二條) and sixty-eight 口 it would have been.
- **Footnotes used:** 1) 座掛は會座の節その場で掛米すること; 2) bids are by 捨米, lowest net take wins; 3) 返掛米十俵に對し法定地價五圓 (cross-reference to 第五講, not followed); 4) 「掛詰メ米」は未取人の掛込米; 5) 宿合力は會席 (cross-reference to 第二講, not followed); 6) 「鬮餘り米」は數回糶りたる後の殘餘; 7) 未取者既取者に拘らず; 8) the last drawer receives 七割五分 of the total; 9) transfer of an undrawn share to an outsider is allowed with the 連中's consent; 10) 宿保證人は講親保證人をいふ.

### 第三十九講 根津忠一郎企米無盡 (秋田縣鹿角郡曙村), printed pp. 105–107

- **Frame 59, left page (p. 105), left-hand columns.** Heading, place, 解說 (first part). The right-hand columns of p. 105 and all of p. 104 belong to 第三十八講, **not on the list**; at overview resolution I saw footnotes and two small forms (a 入札 slip, a 式樣), and did not read them.
- **Frame 60, right page (p. 106), whole.** End of the 解說; 米積立無盡會規約 第一條–第九條.
- **Frame 60, left page (p. 107), right-hand columns.** 第十條; date 大正十一年十一月; signatories 企人 根津忠一郎 and 藏元 國野軍治 (names as printed; the 凡例 says names are altered); footnotes 1)–9). **Read by accident:** my crop took in the heading of **第四十講 八田九郎發起米賴母子 (山口縣吉敷郡嘉川村), not on the list**, and the first two lines of its 解說: 本講は八田九郎の發起せる親賴母子であるが、併し親の特典薄く、その意味で親救濟よりも一般講員の金融に重點を置く講と見做すのが至當であらう。本講は親とも十六口、昭和九年の設立で…. Not used.
- **解說 facts used:** raised by the 講親's relatives in and out of the village to fund the 講親 根津忠一郎's new house; 大正十一年の設立 (the 規約 is dated 大正十一年十一月); 四十口; nominally four meetings a year, in practice two days with two sessions each, and 過去に於て休會の回數多く. Whether it was running in 1936 is not stated.
- **Footnotes used:** 1) 積立米は給付米; 2) 株數は口數; 3) tie-break procedure for bids; 4) 企人(くわだてにん)は講の設立者の意から轉じて講親のこと; 5) 藏元(くらもと)は役員、世話人; 6) if the first bidder is disqualified the second receives at the first's price; 7) 鬮取人は、こゝでは既鬮取人即ち既取人の意; 8) 生株者とは未取者のこと; 9) 未取者の持口即ち入札權.

### 第四十三講 愛宕社講 (靜岡縣富士郡富士町), printed pp. 117–119

- **Frame 65, left page (p. 117), left-hand columns.** Heading, place, 解說. The right-hand columns of p. 117 and all of p. 116 belong to 第四十二講, **not on the list**; at overview resolution I saw numbered 條 (to 第二十一條) and a footnote, and did not read them.
- **Frame 66, right page (p. 118), whole.** 目的; 講則 第一條–第十條; 附則; 右大正五年十一月; the form 割濟米連帶借用之證 (beginning).
- **Frame 66, left page (p. 119), whole.** End of the form (連帶借用主 three lines, addressed 救濟米掛講世話人御中 — the form's addressee names the kō differently, recorded as printed), footnotes 1)–6). Nothing follows on the page; this is the last kō in the volume as far as the frames list goes.
- **Same town as 第三十一講** (富士町). Not independent of it as evidence of anything they share.
- **解說 facts used:** a 部落單位 kō whose purpose is the upkeep of the shrine; members, drawn and undrawn alike, give 一口一升 of rice to the 愛宕社 at each meeting, which the shrine keeps as a fund for repairs after 滿會; 掛米 is 一口につき玄米四斗入一俵; 大正五年の設立 (the 講則 are dated 大正五年十一月); 凶作その他の事由で屢々休會し滿會は相當延期する見込み — still running in 1936, behind schedule; 割濟米 is rice repaid in instalments.
- **Footnotes used:** 1) 大掛は既取人、小掛は未取人; 2) 精米は玄米の意味、白米ではない; 3) 立會スル is to hold the meeting; 4) 「最低ノ一本籤」は手取米最低の者一人を落札とすること; 5) 連名は加入者の意; 6) 講員名簿記載順.
- My prior expected a shrine as organiser or beneficiary with a GV1 gap. The shrine is a beneficiary of a levy (第三條), not the organiser, and the drawn pot goes to members.

### 1.3 Text outside the list seen by accident

Collected from §1.2, so that the maintainer can see it in one place. None of it was used for any cell.

- **第五講** (p. 15, frame 14): layout of a form and footnotes 1)–9), at overview resolution only.
- **第八講 大正合名賴母子講** (p. 20, frame 17): heading, and the existence of a 解說 and 第一條 on the same page, at overview resolution.
- **第十一講** (pp. 28–29, frame 21): numbered 條 and a 以上, at overview resolution.
- **第十三講 秋田實取建賴母子** (p. 31 heading and place; p. 32 one truncated column: 及有價證券其ノ他ハ規例ニヨリ總代會員ニ…).
- **第十六講 大島長次郎發起共榮講** (p. 38): heading, place, first words of the 解說, at overview resolution.
- **第十七講** (pp. 50–51): footnotes and two registration documents, at overview resolution.
- **第十九講 紀念講** (p. 52): heading and place.
- **第二十講** (pp. 56–57): numbered 條, a 會計 heading, 保證人 lines, at overview resolution.
- **第二十二講 無願主講** (p. 59): heading, place, 解說 (親無講, 延滯者の處置、抵當差入等仲々嚴重を極めてをり, 大正十四年 opening, 親無講 rare in 山口縣) and its first rule (lowest bid takes the pot). Read, not used.
- **第二十四講 農友親睦講** (pp. 64–65): heading and first 條 at overview; one line read: 第拾壹條 會場ハ取主ノ家宅トス, and footnote 6) 入札權もしくは落札權の讓渡.
- **第二十八講 直江共同馬講** (p. 72): heading and 解說 (親無講, 二十七名、三十一口, buying 役馬, lots, payment also on a horse's death). Read, not used.
- **第二十九講** (p. 73): heading at overview resolution.
- **第三十講** (p. 76): the close of a 連帶借用證 (…萬一聊タリトモ不履行ノ場合ハ該講則ニ依リ御處理相成候共毛頭異議無之候…) and footnotes 1)–3) (講步 = 花籤; 盛月/盛方; 掛戾し = 既取人の返掛). Read, not used.
- **第三十二講 觀音堂修繕講** (pp. 79, 81): heading and place; the end of a footnote (…ただ親の掛金は觀音堂がなすのでなく、毎回の落札者が受持つといふのである) and footnotes 3)–4). Read, not used.
- **第三十四講 中央實行組合共同作業場講** (pp. 83–85): heading, place, first lines of the 解說 (七十餘名 of the 井伊谷中央實行組合, 六十口 in three 組 of 二十口, 半口持四十名); an addressee line 講事世話人 殿 and footnote 3) 座料は講會々座の諸費用. Read, not used.
- **第三十六講 相互救濟講** (p. 96): heading and 解說 at overview resolution.
- **第三十八講 桝尾源太取建賴母子** (pp. 99, 104–105): heading and place; footnotes and two small forms at overview resolution.
- **第四十講 八田九郎發起米賴母子** (p. 107): heading, place, two lines of 解說 (親賴母子, 親の特典薄く, 親とも十六口, 昭和九年の設立). Read, not used.
- **第四十二講** (pp. 116–117): numbered 條 to 第二十一條 and a footnote, at overview resolution.

### 1.4 Process incidents

- **Ordering incident during 第十八講.** While coding 第十八講 CN3 I re-read the house rule in ko_mitarai_mujin_1773 CN3 (a pledge with no sanction clause is .NR) and saw that my already-fixed CN3 cells for 第七講 (=1) and 第十二講 (=1) had rested on bond-plus-surety instruments with no clause stating a consequence for the defaulter. I edited both cells (第七講 to P, 第十二講 to .NR), then recognised that this broke the rule that a kō's cells are fixed before moving on, and **reverted both edits to the values first fixed**, before coding anything further. No other cell was touched. The values in the table for 第七講 CN3 and 第十二講 CN3 are therefore the values fixed when those kō were coded. The inconsistency is reported, not repaired, in answer 5. 第十八講 CN3 was coded on its own merits against the definition and the ko_mitarai_mujin_1773 note, not by matching my earlier cells.

- **Browser disconnect.** During 第二十三講 the browser extension dropped once; I reconnected to the same tab and resumed at the same frame. No page outside the list was opened in the interval.
- **凡例 re-read.** Frame 3 was re-read after all cells were fixed (§1.1). Frame 3 is on the list, and re-reading it changed no cell.

## 2. Cells, decision points and `.NR` arguments, by kō

Every cell, with the clause it rests on in its original script, the alternative reading where there is one, and for each `.NR` what was read and found silent. The same text is in the `notes` column of the table.

### 第6講 山野草平取建頼母子 (山口縣吉敷郡仁保村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 16–18, 第六條, 第十八條–第二十條, 追加). Silent beyond the drawn member's own security. A payout does create a debt (第五條 子方ノ返掛ハ毎會金參拾圓ニ利子金參圓ヲ附シ將來返掛スルモノトス; 第四條 for the 發起人), so the cell applies and is not .NA. The security is 抵當 plus 保證人貳名 (第六條), which is RB3's ground (rule 1). Nothing names a bearer once 抵當 and 保證人 fail. Three clauses could be mistaken for one and are not: (i) 第十九條 後取者ニシテ掛金ノ不埒ノ節ハ除名ノ上掛金捨ノ事 is an unwon member's default, CN3's ground under rule 5; (ii) 第十八條 此賴母子滿會前ヨリ利子相增シ高金壹千拾圓ヲ取除ケ殘リノ金員ハ親ヲ除キ子方惣割ノ事 divides a SURPLUS among the 子方, not a loss; (iii) 第二十條 右規約將來故障事項差起リタル時ハ協議ノ上之ヲ變更スルコトヲ得 is a general amendment power for any 故障, not an instruction that the members will decide who bears an unpaid residue. ALTERNATIVE READING, stated fairly: 第二十條 could be read as `deferred`, since a drawn member's unpaid residue is plainly a 故障事項 and the remedy is 協議. Rejected because `deferred` asks whether the instrument says the members will decide THIS question, and a general amendment clause says only that the rules can be changed. If the maintainer reads general 協議 clauses as `deferred`, this cell moves.

- **`RB3` = `mixed`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 16–17, 第六條–第七條). Property and surety together. 第六條 返掛證書ハ普通賴母子證書ニシテ抵當ハ左ノ三種トシ、保證人貳名相立テ會日ノ五日前惣代人ニ照會シ賴母子惣代人ニ宛テタル證書ヲ認メ登記濟ノモノタルコト, the three 抵當品 being 一、田地ナレバ小作米參石貳斗カ地價ナレバ二掛ケトス / 一、公債證書ナレバ返掛高ノ七掛トス / 一、山林、畑、宅地其他ハ協議ニ附スベシ, with 但シ該抵當品書入ニ就テハ年ヲ經ルニ從ヒ協議ノ上變更スル事ヲ得. Registration is required (登記濟ノモノ), and 第七條 puts the 登記所 fee (金五拾錢) on the 負債主. `mixed` here carries both mixtures the ko_mitarai_gin_1805 note warns of: several kinds of property (land, public bonds, forest/fields/house-plots) AND property plus two sureties.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 16–18, 第一條–第二十條, 追加). No rule distributes an unmet loss. The only distribution rule is 第十八條 此賴母子滿會前ヨリ利子相增シ高金壹千拾圓ヲ取除ケ殘リノ金員ハ親ヲ除キ子方惣割ノ事, which divides an accumulated SURPLUS among the 子方 excluding the 親; reading it as the loss rule would turn a surplus clause into a loss clause. Silence, not absence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, pp. 16–17, 第五條–第七條). Coded on HOUSE PRACTICE, and the definition strains under it. Once he draws, a 子方 owes 返掛 of 參拾圓 plus 利子金參圓 a meeting (第五條), secured by registered 抵當 and 保證人貳名 (第六條 返掛證書ハ普通賴母子證書ニシテ抵當ハ左ノ三種トシ、保證人貳名相立テ…登記濟ノモノタルコト). His land or bonds answer for the debt, which is how ko_mitarai_mujin_1773 and ko_mitarai_hanei_1840 were coded LS3=1 ('Property answering for the debt is exposure beyond what has been paid in'). Against it: the definition says beyond what he has contributed OR AGREED TO CONTRIBUTE, and the 返掛 is exactly what he agreed to contribute; on that reading the cell is .NR, because no clause exposes him beyond his own 返掛. Medium and analyst-imposed for that reason; the tension is raised in answer 5.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 16–18, 第六條, 第十條, 第十九條). Compellable on both sides of the draw. Drawn members: registered 抵當 and 保證人貳名 (第六條). Unwon members (rule 5 of RD-TEST-DEFINITION, recorded here): 第十九條 後取者ニシテ掛金ノ不埒ノ節ハ除名ノ上掛金捨ノ事 — expulsion and forfeiture of what he has paid in. Lateness is fined: 第十條 掛金ハ各自持寄ニシテ午後三時ヲ經過スルトキハ會席妨料トシテ金參拾錢ヲ出スベシ. Not P: unlike ko_usui_bango_1822, the sanction is not limited to forfeiture of the draw.

- **`GV1` = `collective`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 17–18, 第十條, 第十二條, 第十五條–第十七條, 第二十條). Officers are chosen by and from the whole membership and the open questions go to 協議. 第十五條 本會ヲ整理スル爲メ役員貳名ヲ置ク、但シ惣會員中ヨリ互選セルモノヲ惣代人トシ後取中ヨリ互選セルモノヲ證書保管人トス (footnote 5: 惣會員は總會員で講員一同のこと); penalty money 協議ノ上處分スルモノトス (第十條 但書); the rules themselves 協議ノ上之ヲ變更スルコトヲ得 (第二十條); the 昭和六年 suspension was 協議ノ結果 (追加). The 發起人 (= 講親, footnote 3) has only the duty of notice (第十一條) and his own 返掛 (第四條); the 惣代人 has discretion over a week's postponement (第十二條). ALTERNATIVE: house practice codes .NR where a beneficiary-convener sits beside officers (ko_mochiyori_yutsu_1876, ko_usui_bango_1822). Not followed here because these rules give the convener no decision power over the fund and vest it in elected officers and 協議. Medium: 協議 never names its participants.

### 第7講 昭和講 (福岡縣宗像郡吉武村)

- **`RD-test` = `standing-subgroup`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 19, 講則 items 6, 7, 8). The rule names a group fixed in advance by the rules and liable by belonging. 講則 item 6: 一、時間內掛金不足ノ際ハ講クビリヨリ立替ヘルコト / 但シ猿田一クビリ、高六上組一クビリ、高六下組一クビリト定ム. The クビリ are the three 部落 of the kō, so liability attaches by residence, not by signature, which is the rule-1 test for `standing-subgroup`. Why it reaches a DRAWN member's default: item 7 provides separately for the 子 (footnote 4: 子は未取者), 一、子ノ時間內掛金不足ノ際抽籤除ケトス, so item 6 is the provision that covers a 既取者's unpaid 返掛. Three reasons for medium rather than high: (i) item 6 says 立替ヘル, to advance, and names no further bearer, so the クビリ is the last bearer the instrument NAMES (rule 2) but the text does not say it bears the loss finally rather than advancing it against recovery; (ii) item 6 does not say in words that the defaulter's OWN クビリ advances, although dividing the kō into three クビリ makes no sense otherwise; (iii) the order against the drawer's own security (the 連帶借用證書 of item 8) is not stated: item 6 operates at the meeting, before any security could be realised. The 解說's stronger reading (既取者 … 返掛を怠り … 各クビリの講員は、連帶してその責に任ずる) agrees but is the ministry's gloss, not the rule, and is not counted as a second witness.

- **`RB3` = `surety`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 19, 講則 item 8). 講則 item 8: 一、講取當ノ者ハ連帶借用證書ヲ支配人ニ差入ルルコト. A 連帶借用證書 has joint obligors by definition, so a co-signer stands behind the drawer; no property is named. Medium because the rule does not say who the co-obligors are. If they are the members of the drawer's クビリ (as the 解說's gloss 講クビリといふ場合連帶保證 … の意味に用ひられて would suggest), then the line between signing (RB3) and belonging (RD-test) is blurred in this kō: see answer 4. Coded on the text, which speaks of a bond, not of the クビリ.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 19, 講則 items 1–15). Who bears the shortfall is stated (講則 item 6, the クビリ); how it is divided among the クビリ's members is not. 立替ヘル says nothing on pro-rata, equal or capped shares. The 解說's 連帶して is joint liability, which is not one of LS1's values and in any case is the ministry's gloss. Silence on the division.

- **`LS3` = `1`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 19, 講則 items 6, 8). A member can be made to pay beyond his own contribution: through his クビリ, for another member's shortfall (講則 item 6 一、時間內掛金不足ノ際ハ講クビリヨリ立替ヘルコト, with the three クビリ fixed by its 但書), and, once he has drawn, on a 連帶借用證書 (item 8). This is exposure for OTHERS' obligations, so it does not depend on the house-practice reading noted at 第六講. Medium: 立替ヘル is an advance and the rule does not say how it falls on individual members of the クビリ.

- **`CN3` = `1`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 19, 講則 items 6, 7, 8). Drawn members sign a 連帶借用證書 to the 支配人 (講則 item 8 一、講取當ノ者ハ連帶借用證書ヲ支配人ニ差入ルルコト), which is a debt instrument enforceable against them and their co-obligors, and their shortfall at a meeting is covered by their クビリ (item 6). Unwon members (rule 5, recorded here): 一、子ノ時間內掛金不足ノ際抽籤除ケトス (item 7), exclusion from that round's lot, which alone would be the P of ko_usui_bango_1822. The value rests on the drawn side. Medium because no clause speaks of suit or distraint in words.

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 19, 講則 items 1–15). Five 支配人 (footnote 1: 支配人は世話人のこと) paid 一回ニ付金一圓 (items 2–3) receive the drawers' bonds (item 8) and the notice of a member's removal from the village (item 13). The rules do not say how the 支配人 are chosen, and no clause gives decision over the fund to an assembly, an elder or an outside body. Silence on the locus of decision.

### 第12講 春山夏助長壽講 (靜岡縣引佐郡井伊谷村)

- **`RD-test` = `officers`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 30–31, 第三條, 第六條). The 世話人 answer for the 講主's default itself. 第三條: 初回ノ掛金ハ講主之ヲ申受ケ直チニ講主及講主引受人連帶ノ借用證書ヲ世話人ヘ提出シ、期日ニハ無相違掛金致シ屹度義務ヲ相果シ可申萬一之場合ハ世話人ニ於テ辨濟到シ決シテ加入者ニ對シ御迷惑相懸申間敷事 (辨濟到シ as printed). The 講主 (footnote 1: 講親) holds one of the 二十口 and takes the first pot, so he is a drawn member; his own security is the joint bond with his 引受人 (footnote 3: 講親の保證人), which is RB3's ground; beyond it the clause names the 世話人, and expressly shields the 加入者. This is liability for the default, not for mishandling, so rule 3 does not apply. Medium for one reason that matters: the clause covers the 講主 only. For the other drawers (落札シタル者) 第六條 requires 世話人ニ於テ充分ナルモノト認ムル抵當權 before the pot is handed over and names no bearer if it fails. Rule 2 has me code the last bearer the instrument names, and the only one it names is the 世話人; but the value describes the convener's default, not every drawer's. See answer 4: RD-test has one cell where this kō has two regimes. ALTERNATIVE: .NR, on the ground that the question is about 'a member' generally and the instrument is silent for 十九 of the 二十口.

- **`RB3` = `mixed`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 30–31, 第三條, 第六條). Surety for the convener, property for the other drawers. 講主: 講主及講主引受人連帶ノ借用證書 (第三條; footnote 3 講主引受人は講親の保證人). Other drawers: 本講ニ於テ落札シタル者ハ世話人ニ於テ充分ナルモノト認ムル抵當權ヲ取得シ以テ落札金ヲ引渡スモノトス (第六條), a hypothec whose object is not named. `mixed` because the instrument takes property and surety together, BUT not on the same drawer: no drawer gives both. That is a third sense of `mixed`, beside the two the ko_mitarai_gin_1805 note distinguishes. ALTERNATIVE: `surety`, coding only the fully specified clause, since the object of the 抵當權 is not named (the ko_meio_1498 objection). Rejected because a 抵當權 is property security whatever its object, and dropping 第六條 would describe one drawer out of twenty.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 30–31, 第一條–第八條). The bearer is named for the 講主's default (第三條, the 世話人) but not how the 世話人 divide it; nothing distributes a loss on any other drawer. 第五條's 親子割 (鬮出金ハ親子割トシ貳拾口割トス; footnote 6) divides the bid discount, a surplus, across all twenty 口. It is not a loss rule. Silence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, pp. 30–31, 第三條, 第六條). Coded on house practice, as at 第六講. A drawer's property answers for his debt (第六條 世話人ニ於テ充分ナルモノト認ムル抵當權ヲ取得シ以テ落札金ヲ引渡ス), and the 講主 is bound jointly with his 引受人 (第三條). That is ko_mitarai_mujin_1773's ground for LS3=1. The definitional objection is the same: what is secured is the 返掛 he agreed to pay. Not counted: the 世話人's liability for the 講主 (第三條), because the rules do not say the 世話人 are members; if they are, this cell would rest on exposure for another's debt and would be high.

- **`CN3` = `1`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 30–31, 第三條, 第四條, 第六條). Drawn side compellable: the 講主 binds himself 期日ニハ無相違掛金致シ屹度義務ヲ相果シ可申 on a 連帶ノ借用證書 with his 引受人 (第三條), and other drawers give a 抵當權 (第六條). That is the ko_mitarai_gin_1805 pattern (bond plus surety), not the ko_mitarai_mujin_1773 one (pledge with no sanction clause). Unwon members (rule 5): nothing beyond 第四條 …トシ掛金掛持ノ事; no sanction for an undrawn member's arrears is stated. Medium because the sanction is the instrument, not a clause saying what follows default.

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 30–31, 第三條, 第六條, signatories). NO FITTING VALUE. Decision over the fund sits with the 世話人: they take and judge the drawers' security and hand over the pot (第六條 世話人ニ於テ充分ナルモノト認ムル抵當權ヲ取得シ以テ落札金ヲ引渡スモノトス) and they guarantee the 講主 (第三條). Nine or so 講事世話人 sign the rules beside the 講主 and his 引受人. Nothing says how they are chosen or that an assembly decides anything. A board of officers who are also guarantors of the convener is neither collective, nor elder-fixed, nor external-administered on the record; coded .NR as house practice does for named officers whose mandate is not described (ko_mitarai_hanei_1840, ko_horyuji_50kan).

### 第14講 深井朝右衞門發起頼母子 (山口縣吉敷郡嘉川村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 33–34, 第拾條, 第拾壹條, 第拾五條, 賴母子金借用證書). Silent beyond the drawer's own security, and the rules say where they send the silence. A payout creates a debt (第六條 次親ハ無利息元掛ノコト; the form 毎回金貳拾圓宛無相違返濟可致候), so the cell applies. The drawer's security is 入組人中ヨリ連帶保證人貳名 (第拾條), RB3's ground under rule 1 even though the guarantors must come from the membership: they are chosen for this loan and bind by signing. The form adds acceleration on default (萬一違約致候節ハ年賦方法ヲ解キ全部一時ニ請求セラルヽモ異議申間敷候), which is the defaulter's own liability (rule 4). 第拾壹條 (取當人前條ヲ履行セザルトキハ貳番札ヲ以テ取當者トス、入札ノ差金ハ違約者ヨリ辨償セシメ後取者ニ分配スルモノトス) is a winner who fails to complete, again the defaulter's own liability (rule 4). Beyond that: 第拾五條 右規約以外ノ事項ハ地方賴母子ノ慣例ニ從フモノトス. That is an express reference to local custom, not an instruction that the members will decide, so it is not `deferred`; and rule 6 forbids coding what custom or law would supply. .NR, with the reference to custom recorded because it is a different kind of silence from a rulebook that says nothing.

- **`RB3` = `surety`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 33–34, 第拾條, 賴母子金借用證書). 第拾條 取當者決定シタルトキハ五日以內ニ入組人中ヨリ連帶保證人貳名ヲ立テ、末尾記載ノ書式ニ準ジ證書ヲ調製シ總代ニ差出シ受金スルコト、但シ連帶保證人ノ內壹名ハ入組外ニテモ總代ノ承認スル者ナレバ差支ヘナシ. The form confirms it: 爲後日連帶保證人貳名相立借用證書差出置候. No property is taken. Note that the 取建親 (發起親), who receives the first pot without bidding, is not said to give guarantors; 第拾條 speaks of the 取當者 chosen at a meeting.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 33–34, 第一條–第拾五條). No rule distributes an unmet loss. The distribution clauses all divide gains: 入札棄金ハ後取者ノ所得トス (第八條), the defaulting winner's 差金 後取者ニ分配スル (第拾壹條), 延滯利息ハ取當者ノ所得トス (第拾四條). 第拾五條 sends anything else to 地方賴母子ノ慣例, which is not a rule of this instrument.

- **`LS3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 33–34, 第拾條, 賴母子金借用證書). Members are exposed for other members' debts. 第拾條 requires the drawer to find 入組人中ヨリ連帶保證人貳名 (one may be an outsider approved by the 總代), so at least one fellow member stands as joint and several guarantor for a draw that is not his. That is the ko_mochiyori_yutsu_1876 ground (sureties who undertake to discharge another's debt), not the weaker house-practice ground of a drawer's own property, so this cell does not carry the definitional doubt noted at 第六講.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 33–34, 第拾條, 第拾四條, 賴母子金借用證書). Sanctioned on both sides of the draw. 第拾四條 前取者ト後取者ヲ問ハス掛金ノ延滯ニ對シテ日步百圓ニ付四錢ノ延滯利息ヲ附スルコト. For the unwon member (rule 5, recorded here) that penalty interest is the only stated sanction. For the drawer: joint and several guarantors (第拾條) and acceleration of the whole debt on default (form: 萬一違約致候節ハ年賦方法ヲ解キ全部一時ニ請求セラルヽモ異議申間敷候).

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 33–34, 第二條, 第拾貳條, 第拾三條). A 總代 runs the fund (第拾三條 總代ハ全般ノ整理ヲナシ諸證書及ビ帳簿ノ保管ヲ成シ併セテ金錢ノ取扱ヲ成スモノトス, with a 副總代), may convene in place of a dilatory 發起者 (第拾貳條), and approves an outside guarantor (第拾條). How the 總代 is chosen is not stated. The membership acts as a body only on transfer of a share (第二條 入組者全部ノ快諾アル時ハ此限リニ非ス), which is a decision over membership, not over the fund. None of collective, elder-fixed, external-administered is supported by what is written; silence on the locus.

### 第15講 權田太郎兵衞發起頼母子 (山口縣吉敷郡嘉川村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 36–37, 第八條–第十四條, 第二十一條, 第二十二條). Silent beyond the drawer's own security. The security is 貳名以上ノ保證人並ニ擔保物件 (第八條), one guarantor 必ス入組人タルコト (第九條): guarantors chosen for this loan, so RB3's ground under rule 1 even though one must be a member. On arrears the instrument goes to the drawer's own pledge and stops: 第十四條 前取者掛金延滯貳拾日以上ニ及フトキハ擔保物件ノ處分ニ着手ス. 第十三條 (取當者…完全ナル證書ヲ調ヘサル時ハ落札權ヲ失シ臨時會ヲ開キ處分ス、其ノ費用及差損金ハ失權ノ負擔トス) puts the loss of a failed completion on the defaulter himself (rule 4). Two general clauses are not read as answers: 第二十一條 右規約ノ改正及必要ノ事項ハ參分ノ貳以上ノ同意ヲ以テ決ス is a general decision rule, not an instruction that the members will decide who bears an unpaid residue (the `deferred` reading is stated and rejected as at 第六講); 第二十二條 本規約以外ハ總テ地方賴母子ノ慣例ニ依ル sends the gap to custom, which rule 6 forbids me to code.

- **`RB3` = `mixed`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 36, 第八條–第十一條; p. 37, 賴母子返掛借用證書). Property and surety together, on the same drawer. 第八條 取當者ハ貳名以上ノ保證人並ニ擔保物件ヲ定メ證書作成ノ上金錢ヲ受領スヘシ; 第九條 保證人ハ一名ハ必ス入組人タルコトヲ要ス; 第十條 取當者債務擔保物件ハ有價證券、田畑、山林、宅地家屋ヲ左ノ各項ニ準シ提供スヘシ, with cover ratios (五分利以上ノ公債ハ債務額百圓ニ付額面八十圓以上; 田地ハ債務額百圓ニ對シ地價十圓以上) and, for other property, 正副總代及評價人ノ承認, houses to carry fire insurance, real property only 嘉川村、井關村所在ノモノ; 第十一條 top-up on a fall in value (增擔保ノ請求ニ應スヘシ). The form has 債務者 and two 連帶保證人 and a schedule of 擔保物件. `mixed` again carries both mixtures (several kinds of property, and property plus surety).

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 35–37, 第一條–第二十二條). No rule distributes an unmet loss. The one distribution clause divides a surplus: 第三條 但シ滿會ハ親ノ利ハ入組全員配當トス (footnote 4: 入組全員は加入者全員), the 講親's interest shared among all members at the end. A failed completion's 差損金 falls on the defaulter (第十三條). Silence.

- **`LS3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 36, 第八條–第九條; p. 37, 賴母子返掛借用證書). A member must stand as guarantor for another's draw: 第九條 保證人ハ一名ハ必ス入組人タルコトヲ要ス, with 第八條's 貳名以上ノ保證人, and the form makes them 連帶保證人. A member is therefore exposed beyond his own contribution for a debt that is not his. The ko_mochiyori_yutsu_1876 ground; does not depend on the house-practice reading noted at 第六講.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 36–37, 第十二條–第十四條). Sanctioned on both sides of the draw. 第十二條 會座ノ節掛金未納者ハ前取後取ヲ論セス百圓ニ付一日金五錢ヲ取當者ニ支拂フモノトス (footnote 7: 既取未取を論ぜずの意), which is the only stated sanction for an unwon member (rule 5, recorded here). Drawers: 第十四條 前取者掛金延滯貳拾日以上ニ及フトキハ擔保物件ノ處分ニ着手ス, plus guarantors (第八條–第九條).

- **`GV1` = `collective`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 37, 第十五條–第二十一條). Rule change and 'necessary matters' are decided by a qualified majority: 第二十一條 右規約ノ改正及必要ノ事項ハ參分ノ貳以上ノ同意ヲ以テ決ス; a transfer of a share needs 役員及子方半數以上ノ承諾 (第二十條; footnote 9 子方はここでは講員の意). Officers (正副總代, 評價人貳名) keep the books and cash and appraise collateral (第十五條–第十八條) for four-year terms, 再選ヲ妨ケス (第十九條); how they are chosen is not stated. Medium: 第二十一條 does not say whose two-thirds, although the members are the only body it can mean, and 必要ノ事項 is the broadest grant in the rules. ALTERNATIVE: .NR on house practice for officer-run kō; rejected because the rules put a decision rule on the membership in words.

### 第18講 山坂昇講 (福岡縣糸島郡深江村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 51–52, 講則 items 1–8). Silent. A payout creates a debt (掛戾金, footnote 5 返掛金即ち償還金), so the cell applies. The drawer's security is 掛戾金ノ總額ニ對シ擔保ヲ提供シ尙相當ノ保證人一名 (item 7), RB3's ground. Nothing names a bearer beyond it. One fact that could be misread as `fund`: every pot pays 積立金及雜費 貳圓五拾錢 (item 8), so a reserve exists; but no clause applies it to a default, and coding `fund` would infer the reserve's purpose from its existence. The kō was wound up before 1936 (解說), which does not affect what the rules say.

- **`RB3` = `mixed`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 52, 講則 item 7). 一、落札人ガ其取當金ヲ領收スルニハ掛戾金ノ總額ニ對シ擔保ヲ提供シ尙相當ノ保證人一名ヲ要ス. Security for the whole remaining debt AND a surety, on the same drawer. The object of the 擔保 is not named; `mixed` rests on the clause distinguishing 擔保 from 保證人 (尙), so the 擔保 is something other than a person. The 解說 says the 親 gave 抵當物件 like any other drawer; that is the ministry's statement, used only as confirmation that item 7 bound the 親 too.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 51–52, 講則 items 1–8). No rule distributes an unmet loss. Item 8 lists deductions from each pot (盛料, 割取, 銀座手當, 積立金及雜費), none of which is a loss allocation. Silence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 52, 講則 item 7). Coded on house practice (ko_mitarai_mujin_1773, ko_mitarai_hanei_1840): the drawer's 擔保 and his 保證人 answer for 掛戾金ノ總額 (item 7). Same definitional objection as at 第六講: what is secured is the repayment he agreed to make, so on a strict reading of 'beyond what he has … agreed to contribute' this would be .NR. Whether the 保證人 must be a member is not stated, so the stronger ground (exposure for another's debt) is not available here.

- **`CN3` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 51–52, 講則 items 1–8). No consequence of non-payment is stated. Item 4 fixes a deadline (集金ハ正午迄ト定メ) without saying what follows if it is missed; item 7 takes 擔保 and a 保證人 from the drawer and says nothing on when or how they are called. House practice: ko_mitarai_mujin_1773 CN3=.NR on a pledge with no sanction clause; this is the same case. Unwon members (rule 5): nothing stated. ALTERNATIVE: 1, reading a surety and a pledge as instruments of compulsion by their nature; that is the reading on which the existing row and this cell would both move.

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 51–52, 講則 items 5, 8). 一、本講ハ管理ノタメ三人ノ銀座ヲ選任シ手當ヲ支給ス (item 5; footnote 2 銀座とは世話人或は役員のこと), paid 銀座手當 from each pot (item 8). Who chooses them and who decides over the fund are not stated. Silence on the locus.

### 第21講 共同信用講 (靜岡縣磐田郡富岡村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 58, 會則 落札金預リ方法; 講金預リ證書). Silent beyond the drawer's own security. The rules stop at the guarantors: 會則 一、落札金預リ方法 落札金預リ證劵ニハ抵當書入確實ナル保證人貳名以上ヲ要ス、然ル上ハ不動產ノ登記ヲ要セズ, and the form makes the guarantors pay first and regardless of the pledge: 若シ壹回タリトモ遲滯シ掛返シ出來難キ時ハ辨濟保證人ハ本人ニ成リ代リ右抵當事實有無ニ拘ラズ金額ノ預リ金辨濟可仕候. Guarantors chosen for this loan are RB3's ground (rule 1). No clause names anyone beyond them. The heading 共同信用講 and the ministry's class say nothing the rules say, and are not coded from (FRAMES.md). Applicability: payout creates a debt (掛返シ), so not .NA.

- **`RB3` = `mixed`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 58, 會則 落札金預リ方法; 講金預リ證書). Property and surety on the same drawer. 會則: 落札金預リ證劵ニハ抵當書入確實ナル保證人貳名以上ヲ要ス、然ル上ハ不動產ノ登記ヲ要セズ — the mortgage is written into the deposit certificate and registration of the real property is waived once two sound guarantors stand. The form names the pledge as real property (此ノ抵當 一、家屋一棟 間口 間 奧行 間, 所有者 何某) and calls the guarantors 辨濟保證人. Of note for RB3: the clause trades registration of the pledge against the guarantors' standing, and the form makes the guarantors answer 抵當事實有無ニ拘ラズ, so the surety, not the property, is the operative security.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 58, 會則 items 1–7). No rule distributes an unmet loss. 落札金ヲ總口數ニ割ル事則チ親子割 (鬮取方法) divides the bid discount, a surplus, by heads (footnote 2). Silence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 58, 會則 落札金預リ方法; 講金預リ證書). Coded on house practice, as at 第六講: the drawer's house is pledged and his guarantors stand behind his 掛返シ (會則 落札金預リ方法; form 此ノ抵當 一、家屋一棟 … 辨濟保證人ハ本人ニ成リ代リ). The rules do not say the guarantors must be members, so the stronger ground (a member liable for another's debt) is not available. Definitional objection as at 第六講.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 58, 會則 花割方法; 講金預リ證書). Explicit consequences of non-payment on both sides of the draw. Any member who fails to bring his 掛金 on the day loses his 花割 refund: 立會當日掛金持參ハ勿論ナルモ萬一持參無キ方ヘハ花割ヲ戾サズ (會則 花割方法); this is the only stated sanction on an unwon member (rule 5, recorded here). A drawer's single missed payment calls his guarantors in his place: 若シ壹回タリトモ遲滯シ掛返シ出來難キ時ハ辨濟保證人ハ本人ニ成リ代リ右抵當事實有無ニ拘ラズ金額ノ預リ金辨濟可仕候 (form). The ko_mitarai_gin_1805 pattern, stated in words.

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 58, 會則 items 1–7; 講金預リ證書). No officer, assembly or decision procedure appears in the 會則 or the form; the form is addressed to no named body. The 解說's report that meetings were cut from three to two after 昭和七年 shows that someone decided, but not who, and it is the ministry's statement. Silence on the locus.

### 第23講 昭和御大典記念講 (福岡縣築上郡東吉富村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 62–63, 第十條, 第十一條, 第十三條–第十五條, 第十九條). Silent beyond the drawer's own security. The drawer gives (イ) 理事ニ於テ身元確實ト認ムル二名以上ノ連帶證書 or (ロ) 理事ニ於テ適當ノ擔保ト認ムヘキモノヲ書入レ登記スルコト (第十條), RB3's ground. Four clauses that could be mistaken for an answer, and why each is not: (i) 第十九條 理事ハ故意又ハ重大ナル過失ニ依リ本講ニ損害ヲ及ホシタルトキハ連帶責任ヲ以テ賠償ノ責ニ任ス is officers' liability for misconduct only, which rule 3 sends to .NR, not `officers`; (ii) 第十四條 積立金ハ訴訟其他避クヘカラサル費用ノ外使用スルコトヲ得ス lets the reserve pay for litigation, which is the cost of pursuing a defaulter, not the defaulted sum; reading it as `fund` would turn a costs clause into a loss clause; (iii) 第十一條 (再入札ヲ行ヒ其間際金及臨時費用トシテ金拾圓ヲ差出サシムル…若シ之ヲ拒ムトキハ講員ノ資格ヲ失ヒ既掛込金ハ全部沒收スル) is the defaulter's own liability on a refused or uncompleted draw (rule 4); (iv) 第十五條 divides the surplus 殘餘金 among the 未取得者. Applicability: 掛戾金 (footnote 1) is a debt, so not .NA.

- **`RB3` = `mixed`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 62–63, 第十條). 第十條 落札人ハ左ノ各項ノ一ニ依ルニアラサレハ落札金ヲ受取ルコトヲ得ス (イ) 理事ニ於テ身元確實ト認ムル二名以上ノ連帶證書ヲ差出ス事 (ロ) 理事ニ於テ適當ノ擔保ト認ムヘキモノヲ書入レ登記スルコト. Surety OR registered property, at the drawer's choice: 各項ノ一. The vocabulary defines `mixed` as property and surety TOGETHER, which this is not; neither `surety` nor `real-estate` describes the arrangement either, and the object of the 擔保 is not named. Coded `mixed` at medium as the nearest value for an instrument that admits both, and raised in answer 4. ALTERNATIVE: .NR as 'no fitting value'.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 62–63, 第一條–第二十一條). No rule distributes an unmet loss. The distribution rules divide gains: 第十三條 積立金 … 滿會ノトキ精算ノ上講員平等ニ分配スル and 第十五條 殘餘金ハ利益トシテ未取得者ニ平等ニ配當スル. Reading 平等 in either as the loss rule would be the surplus-for-loss substitution. Silence.

- **`LS3` = `1`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 62–63, 第七條, 第十條). Members stand jointly for other members' draws. The drawer may give 二名以上ノ連帶證書 (第十條イ), and the rules treat those 證人 as members: 第七條 落札者ニシテ前條該當者アルトキハ其證人ニ對シテハ花籤ノ抽籤權ヲ停止ス — a guarantor of a defaulting drawer loses his 花籤 right, which only members hold. A member is thus exposed beyond his own contribution for another's debt. Medium because (イ) is optional (the drawer may pledge property instead) and membership of the 證人 is inferred from 第七條, not stated.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 62–63, 第六條, 第七條, 第十一條). Sanctioned on both sides of the draw, in graded money penalties. 第六條 掛金、掛戾金ヲ時間內ニ差出サヾルトキハ、辨當料ノ交付並ニ花籤ノ抽籤權ヲ失ヒ、且ツ掛金延滯ニ對シ左ノ通リ違約金ヲ徵收スルモノトス 一、掛戾金ニ對シテハ 一口ニ付一日拾錢 一、掛金ニ對シテハ 同上 四錢. The unwon member's (rule 5) sanction is the 四錢 a day and the loss of 辨當料 and 花籤. A drawer's default also costs his guarantor (第七條). A winner who will not complete loses membership and everything paid in (第十一條 講員ノ資格ヲ失ヒ既掛込金ハ全部沒收).

- **`GV1` = `collective`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 62–63, 第四條, 第十八條, 第二十一條). Decision sits with the membership in three clauses: officers are elected by the members and replaced the same way (第十八條 本講ノ事務ヲ處理スル爲メ講員ノ互選ニ依リ理事五名ヲ選定ス 但缺員ヲ生シタルトキハ其都度互選ニ依リ補充ス); the rules change only by 講員半數以上ノ許決 (第二十一條); and no pot is auctioned without a quorum (第四條 出席講員過半數ニ達スルトキハ花籤及入札ヲ行フ). The 理事 run business, approve security (第十條) and keep the passbook (第十三條), under that mandate.

### 第25講 親睦講 (秋田縣仙北郡千屋村)

- **`RD-test` = `all-members`** (confidence low, articulation articulated; 農林省經濟更生部 1936, p. 67, 規約 藏元ノ任務 (4); p. 68, footnote 4)). The one clause in the seventeen that I read most narrowly, and the cell rests on how it is parsed. 一、藏元掛返シ金遲滯ノ節ハ裁判所ニ申請スルコトアルヘシ 右ノ費用ハ被告ノ負擔タルハ勿論タリト雖モ講中一同出金ノ上取扱フコト、尤モ損害費用要求シ不足ヲ生シタルトキハ講員一同ノ負擔タルヘキコト. When a drawer (既諍取者) fails to pay his 掛返シ金 the 藏元 may sue; costs are the defendant's but are advanced by all; and 尤モ損害費用要求シ不足ヲ生シタルトキハ講員一同ノ負擔タルヘキコト — if, on claiming 損害費用, a shortfall remains, it falls on 講員一同. The drawer's own security is a registered mortgage on rice land (規約 item 6, RB3's ground), and suit is the step after it; so 講員一同 is the last bearer the instrument names (rule 2). WHY LOW: 損害費用 can be read as one compound ('the costs, as damages') or as two ('the damages and the costs'). On the first reading the shortfall is only unrecovered LITIGATION COSTS, which is not the unpaid residue this characteristic asks about, and the cell is .NR. The editor's footnote 4) glosses the clause as about costs only (これに要する費用は該既取者の負擔…裁判終了まで諸費用は一時講員一同が立替へる) and does not mention the 不足 sentence at all. I read 損害 as the unpaid 掛返シ金 because the clause opens on that default (藏元掛返シ金遲滯ノ節) and 損害 is not otherwise used for costs in these rules (they say 費用); the editor's gloss is not evidence against it, since he does not address the sentence. ALTERNATIVE, stated fairly: .NR, on the costs-only reading. Raised in answer 4.

- **`RB3` = `real-estate`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 67, 規約 item 6, 藏元ノ任務 (1)). 本講資金諍取者ハ前項ノ義務ヲ履行スル爲メ掛返シ金拾圓ニ對シ地價金壹圓宛（田地ニ限ル）ノ土地ヲ擔保トシ、抵當權ヲ設定シ登記濟ノ上諍取金ヲ受領スルモノトス (規約 item 6; footnote 3 地價は法定地價), and the 藏元 must obtain the registration (藏元ノ任務 (1) 一、藏元ハ諍取者ヨリ規定ノ登記ヲ取得スベシ). Rice land only, registered, at a stated cover ratio; no guarantor is required anywhere in the rules.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 67, 規約 藏元ノ任務 (4)). The bearer of the shortfall is named (講員一同ノ負擔, see RD-test) and how it is divided is not: no pro-rata, per-share or equal rule. The costs are 講中一同出金 with no ratio either. 講員一同 is a set of bearers, not a division rule. Silence on the division.

- **`LS3` = `1`** (confidence low, articulation articulated; 農林省經濟更生部 1936, p. 67, 規約 藏元ノ任務 (4)). Rests on the same clause as RD-test, and is low for the same reason. On the reading taken there, each member bears a share of another drawer's unrecovered default (講員一同ノ負擔), which is exposure beyond his own contribution. On the costs-only reading the members still advance litigation costs (講中一同出金ノ上取扱フコト) and bear any unrecovered part of them, which is also an outlay beyond contribution, though a smaller one; so this cell survives the alternative reading of RD-test better than RD-test does. The two cells are not independent evidence.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 67, 規約 藏元ノ任務 (2), (4)). Graduated sanctions, on both sides of the draw. A drawer who misses the deadline is dunned by the 世話掛 within five days and pays 延滯損害料 at 掛返シ金五拾圓ニ對シ日步拾錢 plus a 督促料 of 參拾五錢 a time; then suit (藏元掛返シ金遲滯ノ節ハ裁判所ニ申請スルコトアルヘシ) against a registered mortgage. Unwon members (rule 5, recorded here): 又未諍取者ニアリテハ前掛金沒收シ除名スルコトアルヘシ — forfeiture of what he has paid and expulsion.

- **`GV1` = `collective`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 66–67, 規約 items 3, 4, 8). The fund is allocated in the general meeting: 本講資金融通使用セントスルモノハ毎年十一月十五日ノ總會ニ於テ總資本金一千五拾圓ノ內ヨリ口諍ヲ以テ順次諍下ヲ執行シ (規約 item 4), the kō meeting once a year as a 總會 (item 3). Officers are put forward for fixed terms: 本講會務ヲ整理セン爲メ藏元二名及世話掛一名ヲ推薦シ任務ヲ五ケ年トス (item 8; footnote 2 藏元は世話人又は講元); 推薦 does not say by whom. Medium: the 總會 is the place of allocation by auction, which is a decision rule over the fund, but no clause gives the meeting power to amend or to decide other questions.

### 第26講 正利講親無金無盡 (秋田縣仙北郡千屋村)

- **`RD-test` = `deferred`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 69, 規約 第九, 第十一, 第十三, 第十四; pp. 69–70, 正利講金借用證書). The instrument sends default to the members' decision. Order of recourse: the drawer; then his 連帶保證人 (form: 若シ期限相違ノ節又ハ居處不定死亡事故不在ノ時ハ連帶保證人ハ本人ニ代リ速ニ辨償可仕候萬一辨償ノ義務ヲ果サヽル時ハ成規ノ御取計被成候共決シテ異議無之候), or a mortgage in their place (規約 第九); all of which is the drawer's own security and RB3's ground (rule 1; footnote 6 makes the guarantors persons the members accept, not members by belonging). Beyond that the rules name no bearer and say instead: 第十一、本講連中ニ於テ約定ヲ履行セザル者アル時ハ臨時會ヲ開キ協議ノ上決定スル事, decisions by majority (第十三 但シ此ノ場合ハ凡テ多數決ヲ以テ定ムル事) and binding (第十四). I code `deferred` because 第十一 is a clause about DEFAULT specifically, not a general power to amend the rules or decide 'necessary matters'; a general clause of that kind would not by itself be `deferred`. Medium, because 第十一 does not say that the meeting decides WHO BEARS the unpaid residue; it says the meeting decides about the non-performer, which could be read as deciding only what to do to him (his own liability, rule 4). ALTERNATIVE: .NR on that narrower reading. 第十一 also covers unwon members who stop paying (rule 5); recorded at CN3.

- **`RB3` = `mixed`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 69, 規約 第九; pp. 69–70, 正利講金借用證書). Surety OR property, at the drawer's option. 第九、本講取主ハ連中開濟ノ連帶保證人貳名ヲ連署シタル左記債券ヲ藏元ニ差出シ引配スル事、尤モ抵當權ヲ設定スル時ハ證人ヲ要セス; the form is the guarantors' version (連帶保證人連署ヲ以テ金借用證書差入候), and it also binds the parties to give a mortgage on demand if default threatens (尚期限中ト雖モ前約定不履行ノ恐アル時ハ一時ニ皆金之返濟若シクハ抵當權ノ設定ニ應ジ可申候). The vocabulary's `mixed` is property and surety TOGETHER; here they are alternatives (with property as a fallback on demand). Coded `mixed` at medium as the nearest value and raised in answer 4. ALTERNATIVE: `surety`, since the printed form is the surety version and property is only an option.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 69, 規約 第一–第十四). No rule distributes an unmet loss. 第六、鬮取高ハ正手取トシ前取主ノ返濟金ヲ差引キ殘額ヲ末人數ノ平等割トス divides the bid surplus equally among the undrawn (footnote 5 末は未取人); reading 平等割 there as the loss rule would be the surplus-for-loss substitution. 第十一 defers default to 協議 and states no division. Silence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 69, 規約 第九; pp. 69–70, 正利講金借用證書). Coded on house practice (ko_mitarai_mujin_1773): the drawer's guarantors, or his mortgaged property, answer for his debt, and the form accelerates the whole debt if default threatens (一時ニ皆金之返濟). Same definitional objection as at 第六講. The guarantors are persons the members accept (footnote 6), not stated to be members, so the stronger ground is not available.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 69, 規約 第十, 第十一; pp. 69–70, 正利講金借用證書). Sanctioned on both sides of the draw. Any member: 第十、本會期ニ金ヲ積マズ督促ヲ受クル者ハ毎回貳拾錢ノ督促料ヲ支拂フ事, and 第十一 (any 約定ヲ履行セザル者 goes before a 臨時會). For the unwon member (rule 5, recorded here) those are the stated sanctions. Drawers: guarantors pay at once, and if they fail 成規ノ御取計被成候共決シテ異議無之候 (form), with acceleration or a mortgage on demand if default threatens.

- **`GV1` = `collective`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 69, 規約 第八, 第十一, 第十三, 第十四). The membership decides, by majority, on officers, rules and defaults: 第十三、藏元事故アリテ辭スルカ講中ノ協議ニヨリ改ムルコトヲ得、尚協議ニ依リ此ノ規約ヲ變更追加スルコトアルヘシ 但シ此ノ場合ハ凡テ多數決ヲ以テ定ムル事 (footnote 7 講中は連中と同じく加入者); 第十一 defaults go to a 臨時會 and 協議; 第十四 本講中ノ協議決定シタルコトハ堅ク相守リ違背セサル事. The single 藏元 (第八) holds the books and bonds and passes money, as the members' agent.

### 第27講 蒲團講 (靜岡縣庵原郡小島村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 71, 講則 第一–第八). Silent beyond the drawer's own security. A payout creates a debt (大掛, footnote 2 既取人の返掛金), so the cell applies; the bedding purpose does not make it .NA, since the pot is money and the 解說 says spending it on bedding is left to the member. The drawer's security is 會員中ヨリ保證人二名以上 (第六). Under rule 1 these are guarantors chosen for this loan, so RB3's ground, even though they must be members: liability attaches by signing, not by belonging. Nothing names a bearer once they fail.

- **`RB3` = `surety`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 71, 講則 第六). 第六、落札者ハ會員中ヨリ保證人二名以上ヲ立テ證書ヲ提出スルコト. Two or more guarantors drawn from the membership, with a bond; no property is taken.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 71, 講則 第一–第八). No rule distributes an unmet loss. 第七、利益金ハ毎回親子割トス divides a surplus, by footnote 4) 未取人既取人を問はず平均割; reading it as a loss rule would be the surplus-for-loss substitution. Silence.

- **`LS3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 71, 講則 第六). Members are made guarantors of other members' draws: 第六、落札者ハ會員中ヨリ保證人二名以上ヲ立テ證書ヲ提出スルコト. A member who signs is exposed beyond his own contribution for a debt that is not his. This is the stronger ground (ko_mochiyori_yutsu_1876's co-sealers), not the house-practice reading of a drawer's own security.

- **`CN3` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 71, 講則 第三, 第六). No consequence of non-payment is stated. 第三 掛金ハ會合ノ當日持參ノコト fixes the duty; 第六 takes guarantors and a 證書 from the drawer; nothing says what follows a failure to pay, for a drawn member or for an unwon one (rule 5: nothing to record). House practice reads security without a sanction clause as .NR (ko_mitarai_mujin_1773 CN3). ALTERNATIVE: 1, on the ground that a bond with two guarantors is compulsion by its nature.

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 71, 講則 第二, 第四, 第五, 第八). The 會主 (footnote 1 講親) takes the first pot (第五), hosts the meeting (第八), fixes and notifies its time (第四 日時ハ其ノ都度會主ニ於テ通知ス) and receives notice of a member's wish to use his share otherwise (第二). Nothing says who decides over the fund beyond that. The 解說 calls the 親 むしろ會員の世話役, but that is the ministry's characterisation. Silence on the locus.

### 第31講 富士石碑講 (靜岡縣富士郡富士町)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 77–78, 第八條, 第十條, 第十三條, 第十六條, 第十七條; p. 79, 割濟金連帶借用之證). Applies, and silent. Applicability: the payout is a stone monument, not cash, but the drawer then owes 掛戾金 (第十六條; footnotes 4–5), so a debt to the fund exists. Recourse runs: the drawer and his 連帶借用人三名以上 (第十條, 第十三條; the form 連帶債務者ノ內ニ於テ返金相成兼候時ハ三名ノ內壹名ニテモ引受ケ必ズ返金可仕候), RB3's ground; then suit by the 世話人, or assignment of the claim if they cannot sue: 第十六條 本講員ニシテ大掛トナリ掛戾金ヲ怠リタルトキハ世話人ニ於テ訴訟ヲ提起スル事能ハザル場合ハ、債權ヲ他ニ讓渡スルコトアルモ、債務者ニ於テ必ズ異議ナキモノトス; costs on the debtor (第十七條). Nothing names who bears what is still unpaid. DECISION POINT, stated fairly: 第八條 本講出金花ヲ第一回ヨリ第三回迄積立テ掛金延滯ノ爲費消シタル時ノ費用ニ充ツ sets up a reserve for when there is 費消 owing to arrears. It could be read as `fund`: the reserve absorbs what arrears consume. I read 費用 as expenses (the 解說 calls it 訴訟費用, which agrees, though I do not rest on the 解說), so the clause pays the cost of pursuing a defaulter, not the defaulted sum; on that reading the rules leave the residue unassigned. If the maintainer reads 第八條 as covering the shortfall itself, this cell moves to `fund` and LS1 to `residual-on-fund`.

- **`RB3` = `surety`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 78, 第十條, 第十三條; p. 79, 割濟金連帶借用之證). 第十條 落札人定マリタルトキハ別紙證書雛形ニ依リ連帶借用人三名以上ニテ受取ルモノトス; 第十三條 本講落札人ハ連帶借用人ヲ參名以上選ビ世話人ニ一應相談ノ上定ムルコト. The form makes them joint co-borrowers each liable for the whole: 連帶債務者ノ內ニ於テ返金相成兼候時ハ三名ノ內壹名ニテモ引受ケ必ズ返金可仕候. No property is taken. 連帶借用人 are co-debtors rather than sureties in form, but they are third parties chosen for this loan who answer for it, which is what `surety` records; there is no closer value.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 77–78, 第一條–第十七條). No rule distributes an unmet loss among members. 第八條's reserve pays 費用 (see RD-test for the alternative reading under which this cell would be `residual-on-fund`). Silence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 78, 第十條, 第十三條, 第十六條; p. 79, 割濟金連帶借用之證). Coded on house practice (ko_mitarai_mujin_1773): the drawer and his three co-borrowers answer jointly for his 掛戾金 and the claim may be sued on or sold (第十六條). Same definitional objection as at 第六講. The rules do not say the 連帶借用人 must be members, so the stronger ground is not available.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 78, 第十四條, 第十六條, 第十七條; p. 79, 割濟金連帶借用之證). Sanctioned on both sides of the draw. Penalty interest: 第十四條 本講掛金ハ開會月內ニ出金セハ無利子ナルモ、翌月ニ渡ル時ハ翌日ヨリ日步百圓ニ付四錢ヲ徵收スルコト. Drawers: suit or sale of the claim (第十六條), costs on the debtor (第十七條), and in the form acceleration of the whole (割濟ノ契約ヲ取消シ壹時ニ全額ヲ辨濟可仕候). Unwon members (rule 5, recorded here): 第十六條 小掛者タリトモ掛込金ヲ怠リタルトキハ競賣スルコトアルベシ — his share may be sold (footnote 6 未取者の持口を他に賣ること).

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 77–78, 第二條, 第七條, 第十一條, 第十五條). The fund is handled by officers: 第七條 本講金取扱ハ世話人ニ於テ扱フモノトシ、世話人四名及ビ取締人一名ヲ置クコトトス; they pay the 會主 (第十一條), are consulted on the choice of co-borrowers (第十三條) and on transfers (第十五條). The 會主 is named in the rules (第二條 本講會主ヲ甲野丙吉ト定メ) as the maker and seller of the steles. How officers are chosen and who decides over the fund are not stated. ALTERNATIVE: `external-administered`, if the 會主 (an outside supplier, on the 解說's account) is taken to run the kō; rejected because the rules give him the meeting and the sale, and the money to the 世話人.

### 第33講 加茂川原昭和講 (靜岡縣磐田郡富岡村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 82, 會則 items 7, 10; 年賦金借用證書). Silent beyond the drawer's own security. The drawer gives a bond with 貳名以上ノ連帶債務者 who must be 世帶主又ハ講員 (會則 item 10). Under rule 1 they are security chosen for this loan, RB3's ground, even when they are members: they bind by signing. The form gives the creditor every remedy against the signatories (如何ナル御處分ニ及フモ異議申間敷…殘額及ヒ費用等一時ニ御取立下サレ度候) and names nobody after them. 會則 item 11 (總テ本講ハ共力一致シテ…御互ヒニ德義ヲ以テ本講ノ目的ヲ達成センコトヲ契約ス) is an exhortation, not a rule on who bears an unpaid residue; reading it as `all-members` would turn a statement of purpose into a liability clause. Applicability: payout creates a debt (form: 毎定日壹回ニ付キ金拾五圓宛必ラズ返濟可致候).

- **`RB3` = `surety`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 82, 會則 item 10; 年賦金借用證書). 一、落札者ハ落札セシ次回ヨリ終回ニ致ル掛金ノ辨濟證書ヲ貳名以上ノ連帶債務者ヲ以テ作製ノ上落札金ノ給付ヲ受クルモノトス、但シ連帶債務者ハ世帶主又ハ講員タルコト (item 10). The form is a joint bond (右金額我等連帶ニテ借用候處實證也). No property is taken. Joint co-debtors chosen for this loan; `surety` is the value for third parties standing behind the drawer.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 81–82, 會則 items 1–11). No rule distributes an unmet loss. 一、糶金ハ口數ニ平等ニ分配ス (item 9; footnote 4 糶金は入札差金) divides the bid surplus; it is not a loss rule. Silence.

- **`LS3` = `1`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 82, 會則 item 10; 年賦金借用證書). A member may be bound for another's draw: the co-debtors must be 世帶主又ハ講員 (item 10), and they are jointly liable for the whole remaining 年賦金 and costs (form: 殘額及ヒ費用等一時ニ御取立下サレ度候). Medium because 又ハ makes membership one option, not a requirement; where the co-debtors are household heads outside the kō, the ground falls back to house practice (the drawer's own bond answering for his debt).

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 82, 會則 item 7; 年賦金借用證書). Any member who does not pay on the day is fined: 一、掛金ハ壹口金拾五圓トシ毎定日ニ會場迄持參拂込ムモノトス、但シ當日不拂者ハ過滯金五拾錢宛申受クルモノトス (item 7); for an unwon member (rule 5, recorded here) that fine is the only stated sanction. For a drawer, one missed date opens every remedy and accelerates the debt: 若シ一定日ニ於テ返金出來兼ネ候節ハ我等ニ對シ如何ナル御處分ニ及フモ異議申間敷其ノ場合ニ於テハ當時ノ返金額ハ勿論殘額及ヒ費用等一時ニ御取立下サレ度候 (form).

- **`GV1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 81, 會則 items 1, 3). The kō is 加茂川原煙草耕作組合ノ主催 (item 1) and run day to day by 世話人四名 who 講ノ事務ヲ掌リ (item 3). How the 世話人 are chosen, and whether the 組合 has any power over the fund, are not stated. ALTERNATIVE: `external-administered`, reading 主催 as administration by a body outside the subscribing members. Rejected on two grounds: 主催 says the 組合 sponsors the kō, not that it decides over the fund; and on the 解說's account the members are themselves 組合員, so the 組合 is not clearly outside the subscribing body. Silence on the locus.

### 第35講 吉武信用貯金講會 (福岡縣宗像郡吉武村)

- **`RD-test` = `fund`** (confidence low, articulation articulated; 農林省經濟更生部 1936, p. 93, 規則 第九條 (as amended 昭和九年); p. 88, 第七條; pp. 94–95, 金借用證書 items 五, 九). LOW, and the cell turns on one phrase. Amended 第九條 makes every drawer deposit a reserve against arrears: 本講會當籤者ハ貸付ヲ受クル際本講會掛不足整理費トシテ金參圓ヲ講會ニ供託シ置クモノトス、此押ヘ金ハ整理費ヲ控除シ殘金ハ滿會ノ際會員平等ニ分配スルモノトス, and the interest on the kō's deposits 押ヘ金ト見做シ講會費用ニ備ヘ. The drawer's own security comes first and is RB3's ground: property (第七條) and 連帶保證人 who answer as independent debtors (金借用證書 item 九 連帶保證人ハ…獨立ノ債務ヲ負擔シタルモノト看做シ其ノ履行ノ責ニ任シ可申候). After that the only provision for 掛不足 is the 押ヘ金 reserve, so on my reading the fund absorbs the shortfall and the remainder is shared out at the end. WHY LOW: 掛不足整理費 can be read as a charge for the expense of clearing up arrears, not as money that makes the arrears good; on that reading the clause is a costs clause and the cell is .NR. I read it as the latter because its object is 掛不足 itself, not 訴訟 or 費用 in general. TWO FURTHER DECISION POINTS. (i) The same 第九條 says 講會加盟者ニシテ掛込金ヲ怠リタルトキハ未取者（子）ハ本人ノ本會ニ於ケル抽籤權ヲ除キ取親（親）ナルトキハ其部落加盟者全部ノ抽籤權ヲ除クモノトス: when a drawer (footnote 2) defaults, every member of his 部落 loses his right to draw. That is a sanction that falls on a standing group by belonging, which is the rule-1 test for `standing-subgroup`, but it makes no one liable for the sum; I record it here and do not code it as the bearer. ALTERNATIVE: `standing-subgroup`, if collective pressure by belonging is read as the answer to 'who bears it'. (ii) The 解說's 實際には概ね部落保證を徵してゐる would support `standing-subgroup` in practice; it is the ministry's account, not the rules, and is not used. LS1 = residual-on-fund rests on the same clause; the two cells are one fact.

- **`RB3` = `mixed`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 88, 規則 第七條; pp. 94–95, 金借用證書 items 五, 九). Property and surety together. 第七條 本講金貸與ヲ受ケタルモノハ貸付金ノ三分ノ一ノ地價ヲ有スル田、畑、山林、貸付金ト同額ノ地價ヲ有スル宅地、貸付金ノ一倍半ノ時價ヲ有スル有價證券又ハ貸付金ト同額以上ノ吉武信用購買販賣利用組合ノ貯金證券ヲ担保トシテ提供スベシ 但シ支配方ニ於テ適當ト認メタル場合ハ三人以上ノ連帶保證人アル場合ニ限リ前記担保ヲ供セズシテ貸付スルコトアルベシ (footnote 3: 地價は法定地價). The 金借用證書 that every borrower signs carries 連帶保證人 (six signature lines), who must be replaced if they lose 資力又ハ信用 (item 五) and who answer as independent debtors (item 九). So the ordinary case is property plus sureties, with sureties alone (three or more) by the 支配方's dispensation. `mixed` carries both mixtures (several kinds of property, and property plus surety).

- **`LS1` = `residual-on-fund`** (confidence low, articulation articulated; 農林省經濟更生部 1936, p. 93, 規則 第九條 (as amended 昭和九年)). ONE CLAUSE, TWO CELLS: this cell and RD-test = fund rest on the same words, as RD-TEST-DEFINITION.md requires. Amended 第九條: 本講會當籤者ハ貸付ヲ受クル際本講會掛不足整理費トシテ金參圓ヲ講會ニ供託シ置クモノトス、此押ヘ金ハ整理費ヲ控除シ殘金ハ滿會ノ際會員平等ニ分配スルモノトス. On my reading arrears are met from the 押ヘ金 reserve, and what is left is divided equally at the end. Low for the reason stated at RD-test: if 整理費 means only the cost of dealing with arrears, there is no loss rule and the cell is .NR. ALTERNATIVE: `equal`, on the ground that a loss absorbed by the reserve reduces each member's equal share of what is returned at 滿會 (會員平等ニ分配). Rejected because the clause allocates what is LEFT of the reserve, not the loss; the loss stops at the reserve. Beyond the reserve the rules are silent.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 88, 規則 第七條; pp. 94–95, 金借用證書 items 六, 九). Coded on house practice (ko_mitarai_mujin_1773): the drawer's land, securities or 組合 savings certificates and his 連帶保證人 answer for his debt, with acceleration on attachment, auction, bankruptcy or 'harm to the 組合's claim' (金借用證書 item 六 左ノ場合ニハ期限內ト雖モ貴組合ノ御請求次第即時元利金返濟可致候). Definitional objection as at the first kō coded: what is secured is the repayment he agreed to. The guarantors are not required to be members, so the stronger ground is not available. NOTE: the 金借用證書 is addressed to 貴組合 (the 組合), which is not the kō; whether the debt is owed to the kō or to the 組合 is not settled by the rules, and this matters for RD-test's applicability. I take it as a debt to the kō because 第六條 says the kō lends (本講會ヨリ貸付シタル金員) and the loan application is addressed to 吉武信用講支配人.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 93, 規則 第九條 (as amended); pp. 94–95, 金借用證書 items 四, 六, 七). Sanctioned on both sides of the draw. Unwon members (rule 5, recorded here): under amended 第九條 an undrawn member who fails to pay loses his own right to draw at the 本會 (未取者（子）ハ本人ノ本會ニ於ケル抽籤權ヲ除キ). The unamended text was harsher: 加盟者ニ於テ掛込金ヲ爲サヾルトキハ本講會員ヲ除名シ殘加盟者ニ於テ其掛込權利ヲ競賣ニ附シ落札金ハ本講會ノ所得トス (p. 88), superseded from 昭和九年二月八日. Drawers: penalty damages from the day after default (金借用證書 item 四 支拂遲滯致候節ハ期日ノ翌日ヨリ損害金トシテ…賠償可致候), acceleration (item 六), costs of suit including counsel on the borrower (item 七), sureties as independent debtors (item 九), and the 部落-wide suspension of draw rights (amended 第九條).

- **`GV1` = `external-administered`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 93, 規則 第二條 (as amended); p. 88, 第五條, 第七條; p. 89, 第十三條; p. 93, 第九條). The fund is run, ex officio, by officers of another body. Amended 第二條: 本講會ニ支配人及監査人ヲ置キ支配人ハ吉武信用購買販賣利用組合ノ理事部長是ニ當リ本講會ノ進行事務ヲ司リ監査人ハ同組合ノ監事是ニ當リ本講會全部ニ亘リ監査ヲナスモノトス (the unamended text had 支配方ハ…組合理事是レニ當リ). The 支配方 judge security and may waive it (第七條), the draw is held 支配方、監査人立會ノ上 (第五條), the kō's money is deposited in the 組合 (amended 第九條), and loans go first to pay debts owed to the 組合 (第六條 本講會ヨリ貸付シタル金員ハ先ヅ第一ニ吉武信用購買販賣利用組合ニ對スル債務ノ辨濟ニ充當シ). Against this, the members amend the rules: 第十三條 本講々則ノ變更ハ會員ノ半數以上ノ同意アルコトヲ要ス. Medium for two reasons: (i) that is a collective decision rule, and the ALTERNATIVE is `collective`; I code the body that decides over the fund day to day rather than the body that may change the rules; (ii) the 組合 is not wholly outside the subscribing body, since many members are 組合員 (第三條 as amended), though the officers are appointed by their office in the 組合, not chosen by the kō. The 解說 calls the kō 獨立の全く別個のもの; the rules say otherwise about who runs it, and I code the rules.

### 第37講 岡龍無盡 (秋田縣由利郡平澤町)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 98–99, 第四條, 第五條, 第七條, 第八條, 第十條, 第十五條; p. 99, 玄米借用證). Applies, and silent beyond the drawer's own security. The payout (rice) creates a debt: the form binds the drawer to 毎年拾壹月廿九日參等玄米壹俵宛滿會迄無遲滯返米. His security is 連帶保證人 (第四條), two of them where he also pledges land or a 信用組合 deposit certificate (第五條), and for the 講親 a 宿保證人 (第十五條; footnote 10 宿保證人は講親保證人をいふ); all RB3's ground. The form adds the guarantors' undertaking that the members will not suffer: 萬一壹回タリトモ相滯候節ハ連帶者ハ本人ニ成リ替リ聊モ御連中ニハ御迷惑相懸申間敷候. That says who must NOT bear the loss (御連中), not who bears it if the guarantors fail, so it is not `all-members` and is not `fund`. 第七條 gives the 世話人 出訴ノ權 against 不掛ノ者; 第八條 puts costs of suit on the defaulter (rule 4); 第十條 keeps 毎回金壹圓 for 臨時費又ハ訴訟費用 — a reserve for costs, not for the defaulted rice. Nothing names a bearer beyond the guarantors.

- **`RB3` = `mixed`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 98, 第四條, 第五條; p. 99, 第十五條, 玄米借用證). Surety always, property in addition. 第四條 取入主ハ自己ニ對スル保證人ヲ前以テ豫メ定メ置キ取入ノ節不都合ナキ樣可致事 但連帶保證人無キ爲メ取入兼候トキハ次會ヨリ五ケ年間鬮札入ルヽ事ヲ不得; 第五條 取入者ニシテ抵當ヲ差出シタル者ハ保證人貳名トス 但未掛米ニ對スル田ハ五畝步、畑宅地ハ未掛米拾俵ニ對スル地價金五圓トス 信用組合ノ預金證ハ金貳百圓ト定ム. The form 玄米借用證 takes 此爲抵當平澤町信用購買販賣利用組合ノ…預金證書壹通 (又ハ) … 田、畑、宅地 何段何畝何步 and is signed by 落取主 and 保證人. The 講親's own performance is guaranteed by a 宿保證人 (第十五條).

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 98, 第十條, 第十一條). No rule distributes an unmet loss. 第十條 臨時費又ハ訴訟費用等ニ要スルタメ毎回金壹圓宛積置キ餘金ハ滿會ノ節一同配分スルモノトス divides what is left of a costs reserve; 第十一條 takes 配當金 from the 鬮餘リ米 (footnote 6). Neither is a loss rule.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 98, 第四條, 第五條; p. 99, 玄米借用證). Coded on house practice (ko_mitarai_mujin_1773): the drawer's land or deposit certificate and his guarantors answer for his rice debt. Definitional objection as at the first kō coded: what is secured is the repayment he agreed to. The guarantors are not required to be members, so the stronger ground is not available.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 98, 第四條, 第七條, 第八條, 第九條). Sanctioned on both sides of the draw. Drawers: suit by the 世話人 (第七條 不掛ノ者有ル節ハ出訴ノ權ヲ擔當可致), with all costs on the defaulter (第八條 取入者ニシテ不掛ノタメ訴訟ノ節ハ訴訟費用ハ勿論世話人若クハ代理人ノ旅費日當共一切不掛者ニ於テ負擔可致者トス), and guarantors who stand in his place (form). Unwon members (rule 5, recorded here): 第九條 不取ノ者ニシテ二回不掛致シタル者ハ掛詰メ米返米不致シテ除名可致事 — expulsion with forfeiture of the rice paid in (footnote 4). A would-be drawer who cannot find a guarantor is barred from bidding for five years (第四條 但書).

- **`GV1` = `collective`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 98–99, 第六條, 第十四條, 第十六條, 第十七條). The membership elects the officers, controls transfers and changes the rules by majority. 第六條 證券名宛人壹名、證券預リ人壹名、世話人參名選擧ヲ以テ決定ス; 第十四條 transfer 連中ノ承諾ヲ得タル (footnote 9 講員(連中)の承認); 第十六條 本無盡會則ハ連中協議ノ上變更スル事アルベシ; 第十七條 本無盡會則ハ連中過半數ヲ以テ取極メタル條件ニ付後日不服ヲ唱フル事ヲ得ス. The 世話人 run the business and hold the right to sue (第七條) under that mandate.

### 第39講 根津忠一郎企米無盡 (秋田縣鹿角郡曙村)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 106, 第四條–第七條). Applies, and silent beyond the drawer's own security. The draw is a loan of rice (第四條 積米ノ貸付), so it creates a debt. The drawer gives 戸主三名以上ノ保證アル證書 (第四條), RB3's ground. On default: 第六條 鬮取人ニ於テ掛米ヲ延滯シタルトキハ藏元ハ評議員會ノ決議ニ依リ正當ノ手續ニ依リ之レヲ徵收スルモノトス、此ノ場合ニ於ケル一切ノ費用ハ鬮取人ノ負擔トス (footnote 7: 鬮取人 = 既取人) — collection and costs against the defaulter himself (rule 4). The rules name no bearer once that fails. NOT TO BE MISREAD: 第七條 makes all members take over an expelled member's share (該株ニ對スル一切ノ權利義務ヲ加入者一同ニテ繼承スル), which would be `all-members` if it applied to drawn members; but it applies to 生株者 (footnote 8: 未取者), so it is an unwon member's default and belongs to CN3 under rule 5. Recorded there. 第五條's 差額米ハ落札者ニ於テ負擔 is a winner who fails to give his bond (rule 4).

- **`RB3` = `surety`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 106, 第四條). 第四條 鬮取リニ依リ積米ノ貸付ヲ受ケントスルモノハ戸主三名以上ノ保證アル證書ヲ藏元ニ差出シ承認ヲ經タル後貸付ヲ受クルモノトス 但シ藏元ニ於テ必要アリト認メタルトキハ證人ノ定數ヲ增減セシムルコトヲ得. Three or more household heads as guarantors, the number adjustable by the 藏元 (footnote 5: 役員、世話人); no property is taken.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, pp. 106–107, 第一條–第十條). No rule distributes an unmet loss on a drawn member's default. 第七條's 加入者一同ニテ繼承 is the one place where members collectively take on a defaulter's obligations, and it is an unwon member's share (see RD-test and CN3); it states who takes it over, not how it is divided among them, and it does not concern a loss after the pool is exhausted. Silence.

- **`LS3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 106, 第七條). Members are exposed beyond their own agreed contribution for another member's obligations: 第七條 生株者掛米ヲ延滯シタルトキハ會ノ決議ニ依リ之ヲ除名ス、此場合ニ於テハ該株ニ對スル一切ノ權利義務ヲ加入者一同ニテ繼承スルモノトス 除名ヲ受ケタルモノ、既納掛米ハ無盡終了後之ヲ返付ス. When an undrawn member is expelled, the remaining members inherit his share's duties, including its remaining contributions and the refund of what he paid in. This is a direct, articulated exposure, not the house-practice reading of a drawer's own security; the 戸主 who guarantee drawers (第四條) are not said to be members, so they are not relied on here.

- **`CN3` = `1`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 106, 第四條, 第六條, 第七條). Sanctioned on both sides of the draw. Drawers: collection 正當ノ手續ニ依リ on the 評議員會's decision, costs on the drawer (第六條), against three household-head guarantors (第四條). Unwon members (rule 5, recorded here): 第七條 生株者掛米ヲ延滯シタルトキハ會ノ決議ニ依リ之ヲ除名ス — expulsion by decision of the meeting; his share's rights and duties pass to 加入者一同, and the rice he paid in is returned only after the kō ends (既納掛米ハ無盡終了後之ヲ返付ス).

- **`GV1` = `collective`** (confidence high, articulation articulated; 農林省經濟更生部 1936, pp. 106–107, 第六條, 第七條, 第八條, 第十條). Officers are chosen by the general meeting and act on the meeting's or council's decisions. 第十條 本會ニ藏元二名評議員三名ヲ置キ總會ニ於テ之ヲ定ム 藏元ハ本會ノ業務一切ノ取締ニ當ル 評議員ハ藏元ノ業務ヲ應援ス; collection against a defaulting drawer is on the 評議員會ノ決議 (第六條); expulsion of an unwon member is by 會ノ決議 (第七條); a transfer needs 會員一同ノ承認 (第八條). The 企人 (footnote 4: 講親) hosts the meetings (第三條) and takes a fee from each drawer (第九條), with no stated decision power.

### 第43講 愛宕社講 (靜岡縣富士郡富士町)

- **`RD-test` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 118, 第五條; pp. 118–119, 割濟米連帶借用之證). Applies, and silent beyond the drawer's own security. The shrine levy (第三條) does not make the kō a pure donation scheme: the pot is drawn by a member (第五條) and repaid in instalments (form: 割濟), so a debt to the fund exists. Security: 落札人ハ連借證書ニテ猶ホ堅固ナル事ヲ計リ世話人指名ノ連借四名記載スル事 (第五條), co-borrowers named by the 世話人, which is RB3's ground (rule 1). The form makes them answer one for all: 萬一連帶債務者ノ內ニ於テ返米相成兼候時ハ參名ノ內誰彼ヲ問ハズ一名ニテモ引受必ズ返米可仕候聊タリ共御損毛相懸申間敷候. That promises the 世話人 no loss; it does not say who bears it if the co-borrowers fail. Nothing in the 講則 does.

- **`RB3` = `surety`** (confidence high, articulation articulated; 農林省經濟更生部 1936, p. 118, 第五條; pp. 118–119, 割濟米連帶借用之證). 第五條 本講ハ鬮講トシ最低ノ一本籤トシ、落札人ハ連借證書ニテ猶ホ堅固ナル事ヲ計リ世話人指名ノ連借四名記載スル事 但シ落札米ハ證書引替ノ事. No property is taken. A DISCREPANCY IN THE INSTRUMENT, recorded and not resolved: the 講則 require four co-borrowers (連借四名), the form provides three 連帶借用主 lines and speaks of 參名ノ內. Whether the drawer counts as one of the four is not stated. The value does not depend on it.

- **`LS1` = `.NR`** (confidence .NR, articulation .NR; 農林省經濟更生部 1936, p. 118, 第一條–第十條, 附則). No rule distributes an unmet loss. 第三條's levy of 精米壹升 per 口 for the shrine is a contribution to a third party's fund, not a loss rule and not a reserve of the kō. Silence.

- **`LS3` = `1`** (confidence medium, articulation analyst-imposed; 農林省經濟更生部 1936, p. 118, 第五條; pp. 118–119, 割濟米連帶借用之證). Coded on house practice (ko_mitarai_mujin_1773): the drawer and his co-borrowers answer jointly for his rice debt, accelerated on a single default (割濟ノ契約ヲ取消一時ニ全額ヲ辨濟可仕候). Definitional objection as at the first kō coded. The 連借 are named by the 世話人 and are not said to be members (the rules' word for members is 連名, footnote 5), so the stronger ground is not available.

- **`CN3` = `1`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, pp. 118–119, 割濟米連帶借用之證). The consequence of a drawer's default is stated in the form: 若期日ニ到リ壹回タリトモ相滯候節ハ割濟ノ契約ヲ取消一時ニ全額ヲ辨濟可仕候, the co-borrowers answer one for all, and suit is contemplated (該債務不履行ノ爲メ訴訟ヲ提起スル場合ハ貴殿所在地ヲ管轄スル裁判所ヲ以テ裁判籍トナル事ヲ承諾仕候). Unwon members (rule 5): nothing stated beyond the duty to bring rice (第三條, 第八條); no sanction for a 小掛 who stops paying. Medium because the sanction is only in the form, and only for drawers.

- **`GV1` = `collective`** (confidence medium, articulation articulated; 農林省經濟更生部 1936, p. 118, 第五條, 第六條, 第七條, 第十條). The members amend the rules by majority, subject to the 世話人's consent: 第十條 右講則中改正ノ必要アリト認メタル時ハ連名半數以上ノ決議ニヨリ世話人ノ承諾ヲ經テ變更スル事ヲ得 (footnote 5 連名は加入者の意). Day to day the two 世話人 attend in turn (第六條) and name the co-borrowers (第五條); 檢査役 rotate among the members in roll order (第七條; footnote 6). Medium: the 世話人 hold a veto over amendment, and how they are chosen is not stated. ALTERNATIVE: .NR, reading a member majority subject to an officer's consent as no fitting value.

## 3. The matrix, computed after all 102 cells were fixed

Values, with confidence in brackets where it is not `high` (and not `.NR`):

| kō | name        | RD-test                    | RB3             | LS1                    | LS3        | CN3        | GV1                            |
|----|-------------|----------------------------|-----------------|------------------------|------------|------------|--------------------------------|
| 6  | 山野草平取建頼母子   | .NR                        | mixed           | .NR                    | 1 (medium) | 1          | collective (medium)            |
| 7  | 昭和講         | standing-subgroup (medium) | surety (medium) | .NR                    | 1 (medium) | 1 (medium) | .NR                            |
| 12 | 春山夏助長壽講     | officers (medium)          | mixed (medium)  | .NR                    | 1 (medium) | 1 (medium) | .NR                            |
| 14 | 深井朝右衞門發起頼母子 | .NR                        | surety          | .NR                    | 1          | 1          | .NR                            |
| 15 | 權田太郎兵衞發起頼母子 | .NR                        | mixed           | .NR                    | 1          | 1          | collective (medium)            |
| 18 | 山坂昇講        | .NR                        | mixed           | .NR                    | 1 (medium) | .NR        | .NR                            |
| 21 | 共同信用講       | .NR                        | mixed           | .NR                    | 1 (medium) | 1          | .NR                            |
| 23 | 昭和御大典記念講    | .NR                        | mixed (medium)  | .NR                    | 1 (medium) | 1          | collective                     |
| 25 | 親睦講         | all-members (low)          | real-estate     | .NR                    | 1 (low)    | 1          | collective (medium)            |
| 26 | 正利講親無金無盡    | deferred (medium)          | mixed (medium)  | .NR                    | 1 (medium) | 1          | collective                     |
| 27 | 蒲團講         | .NR                        | surety          | .NR                    | 1          | .NR        | .NR                            |
| 31 | 富士石碑講       | .NR                        | surety          | .NR                    | 1 (medium) | 1          | .NR                            |
| 33 | 加茂川原昭和講     | .NR                        | surety          | .NR                    | 1 (medium) | 1          | .NR                            |
| 35 | 吉武信用貯金講會    | fund (low)                 | mixed           | residual-on-fund (low) | 1 (medium) | 1          | external-administered (medium) |
| 37 | 岡龍無盡        | .NR                        | mixed           | .NR                    | 1 (medium) | 1          | collective                     |
| 39 | 根津忠一郎企米無盡   | .NR                        | surety          | .NR                    | 1          | 1          | collective                     |
| 43 | 愛宕社講        | .NR                        | surety          | .NR                    | 1 (medium) | 1 (medium) | collective (medium)            |

Distribution:

| characteristic | values (count)                                                             | confidence (count)       |
|----------------|----------------------------------------------------------------------------|--------------------------|
| RD-test        | .NR 12, standing-subgroup 1, officers 1, all-members 1, deferred 1, fund 1 | .NR 12, medium 3, low 2  |
| RB3            | mixed 9, surety 7, real-estate 1                                           | high 13, medium 4        |
| LS1            | .NR 16, residual-on-fund 1                                                 | .NR 16, low 1            |
| LS3            | 1 17                                                                       | medium 12, high 4, low 1 |
| CN3            | 1 15, .NR 2                                                                | high 12, medium 3, .NR 2 |
| GV1            | collective 8, .NR 8, external-administered 1                               | .NR 8, medium 5, high 4  |

64 substantive cells, 38 `.NR`, 0 `.NA`, no `0` (`RD-test`, `RB3` and `LS1` have no `0`; on `LS3` and `CN3` no observed absence was found).

By component: **loss-sharing** (`RD-test`, `LS1`, `CN3`): `RD-test` 5 of 17 substantive, `LS1` 1 of 17, `CN3` 15 of 17. **owner-shielding** (`RB3`, `LS3`): 17 of 17 each. **none** (`GV1`, description only): 9 of 17. The loss-sharing component is where the rulebooks are silent; the owner-shielding component is full but, for `LS3`, uninformative (answer 5).

## 4. The six answers

### Answer 1. What was coded, and on what evidence

All 102 cells (17 kō × 6 characteristics) were coded, from the printed rules and the printed forms of each kō on the pages `FRAMES.md` lists, read whole for each kō (`source_read = full` on every row). Every substantive cell quotes the clause it rests on, in the original script, with printed page and article. The ministry's 解說 was used only for facts the rules do not state — place, date of foundation, whether the kō was running, the size of the pot — and each cell or reading record says so where it was used. No cell rests on a heading, a ministry class, a 解說's interpretation, or a footnote's gloss of a clause (footnote glosses of single words such as 子は未取者 were used to read the clauses, and are cited where they are).

Substantive values: `RD-test` 5 (`standing-subgroup` at 第七講, `officers` at 第十二講, `all-members` at 第二十五講, `deferred` at 第二十六講, `fund` at 第三十五講; two of the five are low confidence); `RB3` 17 (`mixed` 9, `surety` 7, `real-estate` 1); `LS1` 1 (`residual-on-fund` at 第三十五講, on the same clause as `RD-test = fund`, both low); `LS3` 17 (`1` throughout; 9 analyst-imposed on house practice, 8 articulated on a stronger ground); `CN3` 15 (`1`); `GV1` 9 (`collective` 8, `external-administered` 1).

### Answer 2. What could not be coded, and why

38 cells are `.NR`; none is `.NA`; none is `0`.

- **`RD-test`, 12 `.NR`.** In each the rules take security from the drawer — guarantors, co-borrowers, a mortgage or both — and stop. No clause names who bears what remains once that security fails. Two of the twelve (第十四講 第拾五條, 第十五講 第二十二條) send everything the rules do not cover to 地方賴母子ノ慣例; rule 6 forbids coding what custom would supply, so they are `.NR`, but they are a different kind of silence from a rulebook that says nothing, and the note says so. Four keep a reserve: three state its use as costs (第二十三講 第十四條, 第三十一講 第八條, 第三十七講 第十條), which I did not read as absorbing the defaulted sum, and one states no use (第十八講's 積立金, a deduction from each pot); 第三十一講 第八條 is the closest call and its alternative reading (`fund`) is stated. **No `.NA`:** in every kō the payout created a debt to the fund, including the in-kind and purpose kō (第二十七講 bedding money, 第三十一講 a stone monument, 第三十七講, 第三十九講 and 第四十三講 rice).
- **`LS1`, 16 `.NR`.** No rule in the seventeen divides an unmet loss among members by any ratio. The only distribution clauses divide surpluses (bid discounts, reserve balances, the 講親's interest), and I declined in every case to read a surplus clause as a loss clause. Where a bearer is named (第七講, 第十二講, 第二十五講) the division among the bearers is not.
- **`CN3`, 2 `.NR`** (第十八講, 第二十七講): security is taken but no consequence of non-payment is stated, which house practice (`ko_mitarai_mujin_1773`) reads as `.NR`. See answer 5 for the inconsistency this creates with two of my own cells.
- **`GV1`, 8 `.NR`.** Officer-run kō whose officers' mandate, and the body that chooses them, are not stated (第七講, 第十二講, 第十四講, 第十八講, 第二十一講, 第二十七講, 第三十一講, 第三十三講). The vocabulary has no value for a board of officers acting on an unstated mandate, and house practice is `.NR`.

### Answer 3. Which of my priors were falsified

Quoted verbatim from `PRIORS-residual-default-filled-2026-10-22.md`.

- > `RD-test`: `.NR` in about 11; `officers` in about 2–3; `all-members` in about 2; `deferred` in about 1; `standing-subgroup` 0–1; `fund` 0–1; `.NA` 0–1 (a purpose kō with no payout to members).

  Roughly held: `.NR` 12, and each of the five values once. `officers` and `all-members` were overestimated; `.NA` never occurred.

- > **Most often:** `officers` (a 講元, 親, 發起人 or 世話人 named as liable once the guarantors fail), narrowly ahead of `all-members`. **Not at all:** `standing-subgroup`, with `21 共同信用講` the one place I would not be surprised to see it.

  **Falsified.** No value occurred more than once. `standing-subgroup` did occur — at 第七講 昭和講, through its 講クビリ, and not at 第二十一講, which is `.NR`.

- > **How many state who bears a drawn member's default beyond his own security?** About 5 of the 17.

  Held: 5 (第七講, 第十二講, 第二十五講, 第二十六講, 第三十五講), two of them at low confidence.

- > `RB3`: `surety` in about 9; `mixed` in about 5; `real-estate` in about 1; `none` in about 0–1; `.NR` in about 1–2.

  **Falsified** in direction: `mixed` 9, `surety` 7, `real-estate` 1, `.NR` 0. Property was taken more often than I expected — though three of the nine `mixed` are alternatives or splits, not property and surety together (answer 4).

- > `LS1`: `.NR` in about 13; `pro-rata` in about 2; `equal` in about 1; `residual-on-fund` 0–1.

  **Falsified** on the division values: no `pro-rata`, no `equal`; `.NR` 16.

- > `LS3`: `1` in about 10; `.NR` in about 6; `0` in about 0–1; `P` 0–1.

  **Falsified:** `1` in all 17. Every rulebook takes security from the drawer, and house practice reads that as `1`.

- > `CN3`: `1` in about 14; `P` in about 2 (forfeiture of the draw only); `.NR` in about 1; `0` none.

  Partly falsified: `1` 15, `.NR` 2, **no `P`**. 第七講 is the one candidate for `P`, and it is the cell I flag as inconsistent in answer 5.

- > `GV1`: `collective` in about 7; `.NR` in about 8; `elder-fixed` in about 1; `external-administered` in about 1.

  Held: 8, 8, 0, 1.

- > **6 山野草平取建頼母子.** 取建 suggests a kō raised for the relief of a named person (a 親頼母子). Expect the beneficiary-organiser problem on `GV1` (`.NR`, as `ko_mochiyori_yutsu_1876`), and possibly the 親 or 世話人 named for residual loss.

  **Falsified.** `GV1 = collective`: the rules give the 講親 no power over the fund and put it in officers elected by 惣會員 and in 協議. No one is named for residual loss.

- > **14 深井朝右衞門發起頼母子, 15 權田太郎兵衞發起頼母子.** 發起 names a promoter; I expect the 發起人 to carry duties and possibly a guarantee, which could make `RD-test = officers`.

  **Falsified** for both: `.NR`, and both refer the gap to local custom. The one `officers` cell (第十二講) has the 世話人 guaranteeing the convener, not the convener guaranteeing anyone.

- > **21 共同信用講.** 共同信用 suggests joint liability; the likeliest kō in the set for `all-members` or `standing-subgroup` on `RD-test`, and for `LS1` to be coded.

  **Falsified.** `RD-test` and `LS1` are both `.NR`. The name predicted nothing; its rules stop at two guarantors and a pledge.

- > **25 親睦講.** Fellowship framing; I expect lighter security and possibly `deferred` or `.NR` on `RD-test`.

  **Falsified.** Security is a registered mortgage on rice land at a stated ratio, and `RD-test = all-members` (low).

- > **31 富士石碑講.** A kō for a stone monument; possibly no payout to members at all, in which case `RD-test`, `RB3` and perhaps `LS3` could be `.NA`. This is the likeliest `.NA` kō.

  **Falsified.** The stele is a payout in kind to the drawer, who then owes 掛戾金 on three co-borrowers' bond.

- > **35 吉武信用貯金講會.** Twelve printed pages and a 信用・貯金 name: the most detailed rulebook, and the likeliest to have a reserve (積立金) and so `RD-test = fund` with `LS1 = residual-on-fund`, and the likeliest `GV1 = collective`.

  Reserve, `fund` and `residual-on-fund` held, at low confidence, on a reserve called 押ヘ金 rather than 積立金. **`GV1` falsified:** the fund is run ex officio by the 信用組合's officers (`external-administered`, medium).

- > **37 岡龍無盡, 39 根津忠一郎企米無盡.** 秋田 usage of 無盡; 39 is perhaps reckoned in rice (企米). No expectation on liability beyond `RB3 = surety`.

  第三十九講 `surety` held. 第三十七講 **falsified**: `mixed` (two guarantors plus land or a 信用組合 deposit certificate). Both are rice kō, as guessed for 39 only.

- > **43 愛宕社講.** A shrine kō; the shrine may be organiser or beneficiary, which would put `GV1` in the same gap as `ko_hokoin_1832`.

  **Falsified.** The shrine receives a levy of rice per meeting and has no role in running the kō; `GV1 = collective` (medium).

- > I have a general impression, not tied to any source I can name, that a 親 or 發起人 sometimes stood as guarantor of last resort, and that elsewhere the loss fell on the members not yet drawn.

  Neither pattern appears in these seventeen. The nearest is its inverse (第十二講: officers guarantee the 親). The undrawn members appear as beneficiaries of surpluses, never as bearers of a drawn member's default.

Priors that held without comment: 第二十七講 `RB3 = surety`; the view that `RD-test` would not be `.NA` for 第二十七講 on its name alone.

### Answer 4. Characteristics that did not fit the evidence

**`RD-test`.** Coded as defined throughout; the value set was not widened. Six places where the definition did not fit:

1. **Two regimes in one instrument (第十二講).** The convener's default is guaranteed by the 世話人 (第三條); the other nineteen drawers' defaults are not provided for (第六條). One cell per kō cannot hold both. I coded `officers` on rule 2 (the last bearer the instrument names) and stated the `.NR` alternative.
2. **Advance or bear (第七講).** The クビリ 立替ヘル — advance — the shortfall. The definition asks who is liable for what remains unpaid; an advance may be recovered. The クビリ is the last bearer named, so `standing-subgroup`, medium. The same kō also blurs rule 1's line between signing and belonging if the co-obligors on the 連帶借用證書 are the members of the drawer's クビリ, which the rules do not say.
3. **Penalised by belonging, not liable (第三十五講).** Amended 第九條 suspends every member of a defaulting drawer's 部落 from the draw. That is a sanction on a standing group by belonging — the rule-1 criterion for `standing-subgroup` — without any liability for the sum. The definition has no place for a group that is penalised but not made to pay. Not coded as the bearer; recorded.
4. **Costs or the debt (第二十五講, 第三十五講, 第三十一講).** Each rests on whether a word means the cost of pursuing a default or the defaulted sum: 損害費用 (第二十五講), 掛不足整理費 (第三十五講), 費用 in 第八條 (第三十一講). The definition is about the unpaid residue; a costs clause is not it. I read 第二十五講 and 第三十五講 as reaching the debt (low) and 第三十一講 as costs only (`.NR`); all three could go either way.
5. **Where `deferred` ends (第二十六講 against 第六講 and 第十五講).** I coded `deferred` only for a clause about default specifically (第二十六講 第十一條) and not for general amendment or 必要ノ事項 clauses. The definition does not say which. If general 協議 clauses count, 第六講 and 第十五講 move to `deferred`.
6. **Custom as the answer (第十四講, 第十五講).** Both rulebooks say that anything outside the rules follows 地方賴母子ノ慣例. Rule 6 makes that `.NR`, which I followed, but it is a third state — the instrument names custom as the decider — that is neither silence nor `deferred`.

**`RB3 = mixed` carries three different facts.** Property and surety on the same drawer (the vocabulary's definition: 第六講, 第十五講, 第十八講, 第二十一講, 第三十五講, 第三十七講); property *or* surety at the drawer's option (第二十三講, 第二十六講); and surety for one drawer, property for the others (第十二講). The second and third are not `mixed` as defined; there was no closer value, so they are coded `mixed` at medium and flagged. The existing note on `ko_mitarai_gin_1805` already warns that `mixed` carries two mixtures; on this evidence it carries four. Also: joint co-borrowers (連帶借用人, 連帶債務者) were coded `surety` (第三十一講, 第三十三講, 第四十三講); they are co-debtors in form.

**`LS3` against its own definition.** The definition says beyond what a member has contributed *or agreed to contribute*. A drawer's repayments are what he agreed to contribute, so security for them is, on a strict reading, not exposure beyond it. House practice (`ko_mitarai_mujin_1773`, `ko_mitarai_hanei_1840`) codes `1` on that ground, and I followed it in nine cells, marking them `analyst-imposed`, medium. The other eight rest on members answering for *other* members' debts (guarantors who must be members, クビリ, inheritance of an expelled member's share), which fits the definition without strain.

**`GV1`.** Three shapes it cannot hold: a board of officers with an unstated mandate (eight `.NR`); member amendment subject to an officer's veto (第四十三講, coded `collective`, medium); and a fund run ex officio by another body's officers while the members keep the power to amend (第三十五講, coded `external-administered`, medium, with `collective` as the alternative).

**`LS1`.** Where the instrument names a set of bearers (第二十五講 講員一同, 第七講 the クビリ), `LS1` has no value for "a named set, division unstated". Coded `.NR`.

### Answer 5. Dependence and well-formedness problems noticed and not repaired

1. **An inconsistency among my own `CN3` cells.** 第七講 and 第十二講 are `CN3 = 1` on instruments that state no consequence for the drawer who defaults (第十二講), or state only exclusion from the lot (第七講). 第十八講 and 第二十七講 are `.NR` on the same kind of instrument, following `ko_mitarai_mujin_1773`. I noticed this while coding 第十八講, edited the two earlier cells, recognised that this broke the fix-before-moving-on rule, and **reverted them** (§1.4). Not repaired. On the house rule the consistent values are 第十二講 `.NR` and 第七講 `P`; on the looser reading (a bond with sureties is compulsion in itself) 第十八講 and 第二十七講 become `1`. This needs a ruling, not a re-reading.
2. **`LS3` has no variance on this set and is predicted by `RB3`.** `LS3 = 1` in all seventeen. Under house practice any drawer's security makes `LS3 = 1`, so wherever `RB3` is substantive `LS3` follows: the mapping is a function on this set, and `LS3` adds nothing to it. Under the strict reading of its definition `LS3` would split 8 against 9, and the 9 would become `.NR`. Both characteristics carry `component = owner-shielding`, so any WP1 comparison running on that component double-counts. I propose nothing here; it is the kind of collinearity `check_dependence.py` reports without enforcing.
3. **`RD-test` depends on `RB3`.** `RD-test` asks what happens once the drawer's own security is exhausted; its applicability is defined by a payout debt and its object by `RB3`'s boundary (rule 1). If it enters the vocabulary, `applicability_on` should say so. On this set `.NA` never occurred, so the applicability condition is untested.
4. **One clause, two cells, three times.** `RD-test = fund` and `LS1 = residual-on-fund` at 第三十五講 rest on one clause (as the definition requires). `RD-test` and `LS3` at 第二十五講 rest on one clause, and so do `RD-test` and `LS3` at 第七講. These are not independent observations, and a loss-sharing comparison that counts them separately counts one sentence twice.
5. **Rule 5 hides collective liability for unwon members.** 第三十九講 第七條 makes 加入者一同 inherit an expelled undrawn member's share, and 第三十五講's 部落 sanction reaches undrawn members too. Rule 5 puts unwon defaults on `CN3`'s ground, but `CN3` asks only whether non-payment can be compelled. The fact that *all members* answer for an unwon member's default therefore has no cell in either characteristic; it survives only in notes (and, at 第三十九講, as the ground for `LS3`).
6. **One editor, one village.** Five pairs of kō come from one village or town (head of file), and all seventeen were selected 適當と認め得るもの by one office, transcribed verbatim only where legible, and anonymised. No comparative statement in this file treats agreement between kō as corroboration, and none should be made from this set without a second, independent selection.
7. **`RB3 = mixed`** (answer 4) is a well-formedness problem of the type `CHARACTER-CODING.md` test 1 describes: one value silently answering two questions (what kinds of security, and how they combine). Recorded, not repaired, per the rule against proposing the repair in the batch that motivates it.

### Answer 6. What to read next, and which cell it would move

- **The other 福岡 rulebooks in this volume that use 講クビリ.** The 解說 to 第七講 says クビリ 隨所に散見される in 福岡. A rule that says the クビリ 負擔 (bears) rather than 立替ヘル (advances) would move 第七講 `RD-test` from medium to high; one that shows 立替 is recovered from the defaulter would move it to `.NR`. Same editor, so it would clarify usage, not corroborate.
- **The 吉武信用購買販賣利用組合's own rules or minutes** (outside this volume). They would settle what 掛不足整理費 and 押ヘ金 were for, and whether 部落保證 (which the 解說 says was usual) was a rule. They would move 第三十五講 `RD-test` between `fund`, `standing-subgroup` and `.NR`, and `LS1` with it; and `GV1` between `external-administered` and `collective`.
- **Another 仙北郡 rulebook, or the original 規約 of 第二十五講,** to settle whether 損害費用 means damages and costs or costs only. It would move 第二十五講 `RD-test` between `all-members` and `.NR`, and the confidence of its `LS3`.
- **A maintainer ruling, not a reading,** on (a) whether a bond with sureties and no sanction clause is `CN3 = 1` — moves 第七講, 第十二講, 第十八講, 第二十七講; (b) whether `LS3` covers security for a drawer's own agreed repayments — moves nine `LS3` cells to `.NR`; (c) whether a general 協議 clause is `deferred` — moves 第六講 and 第十五講 `RD-test`.
- **An independent selection.** A second set of 1930s rulebooks not chosen by 農林省經濟更生部 — a prefectural survey, or the kō records of a single village — is what any comparative claim from these seventeen needs. It would not move a cell here; it would decide whether the distribution in §3 says anything about kō rather than about this editor's sample.
- **第五講 解說 (p. 13),** cross-referenced in four footnotes for 法定地價. It would move nothing: it explains a valuation ratio, not a liability.
