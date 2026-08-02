# Adding and coding characteristics

CONTRIBUTING §5 says schema growth is additive. That is a rule about *how* to grow the schema. This file is about *whether* to — when a new characteristic is warranted, when it is a mistake, and why the dependence columns in `vocabularies/organizational_form_characteristic.csv` exist.

The short version: **discriminating power is free, so it is worthless as a justification.** Adding characteristics until forms separate is not a finding.

## The problem, stated formally

Watanabe's **ugly duckling theorem** (*Knowing and Guessing*, 1969): given a finite set of objects and the set of all possible predicates over them, any two objects satisfy exactly the same number of shared predicates. Similarity is constant across every pair unless the predicates are *weighted*, and no weighting can be derived from the objects themselves. Classification without bias makes everything equally similar and equally dissimilar.

For a Zwicky matrix this is not an abstraction. With *k* binary characteristics there are 2^*k* possible configurations. When the number of coded forms is far below that — and it always is — every form occupies its own cell **by construction**. "These forms differ" then reports how many characteristics were used, not anything about the forms.

Systematics has fought this out at length. Rieppel's *Similarity* (2002) and *The Poverty of Taxonomic Characters* (2007) are the discipline arguing with itself about exactly this.

## Five tests before adding a characteristic

The first three can be applied from the desk. The last two cannot be applied at all without more forms.

### 1. Well-formedness — does the existing characteristic contain two variables?

Sereno (2007) decomposes a character statement into locator, variable, variable qualifier and state, and shows that most classic coding controversies are symptoms of **incomplete character statements**. If one characteristic silently asks two questions, its values are uninterpretable and splitting is *mandatory*, not optional.

Worked case: `LR2 outcome coupling` returned `coupled` for the *muḍāraba*, the *commenda* and the *ʿisqa* alike. It was bundling *is the decision-maker bound to outcomes?* with *in which direction?* — so an agent holding a call option bounded below at zero and a manager holding a debt read identically. `LR6 coupling symmetry` is the repair, not an embellishment.

### 2. Ontological dependence — is the characteristic conditional on another?

Some characteristics are meaningful only given another's state. `LR5` asks the correlation of pooled baskets, which is senseless where `LR4` says there is no pooling. Record the dependency in `applicability_on`; do not treat the characteristic as a free dimension.

Vogt (2018) is directly on this. Strong & Lipscomb (1999) and Maddison (1993) are on the associated missing-data problem, and Maddison's distinction between *missing data* and *missing characters* is the ancestor of this repo's `.NR`/`.NA` split (CONTRIBUTING §4).

**The dependency runs backwards as well as forwards.** If a child characteristic is inapplicable, that is evidence about the parent's value. `waqf_khayri` was coded `LR4=P` (partial pooling) with `LR5=.NA`; since there were no baskets whose correlation could be asked about, the `.NA` was diagnostic and the `P` was the error. `LR4` is now `0`.

### 3. Comparative-concept hygiene — whose category is this?

Haspelmath (2010) distinguishes **comparative concepts**, built by the analyst for comparison and belonging to no particular tradition, from **descriptive categories**, which are internal to one tradition and cannot be exported. Equating a descriptive category across traditions is illegitimate; comparison requires concepts defined in substantive terms available to all of them.

Several characteristics here fail this now and are flagged in the vocabulary rather than quietly fixed:

- `AP4` is written around a *founder* and a *corpus* — a waqf-shaped category, which is why it fitted the *asiento* badly and needed a note.
- `MG4=religious` for the *ʿisqa* was coded "for consistency with `waqf_khayri`", which is precisely the prohibited move.
- `FP4`'s "political authority" does not map onto a corporate minority community.

### 4. Discriminant validity — is it one construct or two?

Campbell & Fiske (1959) on the multitrait–multimethod matrix: whether two purported constructs are distinct **cannot be settled analytically**. You must observe cases where they come apart.

This repo has a worked instance. `AP3`, `LR1`, `CF2` and `LR6` were grouped as `agent-loss-exposure` on the argument that for bilateral capital-labour contracts they all record one fact — the agent is a debtor. Coding `asiento_averia`, which is multilateral and has no capital-labour asymmetry, separated them on substantive values: `LR1=limited` now occurs with `LR6=symmetric` *and* with `LR6=upside-only`. Limited liability does not determine the direction of exposure. One form settled what no amount of reasoning could.

### 5. Diversity budget — can you afford it?

Characteristics are paid for in forms. Marx & Duşa (2011) simulated over five million random datasets to find where configurational analysis starts returning apparently meaningful results from noise, and produced benchmark tables; their guidance is roughly **five cases per condition**. This dataset is nowhere near that and will not be soon.

Treat the benchmark as contested rather than settled — Thiem & Mkrtchyan (2024) attack the case-to-factor framing and Duşa & Marx reply in the same issue. Cite the dispute; it is more defensible and more interesting than either side.

## What this means in practice

**Add forms, not features.** Tests 4 and 5 both say so, and the *asiento* demonstrated it in an afternoon: one new form falsified a dependence claim, gave the pooling facet its first variance, and exposed two characteristics as waqf-shaped.

