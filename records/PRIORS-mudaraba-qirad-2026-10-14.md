# Priors for the *muḍāraba*–*qirāḍ* pass (2026-10-14)

**Written before any source is read for coding, to be committed by MS before the first block is opened. Pass `mudaraba-qirad-2026-10-14`; open, not blind; coder `claude-opus-5-5`, effort `high`. Scope: `records/RULINGS-mudaraba-qirad-2026-10-14.md`, rulings 1–6; brief `records/NOTES-mudaraba-sarakhsi-2026-10-14.md`.**

**H** = the Ḥanafī rows `mudaraba` / `mudaraba_alloc`, from al-Sarakhsī. **M** = the Mālikī rows `qirad` / `qirad_alloc`, from the *Muwaṭṭaʾ* and the *Mudawwana*. In the basis column, **K** marks a cell whose deciding passage was already read in an earlier open pass: that prior is a record, not a prediction, and **its holding is not a result**. **E** marks an expectation. Where the earlier reading reached only part of a cell, the K is qualified. **The fate of each prior (held, falsified, changed) is recorded with the cell's ruling.**

## Structure measured before writing (rung 2: headings and page markers only; no body text read)

**Wikisource and Shāmila are refused by the network allowlist in both the cloud workspace and the Mac VM shell** (HTTP 403, `blocked-by-allowlist`). Structure was therefore taken in MS's Chrome, by scripts returning only page markers and bracketed headings. Pages are reached the same way for coding.

- **al-Sarakhsī, *al-Mabsūṭ* 22** (Arabic Wikisource, two pages: "…الجزء الثاني والعشرون", markers [1]–[83]; "…الجزء الثاني و العشرون2", [84]–[188]). ***Kitāb al-muḍāraba* runs 17–188**, to the end of the volume. Vol. 23 opens with *Kitāb al-muzāraʿa* (p. 2), so the chapter ends at 188. Its 28 *bāb* headings, by page:
  - 29 *ishtirāṭ baʿḍ al-ribḥ li-ghayrihimā*
  - 33 *al-muḍāraba bi'l-ʿurūḍ*
  - 38 *mā yajūzu li'l-muḍārib*
  - 48 *shirāʾ al-muḍārib wa-bayʿuhu*
  - 62 *nafaqat al-muḍārib*
  - 73 *al-murābaḥa fī al-muḍāraba*
  - 81 *al-muḍārib yabīʿu al-māl thumma yashtarīhi li-nafsihi*
  - 83 *ʿamal rabb al-māl maʿa al-muḍārib*
  - 89 *al-ikhtilāf bayna al-muḍārib wa-rabb al-māl*
  - 98 *al-muḍārib yadfaʿu al-māl muḍārabatan*
  - 105 *qismat rabb al-māl wa'l-muḍārib*
  - 109 *ʿitq al-muḍārib wa-daʿwatuhu*
  - 118 *jināyat al-ʿabd*
  - 122 *mā yajūzu li'l-muḍārib an yafʿalahu wa-mā lā yajūzu*
  - 125 *muḍārabat ahl al-kufr*
  - 131 *al-sharika fī al-muḍāraba*
  - 140 *iqrār al-muḍārib … fī al-maraḍ*
  - 145 *al-shufʿa*
  - 149 *al-shurūṭ fī al-muḍāraba*
  - 153 and 158 *al-murābaḥa* (two)
  - 157 *ḍamān al-muḍārib*
  - 163 *daʿwā al-muḍārib wa-rabb al-māl*
  - 168 *ḍiyāʿ māl al-muḍāraba qabla al-shirāʾ aw baʿdahu*
  - 178 *al-muḍārib yaʾmuruhu rabb al-māl bi'l-istidāna*
  - 185 *al-shahāda fī al-muḍāraba*

  The chapter opens at 17 with no *bāb* until 29.
- **Mālik, *al-Muwaṭṭaʾ*, *Kitāb al-qirāḍ*** (Arabic Wikisource, "موطأ الإمام مالك/كتاب القراض"): 42 numbered paragraphs, **2015–2056**, under 15 *bāb* headings (the number given is the last before each heading):
  - *mā jāʾa fī al-qirāḍ* (start)
  - *mā yajūzu* (after 2016)
  - *mā lā yajūzu* (2020)
  - *mā yajūzu min al-sharṭ* (2023)
  - *mā lā yajūzu min al-sharṭ* (2025)
  - *al-qirāḍ fī al-ʿurūḍ* (2031)
  - *al-kirāʾ* (2032)
  - *al-taʿaddī* (2033)
  - *mā yajūzu min al-nafaqa* (2038)
  - *mā lā yajūzu min al-nafaqa* (2040)
  - *al-dayn* (2041)
  - *al-biḍāʿa* (2043)
  - *al-salaf* (2044)
  - *al-muḥāsaba* (2046)
  - *jāmiʿ mā jāʾa* (2051)
