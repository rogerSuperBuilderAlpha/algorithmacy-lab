# X. The counter-case: evidence that favours the platforms

*Facet X of the Decision Experience Design (DXD) Part 3 literature base. Agent-drafted on 2026-10-03 as opposing counsel to the author's thesis. The author has not reviewed it, and none of the text below is the author's.*

**The thesis under attack (author ruling, 2026-10-03).** Kalshi and Polymarket present as prediction and decision markets and are sports betting in that dress; the dress is the design failure. The interface asks for a trade where a decision-maker needs a probability, demands a skill the decision does not need, offers no scaffold, and borrows the form of a betting product.

**What this facet does.** I built the strongest case against that thesis that the sources will bear, along seven lines the brief set, and rated each line by what the evidence supports. Sibling seats cover Hanson (H), Mansour and Kalshi's own arguments (M), the law (L) and platform facts (D); I do not repeat them, and where a counter-argument needs a platform fact I say so and leave it to D.

**Read-status legend.** *Full text* = I opened the whole paper this session and read the abstract, the result tables and the conclusion, plus the sections the entry cites; a locator (section, table or page) accompanies every number. *Abstract* = I read a database abstract (Crossref, OpenAlex, Semantic Scholar or Consensus) and verified the DOI against Crossref or OpenAlex; nothing beyond the abstract may be quoted. *Metadata* = DOI and bibliographic record verified; content not read. *Web* = a web page opened this session (primary or secondary, as marked). Preprints and working papers are flagged. Where I read a working-paper version of a published article, the entry says which version I read.

**Network this session.** api.crossref.org, api.openalex.org, arxiv.org, nber.org, federalreserve.gov, api.semanticscholar.org, repository mirrors (NTU IRep, UEA eprints, Birmingham RePEc, Swansea Cronfa, MDPI, Cambridge Core), karlwhelan.com, biz.uiowa.edu, pewresearch.org and gamblingcommission.gov.uk answered. doi.org, papers.ssrn.com, web.archive.org, onlinelibrary.wiley.com, sciencedirect.com and tandfonline.com returned 403.

---

## (a) Search log

All requests ran on 2026-10-03.

| # | Source | Exact query / request | Result | Used for |
|---|---|---|---|---|
| 1 | Crossref `query.bibliographic` | 24 title-and-author strings for the brief's named leads (Smith, Paton and Vaughan Williams 2006 and 2009; Franck, Verbeek and Nüesch 2010 and 2013; Croxson and Reade; Kyle 1985; Black 1986; Hanson and Oprea; Atanasov et al. 2017; Dana et al.; Servan-Schreiber et al.; Rosenbloom and Notz; Erikson and Wlezien; Cowgill and Zitzewitz 2015; Snowberg, Wolfers and Zitzewitz 2007; Wolfers and Zitzewitz 2009; Buhagiar, Cortis and Newall; Westwood, Messing and Lelkes; Rothschild 2009; Mellers et al. 2014; Baker et al.; Moshrefi; Newall and Cortis) | 23 resolved; Servan-Schreiber hit HTTP 429, resolved on retry (row 7) | All lines |
| 2 | arxiv.org | PDF download of 2609.12878, 2602.19520, 2604.24366, 2608.16814, 2607.14430 | 5 PDFs | Lines 2, 6, 7 |
| 3 | OpenAlex `search` | `bookmaker account restriction winning bettors closure stake limits`; `bookmakers restrict successful bettors accounts`; `betting exchange versus bookmaker odds accuracy Betfair efficiency`; `prediction market participants gambling harm problem gambling survey event contracts`; `Kalshi gambling harm users`; `prediction market participation improves calibration probabilistic reasoning learning traders`; `prediction markets classroom students learning probability`; `journalists use prediction market prices media coverage election forecasts markets`; `Kalshi macroeconomic prediction markets forecasts Federal Reserve`; `noise traders liquidity prediction markets accuracy manipulation subsidize`; `favorite longshot bias betting exchange Betfair compared bookmakers`; `prediction market real money play money accuracy comparison` | Surfaced Torrance et al. 2026, Grant et al. 2018, Diercks et al. 2026, Brown and Yang 2019 (via Consensus), Casadesus-Masanell and Campbell 2019. No study of harm among event-contract users; no study of calibration learning from market participation | Lines 1, 3, 4, 6, 7 |
| 4 | Semantic Scholar Graph API | `openAccessPdf` and `abstract` for 19 DOIs | OA locations for Smith et al. 2006, Smith et al. 2009, Mellers et al. 2014, Reade and Vaughan Williams 2019, Buhagiar et al. 2018 (403 on fetch), Moshrefi 2026 (arXiv) | All lines |
| 5 | OpenAlex `works/doi:` | Abstracts and OA locations for 13 DOIs (Kyle, Black, Franck 2010, Croxson and Reade, Smith 2006, Cowgill and Zitzewitz 2015, Erikson and Wlezien, Rosenbloom and Notz, Brown and Yang, Casadesus-Masanell, Grant, Torrance, Buhagiar) | Kyle 1985 and Franck 2010 have no OpenAlex abstract | Lines 1, 3, 5 |
| 6 | Consensus `search` | `prediction market users problem gambling severity survey event contracts Kalshi Polymarket harm` | 20 hits; none measures harm among event-contract users; Johnson et al. 2025 (letter), Dai et al. 2026 (settlement manipulation), Cox et al. 2020 and Lee et al. 2023 (trading and problem gambling) | Line 6 |
| 7 | Consensus `search` | `does participating in prediction markets or forecasting tournaments improve calibration of probability judgments over time` | 19 hits; all tournament or training studies (Mellers 2014; Chang 2016; Moore 2016; Hauenstein 2024); none measures calibration change from market trading | Line 7 |
| 8 | Consensus `search` | `bookmakers restrict or close accounts of winning bettors stake limits exchange betting` | 20 hits; Franck et al. 2013 (arbitrage), Grant et al. 2018, Casadesus-Masanell and Campbell 2019; no quantitative study of restriction rates | Line 1 |
| 9 | Crossref retry | Servan-Schreiber et al. 2004; Levitt 2004 (Economic Journal); Christiansen 2012; Casadesus-Masanell and Campbell | All resolved | Lines 1, 5 |
| 10 | WebSearch | `Bürgi Deng Whelan "Makers and takers" Kalshi CESifo working paper pdf` | Author copy at karlwhelan.com; CESifo WP 12122; CEPR DP 20631; UCD WP 2025/19 | Line 2 |
| 11 | WebSearch | `bookmakers restricting winning accounts survey Horserace Bettors Forum Gambling Commission minimum bet liability` and `Gambling Commission "643,779" accounts restricted 2024` | Led to the Gambling Commission blog post of 23 July 2025 (primary; row 14) | Line 1 |
| 12 | WebSearch | `Pew Research Center 2026 prediction markets Americans use Kalshi Polymarket survey` | Two Pew short reads (rows 15, 16); several opinion polls (NBC, Ipsos, Paradigm, Navigator) not opened | Lines 4, 6 |
| 13 | WebSearch | `Croxson Reade "Information and Efficiency: Goal Arrival in Soccer Betting" pdf` | Birmingham Discussion Paper 11-01 PDF | Line 1 |
| 14 | WebFetch | gamblingcommission.gov.uk/blog/post/commercial-restrictions-by-betting-operators | Read (primary) | Line 1 |
| 15 | WebFetch | pewresearch.org/short-reads/2026/07/22/what-we-know-about-the-typical-polymarket-user/ | Read (secondary analysis of Polymarket API data) | Lines 4, 6 |
| 16 | WebFetch | pewresearch.org/short-reads/2026/09/23/… (volume doubled May to July) | Read (secondary; data from The Block) | Volume context |
| 17 | Fetch failures | SSRN (Krause 2026; Franck 2010 SSRN copy), ScienceDirect (Buhagiar et al. 2018), Taylor & Francis (Torrance; later obtained from Swansea Cronfa), Wiley (Franck et al. 2011), AEA (Wolfers and Zitzewitz 2004), JSTOR (Erikson and Wlezien), UPenn and UT Austin author pages (Atanasov 2017; Erikson and Wlezien) | 403 or HTML shells | Noted in entries |

