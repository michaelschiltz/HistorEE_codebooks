## 2026-08-17 — ai (what the Amsterdam acts say that the matrix cannot hold)

Five things came out of the bodemerij corpus that bear on the instrument rather than on the
form. **None of them is a proposal to add a characteristic.** Four are recorded here
because the matrix cannot hold them; the fifth is a well-formedness problem in an existing
pair, offered for the maintainer's decision and not repaired.

### (i) `RB1` and `RB2` use one role label for two different people

`RB1` is coded `capital-provider` and means the **lender**: he advances the money and loses
it if the ship is lost. `RB2` is coded `capital-provider` and means the **borrower**: the
opgeld is a fixed figure that does not move with the price the cargo fetches, so the market
loss stays with the owner of the goods.

Both codings are right and together they are unreadable. The two characteristics were
written for the commenda-shaped case, where one party brings capital and the other brings
labour, and in that case `capital-provider` picks out one person. **A secured loan has two
capital providers**, and the label silently switches referent between the two cells.

This is Sereno's incomplete character statement: the **locator** is missing. `RB1` and
`RB2` name a variable (which loss) and a state (who bears it) but never say *of what* the
role is predicated — of the venture, or of the advance. It is not the `LR2`/`LR6` case,
because the characteristic is not asking two questions; it is asking one question with an
underspecified subject.

**The repair, if one is wanted, is a locator in the definition, not a new characteristic.**
Something of the form "roles are predicated of the *venture*, so the party advancing money
against a pledge is `third-party` where he has no stake in the outcome beyond his advance"
would settle it — and would incidentally force a re-reading of this row's `RB1`, since on
that locator most of these lenders are outsiders and the value would become `third-party`,
collapsing the distinction from `marine_insurance` that `RB1` currently carries. **That is
exactly why the decision is the maintainer's and not mine.** Recorded, not acted on.

### (ii) The premium is paid only if the venture succeeds, and no `CN1` value says so

`CN1` asks when contributions fall due and offers `ex-ante-periodic`, `ex-ante-lump` and
`ex-post-assessment`, the last glossed in the vocabulary as the general-average pattern —
contribute *after the loss*.

Bodemerij inverts it. The opgeld is fixed before departure and falls due 8 to 16 days
**after safe arrival**, and it is not payable at all if the venture is lost, because
principal and opgeld are forfeited together. A premium contingent on success is neither
ex ante in its timing nor ex post on a loss.

**No row was written for `CN1`.** Forcing `ex-post-assessment` would have told a downstream
consumer reading the definition that this behaves like general average, which is the
opposite of the truth. This is the difference between marine insurance and bodemerij that
the matrix currently cannot see: the underwriter takes his premium whatever happens, the
bodemerij lender takes his only out of a venture that came home. Winkelman's Verwer
quotation is the contemporary awareness of it — the lender charges roughly double the
insurance premium, and Verwer's first reason is that he must reinsure.

### (iii) On deviation the risk stops but the whole opgeld is still owed — and the acts disagree about it

The protests supply what the contracts do not, exactly as expected of dispute records.
**Deviation, not shipwreck, is the whole subject of this litigation.** In no. 955 the master
sailed on from Danzig to Riga and the lender declares "dat hij geen voirder resicque oft
pericule begeert te loopen; alsoe naer recht ende coustume sijne penningen verschenen
sijn" — the risk-bearing terminates, the principal accelerates, and the ground given is
custom. No. 957 is the same shape with the rate named, 16 per cent, and the same phrase:
"gemerct hij door 't veranderen van de voorsz. reyse niet gehouden is eenige voirdere
risicque te loopen." No. 959 likewise.

No. 1995 writes the rule into the contract, and writes it hard: on deviation "sal de voorsz.
hooftsomme mettet opgelt van dien datelijck verscheenen weesen, zonder dat alsdan den
voorn. Hendrick Voet eenich vorder resicque zal loopen", the borrower bound to pay "de
voorsz. somme **mette volle bodemerije in 't geheel**". The full risk price, for a risk the
lender has stopped running.

