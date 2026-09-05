#!/usr/bin/env python3
"""Build reader-facing views of a coded morphological matrix.

Two artefacts, deliberately, because they answer to different rules
(CHARACTER-CODING.md, "Claims, not columns"):

  * the SCOPED MATRIX is a description view. It is always restricted to one
    declared `component`, never printed over the full characteristic set, and
    it carries n in its caption. Its honest use at present n is as a coverage
    map -- which cells are not yet coded -- not as evidence.

  * the CLAIM TABLE is a comparative view over two or three characteristics,
    printed with full values and no state codes, for a claim that has been
    stated in advance.

Both preserve the four missingness states distinctly. A view that renders
`.NR`, `.NA`, `0` and "no row at all" the same way is worse than no view.

Standard library only, deterministic, no wall-clock dependency -- matching
scripts/build_codebook.py so CI needs no new runtime.

Usage:
    python3 scripts/build_views.py --component risk-pooling --mechanism pooling
    python3 scripts/build_views.py --component risk-pooling --format tex
    python3 scripts/build_views.py --component risk-pooling --check
"""

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Markdown tables are padded to aligned columns. The padder already exists, in
# scripts/build_codebook.py, and is imported rather than reimplemented here:
# CONTRIBUTING §4 warns that an unregistered duplicate is precisely what drifts
# unnoticed, and a second table renderer would be one. sys.path is nudged so the
# import holds however the script is invoked.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_codebook import md_table  # noqa: E402

# The four states a cell can be in, kept visually distinct in every format.
NO_ROW = "--"          # the form x characteristic pair was never entered
MISSING_TOKENS = {".NR", ".IL", ".NA"}

# Which vocabularies describe which dataset. Mirrors the registry in
# scripts/check_dependence.py; a dataset absent here has no characteristic
# vocabulary and cannot be viewed. Before 2026-08-29 this module read the
# loss-mitigation vocabularies unconditionally, so every view of
# organizational_forms was built against the wrong characteristic set: WP2
# components returned "no characteristics", and --component owner-shielding
# succeeded while crossing organizational form ids with LS3/RB3/RB4.
VOCAB = {
    "loss_mitigation_forms": ("loss_mitigation_characteristic.csv",
                              "loss_mitigation_type.csv"),
    "organizational_forms": ("organizational_form_characteristic.csv",
                             "organizational_form_type.csv"),
}

# The mechanism filter is MC1, which exists only in loss_mitigation_forms.
MECHANISM_KEY = {"loss_mitigation_forms": "MC1"}

# The claim table's default pair is dataset-specific for the same reason: PR1 and
# PY0 are loss-mitigation characteristics and raise KeyError against any other
# vocabulary. A dataset with no declared default gets no claim table unless one
# is asked for explicitly.
DEFAULT_CLAIM = {"loss_mitigation_forms": "PR1,PY0"}

LATEX_ACCENTS = {
    "á": r"\'a", "é": r"\'e", "í": r"\'i", "ó": r"\'o", "ú": r"\'u",
    "à": r"\`a", "è": r"\`e", "ù": r"\`u",
    "ä": r'\"a', "ë": r'\"e', "ï": r'\"i', "ö": r'\"o', "ü": r'\"u',
    "ā": r"\=a", "ē": r"\=e", "ī": r"\=i", "ō": r"\=o", "ū": r"\=u",
    "ç": r"\c{c}", "ñ": r"\~n", "ḍ": r"\d{d}", "ṣ": r"\d{s}", "ʿ": r"{'}",
    "—": "---", "–": "--", "’": "'", "‘": "`", "“": "``", "”": "''",
}


def tex(s):
    """Escape a string for pdfLaTeX with T1 encoding (no fontspec dependency)."""
    out = []
    for ch in str(s):
        if ch in LATEX_ACCENTS:
            out.append(LATEX_ACCENTS[ch])
        elif ch in "&%$#_{}":
            out.append("\\" + ch)
        elif ch == "\\":
            out.append(r"\textbackslash{}")
        elif ch in "~^":
            out.append(r"\textasciitilde{}" if ch == "~" else r"\textasciicircum{}")
        elif ord(ch) < 128:
            out.append(ch)
        else:
            out.append("?")
    return "".join(out)


