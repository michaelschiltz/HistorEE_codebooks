#!/usr/bin/env python3
"""Build the proposed data.csv rows for the four allocation anchors.

Emits proposed/loss_mitigation_forms-rows.csv (header + 37 rows) and, with
--apply, appends them to the working copy of the dataset so the checks can run.
"""
import csv, sys, pathlib

HEADER = ["record_id","type_id","char_id","value","confidence","articulation",
          "source_ref","source_lang","coder","source_read","reviewed_by",
          "review_status","notes"]

HELD  = "Held 2025, 11-13 and 20-22 (Statute of Dubrovnik 1272, lib. VII, 50-51 and lib. III, 46; MHR I-IV, 53 contracts 1278-1301)"
HARR7 = "Harris 2007, 9-13"
RAMLI = "Ramli 2018, 95 and 97-98 (al-Sarakhsi, al-Mabsut 22:18)"
AL11  = "Ackerman-Lieberman 2011, 662-664"
GDL   = "Gonzalez de Lara 2002, 259"
VD    = "van Doosselaere 2009, 64-68 (Genoese notarial cartularies; 6,764 commenda ties 1154-1315)"

# (type_id, char_id, value, confidence, articulation, source_ref, source_lang, source_read, notes)
R = []

# ---------------------------------------------------------------- commenda_alloc
R += [
("commenda_alloc","MC1","allocation","high",".NR",HARR7+"; "+HELD,"en","partial",
 "Risk assigned to named parties by contract, not mutualised across a membership and not sold to an outsider for a premium. "
 "Coded allocation on Harris's own trichotomy, but see the logbook 4 entry: this batch takes MC1=allocation from four forms to eight. "
 "Before it the value held sea_loan, bottomry, respondentia and avariz_vakfi_kirkcesme, and of the three with RB1/RB2 coded all three "
 "were loans reading capital-provider/labour-provider. All four forms added here read the two TOGETHER - capital-provider/"
 "capital-provider or shared/shared - so allocation now contains the whole range of the RB1/RB2 contrast and cannot express it. "
 "The contrast does not respect MC1 in either direction: bodemerij_amsterdam is MC1=spreading and particular_average MC1=.NR, and "
 "both read capital-provider/capital-provider. MC1 and RB1/RB2 are independent across the coded set. "
 "NOT articulated: the three-way mechanism vocabulary is Harris 2023's, not the tradition's - what the tradition articulates is the "
 "bearer (RB1), not the mechanism type."),

("commenda_alloc","MB3","voluntary","high",".NR",HELD,"en","full",
 "A contract, not a levy. Held 2025, 17-18: commendators include noblewomen, tutors investing a ward's money and testamentary "
 "executors, which he reads as evidence the form 'was not seen as particularly risky on the capital market'. Same value as sea_loan."),

("commenda_alloc","RB1","capital-provider","high","articulated",HELD+"; "+HARR7,"en","full",
 "THE DEFINING CELL, AND IT IS IN THE INSTRUMENT'S OWN WORDS. The Ragusan maritime acts carry the clause "
 "'dicti solidi sunt ad periculum dicti [commendator] maris et gentis clarefactum' (Held 2025, 20), a formula Held reports as "
 "'common in Venetian documents of the time', denoting perils of the sea generally (shipwreck, storm) and piracy or seizure by "
 "foreign rulers - and the Genoese SEA LOAN carries the cognate formula 'risicum et fortunam dei maris et gentium' (van "
 "Doosselaere 2009, 130), so what varies between the two instrument families is not the clause but whose name stands in it. "
 "Held's count for the maritime category: commendator 11, tractator 0, unspecified 1, divided 1. Statute of "
 "Dubrovnik VII,50 states the same as the default. Harris 2007, 9 gives the doctrinal form: on 'travel-related loss' the traveling "
 "party 'did not have to return that part of the capital that was lost'. "
 "GENOESE CORROBORATION ON THE LARGEST CORPUS THERE IS: van Doosselaere 2009, 65, on 6,764 commenda ties from the notarial "
 "cartularies 1154-1315 (93 per cent of all coded maritime ties) - 'In a unilateral commenda, the investor collected three-fourths "
 "of the net proceeds and bore ALL LIABILITY FOR LOSS, while the traveler received only one-fourth of the net and BORE NO CAPITAL "
 "RISK.' "
 "MANDATE CONDITION, NOT A HEDGE: Statute VII,50 shifts totum periculum onto the tractator if he leaves the Adriatic without "
 "permission, and the Genoese acts carry the same device as a standard term - the traveller 'swore to abide by certain "
 "instructions concerning the use of the money, such as RESTRICTIONS ON DESTINATIONS OR GOODS TRANSACTED' (van Doosselaere 2009, "
 "65). That is a condition on the scope of the mandate, not a partial state - the same structure the sea-loan family carries as "
 "the deviation rule - and it is coded here in the note rather than as P. See the qirad_alloc RB1 note for the two Islamic "
 "parallels; the device is now attested in four independent corpora, and in Genoa and in the hadith of al-'Abbas it restricts the "
 "same two things, destinations and goods."),

("commenda_alloc","RB2","capital-provider","high","analyst-imposed",HARR7+"; "+HELD,"en","partial",
 "THE CELL THAT SEPARATES THE PARTNERSHIP FAMILY FROM THE LOAN FAMILY. Harris 2007, 9: 'In the occurrence of travel-related loss "
 "OR TRADE-RELATED LOSS, the traveling party did not have to return that part of the capital that was lost, even when it was the "
 "entire sum invested... The investing party was a residual claimant.' Contrast sea_loan RB2=labour-provider: there the borrower "
 "keeps the market risk and only the peril moves. Held's Statute VII,51 says the same without distinguishing the two perils - if "
 "part of the capital is lost the commendator may take what remains and the tractator need not make up the difference. "
 "ANALYST-IMPOSED AND THE REASON IS ITSELF A FINDING: the notarial clause names the PERIL bearer only (periculum maris et gentis). "
 "The market-loss bearer is recovered by inference from the absence of any repayment obligation. RB1 and RB2 are separately "
 "articulated only in the forms where they DIVERGE - Harris 2023 states both in one sentence for the sea loan precisely because "
 "they part company there. Where they coincide the tradition draws only one clause."),

("commenda_alloc","RB3","none","high",".NR",HARR7,"en","partial",
 "No pledge and nothing to pledge: the advance is equity, not debt (Harris 2007, 9 - 'the investment was in the form of equity, "
 "not of debt'). Same value as sea_loan (generic), marine_insurance and particular_average, for three different reasons; RB3=none "
 "is doing no discriminating work in this batch."),

("commenda_alloc","RB4","1","high","articulated",HELD,"en","full",
 "Statute of Dubrovnik VII,51: if part of the capital is lost the commendator may choose to accept what remains, 'and then the "
 "tractator will not have to reimburse the amount that was lost'. Statute III,46 (aptagi) puts the limit from the other side - the "
 "tractator answers only for losses 'malo modo et in sua culpa' and not for those 'iudicio Dei et non in sua culpa'. "
 "Salvage accrues to the commendator, which matches Gonzalez de Lara 2002, 259 on Venice: merchants 'were exempted from repayment "
 "beyond the amount saved from loss at sea', i.e. discharge is of the shortfall, not of an obligation that never existed."),

("commenda_alloc","PR1","0","high",".NR",HARR7+"; "+HELD,"en","partial",
 "No peril is priced ex ante, and this is a substantive 0 rather than an unrecorded absence: the return is a share of realised "
 "profit, contingent on outcome, and nothing is paid if there is no profit (Harris 2007, 9-11). "
 "REJECTED READING, RECORDED: the profit ratio (3/4-1/4, 1/2-1/2) could be read as an embedded premium. It is not coded that way, "
 "for three reasons. PR1's own coding rule bars a premium recovered by inference. Held 2025, 19-20 has the Ragusan ratios moving "
 "with the capital market rather than with the peril - most contracts depart from the statutory 2/3 in the commendator's "
 "disfavour, which he reads as 'an overabundance of capital'. And the Genoese corpus points the same way from the opposite "
 "direction: van Doosselaere 2009, 66-67 finds the terms 'virtually independent of either the business characteristics at hand or "
 "the social circumstances of the partners', with only a handful of departures from the customary split in 4,860 ties across "
 "dozens of destinations, 1154-1265. A ratio that tracks the supply of capital is not a peril price; neither is one that tracks "
 "nothing at all. THE TWO CORPORA DISAGREE ABOUT WHETHER THE RATIO MOVES, and PR1=0 survives either answer. "
 "RESULT: MC1=allocation now spans PR1 = 0 (all four forms in this batch), P (sea_loan) and 1 (bottomry, respondentia). The "
 "2026-08-07 tontine split established that pricing is orthogonal to mechanism inside MC1=pooling; this batch reproduces that "
 "inside MC1=allocation, from a different literature."),

("commenda_alloc","PY0",".NA",".NA",".NA",".NA",".NA",".NA",
 "Inapplicable: a bilateral contract, not a fund with an output. Propagates as for sea_loan; PY1-PY3 are not entered."),

("commenda_alloc","VF1","documentary","high","articulated",HELD+"; "+GDL,"en","full",
 "The clause is the verification rule. 'Clarefactum' in the periculum formula 'refers to the need that the occurrence of such "
 "extraordinary events which led to a loss of commendator's capital had to be sufficiently clarified' (Held 2025, 21). Gonzalez de "
 "Lara 2002, 259 has the same condition in Venice - exemption from repayment applied 'if this was clearly apparent' - and makes the "
 "state's capacity to generate verifiable information (delegates in the colonies, scribes en route, public mediators in Venice) the "
 "cause of the transition from the sea loan to the commenda. Statute of Dubrovnik VII,28 requires the ship's scribe to register "
 "every profit separately. Coded documentary rather than official-adjudication because what the sources describe is a standard of "
 "proof written into the instrument and a record generated en route, not a forum. "
 "SECOND VF1 IN THE MC1=allocation FAMILY AND THE FIRST WITH A CONTEMPORANEOUS CLAUSE BEHIND IT: avariz_vakfi_kirkcesme is "
 "official-adjudication, sea_loan, bottomry and respondentia carry no VF1 row at all, and bodemerij_amsterdam is .NR."),

("commenda_alloc","VF2","mixed","high","articulated",HELD,"en","full",
 "Three distinct objects are established, which is what 'mixed' is for. (i) loss-occurrence: that the periculum maris et gentis "
 "actually happened - the clarefactum standard. (ii) claimant-fault: Statute III,46 divides losses 'malo modo et in sua culpa' from "
 "those 'iudicio Dei et non in sua culpa', and Held 2025, 21 n.54 cites a 1253 proceeding determining the travelling merchant's "
 "culpability for a seizure by pirates. (iii) conduct-compliance: Statute VII,50 shifts totum periculum if he left the Adriatic "
 "unpermitted, so observance of the mandate must be established before the discharge operates."),
]

