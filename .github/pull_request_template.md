## What this PR changes

<!-- Data? Schema? Vocabulary? Logbook? Be specific. -->

## Coder / authority

- Coder: @
- Interpretive decisions authored by: @

## Checklist

- [ ] Edited `data.csv` as text (not via Excel round-trip)
- [ ] No blank cells — absence is coded (`.NR` / `.IL` / `.NA` / `.ZERO`)
- [ ] If schema changed: bumped `version`, updated `CHANGELOG.md`
- [ ] If schema changed: regenerated `codebook.md` (`python scripts/build_codebook.py`)
- [ ] `frictionless validate` passes locally
- [ ] Commits are signed (`-S`)
- [ ] Contestable decisions logged in `logbook/` or an issue
