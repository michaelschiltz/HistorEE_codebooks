#!/usr/bin/env python3
"""Add societas_maris to organizational_form_type.csv and record the mudaraba determination."""
import csv, sys, pathlib

TRIAD = "Coded 2026-08-18; see logbook 2 and logbook 4 for that date."

NEW = {
"societas_maris": dict(
  name="Societas maris (the bilateral commenda; Venetian collegantia)",
  tradition="Venetian / Genoese",
  period="12c-13c (Genoese corpus 1154-c.1300)",
  key_source=(
    "ADDED 2026-08-18 as a new type row - the code did not previously exist in this vocabulary, though it does in "
    "loss_mitigation_type.csv, where it is now coded. van Doosselaere 2009, 64-68: the Genoese notarial cartularies, 6,764 "
    "commenda ties 1154-1315, 93 per cent of all coded maritime ties. p.65 states the two liability rules side by side - the "
    "unilateral investor 'bore all liability for loss' and the traveller 'bore no capital risk', while in the bilateral form, "
    "'often called SOCIETAS IN GENOA', 'the liability for loss was proportional to the respective initial investments'. "
    "Contribution ratio customarily one third traveller, two thirds investor; profit split equally. Harris 2007, 9-13; Held "
    "2025, 22 for the Ragusan contracts sharing lucrum and damnum in the same proportions. "
    "CODED ON EXACTLY THE ELEVEN CHARACTERISTICS commenda CARRIES, so the pair is comparable cell for cell. It separates on two: "
    "LR6 (symmetric against upside-only) and CF1 (P against 1). It agrees on AP3, LR1, LR2, LR3, LR4, LR5, CF2, CF3 and TS2. "
    "DISSENT, RECORDED NOT RESOLVED: Pryor 1977, Luzzatto 1961, 119 and van Doosselaere 2009, 65 n.7 all hold unilateral and "
    "bilateral commenda to be 'essentially the same agreement', the choice turning on the traveller's wealth. Every one of them "
    "reaches that on the PAYOUT, where the economics are identical by construction (the arithmetic is at 65 n.6). None reaches "
    "it on the loss. The row is kept separate because both of this project's datasets measure the loss. "
    "PERIOD NOTE: loss_mitigation_type.csv gives '10-13c' for the same code. That is probably too early for the Genoese "
    "evidence, which van Doosselaere's corpus opens in 1154, and the two rows should be reconciled at review. "
    "CROSS-DATASET LINK, WHICH cooccurs_with CANNOT EXPRESS: the same code is coded in loss_mitigation_forms "
    "(RB1=RB2=shared). check_vocabularies.py normalises the '@dataset' suffix away and then reads societas_maris@loss_mitigation_forms as a self-reference, so the link is recorded here in prose instead. "
    "STILL WANTED: Lopez & Raymond 174-184, where the contracts are translated - it would supply the quoted clause van "
    "Doosselaere paraphrases. " + TRIAD),
  cooccurs_with="commenda;qirad",
  cooccurrence_basis="same-institution",
),
"mudaraba": dict(
  key_source=(
    "NOT CODED HERE, AND THIS IS A DETERMINATION RATHER THAN AN OMISSION - the same disposition as ortoq_alloc in "
    "loss_mitigation_type.csv. Mudarabah is the HANAFI name for the institution coded in this dataset as 'qirad'. Ramli 2018, "
    "97 on al-Sarakhsi's Kitab al-Mudarabah: al-Sarakhsi treats muqaradah as synonymous with mudarabah, 'the Malikites, "
    "Shafi'ites and Hanbalites unanimously use a different term i.e. qirad to denote such an activity', and 'in general, be it "
    "mudarabah, or muqaradah or qirad, it is by definition a commercial association whereby an investor or capital provider "
    "(rabb al-mal) entrusts some amount of capital to an agent... who trades with it and shares with the investor a "
    "pre-determined proportion of the profits'. Coding both rows would enter one institution twice and manufacture agreement "
    "between them on every cell. "
    "FALSIFICATION CONDITION, so this is not a permanent verdict. The schools are not known to diverge on any of the 32 "
    "characteristics, but one candidate is live and unverified: the vault note [[The mudaraba is revocable not locked in]] "
    "records that classical fiqh predominantly classifies the contract as an 'aqd ja'iz (revocable) while 'Maliki jurists "
    "restrict revocation once the agent has commenced work', flagged there as needing verification against fiqh sources. If "
    "that holds, mudarabah (Hanafi) and qirad (Maliki) separate on TS3 revocability - a WP2 capital-lock-in question, not a "
    "trivial one - and mudaraba earns a row. Note that qirad's own TS3 is currently uncoded, so the test cannot be run from "
    "what is in the matrix; it needs a Maliki source, which the library does not hold. " + TRIAD),
  cooccurs_with="qirad",
  cooccurrence_basis="same-institution",
),
"qirad": dict(
  key_source=(
    "vault: qirad notes. Ramli 2018, 95-98 and 105 (al-Sarakhsi, al-Mabsut 22) for the Hanafi statement of the same "
    "institution. NAME: qirad is the Maliki, Shafi'i and Hanbali term and mudarabah the Hanafi one for one institution (Ramli "
    "2018, 97); the mudaraba type row is deliberately left uncoded on that ground - see its key_source. Loss-allocation aspect "
    "coded separately as qirad_alloc in loss_mitigation_forms, where it is identical to commenda_alloc in every cell. "
    "NOT HELD WITH TEXT and wanted: Udovitch 1970 (Zotero RPV4XSBG is a linked-URL stub)."),
  cooccurs_with="mudaraba;commenda;qirad_alloc@loss_mitigation_forms",
  cooccurrence_basis="same-institution",
),
"commenda": dict(
  key_source=(
    "Harris; vault qirad notes. Extended 2026-08-18: van Doosselaere 2009, 64-68 corroborates AP3, LR1, LR3, LR4, CF1, CF2 and "
    "LR6 on the Genoese corpus, and Harris 2007, 11 describes the arrangement in Hansmann-Kraakman-Squire terms as a separate "
    "asset pool with 'asymmetric owners' shielding and an asymmetric entity shielding'. "
    "TWO THINGS OUTSTANDING ON THIS ROW. (i) AP3=1 and LR1=limited may both be wrong: the traveller 'would bear sole liability "
    "toward third parties' (Harris 2007, 9) and his private assets are reachable by commenda creditors (11), so P is a "
    "candidate for AP3. Not changed in the batch that added the comparison form; see logbook 1, 2026-08-18. (ii) The row is "
    "coded on eleven of 32 characteristics and the entity questions - LP1-LP3, AP1, AP2, AP4, CI1-CI4 - are unasked, though "
    "Harris 2007, 11 and van Doosselaere 2009, 66 would now answer several. "
    "PAIRED WITH societas_maris, added 2026-08-18 and coded on the same eleven cells. This row covers the UNILATERAL form; the "
    "bilateral form is the other row. CF3=bilateral here means TWO PRINCIPALS and is not the literature's 'bilateral commenda' "
    "- see the societas_maris CF3 note."),
  cooccurs_with="societas_maris;qirad;isqa;commenda_alloc@loss_mitigation_forms",
  cooccurrence_basis="same-institution",
),
}


