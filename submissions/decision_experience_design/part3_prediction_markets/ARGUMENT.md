# Part 3 — The argument, premise by premise

<!-- Claude-drafted evidence document, 2026-10-03. Not the essay and not author text. The premises P1–P8 and C
are the author's argument as stated on 2026-10-03; everything under each premise is assembled from the facets
in literature/facets/ (first run: A, B, C, D, H, L, M, X; second run: F, K, T, R).
Flags: [checked] I opened the source and confirmed the quotation or number (literature/audit/AUDIT_00.md,
AUDIT_01.md). [facet] a facet agent read it and gives a locator; not re-checked by me. [inference] no source
says it. Nothing flagged [facet] may be quoted in a draft before the citation audit covers it. -->

**The argument as the author stated it.** Prediction markets are poor decision experience design. They show
the dark pattern familiar from user experience design, and they show it the way dark patterns usually arise:
through designs meant to help. Hanson holds that markets tend toward the truth; Mansour holds that a
structured exchange beats a sportsbook. The obvious pitfall is gambling. The subtler one is structural: a
decision, unlike a choice, has to consider coordination through a third party, and a bet is a plain win or
lose between two sides. Foreign-exchange participants get what they need while coordinating through the
market; only speculators win or lose. Presenting the two-sided bet as three-party coordination is the dark
pattern.

**Verdict in one paragraph.** Five premises hold, two hold only in a narrower form, and one fails as worded
and needs the author's decision. The Forex contrast (P6) survives only as hedger-with-speculator against
speculator-with-speculator. "Prediction markets are really dyads" (P4, P8) contradicts the author's own
ALGOCON argument, which classes a posted price as a triad; it holds if the essay separates the price, which
is jointly set, from the bet, which factors into two win-or-lose outcomes. The conclusion (C) can then take
one of two forms, set out at the end.

---

## P1. Dark patterns usually begin as well-meant design; the harm is in the structure

**Status: holds with a stated limit.**

