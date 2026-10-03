# Part 3 — Decision markets as decision experience design: Outline

<!-- Claude-drafted outline. First version 2026-10-03 (cloud session, abstract level). Revised 2026-10-03 after
the local deep-research run. Nothing here is author text.
Every claim carries a status flag:
  [checked]   I opened the source and confirmed the quotation or number (see literature/audit/AUDIT_00.md)
  [full]      a facet agent read the full text and gives a locator; not re-checked by me
  [abstract]  read at abstract level only
  [verify]    lead with no primary source opened; cannot enter a draft
  [none]      no source located; inference or open question
Nothing flagged [abstract], [verify] or [none] may be copied into a draft. [full] claims need the citation
audit before print. ARGUMENT_MAP.md indexes the Hanson, Mansour and counter-case arguments. -->

**Working title.** *Decision Experience Design, Part 3: What a Prediction Market Asks You to Do*

**Thesis note (2026-10-03).** Read section (b): the target is sports betting dressed as decision markets.

**Form.** Substack essay in the register of the live Part 1: author-date APA, headed sections, falsifiable
propositions and limitations at the end. Target length 4,000 to 6,000 words.

---

## (a) Thesis

Prediction markets exist to produce a probability. The person who wants that probability must still open a
trading interface, read a price, and place a bet. The essay argues that this gap between what the market
computes and what the interface asks of the user is a decision experience design failure, and that Part 1's
and Part 2's criteria locate it: the interface requires a trading skill the decision does not need, gives the
user no scaffold toward the skill the decision does need, and borrows the form of a betting product.

The altitude follows the repo rule. The essay is modest about what is shown (no experiment measures how lay
users read Polymarket or Kalshi prices) and confident about the design claim.

## (b) Author ruling (2026-10-03): the target is sports betting dressed as decision markets

The author settled the fork. Kalshi and Polymarket present themselves as prediction and decision markets, and
the product is sports betting in that dress. The design failure is the dress: the decision-market frame
(information, forecasting, a price that guides a choice) licenses an interface built for betting, and the user
who wants a probability gets a bet slip.

Consequences for the plan:
1. Section 1 states the promise only to set up the gap. Facets A and C become the contrast, not the target.
2. Section 2 carries the volume mix, which now verifies. Pew reports sports at 80% of Kalshi's volume and 39%
   of Polymarket's from July 2024 to April 2026, measured as notional taker volume [checked]. The Ninth
   Circuit states that over 90% of Kalshi's 2025 trades and 95% of its revenue were sports related [checked;
   the court's record citation is not traced]. Mansour himself says "95% of the volume on sports" for late
   2025 [full, facet M]. For Polymarket, facet D's run on the platform's own data gives 65.7% on an
   undocumented volume unit [full], so the essay should write "two fifths to two thirds".
3. Section 5 (the betting form) is the spine. It stays an analogy argument: no study measures user behaviour
   against an interface feature on either platform [gap search logged, facet B].
4. Part 3 argues design, not accuracy. Calibration findings (section (d)) stay in as limits.
5. The regulatory dress is now a sourced section (facet L). Kalshi's own 2024 appellate brief calls a sports
   contract the "classic example" of gaming and says game contracts "are unlikely to serve any 'commercial or
   hedging interest'" [checked]; its 2025 sports self-certifications place the risk-mitigation analysis in
   confidential appendices [checked]. Facts here still move quickly: three circuits have ruled (Third for
   Kalshi, Ninth and Sixth against) and the Fourth is pending [full].
6. Two positions must be stated at full strength before the essay answers them: Hanson's (there is no
   probability without the trade; the missing piece is a funder) and Mansour's (an exchange is not a
   sportsbook; the chart is the product). See `ARGUMENT_MAP.md`.

## (c) Section plan