---

## (b) Entries

Grouped by the line they serve. Bib keys are in `X_counter_case.bib`.

### Line 1. Exchange versus sportsbook

**smith2006market** — Smith, M. A., Paton, D., & Vaughan Williams, L. (2006). Market efficiency in person-to-person betting. *Economica*, 73(292), 673–689. doi:10.1111/j.1468-0335.2006.00518.x.
- *Read status:* full text (NTU IRep post-print dated August 2005, 6,990 words).
- *What it shows:* on 700 UK horse races in 2002, matched between bookmakers and Betfair, the bookmakers' overround "averages at 25.63% in our 700 race sample (based on mean bookmaker prices)" while Betfair's commission "is normally set at a maximum of 5% of winnings" (section 4). Shin's insider measure z, the paper's bias statistic, is 2.17% for mean bookmaker fixed odds, 1.19% for the best (outlier) bookmaker odds and 0.9% for the exchange, and the formal tests "confirm that the estimated bias in the exchange data is significantly lower than both the mean and outlier fixed odds data" (section 6, Table 3 and Table 8). The authors read the exchange's lower bias as support for a transaction-cost explanation of the favourite-longshot bias.
- *Bearing:* **supports the counter-case.** The exchange form is a different product from a sportsbook for the user: a cost of at most 5% of winnings against a 25.63% notional margin, and less price bias. This is the precedent for Kalshi and Polymarket as order books.

**franck2010prediction** — Franck, E., Verbeek, E., & Nüesch, S. (2010). Prediction accuracy of different market structures — bookmakers versus a betting exchange. *International Journal of Forecasting*, 26(3), 448–459. doi:10.1016/j.ijforecast.2010.01.004.
- *Read status:* abstract (Consensus; DOI verified in Crossref). No OA copy found; SSRN and Wiley refused.
- *What it shows:* on 5,478 matches in the five major European football leagues over three seasons, "the betting exchange provides more accurate predictions of the same underlying event than bookmakers," and a strategy of backing outcomes where bookmakers quote higher odds than the exchange "generates above average and, in some cases, even positive returns."
- *Bearing:* **supports.** Same conclusion as Smith et al. in a second sport and country.

**croxson2014information** — Croxson, K., & Reade, J. J. (2014). Information and efficiency: goal arrival in soccer betting. *Economic Journal*, 124(575), 62–91. doi:10.1111/ecoj.12033.
- *Read status:* full text of the Birmingham Department of Economics Discussion Paper 11-01 (21 January 2011, 21,581 words), the working-paper version of the article.
- *What it shows:* using Betfair in-play order-book snapshots and 160 goals scored within five minutes of half-time (53 in the final minute), the authors find that "prices update so swiftly and completely that the news of a goal is fully digested by the time the break commences" (section 2) and that Betfair-implied probabilities "closely track those implied by the selected Poisson process" (section 5). Abstract: "On our evidence, prices update swiftly and fully."
- *Bearing:* **supports** the claim that an exchange price is an efficient estimate in-play, which is the hardest case for calibration.

**levitt2004why** — Levitt, S. D. (2004). Why are gambling markets organised so differently from financial markets? *Economic Journal*, 114(495), 223–246. doi:10.1111/j.1468-0297.2004.00207.x.
- *Read status:* full text of NBER Working Paper 9422 (December 2002, 11,841 words), the working-paper version, titled there "How do markets function? An empirical analysis of gambling on the National Football League."
- *What it shows:* sportsbooks do not match buyers and sellers; they "take large positions with respect to the outcome of game," set prices that exploit bettor biases and thereby "increase their gross profit margins by 20-30 percent over a price-setting policy that attempts to balance the amount of money on either side of the wager" (abstract; section 2). The commission is treated as fixed: "Commissions are virtually always 10 percent" (footnote 8), so "a bettor must win 52.4 percent of bets to make profit" (section 2). Levitt finds "little evidence that there exist bettors who are systematically able to beat the bookmaker" (abstract).
- *Bearing:* **supports** the structural contrast. A sportsbook is a dealer with a house position and a bias-exploiting price; an order-book exchange has neither by construction. My computation from Levitt's figures: at the standard −110 line on both sides, the implied probabilities sum to 1.0476, so a coin-flip bettor loses 4.55 cents per dollar staked. Compare the Kalshi taker fee below.

**gamblingcommission2025restrictions** — Rhodes, A. (2025, 23 July). Commercial restrictions by betting operators. Gambling Commission blog.
- *Read status:* web (primary regulator page).
- *What it shows:* from a data request to the largest online real-event betting operators in Great Britain covering calendar 2024: "From a total of 14,923,840 active customer accounts, operators reported 643,779 accounts restricted in some form – a rate of 4.31 per cent." Stake-factor reductions applied to 2.68% of active accounts, closures to 2.23%, withdrawal of betting facilities to 0.83%, market restrictions to 0.25%. Of stake-factored accounts, 22.41% were cut to 1% of normal stake or less and 36.22% to 1–9%. Restricted customers were in profit 46.78% of the time against 25.42% of all customers.
- *Bearing:* **supports.** Sportsbooks restrict winners at scale and the restricted are twice as likely to be in profit. Whether Kalshi and Polymarket restrict winning accounts is a platform fact for seat D; the counter-case needs it to be "no" for this point to bite.

**torrance2026difficult** — Torrance, J., Smith, J., Crawford, T., & Newall, P. (2026). 'It's so difficult that you have to be fully in control of your emotions…': how professional sports bettors succeed by using rational thinking to cope with uncertainty. *Addiction Research & Theory*. doi:10.1080/16066359.2026.2693272.
- *Read status:* full text (Swansea Cronfa author copy, 9,578 words). Five interviews; qualitative.
- *What it shows:* "Account restrictions and closures represented the most immediate challenge to sustained profitability." Participant 5 described "hundreds of UK accounts on each bookmaker" and said "UK bookmakers limit your accounts, and you can't get on"; Participant 2 said even Asian bookmakers "had 'brought in restrictions,' emphasizing that 'winners are not welcome anywhere'" (Main theme 2, subtheme 2.1).
- *Bearing:* **supports** the restriction point from the bettor's side. N = 5; illustrative only.