- **Saḥnūn, *al-Mudawwana*** (shamela.ws book 587, table of contents): ***Kitāb al-qirāḍ* = Shāmila 1730–1765**, followed by *Kitāb al-aqḍiya* at 1766. This agrees with vol. 3, 629–664 as recorded on 2026-10-13. *Kitāb al-wadīʿa* (2196), *al-taflīs* (1839) and *al-ghaṣb* (1932) are read only where the *qirāḍ* chapter refers to them.

## Organizational rows (33 each)

**O1, contract core**

| char | H prior | M prior | basis | falsifier |
| --- | --- | --- | --- | --- |
| `CF1` | 1 | 1 | H K (in part: 22, 32, 140 deny the investor profit on the agent's own money); M K (in part: 647–648 bar *stipulating* the agent's contribution); E for the whole | the agent's capital contribution is a constitutive or default term → P |
| `CF2` | 0 | 0 | E (M: no. 2029 expected to void a stipulated guarantee) | capital loss on the agent without breach, or a valid stipulation of his guarantee → 1 or P |
| `CF3` | bilateral | bilateral | E | several principals as the base case |
| `LR2` | coupled | coupled | E | a fixed wage for the agent in the *valid* contract → attenuated |
| `LR3` | 1 | 1 | E | a fixed sum to either party in a valid contract → P or 0 |
| `LR4` | 0 | 0 | E; M candidate against: *Mudawwana* 645 (two investors' funds mixed, held pro rata) and 650–651 (mixing a second *qirāḍ* into one with gain or loss barred as *khaṭar*) | one party's separate loss borne in part by another by rule → P or 1 |
| `LR5` | .NA | .NA | follows `LR4` = 0 | `LR4` ≠ 0 |
| `LR6` | upside-only | upside-only | E | the agent bears capital loss beyond his labour → symmetric |

**O2, term and exit.** `TS3` is the test named on 2026-08-18; its source for M is the vault seed "The mudaraba is revocable not locked in" (`[verify]`), a hypothesis, not evidence.

| char | H prior | M prior | basis | falsifier |
| --- | --- | --- | --- | --- |
| `TS2` | open | open | E: H expected to *permit* a time limit as a term, M to *bar* one; the live `qirad TS2 = single-venture` (Udovitch, read unknown) is predicted to change | the contract ends at the first realisation in cash → single-venture; a term by default → fixed-term |
| `TS3` | 1 | P | E: H, either party may dissolve at will, any wait for conversion to cash being execution, not a bar; M, the investor's recall barred once the agent has begun work, free before (no. 2027 bears on recall) | **the pre-named test fails if H = M** (both P, or both 1) |
| `CI2` | 0 | 1 | E: M, the capital cannot be recalled until the goods are sold, the shape of `commenda CI2 = 1` | H = M |
| `TS1` | 0 | P | E: H, death of either party ends it; M, the agent's heirs may complete the venture if trustworthy | H continues through heirs; M ends on death with no completion |
| `TS4` | .NR | .NR | E | a rule on the parties altering terms after the capital is handed over (e.g. the investor narrowing a general mandate) → coded on the text |

**O3, creditors and entity**

| char | H prior | M prior | basis | falsifier |
| --- | --- | --- | --- | --- |
| `AP3` | 0 | 0 (low) | E: H, the agent is the contracting party and debt beyond the capital is his unless the investor authorised borrowing (*bāb al-istidāna*, 178); M, buying beyond the capital puts the excess on him (no. 2035; *Mudawwana* 637) | the agent's exposure to sellers capped at the capital → 1 or P; silence → .NR |
| `LR1` | unlimited-several | unlimited-several (low) | E, as `AP3` | as `AP3` |
| `AP1` | .NR | .NR | E; H candidate: 22, 143 (the investor's capital in the agent's estate on insolvency), which answers the investor against the agent's creditors, `AP1` only if the entity reading reaches it | venture creditors ranked over a party's personal creditors in venture goods |
| `AP2` | 0 | .NR | E: H, either party can force termination and division | partition or withdrawal barred to a party or his creditors |
| `AP4` | .NA | .NA | no founder (family disposition) | a corpus constituted from a founder's patrimony |
| `LP1` | 0 | 0 (low) | E | the arrangement treated as a subject distinct from the two parties |
| `LP2` | 0 | 0 | E: title stays with the investor; goods bought with the capital are his | goods held in the arrangement's name |
| `LP3` | 0 | 0 | E: actions are the parties' own | an action by or against the arrangement as such |

**O4, capital**

| char | H prior | M prior | basis | falsifier |
| --- | --- | --- | --- | --- |
| `CI1` | none | none | E: one investor in the base case | several contributors' capital held as the base case |
| `CI3` | 0 | .NR | E: H, the agent may not hand the capital on without authority (*bāb* 98) and no assignment of the investor's claim | an interest alienable without dissolution → 1 or P |
| `CI4` | 0 | .NR | follows `CI3` | `CI3` ≠ prior |
| `CI5` | segregated | commingled | **K** both (22, 48, 132–133; *Mudawwana* 641, 645; `OF-0903`): the reason the row was opened, carries no weight | — |

**O5, governance and frame**

| char | H prior | M prior | basis | falsifier |
| --- | --- | --- | --- | --- |
| `MG1` | contract | contract | E | a claim grounded in membership or beneficiary status |
| `MG2` | single-principal | single-principal | H **K** (22, 41, 48); M E | control held jointly or by the investor in the base case |
| `MG3` | .NA | .NA | `MG1` ≠ membership | `MG1` = membership |
| `MG4` | private-contract | private-contract | E: the jurists' scriptural warrant is not the parties' authorization (the `isqa MG4 = religious` hygiene warning) | the contract valid only by an authority's licence or as a religious act |
| `FP1` | commercial-profit | commercial-profit | E | a declared pious or mutual purpose |
| `FP2` | .NR | .NR | E | any franchise held by the arrangement |
| `FP3` | .NR | .NR | E; H candidate: *muḍārabat ahl al-kufr* (125) | the form used to give a party a status or access he lacks → P or 1 |
| `FP4` | .NR | .NR | E: writing and witnesses (*bāb al-shahāda*, 185) are not registration | registration with an authority |

## Loss rows (26 each)

**L1, the family's ten**

| char | H prior (`mudaraba_alloc`) | M prior (`qirad_alloc`) | basis | falsifier |
| --- | --- | --- | --- | --- |
| `MC1` | allocation | allocation | E | loss spread to an outsider for a premium, or mutualised |
| `MB3` | voluntary | voluntary | E | — |
| `RB1` | capital-provider | capital-provider | E | peril loss on the agent without fault |
| `RB2` | capital-provider | capital-provider | E (M possibly analyst-imposed, as `LM-0540`) | market loss on the agent |
| `RB3` | none | none | E: H, no surety or pledge for a trust (*amāna*); M, no. 2029 | a valid pledge or surety for the capital |
| `RB4` | 1 | 1 | E | the agent owes the capital after a total loss without fault |
| `PR1` | 0 | 0 | E | a return fixed before the outcome |
| `PY0` | .NA | .NA | bilateral contract, not a fund | — |
| `VF1` | claimant-oath | claimant-oath | H **K** (22, 27, 51); M E (no. 2054 bears on the oath) | proof by witnesses or documents required |
| `VF2` | mixed | mixed | H **K** (22, 108); M E | one object only |

**L2, the other sixteen.** The prior for each is **declined on both rows** (ruling 4). Grounds:
- `MB1`: entailed by the form, not addressed.
- `MB2`: no membership.
- `CN1`, `CN2`, `CN3`: no contribution schedule to a pool.
- `HZ1`, `HZ2`: not addressed.
- `PY1`, `PY2`, `PY3`: follow `PY0 = .NA`; 7 of 8 such rows carry no cell.
- `LS1`, `LS2`: would restate `RB1`, `RB2` and `LR3`.
- `LS3`: uncoded by ruling 4.
- `GV1`: would restate `MG2`.
- `DR1`, `DR2`: would restate `TS2` and the division.

A prior fails if a text addresses one of these substantively in a way no other cell carries. The likeliest are `DR2`, from *bāb qismat rabb al-māl wa'l-muḍārib* (105) and *bāb al-muḥāsaba* (after 2046), and `LS1`, from the rule that profit makes good capital loss before division.

## Count

Organizational: 8 + 5 + 8 + 4 + 8 = 33 per row, × 2 = 66. Loss: 10 + 16 = 26 per row, × 2 = 52. **118 priors.** Of these, 7 are K, recorded but not predictions:
- H `CI5`, `MG2`, `VF1`, `VF2`;
- M `CI5`;
- `CF1` in part on both rows.

The prior that matters most is **`TS3`, H 1 against M P**: it is the only separation named before any Mālikī text was read.