def main():
    p = pathlib.Path("vocabularies/organizational_form_type.csv")
    with p.open(encoding="utf-8") as fh:
        rd = csv.DictReader(fh); header = rd.fieldnames; rows = list(rd)
    codes = {r["code"] for r in rows}
    changed = []
    for r in rows:
        if r["code"] in NEW and r["code"] != "societas_maris":
            for k, v in NEW[r["code"]].items():
                r[k] = " ".join(v.split())
            changed.append(dict(r))
    if "societas_maris" not in codes:
        new = {k: ".NR" for k in header}
        new["code"] = "societas_maris"
        for k, v in NEW["societas_maris"].items():
            new[k] = " ".join(v.split())
        # insert immediately after commenda so the pair reads together
        i = next(k for k, r in enumerate(rows) if r["code"] == "commenda")
        rows.insert(i + 1, new)
        changed.insert(0, new)
    assert len(changed) == 4, [c["code"] for c in changed]
    out = pathlib.Path("proposed-of"); out.mkdir(exist_ok=True)
    q = out / "organizational_form_type-rows.csv"
    with q.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=header, lineterminator="\n")
        w.writeheader(); w.writerows(changed)
    print("wrote", len(changed), "type rows ->", q)
    if "--apply" in sys.argv:
        with p.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=header, lineterminator="\n")
            w.writeheader(); w.writerows(rows)
        print("rewrote", p)


if __name__ == "__main__":
    main()