**grant2018new** — Grant, A., Oikonomidis, A., Bruce, A. C., & Johnson, J. E. V. (2018). New entry, strategic diversity and efficiency in soccer betting markets: the creation and suppression of arbitrage opportunities. *European Journal of Finance*. doi:10.1080/1351847x.2018.1443148.
- *Read status:* abstract (OpenAlex; Nottingham repository PDF returned an HTML shell).
- *What it shows:* bookmakers split into "position-takers," who "alter their odds infrequently, while actively restricting informed traders," and "book-balancers," who "place few restrictions on their customers"; 545 arbitrage portfolios existed but "the management practices of position-takers generally prevent these opportunities being exploited in practice."
- *Bearing:* **supports.** Restriction is a price-protection strategy of the dealer model.

**casadesusmasanell2019platform** — Casadesus-Masanell, R., & Campbell, N. (2019). Platform competition: Betfair and the UK market for sports betting. *Journal of Economics & Management Strategy*, 28(1), 29–40. doi:10.1111/jems.12310.
- *Read status:* abstract (OpenAlex).
- *What it shows:* Betfair and bookmakers "developed a highly complementary relationship that favored all parties."
- *Bearing:* **complicates** the counter-case. The exchange did not replace the sportsbook; the two coexisted, which weakens any claim that the exchange form is a cure.

**newall2021are** — Newall, P. W. S., & Cortis, D. (2021). Are sports bettors biased toward longshots, favorites, or both? A literature review. *Risks*, 9(1), 22. doi:10.3390/risks9010022.
- *Read status:* full text (MDPI PDF, 5,938 words).
- *What it shows:* the review defines the bookmaker margin as the excess of implied probabilities over 100% and works an example in which a bettor loses "€4 (4%) overall" at odds of 1.2 (section 2.1). It argues that bettors show both favourite and longshot bias depending on the number of outcomes. It contains no analysis of exchanges.
- *Bearing:* **background** for the margin definition only.

**burgi2026makers (fee passage)** — see Line 2 for the full entry. Kalshi's taker fee during the sample was "$0.07P(1 − P) times the number of contracts where p is the price in dollars, rounding the total up to the nearest cent"; makers paid nothing until April 2025; the rounded fee at 50 cents is "1.77% of the price" (section 3.3). My computation: 1.75 cents on a 50-cent stake is 3.5 cents per dollar staked for the taker on a one-way trade, against 4.55 cents per dollar for a −110 sportsbook line (Levitt). The gap in explicit cost is real but narrow for a taker at even odds; it widens toward the price extremes and is zero for makers in the sample period.

### Line 2. Sports contracts are informative and calibrated

**burgi2026makers** — Bürgi, C., Deng, W., & Whelan, K. (2026). Makers and takers: the economics of the Kalshi prediction market. CESifo Working Paper 12122; CEPR DP 20631; UCD WP 2025/19.
- *Read status:* full text (karlwhelan.com copy dated January 2026, 12,460 words). Working paper.
- *What it shows:* 46,282 Yes contracts in 12,403 events open at least 24 hours, 2021 to April 2025; 156,986 daily Yes prices, 313,972 purchased-contract prices. "Contract prices are informative and become more accurate as markets approach closing" (abstract). "Investors who buy contracts costing less than 10c lose over 60 percent of their money," contracts above 50c earn "a small positive rate of return," and "the average rate of return on Kalshi contracts is about minus 20%" (section 1). Makers' average return was −9.64% and takers' −31.46% (section 4). Volumes "increased substantially in January 2025 as it began taking bets on sporting events. Our results below are not sensitive to cutting the data off in December 2024 or to excluding the category containing sports bets" (section 2). Table 9 gives year-by-year price coefficients of 0.041, 0.023, 0.036, 0.048 and 0.021 for 2021–2025; the text calls this "some evidence that the bias in prices is diminishing over time." The conclusion: "their prices should not be interpreted as unbiased probability estimates" and the bias "mirrors the biases long documented in traditional betting markets where prices are set by bookmakers."
- *Bearing:* **cuts both ways.** For the counter-case: prices are informative and improve toward close. Against it: the platform-wide favourite-longshot bias, the −20% average per-contract return and the maker/taker gap are facts about an exchange with no house, so the exchange form alone does not remove the pattern the gambling literature documents.

**cardozo2026favorite** — Cardozo, M., & Rivero-Wildemauwe, J. I. (2026). The favorite–longshot bias in prediction markets: evidence from Polymarket. arXiv:2609.12878v1 (11 September 2026).
- *Read status:* full text (20,482 words). Preprint.
- *What it shows:* 588 million trades by 2.48 million wallets, November 2022 to March 2026. Sports is 16.1% of purchases and 36.8% of the $23.67 billion paid (Table 2). In Table 8, sports longshots (price below 10 cents) return +2.43% [−0.93, 5.79] with equal child-market weights and +18.11% [−74.68, 110.91] pooled; sports favourites (90 cents and above) return −0.230% [−0.285, −0.174] and +0.137% [−0.100, 0.373]. "Sports is the clearest counterexample: its longshot returns are positive under both methods" (section 4.1); "Sports remains closer to the equality line" (section 4.2). Platform-wide, longshots lose 19.3 cents per dollar pooled, 6.3 cents with equal weights, and gain 4.1 cents when grouped by parent event (abstract). Longshot losses "persist after substantial previous trading, across experience levels and ways of buying, in markets without reported fees" (section 8).
- *Bearing:* **supports the counter-case on sports** and **cuts against Line 7**: the largest category by listed markets shows no favourite-longshot bias, but experience does not cure the bias where it exists.

**le2026decomposing** — Le, N. A. (2026). Decomposing crowd wisdom: domain-specific calibration dynamics in prediction markets. arXiv:2602.19520v2 (4 August 2026).
- *Read status:* full text (12,862 words). Preprint.
- *What it shows:* 353 million trades on 429,000 binary contracts. On Kalshi, sports is 55,637 markets and 43.2 million trades against 4.9 million for politics (Table 2); on Polymarket, sports is 49.1 million trades against 45.7 million for politics (Table 3). Kalshi sports recalibration slopes run 1.10, 0.96, 0.90, 1.01, 1.05, 1.08 from 0–1 hour to 24–48 hours, 1.04 at 2 days to 1 week, 1.24 at 1 week to 1 month and 1.74 beyond a month (Table 4); politics runs 0.93–1.83. "Sports markets are close to calibrated at short-to-medium horizons (slopes 0.90–1.10 from 0 to 48 hours)" and on Polymarket "Sports is near-calibrated (1.06)" against politics at 1.45 (section 5, Stylized Fact 2). Conclusion: "raw prices should not be treated as context-free probabilities."
- *Bearing:* **supports on sports, complicates on politics.** The category the thesis calls "the dress" is the one where the price most nearly is a probability; the category the thesis calls "the promise" is the one where it is not.