1. The promise. Markets as forecasting by aggregation (Wolfers and Zitzewitz 2004; Arrow et al. 2008) [full].
   Why a price is only sometimes a probability: Manski shows a price of 0.75 fits mean belief anywhere from
   0.5625 to 0.935 and ends by recommending direct elicitation [full]; Wolfers and Zitzewitz (2006) reply
   that prices sit near mean belief under plausible risk aversion [full]; Gjerstad's version of that reply
   was not obtained [abstract]. Hanson's design assumes a consumer who reads the price and does not trade,
   and a sponsor who pays for it [full, facet H]. Backward hook to Part 1: the unit of design is the
   decision, not the screen.
2. What the product is. The volume mix (see (b)2). How the platforms name themselves: App Store titles
   "Kalshi: Trade Football & more" and "Polymarket: Trade Live Sports"; both offer parlays as "Combos"
   [full, facet D]. Kalshi "advertises itself as 'the first app for legal sports betting in all 50 states'"
   [checked, Ninth Circuit].
3. What the interface asks. A trade, a position size, fee and spread exposure. Kalshi's "Quick Order" is a
   market order sized in dollars or contracts; Polymarket shows the bid–ask midpoint and the buyer pays the
   ask [full, facet D]. On Kalshi, makers averaged −9.64% per contract and takers −31.46% (Bürgi, Deng and
   Whelan 2026) [checked], so the default order type decides who pays. The default on a fresh install,
   streaks and share buttons need a logged-in view [none].
4. Reading a price. Cents on the dollar as a probability. Format and numeracy interact: Gigerenzer and
   Hoffrage (1995) [full]; Peters et al. (2006) and McDowell and Jacobs (2017) [abstract]; the Zhu and Feldman
   (2023) replication of Peters holds for three of four effects [full]. Probability-of-precipitation
   misreading traces to a missing reference class [full, C2]. Displayed win probabilities confuse readers
   and about one in ten mistake them for vote share (Westwood, Messing and Lelkes 2020) [full]. One study
   now covers Kalshi's own display: Sah et al. (2026, arXiv; 360 Reddit posts, qualitative) find users
   struggle with the charts [full]. No experiment tests lay reading of a cents price [none; gap search
   logged, facet C]. State the gap; do not fill it.
5. The betting form. Rockloff et al. (2026) report 23% fewer bets, 39% less spending and 67% fewer short-term
   harms when bettors opt out of all direct marketing (email, text and push) [checked]. The analysed sample
   is 227 of 405 enrolled and the authors call the analysis exploratory [checked], so the essay must not
   present it as a notification experiment or as confirmatory. Chapkovski et al. (2026) attribute 70% of
   the gamification gap in trading activity to self-selection [abstract; full text not obtained]. Kalda et
   al. (2021, working paper) find the smartphone effect is as strong for assets the apps do not feature and
   conclude nudges "do not drive" it; they could not observe the app displays [full]. Dark patterns are
   measured in shopping (Mathur et al. 2019 [full]; Luguri and Strahilevitz 2021 [partial]) and only
   catalogued in gambling (McGarrigle et al. 2026, n = 16 sources) [full]. A CFTC letter announced on
   2026-08-07 says the "American" odds format "is likely to mislead market participants", and Kalshi removed
   it on 2026-08-31
   [full, facet D].
6. Whether anyone learns. Plain outcome feedback teaches little; apparent learning by trading is two to four
   times higher before adjusting for attrition (Seru, Shumway and Stoffman 2010) [full]. Longshot losses on
   Polymarket persist across experience levels (Cardozo and Rivero-Wildemauwe 2026) [full]. The one
   documented calibration gain came from training, not trading (Mellers et al. 2014) [full]. Link to Part 1:
   the competence is algorithmacy, which the interface does not scaffold.
