## 2026-08-17 — ai (blind coding: Winkelman's Amsterdam bodemerijen)

Read 46 of the 48 notarial acts in Winkelman (ed.) 1983, *Bronnen tot de geschiedenis van
den Oostzeehandel*, RGP Grote Serie 184/185/186 — nrs 946–962, 1991–2005, 3227–3242. Of
the 46, **36 are `contract van bodemerij` and 10 are `protest wegens contract van
bodemerij`**. No. 946 is wanting from the copy consulted and no. 947 survives only as a
tail fragment; both are excluded. Winkelman's Inleiding on bodemerij was read with them.

### In: `bodemerij_amsterdam`, `LM-0512`–`LM-0524`

**One form, not several, and the reason is a missingness rule rather than a judgement of
taste.**

The corpus varies on four axes that could each have carried a split. Pledge object: keel
and gear, fractional parts, freight in its own right, goods and their returns, the
borrower's whole estate, sureties. Pricing basis: a flat per-voyage percentage in 31 acts,
a monthly rate in five, an absolute sum in one (no. 2002, 60 gld on 600, "maeckende
tesamen 660 gld."). Duration: 30 single-voyage against six running by time with free
navigation. Peril definition: a bare "op 't recht aventuyr van der zee" in most, an
enumerated piracy clause in four, and in nos 3240 and 3242 a clause importing the whole
custom of insurance — "alle anderen periculen, egeene uytgesondert, die een asseuradeur
naer coustume van asseurantie is loopende", *haverije grosse* included.

That last group looked like the strongest candidate for a second form, because in it the
lender bears **partial** loss pro rata ("penninck ponts gelijck") and takes pro rata of net
salvage, where classic bottomry is all-or-nothing on the pledged thing. **It was rejected
on the `.NR`/`0` rule.** The other 30 contracts do not deny proportional sharing; they are
*silent* on partial loss. Splitting the corpus here would have coded that silence as a
contrary value and manufactured a difference where the evidence shows only a difference in
what was written down. `check_dependence.py` makes the same point in its own idiom when it
marks separations achieved via `.NA` as weak.

Two further facts confirm the single form. The six insurance-referenced and piracy-clause
acts cluster on **three parties** — Abraham de Velaer as lender, Marten Corsen as borrower,
Dirck Woutersen and the pair Breugel & Smith — and on **eighteen months**, July 1618 to
September 1621. That is a drafting habit of particular counterparties, not an institution.
And the notary calls every one of them `contract van bodemerij`, in a register that also
holds the plain ones.

### Naming and dating: Amsterdam, 1601–1621, and not Hanseatic

**The row is named for what was actually read.** The corpus is the practice of two
Amsterdam notarial offices — Jan Franssen Bruyningh and Jacob Meerhout, with Epo
Stoltenburch appearing once by inserted copy — over twenty years. Calling it Hanseatic
*Bodmerei* or a northern European form would assert a geographic reach the evidence does
not carry, and **Frankot is the reason that assertion is not available cheaply**. Her case
is that Lübeck, Reval, Danzig, Kampen and Aberdeen used differing law in court despite
holding overlapping written compilations, so a shared text never licenses an inference to
shared practice. That argument is *methodological* here and nothing more: neither Frankot
2007 nor Frankot 2010 mentions bodemerij, bottomry or the sea loan at all, and it must not
be cited as though it did. Jenks 2010 on Prussian Hanseatic trade finance points the same
way from the other side — his instruments are *Wechsel* and *Darlehen* under a
*Kreditverbot*, with no bodmerei in view.

The acts do reach beyond Amsterdam, and that is recorded rather than used. Money is taken
up on bodemerij at La Rochelle (nos 955, 957, 959), Danzig (nos 960, 961, 1994, 1996) and
Königsberg (nos 2004, 2005, 3238); borrowers come from Stralsund, Emden, Reval and
Harlingen. **But every one of those instruments enters the record because an Amsterdam
notary protested it.** The corpus is a window cut by Amsterdam procedure, and the sample is
of Amsterdam enforcement, not of Baltic practice.

### `boundary_basis = documented-instance`, `boundary_confidence = high`

**What the value claims, and what it deliberately does not.** It claims that this row
exists because a dated, localised body of transactional practice was read and coded from
the acts themselves, in the way the `ko_*` rows and `avariz_vakfi_kirkcesme` do. It does
not claim a structural difference from the existing `bottomry` row, and that is not
modesty — **it could not be assessed.** This coding was run blind and the `bottomry`
codings were among the withheld material. The boundary against `bottomry` therefore stands
open, and the maintainer should treat re-basing this row to `structural-difference` (or
merging it into `bottomry`) as the first sighted decision after the blind is lifted.

The boundary against `sea_loan` **can** be stated from the sources and is not the same
question. `sea_loan` is separated on `contemporary-terminology`; what separates
`bodemerij_amsterdam` from it is a **constitutive pledge named in every single act** —
"op kielscheeps ende 't gereetschap van dien", or on named goods — the pledge that the word
*bodem* denotes. No. 3236 goes further and invokes a customary law for it by name: the
money runs "op 't recht avontuyr van der see, op kielscheeps ende 't gereetschap **naer
recht ende costume van bodemerije**". A contemporary Dutch legal form with its own custom
and its own instrument, the *bodemerijebrief*, is not the undifferentiated *foenus
nauticum*.

### Out: nothing, but three limits on the sample belong on the record

**The two missing acts are not random.** Nos 946 and 947 are the first two of the earliest
run; the loss truncates the corpus at its early end, so any statement about change between
1601 and 1621 begins one contract late.

**The 150 contracts Winkelman counts are not the population of Amsterdam bodemerij.** He
says so himself: much bodemerij was raised without a notary, and abroad the master could
raise it under the *Plakkaat* of 1563 art. 19 without any Amsterdam instrument at all. He
also gives the reason the notarial series is thin — the *partenrederij*, the free advance
on freight, and marine insurance at roughly half the opgeld were all competing with it.
**The survival is of the expensive, contested and formal cases.**

**Winkelman is a publisher's transcription, not the manuscript.** Every reading here is at
one remove, the OCR of the printed page adds a second, and the edition's own apparatus
carries at least one gap in the substance — at no. 3240 the percentage is simply absent,
and the editor notes it: "Het percentage niet vermeld; blijkbaar overgeslagen." That cell
is therefore not coded from that act.