**moshrefi2026prices** — Moshrefi, N. (2026). Prices, probabilities, and parlays: systematic bias in sports prediction markets. *2026 IEEE Symposium on Computational Intelligence for Financial Engineering and Economics (CIFEr)*, 250–257. doi:10.1109/cifer67845.2026.11692409.
- *Read status:* full text of arXiv:2607.14430v1 (15 July 2026, 5,731 words); refereed conference paper.
- *What it shows:* 23 million Kalshi moneyline trades. Calibration parameters "sit at their perfect-calibration reference values in the middle of a contract's life but depart sharply as expiry approaches"; in the final ten minutes the curve is step-like (abstract). Cross-game parlay median overpricing ratios are 0.991, 0.995, 0.999 at 2–4 legs, 1.01 at five, 1.07 at eight, 1.22 at ten and 1.31 at eleven; a fitted slope implies "a per-leg multiplicative inflation of roughly 3% in the median" (section V-B). "A parlay priced at 0.30 wins on average about 24% of the time; one priced at 0.40, about 30%" (section V-C). The markup exists "in a regime where the underlying legs are calibrated."
- *Bearing:* **supports on single contracts, cuts against on parlays.** A single-leg sports price mid-life is a probability; the betting-product feature layered on top (the parlay) carries a markup the leg prices do not explain.

**dubach2026anatomy** — Dubach, P. D. (2026). The anatomy of a decentralized prediction market: microstructure evidence from the Polymarket order book. arXiv:2604.24366v2 (14 May 2026).
- *Read status:* full text (8,501 words). Preprint; pre-registered panel of 600 markets, 52 days.
- *What it shows:* median quoted spread about 400 basis points in the central price deciles and 1,818 basis points for markets trading below 0.10 (Table 1); median effective half-spread 0.0075 probability points in sports against −0.0393 in crypto (Table 3); "the median wash share is 0.97%, with p90 = 4.5%, p99 = 10.6%, and a maximum of 22.2%" (section 5.7); feed-inferred trade direction matches the on-chain record about 59% of the time (abstract).
- *Bearing:* **supports.** Wash trading is small at the median, so manipulation-by-volume is not the thesis's best ground; sports spreads are tight.

**gruca2026forecasting** — Gruca, T. S., & Rietz, T. A. (2026). Forecasting 2026 congressional control: a comparison of IEM and Kalshi prediction markets. Forthcoming, *PS: Political Science & Politics* (manuscript dated 20 September 2026).
- *Read status:* full text (11,086 words). Forthcoming; no DOI yet.
- *What it shows:* the IEM has "(1) zero aggregate risk, (2) no trading fees, (3) an easily exploited arbitrage restriction, and (4) a $500 investment cap. None of these features characterize Kalshi markets." The two markets "generally forecast similar outcome probabilities and are significantly correlated in price levels"; vector autoregressions show "neither market consistently leads the other"; "the Kalshi markets sometimes display significant day-to-day price momentum, which the IEM does not" (abstract; section 1).
- *Bearing:* **supports with a caveat.** A commercial exchange with fees and no cap produces the same forecast as the academic reference market; it also shows momentum the reference market lacks.

### Line 3. Noise traders subsidise informative markets

**black1986noise** — Black, F. (1986). Noise. *Journal of Finance*, 41(3), 528–543. doi:10.1111/j.1540-6261.1986.tb04513.x.
- *Read status:* abstract (OpenAlex). Wiley full text refused.
- *What it shows:* "Noise makes trading in financial markets possible, and thus allows us to observe prices for financial assets. Noise causes markets to be somewhat inefficient, but often prevents us from taking advantage of inefficiencies."
- *Bearing:* **supports** the theoretical form of the argument: without uninformed trading there is no counterparty for the informed, hence no price.

**kyle1985continuous** — Kyle, A. S. (1985). Continuous auctions and insider trading. *Econometrica*, 53(6), 1315–1335. doi:10.2307/1913210.
- *Read status:* metadata only (Crossref; OpenAlex has no abstract; JSTOR not reachable). Not read this session. I rely on Hanson and Oprea's description of the model, below.

**hanson2009manipulator** — Hanson, R., & Oprea, R. (2009). A manipulator can aid prediction market accuracy. *Economica*, 76(302), 304–314. doi:10.1111/j.1468-0335.2008.00734.x.
- *Read status:* full text of the December 2007 working-paper version on Hanson's site (5,807 words). Seat H owns Hanson; I use this paper only for the noise-trader mechanism.
- *What it shows:* "a manipulative trader is in essence a 'noise' trader"; in a Kyle-style model "by inducing more traders to become better informed, an increase in noise trading indirectly improves the accuracy of market prices" (introduction, citing Kyle 1989). The result is theoretical.
- *Bearing:* **supports** the mechanism by which uninformed sports volume could raise the returns to informed trading. It says nothing about cross-market subsidy on a multi-category platform.

**brown2019wisdom** — Brown, A., & Yang, F. (2019). The wisdom of large and small crowds: evidence from repeated natural experiments in sports betting. *International Journal of Forecasting*, 35(1), 288–296. doi:10.1016/j.ijforecast.2018.06.002.
- *Read status:* full text of the UEA accepted manuscript dated 11 June 2018 (7,655 words).
- *What it shows:* 13 million Betfair prices on the Queen's Club tennis championships, 2008–2013. In even years, when a major football tournament clashed, pre-match trading was "18.33% less frequent" and in-play trading "15.15% less frequent," and forecast errors were "12.75% higher" pre-match and "15.84% higher" in-play (Panel A; Panel B: 15.9% and 23.25%) (section 4). "This suggests that measures which increase prediction market participation may lead to greater forecast accuracy" (abstract). The introduction notes that "without noise traders and wide participation, the returns to informed trading" fall.
- *Bearing:* **supports** the participation-to-accuracy link with a quasi-experiment. It does not show that participation in one market improves another.

**diercks2026kalshi (liquidity passage)** — see Line 4. Kalshi federal funds contracts show "volumes greater than a million for several strikes" in recent periods (section 2.3, Figure 2) and market making "provided by firms such as Susquehanna" (section 2). Whether sports volume pays for that infrastructure is not tested in any source I found.

### Line 4. A price you can read without trading is a public good

**diercks2026kalshi** — Diercks, A. M., Katz, J. D., & Wright, J. H. (2026). Kalshi and the rise of macro markets. Finance and Economics Discussion Series 2026-010, Board of Governors of the Federal Reserve System. doi:10.17016/FEDS.2026.010 (also NBER w34702).
- *Read status:* full text (12,583 words). Staff working paper; views are the authors'.
- *What it shows:* "For the federal funds rate forecasts 150 days (3 FOMC meetings) ahead, Kalshi's mean absolute error is very similar to that of professional forecasters" in the FRBNY Survey of Market Expectations; "the Kalshi median and mode have a perfect forecast record on the day before the FOMC meeting, which represents a statistically significant improvement over the fed funds futures forecast"; for core CPI and unemployment Kalshi errors are "almost the same as the Bloomberg consensus," and "for headline CPI, we find Kalshi provides a statistically significant improvement over the Bloomberg consensus forecast" (section 1). The authors argue Kalshi "should be used to provide risk-neutral pdfs concerning FOMC decisions" (section 2.2) and that the markets are "valuable to both researchers and policymakers" (abstract).
- *Bearing:* **supports.** Federal Reserve staff read the displayed distribution without trading. This is the clearest documented case of non-trader use.

