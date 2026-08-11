# The interdealer FX venue as a third: re-argument after the dealer claim failed

**Built:** 2026-08-11. **Status:** evidence card + verdict. Nothing here is cleared for the chapter
until the sentences in §8 are read against the objections in §7.

## 0. What this tests, and what it replaces

The Business Horizons run killed a claim. Its own adversarial review found that "the strong claim
fails against three primary sources, one of them the BIS itself," and the killing objection was one
sentence: **the dealer is a counterparty, not a third party**
(`dissertation/derivatives/business_horizons/runs/P4_RUN_GENEALOGY.md`, §R-C). That objection is
correct and this card does not contest it.

The objection was aimed at the dealer. It leaves untouched a different object — the **interdealer
electronic broking venue**: Reuters Dealing 2000-2 (later Reuters Matching, Thomson Reuters
Matching, Refinitiv Matching, now LSEG Matching) and EBS (Electronic Broking Services, now CME
Group's EBS Market). This card asks whether the venue survives what the dealer did not.

Every quotation below was read against the source file, locally, in this run. Nothing is inherited
from the earlier run's notes without re-verification against the source PDF. Two retrievals ran in
parallel and their findings were re-verified here rather than relayed: the fee tables were re-rendered
and read digit by digit, the New York Fed scans were re-OCR'd, and the LSEG and EBS clauses were
re-read in the files. Where a URL is unrecorded or a figure unverified, §9 and the surrounding text
say so.

---

## 1. Verdict

**SURVIVES, NARROWED — and narrowed differently from the way the brief anticipated.**

What holds, on primary sources:

1. **The venue is a third party, not a counterparty.** Four independent kinds of source say so: the
   operators' own rulebooks at both primary venues, a G10 central-bank working group in 2001, the
   Federal Reserve Bank of New York in 1998, and the exact BIS taxonomy that convicted the dealer.
   This is the strongest part of the case and it is not close.
2. **It tipped.** One winner per currency pair, two winners globally, by the end of the 1990s,
   attributed to network externalities by a Norges Bank working paper, to "tipping" by a G10
   central-bank working group that defines the word in its glossary, and to concentration on "only
   one of the two systems" by a Federal Reserve Board paper. The New York Fed measured it: 18 per
   cent of brokered US turnover in 1995, 57 per cent in 1998.
3. **Three of the four capacities hold outright** — price the exchange, evaluate a party, remove a
   party. Pricing holds far more strongly than the brief assumed: the operator publishes a
   per-million tariff that charges the two sides of one trade differently, keys the rate to each
   firm's own monthly volume, discounts by hour and surcharges by order type, and re-priced it
   unilaterally between two published editions. See §5.1.
4. **The fourth capacity, withholding the reason, holds by omission rather than by policy.** That is
   a weaker evidentiary object than the chapter's Amazon exhibit and the chapter must not pretend
   otherwise. See §5.4.
5. **The best finding in the file was not on the brief.** The capacity to withhold a reason tracks
   the regulatory frame rather than the market function. Same firm, same order book: LSEG owes
   written reasons and a board reconsideration on its CFTC-supervised swap execution facility, owes
   none on its FCA-supervised MTF; CME's unregulated dealing service, which governs the primary spot
   venue, grants no reasons, no review and no appeal at all. The FX Global Code obliges platforms to
   be transparent about how they treat an **order** and says nothing about how they treat a
   **party**. See §5.5.

What fails, and must be dropped or rewritten:

6. **The date alignment with the film fails as stated.** Reuters Dealing 2000-2 is 1992; EBS launched
   September 1993. The Dobie run is 1990 and the New York opening 5 July 1991. "The same years" is
   false. What is true, and citable to the New York Fed, is that the systems were under development
   in November 1991. See §4.
7. **"Matches two parties who do not deal with each other directly" is wrong for interdealer FX.**
   The same dealers traded both directly and through the venue, in parallel, throughout. The venue
   was an alternative to direct dealing, not a substitute for a relationship that never existed. See
   §7.1.
8. **The four capacities cannot all be dated to 1992–93.** For the 1990s the record carries the
   third-party structure, the credit screen, a fee, an access rule and the tipping. The
   conduct-policing capacities — evaluation, graded penalty, expulsion — are documented from 2011
   onward. See §7.2.
9. **EBS was owned by its own users from 1990 to 2006.** A third party to every trade; not an
   outside party to the class of traders. Reuters was the genuine outsider. See §7.3.

---

## 2. Question 1 — third party or counterparty?

### 2.1 The venue's own rulebook

**CME Group, *EBS Dealing Rules — General Terms*, effective 14 April 2025**, retrieved
2026-08-11 from
`cmegroup.com/trading/market-tech-and-data-services/files/ebs-dealing-rules-general-terms-effective-041425.pdf`,
19 pp., read in full. The Operator is defined at p. 4 as "EBS Service Company Limited, a company
registered in Switzerland."

> **Rule 2.9.** "The Operator is not a party to any Transaction. The Operator provides the EBS
> Dealing Services, each of which are a facility for Participants to effect dealings in certain
> Products for the sole purpose of allowing Participants to effect Transactions in Products. The
> Operator is not subject to any fiduciary or equitable duties to any Participant (except for those
> that cannot be excluded by Applicable Law)."
> — p. 6

The identical rule, same number, appears in the regulated sibling document. **CME Group, *EBS UK MTF
Rulebook — General Terms*, dated 2 March 2023**, retrieved same day from the same directory:

> **Rule 2.9.** "The Operator is not a party to any Transaction. The Operator provides the EBS UK
> MTF, a facility for Participants to effect dealings in certain Products for the sole purpose of
> allowing Participants to effect Transactions in Products."
> — p. 5

The other primary venue says it too, and adds who does bear the trade. **LSEG FX UK Multilateral
Trading Facility (MTF) Rule Book, effective 5 February 2025, version 1.1** (the successor rulebook
to Reuters Dealing 2000-2), retrieved 2026-08-11:

> **Rule 1.1.4 [R].** "LSEG is not a party to, and will not have any liability, or maintain any
> trading accounts, with respect to, Transactions conducted on the Platform. **Payment and
> settlement of executed Orders are the sole responsibility of the two Participants concerned.**"
> — p. 13

Three documents from two companies, one unregulated and two regulated, all disclaim counterparty
status in the general section. There is no central counterparty, no riskless principal, no novation.
The venue matches and steps out.

### 2.2 A G10 central-bank working group, describing the same systems in 2001

**Committee on the Global Financial System, *The implications of electronic trading in financial
markets*, January 2001**, retrieved 2026-08-11 from `bis.org/publ/cgfs16.pdf`, read in full.

*The report's own thesis, stated before comparison:* it is a stability report. A working group of the
G10 central banks asks whether the migration of trading to electronic systems changes the
efficiency, liquidity, orderliness and resilience of financial markets, and whether it creates new
operational and concentration risks. It makes no argument about platform capitalism, about
organisations, or about the political economy of intermediaries. It reaches for network-economics
vocabulary only as a way of predicting which trading systems will survive.

The taxonomy, at the head of the report's account of who is who:

> "Various classes of intermediaries can be distinguished by the type of services they provide.
> **Brokers do not take positions or trade for their own account; they are merely conduits for the
> orders or quotes of others.** Dealers take positions and trade for their own account as their
> primary business and usually make markets for their customers by providing bid and ask quotes."
> — p. 6

The glossary makes it a definition:

> "**Broker** — Firm which operates in a market on behalf of other participants to arrange
> transactions without being a party to the transactions itself (cf dealer)."
> — p. 25

> "**System provider** — Market participant which provides the infrastructure for trading (eg a
> stock exchange, EBS)."
> — p. 28

And Box D, which describes the two systems by name and traces a trade through them:

> "Trading in the inter-dealer foreign exchange market is dominated by ET systems. **The most
> important electronic brokerage facilities are Reuters' Dealing 2000-2 and Electronic Broking
> Services' (EBS) Spot Dealing System.** Participation in both systems is limited to dealers, who
> anonymously enter bids and/or offers into their terminals. … Since dealers will only be willing to
> take on settlement risk with counterparties for which they have internally approved credit lines,
> each participant identifies those subscribers with whom it is willing to trade and the credit
> limit it is willing to allocate to each trading party. That way, a subscriber will only be matched
> with counterparties with whom it is willing to deal, and for which it has available credit lines.
> **Upon hitting a bid or offer on the system, the two counterparties are revealed to each other and
> settlement occurs (on T+2).**"
> — Box D, "ET systems in the inter-dealer foreign exchange market," p. 16

That last sentence is the whole answer in the century the chapter cares about. The counterparties
are the two dealers. They are revealed *to each other*. They settle *with each other*. The system
holds no position at any point in the sequence.

### 2.3 The same structure, described by a Federal Reserve Bank in 1998

The rulebooks are current documents. This one is not, and it matters, because it puts the third-party
structure, the credit mechanism and the fee in the decade the chapter is writing about.

Federal Reserve Bank of New York, Sam Y. Cross, *All About… The Foreign Exchange Market in the United
States* (1998), ch. 4, "The Main Participants in the Market," p. 29:

> "The electronic broking systems are regarded as fast and reliable. Like a voice broker, they offer
> a degree of anonymity. **The counterparty is not known until the deal is struck, and then only to
> the other counterparty.** Also, **the systems can automatically manage credit lines. A trader puts
> in a credit limit for each counterparty that he is willing to deal with, and when the limit is
> reached, the system automatically disallows further trades.** **The fees charged for this
> computerized service** are regarded as competitive."

Every element the argument needs is in that paragraph, in 1998: the system is not a counterparty (the
counterparty is the other trader, revealed at the deal); the system operates a credit screen whose
limits the traders set; and the system charges a fee for doing it.

### 2.4 The BIS instrument that killed the dealer claim, applied to the venue

