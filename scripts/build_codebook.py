#!/usr/bin/env python3
"""Generate codebook.md for every dataset from its datapackage.json.

One source of truth: the schema. The human-readable codebook is compiled, never
hand-edited. Standard library only, so it runs anywhere with no install.

Usage:
    python scripts/build_codebook.py          # regenerate all
    python scripts/build_codebook.py <dir>    # regenerate one dataset folder
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "datasets"


def coverage(csv_path: Path, fields: list[dict], missing: list[str]) -> tuple[int, dict[str, int]]:
    """Count rows and, per field, how many are present (not a missing token)."""
    miss = set(missing)
    present: dict[str, int] = {f["name"]: 0 for f in fields}
    rows = 0
    if not csv_path.exists():
        return 0, present
    with csv_path.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            rows += 1
            for f in fields:
                v = (row.get(f["name"]) or "").strip()
                if v != "" and v not in miss:
                    present[f["name"]] += 1
    return rows, present


def md_escape(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ")


def md_table(headers: list[str], rows: list[list[str]], aligns: str = "") -> list[str]:
    """Render an aligned GitHub-flavoured markdown table.

    aligns: one char per column, 'l' (default) / 'c' / 'r'.
    """
    aligns = (aligns + "l" * len(headers))[: len(headers)]
    widths = [len(h) for h in headers]
    for row in rows:
        for i, c in enumerate(row):
            widths[i] = max(widths[i], len(c))

    def cell(text: str, w: int, a: str) -> str:
        return text.rjust(w) if a == "r" else text.center(w) if a == "c" else text.ljust(w)

    def sep(w: int, a: str) -> str:
        if a == "r":
            return "-" * (w + 1) + ":"
        if a == "c":
            return ":" + "-" * w + ":"
        return "-" * (w + 2)

    lines = ["| " + " | ".join(cell(h, w, a) for h, w, a in zip(headers, widths, aligns)) + " |"]
    lines.append("|" + "|".join(sep(w, a) for w, a in zip(widths, aligns)) + "|")
    for row in rows:
        lines.append("| " + " | ".join(cell(c, w, a) for c, w, a in zip(row, widths, aligns)) + " |")
    return lines


def build(dataset_dir: Path) -> Path:
    dp = json.loads((dataset_dir / "datapackage.json").read_text(encoding="utf-8"))
    res = dp["resources"][0]
    schema = res["schema"]
    fields = schema["fields"]
    missing = schema.get("missingValues", [""])
    csv_path = dataset_dir / res["path"]
    n_rows, present = coverage(csv_path, fields, missing)

    lic = ", ".join(l.get("name", "") for l in dp.get("licenses", [])) or "—"
    contribs = ", ".join(
        f'{c.get("title","")} ({c.get("role","")})' for c in dp.get("contributors", [])
    ) or "—"

    out = []
    w = out.append
    w(f"# Codebook — {dp.get('title', dp['name'])}\n")
    w("> **Generated file.** Do not edit by hand. Produced by "
      "`scripts/build_codebook.py` from `datapackage.json`. "
      "Edit the schema and regenerate.\n")
    w(f"- **Dataset**: `{dp['name']}`  ")
    w(f"- **Version**: {dp.get('version','—')}  ")
    w(f"- **License**: {lic}  ")
    w(f"- **Contributors**: {contribs}  ")
    w(f"- **Rows**: {n_rows}  ")
    w("- **Generated**: deterministically from `datapackage.json` "
      "(timestamps via Git history)\n")
    w(f"\n{dp.get('description','')}\n")

    w("\n## Provenance\n")
    w("Attribution and timestamps are supplied by Git (`git blame` for line-level "
      "history); releases are frozen and citable via a FigShare and Zenodo DOI. "
      "Per-observation coder attribution is carried in the `coder` field.\n")

    w("\n## Missing-value conventions\n")
    w("Absence is coded, never blank. These tokens are treated as missing by the "
      "schema (`missingValues`):\n")
    for line in md_table(
        ["Token", "Meaning"],
        [
            ["`.NR`", "not recorded in the source"],
            ["`.IL`", "present but illegible / damaged"],
            ["`.NA`", "not applicable to this record type"],
        ],
    ):
        w(line)
    w("\n> `.ZERO` is **not** here: a source-recorded zero is the value `0`, a datum, "
      "not an absence (see the `missingness` field).\n")

    w("\n## Variables at a glance\n")
    rows = []
    for i, f in enumerate(fields, 1):
        c = f.get("constraints", {}) or {}
        req = "✓" if c.get("required") else ""
        enum = ", ".join(f"`{v}`" for v in c["enum"]) if "enum" in c else ""
        cov = f"{present.get(f['name'], 0)}/{n_rows}" if n_rows else "—"
        rows.append([str(i), f"`{f['name']}`", f.get("type", ""), req, md_escape(enum), cov])
    for line in md_table(["#", "Field", "Type", "Required", "Coded values", "Present"], rows, aligns="rllclr"):
        w(line)

    w("\n## Variable definitions\n")
    for f in fields:
        c = f.get("constraints", {}) or {}
        w(f"\n### `{f['name']}` — {md_escape(f.get('title',''))}\n")
        w(f"{md_escape(f.get('description',''))}\n")
        bits = [f"**type** {f.get('type','')}"]
        if c.get("required"):
            bits.append("**required**")
        if c.get("unique"):
            bits.append("**unique**")
        if c.get("pattern"):
            bits.append(f"**pattern** `{c['pattern']}`")
        if "enum" in c:
            bits.append("**values** " + ", ".join(f"`{v}`" for v in c["enum"]))
        w("- " + " · ".join(bits) + "\n")

    text = "\n".join(out) + "\n"
    dest = dataset_dir / "codebook.md"
    dest.write_text(text, encoding="utf-8")
    return dest


def main() -> None:
    targets = (
        [Path(sys.argv[1])]
        if len(sys.argv) > 1
        else sorted(
            p for p in DATASETS.iterdir()
            if (p / "datapackage.json").exists() and not p.name.startswith("_")
        )
    )
    for d in targets:
        dest = build(d)
        print(f"wrote {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
