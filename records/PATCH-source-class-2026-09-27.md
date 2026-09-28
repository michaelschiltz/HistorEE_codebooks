# PATCH (proposed, not applied): `source_class` in `recodings.csv`, 2026-09-27

**Status: APPLIED 2026-09-28, approved by MS.** One correction was made at application: the codebooks **did** need regenerating (§6 below said otherwise). See logbook 1, 2026-09-27. *(Original status: a proposal for MS; nothing written.)* The decision to add the column was MS's (2026-09-27), made in the methodological discussion recorded in the vault note *Hold the rater fixed and vary the evidence*. This file specifies the change for approval.

## Why

A re-coding pass that varies the evidence (the commenda pilot, `claude/commenda-pilot-design-2026-09-27.md`) is only interpretable if every re-coded cell says which *class* of source it rests on. The pass slug carries the class implicitly, but a slug cannot be queried or validated and says nothing about a mixed citation. The census treats three things differently:

- the secondary literature, which compresses practice;
- normative primary texts, which are themselves compressions;
- transactional primary documents, which are the instance-level evidence.

It needs a column that keeps them apart.

## The change

**One field, appended after `notes`** in the `recodings` resource of both censuses. Appending moves no existing column for a positional reader, on the `coder_model`/`coder_effort` precedent of 2026-09-26.

```json
{
  "name": "source_class",
  "type": "string",
  "title": "Source class",
  "description": "Class of the source(s) in `source_ref`, judged by the cited passage, not by the container. `secondary`: a modern author's account of the institution, including documents they quote inside their own argument. `primary-transactional`: an edited or transcribed contract, notarial act, ledger, letter or court entry, including a transcription printed in an appendix to a secondary work. `primary-normative`: a code, statute, custom, sea law, fatwa or juristic treatise stating a rule. `primary-institutional`: a charter, minute, resolution, placard or register of an institution's own proceedings. `mixed`: `source_ref` cites passages of more than one class; `notes` should say which carries the value. `.NA` where the row has no source.",
  "constraints": {
    "enum": ["secondary", "primary-transactional", "primary-normative", "primary-institutional", "mixed"]
  }
}
```

The dataset's `missingValues` already include `.NA` (and `.NR`, `.IL`, empty), so they pass the enum as elsewhere. **Should `source_class` be `required`?** Recommended **no**, matching `coder_model`: a blank is then a declared missing value, and the application procedure, not the schema, is what guarantees that every new row carries it.

## Classification rule, for MS to approve

1. **Judge the cited passage, not the publication.** A transcription in Kıvrım 2019's appendix (Ek, printed pp. 43–49) is `primary-transactional` even though the article is secondary.
2. **A document quoted inside an author's own argument is `secondary`.** The author chose, cut and framed it. Example: Kıvrım 38 quoting GŞS 33-328/2 in his running text.
3. **An editor's apparatus is `secondary`.** This covers regesti, headings and commentary, e.g. Pryor 1981's chapter essays, even though they share a PDF with the notulae.
4. **More than one class in one `source_ref` is `mixed`**, and the note names the passage that carries the value.

## Backfill of the 64 existing rows (pass `opus55-recode-mutual-pole-2026-09-26`)

The rule was applied mechanically: Kıvrım pages ≥ 43 were read as Ek transcriptions, and everything else was read as secondary.

| class                                   | rows |
|-----------------------------------------|------|
| `secondary`                             | 54   |
| `mixed`                                 | 5    |
| `.NA` (value `.NA`, `source_ref` `.NA`) | 5    |

The five `mixed` rows each cite Kıvrım's appendix transcriptions *alongside* secondary text:

| recoding_id | form         | char | source_ref                                                                   |
|-------------|--------------|------|------------------------------------------------------------------------------|
| OF-R0002    | avariz_vakfi | LP2  | Kars 2020, 164, 176-184; Kıvrım 2019, 43-47                                  |
| OF-R0005    | avariz_vakfi | AP2  | Kars 2020, 167, 179; Küçük 2025, 151; Kıvrım 2019, 48                        |
| OF-R0012    | avariz_vakfi | CI1  | Kars 2020, 174; Gürsoy 2019, 105; Küçük 2025, 153; Kıvrım 2019, 39, 45-47    |
| OF-R0013    | avariz_vakfi | CI2  | Kars 2020, 167, 179; Küçük 2025, 151, 154; Kıvrım 2019, 48; Gürsoy 2019, 110 |
| OF-R0023    | avariz_vakfi | MG2  | Kıvrım 2019, 38, 47-48; Küçük 2025, 160; Kars 2020, 173                      |