The sentence that convicted the dealer is a table
footnote in the BIS execution taxonomy, and the same footnote acquits the venue by name.

**Schrimpf, A., & Sushko, V., "FX trade execution: complex and highly fragmented," *BIS Quarterly
Review*, December 2019, 39–51**, retrieved 2026-08-11 from `bis.org/publ/qtrpdf/r_qt1912g.pdf`, read
in full, page numbers verified against the PDF's own footers.

> "'Direct' includes relationship-based trading by phone, trades through a chatting system, via a
> proprietary single-bank platform, or a direct electronic price stream. **'Indirect' refers to the
> involvement of a third party in the matching process. This can, for instance, be a traditional
> voice broker, an electronic broking platform or a multi-bank platform.**"
> — pp. 41–42 (the sentence begins at the foot of p. 41 and completes on p. 42)

And the annex table's footnote, which names the venues:

> "Electronic trading platforms geared to the non-disclosed inter-dealer market (eg EBS Market,
> Hotspot FX ECN, Reuters (Refinitiv) Matching)."
> — Annex Table A, note 7, p. 51

The dealer's own single-bank platform lands in the *direct* column, "not intermediated by a third
party." EBS Market and Reuters Matching land in the *indirect* column, as the third party. The BIS
draws exactly one line and puts the dealer on one side of it and the venue on the other.

The taxonomy is not stale. The current Triennial article restates it verbatim:

> "Direct: trades not intermediated by a third party. Indirect: trades intermediated by a third
> party – either a voice broker or a third-party electronic platform."
> — Krohn, I., Schrimpf, A., & Sushko, V., Box B, "The FX trade execution landscape through the
> prism of the 2025 BIS Triennial Survey," *BIS Quarterly Review*, December 2025, Graph B1 note 2,
> p. 36. Retrieved 2026-08-11 from `bis.org/publ/qtrpdf/r_qt2512.pdf`.

The same box names the venues as "the primary central limit order books (CLOBs), namely LSEG
Matching and EBS" (p. 36) and, in the Graph B2 note, "Primary venues: CME EBS Market and LSEG
Matching" (p. 37).

### 2.5 One more line, from the same 2025 box, that settles it obliquely

Discussing the extension of anonymous CLOB trading from spot into forwards and swaps:

> "The challenge for trading forwards and FX swaps in an anonymous electronic environment is that,
> unlike with spot trading, **these trades leave counterparties with future exposures to each
> other.** Currently, platform providers are developing various solutions to address counterparty
> credit risk in a (pre-trade) anonymous trading environment."
> — Box B, p. 37

If the platform provider were the counterparty there would be no problem to solve. The BIS describes
platform providers as parties working *on* a counterparty-credit problem that exists *between* the
two matched firms. That is a third party's position, described from the outside.

### 2.6 Verdict on Question 1

**The venue is a third party.** No source retrieved in this run puts an interdealer FX broking venue
in a principal or central-counterparty role, and four independent kinds of source — the operator's
rulebook, a G10 working group, the BIS Triennial taxonomy in two editions six years apart, and a
Norges Bank working paper (§3) — put it on the third-party side. The argument does not die here.

**One durability caveat, flagged not inferred away.** The 2025 box says platform providers are
"developing various solutions to address counterparty credit risk in a (pre-trade) anonymous trading
environment" for forwards and swaps. If one of those solutions is a central counterparty, the
third-party claim would need re-checking *for those instruments*. It would not touch spot. This run retrieved no document
showing an FX spot CLOB operating as a central counterparty, and no exhaustive search for one was
attempted.

---

## 3. Question 2 — the tipping claim

Three independent sources, three different institutions, and the two-winner qualification stated by
two of them in their own words.

### 3.1 Norges Bank

**King, M. R., Osler, C., & Rime, D., "Foreign exchange market structure, players and evolution,"
*Norges Bank Working Paper* 2011/10**, retrieved 2026-08-11 from
`norges-bank.no/globalassets/upload/english/publications/working-papers/2011/norges_bank_working_paper_2011_10.pdf`,
44 pp. The passage below was re-extracted from the PDF text layer in this run and sits on p. 22 of
the paper's own pagination.

> "In 1992, Reuters introduced the first electronic limit-order market to FX, now known as Thomson
> Reuters Matching. Other banks, worried that Reuters might monopolize interdealer trading, formed a
> consortium and introduced another such platform a year later, the Electronic Broking Service
> (EBS). … **By the end of the 1990s the electronic brokers dominated interdealer trading in the
> liquid currencies. Due to network externalities, liquidity naturally gravitated to just one
> platform for each currency. EBS has long dominated interbank trading for the EUR, JPY, and CHF,
> while Reuters dominates the GBP, AUD, CAD, and the Scandinavian currencies.** Voice brokers remain
> important for less liquid currencies – which are not traded over electronic brokers – so in 2010
> they still accounted for 10 percent of global spot FX trading."
> — p. 22

The prior run's recorded caution — that this is a two-winner outcome, not a single global winner —
is correct, and the source states the split itself in the next clause. The full pair allocation is
in the quotation above and should travel with the "one platform per currency" sentence every time it
is used.

Two further things on the same page that the chapter should not lose. First, the venues screen:

> "To ensure that dealers only trade with creditworthy counterparties, FX brokers screen every
> quote, comparing the existing exposure of a quoting bank (Citi) to its existing credit line with
> the potentially observing bank (Deutsche)."
> — p. 22, n. 14

Second — and this cuts against the chapter — the venue equalised rather than discriminated:

> "The introduction of interdealer limit-order markets reduced trading costs for small banks, since
> **the anonymous trading environment did not permit price discrimination.**"
> — p. 22

### 3.2 The G10 working group, in network-economics vocabulary, in January 2001

CGFS (2001), pp. 18–19, in a section headed "First-mover advantages and network effects" and a later
one on consolidation:

> "Five factors may lead to consolidation: economies of scale, network effects, standard-setting,
> switching costs and tipping effects. Economies of scale arise because ET systems, like most
> information goods, are characterised by low variable costs, the classic condition that tends
> towards monopoly. **Network externalities arise because the benefit of participating in a network
> increases with the number of other participants. Since traders move to the system offering the
> most liquidity, the large systems become even larger.** … Once a system becomes established, there
> may be 'tipping' effects: competition may be keen between rival trading systems when none accounts
> for a majority of transactions, but once one achieves a market share of, say, 70%, it may then
> rapidly take over almost the whole market."
> — pp. 18–19

> "A system that becomes dominant due to such first-mover advantages may not necessarily be the most
> efficient. … This raises the possibility of predatory pricing; a system being offered at below
> marginal cost to attract large numbers of subscribers who are then **faced with higher fees once
> the system has an effective monopoly**. The dominant players will be those with deep pockets."
> — p. 19

> "In some cases, markets will be split with different systems dominant in different parts. For
> example, **there are two dominant systems in the foreign exchange market, each dominating in
> particular currency pairs.** This underscores the point that once liquidity is concentrated on a
> certain platform, it will not easily migrate to another."
> — p. 19

And the glossary entry, which is the single most quotable line in the report for this chapter's
purposes:

> "**Tipping** — Tendency for a system provider that has achieved a dominant market share to move to
> (a near) monopoly."
> — p. 28

A G10 central-bank working group defined *tipping* in a glossary, named EBS as a *system provider*
in the entry two above it, and observed the two-winner split in the body — in January 2001.

### 3.3 The Federal Reserve Board

**Chaboud, A., Chiquoine, B., Hjalmarsson, E., & Vega, C., "Rise of the Machines: Algorithmic
Trading in the Foreign Exchange Market," *Board of Governors of the Federal Reserve System,
International Finance Discussion Papers* No. 980, October 2009**, retrieved 2026-08-11 from
`federalreserve.gov/pubs/ifdp/2009/980/ifdp980.pdf`. Published as *Journal of Finance* 69(5), 2014,
2045–2084; **the published version was not retrieved and its wording was not checked.** Cite the
IFDP for these words, or verify against the JF text before citing the JF.

> "Today, two electronic platforms process the vast majority of global interdealer spot trading in
> the major currency pairs, one offered by Reuters, and one offered by EBS. These platforms, which
> are both electronic limit order books, have become essential utilities for the foreign exchange
> market. **Importantly, trading in each major currency pair has over time become very highly
> concentrated on only one of the two systems.** Of the most traded currency pairs, the top two,
> euro-dollar and dollar-yen, trade primarily on EBS, while the third, sterling-dollar, trades
> primarily on Reuters. As a result, the reference price at any moment for, say, spot euro-dollar,
> is the current price on the EBS system, and all dealers across the globe base their customer and
> derivative quotes on that price. **EBS controls the network and each of the terminals on which the
> trading is conducted.** Traders can enter trading instructions manually, using an EBS keyboard,
> or, **upon approval by EBS**, via a computer directly interfacing with the system."
> — p. 3

Note "essential utilities," "EBS controls the network and each of the terminals," and "upon approval
by EBS." A Federal Reserve Board paper reaching for the language of infrastructure and permission,
about a private company, in 2009.

### 3.4 Verdict on Question 2

**Confirmed, with the scope stated.** The mechanism is network externalities; the outcome is one
winner per currency pair and two winners globally; the timing is "by the end of the 1990s" (King,
Osler & Rime, p. 22). Any sentence the chapter writes must carry the pair split. "Liquidity
gravitated to one platform for each currency" is the source's own wording and is safe. "The market
tipped to a single winner" is false and must never appear.

---

## 4. Question 3 — the dates

The prior run's recorded caution — "1992 is Reuters alone and EBS is 1993" — is **confirmed, and
sharpened.** Four independent sources bracket the sequence, and one of them is EBS's own website.