def load(dataset):
    if dataset not in VOCAB:
        sys.exit(f"no characteristic vocabulary registered for {dataset!r}; "
                 f"known datasets: {', '.join(sorted(VOCAB))}")
    char_file, type_file = VOCAB[dataset]
    base = ROOT / "datasets" / dataset
    chars = {r["code"]: r for r in csv.DictReader(
        open(ROOT / "vocabularies" / char_file, encoding="utf-8"))}
    types = {r["code"]: r for r in csv.DictReader(
        open(ROOT / "vocabularies" / type_file, encoding="utf-8"))}
    rows = list(csv.DictReader(open(base / "data.csv", encoding="utf-8")))
    cells = {}
    for r in rows:
        cells.setdefault(r["type_id"], {})[r["char_id"]] = r
    return chars, types, cells


def state_map(char):
    """Map a characteristic's allowed values to compact display codes.

    Ternary characteristics keep their literal 1/P/0 -- recoding them would
    hide that `0` is an observed absence rather than an arbitrary state index.
    Nominal characteristics take integer codes with a printed legend.
    """
    allowed = [v for v in char["allowed_values"].split("|") if v and v != ".NA"]
    if char["value_type"] == "ternary" or set(allowed) == {"1", "P", "0"}:
        return {v: v for v in allowed}, []
    m, legend = {}, []
    for i, v in enumerate(allowed):
        m[v] = str(i)
        legend.append((str(i), v))
    return m, legend


def select(chars, types, cells, component, mechanism, dataset=None):
    codes = sorted(c for c, r in chars.items() if r["component"] == component)
    key = MECHANISM_KEY.get(dataset)
    if mechanism is not None and key is None:
        sys.exit(f"--mechanism is not available for dataset {dataset!r}: it has no "
                 f"mechanism characteristic. Pass --mechanism all.")
    forms = sorted(f for f in cells
                   if mechanism is None
                   or (cells[f].get(key) or {}).get("value") == mechanism)
    return codes, forms


def cell_value(cells, form, code):
    r = cells.get(form, {}).get(code)
    return NO_ROW if r is None else r["value"]


# --------------------------------------------------------------- markdown ---

