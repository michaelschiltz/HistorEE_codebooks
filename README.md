# HistorEE_codebooks

Versioned, timestamped, attributed data and codebooks for the project HistorEE.

This repository is the data-and-documentation backbone of HistorEE. It is the natural successor to the single-author logbook method used in [`even-keel`](https://github.com/michaelschiltz/even-keel), yet extended into a team-grade apparatus for a multi-year, multi-member project.

The design goal is *provenance that survives scrutiny*: every datum traceable to a source, every coding decision attributed to a person and a date, and every published state frozen and citable.

## How this repository is organised

```
HistorEE_codebooks/
├── datasets/<dataset>/        one folder per dataset
│   ├── data.csv               the data — plain text, diffable, canonical
│   ├── datapackage.json       machine-readable schema (Frictionless Table Schema)
│   └── codebook.md            human-readable codebook — GENERATED, do not hand-edit
├── vocabularies/              controlled vocabularies (one CSV per coded field)
├── logbook/                   narrative decision log (the even-keel convention)
├── scripts/build_codebook.py  regenerates every codebook.md from its datapackage.json
├── CONTRIBUTING.md            the coding manual — read before touching data
├── CITATION.cff               makes the repo citable ("Cite this repository")
├── CHANGELOG.md               human-readable record of dataset-level changes
└── LICENSE / LICENSE-DATA.md  dual licence: code vs. data (see below)
```

## Three layers, one source of truth

1. **Data** — `data.csv`. Plain-text UTF-8. Canonical. Never a spreadsheet.
2. **Schema** — `datapackage.json`. Machine-readable field definitions, types, constraints, and controlled-vocabulary references (Frictionless standard).
3. **Codebook** — `codebook.md`. The human-readable, interpretive layer. It is **generated** from `datapackage.json` by `scripts/build_codebook.py` (Python, standard library only — no dependencies). **Editing the codebooks by hand is a mistake**: edit the schema and regenerate. One source of truth, rendered two ways.

## Provenance apparatus

- **Git history** supplies line-level attribution and timestamps (`git blame`).
- **Signed commits** and a **protected `main`** make attribution cryptographic.
- **Tagged releases minted to a FigShare and Zenodo DOI** freeze citable snapshots at each milestone (the model used by the Seshat Global History Databank). `v0.1.0`: [Zenodo](https://doi.org/10.5281/zenodo.21341361) · [FigShare](https://doi.org/10.6084/m9.figshare.32947250).
- **Redundancy**: the repository is mirrored to FigShare and Zenodo, so survival does not solely depend on GitHub.

## Licensing

This repository uses a **dual licence**, because code and data are different things and conflating them causes exactly the mess visible in the Seshat databank (where the GitHub copy carried CC0 while the project page asserted CC-BY-NC-SA). Do not repeat that.

- **Code** (`scripts/`, workflows) — MIT. See [`LICENSE`](LICENSE).
- **Data and codebooks** (`datasets/`, `vocabularies/`, `logbook/`) — **Creative Commons Attribution 4.0 (CC-BY-4.0)**. See [`LICENSE-DATA.md`](LICENSE-DATA.md).

If a source archive imposes non-commercial or redistribution restrictions on transcribed material, that dataset's folder carries its own `LICENSE` overriding this default, and the restriction is noted in its codebook. Resolve licence questions **before** publishing a dataset, never after.

## Provisional status

The schema is deliberately minimal and **additive-extensible**. This means that fields will accrete from archival work; they will not be retrofitted. The provenance apparatus is fixed from the first commit, because history cannot be back-dated.

> ⚠️ The dataset shipped in `datasets/clearing_records/` is **illustrative and synthetic** — a worked example demonstrating the schema, not archival data.
> See its codebook header.