**Upper bracket: nothing was live in November 1991.** Federal Reserve Bank of New York, Foreign
Exchange Committee, *1991 Annual Report*, p. 8, retrieved 2026-08-11 from
`newyorkfed.org/medialibrary/microsites/fxc/files/annualreports/fxcar91.pdf`. The PDF carries no text
layer; the page was rendered at 300 dpi and read by OCR, then read again by eye against the render.

> "For several years a number of private-sector entities have been working to develop electronic
> order-matching systems for foreign exchange. … the Market Structure subcommittee organized
> presentations to the Committee in **November 1991 by the three groups developing electronic
> order-matching systems: Electronic Broking Services (EBS), MINEX Corporation, and Reuters plc**. An
> overview of the three systems **under development** by these groups is presented in the
> accompanying table."

Three systems, all still being built, in November 1991. "Electronic Broking Services" was already the
name.

**Reuters Dealing 2000-2: 1992.** The same committee's *1992 Annual Report*, p. 41, n. 53 (also
image-only, OCR'd and re-read here), defines the instruments of the April 1992 US turnover survey:

> "For the purpose of this survey, electronic dealing systems were defined to include **Reuters
> Dealing 2000-1 and 2000-2**, Quotron's F/X Trader, Telerate's TTS, or any other comparable system"

D2000-2 was an extant, nameable product when the April 1992 survey was designed. That agrees with
King, Osler & Rime, p. 22 ("In 1992, Reuters introduced the first electronic limit-order market to
FX") and with the Federal Reserve Bank of New York's own retrospective, below ("Until 1992, all
brokered business in the U.S. OTC market was handled by voice brokers"). An assisting run reports a
specific launch day of 29 April 1992 from a single non-independent source; **that day was not
verified here and should not be printed.** The year is solid.

**EBS: four dates, not one.** EBS's own business chronology, published on its live corporate site and
captured by the Internet Archive on **28 June 1998** at `web.archive.org/web/19980628094332if_/http://www.ebsp.com/chrono.html`
and `…/intro.html`. Corporate self-description, and dated; treat it as the company's account of
itself, which is exactly what it is.

> "**In January 1990**, when a group of leading market-making banks first decided to fund the
> development of an electronic broking system for interbank foreign exchange, its major objective was
> **to provide effective competition to Reuters**, the predominant provider of screen-based foreign
> exchange transaction services. **Since its official launch in September 1993**, however, EBS has
> captured a significant share of the global foreign exchange spot broking market…"
> — `intro.html`

> "**May 1992: Establishment of formal Partnership with 12 founding partner banks and Citicorp
> Dealing Resources.** The Electronic Broking Service (EBS) project was formally endorsed in 1992
> with the establishment of a partnership of the project participants and was the culmination of two
> years of research and development undertaken by Bank of America, Barclays Bank, Chemical Bank,
> Citibank, Credit Suisse, Lloyds Bank, Midland Bank, J P Morgan, National Westminster Bank, Quotron,
> Swiss Bank Corporation and Union Bank of Switzerland."
> · "**April 1993:** Lehman Brothers … the twelfth" · "**August 1993:** Commerzbank … the 13th bank"
> · "**September 1993: Official launch in UK, US and major European centres**" · "**November 1993:**
> EBS live in Japan, Singapore and Hong Kong"
> — `chrono.html`

Write it as four events. Funding decision January 1990. Formal partnership May 1992. Launch in
London, New York and Europe September 1993. Asia November 1993. "Founded 1993" is wrong and "launched
1990" is wrong; both circulate. Note also that the May 1992 list of twelve names is eleven banks plus
**Quotron**, Citicorp's screen business — the thirteenth bank arrives with Commerzbank in August
1993, which is where the familiar "consortium of thirteen banks" comes from.

**Minex.** Same chronology: "**December 1995: EBS and MINEX merge** — In December 1995 EBS and MINEX
joined forces in Asia. The combined service, now known locally as EBS/MINEX, quickly established
itself as the leading electronic broking service in the region **upon commencing operations in March,
1996**." The `intro.html` page calls the same event "an alliance," and the two pages disagree about
whether the Citicorp Dealing Resources acquisition was June or September 1996. EBS's own copy is not
internally consistent; attribute to the specific page.

**When it became dominant.** Federal Reserve Bank of New York, Sam Y. Cross, *All About… The Foreign
Exchange Market in the United States* (1998), ch. 4, p. 29, retrieved 2026-08-11 from an Internet
Archive capture of `ny.frb.org/education/addpub/usfxm/chap4.pdf`:

> "**Until 1992, all brokered business in the U.S. OTC market was handled by voice brokers.** But
> during the past few years, electronic broker systems (or automated order-matching systems) have
> gained a significant share of the market for spot transactions. The two electronic broking systems
> currently operating in the United States are Electronic Brokerage Systems [*sic*], or EBS, and
> Reuters 2000-2. **In the 1998 survey, electronic broking accounted for 13 percent of total market
> volume in the United States, more than double its market share three years earlier.** In the
> brokers market, **57 percent of turnover is now conducted through order-matching systems, compared
> with 18 percent in 1995**."

Two years of data, one page, from the central bank that ran the survey: 18 per cent of brokered US
turnover in 1995, 57 per cent in 1998. That is the tipping, measured. (Carry the `[sic]`: the NY Fed
expands EBS as "Electronic Brokerage Systems," which is not the company's name.) King, Osler & Rime,
p. 22, give the same finding without numbers: "By the end of the 1990s the electronic brokers
dominated interdealer trading in the liquid currencies."

**A gift for the tipping argument.** EBS recruited a Nordic partner bank in December 1996 for the
express purpose of taking the Scandinavian currencies from Reuters. Its own chronology quotes Göran
Bronner of S-E-Banken: "we hope to be able to encourage greater local participation in EBS and to
**enhance liquidity in smaller volume currencies, particularly Scandinavian currencies**." Fifteen
years later Reuters still held them (King, Osler & Rime, p. 22). A documented attempt, and a
documented failure, which is better evidence of lock-in than the assertion of lock-in.

**The problem this creates for the chapter.** *Slacker* ran at Austin's Dobie Theatre from 27 July to
11 October 1990 and opened in New York on 5 July 1991 (`v4/factbase/CLAIMS.md`, S1-088, S1-089,
S1-030). Reuters Dealing 2000-2 arrives in 1992 and EBS launches in September 1993. The chapter
cannot say platform coordination in wholesale finance dates to "the same years as the film." It can
say that the first electronic order-matching venue for currencies opened the year after the film's
New York run, and that the banks' answer to it opened two years after — checkable either way. Any
looser phrasing is the kind of thing a referee kills in a margin note. The film's shooting year was
not verified in this run and should not be asserted here.

There is a better sentence available, and the sources support it exactly. In November 1991, while
*Slacker* was in its first-run life, three consortia were building the systems: "the three groups
developing electronic order-matching systems: Electronic Broking Services (EBS), MINEX Corporation,
and Reuters plc" (NY Fed FXC, *1991 Annual Report*, p. 8). The film and the venues are not
contemporaries in operation. They are contemporaries in development, and that is a claim with a
central-bank citation behind it.

**What must not be spliced in to close the gap.** Reuters had electronic FX products well before
1992 — a bilateral dealing system from 1987 and the indicative-quote FXFX page at roughly the same
time (King, Osler & Rime, p. 22). Neither is a third-party matching venue. The 1987 system "merely
replaced telephone conversations with typed messages" (ibid.). Reaching back to 1987 to make the
dates line up would repeat the exact error the dealer claim died of: calling something a platform
because it is electronic.

---

## 5. Question 4 — the four capacities

The chapter's register, from `chapter/chapter_v5.md` §5: "A third can price an exchange, evaluate a
party, remove a party, and withhold its reason." Its exhibit for the platforms is a **written
policy** — Amazon's Prime Video licensing page. The right comparable object for an FX venue is
therefore its rulebook, and that is what this section reads.

### 5.1 Price the exchange — HOLDS, and more strongly than the brief assumed

The venue publishes a price list. **CME Group, *EBS UK MTF Fee Schedule*, cover date August 2025**,
retrieved 2026-08-11 from
`cmegroup.com/trading/market-tech-and-data-services/files/ebs-uk-mtf-fee-schedule.pdf`. Its own scope
line, p. 2: "This Fee Schedule applies to Participants on the EBS UK MTF, operated by BrokerTec
Europe Limited (BEL)," and it "forms part of participants' EBS Customer Agreement."

The transaction-fee table is a raster image inside the PDF, so `pdftotext` drops it silently. It was
recovered by rendering page 4 at 150 dpi and read digit by digit; the rendering was done twice, once
by an assisting run and once independently here, and the two agree.

> **Transaction Fees.** "Transaction fees for EBS Non-Deliverable Forward currency pairs traded on
> the EBS UK MTF are volume based on a price per million basis with separate prices for Make and
> Take volumes."
>
> | Monthly Volume Tier | Make Price | Take Price |
> |---|---|---|
> | $0 – $5.0bn | $8.00 | $12.00 |
> | $5.0bn – $10.0bn | $6.75 | $11.50 |
> | $10.0bn – $15.0bn | $6.25 | $11.50 |
> | $15.0bn – $20.0bn | $5.25 | $11.50 |
> | $20.0bn – $25.0bn | $3.25 | $8.75 |
> | Greater than $25bn | $2.25 | $8.75 |
>
> "An Asian hours (GMT 00:00:00 to GMT 04:59:59) discount will be applied at $1.75 per million traded
> for both Makes and Takes." · "IOC (FOK/FAK) Taker surcharge will be applied at $0.75 per million
> per Take."
> — p. 4

Read that as a doorman's tariff and it does everything the chapter needs. The two sides of a single
trade pay different amounts. What each pays depends on that firm's own monthly volume, so two firms
pay different prices for an identical trade. The hour of the night changes the price. The order type
changes the price. Access is charged separately and recurrently — the schedule's own definition, p.
2: "'Access Fee' means any recurring fee for access to EBS UK MTF or any Market" — with connectivity
lines at USD 3,000 per month on twelve-month minimum commitments.

**The operator re-prices at will, and the record shows it doing so.** The superseded edition, *EBS UK
MTF Fee Schedule*, cover date October 2024, same source directory, carries Make prices of $8.00,
$7.50, $7.00, $6.00, $4.00 and $3.00 across the same six tiers, and an Asian-hours discount of
"$2.50 per million." Five of the six Make rates were cut and the night discount was cut by 30 per
cent between editions. Take rates and connectivity charges did not move. Page 3 of the current
schedule states the mechanism: "Changes may be made to this fee schedule from time to time on notice
to customers." Notice, not consent.

The rulebook that governs the schedule states the obligation the other way round. *EBS UK MTF
Rulebook* (2023), Rule 12.2, p. 17:

> "Participants are liable for the payment of any applicable taxes, fees, duties, or levies that
> arise in connection with the trading of Products on the EBS UK MTF. **The fees which the Operator
> charges for access to the EBS UK MTF will be communicated to Participants on the Operator's
> website.**"

And a second charge sits on top of the order flow itself. *EBS Dealing Rules — Appendix: EBS Market*
(25 March 2022), §1.2 "Order Capacity", p. 13:

> "1.2.1 The Operator throttles the maximum number of Order submissions in a rolling 5 second window
> and restricts the number of Orders outstanding across each individual session. …
> 1.2.3 Order capacity may be increased for firms: a) exceeding the minimum fill ratio targets; and
> b) not appearing on the disruptive behaviour watch list (see Section 3).
> **A fee can be charged to the Participant for additional capacity.**"