# ---------------------------------------------------------------- qirad_alloc
CROSSREF = ("READ WITH commenda_alloc: on the loss-allocation characteristics these two rows are identical in every coded cell. "
            "That agreement is a finding, not two observations - see logbook 2, 2026-08-18, and the boundary_basis="
            "contemporary-terminology entered on both type rows. Do not count them as two cases in any comparative claim.")

R += [
("qirad_alloc","MC1","allocation","high",".NR",RAMLI+"; "+HARR7,"en","partial",
 "Risk assigned to a named party by contract. " + CROSSREF),

("qirad_alloc","MB3","voluntary","high",".NR",RAMLI,"en","partial",
 "A contract between a rabb al-mal and a mudarib, entered freely. " + CROSSREF),

("qirad_alloc","RB1","capital-provider","high","articulated",RAMLI+"; "+AL11,"en","partial",
 "Ramli 2018, 95 on al-Sarakhsi's Kitab al-Mudarabah: 'Losses incurred in the venture are the responsibility of the investor. "
 "Meanwhile, the agent loses his time and efforts for which he will neither be given any remuneration nor would he be penalised "
 "monetarily.' Articulated: this is the fiqh's own statement, not a modern gloss. "
 "THE PERIL IS NAMED SEPARATELY, WHICH IS WHY RB1 IS ARTICULATED AND RB2 IS NOT. The hadith of al-'Abbas b. 'Abd al-Muttalib, "
 "which al-Sarakhsi cites as the sunnaic warrant (Ramli 2018, 97-98), has capital given on condition the mudarib 'go neither on sea, "
 "nor down the oasis, nor buy a live animal (kabid ratb)' - three perils, named - and 'if the mudarib did so, he had to guarantee "
 "the capital due to the risks involved'. Al-Nuwayri's fourteenth-century formulary carries the same restriction as a drafting "
 "clause: the agent 'shall travel with the goods wherever he wishes in Islamic lands ON SAFE ROUTES' (Ackerman-Lieberman 2011, 664, "
 "who reads it as a control on the agent's incentive to choose a suboptimally risky asset). "
 "SAME DEVICE IN THREE TRADITIONS: cf. commenda_alloc RB1 and the Statute of Dubrovnik VII,50 (totum periculum on the tractator if "
 "he leaves the Adriatic unpermitted). Coded capital-provider, with the mandate condition in the note, not as P. " + CROSSREF),

("qirad_alloc","RB2","capital-provider","high","analyst-imposed",RAMLI+"; "+HARR7,"en","partial",
 "Ramli 2018, 95 says 'losses' without qualification and the agent is 'not penalised monetarily', so market loss falls on the "
 "rabb al-mal with the peril. Harris 2007, 9 states it for the same institution under its Latin name. "
 "ANALYST-IMPOSED: the peril/market distinction is the analyst's here. The fiqh names the perils (see RB1) but nowhere separates "
 "loss to price movement from loss to the voyage; the undifferentiated 'losses' is what the source gives. "
 "THIS IS THE CELL BEHIND THE VAULT CLAIM THAT THE QIRAD ENVELOPS THE SEA LOAN: sea_loan splits RB1=capital-provider from "
 "RB2=labour-provider, and the qirad refuses the split, absorbing the peril tail inside a general loss-sharing. " + CROSSREF),

("qirad_alloc","RB3","none","high",".NR",RAMLI,"en","partial",
 "The mudarib holds the capital as amana (trust) and gives no security; Ramli 2018, 105 - 'When the ra's al-mal is submitted to a "
 "mudarib, he is deemed as a trustee, just like a depositor (al-muwaddi')'. Liability (daman) attaches only on breach, at which "
 "point he is guarantor of the whole, which is a liability rule and not a pledge. " + CROSSREF),

("qirad_alloc","RB4","1","high","articulated",RAMLI,"en","partial",
 "The obligation is extinguished on loss: the agent 'loses his time and efforts... nor would he be penalised monetarily' "
 "(Ramli 2018, 95). Daman attaches only where he exceeded the mandate. " + CROSSREF),

("qirad_alloc","PR1","0","high",".NR",RAMLI+"; "+AL11,"en","partial",
 "No ex-ante price for bearing the peril: the return is 'a pre-determined proportion of the profits' (Ramli 2018, 95), a ratio "
 "applied to a realised outcome. The doctrinal reason is stronger here than for commenda_alloc - a stipulated return would be the "
 "leasing (ujr / ijarah fasidah) that al-Sarakhsi and al-Kasani say the contract would be under qiyas, and is what the istihsan "
 "warrant exists to avoid (Ramli 2018, 99). "
 "A DIFFERENCE FROM commenda_alloc THAT NO CELL IN THIS DATASET HOLDS, RECORDED HERE BECAUSE IT QUALIFIES THE "
 "boundary_basis=contemporary-terminology ON BOTH TYPE ROWS. The two forms differ in HOW the payout ratio is formed, though not "
 "in whether the peril is priced. van Doosselaere 2009, 68, reading Udovitch 1970, 190-6: in the qirad 'any proportional division "
 "of net proceeds agreed to by the partners was deemed acceptable', the manuscripts contemplating splits 'from half-and-half to "
 "1/20-19/20', so 'the cost of capital among eastern Mediterranean long-distance participants was a function of market conditions "
 "and, of course, of one's position in the traders' network'. The Genoese ratio was customary and invariant until the late "
 "thirteenth century. That is a real structural contrast - negotiated against customary - and it is not a peril price, so PR1 "
 "cannot carry it and nothing else here can either. See logbook 4, 2026-08-18 (vi). " + CROSSREF),

("qirad_alloc","PY0",".NA",".NA",".NA",".NA",".NA",".NA",
 "Inapplicable: a bilateral contract, not a fund with an output."),

("qirad_alloc","VF1",".NR",".NR",".NR",RAMLI+"; "+AL11,"en","partial",
 "NOT RECORDED, AND EMPHATICALLY NOT 'none'. The sources read establish that a verification question exists and is justiciable - "
 "daman attaches when the mudarib 'goes against the decision' (Ramli 2018, 105), and al-Nuwayri's safe-routes clause presupposes "
 "that route compliance can be established - but neither describes HOW a claimed loss is proved, by whose oath or before which "
 "forum. Held at .NR rather than coded official-adjudication by analogy. "
 "THE ASYMMETRY WITH commenda_alloc VF1=documentary IS A FACT ABOUT WHAT IS HELD IN THE LIBRARY, NOT ABOUT THE FORMS. Udovitch 1970, "
 "the monograph for this row, is a metadata-only stub with no PDF; Khalilieh 2020's saved attachment is a paywall landing page. "
 "A reader must not take the difference between this cell and commenda_alloc VF1 as a differentia. See logbook 5, 2026-08-18."),
]