7. Using the price in a decision. Corporate markets: Cowgill and Zitzewitz's 25% accuracy gain is the Ford
   comparison only, at p = 0.104 [full]. Managers forgo 37% of payoff by distrusting the market (Choo, Kaplan
   and Zultan 2022) [full]. Futarchy and decision markets remain designs; Hanson's own requirements list is
   the test [full, facet H]. Fed staff find Kalshi's rate forecasts match the New York Fed survey (Diercks,
   Katz and Wright 2026) [full], which is the best case for the price as a public good. The claim that
   numeracy does not moderate crowd-advice use (Fiedler et al. 2019) is withdrawn: it is not in the abstract
   and the full text was not obtained [verify].
8. Resolution and rules. Kalshi resolves from listed sources at its own discretion; Polymarket resolves
   through UMA token-holder votes [full, facet D]. The Khamenei market: the death clause was in Kalshi's
   certification of 2025-05-15, before trading; what followed in March 2026 was a broader rulebook provision
   [full]. The earlier lead "a rule written afterward" was wrong. The 1,150 disputed markets figure is
   third-hand [verify].
9. The regulatory dress. See (b)5 and facet L. The 2024 CFTC wrote that gaming contracts on its markets
   "avoid these legal regimes and protections" [full]; the 2026 proposal demotes hedging to "a significant factor" and adds
   "information aggregation" to the public-interest test [full]. Macey and Enriques (2026) defend the markets on
   information alone and grant that hedging use is theoretical [full].
10. What a decision market would look like by the Part 1 criteria. Declared operating envelope for the price,
    scaffolding toward steering skill, counter-delegation, structural refusal, bounded outputs. Hanson's two
    funders (a sponsor, or a decision-maker bound to the price) belong here as the design he specified and
    the platforms did not build [full]. Each is a proposition a test can falsify.
11. Limitations and propositions. No field study links a price to a decision and its outcome; no study of
    harm among users of either platform; the platform calibration papers are working papers or preprints;
    the cross-market subsidy claim (sports volume improves other prices) is untested.

## (d) Evidence that cuts against the thesis

Report these in the essay, not around it. Full treatment in `literature/facets/X_counter_case.md`.
- Sports is the best-calibrated category on Polymarket: longshot return +2.43% [−0.93, 5.79] against losses
  in crypto and politics (Cardozo and Rivero-Wildemauwe 2026) [checked].
- The exchange form differs from a sportsbook for the user: bookmaker overround 25.63% against exchange
  commission of at most 5% of winnings on Betfair (Smith, Paton and Vaughan Williams 2006) [full]. Whether
  Kalshi restricts no winning accounts is not verified [none].
- The price has a public life among non-traders (Diercks et al. 2026) [full].
- Median wash trading on Polymarket is about 1% (Dubach 2026) [full].
- Hanson defends sports betting and has not called either platform a disguise [full, facet H].
- Rasooly and Rozzi's 60-day manipulation persistence ran on a play-money platform [full]; it does not
  transfer without that caveat.

## (e) Jargon table

| Term | Treatment |
| --- | --- |
| decision experience design (DXD) | Kept; defined in Part 1 |
| algorithmacy | Kept; public construct, glossed on first use |
| decision market | Defined on first use, in Hanson's sense: markets conditional on a decision, whose price gap estimates the decision's effect |
| event contract, swap | Defined on first use if section 9 stays |
| implied probability, vig, overround, maker, taker | Defined on first use, only where used |
| ALC properties, Φ, IIT | Excluded from public prose per project rules |

## (f) Open questions for the author

1. Whether the essay answers Hanson on his ground (the missing funder) or holds to the interface. The
   evidence supports both; the two make different essays.
2. Whether to use Kalshi's 2024 brief against its 2025 sports listings. It is the sharpest fact in the
   record, and it is Kalshi's legal position at a date, not a statement by Mansour.
3. How to word the Polymarket share: Pew's 39% or the range.
4. Whether section 9 (the regulatory dress) stays, given three circuit rulings in six months and a fourth
   pending.
5. Whether Part 1's "awareness without agency" line needs the correction Part 2 already flags (Eslami et
   al. 2015).
6. Whether the closing offers design proposals or only falsifiable propositions.
