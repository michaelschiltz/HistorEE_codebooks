#!/usr/bin/env python3
"""Check that every work cited in a `source_ref` resolves to an item in the maintainer's Zotero library.

`source_ref` stays what it is: a Chicago author-date short form ("Kars 2020, 175; Küçük 2025, 149-151"),
readable in the codebook and the views. Resolution lives in a separate registry, `references/works.csv`,
one row per distinct work label as it is written in `source_ref`:

    label,zotero_key,citekey,status,notes
    Kars 2020,GAZN2XVN,karsYuzyilaAitIstanbul2020,resolved,
    Cizakca 2000,,,not-in-library,"no 2000 item in the library; A History of Philanthropic Foundations?"

`status` is one of
    resolved        zotero_key and citekey required
    not-in-library  the work is cited but has no Zotero item yet (warning; error under --strict)
    ambiguous       several candidate items; the candidates are listed in notes (warning; error under --strict)

Three modes, all read-only with respect to data, registry and Zotero:

    python scripts/check_citations.py                 # offline; what CI runs
    python scripts/check_citations.py --zotero        # also verify the registry against the local library
    python scripts/check_citations.py --zotero --bootstrap proposed-of/works-candidates.csv
                                                      # propose rows for unregistered works, for adjudication

Offline checks (no Zotero needed):
    E1  an author-date-shaped head ("Surname[ et al.] YYYY[a]") with no registry row
    E2  an inline "(Zotero XXXXXXXX)" key that disagrees with the registry row of the same work
    E3  registry hygiene: duplicate labels, unknown status, a resolved row without key or citekey,
        a malformed key
    W1  a registry row whose status is not-in-library or ambiguous
    W2  a non-missing source_ref with no anchored work at all
    W3  a registry label that no source_ref uses (stale row)
    N1  unanchored segments (commentary, sub-locators, "repeated in ..."): counted, listed with --verbose

--zotero adds:
    E4  a resolved zotero_key that is not in the library, is in the trash, or is an attachment/note
    E5  a citekey that differs from the item's Better BibTeX / Zotero citation key
    W4  a label year that differs from the item's year (often legitimate: reprints, editions, archival
        dates; listed so each one is looked at once)

The library is read from a temporary copy of zotero.sqlite, never in place, so a running Zotero is
neither locked nor written. The data directory is taken from --zotero DIR, else from Zotero's prefs.js
(extensions.zotero.dataDir), else ~/Zotero.

Exit status 1 on any E (or on any W with --strict). Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import glob
import re
import shutil
import sqlite3
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "references" / "works.csv"
REGISTRY_FIELDS = ["label", "zotero_key", "citekey", "status", "notes"]
STATUSES = {"resolved", "not-in-library", "ambiguous"}
MISSING = {"", ".NA", ".NR", ".IL"}
KEY_RE = re.compile(r"^[A-Z0-9]{8}$")
INLINE_KEY_RE = re.compile(r"\bZotero ([A-Z0-9]{8})\b")
YEAR = r"(1[0-9]{3}|20[0-3][0-9])[a-z]?"
# An author-date head: up to eight words of name material (commas, '&', 'and', particles and CJK allowed),
# then a year followed by end, space, comma, semicolon or parenthesis.
AD_RE = re.compile(r"^(?P<auth>[^\d;()]{1,90}?)\s+(?P<year>" + YEAR + r")(?=$|[\s,;(])")
# Name material that is really a locator or an edition statement, not an author list.
NOT_AUTHOR_RE = re.compile(r"\b(ed|eds|no|nos|vol|p|pp|nr|nrs|c|fol|ff)\.|^(repeated|see|cf\.|also|and|against)\b", re.I)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def fold(s: str) -> str:
    """Casefold and strip diacritics, for candidate matching only (never for the checks themselves)."""
    s = unicodedata.normalize("NFKD", s.casefold())
    return "".join(ch for ch in s if not unicodedata.combining(ch)).replace("ı", "i")


def split_top(ref: str) -> list[str]:
    """Split a source_ref on ';' outside parentheses and brackets."""
    out, depth, cur = [], 0, []
    for ch in ref:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur))
    return [s.strip() for s in out if s.strip()]


def author_date_head(segment: str) -> str | None:
    m = AD_RE.match(segment)
    if not m:
        return None
    auth = m["auth"].strip()
    if NOT_AUTHOR_RE.search(auth) or len(auth.split()) > 8:
        return None
    return f"{auth} {m['year']}"


def load_registry(errors: list[str]) -> dict[str, dict]:
    if not REGISTRY.exists():
        return {}
    reg: dict[str, dict] = {}
    with REGISTRY.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != REGISTRY_FIELDS:
            errors.append(f"E3 {REGISTRY.relative_to(ROOT)}: header must be {','.join(REGISTRY_FIELDS)}")
            return {}
        for n, row in enumerate(reader, start=2):
            label = nfc(row["label"].strip())
            where = f"E3 works.csv line {n} ({label!r})"
            if not label:
                errors.append(f"{where}: empty label")
                continue
            if label in reg:
                errors.append(f"{where}: duplicate label")
                continue
            if row["status"] not in STATUSES:
                errors.append(f"{where}: status {row['status']!r} not in {sorted(STATUSES)}")
            if row["status"] == "resolved" and not (row["zotero_key"] and row["citekey"]):
                errors.append(f"{where}: resolved rows need zotero_key and citekey")
            if row["zotero_key"] and not KEY_RE.match(row["zotero_key"]):
                errors.append(f"{where}: zotero_key {row['zotero_key']!r} is not an 8-character item key")
            reg[label] = row
    return reg


def iter_refs():
    """Yield (file, record_id, source_ref) for every data.csv and recodings.csv row that has a source_ref."""
    for f in sorted(glob.glob(str(ROOT / "datasets" / "*" / "*.csv"))):
        p = Path(f)
        if p.parent.name == "_template" or p.name not in {"data.csv", "recodings.csv"}:
            continue
        with p.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                if "source_ref" not in row:
                    break
                rid = row.get("record_id") or row.get("recoding_id") or "?"
                yield p.relative_to(ROOT), rid, nfc(row["source_ref"] or "")


def match_label(segment: str, labels_by_len: list[str]) -> str | None:
    for label in labels_by_len:  # longest first
        if segment.startswith(label) and (len(segment) == len(label) or not segment[len(label)].isalnum()):
            return label
    return None


# --------------------------------------------------------------------------------------------------
# Zotero (read-only, from a temporary copy of zotero.sqlite)


def zotero_data_dir(arg: str | None) -> Path:
    if arg:
        return Path(arg).expanduser()
    for prefs in glob.glob(str(Path.home() / "Library/Application Support/Zotero/Profiles/*/prefs.js")) + glob.glob(
        str(Path.home() / ".zotero/zotero/*/prefs.js")
    ):
        text = Path(prefs).read_text(encoding="utf-8", errors="replace")
        m = re.search(r'user_pref\("extensions\.zotero\.dataDir",\s*"(.+?)"\);', text)
        if m:
            return Path(m.group(1).encode().decode("unicode_escape"))
    return Path.home() / "Zotero"


class Library:
    def __init__(self, data_dir: Path):
        src = data_dir / "zotero.sqlite"
        if not src.exists():
            sys.exit(f"no zotero.sqlite in {data_dir}; pass the data directory with --zotero DIR")
        self.tmp = tempfile.TemporaryDirectory()
        dst = Path(self.tmp.name) / "zotero.sqlite"
        shutil.copy2(src, dst)
        for ext in ("-wal", "-shm"):
            if (data_dir / f"zotero.sqlite{ext}").exists():
                shutil.copy2(data_dir / f"zotero.sqlite{ext}", Path(self.tmp.name) / f"zotero.sqlite{ext}")
        self.db = sqlite3.connect(f"file:{dst}?mode=ro", uri=True)
        self.source = src
        self._fields = {}

    def close(self):
        self.db.close()
        self.tmp.cleanup()

    def item(self, key: str) -> dict | None:
        row = self.db.execute(
            """SELECT i.itemID, t.typeName, i.libraryID,
                      EXISTS(SELECT 1 FROM deletedItems d WHERE d.itemID = i.itemID)
               FROM items i JOIN itemTypes t USING (itemTypeID)
               WHERE i.key = ? AND i.libraryID = 1""",
            (key,),
        ).fetchone()
        if not row:
            return None
        item_id, type_name, _, trashed = row
        return {
            "id": item_id,
            "type": type_name,
            "trashed": bool(trashed),
            "year": self.year(item_id),
            "citekey": self.citekey(item_id),
            "title": self.field(item_id, "title"),
        }

    def field(self, item_id: int, name: str) -> str:
        row = self.db.execute(
            """SELECT v.value FROM itemData d
               JOIN fields f USING (fieldID) JOIN itemDataValues v USING (valueID)
               WHERE d.itemID = ? AND f.fieldName = ?""",
            (item_id, name),
        ).fetchone()
        return row[0] if row else ""

    def year(self, item_id: int) -> str:
        date = self.field(item_id, "date")  # stored as "YYYY-MM-DD original"
        m = re.match(r"(\d{4})", date)
        return m.group(1) if m else ""

    def citekey(self, item_id: int) -> str:
        key = self.field(item_id, "citationKey")
        if key:
            return key
        m = re.search(r"^Citation Key:\s*(\S+)", self.field(item_id, "extra"), re.M)
        return m.group(1) if m else ""

    def candidates(self, surname: str, year: str) -> list[tuple[str, str, str, str]]:
        """Top-level items in the personal library whose creator matches surname and whose year matches."""
        token = fold(surname).split()[-1] if surname.split() else ""
        if not token:
            return []
        rows = self.db.execute(
            """SELECT DISTINCT i.key, i.itemID, c.lastName, c.firstName
               FROM items i
               JOIN itemTypes t USING (itemTypeID)
               JOIN itemCreators ic USING (itemID)
               JOIN creators c USING (creatorID)
               WHERE i.libraryID = 1
                 AND t.typeName NOT IN ('attachment', 'note', 'annotation')
                 AND i.itemID NOT IN (SELECT itemID FROM deletedItems)"""
        ).fetchall()
        out = []
        for key, item_id, last, first in rows:
            names = {fold(last or ""), fold(first or "")}  # CJK names are sometimes stored swapped
            if not any(n == token or n.endswith(" " + token) or token in n.split() for n in names if n):
                continue
            if self.year(item_id) != year[:4]:
                continue
            n_att = self.db.execute("SELECT COUNT(*) FROM itemAttachments WHERE parentItemID = ?", (item_id,)).fetchone()[0]
            title = f"{self.field(item_id, 'title')[:70]} [{n_att} att]"
            out.append((key, self.citekey(item_id), self.year(item_id), title))
        return sorted(set(out))


def first_surname(label: str) -> str:
    auth = re.sub(r"\s+" + YEAR + r"$", "", label)
    return re.split(r",|\s&\s|\sand\s|ほか|\set al\.?", auth)[0].strip()


# --------------------------------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--zotero", nargs="?", const="", metavar="DIR", help="verify against the local Zotero library")
    ap.add_argument("--bootstrap", metavar="OUT.csv", help="with --zotero: write candidate registry rows for unregistered works")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--verbose", action="store_true", help="list unanchored segments and every warning")
    args = ap.parse_args()
    if args.bootstrap and args.zotero is None:
        ap.error("--bootstrap needs --zotero")
    if args.bootstrap and Path(args.bootstrap).resolve() == REGISTRY.resolve():
        ap.error("--bootstrap never writes the registry itself; write to proposed-of/ and adjudicate")

    errors: list[str] = []
    warnings: list[str] = []
    reg = load_registry(errors)
    labels_by_len = sorted(reg, key=len, reverse=True)

    used = Counter()
    unregistered: dict[str, list[str]] = defaultdict(list)
    unanchored = Counter()
    n_refs = n_verify = n_bare = 0

    for path, rid, ref in iter_refs():
        if ref in MISSING:
            continue
        n_refs += 1
        n_verify += "[verify]" in ref
        n_bare += ref.strip() == "[verify]"
        anchored = False
        for seg in split_top(ref):
            seg = re.sub(r"^\[verify\]\s*", "", seg).strip()
            if not seg:
                continue
            label = match_label(seg, labels_by_len)
            if label:
                anchored = True
                used[label] += 1
                for k in INLINE_KEY_RE.findall(seg):
                    if reg[label]["zotero_key"] and k != reg[label]["zotero_key"]:
                        errors.append(f"E2 {path} {rid}: inline Zotero {k} but works.csv has {reg[label]['zotero_key']} for {label!r}")
                continue
            head = author_date_head(seg)
            if head:
                anchored = True
                unregistered[head].append(f"{path.parent.name}/{path.name}:{rid}")
            else:
                unanchored[seg[:90]] += 1
        if not anchored:
            warnings.append(f"W2 {path} {rid}: no anchored work in {ref[:100]!r}")

    for head, where in sorted(unregistered.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        errors.append(f"E1 unregistered work {head!r} ({len(where)} segments; first {where[0]})")
    for label, row in reg.items():
        if row["status"] in {"not-in-library", "ambiguous"}:
            warnings.append(f"W1 {label!r}: {row['status']}" + (f" ({row['notes']})" if row["notes"] else ""))
        if not used[label]:
            warnings.append(f"W3 {label!r}: in works.csv but cited nowhere")

    lib = None
    if args.zotero is not None:
        lib = Library(zotero_data_dir(args.zotero or None))
        for label, row in reg.items():
            if row["status"] != "resolved":
                continue
            it = lib.item(row["zotero_key"])
            if it is None:
                errors.append(f"E4 {label!r}: {row['zotero_key']} is not in the personal library")
                continue
            if it["trashed"]:
                errors.append(f"E4 {label!r}: {row['zotero_key']} is in the trash")
            if it["type"] in {"attachment", "note", "annotation"}:
                errors.append(f"E4 {label!r}: {row['zotero_key']} is an {it['type']}, not a work")
            if it["citekey"] and it["citekey"] != row["citekey"]:
                errors.append(f"E5 {label!r}: citekey {row['citekey']!r} but the library has {it['citekey']!r}")
            m = re.search(YEAR + r"$", label)
            if m and it["year"] and it["year"] != m.group(0)[:4]:
                warnings.append(f"W4 {label!r}: label year {m.group(0)[:4]}, item year {it['year']} ({it['title'][:60]})")

    if args.bootstrap:
        out = Path(args.bootstrap)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(REGISTRY_FIELDS)
            for head in sorted(unregistered):
                year = re.search(YEAR + r"$", head).group(0)
                cands = lib.candidates(first_surname(head), year)
                if len(cands) == 1:
                    # Still a proposal: matching runs on romanised surnames, so an original-script twin of the
                    # same work (the copy actually read) is invisible to it. Check before accepting.
                    key, citekey, _, title = cands[0]
                    w.writerow([head, key, citekey, "resolved", f"bootstrap: single candidate - {title}"])
                elif cands:
                    w.writerow([head, "", "", "ambiguous", " | ".join(f"{k} {c} {t}" for k, c, _, t in cands)])
                else:
                    w.writerow([head, "", "", "not-in-library", "bootstrap: no item with this surname and year"])
        print(f"wrote {len(unregistered)} candidate rows to {out} - adjudicate, then move the accepted rows into {REGISTRY.relative_to(ROOT)}")

    if lib:
        lib.close()

    print(f"{n_refs} source_refs ({n_verify} carrying [verify], {n_bare} of them nothing else) · {len(reg)} registered works · "
          f"{len(unregistered)} unregistered · {sum(unanchored.values())} unanchored segments")
    for e in errors:
        print(e)
    shown = warnings if args.verbose else warnings[:25]
    for w_ in shown:
        print(w_)
    if len(shown) < len(warnings):
        print(f"... {len(warnings) - len(shown)} more warnings (--verbose)")
    if args.verbose:
        for seg, n in unanchored.most_common():
            print(f"N1 {n:4d}  {seg}")
    failed = bool(errors) or (args.strict and bool(warnings))
    print(("FAIL" if failed else "OK") + f": {len(errors)} errors, {len(warnings)} warnings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