# ---------------------------------------------------------------- isqa_alloc
R += [
("isqa_alloc","MC1","allocation","medium",".NR",AL11,"en","partial",
 "Coded allocation, with a reservation about the value's wording. MC1's definition has allocation 'assign[ing] the risk to A NAMED "
 "PARTY by contract' - singular. The 'isqa divides it between two named parties by contract, in stated fractions. It is plainly not "
 "spreading (no third party, no premium) and plainly not pooling (organizational_forms isqa LR4=0: bilateral risk-sharing, not "
 "mutualisation across a membership), so allocation is the only available value; but the singular in the definition strains, and "
 "societas_maris strains it in the same way. Recorded rather than resolved - two forms is not a case for touching MC1. "
 "Falsification condition: a third allocation form that divides rather than assigns, at which point the question is whether MC1 "
 "needs a companion recording whether the risk is assigned entire or apportioned."),

("isqa_alloc","MB3","voluntary","high",".NR",AL11,"en","partial",
 "A contract recorded in a shetar before the beit din, not a levy."),

("isqa_alloc","RB1","shared","medium","analyst-imposed",AL11,"en","partial",
 "The manager's peril exposure is at least a half and may be the whole, and the sources read do not settle which. Two mechanisms "
 "run together. (i) On the milveh half the capital is his and he owes it back as a debt, so peril loss on that half is his outright. "
 "(ii) On the pikkadon half he is a PAID bailee, not an unpaid one, because Maimonides requires the investor to pay him a wage or "
 "an extra share for his work; Ackerman-Lieberman 2011, 662 draws the consequence - 'unlike the ordinary agent, who, like any other "
 "unpaid bailee, is not held liable when an item is lost or stolen, the active partner in an 'isqa would actually be held liable in "
 "such circumstances'. "
 "MEDIUM AND ANALYST-IMPOSED, DELIBERATELY: the source addresses loss and theft, not maritime peril, and does not say whether the "
 "Talmudic ones exemption (unavoidable accident - shipwreck, brigandage) relieves the paid bailee here. Coded shared as the value "
 "the evidence supports; labour-provider would assert more than the source does. Resolving this needs Gamoran 2008 or "
 "Ackerman-Lieberman 2014, neither of which is held with a PDF. "
 "INDEPENDENT CORROBORATION FROM OUTSIDE THE JEWISH-LAW LITERATURE: van Doosselaere 2009, 68, comparing the Genoese commenda with "
 "its eastern analogues - 'both the chreokoinonia and the ISQUA agreements suggest the idea of debt, or at least equal and joint "
 "liability, which severely restricted the pairing of participants with substantial differences in wealth... whereas in the "
 "western Mediterranean, any traveler could take a large amount invested by a wealthy investor on a sea venture because HIS LOSS "
 "WAS LIMITED TO THE VALUE OF HIS LABOR.' A Genoese economic sociologist, reading Pryor and Udovitch rather than the Talmud, "
 "arrives at the same allocation."),

("isqa_alloc","RB2","shared","high","articulated",AL11,"en","partial",
 "THE DISCRIMINATING CELL AGAINST commenda_alloc AND qirad_alloc, AND THE ONLY FORM IN THIS BATCH WHERE THE MARKET SIDE IS THE "
 "ARTICULATED ONE. Ackerman-Lieberman 2011, 663: 'because the structure of the Talmudic 'isqa allocates the active partner half of "
 "the invested capital as a loan, Maimonides holds the active partner responsible for HALF OF ALL TRADING LOSSES to the partnership "
 "capital. The corresponding relationship described by Islamic law - the investment partnership known as the commenda (qirad or "
 "mudaraba in Arabic) - holds the active partner indemnified from all partnership losses.' The two forms are set against each other "
 "on this exact question by the source itself. "
 "WHY THE ARTICULATION FLIPS: the Latin and Islamic sources name the peril (a voyage clause) and leave the market side to be "
 "inferred; the rabbinic source names the trading loss and leaves the peril to bailment law. The doctrinal pressure is different - "
 "ribbit forces the discussion onto the return on capital, the periculum clause and the hadith are about the voyage. "
 "DOCUMENTARY COUNTER-EVIDENCE THAT CUTS THE OTHER WAY, RECORDED HERE BECAUSE IT BEARS ON qirad_alloc RATHER THAN ON THIS ROW: at "
 "664 Ackerman-Lieberman reports that 'legal documents from the Geniza concerning investment partnerships allocate both partners a "
 "share of both profits and losses, with very few documents indemnifying the active partner against losses'. On his reading those "
 "documents are 'isqa-shaped, which is his thesis; on Udovitch's and Goitein's they are qirad in practice, in which case "
 "qirad_alloc RB2=capital-provider is a doctrinal coding that the instruments contradict. The dispute is left open as a coding "
 "rather than resolved - see the type-row key_source and logbook 5."),

("isqa_alloc","RB3","none","medium",".NR",AL11,"en","partial",
 "No pledge is described. The manager's exposure on the milveh half runs against his estate, but that is a liability rule and is "
 "already carried in organizational_forms as isqa AP3=0 and LR1=unlimited-several; entering it here as RB3=general-estate would "
 "restate it and manufacture agreement between two datasets on one piece of evidence. Coded none rather than .NR because the "
 "sources describe the 'isqa as an unsecured bifurcation of ownership, not as a secured advance; medium because none of them "
 "discusses security clauses in shetarot 'isqa."),

("isqa_alloc","RB4","0","high","articulated",AL11+"; BT Bava Metzia 104b (via the maintainer's vault note [[isqa]])","en","partial",
 "THE FIRST NON-1 VALUE RB4 HAS TAKEN IN THIS CENSUS. The obligation is NOT extinguished by loss of the venture: Rav Idi bar Avin's "
 "pelga milveh u-pelga pikkadon makes half the advance a debt the manager owns and owes, so on total loss that half survives against "
 "him, and on the deposit half his paid-bailee status makes him answerable for loss and theft (Ackerman-Lieberman 2011, 662). "
 "CONSEQUENCE FOR THE CHARACTERISTIC, WHICH IS THE POINT OF CODING IT. Before this batch RB4 read 1 for sea_loan, bottomry, "
 "respondentia and bodemerij_amsterdam and .NA for marine_insurance and particular_average - one observed value across four forms, "
 "which the sea_loan LS3 note (LM-0526) cited as making 'its retirement case correspondingly stronger'. RB4 now separates on "
 "substantive values, 1/1/0/1 across commenda_alloc, qirad_alloc, isqa_alloc and societas_maris. The retirement case is withdrawn. "
 "This is the CHARACTER-CODING test-4 pattern again: one form settled what no amount of reasoning could, and it did so by being "
 "added rather than by being argued about. "
 "CORROBORATED FROM A SECOND LITERATURE: van Doosselaere 2009, 68 has the isqua manager unable to 'withstand the financial risk "
 "of an association with a wealthier partner', which is the same non-discharge stated as a selection constraint. That is also, "
 "unprompted, the falsifiable prediction the vault note [[The isqa refuses the agent's shield]] made - that the 'isqa should "
 "select for managers who already hold a wealth buffer."),

("isqa_alloc","PR1","0","high",".NR",AL11,"en","partial",
 "No peril priced ex ante. There IS an ex-ante stipulated payment - Maimonides requires the investor to pay the manager 'either a "
 "portion of profits or a daily wage' (sekharo ke-po'el batel), Ackerman-Lieberman 2011, 662 - but it runs the wrong way (investor "
 "to manager) and prices LABOUR, not the peril. Its purpose is doctrinal: 'to parry the claim that profits paid to the investor "
 "from the half of capital allocated as a deposit were unjust enrichment or interest'. Pricing the peril is precisely what ribbit "
 "forbids, so PR1=0 is here an observed absence with a stated cause."),

("isqa_alloc","PY0",".NA",".NA",".NA",".NA",".NA",".NA",
 "Inapplicable: a bilateral contract, not a fund with an output."),

("isqa_alloc","VF1",".NR",".NR",".NR",AL11,"en","partial",
 "Not recorded, not 'none'. Ackerman-Lieberman's corpus is court and notarial material - releases, partnership-dissolution "
 "documents, powers of attorney - so verification manifestly occurred before the beit din, but he is arguing about contract "
 "STRUCTURE and never describes how a claimed loss was proved. Coding communal-attestation or official-adjudication from the "
 "existence of the forum would be inference, not evidence."),
]

