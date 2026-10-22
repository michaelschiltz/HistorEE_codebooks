# Shortlist: sources for a blind re-test of `RD-test` (2026-10-22)

Slug `residual-default-retest-scan`. A catalogue scan, not a selection brief: it names candidate sources for Chat A of a re-test and reads none of them. Written by the chat that coded and scored the first test (`residual-default-coding`), so that chat must not code the re-test.

## 1. What a re-test needs

From the scoring of 2026-10-22 (logbook 4) and the operator brief's rules:

- **Another selector.** Rulebooks chosen by someone other than 農林省經濟更生部.
- **Enough rulebooks.** In the 1936 volume about two in five rulebooks named a bearer beyond the drawer's security (8 of 21 in the open half, 5 of 17 in the reserve). Six eligible kō in at least four villages needs roughly fifteen rulebooks or more.
- **Readable on NDL and unread.** Unread by any session of this project, and readable online or through the transmission service (送信サービス).
- **A declared population.** The first test was on Shōwa rulebooks chosen by a regulator. A re-test on another period or another institution (十錢講, 模合) tests a different population, and the brief must say so before the coding.

## 2. Budget, and what was read

**Budget:** rung 0 (catalogue fields), rung 1 (hit lists of the NDL Digital Collections full-text search, titles and ids only, no snippets) and rung 2 (tables of contents), the last only to confirm that an item prints rulebooks. No page of any candidate was to be opened.

**Reconciled.** As budgeted, with one incidental exposure. The NDL viewer shows frame 1 when a table of contents is opened, so the covers or title frames of pids 956756, 1444166 and 1909099 were displayed; nothing else of them was. One search-result line quoted a bibliography's mention of the 1936 volume (pid 1219863). Exposure to the project's own record was by count: a term count over `logbook/`, `records/`, `datasets/`, `vocabularies/` and `CHANGELOG.md` for each candidate's title and pid, and the two matching lines of logbook 5 read to establish status.

## 3. Candidates

| # | source | selector | date | rulebook content (by table of contents) | access | prior exposure |
|---|--------|----------|------|------------------------------------------|--------|----------------|
| 1 | 大蔵大臣官房銀行課 編『無尽ニ関スル調査』 (pid 944336) | Finance Ministry, bank section | 1915 | 第二章 無盡講 239–276, with 附 無盡講會規約ノ數例 at 257–276; number of rulebooks not known (數例) | internet, public domain | 0 hits |
| 2 | 司法省調査部『世態調査資料』第三十六號 (pid 1909099) | Ministry of Justice research section, from court-district reports | c. 1942 | Aomori report: 附錄 二 講規約及證書（十錢講、賴母子講、和合講等） 73–82, and a section 五 借用證書 42. Tokushima report: 發起及規約の作成 114 and discussion, no appendix of rules in the TOC. Okinawa report: 模合, a different institution | 送信サービス (login) | 0 hits |
| 3 | the other forty numbers of 『世態調査資料』 (1938–1943) | as 2 | 1938–1943 | not checked; other regional kō reports are possible | mixed | 0 hits on the series |
| 4 | 池田竜蔵『稿本無尽の実際と学説』 (1930, pid 1444166; 1918, pid 956756) | private author, published by the licensed industry's association | 1918, 1930 | 第三卷 無盡研究資料 365 and 附錄; whether rulebooks are printed is not shown | 1930 internet; 1918 per logbook 5 restricted | **listed in logbook 5**; check before use |
| 5 | 古屋能勢雄『営業無尽ト頼母子講』 (pid 986238) | private author, Tokushima | 1918 | 第五章 頼母子講ノ組織及ビ標本: model forms | internet | **listed in logbook 5** |
| 6 | municipal and prefectural histories, 史料編 (e.g. 新修豊田市史 11, 熊谷市史 資料編 8, 戸田市史 資料編 4, 明石市史資料 8) | one editorial committee each | published 1960s–2010s; documents mostly Edo or Meiji | one or a few rulebooks each, by full-text hit; not checked | mostly 送信サービス or print only | 0 hits on those checked |
| 7 | single rulebooks held by university or regional archives and aggregated in NDL Search (e.g. 大縣郡高井田村溜池頼母子加入者規約改正簿, 1885, Kobe University) | none (archival survival) | Meiji | one each | holder's site | 0 hits |

**Excluded.** Everything from 農林省經濟更生部 (『頼母子講ニ關スル調査』 1935, 『農村金融資料』 第1–2號, the 1933 Hyōgo case collection): same selector. 司法省調査課 1928 (pid 1907434), listed in logbook 5 as read: spent. 古屋 1918 (5) prints model forms, which are drafted examples and not rules in force, and fails the test's premise. Prefectural police regulations (e.g. 『警察法規類典 山口縣』 1931) frame the rules but are not rulebooks.

## 4. Assessment

**No single unread source matches the 1936 volume's scale.** The two that are unread, independent and contemporary are candidates 1 and 2, from two ministries and about 27 years apart. Together they probably print well under the fifteen rulebooks a re-test needs. Candidate 2 mixes 十錢講 rules with kō rules, and the Aomori and Tokushima reports are court-district accounts whose selection principle is not stated.

**A combined set is the realistic route, and its population must be declared before coding:** candidate 1 (1915, before the 無尽業法), candidate 2's kō rules only (c. 1942), and candidate 3 if other numbers carry appendices of rules. Candidate 6 is a fallback that buys independence (one editor per rulebook) at the cost of period mixing and item-by-item assembly.

## 5. Next steps, for Chat A, all at rung 0–2

1. List the titles of the forty other numbers of 『世態調査資料』 (rung 0).
2. Confirm transmission-service access to pid 1909099 under MS's login (rung 0).
3. Decide whether the number of rulebooks in candidate 1's appendix may be counted from its running heads (rung 2). Counting them is the only way to size the set before choosing, and it spends the appendix's shape but not its clauses.
4. Decide the population (kō only, or kō and 十錢講; Taishō and Shōwa, or Shōwa only) and write it into the brief before any rulebook is read.
5. Check candidate 4's status in logbook 5 in full before treating it as unread.

## 6. Standing-table row (proposed for logbook 4)

| slug | session | what it spent |
|------|---------|---------------|
| `residual-default-retest-scan` | 2026-10-22, catalogue scan in the `residual-default-coding` chat | NDL Search and Digital Collections catalogue fields, full-text hit lists (titles and ids) for 頼母子講規約 and related terms, and the tables of contents of pids 944336, 986238, 956756, 1444166 and 1909099; frame 1 of 956756, 1444166 and 1909099 shown by the viewer. No page of content. **Prejudices:** nothing about any candidate's clauses; it does fix which sources a re-test would draw on, so a Chat A that adopts this shortlist inherits its framing. |
