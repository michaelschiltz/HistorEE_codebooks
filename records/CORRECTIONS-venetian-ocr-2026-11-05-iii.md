# Venetian OCR check, third part (2026-11-05): parties, roles, places and notaries of the 121 instances

**Applied by the assistant (`claude-opus-5-5`) on 2026-11-05 at MS's instruction ("Let's go on").** The ledger is `records/CORRECTIONS-venetian-ocr-2026-11-05-iii.csv`: 68 changes, one per field.

Successor file: `records/INSTANCES-venetian-pass-2026-11-05-ii.csv` (121 rows) succeeds `INSTANCES-venetian-pass-2026-11-05.csv`, which is untouched. No characteristic state, `n_parties`, form assignment or live cell changes.

## What was checked

The verbatim name fields of all 121 instances (`parties`, `place`, `notary`) were checked first by script against the act's text, then on the page image for every flag.

- The scripts read the 2026-11-03 layer and the bundle.
- Roles were checked against the operative words of the act («ego … recepi a te», «securitatem facio ego … tibi»), never against the editors' regest (CONTRIBUTING §3).
- Where the script could not find an act's opening, the bundle's text of the act was read.

## Findings

- **Wrong absences in `parties`: 29.** A party coded `.NR` stands named in the operative clause («a te namque Matheo Marçolo», «a vobis Iohanne Caucanino et Panchratio Signolo»).
  - The coder had read them: every `n_parties` and every note agrees with the act. The display field was missed in extraction.
  - All are filled from the image, in the printed form.
  - Act 539 stays `.NR`: it is a fragment whose names fall in a lacuna. The editors' regest names a party, but a regest is not evidence of roles.
- **Garbled names: 5 corrected:**
  - 045 «Aurius Navigaiosus et irrev» → «Aurius Navigaiosus»; its releasee «Bi lonzo» → «Bilongo»;
  - 418 «Frugerius S2nalori» → «Frugerius Senatori»;
  - 667 «Vidota mei»;
  - 704 «[Maia] «9 Pasqual»;
  - 801 «Marco Spatario valoris».
  - Lacunae are kept as printed («[Maria] …… Pasqual ……»).
  - No. 401's releasee stays «Peiro Teupulo»: the print reads «Peiro».
- **Roles: 1 wrong.**
  - No. 42 named «Petro patri tuo» as releasee. The act releases «Iohanni Mauro filio Petri Mauri»; Petrus is the consenting father («consenciente tibi Petro patri tuo»).
  - No coded state changes: `n_parties` 2, CF3 `bilateral` and CF1 `P` all rest on the two principals.
  - Every other assignment matches the operative words, including the multi-party acts 622 (two receivers) and 782 (two investors).
- **Places: 3 corrected:**
  - 045 `.NR` → «Constantinopoli»;
  - 405 «Hivoallo [read by fallback]» → «Rivoalto»;
  - 418 `.NR` → «Rivoalto».
- **Notaries: 3 filled from the image:**
  - 380 Matheus Capello;
  - 400 Warientus Calbo;
  - 418 Wido Gisperto (the layer reads «Gisperlo»).
  - Each completio stands between its act's opening and the next act. The completio found on an act's pages can belong to the act before it, as at no. 512.
  - 489, 512 and 654 stay `.NR`: no completio is printed between the act's opening and the next act. At 489 the editors only attribute the notary.

## Not changed

Party names that the old layer misread but that remain recognisable (*Pelrus Teu pulus*, *Lagaro*) are left as recorded, except where an entry was rewritten for the reasons above. They are the coder's verbatim record. No count depends on their spelling.