# ---------------------------------------------------------------- societas_maris
THIN = ("BOUNDARY CAVEAT ON THIS WHOLE ROW: Pryor 1977, Luzzatto 1961 and van Doosselaere 2009, 65 n.7 all hold that unilateral "
        "and bilateral commenda are 'essentially the same agreement', the choice between them turning on the traveller's wealth "
        "rather than on the contract. That verdict is reached on the PAYOUT, where the economics are identical by construction "
        "(van Doosselaere's arithmetic at 65 n.6: the bilateral traveller's half is his 1/4 labour share on the investor's two "
        "thirds, 1/6, plus the whole return on his own third). It is not reached on the LOSS, where they are not identical. This "
        "census measures the loss, so the rows are kept apart - but a reader who wants them merged has three authorities and this "
        "note is where to start. See logbook 4, 2026-08-18 (v).")

R += [
("societas_maris","MC1","allocation","high",".NR",VD+"; "+HARR7,"en","partial",
 "Risk divided between two named parties by contract, in proportion to their contributions. Same reservation about the "
 "definition's singular 'a named party' as isqa_alloc MC1 - see that note. " + THIN),

("societas_maris","MB3","voluntary","high",".NR",VD,"en","partial",
 "A contract, not a levy; van Doosselaere 2009, 66 calls the commenda family 'a real joint venture' whose partners are named "
 "socii in the statutes of Genoa, Pera, Marseilles and Pisa. " + THIN),

("societas_maris","RB1","shared","high","articulated",VD+"; "+HELD+"; "+HARR7,"en","partial",
 "THE CELL THAT SEPARATES THIS ROW FROM commenda_alloc, AND IT IS NOW SOURCED ON THE GENOESE CORPUS. van Doosselaere 2009, 65 sets "
 "the two side by side as invariable terms of the standard contract: 'In a unilateral commenda, the investor collected "
 "three-fourths of the net proceeds AND BORE ALL LIABILITY FOR LOSS, while the traveler received only one-fourth of the net and "
 "bore no capital risk. In a bilateral commenda, often called SOCIETAS IN GENOA... In a bilateral venture, THE LIABILITY FOR LOSS "
 "WAS PROPORTIONAL TO THE RESPECTIVE INITIAL INVESTMENTS OF THE PARTICIPANTS.' The traveller's contribution is itself fixed by "
 "custom - 'always to the ratio one-third traveler, two-thirds investor' (65) - so the shares are 1/3 and 2/3. "
 "ARTICULATED: van Doosselaere presents the allocation as a term the contract 'invariably included' across a corpus of 6,764 ties, "
 "not as a modern reconstruction. He does not quote a clause, so this rests on his characterisation of the standard form rather "
 "than on a transcribed act; the cognate unilateral clause IS quoted, by Held 2025, 20. "
 "SECOND CORPUS, INDEPENDENT: Held 2025, 22 reports Ragusan contracts that 'explicitly state that the parties share both profits "
 "and losses (lucrum and damnum) in the same shares', which he reads as 'essentially more societas than commenda' and Margetic as "
 "'essentially bilateral commenda contracts'. " + THIN),

("societas_maris","RB2","shared","high","analyst-imposed",VD+"; "+HELD,"en","partial",
 "Follows RB1 on the same evidence. ANALYST-IMPOSED for the same reason as every other row in this batch: van Doosselaere's "
 "'liability for loss' and Held's 'lucrum and damnum' are both undifferentiated as between the peril and the market, so the "
 "peril/market split is the analyst's. Confidence high because the proportional rule itself is firmly attested; what is inferred "
 "is only that it covers both kinds of loss, which follows from there being no repayment obligation to carve out. " + THIN),

("societas_maris","RB3","none","high",".NR",VD,"en","partial",
 "No pledge; each party's contribution is equity in the venture. van Doosselaere 2009, 66 draws the contrast with the credit "
 "instruments explicitly - a credit outcome 'was simply a function of the solvency of the creditor', the commenda outcome "
 "'depended solely on the success of the business enterprise'. " + THIN),

("societas_maris","RB4","1","high","analyst-imposed",VD,"en","partial",
 "As to the investor's two thirds the traveller owes no repayment on loss: the loss is borne, not repaid, and the profit split "
 "follows 'restitution of the capital originally invested' only where there is capital to restitute (van Doosselaere 2009, 65). "
 "What the traveller loses on his own third is RB1's question, not this one - the distinction matters, because collapsing it "
 "would make RB4 read P and destroy the 1/1/0/1 contrast that isqa_alloc has just given the characteristic. " + THIN),

("societas_maris","PR1","0","high",".NR",VD,"en","partial",
 "No ex-ante price for the peril, and the Genoese evidence makes this the strongest PR1=0 in the census. van Doosselaere 2009, "
 "66-67: commenda financial terms 'did not vary according to market conditions until the end of the thirteenth century'; in a "
 "sample of 4,860 ties, 1154-1265, spanning dozens of destinations and sizes from under one Genoese pound to several thousand, "
 "'only a handful of contracts provided a payout different from the customary one-fourth/three-fourths payout for the unilateral "
 "commenda and the half-and-half-payout for the bilateral commenda'. A ratio invariant across destination - and therefore across "
 "peril - cannot be a price for the peril. See the qirad_alloc PR1 note for the eastern contrast. " + THIN),

("societas_maris","PY0",".NA",".NA",".NA",".NA",".NA",".NA",
 "Inapplicable: a bilateral contract, not a fund with an output."),

("societas_maris","VF1",".NR",".NR",".NR",HELD+"; "+VD,"en","partial",
 "Not recorded. The clarefactum standard coded at commenda_alloc VF1 belongs to contracts Held classifies as UNILATERAL; he does "
 "not report the risk clause of the handful of societas-shaped acts, and van Doosselaere does not discuss proof of loss at all. "
 "Inferring it from the neighbouring form would import the very identity this row exists to test. " + THIN),
]

def main():
    start = 527
    rows = []
    for i, (t, c, v, conf, art, sref, slang, sread, note) in enumerate(R):
        rows.append({
            "record_id": "LM-%04d" % (start + i),
            "type_id": t, "char_id": c, "value": v,
            "confidence": conf, "articulation": art,
            "source_ref": sref, "source_lang": slang,
            "coder": "ai", "source_read": sread,
            "reviewed_by": "none", "review_status": "unreviewed",
            "notes": " ".join(note.split()),
        })
    out = pathlib.Path("proposed"); out.mkdir(exist_ok=True)
    p = out / "loss_mitigation_forms-rows.csv"
    with p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER, lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    print("wrote %d rows -> %s (%s..%s)" % (len(rows), p, rows[0]["record_id"], rows[-1]["record_id"]))

    if "--apply" in sys.argv:
        d = pathlib.Path("datasets/loss_mitigation_forms/data.csv")
        with d.open("a", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=HEADER, lineterminator="\n")
            w.writerows(rows)
        print("appended to", d)

if __name__ == "__main__":
    main()