**gelman2020information** — Gelman, A., Hullman, J., Wlezien, C., & Morris, G. E. (2020). Information, incentives, and goals in election forecasts. *Judgment and Decision Making*, 15(5), 863–880. doi:10.1017/s1930297500007981.
- *Read status:* full text (Cambridge Core PDF, 14,992 words).
- *What it shows:* section 2.6 treats prediction markets as "a completely different way to evaluate forecasts": during the 2020 campaign markets "consistently given Biden an implicit win probability in the 50–60% range, compared to poll-based forecasting models that have placed the Democrat's chance of winning to be in the 70–90% range." The authors warn that markets "can overreact to polls or can fail in the other direction by self-reinforcing" and that reading winner-take-all prices as probabilities "is not entirely straightforward (Manski 2006)."
- *Bearing:* **supports with reservations.** Statistical forecasters use the market price as a check on their own models; they also list the price's known defects.

**westwood2020projecting** — Westwood, S. J., Messing, S., & Lelkes, Y. (2020). Projecting confidence: how the probabilistic horse race confuses and demobilizes the public. *Journal of Politics*, 82(4), 1530–1544. doi:10.1086/708682.
- *Read status:* abstract (Semantic Scholar; DOI verified in Crossref). SSRN copy refused.
- *What it shows:* "forecasting increases certainty about an election's outcome, confuses many, and decreases turnout"; "election forecasting has become prominent in the media."
- *Bearing:* **cuts both ways.** It documents the public life of probabilistic forecasts in media, which the counter-case needs, and it finds that a displayed win probability confuses and demobilises, which the thesis can use. The experiments concern poll-based forecasts, not market prices.

**le2026decomposing (media passage)** — "News coverage often translates such prices directly into probabilities" (introduction), with the 5 November 2024 election contracts at 62 cents as the example. **moshrefi2026prices (media passage)** — prices "are increasingly treated as probabilities—by traders, researchers, journalists, and the designers of derivative products" (conclusion). Both are assertions by the authors, not measurements of media use.

**pew2026typical** — Radde, K. (2026, 22 July). What we know about the typical Polymarket user. Pew Research Center short read.
- *Read status:* web (secondary analysis of the Polymarket user-activity API; 11,989 wallets active on 10 high-volume events, 7 May to 19 June 2026).
- *What it shows:* "The typical (median) Polymarket user placed a total of 46 trades across 10 active trading days"; "the value of the average trade was $6.50"; 24% placed fewer than 10 trades, 39% 10–99, 27% 100–999, 11% 1,000 or more; "the typical Polymarket user largely broke even," with 58% within $100 of zero over six weeks, 9% losing more than $1,000 and 7% gaining more than $1,000; sports traders' median trade count was 69, crypto 59, politics 13.
- *Bearing:* **cuts both ways.** For the counter-case: the median user is a small-stakes participant who roughly breaks even. For the thesis: 46 trades in six weeks at $6.50 is a betting-app usage pattern, and sports traders trade five times as often as politics traders.

**pew2026volume** — Radde, K. (2026, 23 September). Prediction markets' trading volume doubled between May and July. Pew Research Center short read, citing The Block.
- *Read status:* web (secondary).
- *What it shows:* combined Kalshi and Polymarket monthly volume $25.7 billion (May 2026), $47.7 billion (June), $53.0 billion (July); July 2026 Kalshi $31.4 billion and Polymarket $21.6 billion. The page gives July sports volume as $31.4 billion on Kalshi and $10.6 billion on Polymarket, crypto $6.1 billion and $1.2 billion, politics $169 million and $727 million. **[verify]** The Kalshi category figures as the fetch returned them (sports $31.4 billion, crypto $6.1 billion, other $2.4 billion) exceed the Kalshi total of $31.4 billion, so either the total or the sports figure is mis-transcribed; seat D should read the page and The Block's source directly.
- *Bearing:* context for the volume-mix question in OUTLINE section (b); not a counter-argument.

### Line 5. Trading as the mechanism: incentive-compatible elicitation

**atanasov2017distilling** — Atanasov, P., Rescober, P., Stone, E., Swift, S. A., Servan-Schreiber, E., Tetlock, P., Ungar, L., & Mellers, B. (2017). Distilling the wisdom of crowds: prediction markets vs. prediction polls. *Management Science*, 63(3), 691–706. doi:10.1287/mnsc.2015.2374.
- *Read status:* abstract (Consensus; DOI and full author list verified in Crossref). Full text not reachable.
- *What it shows:* more than 2,400 forecasters, 261 events, two seasons; "last day prices from the prediction market were more accurate than the simple mean of forecasts from prediction polls. However, team prediction polls outperformed prediction markets when poll forecasts were aggregated with algorithms using temporal decay, performance weighting and recalibration."
- *Bearing:* **cuts both ways.** Markets beat the naive alternative and lose to the engineered one.

**dana2019are** — Dana, J., Atanasov, P., Tetlock, P., & Mellers, B. (2019). Are markets more accurate than polls? The surprising informational value of "just asking." *Judgment and Decision Making*, 14(2), 135–147. doi:10.1017/s1930297500003375.
- *Read status:* full text (Cambridge Core PDF, 10,006 words).
- *What it shows:* within-subject design; 46,168 market orders on 113 geopolitical questions; each trader reported a 0–100 belief before every order. Mean Brier scores: prices 0.227, aggregated beliefs 0.210 (t(113) = 1.44, p = 0.152), prices and beliefs combined 0.210 (t(113) = 2.92, p = 0.004, d = 0.27) (Table 1). The combination "directionally outperformed Prices on 85% of the 113 forecasting questions" (section 3). Decomposition: prices' calibration error 0.021 against beliefs' 0.014 (Table 3, upper panel). Abstract: self-reports "were at least as accurate as prediction-market prices" and the combination "was significantly more accurate than prediction-market prices alone, indicating that self-reports contained information that the market did not efficiently aggregate."
- *Bearing:* **cuts against the counter-case.** The same people, asked for a probability, produced a number at least as good as the price their trades made, and the market lost information the self-report kept.