**Two caveats, stated rather than resolved:**

- The Ek boundary (43–49) is the coding chat's measurement (`records/NOTES-opus55-recode-mutual-pole-coding-2026-09-26.md` §1). It has not been re-verified here.
- The backfill fills a **metadata** field on the 64 rows. It does not touch `value`, `agreement` or any other field, and it reconsiders no cell. The rows' notes are not edited to say which passage carries the value on the five `mixed` rows. That would be an edit to the frozen coding record, so it is left for adjudication.

`loss_mitigation_forms/recodings.csv` is header-only: it gains the header field and no rows.

## Versions

Adding a field is schema growth (CONTRIBUTING §5):

- `organizational_forms` **0.10.0 → 0.11.0**;
- `loss_mitigation_forms` **0.7.0 → 0.8.0**.

## Considered and rejected

- **Adding `source_class` to `data.csv` now.** Rejected for this patch. It would mean classifying 1,573 `source_ref` values, of which at least 101 are `[verify]`-only. That is a pass in its own right, not a schema tweak. It is recommended as a separate, licensed pass once the pilot shows the class matters. Until then, a live cell's class is determined per pilot, in the pilot's own record.
- **A multi-valued field** (e.g. `secondary;primary-transactional`). Rejected: frictionless cannot enforce an enum on a delimited list, and the census has no list-valued field. `mixed` plus the note carries the same information and stays validated.
- **Encoding the class in the pass slug only.** Rejected: it cannot be queried, it cannot be validated, and it cannot express a mixed citation.
- **Placing the column after `source_read`.** Logically neater, but it would move five existing columns for a positional reader. Appending follows the 2026-09-26 precedent.

## Application procedure (when approved)

1. **Verify the destination:**
   - `recodings.csv` holds 64 rows and a 21-field header in `organizational_forms`, and a header only in `loss_mitigation_forms`;
   - both `datapackage.json` versions are as above;
   - the check suite is green.
2. **Datapackages.** Add the field to the `recodings` resource in both. Bump both versions.
3. **The two CSVs are a rewrite, not an append**, because a column is added:
   - round-trip each file first (`csv.reader` → `csv.writer(lineterminator='\n')`) and `cmp` it;
   - write the new column;
   - assert that for every row the first 21 fields are byte-identical to the original.
4. **Backfill** exactly the table above. The class is recomputed from the file by the stated rule, not typed in.
5. **Documentation:**
   - **CHANGELOG:** one block for both censuses, including this "considered and rejected" list.
   - **Logbook 1:** architecture: why the class is judged by the passage.
   - **CLAUDE.md, Attribution section:** one sentence saying every new `recodings.csv` row fills `source_class`. The skills `run-a-coding-batch` and `code-a-form` need the same line; MS updates skills.
6. **Checks:**
   - `check_vocabularies.py`, `check_softwrap.py`, `check_tables.py`;
   - `check_dependence.py` on both dataset **directories**;
   - `build_codebook.py --check`: *(corrected at application: stale, because `codebook.md` prints the version; regenerated)*;
   - all views `--check`: unchanged;
   - `python3 -m frictionless validate` on both datapackages.
7. **Scripts: no change needed.** `make_blind_bundle.py` scrubs `recodings.csv` using the file's own header, so the new column is carried through. `build_codebook.py` documents only the first resource, so `recodings.csv` still does not appear in any codebook; that gap is pre-existing, flagged on 2026-09-26 and still open.

## Draft commit message

```
Add source_class to recodings.csv in both censuses

Schema growth, additive: organizational_forms 0.10.0 -> 0.11.0,
loss_mitigation_forms 0.7.0 -> 0.8.0. One field appended after notes
in the recodings resource: secondary | primary-transactional |
primary-normative | primary-institutional | mixed, judged by the
cited passage rather than the publication.

Backfill of the 64 opus55-recode-mutual-pole rows: 54 secondary,
5 mixed (Kivrim 2019 Ek transcriptions cited with secondary text),
5 .NA. No value, agreement or adjudication field touched.

Not added to data.csv: classifying 1,573 source_refs is its own pass.
```