def render_md(chars, types, cells, codes, forms, component, mechanism, claim, dataset=None):
    maps = {c: state_map(chars[c]) for c in codes}
    L = []
    L.append(f"# Scoped view — component `{component}`\n")
    key = MECHANISM_KEY.get(dataset)
    filt = (f"Mechanism filter: `{key} = {mechanism}`. " if key
            else "No mechanism filter (this dataset has no mechanism characteristic). ")
    L.append(filt +
             f"**{len(forms)} forms × {len(codes)} characteristics.** "
             f"This is NOT the full characteristic set: comparative claims run on a "
             f"declared component set only (`CHARACTER-CODING.md`). At this *n* the "
             f"matrix is a coverage map, not evidence.\n")
    L.append("## Matrix\n")
    matrix_rows = []
    for f in forms:
        cs = []
        for c in codes:
            v = cell_value(cells, f, c)
            cs.append(v if v in MISSING_TOKENS or v == NO_ROW else maps[c][0].get(v, v))
        matrix_rows.append([f"`{f}`"] + cs)
    L.extend(md_table(["form"] + [f"`{c}`" for c in codes], matrix_rows))
    L.append("")
    L.append(f"**Missingness.** `{NO_ROW}` no row entered · `.NR` not recorded in the "
             "source · `.IL` illegible · `.NA` inapplicable · `0` an observed absence. "
             "These are five different epistemic states and are never collapsed.\n")
    L.append("## Character states\n")
    for c in codes:
        m, legend = maps[c]
        L.append(f"- **`{c}` {chars[c]['name']}** ({chars[c]['value_type']}) — "
                 + ("; ".join(f"`{k}` = {v}" for k, v in legend) if legend
                    else "ternary: `1` present, `P` partial, `0` absent"))
    L.append("")
    if claim:
        L.append("## The claim\n")
        claim_rows = [[f"`{f}`"] + [cell_value(cells, f, c) for c in claim]
                      for f in forms]
        L.extend(md_table(["form"] + [f"`{c}` {chars[c]['name']}" for c in claim],
                          claim_rows))
        L.append("")
    L.append("## Forms\n")
    for f in forms:
        t = types.get(f, {})
        L.append(f"- `{f}` — {t.get('name','(not in vocabulary)')}"
                 + (f" · {t.get('tradition','')} · {t.get('period','')}" if t else ""))
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ latex ---

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=22mm]{geometry}
\usepackage{booktabs}
\usepackage{array}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=black,urlcolor=black]{hyperref}
\setlength{\parskip}{0.4em}
\setlength{\parindent}{0pt}
\renewcommand{\arraystretch}{1.15}
\begin{document}
"""


def render_tex(chars, types, cells, codes, forms, component, mechanism, claim, dataset):
    maps = {c: state_map(chars[c]) for c in codes}
    L = [PREAMBLE]
    L.append(r"\section*{Appendix: scoped morphological view}")
    mech_key = MECHANISM_KEY.get(dataset)
    mech_bit = (rf"\textbf{{Mechanism}} \texttt{{{mech_key} = {tex(mechanism)}}}"
                if mech_key else r"\textbf{No mechanism filter}")
    L.append(rf"\textbf{{Dataset}} \texttt{{{tex(dataset)}}} \quad "
             rf"\textbf{{Component}} \texttt{{{tex(component)}}} \quad "
             + mech_bit)
    L.append(rf"\textbf{{{len(forms)} forms $\times$ {len(codes)} characteristics.}} "
             r"This view is restricted to one declared component set. Comparative claims "
             r"never run on the full characteristic set: with enough characteristics any two "
             r"forms separate, so a matrix printed over all of them reports how many "
             r"characteristics were used rather than anything about the forms. At this $n$ the "
             r"matrix below is a coverage map and not evidence; the comparative reading is "
             r"confined to Table~2, whose two characteristics were fixed before the coding.")

    # Table 1 — matrix
    L.append(r"\begin{table}[htbp]\centering\small")
    L.append(r"\caption{Scoped matrix. States are coded; see the character-state list. "
             r"Missingness is never collapsed: \texttt{--} no row entered, \texttt{.NR} not "
             r"recorded in the source, \texttt{.IL} illegible, \texttt{.NA} inapplicable, "
             r"\texttt{0} an observed absence.}")
    L.append(r"\begin{tabular}{l" + "c" * len(codes) + "}")
    L.append(r"\toprule")
    L.append("form & " + " & ".join(rf"\texttt{{{c}}}" for c in codes) + r" \\")
    L.append(r"\midrule")
    for f in forms:
        cs = []
        for c in codes:
            v = cell_value(cells, f, c)
            cs.append(tex(v if v in MISSING_TOKENS or v == NO_ROW else maps[c][0].get(v, v)))
        L.append(rf"\texttt{{{tex(f)}}} & " + " & ".join(rf"\texttt{{{x}}}" for x in cs) + r" \\")
    L.append(r"\bottomrule\end{tabular}\end{table}")

    # Table 2 — the claim, full values
    if claim:
        L.append(r"\begin{table}[htbp]\centering\small")
        cap = (r"The comparative reading, printed with full values and no state codes.")
        if claim == ["PR1", "PY0"]:
            cap += (r" \texttt{PR1} takes both values \emph{inside} \texttt{MC1=pooling} at a "
                    r"fixed date, so ex-ante pricing is a separate axis rather than a stage of "
                    r"mechanism; \texttt{PY0} separates the forms on whether a draw corresponds "
                    r"to the recipient's own realised loss.")
        L.append(r"\caption{" + cap + "}")
        L.append(r"\begin{tabular}{l" + "l" * len(claim) + "}")
        L.append(r"\toprule")
        L.append("form & " + " & ".join(rf"\texttt{{{c}}} {tex(chars[c]['name'])}"
                                        for c in claim) + r" \\")
        L.append(r"\midrule")
        for f in forms:
            L.append(rf"\texttt{{{tex(f)}}} & "
                     + " & ".join(rf"\texttt{{{tex(cell_value(cells, f, c))}}}" for c in claim)
                     + r" \\")
        L.append(r"\bottomrule\end{tabular}\end{table}")

    # Character states
    L.append(r"\subsection*{Character states}")
    L.append(r"\begin{description}\setlength{\itemsep}{2pt}")
    for c in codes:
        m, legend = maps[c]
        body = ("; ".join(rf"\texttt{{{k}}}~=~{tex(v)}" for k, v in legend) if legend
                else r"ternary: \texttt{1} present, \texttt{P} partial, \texttt{0} absent")
        L.append(rf"\item[\texttt{{{c}}}] \textit{{{tex(chars[c]['name'])}}} — {body}")
    L.append(r"\end{description}")

    # Forms
    L.append(r"\subsection*{Forms}")
    L.append(r"\begin{description}\setlength{\itemsep}{2pt}")
    for f in forms:
        t = types.get(f, {})
        L.append(rf"\item[\texttt{{{tex(f)}}}] {tex(t.get('name','(not in vocabulary)'))}"
                 + (rf" \hfill \textit{{{tex(t.get('tradition',''))}, "
                    rf"{tex(t.get('period',''))}}}" if t else ""))
    L.append(r"\end{description}")

    L.append(r"\vfill\footnotesize All codings marked \texttt{coder=ai} are provisional and "
             r"pending human verification. Cells carrying \texttt{[verify]} in "
             r"\texttt{source\_ref} are asserted against an unpinned citation.")
    L.append(r"\end{document}")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------- main ---

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dataset", default="loss_mitigation_forms")
    ap.add_argument("--component", default="risk-pooling")
    ap.add_argument("--mechanism", default="pooling",
                    help="filter forms by MC1 value; 'all' to disable")
    ap.add_argument("--claim", default=None,
                    help="comma-separated characteristics for the claim table; "
                         "'' to omit. Default is dataset-specific (see DEFAULT_CLAIM).")
    ap.add_argument("--format", choices=["md", "tex"], default="md")
    ap.add_argument("--out", default=None)
    ap.add_argument("--check", action="store_true",
                    help="verify the committed view matches; non-zero exit on drift")
    args = ap.parse_args()

    mechanism = None if args.mechanism == "all" else args.mechanism
    claim_spec = (DEFAULT_CLAIM.get(args.dataset, "")
                  if args.claim is None else args.claim)
    claim = [c for c in claim_spec.split(",") if c]

    chars, types, cells = load(args.dataset)
    unknown = [c for c in claim if c not in chars]
    if unknown:
        sys.exit(f"--claim names characteristics absent from "
                 f"{VOCAB[args.dataset][0]}: {', '.join(unknown)}")
    codes, forms = select(chars, types, cells, args.component, mechanism, args.dataset)
    if not codes:
        sys.exit(f"no characteristics with component '{args.component}' in "
                 f"{VOCAB[args.dataset][0]} — check the component name against "
                 f"that vocabulary, not the other dataset's")

    if args.format == "md":
        text = render_md(chars, types, cells, codes, forms, args.component, mechanism,
                         claim, args.dataset)
        default = ROOT / "views" / f"{args.dataset}--{args.component}.md"
    else:
        text = render_tex(chars, types, cells, codes, forms, args.component, mechanism,
                          claim, args.dataset)
        default = ROOT / "views" / f"{args.dataset}--{args.component}.tex"

    out = Path(args.out) if args.out else default

    if args.check:
        if not out.exists():
            print(f"{out}: missing", file=sys.stderr)
            return 1
        if out.read_text(encoding="utf-8") != text:
            print(f"{out}: stale — regenerate with build_views.py", file=sys.stderr)
            return 1
        print(f"{out}: current")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {out} ({len(forms)} forms × {len(codes)} characteristics)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