Before opening a PR that adds a characteristic, state in the PR which of tests 1–3 it passes. If the answer is "it lets us distinguish X from Y", that is the ugly duckling theorem talking, and the answer is no.

## Running the check

```sh
python scripts/check_dependence.py [datasets/organizational_forms]
```

Enforces applicability (non-zero exit on violation); reports redundancy without enforcing, since collinearity within a declared group is the expectation rather than an error. It distinguishes separation on substantive values from separation via `.NA`, which is weaker — inapplicability is a fact about scope, not evidence that two characteristics vary independently.

Note that counting **distinct signatures** does not test redundancy: *n* forms with *n* signatures is equally consistent with total collinearity and with total independence. The test is whether the mapping between members is a function.

## References

Full records, DOI-verified, in the Zotero collection `method — typology and character coding`.

**Character individuation and independence**

- Sereno, P.C. 2007. Logical basis for morphological characters in phylogenetics. *Cladistics* 23: 565–587. `10.1111/j.1096-0031.2007.00161.x`
- Vogt, L. 2018. The logical basis for coding ontologically dependent characters. *Cladistics*. `10.1111/cla.12209`
- Vogt, L. 2017. Assessing similarity: on homology, characters and the need for a semantic approach to non-evolutionary comparative homology. *Cladistics*. `10.1111/cla.12179`
- Hawkins, J.A., Hughes, C.E. & Scotland, R.W. 1997. Primary homology assessment, characters and character states. *Cladistics* 13: 275–283. `10.1111/j.1096-0031.1997.tb00320.x`
- Pleijel, F. 1995. On character coding for phylogeny reconstruction. *Cladistics* 11: 309–315. `10.1016/0748-3007(95)90018-7`
- Brazeau, M.D. 2011. Problematic character coding methods in morphology and their effects. *Biological Journal of the Linnean Society* 104: 489–498. `10.1111/j.1095-8312.2011.01755.x`
- Strong, E.E. & Lipscomb, D. 1999. Character coding and inapplicable data. *Cladistics* 15: 363–371. `10.1111/j.1096-0031.1999.tb00272.x`
- Maddison, W.P. 1993. Missing data versus missing characters in phylogenetic analysis. *Systematic Biology* 42: 576–581. `10.1093/sysbio/42.4.576`
- Felsenstein, J. 1985. Phylogenies and the comparative method. *The American Naturalist* 125: 1–15. `10.1086/284325`

**Similarity and the limits of classification**

- Rieppel, O. 2002. Similarity. *Biological Journal of the Linnean Society* 75: 59–82. `10.1046/j.1095-8312.2002.00006.x`
- Rieppel, O. 2007. The poverty of taxonomic characters. *Biology and Philosophy* 22: 95–113. `10.1007/s10539-006-9024-z`
- Watanabe, S. 1969. *Knowing and Guessing: A Quantitative Study of Inference and Information.* Wiley. **Not yet in Zotero — pre-DOI, needs manual entry.**
- Goodman, N. 1972. Seven strictures on similarity, in *Problems and Projects.* **Not yet in Zotero.**

**Typology construction**

- Haspelmath, M. 2010. Comparative concepts and descriptive categories in crosslinguistic studies. *Language* 86: 663–687. `10.1353/lan.2010.0021`
- Collier, D., LaPorte, J. & Seawright, J. 2012. Putting typologies to work. *Political Research Quarterly* 65: 217–232. `10.1177/1065912912437162`
- Sartori, G. 1970. Concept misformation in comparative politics. *American Political Science Review* 64: 1033–1053. `10.2307/1958356`
- Campbell, D.T. & Fiske, D.W. 1959. Convergent and discriminant validation by the multitrait-multimethod matrix. *Psychological Bulletin* 56: 81–105. **Not yet in Zotero; pagination unverified.**
- Lazarsfeld, P. 1937, and Barton, A. 1955, on property space and its reduction. **Not yet in Zotero; citations unverified.**

**Diversity budget**

- Marx, A. & Duşa, A. 2011. Crisp-set qualitative comparative analysis (csQCA), contradictions and consistency benchmarks for model specification. *Methodological Innovations Online* 6(2): 103–148. `10.4256/mio.2010.0037`
- Thiem, A. & Mkrtchyan, L. 2024. Case-to-factor ratios and model specification in qualitative comparative analysis. *Field Methods.* `10.1177/1525822X231159458`
- Duşa, A. & Marx, A. 2024. Comment on the above. *Field Methods.* `10.1177/1525822X231159462`

**Unverified leads, not yet consulted.** Archaeology had this argument sixty years ago over material forms with no direct access to descent, which is closer to our case than biology is: the Ford–Spaulding debate (*American Antiquity*, 1953–54), Dunnell's *Systematics in Prehistory* (1971), Adams & Adams' *Archaeological Typology and Practical Reality* (1991). Also Ritchey on cross-consistency assessment in general morphological analysis, which exists to prune exactly the combinatorial explosion described above.
