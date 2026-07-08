# Contributing — the coding manual

This is not boilerplate. It is the coding protocol for the project. In a
multi-member team the codebook is only as trustworthy as the discipline behind
it, so every contributor reads this before touching data.

## 1. Golden rules

1. **The CSV is canonical.** Never edit data in Excel and paste back — you will
   silently mangle encodings, dates, and leading zeros. Edit `data.csv` as text,
   or through a script.
2. **Never hand-edit `codebook.md`.** It is generated. Edit `datapackage.json`
   and run `python scripts/build_codebook.py`.
3. **No blank cells.** Absence is coded, never empty. See §4.
4. **One decision, one commit.** Commit messages record *why*, not just *what*.
5. **Sign your commits** (`git commit -S`). Attribution must be cryptographic,
   not merely a name string.

## 2. Roles and attribution

Contributors and roles are declared in `CITATION.cff`. Every observation carries
a `coder` field naming the person who entered it. Interpretive decisions that are
contestable additionally carry an `authority` note in the codebook. `git blame`
is the backstop: it shows who changed which line, when, in which commit.

| Role | Responsibility |
|------|----------------|
| Maintainer | Owns the schema; approves merges to `main`; cuts releases. |
| Coder | Enters and normalises data; documents decisions in the logbook. |
| Reviewer | Second pair of eyes on every PR touching data or schema. |

## 3. The workflow

1. Branch from `main` (`git switch -c coding/<dataset>-<yourname>`).
2. Make changes. Regenerate the codebook if you touched the schema.
3. Run validation locally: `frictionless validate datasets/<dataset>/datapackage.json`.
4. Open a pull request using the template. CI re-runs validation.
5. A reviewer approves. Only then does it merge to `main`.
6. `main` is protected: no direct pushes, no unreviewed data.

## 4. Coding conventions (the parts referees test)

**Missingness is disaggregated.** Never leave a cell blank. Use:

| Code | Meaning |
|------|---------|
| `.NR` | not recorded in the source |
| `.IL` | present but illegible / damaged |
| `.NA` | not applicable to this record type |
| `.ZERO` | the source records an actual zero |

Conflating these is the single most common way a historical dataset gets
discredited. They are four different epistemic states.

**Uncertainty is explicit.** The `confidence` field is coded `high` / `medium`
/ `low`, defined in the codebook. Do not launder uncertainty into prose.

**Units are normalised transparently.** Any monetary amount carries both its
original figure/unit *and* a normalised value, with the `normalization_method`
naming the conversion applied. For Tokugawa material this means the *sanka* (三貨)
gold/silver/copper problem is made auditable per row, not buried in a footnote.

**Source language is preserved.** Original term, romanisation, and gloss are
kept as separate fields. Where a term's referent shifts across periods, record
the shift in the codebook rather than smoothing it over.

## 5. Extending the schema

Schema growth is **additive**. Add a field; do not repurpose an existing one.
Bump the data-package `version` (semantic versioning) and record the change in
`CHANGELOG.md`. Additive change never breaks a downstream consumer.