The charge is not new. The Federal Reserve Bank of New York noted it of the 1990s systems in one
clause: "**The fees charged for this computerized service** are regarded as competitive" (Cross 1998,
p. 29). What has changed since is not that the venue charges but how finely it does.

A third charge prices conduct directly. **CME Group, *EBS Market NDF Messaging Programme*, effective
3 February 2025**: a firm breaching the quote-efficiency parameters "will be charged an excess
quoting surcharge per quote (in USD) above a maximum allowable quote threshold" — $0.50 per quote for
INR, KRW, TWD, IDR and PHP. The programme adds two discretions: "MEP parameter settings are as
follows but **can be amended at the discretion of EBS** to maintain a healthy market ecology (where
possible, at least one month's notice will be given)," and "The EBS MEP Waiver Committee … has **sole
discretion** as to whether to grant any waivers." The operator sets the price, sets the threshold
that triggers it, and decides who is forgiven.

**Two qualifications that must travel.** First, none of this prices the *exchange rate*. The venue
takes no view on the currency price and cannot discriminate on it: King, Osler & Rime, p. 22, "the
anonymous trading environment did not permit price discrimination," and the BIS Markets Committee,
*FX execution algorithms and market functioning*, Markets Committee Papers No. 13, October 2020,
p. 22, "Anonymous liquidity pools based on a central limit order book (CLOB) do not allow
apportioning of liquidity or price discrimination via the use of customised tags or other means to
identify a counterparty pre-trade." What the venue prices is the passage, not the goods.

Second — and this is a null finding worth as much as the positive ones — **the published schedule
covers non-deliverable forwards on the UK MTF, not spot on EBS Market.** The schedule itself points
at a document that does not exist publicly: "Product segments include Spot/Metals and EBS MTF NDF —
see applicable fee schedule for each." No spot or metals fee schedule appears anywhere on CME's EBS
regulatory-documents index. And where the MTF rulebooks promise publication of access fees, the
off-MTF *EBS Dealing Rules* — which govern EBS Market spot, the actual primary venue — promise
nothing. Rule 17.1 is the whole of its fees section: "Participants are liable for the payment of any
applicable taxes, fees, duties, or levies that arise in connection with the trading of Products on
the EBS Dealing Services." The primary spot venue's tariff is private.

### 5.2 Evaluate a party — HOLDS

*EBS Dealing Rules — General Terms* (2025):

> "3.5. **The Operator may in its absolute discretion approve or reject applications** or approve an
> application subject to such conditions and/or restrictions as it considers appropriate."
> — p. 7

> "4.1.9. Meet such further Eligibility Criteria as the Operator may prescribe from time to time
> with regard to Participation."
> — p. 7

> "10.4.1. … Prior to taking any action in consequence of a breach of the Rules by the Participant,
> the Operator may, in its absolute discretion, give the Participant a period of 20 Business Days in
> which to rectify the breach (the 'Rectification Period'). **If, in the Operator's opinion, the
> breach is not rectified by the end of the Rectification Period**, the actions that the Operator
> may take … include, but are not limited to: a) formal written notification of contravention of
> these Dealing Rules; b) restriction of specific Order types; c) impose systematic enforcements,
> such as a minimum quote life, or throttling of Orders; d) suspension from specific instruments,
> such as currency pairs; and e) suspension from an EBS Dealing Service."
> — p. 13

*EBS Market* appendix, on conduct review:

> "2.10.10. Should a Participant be frequently a Counterparty to reviewed Transactions, **their
> conduct may be reviewed. If the Operator determines that their conduct constitutes disruptive
> trading, it may take action it considers appropriate** under the EBS Dealing Rules – General
> Terms."
> — p. 10

And the same practice, described from the outside by a central-bank committee nine years before that
appendix was written:

> "In addition, both electronic broking platforms have a code or rules of conduct by which
> participants must abide. **The electronic brokers monitor the behaviour of their trading
> counterparties and adjust the trading parameters as required** in order to maintain an orderly
> market between the traditional non-algorithmic (manual) participants and the algorithmic
> (including HFT) accounts."
> — Markets Committee, *High-frequency trading in the foreign exchange market*, Markets Committee
> Papers No. 5, September 2011, §5.3, p. 22. Retrieved 2026-08-11 from `bis.org/publ/mktc05.pdf`.

The venue keeps a **watch list** and grades a firm's order capacity by whether it is on it (§5.1
above). That is evaluation with a consequence attached, in the operator's own document.

### 5.3 Remove a party — HOLDS, EXPLICITLY

*EBS Dealing Rules — General Terms* (2025), §11:

> "11.1. **The Operator may at its absolute discretion and without liability restrict, suspend or
> terminate the Participation of a Participant** (and/or its Authorised Employees) if, at any time:
> … 11.1.6. the Participant ceases to meet the relevant Eligibility Criteria; or **11.1.7. in any
> other circumstances where the Operator considers that restriction, suspension or termination of
> Participant is necessary to ensure or maintain orderly trading on the EBS Dealing Services.**"
> — p. 13

11.1.7 is the catch-all, and it turns on nothing but the Operator's own view of what is necessary.

The graded ladder is quoted at §5.2 above and ends at "suspension from an EBS Dealing Service." The
*EBS Market* appendix carries a parallel ladder for out-of-region quoting, §2.4, p. 14: "a) Formal
written notification of contravention of these Dealing Rules; b) The Operator reserves the right to
restrict throughput capacity; c) Ability to aggress via Quote Submit only …; d) **Suspension from EBS
Market.**"

The BIS said the same thing in 2011, in a sentence the chapter can use as the outside witness:

> "**Ultimately, the platforms have the option of reducing or removing the trading privilege of a
> predatory HFT counterparty.**"
> — Markets Committee Papers No. 5 (2011), §5.3, p. 22

One removal ground deserves separate notice, because it is the venue's version of the guest list.
*EBS Market* appendix, Rule 2.12.4, p. 11:

> "In accordance with the Customer Agreement, each Participant must use reasonable endeavours to
> maintain Credit Limits with other Participants of EBS Market. **The Operator may, at its
> discretion, suspend access to EBS Market where it determines that minimum mutual Counterparty
> credit access is not sufficient.**"

A firm can be suspended not for anything it did but because too few other participants are willing
to extend it credit. The venue enforces a verdict it did not itself reach and need not itself
explain.

### 5.4 Withhold the reason — HOLDS BY OMISSION ONLY

This is the capacity the chapter cares about most and the one the evidence supports least.

**What the rulebooks provide.** A duty to give notice of the decision, and nothing else:

> "11.2. The Operator will notify a Participant of a decision to restrict, suspend or terminate its
> or its Authorised Employee's Participation."
> — *EBS Dealing Rules — General Terms* (2025), p. 13

> "10.2. The Operator will notify a Participant of a decision to restrict, suspend or terminate its
> or its Authorised Employee's Participation."
> — *EBS UK MTF Rulebook* (2023), p. 14

**What they do not provide.** No obligation to state a reason. No review. No appeal. A
string search for "appeal" across all four retrieved EBS rulebooks returns **zero occurrences**
(`ebs-dealing-rules-general-terms-effective-041425`, `ebs-dealing-rules-ebs-market-appendix-20220325`,
`ebs-uk-mtf-rulebook-general-terms-2023-03-02`, `ebs-mtf-rulebook-appendix-ebs-institutional-fx`).

**The sharpest evidence is an asymmetry inside one rulebook.** The MTF rulebook requires publicity
for what the venue does to an *instrument*:

> "6.11. Any decision by the Operator in accordance with Rule 6.10 to suspend or remove any Product
> (and any derivatives referencing a Product) **shall be made public on the EBS UK MTF's website**
> and shall be communicated to the relevant Regulator."
> — p. 11

There is no parallel provision anywhere in the document for what the venue does to a *participant*.
Product suspensions are published to the world; firm suspensions are notified to the firm. The
rulebook is loud about instruments and silent about members.