**servanschreiber2004prediction** — Servan-Schreiber, E., Wolfers, J., Pennock, D. M., & Galebach, B. (2004). Prediction markets: does money matter? *Electronic Markets*, 14(3), 243–251. doi:10.1080/1019678042000245254.
- *Read status:* full text (Wolfers' NBER-hosted copy, 5,561 words).
- *What it shows:* TradeSports (real money) against NewsFutures (play money) on the 2003–2004 NFL season. Mean absolute forecast error 0.439 (0.011) against 0.436 (0.012), difference 0.003 (0.016); root mean squared error 0.468 against 0.467 (Table 2). Correlation between price and win frequency 0.96 and 0.94 (section 4). "Perhaps surprisingly, the play-money markets performed as well as the real-money markets" (abstract).
- *Bearing:* **cuts against the counter-case.** Real stakes added no accuracy in the one head-to-head field test on sports.

**rosenbloom2006statistical** — Rosenbloom, E. S., & Notz, W. (2006). Statistical tests of real-money versus play-money prediction markets. *Electronic Markets*, 16(1), 63–69. doi:10.1080/10196780500491303.
- *Read status:* abstract (OpenAlex; DOI verified in Crossref).
- *What it shows:* "real-money markets are significantly more accurate for non-sports events."
- *Bearing:* **supports the counter-case for non-sports**, and so indirectly concedes the sports result above.

**erikson2008are** — Erikson, R. S., & Wlezien, C. (2008). Are political markets really superior to polls as election predictors? *Public Opinion Quarterly*, 72(2), 190–215. doi:10.1093/poq/nfn010.
- *Read status:* abstract (OpenAlex; DOI verified in Crossref). JSTOR refused.
- *What it shows:* on IEM data 1988–2004, "when poll leads are properly discounted, poll-based forecasts outperform vote-share market prices" and "win projections based on the polls dominate prices from winner-take-all markets."
- *Bearing:* **cuts against** the counter-case for elections.

**reade2019polls** — Reade, J. J., & Vaughan Williams, L. (2019). Polls to probabilities: comparing prediction markets and opinion polls. *International Journal of Forecasting*, 35(1), 336–350. doi:10.1016/j.ijforecast.2018.04.001.
- *Read status:* full text (NTU IRep post-print, 14,626 words).
- *What it shows:* 2008–2012 US elections; Betfair, Intrade, IEM and all available polls. "Betfair and Intrade perform slightly better than the bias-corrected polls, and considerably better than the (uncorrected) IEM polls"; corrected polls "exhibit less bias, yet they seem generally less precise" (section 4). Mincer–Zarnowitz slopes for Betfair 1.447 and Intrade 1.242 show the markets' prices are too compressed (Table 3).
- *Bearing:* **supports with a caveat.** Large exchanges won on Brier score; they carried a correctable bias.

**mellers2014psychological** — Mellers, B., et al. (2014). Psychological strategies for winning a geopolitical forecasting tournament. *Psychological Science*, 25(5), 1106–1115. doi:10.1177/0956797614524255.
- *Read status:* full text (eScholarship PDF, 6,821 words).
- *What it shows:* probability training improved Year 1 Brier scores (F(2, 1586) = 14.29, p < .001); Table 1 gives untrained independent forecasters 0.44, 0.40 and 0.31 across first week, middle two weeks and last week against 0.40, 0.36 and 0.29 with probability training. "Results for prediction-market forecasting are not discussed here" (method, Year 1).
- *Bearing:* **supports the thesis, not the counter-case.** The documented improvement in calibration came from training people to state probabilities, not from trading.

### Line 6. Harm evidence for event contracts

**johnson2025prediction** — Johnson, B., & Chan, G. (2025). Prediction markets: an emerging form of gambling? *Addiction*, 121(2), 458–459. doi:10.1111/add.70272.
- *Read status:* letter text as returned by Consensus (short letter; DOI and authors verified in Crossref).
- *What it shows:* an argument, not a measurement: "functionally, these products resemble gambling"; risk "is heightened by 24/7 mobile access, push notifications, easy deposits and constant availability"; state harm-minimisation measures "generally do not apply."
- *Bearing:* **the counter-case's point stands on the record:** the peer-reviewed literature on event-contract harm is argument by analogy.

**dai2026settlement** — Dai, D., et al. (2026). Settlement manipulation in prediction markets. arXiv:2606.31675 (per Consensus; arXiv ID not independently resolved this session).
- *Read status:* abstract (Consensus).
- *What it shows:* after the launch of Polymarket's five-minute Bitcoin contract, "settlement-time spot order flow spikes," "manipulators capture a large amount of profit, mostly from retail," and "lengthening the contract horizon removes it."
- *Bearing:* **cuts against** the counter-case: a documented wealth transfer from retail in a short-horizon product; it is a design finding (horizon), which fits the thesis.

**cox2020compulsive** — Cox, R., et al. (2020). Compulsive gambling in the financial markets: evidence from two investor surveys. *Journal of Banking & Finance*. doi:10.1016/j.jbankfin.2019.105709. **lee2023association** — Lee, U., et al. (2023). Association between gambling and financial trading: a systemic review. *F1000Research*. doi:10.12688/f1000research.129754.1.
- *Read status:* abstracts (Consensus; DOIs and author lists verified in Crossref).
- *What they show:* 4.4% of a representative Dutch retail-investor sample met compulsive-gambling criteria and 3.6% problem-gambling criteria (Cox); across 12 studies, problem-gambling prevalence among financial traders ranged 1.4% to 47.2%, and trading frequency was "consistently associated with more severe problem gambling" (Lee).
- *Bearing:* **complicates** the counter-case. The analogy the platforms resist (gambling) applies to ordinary retail trading too, so "it is trading, not betting" does not escape the harm literature.

**baker2026retail** — Baker, S. R., Balthrop, J., Johnson, M. J., Kotter, J. D., & Pisciotta, K. (2026). Retail betting markets. *Annual Review of Financial Economics*. doi:10.1146/annurev-financial-111424-023216; NBER w35520.
- *Read status:* abstract (NBER page). PDF not linked.
- *What it shows:* a review of "the rapid expansion and convergence of retail betting markets" covering "shared behavioral drivers of sports betting markets, prediction markets, and retail options trading."
- *Bearing:* **complicates.** A finance review groups the three as one family of retail betting.

**Null result.** OpenAlex and Consensus searches (log rows 3 and 6) returned no study that measures problem-gambling severity, financial harm or loss-chasing among Kalshi or Polymarket users. I found no work that does X in those sources, where X is "measure harm among event-contract users." The Pew user data (above) are the only quantitative description of user outcomes: 58% within $100 of break-even over six weeks, 9% down more than $1,000.

### Line 7. Does participation improve calibration?

**cowgill2015corporate** — Cowgill, B., & Zitzewitz, E. (2015). Corporate prediction markets: evidence from Google, Ford, and Firm X. *Review of Economic Studies*, 82(4), 1309–1341. doi:10.1093/restud/rdv014.
- *Read status:* abstract (OpenAlex; DOI verified in Crossref).
- *What it shows:* "The inefficiencies that do exist generally become smaller over time. More experienced traders and those with higher past performance trade against the identified inefficiencies, suggesting that the markets' efficiency improves because traders gain experience and less skilled traders exit the market."
- *Bearing:* **weakly supports.** Market-level improvement is attributed jointly to learning and to exit; the abstract does not separate them, and Facet B's Seru et al. entry shows attrition can masquerade as learning.

**cardozo2026favorite (experience passage)** — longshot losses "persist after substantial previous trading, across experience levels" (section 8). **burgi2026makers (time passage)** — "some evidence that the bias in prices is diminishing over time," with non-monotonic yearly coefficients (Table 9). **sah2026prediction** — Sah, S., et al. (2026). Prediction market visualizations, betting, and uncertainty. arXiv:2608.16814 (full text opened, 4,718 words): r/Kalshi users "struggle with probability information displayed" (abstract; section 4). **mellers2014psychological** — calibration gains came from training, not trading.

**Null result.** No source in OpenAlex or Consensus (log rows 3 and 7) measures an individual's calibration before and after trading on a prediction market. The tournament literature measures training and teaming effects on people who state probabilities.

---

## (c) The seven lines, each stated as an argument, with evidence and a strength rating

**Line 1. The exchange is a different product from the sportsbook, and the difference favours the user.** A sportsbook is a dealer that takes a position, sets a bias-exploiting price with a commission "virtually always 10 percent" (Levitt 2004), and restricts winners: 643,779 of 14,923,840 British accounts in 2024, with restricted customers in profit 46.78% of the time against 25.42% overall (Gambling Commission 2025). An exchange matches users at a commission of at most 5% of winnings against a 25.63% bookmaker overround on the same races (Smith et al. 2006), shows less favourite-longshot bias (z of 0.9% against 2.17%; Smith et al. 2006) and predicts the same events better (Franck et al. 2010), and lets the user exit a position in-play at prices that incorporate news "swiftly and fully" (Croxson and Reade 2014). Kalshi and Polymarket are order books (Bürgi et al. 2026; Dubach 2026). **Rating: moderate.** The structural contrast is well documented for Betfair. It transfers to the platforms only if seat D confirms that they carry no house position, do not restrict winning accounts and allow exit before resolution. The explicit-cost gap is narrower than the Betfair precedent suggests: a Kalshi taker at 50 cents paid 1.75 cents on a 50-cent stake, 3.5 cents per dollar, against about 4.55 cents per dollar at a −110 sportsbook line (my computation from Bürgi et al. and Levitt). And the exchange form did not remove the favourite-longshot pattern on Kalshi: average per-contract return −20%, takers −31.46% (Bürgi et al. 2026).

**Line 2. Sports contracts are informative and well calibrated.** On Polymarket, sports is the one category with no favourite-longshot bias: longshot return +2.43% [−0.93, 5.79], favourites −0.230%, and the price-outcome curve "closer to the equality line" (Cardozo and Rivero-Wildemauwe 2026, Table 8, Figure 2). On Kalshi, sports recalibration slopes sit between 0.90 and 1.10 from 0 to 48 hours before resolution, and on Polymarket sports averages 1.06 against 1.45 for politics (Le 2026, Table 4 and section 5). Kalshi moneyline prices are calibrated in the middle of a contract's life (Moshrefi 2026). Bürgi et al.'s Kalshi-wide results hold with sports excluded, so the bias they find is not a sports artefact. Betfair precedent: Smith et al. 2006, Franck et al. 2010, Croxson and Reade 2014. **Rating: strong for single-leg sports prices mid-life; moderate overall.** The limits are documented in the same papers: calibration breaks in the final ten minutes (Moshrefi), sports slopes rise to 1.74 beyond a month (Le), and cross-game parlays carry a median markup of about 3% per leg even on calibrated legs (Moshrefi). All four platform studies are preprints or working papers except Moshrefi (refereed conference).

**Line 3. Uninformed volume subsidises informative markets.** Black (1986) and the Kyle framework as Hanson and Oprea (2009) apply it: noise trading is what makes a price observable and raises the return to becoming informed. Brown and Yang (2019) show the empirical link in a quasi-experiment: an 18.33% fall in pre-match participation raised forecast errors by 12.75% (pre-match) and 15.84% (in-play). Kalshi's sports volume (43.2 million trades) dwarfs its politics volume (4.9 million) (Le 2026, Table 2), and Kalshi runs macro markets with professional market making and strikes above a million contracts (Diercks et al. 2026). **Rating: weak for the specific claim, moderate for the general one.** The theory and the within-market participation evidence are sound. No source tests whether sports volume on a platform pays for liquidity or infrastructure in its politics or macro markets; that is an inference from platform economics that nobody has measured. Casadesus-Masanell and Campbell (2019) also show Betfair and bookmakers became complements, so exchange volume does not displace the sportsbook.

**Line 4. The displayed price is a public good that non-traders use.** Federal Reserve staff evaluate Kalshi's distributions against the FRBNY survey and Bloomberg consensus, find them as accurate at 150 days and better for headline CPI, and recommend them as "risk-neutral pdfs concerning FOMC decisions" (Diercks et al. 2026). Election forecasters compare their models to market prices (Gelman et al. 2020). Political scientists compare Kalshi to the IEM and find the same forecast (Gruca and Rietz 2026). Preprint authors assert that journalists translate prices to probabilities (Le 2026; Moshrefi 2026). Probabilistic forecasts have a large media presence (Westwood et al. 2020). If the price page is readable without an account (a platform fact for seat D), then the thesis's premise "the interface asks you to trade" describes the trader's screen and not the number's public life. **Rating: moderate.** Non-trader use by researchers and central-bank staff is documented. No study measures lay non-trader use or comprehension of a displayed market price, and Westwood et al. find that displayed win probabilities confuse and demobilise. The counter-case therefore relocates the design question rather than dissolving it: a public number still needs a display that a non-trader can read.

**Line 5. Trading is the point: stakes make the elicitation incentive-compatible.** Markets beat the simple mean of poll forecasts (Atanasov et al. 2017), beat bias-corrected polls on Brier score in 2008–2012 (Reade and Vaughan Williams 2019), and real money beat play money for non-sports events (Rosenbloom and Notz 2006). **Rating: weak.** The direct tests go the other way. Play money matched real money on NFL games (0.439 against 0.436 mean absolute error; Servan-Schreiber et al. 2004). The same traders' self-reported beliefs scored 0.210 against their market's 0.227, and the combination beat the market with p = 0.004, so the market lost information the self-reports kept (Dana et al. 2019). Engineered polls beat markets (Atanasov et al. 2017); discounted polls beat the IEM (Erikson and Wlezien 2008); training people to state probabilities improved calibration where trading was not even reported (Mellers et al. 2014). The honest form of this line is "a market is a cheap, robust aggregator that roughly matches the best alternatives," which is a defence of the mechanism and not of the interface. A probability-elicitation interface, by Dana et al., would get at least as good a number.

**Line 6. Harm evidence for event contracts is absent, so the gambling analogy may not transfer.** The record contains no measurement of harm among event-contract users; the peer-reviewed material is a letter (Johnson et al. 2025) and a one-sentence Science abstract (Packin et al. 2026, Facet D). The median Polymarket user trades $6.50 at a time and 58% end six weeks within $100 of even (Pew 2026). **Rating: weak as a defence, correct as a description.** Absence of measurement is not evidence of absence; the mechanisms Johnson et al. name (mobile access, notifications, short cycles) are shared with the products the gambling literature studied, and retail trading itself carries problem-gambling prevalence of 4.4% in a representative sample (Cox et al. 2020) and 1.4%–47.2% across 12 studies (Lee et al. 2023). Dai et al. (2026) document a retail wealth transfer in Polymarket's five-minute Bitcoin contract that disappears at fifteen minutes. The counter-case can hold only the narrow point: the essay cannot cite a harm study of these platforms, because none exists.

**Line 7. Participation improves users' calibration.** Cowgill and Zitzewitz (2015) report that inefficiencies shrink as traders gain experience and weaker traders exit; Bürgi et al. (2026) report some decline in bias over 2021–2025. **Rating: unsupported.** No study measures an individual's calibration before and after trading. Cowgill and Zitzewitz's mechanism is confounded with exit; Bürgi et al.'s yearly coefficients are not monotonic; Cardozo and Rivero-Wildemauwe find longshot losses "persist after substantial previous trading, across experience levels"; Sah et al. find r/Kalshi users struggle with the probability display; and the one documented calibration gain in this literature came from training, not trading (Mellers et al. 2014).

---

## (d) What the thesis must concede, and what it can still hold

Numbered propositions. Each cites the entry that forces or permits it.

**Concede.**

1. Sports is the best-calibrated category on both platforms. The favourite-longshot bias is absent in Polymarket sports (Cardozo and Rivero-Wildemauwe 2026) and Kalshi sports slopes sit near 1 up to 48 hours out (Le 2026); politics is the category where the price is least a probability. The essay cannot argue "sports betting in dress" from price quality, and must say so where OUTLINE section (d) already points.
2. The exchange form is a different product from a sportsbook, and the gambling literature the essay borrows from (Facet B) studied sportsbooks. Exchanges carry lower cost and less bias (Smith et al. 2006; Franck et al. 2010), and sportsbooks restrict winners at 4.31% of accounts (Gambling Commission 2025). The essay must name the platforms as exchange-form event betting and either show the interface features it criticises are exchange-independent or restrict its claim.
3. The explicit cost difference is smaller than the Betfair precedent implies for a taker at even odds (3.5 against 4.55 cents per dollar, my computation), and zero for makers in the pre-2025 sample. The essay should not claim the platforms are expensive relative to sportsbooks without the fee schedule from seat D.
4. The price has a documented public life among non-traders (Diercks et al. 2026; Gelman et al. 2020; Gruca and Rietz 2026). "The interface asks you to trade" is true of the account holder's screen and must be stated that narrowly.
5. Wash trading is about 1% at the median (Dubach 2026). Manipulation-by-volume is not a ground the essay should use for Polymarket.
6. Markets are a competent aggregator: they match or beat naive polls (Atanasov et al. 2017), bias-corrected polls (Reade and Vaughan Williams 2019), the IEM (Gruca and Rietz 2026) and professional macro surveys (Diercks et al. 2026). The essay argues design, not accuracy, and should concede accuracy plainly.

**Hold.**

7. Stakes are not what makes the number good. Play money matched real money on sports (Servan-Schreiber et al. 2004); the same traders' stated beliefs matched or beat their own market (Dana et al. 2019). A probability-elicitation interface would deliver at least the same number without the trading skill, which is the thesis's central design claim, and the counter-case's own evidence supports it.
8. The interface decides who pays. On Kalshi, makers returned −9.64% and takers −31.46% (Bürgi et al. 2026); order type is an interface default. The exchange form did not remove the favourite-longshot pattern (average per-contract return −20%). These are design facts about the trading screen, not about accuracy.
9. The borrowed betting-product form adds cost even where the underlying price is a probability: cross-game parlays carry a median markup of about 3% per leg on calibrated legs (Moshrefi 2026), and a parlay priced at 0.30 wins 24% of the time. Short-horizon products transfer wealth from retail (Dai et al. 2026, abstract).
10. No evidence shows that trading teaches calibration (Line 7). The one documented calibration gain came from training people to state probabilities (Mellers et al. 2014). The "no scaffold" criterion stands.
11. Harm is unmeasured, not disproven (Line 6). The essay may say that no harm study exists and that the structural features the gambling literature flags are present; it may not say harm is shown.
12. The volume mix is sports-heavy on both platforms by trade count (Le 2026, Tables 2 and 3: Kalshi 43.2 million sports trades against 4.9 million politics; Polymarket 49.1 million against 45.7 million) and by dollars (Cardozo: sports 36.8% of Polymarket dollars paid, politics 28.5%). The Pew July 2026 category figures need seat D's verification before any percentage is stated (see pew2026volume).
13. The display question survives the public-good concession. If non-traders read the price, the price needs a display a non-trader can read; Westwood et al. (2020) show that displayed win probabilities confuse and demobilise, and Le (2026) shows the same price carries different probabilistic content by domain and horizon. The essay's Part 1 criteria (declared operating envelope, scaffold, bounded output) apply to the public number as much as to the trader's screen.

---

## (e) Verify list

Items that must be checked before anything above enters a draft.

- **Platform facts the counter-case depends on (seat D):** whether Kalshi and Polymarket carry any house position; whether either restricts or closes winning accounts; whether positions can be exited before resolution and at what cost; whether the price page is readable without an account; the current fee schedules (Kalshi charged makers nothing until April 2025 per Bürgi et al.; current maker and taker rates unknown to me).
- **Pew volume figures (pew2026volume):** the Kalshi July 2026 category breakdown as fetched does not reconcile with the Kalshi total; read the page and The Block's data directly.
- **Bürgi, Deng and Whelan DOI:** Facet D lists doi:10.65864/s9kc4p0b7t for the CESifo version; I did not verify it. I read the January 2026 author copy at karlwhelan.com; CESifo WP 12122, CEPR DP 20631 and UCD WP 2025/19 are the series numbers WebSearch returned.
- **Dai et al. 2026** arXiv:2606.31675: ID taken from Consensus; not resolved against arXiv.
- **Kyle 1985:** metadata only; I rely on Hanson and Oprea's description of the model. Read before citing it for any specific claim.
- **Full texts not obtained:** Franck, Verbeek and Nüesch 2010 (IJF); Smith, Paton and Vaughan Williams 2009 (JEBO; HAL copy not fetched); Atanasov et al. 2017; Erikson and Wlezien 2008; Rosenbloom and Notz 2006; Cowgill and Zitzewitz 2015; Westwood et al. 2020; Black 1986; Grant et al. 2018; Casadesus-Masanell and Campbell 2019; Baker et al. 2026; Buhagiar, Cortis and Newall 2018 (not entered; ScienceDirect refused).
- **Working-paper versions read in place of the published article:** Levitt (NBER w9422 for the 2004 EJ article; the NBER title differs); Croxson and Reade (Birmingham DP 11-01 for the 2014 EJ article); Hanson and Oprea (2007 WP for the 2009 Economica article); Smith et al. 2006, Brown and Yang 2019 and Reade and Vaughan Williams 2019 (author post-prints). Page numbers in the bib are the journal's; locators in the entries are section names from the versions I read.
- **Gruca and Rietz 2026:** forthcoming in PS; no DOI; check publication before citing.
- **My computations:** the −110 line implies 4.55 cents expected loss per dollar for a 50/50 bettor (0.5 × 100/110 − 0.5); the Kalshi taker fee of 1.75 cents on a 50-cent contract is 3.5 cents per dollar staked. Both are arithmetic from the sources' stated parameters, not figures the sources report.
- **Opinion polls on prediction-market use** (NBC, Ipsos, Paradigm, Navigator, per WebSearch row 12): not opened; not cited.