**But three later acts write the opposite rule.** In no. 3227 if the master sails outside
the contract "sullen evenwel die voorsz. penningen op 't aventuyr van der zee als boven
blijven loopende", with the opgeld adjusted afterwards "tot seggen ende discretie van goede
luyden hen dies verstaende". Nos 3237 and 3241 do the same, no. 3241 promising the lender
"verbeteringe van opgelt" for the extra exposure. No. 2001 goes further and makes the
instrument renew itself: on the named deviation the first 17 per cent falls due when the
ship passes home waters, "**ende sullen alsdan de hooftpenningen opnieuw weder op
bodemerije loopen**" at a fresh 17 per cent for the next leg.

**Three regimes for one contingency, in one city, inside twenty years, all called
bodemerij.** This is the sharpest single result of the coding and there is no cell for it:
the matrix has no characteristic for what happens when the *conditioning event* of a
contingent obligation is altered by the obligor. It is not `RB4`, which asks only about
total loss. Recorded here rather than made into a feature — and it is a better argument for
Frankot's pluralism operating *within* a jurisdiction than anything the compilations show
between jurisdictions.

### (iv) Ship-pledged and goods-pledged bodemerij are one instrument in Amsterdam practice

`check_boundary`'s own docstring names `bottomry` and `respondentia` as the motivating case
and says the boundary between them waits on **notarial evidence**. This is notarial
evidence, and it does not support a contemporary distinction.

In this corpus the two are drafted by the same two notaries, entered in the same registers,
often within days of each other, under the same heading, with the same clause architecture
— consideration, "op 't recht aventuyr van der zee", the voyage description closing on "wel
heynder maer niet verder te seylen", the repayment interval, the opgeld, the *verbindende*
clause. **The only thing that changes is the noun in the pledge clause.** Nos 3232 and 3234
pledge salt and its returns; nos 3227 and 3230 pledge the keel; no. 956 pledges ship and
freight together; nos 3236 and 3237 pledge the freight first and the ship second. Nos 3232
and 3233 are the same borrower, the same lender and the same day, and no. 3233 is recorded
simply as "in aller vougen ende manieren als vooren verhaelt is".

No Dutch term in the corpus corresponds to *respondentia*. The type row for `respondentia`
already records Schuster calling it an English nominal subdivision, and its
`boundary_basis` is already `analyst-split`. **This corpus is independent confirmation
from practice**, and the maintainer may want to raise that row's `boundary_confidence` from
`medium` — a sighted decision, since the codings are withheld from this session.

### (v) A candidate form, deliberately not created: the floating bodemerij

Six acts (nos 962, 1999, 2003, 3229, 3231, 3239) have **no voyage at all**. No. 3231 lets
the ship sail "Oost, West, Suyden ende Noorden, naer alle ende ygelijcke alsulcke plaetsen,
havenen ende reeden als hem comparant believen sal"; no. 962 runs a calendar year; no. 1999
runs by the month with early repayment at the borrower's option and opgeld pro rata. The
price is a monthly rate, 1 to 3½ per cent, and the conditioning event is the passage of
time rather than the completion of a passage.

That is a different economic object — a revolving credit on the hull at sea-risk, not a
voyage bottomry — and on the surface it has a better claim to a row than the insurance-
referenced group rejected in logbook 2. **It was not created, on the diversity budget and
on the `.NR` rule together.** Six acts, three of them the same lender (Gerrit Bruynsen) and
two the same borrower (Jacob Beek of Alkmaar), is a counterparty relationship, and the
voyage acts are silent rather than contrary on free navigation. **Falsification condition:
a second corpus, from another port or another decade, in which time-priced bodemerij with
unrestricted navigation appears among unrelated counterparties.** At that point the
question is whether `DR1` is doing the work or whether the census needs the form.

### Two things checked and found not to be findings

**The armed merchantman is not evidence of a new hazard class.** No. 1995's six *gootelingen*
and four *steenstucken*, and the artillery quarrel in no. 1992, were briefly attractive as
evidence that the priced peril was adversarial rather than natural. They are already
inside `HZ2=P` and add nothing the characteristic does not hold.

**The multi-lender acts are not pooling.** No. 956 has four lenders on one hull, sharing
Dunkirker loss "penninck ponts gelijck" and expressly ranking *pari passu* — "even naer
gerechtigt sijn ende concurreren sullen sonder dat d'een oft d'ander eenige preferentie sal
mogen pretenderen". This is a syndicate of co-lenders, not a mutualisation among the
exposed, and `MC1` stays `spreading`. Worth a second look only if a fund ever appears
behind such a syndicate.