**Why this is weaker than the Amazon exhibit.** Amazon's licensing page says,
affirmatively, "we cannot provide additional details about why any specific title was or was not
selected for licensing." That is a *stated policy of unstated reasons* — the chapter's own phrase.
(That quotation is carried over from `chapter/chapter_v5.md` §5, where the page is cited as retrieved.
This run did not re-fetch the Amazon page.)
The EBS rulebooks state no such policy. They simply impose no duty. A hostile reader will say that
absence of an obligation is not exercise of a power, and on this document alone the reader is right.
The chapter can claim that the venue **owes no reason**; it cannot claim, from these documents, that
the venue **declares it will give none**.

**The other primary venue is one step better and still short.** The *LSEG FX UK MTF Rule Book* (5
February 2025) runs two parallel tracks. One is disciplinary and has an appeal: the LSEG FX
Disciplinary Committee "may impose any of the following sanctions … verbal warning, written warning,
temporary suspension, termination of access to the Platform" (Rule 7.3.2, p. 35), and "All appeals
against the findings of the LSEG FX Disciplinary Committee must be addressed in writing within five
business days of notification of the sanction to the General Counsel, Capital Markets & Post Trade"
(Rule 7.4.1, p. 35). The other track has no committee and no appeal:

> **Rule 3.1.5.** "LSEG may at any time revoke, suspend, limit conditions, restrict or qualify a
> Participant or User's ability to access the Platform if, **in the sole discretion of LSEG**, such
> action is in the best interests of the Platform."
> — p. 21

Chapter 7 provides a further set of suspension rights under the heading "Other rights of LSEG to
suspend or terminate access" (Rules 7.5.1–7.5.3, pp. 35–36), also outside the disciplinary process.
So a firm removed through the disciplinary door may appeal; a firm removed through Rule 3.1.5 has no
stated route at all. Neither door obliges LSEG to say why. Publicity, as at EBS, runs the other way:
Rule 7.3.3 lets LSEG publish Committee findings "with or without disclosing the identity of the
Participant concerned … where it believes that to do so would be of assistance to the market" — the
venue's discretion, exercised over the participant, in the market's interest.

**The industry's own code does not close the gap.** The **FX Global Code**, published by the Global
Foreign Exchange Committee, **updated December 2024**, addresses platform operators under Principle 9
(p. 14): "Market Participants operating FX E-Trading Platforms should: have rules that are
transparent to users; make clear any restrictions or other requirements that may apply to the use of
the electronic quotations," followed on p. 15 by disclosure duties on market-risk transfer,
subscription services and client-interaction-data policies. Every item concerns how a platform
treats an **order** or an **order's data**. Nothing in the principle concerns how a platform treats a
**party** — admission, suspension, expulsion, or the giving of reasons. The code the market wrote for
itself does not ask.

### 5.5 The finding the chapter should want: the capacity tracks regulation, not function

Three rulebooks, two companies, one order-book technology, three different answers about whether a
removed firm is owed a reason. Line them up.

**Unregulated.** *EBS Dealing Rules — General Terms* (14 April 2025), governing EBS Market spot.
Admission at "absolute discretion" (Rule 3.5, p. 7). Removal at "absolute discretion and without
liability" with an open catch-all (Rule 11.1, 11.1.7, p. 13). Notice of the decision (Rule 11.2, p.
13). No reasons, no reconsideration, no appeal anywhere in the document.

**FCA-regulated.** *EBS UK MTF Rulebook* (2 March 2023) and *LSEG FX UK MTF Rule Book* (5 February
2025). Admission constrained: the identical EBS rule acquires nine words —

> "The Operator may approve or reject applications or approve an application subject to such
> conditions and/or restrictions as it considers appropriate, **subject to the requirement that the
> Operator assesses such applications in an objective and non-discriminatory manner.**"
> — *EBS UK MTF Rulebook*, Rule 3.5, p. 6

Removal still at absolute or sole discretion. LSEG adds a disciplinary committee and a five-day
appeal for one route out of two. Neither venue owes a reason.

**CFTC-regulated.** *LSEG FX SEF Rulebook*, effective 11 August 2026, version 4.1, operated by
Refinitiv US SEF LLC. Same firm, same matching business, US perimeter:

> **Rule 302(g).** "If the SEF decides to decline or condition an application for admission as a
> Participant, or terminate a Person's status as a Participant, the SEF shall promptly notify such
> Person (the 'Affected Person') thereof in a writing … Such Affected Person may, within seven (7)
> calendar days, request in writing that the SEF provide the reasons for the denial, conditioning or
> termination of Participant status. **Within fourteen (14) calendar days after receiving such
> written request, the SEF shall send a written response to the Affected Person setting forth the
> reasons** for the denial, conditioning or termination. Within fourteen (14) calendar days of
> receiving the SEF's written response, the Affected Person may request in writing that the Board
> reconsider the determination."
>
> **Rule 302(h).** "Within twenty-eight (28) calendar days of receiving any request for
> reconsideration, the Board shall either confirm, reverse or modify the denial, conditioning or
> termination of the Affected Person as a Participant…"

The grounds remain wide — Rule 302(e)(3) permits exclusion of a person who "would bring the SEF into
disrepute **as determined by the SEF in its sole discretion**." What changes is that the discretion
must be explained on request, and the explanation can be argued.

Withholding the reason is therefore not intrinsic to standing between two parties. It is what these
venues do wherever no rule compels otherwise, and the rule that compels otherwise exists in exactly
one of the three frames. That is a sharper claim than "platforms have power," and it comes out of
three documents.

**One dependency, flagged.** The CFTC end of that spectrum rests entirely on the *LSEG FX SEF
Rulebook*, whose retrieval URL was not recorded (see §9). The document was read here and Rule
302(g)–(h) verified against it, but the chapter cannot cite what a reader cannot open. Re-source it
before drafting. The unregulated-versus-FCA contrast, which is the weaker but still usable form of
the finding, stands on two CME documents whose URLs are recorded.

### 5.6 Terms the venue sets over the exchange itself

Beyond the four capacities, and worth a clause if the chapter has room. The venue writes the physics
of the encounter.

> "The variation in rules reflects, in part, differences in technologies and, in part, different
> views on market conduct. … the older inter-dealer venues tend to restrict the number of quotes per
> second and demand certain fill ratios … whereas the newer multi-bank ECNs tend to allow freer
> access."
> — Markets Committee Papers No. 5 (2011), p. 6

> "The two main electronic broking platforms (EBS and Reuters) have extensive trade controls,
> including requirements on the minimum amount of time that a quote has to remain active (minimum
> quote life, MQL), on the percentage of actual trades conducted relative to the total amount of
> quotes submitted (minimum fill ratio), and limits on the maximum number of quotes that can be
> submitted in a specified time interval. **These controls vary by currency pair.**"
> — ibid., §5.3, p. 22

> "The March 2011 launch on EBS of decimalised/fractional pip pricing (so-called 'tenths' or 'the
> fifth decimal') for the major currency pairs … is another recent case in point: **while algorithms
> can relatively easily handle the extra digit, human traders find it more difficult to adapt.**"
> — ibid., p. 8

> "the frequency of pricing updates on the EBS platform was raised from every 100 milliseconds (ms)
> to every 20ms in September 2016, and further to every 5ms **for select participants** in February
> 2017."
> — Markets Committee, *Monitoring of fast-paced electronic markets*, Markets Committee Papers
> No. 10, September 2018, p. 6. Retrieved 2026-08-11 from `bis.org/publ/mktc10.pdf`.

And the venue's own account of engineering who gets matched, *EBS Market* appendix, Rule 2.8.2(a),
pp. 7–8:

> "'Latency Floor' is an augmentation to the EBS Market Matching process aimed at ensuring that
> speed as a stand-alone strategy is not a pre-requisite for success on EBS Market. … **The order of
> Participants within a batch is randomised on a per batch basis.** By adding a randomised message
> batching window ahead of Orders being processed by the matching engine, the Operator is able to
> prevent low single digit millisecond differences in hardware and communication path … from being a
> meaningful advantage between Participants."

Changing the price grid redistributed advantage from humans to algorithms; changing the data
frequency gave some participants a faster picture than others; the latency floor deliberately
randomises the queue. None of that is a capacity in the chapter's four-item list. All of it is the
venue setting terms that decide who wins, and the chapter should at minimum know it exists before
claiming the list is complete.

---

## 6. Question 5 — every FX figure, re-verified

Nothing in this table is inherited. Each line was checked against a document retrieved in this run.

