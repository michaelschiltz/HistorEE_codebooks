# Blind bundle: compania-sevilla-2026-11-19

A first coding of a new form for the `organizational_forms` census of HistorEE_codebooks, from one printed edition of Seville notarial deeds. No row of this form exists yet, so nothing in the bundle has been removed by type.

## What is in the bundle

- `HistorEE_codebooks/`: a working copy of the repository, as of 2026-11-19. Read `CLAUDE.md`, `CONTRIBUTING.md` (§3 and §4 above all), `CHARACTER-CODING.md` and `EDITING-CSV.md`, and `vocabularies/organizational_form_characteristic.csv` with its full definitions. `CHANGELOG.md` has been removed, and one dated logbook section has been withheld. Do not run anything that writes into this folder; `build_views.py` writes by default, so use `--check` or read the committed views as files.
- `myfoamrepo/`: a copy of the maintainer's vault. It is context, not evidence for the cells.
- `sources/Martinez-Gijon-1970-AHDE40-pp43-84.pdf`: the only source for this pass. J. Martínez Gijón, "La práctica del comercio por intermediario en el tráfico con las Indias durante el siglo XVI", *Anuario de Historia del Derecho Español* 40 (1970), pp. 5–84. The excerpt is printed pp. 43–83: the Apéndice documental, ten deeds from the Archivo de Protocolos de Sevilla. PDF page *n* of the excerpt is printed page *n*+42. The pages are the original scans (1-bit images) under an OCR text layer made on 2026-11-18. Render any page with `pdftoppm -f N -l N -r 200 -png` to read it as an image.
- `PRIORS-TEMPLATE.md`: to be filled before you open `sources/`.
- `proposed-of/`: where everything you write goes.

## The form to be coded

Working type code `compania_factoria_sevilla`, in `organizational_forms`. The maintainer has scoped it as follows, before any coding:

- A partnership contracted before a Seville notary for trade with the Indies, in which one or more partners supply the capital and another partner travels to the Indies, resides there and manages the sale and reinvestment of the goods, for a share of the profit.
- Its relation to the Catalan comanda and the Italian commenda rows already in the census is a comparison, not an identity. This is a separate form: other period, other jurisdiction, other notarial practice.
- Commission agency (*encomienda*, *comisión*: sale of another's goods for a percentage) is out of scope as a form.
- Scope in time and place is what the deeds you assign to the form show; do not extend it from general knowledge.

## The edition

- The editor states (printed p. 43, note) that he modernised the spelling. Quotations are his text, cited by printed page and by the deed's APS reference.
- The editor's rubrics in small capitals (and any heading) are not evidence of roles or of type. Read the clauses.
- The OCR layer is fair in the deeds' running text and poor in numerals in headings, archival lines and folio markers, and in proper names. Quote every passage you rely on from the page image, and check every numeral, name and coded absence against the image. An absence read off the text layer is a claim about the layer.
- The editor's study (printed pp. 5–42) is not in the bundle. Page 43 begins with its last lines.

## What you do with the deeds

1. Read all ten deeds in full.
2. For each deed, decide whether it is an instance of the form as scoped above, and say why, from its clauses.
3. Record every deed, assigned or not, in an instance file (`proposed-of/INSTANCES-compania-sevilla-2026-11-19.csv`) with this header, one row per deed:

   `instance_id,doc_no,page_printed,date,notary,aps_ref,rubric,parties,party_roles,capital_principals,capital_factor,currency,destination,duration_clause_quote,duration,profit_rule_quote,profit_rule,loss_rule_quote,loss_rule,termination_quote,termination,restraints_quote,other_clauses_quote,assigned_to_form,assignment_reason,quote_checked_against_image,notes`

   Leave a field `.NR` where the deed does not address it.
4. Code all 33 characteristics of `organizational_form_characteristic.csv` for the new form, from the deeds assigned to it, as a proposed row fragment, and propose the type row for `vocabularies/organizational_form_type.csv`.