- The field's definition is moving from intent to effect. Mathur, Kshirsagar and Mayer (2021) count 19
  definitions, of which "eight definitions do not address the role of user interface designers" [checked]
  (`mathur2021dark`, §2.1). The EU Digital Services Act (recital 67: "either on purpose or in effect"),
  California's regulations ("intent... is not determinative") and Gray et al.'s 2024 ontology ("regardless
  of the designer's intent") take the effect side [facet K; the DSA text was not reachable for my check].
- Gray et al. (2018), which Part 1 cites for an intent-based definition, also poses the author's question:
  "A design decision may have been made with good intentions for a specific audience, but resulted in
  manipulative outcomes when exposed to a broader audience" [checked] (`gray2018dark`, p. 9). The same
  paper says "many of these dark patterns result from explicit, purposeful design intentions" [checked]
  (p. 3). "Subvert user intent", Part 1's phrase, does not appear in it [checked].
- The Like button: its builders say they meant well. Pearlman's 2009 launch note frames it as reducing
  redundant comments; Rosenstein speaks of "best of intentions... unintended, negative consequences"
  [facet K, journalism tier]. Facebook had already sold "social actions" to advertisers fifteen months
  before launch [facet K]. The evidence supports "the builders say they meant well", not "the firm meant
  well".
- Personalised ads: Brin and Page (1998, Appendix A) predicted that "advertising funded search engines will
  be inherently biased towards the advertisers and away from the needs of the consumers" [facet K]. They
  named the hazard before building the business.

**Limits.** "Dark patterns rarely occur because someone is trying to hurt people" is an empirical claim about
designers that no source measures [facet K]. No source calls a market or product structure, as opposed to
an interface element, a dark pattern; Part 3 would be the first and should say so [facet K, gap search].
Two 2025–26 papers state near versions of the thesis and were read only as abstracts: Packin and Rabinovitz
(2026, *Science*) and Johnson and Chan (2025, *Addiction*).

**Decision for the author.** Part 3 changes the definition Part 1 published. The honest route: cite Gray et
al. (2018) for the question and the regulators for the effect-based answer, and say Part 3 adopts it.

## P2. Hanson and Mansour state the good the design aims at

**Status: holds, with both positions corrected.**

- Hanson does not claim markets tend toward right decisions as a brute fact. He claims accuracy relative to
  rival institutions, under conditions: a sponsor or a bound decision-maker, and insiders trading (facet H,
  claims 6, 9–11). On current platform topics: "I don't have great confidence in that" (claim 30) [facet].
- Mansour does not say "sloppy bets". His contrast is "an open, fair, liquid marketplace" against "a closed
  forum system against the house" (`mansour2026raskin`) [facet M].
- The two disagree with each other on who pays for the information, whether hedging matters, and who should
  trade [facet R]. The essay can use the disagreement: Hanson's design has a funder and Mansour's product
  has none.

## P3. Gambling harm is the obvious pitfall and not the argument

**Status: holds.** No study measures harm among users of either platform [facets B, X]. The essay concedes
the point is unmeasured and moves to structure.

## P4. A decision, unlike a choice, has to consider coordination through a third party

**Status: holds as a new definition; the series does not yet contain it.**

- Parts 1 and 2 contrast disciplines (choice architecture against decision experience design); neither
  defines "decision" against "choice" [facet T]. The distinction is new to Part 3 and should be marked as a
  sharpening of Part 1.
- Part 2 defines the triad as a third party that "reads both human parties and commits an outcome binding on
  both". An exchange's matching engine does that. So the premise cannot rest on Part 2's definition alone.
- Part 2 grounds the designer's obligation in "mandatory participation" [checked]. Nobody must use Kalshi.
  Part 3 has to draw on Part 1's design principles instead [facet T].

## P5. A prediction-market trade is zero-sum: a plain win or lose

**Status: holds in a corrected form.** The trade is negative-sum among traders: on Kalshi, makers averaged
−9.64% per contract and takers −31.46% [checked] (`burgi2026makers`). Stout (1999, pp. 742–745) calls
disagreement trading between speculators a wager, zero-sum and then negative-sum [facet F]. Mansour concedes
the structure: "When somebody loses on Kalshi, they're losing it to someone else" [facet R].

**Reply to answer (Hanson).** The price is a positive by-product for people who do not trade; Fed staff use
Kalshi's rate prices (`diercks2026kalshi`) [facet X]. The corrected premise: negative-sum for the bettors,
with a public benefit for readers of the price. **Answer available:** stakes are not what make the number
good. Play money matched real money on NFL games, and the same traders' stated beliefs scored 0.210 on the
Brier measure against 0.227 for prices, a difference that is not significant (p = 0.152), while beliefs and
prices combined beat prices alone (p = 0.004) [checked] (`dana2019are`, Table 1). A design could produce the number without the bet.

## P6. In Forex the ordinary participant gets what they need; only speculators win or lose

**Status: fails as worded; a narrower form holds.**

- By volume, currency trading is financial. Trading with non-financial customers was 443 of 9,595 billion
  dollars a day in April 2025, or 4.6%, down from 13.4% in 2010 [checked] (`bis2025triennial`, Table 2). The
  BIS classifies counterparties, not motives.
- By head count, the ordinary retail currency trader loses: "between 74-89% of retail investor accounts lose
  money" (`esma2018cfd`) [facet F].
- By purpose, a hedging class exists and is small: about 3% of Euro currency futures positions and about
  38.5% of corn futures positions, as of 2026-09-29 (`cftc_cot_eurofx_20260929`, `cftc_cot_corn_20260929`)
  [facet F's computation; not rerun by me].
- The hedger pays for the service. Hicks calls the premium "the cost of the co-ordination achieved by
  forward trading" (`hicks1939value`, p. 139) [facet F, scanned copy].

**The form that holds.** Currency and grain markets contain an identifiable class whose position offsets an
exposure they already carry; the speculator is the third party that class needs. Two speculators trading
with each other are making a wager in those markets too. The comparison is hedger-with-speculator against
speculator-with-speculator, not Forex against Kalshi.

**Reply to answer (Mansour).** Speculators supply the liquidity hedgers need, as in grain. Working agrees
for grain: hedgers "prefer to use the exchange which has the largest volume of speculative trading"
(`working1953futures`, p. 319) [facet F]. **Answer available:** the defence presupposes a hedger. See P7.

## P7. Sports contracts have no participant with a need the market meets

**Status: holds, with one concession.**

- Kalshi's 2024 appellate brief: a contract on a sporting event is "the classic example" of gaming, and
  contracts relating to games "are unlikely to serve any 'commercial or hedging interest'" [checked]
  (`kalshi2024appelleebrief`, pp. 41, 45). This is Kalshi's legal position at a date, not Mansour's
  statement.
- The risk-mitigation analysis for the 2025 sports contracts "is included in Confidential Appendices C, D,
  and E" [checked] (`kalshi2025selfcert_title`, p. 2).
- Sports is most of the volume: 80% of Kalshi and 39% of Polymarket, July 2024 to April 2026 [checked]
  (`pew2026may`).
- The only documented sports-contract hedgers are three anecdotes from one local news report, read as a
  summary [facet F]. Bookmakers laying off risk on exchanges exists in UK documents and nobody measures it
  [facet F].

**Concession.** Recreation is a need. Two people who both want action on a game meet each other's need, and
Hanson files sports betting under entertainment (facet H, claim 15) [facet T]. The premise must read: no
participant has a need *of the kind the decision-market name promises*.

**Reply to answer (Hanson).** "Prediction markets... usually have few 'hedging' traders. However, this does
not prevent them from having informative prices" (`hanson2008insider`, §IV) [facet R]. If the test is a
hedger's need, his own design fails it. **Answer available:** let the reader of the price count as the party
with the need, as Hanson himself does. His legislature reads the estimate and votes (claim 5), and his
sponsor pays for it (claims 9–11). On the platforms that reader is bound to nothing and pays nothing.

## P8. The platforms present the two-sided bet as three-party coordination

**Status: holds as description; the word "dyad" needs care.**

- Mansour's own case is the presentation: traders contract with each other, the exchange takes a fee whoever
  wins, "the charts are really the key component of our experience" [facet M].
- The Ninth Circuit quotes that argument and calls it "distinctions without differences"; Kalshi "advertises
  itself as 'the first app for legal sports betting in all 50 states'" [checked] (`ca9_2026assad`). The
  court also records an affiliate, Kalshi Trading, acting "largely as a market maker" (p. 29 n. 5) [facet M;
  the archived help pages the court cites were not opened by anyone].
- A CFTC letter says the "American" odds format "is likely to mislead market participants", and Kalshi
  removed it [facet D].

**The difficulty.** The author's ALGOCON argument classes "a scoreboard, a vote tally or a posted price" as
"set jointly by both parties, read by both" [checked] (`submissions/triadic_reduction/ARGUMENT.md`, P39). A
market price is a triad by the lab's own criterion. Part 1 also says a costless exit collapses "an
irreducible triadic mediator back into a separable, manageable dyad" [checked], which supports the
conclusion and cannot then be cited for the exchange being a triad.

**The repair.** Separate two stages. The price is jointly set: that stage is three-party. The settlement
relays the result of a game to two accounts, and each outcome depends on the event alone: that stage factors
into two win-or-lose results. The dyad is the bet, not the market [facet T].

**Replies to answer (Mansour).** The exchange is the third party, and the form differs for the user:
exchange commission of at most 5% of winnings against bookmaker overround of 25.63% on Betfair
(`smith2006p2p`) [facet X]. The Third Circuit ruled for Kalshi [facet L]. **Answers available:** the maker
and taker gap shows the interface decides who pays; the affiliate market maker puts a house-like counterparty
back; the Ninth Circuit's phrase is a holding about a statutory word, not a design finding, and the essay
should not lean on it as one [facet R].

---

## C. The conclusion, in two forms

**Form 1: a bet presented as coordination (the author's wording, repaired).** The market is three-party at
the price and two-party at the bet. The platforms show the first and sell the second. This keeps the series'
vocabulary and requires the two-stage split, the concession that two currency speculators are also making a
bet, and the definition of decision against choice.

**Form 2: a wager presented as a decision instrument (facet T's recommendation).** Drop the count of parties
in public prose and test the trade at the moment of the match: a trade is coordination when each side leaves
with what it came for, whatever happens next; it is a bet when what each side came for is decided later by
an event neither controls, and only one of them can have it. The dark pattern is the presentation of the
second as the first. This form rests on sources already read (Stout's indemnity test; Lockhart's "extant
versus created risk"; Kalshi's 2024 brief) and does not collide with the ALGOCON talk. A venue that
presented itself plainly as betting would escape it.

**What both forms share.** Hanson's sponsor-funded decision market passes either test: a sponsor with a
decision to make, traders, and a market whose price binds the decision. The retail exchange removed the
sponsor and kept the name. Hanson's "missing funder" and the essay's missing coordination are the same gap
[facet T, inference], so the essay can agree with his design and argue that the platforms did not build it.

**The three replies either form must answer** [facet R]:
1. Hanson: there is no probability without the trade. Answer: P5 (stakes are not what make the number good).
2. Mansour: the exchange is the third party. Answer: P8 (the two-stage split; maker and taker returns; the
   affiliate market maker).
3. Hanson: a hedging standard misjudges an information market. Answer: P7 (count the reader of the price as
   the party with the need, and show the platforms bind that reader to nothing).

## What the essay must concede

1. Sports is the best-calibrated category on Polymarket (`cardozo2026flb`) [checked].
2. The exchange form does differ from a sportsbook on price [facet X].
3. Two currency speculators are making a bet; the Forex contrast is about hedgers.
4. Mansour's grain analogy is right about grain.
5. Recreation is a need, and Hanson defends sports betting and has not called either platform a disguise.
6. The matching engine reads both sides and binds both; a market price is jointly set.
7. Part 2's mandatory-participation argument does not apply to a voluntary venue.
8. The decision-against-choice definition and the effect-based reading of "dark pattern" are new to Part 3.
9. Nothing from the lab's Boolean results is evidence about a market.

## Not yet supported

- That designers of these platforms meant well. Only their own statements bear on it.
- The share of Kalshi volume taken by its affiliate market maker.
- Any measured hedging use of sports, election or macro event contracts.
- Any experiment on how lay users read a cents price as a probability (one qualitative study exists:
  `sah2026visualizations`).