| Figure | Status | The verified form |
|---|---|---|
| "$9.6 trillion per day, April 2025, up 28%" | **SUPERSEDED — do not use** | Preliminary. The final data revise it down. **Use: "$9.5 trillion per day in April 2025, up 27% from 2022."** BIS *Quarterly Review*, December 2025, p. 19; the FX article states "$9.5 trillion in April 2025, more than a quarter higher than in April 2022" at p. 23. The preliminary release at `bis.org/statistics/rpfx25_fx.htm` (30 September 2025) still carries $9.6tn/28% and still carries the notice "The data are subject to revision"; it had not been updated when fetched on 2026-08-11. The earlier library card `bis2025triennial.md` predicted this revision. It happened. |
| Interdealer 46% / $4.4tn; other financial institutions 50% / $4.8tn; non-financial customers 5% | **PRELIMINARY ONLY — flag if used** | These appear only in the 30 September 2025 preliminary release, which is subject to revision, and the December 2025 *Quarterly Review* does not restate them in the same terms. Verified verbatim on the release page 2026-08-11. If quoted, cite the preliminary release and say it is preliminary. The rounding traps recorded earlier still hold: 46 + 50 + 5 = 101, and $4.4tn + $4.8tn = $9.2tn against a $9.6tn total. Do not add either set. |
| "Foreign exchange is the largest financial market in the world" | **STILL UNSUPPORTED as stated** | No BIS document retrieved in this run asserts the rank. The 2025 Triennial release, the December 2025 *Quarterly Review*, the 2019 and 2016 *Quarterly Review* articles and Markets Committee Papers Nos. 5, 10 and 13 state magnitude and never rank. True by turnover, false by outstanding stock. If used at all, use the turnover form with the figure attached. |
| Internalisation "63% in spot, above 90% in some major currency pairs" | **VERIFIED, and now stale** | Verbatim, Moore, Schrimpf & Sushko, *BIS Quarterly Review*, December 2016, Box C, p. 45: "internalisation ratios are highest for spot, at 63% … Internalisers with a large e-FX business can have much larger internalisation ratios (even above 90% in some **major** currency pairs)." The word "major" is in the source and the earlier draft dropped it. **Current figure:** "Internalisation ratios reached levels upwards of 80% across all currencies in major FX trading hubs (those for G10 currencies were even higher)" — Krohn, Schrimpf & Sushko, Box A, *BIS Quarterly Review*, December 2025, p. 31. |
| Internalisation definition | **VERIFIED verbatim** | "Internalisation refers to the process whereby dealers seek to match staggered offsetting client flows on their own books instead of immediately hedging them **in the inter-dealer market**." Moore, Schrimpf & Sushko, December 2016, Box C, p. 45. The earlier draft's "in the open market" was a substitution and is wrong. |
| "concentration begets more concentration" | **VERIFIED verbatim, source corrected** | Schrimpf & Sushko, *BIS Quarterly Review*, **December 2019, p. 45** — not 2016. Re-read from `r_qt1912g.pdf` in this run; the sentence sits in the paragraph beginning "Internalisation may also partly explain why the FX industry remains highly concentrated among a few very large dealers." |
| "more than 75 FX venues" | **VERIFIED but 2019 vintage, and attributed** | *BIS Quarterly Review*, December 2019, p. 41: participants have "more than 75 different FX venues at their disposal (**Sinclair (2018)**)." It is the BIS quoting a trade source, not a BIS measurement. The 2025 successor figure is different in kind: "Customers who turn to indirect disclosed electronic trading could, in theory, transact on over 15 multi-dealer platforms," December 2025, p. 37. Do not present the two as a series. |
| Interdealer share, spot-only vs all-instrument | **TRAP CONFIRMED** | King, Osler & Rime's interdealer shares are spot-only; the BIS 46% is all instruments. Splicing them manufactures a trend. Confirmed again by reading both sources in this run. |
| EBS/Reuters currency-pair split | **VERIFIED verbatim** | "EBS has long dominated interbank trading for the EUR, JPY, and CHF, while Reuters dominates the GBP, AUD, CAD, and the Scandinavian currencies." King, Osler & Rime (2011), p. 22. Corroborated independently for the top three pairs by Chaboud et al., IFDP 980 (2009), p. 3. |
| Ownership chronology | **PARTLY VERIFIED** | EBS founded by a bank consortium (King, Osler & Rime, p. 22, retrieved). "EBS has been part of the ICAP group since 2006" — Chaboud et al., IFDP 980 (2009), p. 3, n. 4, retrieved. CME Group completed its acquisition of NEX Group (which held EBS) on **2 November 2018** — established from CME Group's own press release and the corresponding Form 8-K exhibit on SEC EDGAR (`sec.gov/Archives/edgar/data/0001156375/000119312518322722/d644644dex991.htm`) located by search; **the 8-K exhibit itself was not opened**, so the date stands as authoritative-but-unopened until someone reads it. The 2025 rulebook names the operator as "EBS Service Company Limited, a company registered in Switzerland" and carries "© 2025 CME Group." |

---

## 7. The objections, stated at full strength

### 7.1 "Two parties who do not deal with each other directly" is false here

The brief's framing describes the venue as matching "two parties who do not deal with each other
directly." For interdealer FX the sources contradict it. Direct interdealer
dealing and venue-matched interdealer dealing ran in parallel for decades, between the *same* firms.
King, Osler & Rime, p. 22: dealers "preferred the anonymity of these platforms to direct interdealer
trading because it allowed them to work off positions without tipping off their competitors." The
BIS still counts both channels separately in the current Triennial (December 2025, p. 36, Graph
B1.A: "Voice, direct," "Electronic, direct," against "Voice, indirect," "Electronic, indirect").

The venue's third-party status does not depend on the parties being strangers. It depends on the
venue not being one of them. Write the claim that way and it holds; write it the brief's way and a
referee kills it in one sentence.

### 7.2 The chronology gap is narrower than it looks, but it is real

Most of §5 comes from documents dated 2011, 2018, 2020, 2022, 2023 and 2025. Three things reach back
into the decade the chapter cares about, all from central-bank sources. The Federal Reserve Bank of
New York records, of the 1990s systems, that "the counterparty is not known until the deal is struck,
and then only to the other counterparty," that "the systems can automatically manage credit lines"
with limits the traders set, and that they charge fees for the service (Cross 1998, p. 29). The G10
working group records the access rule: "Participation in both systems is limited to dealers" (CGFS
2001, Box D, p. 16). Third-party status, the credit screen, a charge and a membership boundary are
therefore all documented for the 1990s venue.

What is not documented for the 1990s is the conduct machinery. Minimum quote life, fill ratios, watch
lists, latency floors, throughput throttles, the graded penalty ladder and the discretionary
suspension clause are artefacts of the algorithmic era. They arrived because high-frequency firms
did, and the BIS says so in the report that first catalogues them (Markets Committee Papers No. 5,
2011).

So the chapter sentence has to be two-part: the **structure and the charge** date to 1992–98; the
**disciplinary capacities**, in writing, date to the 2010s. Collapsing the two is the same move that
killed the dealer claim, and it will die the same way.

### 7.3 EBS was owned by the parties it coordinated

King, Osler & Rime, p. 22: "Other banks, worried that Reuters might monopolize interdealer trading,
formed a consortium and introduced another such platform a year later." EBS says the same thing about
itself, and more bluntly — the founding purpose, in its own words, was "**to provide effective
competition to Reuters**, the predominant provider of screen-based foreign exchange transaction
services" (`ebsp.com/intro.html`, captured 28 June 1998). From the January 1990 funding decision until
ICAP bought it in 2006, EBS belonged to its own users. It was a third party to every trade it matched
and not an outside party to the class of firms that traded on it — a mutual, in the old sense.

This cuts two ways and the chapter should take both. Against: the 1993 venue held no power *over* the
banks, because the banks held it. In favour: the founding of EBS is a documented case of parties
building a venue specifically to stop a third party from acquiring the power the chapter describes,
and the record includes the attempt failing in the Scandinavian pairs (§4). That is a better story
than the one the brief wanted, and it is the story the sources actually tell.

Reuters, by contrast, was a genuine outsider — an information company with no dealing book. If the
chapter wants one clean 1992 third party, it is Reuters.

### 7.4 One class of user, not two sides

An interdealer CLOB in 1993 had a single class of participant. CGFS 2001, Box D, p. 16:
"Participation in both systems is limited to dealers." Every participant could be maker or taker.
There were no two distinct sides with a price structure allocated between them, which is the
Rochet–Tirole test the earlier run applied to the dealer. If the chapter's "third" needs a two-sided
market, the 1993 interdealer venue does not supply one.

The chapter's own framing survives this, because its third is defined by position and by capacity,
not by two-sidedness — "a third can price an exchange, evaluate a party, remove a party, and
withhold its reason" (`chapter_v5.md` §5). But if any sentence reaches for "two-sided market" or
cites Rochet and Tirole, that sentence is dead on arrival and should be cut before drafting.

The venues did later acquire two distinct sides. The BIS records the moment: "as a response to
competition from multi-bank platforms (eg FXall, Currenex or Hotspot), **EBS and Reuters opened up
to hedge funds and other customers via prime brokerage arrangements in 2004 and 2005,
respectively**" (Rime, D., & Schrimpf, A., "The anatomy of the global FX market through the lens of
the 2013 Triennial Survey," *BIS Quarterly Review*, December 2013, p. 35; retrieved 2026-08-11 from
`bis.org/publ/qtrpdf/r_qt1312e.pdf`). If the chapter wants a two-sided FX venue, it is dated 2004–05,
not 1992.

### 7.5 The venue does not choose who meets whom in any discretionary sense

Matching runs on price-time priority, subject to a bilateral credit screen the *participants*
populate. *EBS Market* appendix, Rule 2.8.1, p. 7: "**Each Participant must establish a relationship
with its Counterparties, satisfy itself of the creditworthiness of its Counterparties and extend
credit to them as it sees fit.** For a Match to be made in EBS Market between two Participants,
mutual credit must exist between those Participants." The rulebook's definition of Credit Limit (General Terms, p. 2): "The maximum amount of credit allocated to a Counterparty with whom a **Participant** is prepared
to enter into a Deal." CGFS 2001, Box D, p. 16, says the same thing in 2001: "each participant
identifies those subscribers with whom it is willing to trade and the credit limit it is willing to
allocate to each trading party."

The venue operates the screen; the participants write it. That is a real limit on the analogy to a
doorman with a list, and the chapter must not describe the venue as vetting counterparties for
creditworthiness. What the venue does hold is the consequence: Rule 2.12.4 lets it suspend a firm
whose *mutual credit access* has fallen too low (§5.3). It enforces the collective verdict without
owning it.

---

## 8. If the chapter uses this — the sentences that can be published

Each is written to be defensible as it stands. Citations are given in the form the chapter would
need. Do not edit these without re-reading §7.

**On the structure and the date.**

> Platform coordination in wholesale finance is older than the vocabulary for it. In November 1991
> the Federal Reserve Bank of New York's Foreign Exchange Committee sat through presentations by
> "the three groups developing electronic order-matching systems: Electronic Broking Services (EBS),
> MINEX Corporation, and Reuters plc" (Foreign Exchange Committee, 1991 Annual Report, p. 8). Reuters
> got there first, in 1992; the banks' consortium, formed expressly "to provide effective competition
> to Reuters," launched EBS in September 1993 (EBS, business chronology, 1998). Neither was a party
> to the trades it matched. Both were third parties running venues on terms they wrote.

**On when it tipped, if the chapter wants a measured number rather than an assertion.**

> The concentration was fast and it was measured by the central bank that ran the survey. Electronic
> order-matching took 18 percent of brokered turnover in the United States in 1995 and 57 percent in
> 1998, by which point "electronic broking accounted for 13 percent of total market volume in the
> United States, more than double its market share three years earlier" (Cross, 1998, p. 29).

**On the third-party status, using the instrument that convicted the dealer.**

> The Bank for International Settlements draws the line in a table footnote. "Direct" trades are
> those "not intermediated by a third party," and the category takes in a dealer's own single-bank
> platform. "Indirect" trades are those "intermediated by a third party — either a voice broker or a
> third-party electronic platform," and the category takes in EBS Market and LSEG Matching by name
> (BIS, 2025, p. 36; the same distinction at BIS, 2019, pp. 41–42 and p. 51). The dealer and the
> venue fall on opposite sides of one line drawn by the institution that supplies the market's
> numbers.

**On the venue's own disclaimer** — use only if the chapter wants the rulebook in evidence.

> The venue says it in its own rules. CME Group's EBS Dealing Rules open the general section with
> it: "The Operator is not a party to any Transaction" (EBS Dealing Rules, General Terms, effective
> 14 April 2025, Rule 2.9).

**On tipping.**

> Liquidity did not spread; it concentrated. "Due to network externalities, liquidity naturally
> gravitated to just one platform for each currency" — EBS taking the euro, yen and Swiss franc,
> Reuters the pound, the Australian and Canadian dollars and the Scandinavian currencies (King,
> Osler & Rime, 2011, p. 22). A working group of the G10 central banks had already named the
> mechanism and defined the word for it: tipping, "the tendency for a system provider that has
> achieved a dominant market share to move to (a near) monopoly," with EBS given in the glossary as
> an example of a system provider (CGFS, 2001, pp. 19, 28).

**On the capacities.**

> By the 2010s the venue held in writing most of what a doorman holds at a door. It charges for
> access and charges again for more of it, and it may raise a firm's order capacity only if the firm
> is "not appearing on the disruptive behaviour watch list." It may "in its absolute discretion
> approve or reject applications." It may "at its absolute discretion and without liability
> restrict, suspend or terminate the Participation of a Participant," including "in any other
> circumstances where the Operator considers" it necessary. A central-bank committee described the
> practice from the outside in 2011: "Ultimately, the platforms have the option of reducing or
> removing the trading privilege of a predatory HFT counterparty" (CME Group, EBS Dealing Rules,
> Rules 3.5, 11.1, 11.1.7 and EBS Market Appendix §1.2.3; BIS Markets Committee, 2011, p. 22). What
> the rules never promise is a reason. They promise notice of the decision and nothing more, the
> word "appeal" does not occur in them, and the one publicity duty they do impose runs to
> instruments rather than to firms: a decision to suspend a *product* "shall be made public on the
> EBS UK MTF's website," while a decision to suspend a *participant* is notified to the participant
> (EBS UK MTF Rulebook, 2023, Rules 6.11 and 10.2).

**On pricing, if the chapter wants the doorman's tariff.**

> The venue publishes what the passage costs. On the EBS UK MTF the two sides of a single trade pay
> different amounts — $8.00 per million to make, $12.00 to take at the lowest volume tier — and what
> each firm pays depends on its own monthly volume, falling to $2.25 and $8.75 above $25 billion a
> month. Trading between midnight and five in the morning GMT is discounted $1.75 per million; an
> immediate-or-cancel order costs the taker $0.75 more. Between the October 2024 and August 2025
> editions of the schedule the operator cut five of six make rates and cut the night discount by 30
> percent. The rule governing the change reads: "Changes may be made to this fee schedule from time
> to time on notice to customers" (CME Group, EBS UK MTF Fee Schedule, August 2025, pp. 3–4).

**On regulation, if the chapter wants the sharpest single finding.**

> The same company wrote the same rule three ways, and the difference is not technological. On
> LSEG's swap execution facility, supervised by the CFTC, a firm denied admission or terminated may
> ask why, and "within fourteen (14) calendar days after receiving such written request, the SEF
> shall send a written response to the Affected Person setting forth the reasons," after which the
> board must confirm, reverse or modify (LSEG FX SEF Rulebook, Rules 302(g)–(h)). On LSEG's
> FCA-supervised multilateral trading facility, the same firm may remove a participant "at any time
> … if, in the sole discretion of LSEG, such action is in the best interests of the Platform," and
> owes no reason (LSEG FX UK MTF Rule Book, Rule 3.1.5). On CME's unregulated EBS dealing service,
> which runs the primary spot venue, the operator acts "at its absolute discretion and without
> liability," notifies the participant of the decision, and the word appeal does not occur in the
> document (EBS Dealing Rules, Rules 11.1, 11.2). Withholding the reason is not what it takes to
> stand between two parties. It is what a third does where nothing obliges it otherwise.

**Sentences that must NOT be written.**

- ~~"Platform coordination in wholesale finance dates to the same years as the film."~~ Reuters
  Dealing 2000-2 is 1992 and EBS launched September 1993. Only the *development* of the systems is
  contemporaneous with the film, and that is the claim to make.
- ~~"EBS was founded in 1993."~~ Funding decision January 1990, formal partnership May 1992, launch
  September 1993. Pick the event and name it.
- ~~"The market tipped to a single winner."~~ Two winners, one per currency pair.
- ~~"EBS matched two parties who did not deal with each other directly."~~ They dealt directly too,
  in parallel, throughout.
- ~~"The venue screened counterparties for creditworthiness."~~ The participants set the credit
  limits; the venue enforced them.
- ~~"The venue priced each party's access differently."~~ Anonymous CLOBs do not price-discriminate
  pre-trade (King, Osler & Rime, 2011, p. 22; BIS Markets Committee Papers No. 13, 2020, p. 22).
- Any sentence citing Rochet and Tirole, or the phrase "two-sided market," about the 1993
  interdealer venue. It had one side.

---

## 9. Sources retrieved in this run

All fetched 2026-08-11 unless noted, converted with `pdftotext -layout` (or `pdftoppm` + `tesseract`
where a document carries no text layer), and held in the session scratchpad under `scratchpad/fx/`,
`scratchpad/fx_dates/` and `scratchpad/fx_rules/`.

### Central-bank and official

| Document | URL | Read |
|---|---|---|
| CGFS, *The implications of electronic trading in financial markets*, Jan 2001 | `bis.org/publ/cgfs16.pdf` | full |
| Markets Committee Papers No. 5, *High-frequency trading in the FX market*, Sep 2011 | `bis.org/publ/mktc05.pdf` | full |
| Markets Committee Papers No. 10, *Monitoring of fast-paced electronic markets*, Sep 2018 | `bis.org/publ/mktc10.pdf` | targeted |
| Markets Committee Papers No. 13, *FX execution algorithms and market functioning*, Oct 2020 | `bis.org/publ/mktc13.pdf` | targeted |
| Rime & Schrimpf, *BIS Quarterly Review*, Dec 2013 | `bis.org/publ/qtrpdf/r_qt1312e.pdf` | targeted |
| Moore, Schrimpf & Sushko, *BIS Quarterly Review*, Dec 2016 | `bis.org/publ/qtrpdf/r_qt1612e.pdf` | targeted, Box C re-verified |
| Schrimpf & Sushko, *BIS Quarterly Review*, Dec 2019 | `bis.org/publ/qtrpdf/r_qt1912g.pdf` | full, page map verified |
| *BIS Quarterly Review*, Dec 2025 (whole issue; Krohn/Schrimpf/Sushko FX article, Boxes A and B) | `bis.org/publ/qtrpdf/r_qt2512.pdf` | targeted, page map verified |
| BIS Triennial preliminary release, 30 Sep 2025 | `bis.org/statistics/rpfx25_fx.htm` | full |
| King, Osler & Rime, Norges Bank WP 2011/10 | `norges-bank.no/globalassets/upload/english/publications/working-papers/2011/norges_bank_working_paper_2011_10.pdf` | targeted, p. 22 re-verified |
| Chaboud, Chiquoine, Hjalmarsson & Vega, Federal Reserve Board IFDP No. 980, Oct 2009 | `federalreserve.gov/pubs/ifdp/2009/980/ifdp980.pdf` | targeted, p. 3 |
| NY Fed Foreign Exchange Committee, *1991 Annual Report* | `newyorkfed.org/medialibrary/microsites/fxc/files/annualreports/fxcar91.pdf` | image-only PDF; p. 8 rendered at 300 dpi and OCR'd, then read against the render |
| NY Fed Foreign Exchange Committee, *1992 Annual Report* | `…/fxcar92.pdf` | image-only PDF; pp. 20–55 rendered and OCR'd; n. 53 at printed p. 41 verified against the render |
| Cross, S. Y., *All About… The Foreign Exchange Market in the United States*, FRBNY, 1998, ch. 4 | Internet Archive capture of `ny.frb.org/education/addpub/usfxm/chap4.pdf` | full chapter, pp. 23–30 |

### Venue documentation

| Document | Source | Read |
|---|---|---|
| CME Group, *EBS Dealing Rules — General Terms*, eff. 14 Apr 2025 | `cmegroup.com/trading/market-tech-and-data-services/files/ebs-dealing-rules-general-terms-effective-041425.pdf` | full, 19 pp. |
| CME Group, *EBS Dealing Rules — Appendix: EBS Market*, 25 Mar 2022 | `…/ebs-dealing-rules-ebs-market-appendix-20220325-globex-clean.pdf` | full, 14 pp. |
| CME Group, *EBS UK MTF Rulebook — General Terms*, 2 Mar 2023 | `…/ebs-uk-mtf-rulebook-general-terms-2023-03-02.pdf` | full |
| CME Group, *EBS MTF Rulebook — Appendix: EBS Institutional FX* | `…/ebs-mtf-rulebook-appendix-ebs-institutional-fx.pdf` | targeted |
| CME Group, *EBS UK MTF Fee Schedule*, cover date Aug 2025 | `…/ebs-uk-mtf-fee-schedule.pdf` | full; p. 4 fee table is a raster image, rendered at 150 dpi and read digit by digit, twice, independently |
| CME Group, *EBS UK MTF Fee Schedule*, cover date Oct 2024 (superseded) | `…/ebs-uk-mtf-fee-schedule-oct-2024.pdf` | p. 4 rendered and compared against the Aug 2025 edition |
| CME Group, *EBS Market NDF Messaging Programme*, eff. 3 Feb 2025 | `…/ebs-market-ndf-messaging-programme-02-2025.pdf` | targeted |
| CME Group, EBS regulatory-documents index | `cmegroup.com/markets/ebs/regulatory-documents.html` | index enumerated, 16 documents |
| LSEG, *LSEG FX UK Multilateral Trading Facility (MTF) Rule Book*, eff. 5 Feb 2025, v1.1 | lseg.com — **exact URL not recorded**; retrieved by an assisting run, verified here from the file (PDF metadata: title "LSEG FX UK MTF Rule Book", created 5 Feb 2025) | targeted, Chs. 1–3, 7 |
| LSEG, *LSEG FX SEF Rulebook*, eff. 11 Aug 2026, v4.1 (Refinitiv US SEF LLC) | lseg.com — **exact URL not recorded**; same provenance | targeted, Rule 302 |
| Global Foreign Exchange Committee, *FX Global Code*, updated Dec 2024 | `globalfxc.org/docs/fx_global.pdf` — re-fetched here and byte-identical (MD5 match) to the assisting run's copy | targeted, Principle 9, pp. 14–15 |

**Provenance caveat on the two LSEG rulebooks.** Both were retrieved by an assisting run whose URLs
were not recorded, and direct probing of lseg.com in this run did not recover them (`/en/fx` returns
a JavaScript shell; the obvious `/content/dam/…` paths 404). The documents themselves were read here
and every quotation above was verified against the file. The UK MTF Rule Book carries "Sensitivity:
Confidential" in its page footer, so before the chapter cites it, someone must establish that LSEG
serves it publicly. Until then, treat the LSEG material as corroboration for the CME material rather
than as an independently citable source.
| EBS, corporate business chronology and introduction, `ebsp.com` | `web.archive.org/web/19980628094332if_/http://www.ebsp.com/chrono.html` and `…/intro.html` | full, both pages |

**Retrieval notes for reuse.** `bis.org`, `norges-bank.no`, `federalreserve.gov`, `newyorkfed.org` and
`web.archive.org` serve to a plain `curl -sL -A "Mozilla/5.0"`. `cmegroup.com` returns 403 to that and
times out under WebFetch at 60 s. It serves PDFs to `curl` carrying the full browser header set —
`User-Agent`, `Accept`, `Accept-Language`, `Referer: https://www.cmegroup.com/`, `Sec-Fetch-Dest:
document`, `Sec-Fetch-Mode: navigate`, `Sec-Fetch-Site: same-origin`, `Upgrade-Insecure-Requests: 1`.
Its Akamai layer also blocks on request *rate*: three or more near-simultaneous requests trip a
multi-minute block, so space requests roughly 20 seconds apart. HTML pages on the same host need
`Sec-Fetch-Site: none` instead of `same-origin`.

**Two documents whose tables `pdftotext` silently drops.** The EBS fee schedules carry their
transaction-fee tables as raster images. Text extraction returns the surrounding bullets and no
numbers at all, with no error, which is how a wrong figure would enter a draft unnoticed. Render the
page (`pdftoppm -r 150 -f 4 -png`) before quoting any EBS fee.

**Not retrieved, and named so.** The published *Journal of Finance* (2014) text of Chaboud et al. The
published *RAND Journal of Economics* (2023) text of Gautier, Hu & Watanabe. The CME Group Form 8-K
exhibit for the NEX acquisition (located on SEC EDGAR, not opened). The comparison table of the three
order-matching systems at p. 9 of the NY Fed FXC *1991 Annual Report* — the PDF the New York Fed
serves stops at eight pages, and that table, drawn up in November 1991, is the single most promising
unretrieved document for this argument. Any EBS or Reuters rulebook from the 1990s. Any Reuters,
Thomson Reuters, Refinitiv or LSEG corporate filing. The Amazon Prime Video licensing page (carried
over from the chapter, not re-fetched).

---

## 10. Citation corrections and the closed sourcing caveat, 2026-08-11

A re-verification pass ran after this card was written. It closes the caveat in §8 and
corrects three fee attributions. Recorded here rather than folded in above, so the audit
trail holds.

### 10.1 The sourcing caveat is closed

§8 warned that the LSEG rulebooks were retrieved by an assisting run whose URLs were not
recorded, and that the SEF material could not be cited until re-sourced. The URLs are now
recorded, and each returns HTTP 200 to a bare request with no User-Agent, cookie jar, referer
or auth:

- **UK MTF Rule Book** v1.2, eff. 1 Dec 2025, 47pp — `thesource.lseg.com/TheSource/getfile/download/b8ed9314-1e93-4ea8-8f3d-6dd1e84455b1`
- **UK MTF Rule Book** v1.1, eff. 5 Feb 2025 — `lseg.com/content/dam/lseg/en_us/documents/fx/lseg-fx-uk-mtf-rulebook.pdf`
- **EU MTF Rule Book** v3.2, eff. 1 Dec 2025 — `thesource.lseg.com/TheSource/getfile/download/e7abafc2-9c41-4ce9-b561-4e526828b203`
- **SEF Rulebook** v4.1, eff. 11 Aug 2026, 95pp — `lseg.com/content/dam/fx/en_us/documents/sef/lseg-fx-sef-rulebook.pdf`
- **FX Global Code**, updated Dec 2024, 84pp — `globalfxc.org/uploads/fx_global.pdf`

**The SEF material is citable**, which matters because it carries this card's best finding.

Two retrieval notes. The v1.2 URL **rejects HEAD** — a HEAD redirects to
`/thesource/Error/NotFound` and reads as a dead link, while a GET returns 1,561,961 bytes.
And `getfile/index/<uuid>` serves an HTML interstitial; `getfile/download/<uuid>` serves the
bytes.

**On the "Sensitivity: Confidential" footer.** It is boilerplate that survived publication,
not an access control, and quoting the rulebook is safe. The document contradicts its own
legend at **Rule 1.1.2, p. 13** — "This Rule Book is available on the LSEG FX MTF website" —
and **Rule 1.1.3** names the genuinely non-public document: "Documents that are not available
publicly, for example, the LSEG FX UK MTF Supplementary Annex, can be accessed via MyAccount."
Do not quote the Supplementary Annex; nobody here has it.

A diff of v1.1 against v1.2 found every clause quoted in this card **word-identical** — 1.1.4,
3.1.5, 7.3.1–7.3.3, 7.4.1, 7.5.6, 8.1.1, 8.2.2, 5.8.1. Cite v1.2; nothing in the argument
moves.

### 10.2 One clause v1.2 adds, which sharpens §5.4

**Rule 5.1.4**: "LSEG shall endeavour to provide prior written notice of any actions taken
under Sections 5.1.2 or 5.1.3 to the extent it is reasonably able to."

This refines the finding rather than overturning it. Withholding the reason still holds by
omission rather than by stated policy, but the omission is not total — there is an endeavour
to give notice, qualified twice. Notice that an action was taken is not a reason for it, and
the chapter should claim exactly that much.

### 10.3 Three fee figures, correctly attributed

| Figure | Actually from | Correction |
|---|---|---|
| $0.10–$0.55 per million, aggressor-pays | **LSEG FX EU MTF**, operator FRTSIL. *Forwards Matching Rate Card* v5.0, 11 Aug 2026 | Not a UK MTF fee. "Fee per Aggressor $M," five marginal tiers, and **"There are no fees for Market Making"** — aggressor pays, maker free |
| $10.00 per USD million, spot | *FXall RFQ Fee Schedule* v1.4, §I.A.4.a, p. 3 | **Off-venue by its own document.** §II.A.2, p. 6: "Spot instruments are not provided on the LSEG MTF or LSEG UK MTF and are considered 'off-venue'." Do not call it a venue fee |
| $10,005 per month, co-location | *LSEG FX Transactions — Connectivity Options* v2.1 | Cross-venue document, not UK-MTF-specific |

The off-venue figure is arguably the *stronger* evidence for the pricing capacity, since it
shows the operator pricing execution where no rulebook compels it to publish anything. It
simply cannot be labelled a venue fee. The fee schedule also **contradicts itself on its
effective date** (cover 1 Jan 2026; introduction "1March2025") — cite the cover, footnote the
discrepancy.

The rulebook's own fee text is one delegating sentence, **Rule 5.8.1, p. 30**. The clause
carrying argumentative weight is **Rule 8.2.2, p. 37**: "As consideration for this access, the
Participant will pay any Platform fees (if applicable) to the relevant LSEG Affiliate, abide
by these Rules and contribute to the level of trading activity on the Platform." Fee as the
price of access, in the operator's own words, needing no rate card at all.

### 10.4 A caveat on the FX Global Code

At printed p. 3 the Code lists five GFXC Reports, including "The Role of Disclosure and
Transparency on Anonymous E-Trading Platform," and states they "are not part of the Code or
the Statement of Commitment." Nothing resting on those reports may be cited as Code text.
