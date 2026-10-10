# B. Gamified and betting-style interfaces and behavioral harms

Facet B of the Decision Experience Design (DXD) Part 3 literature review. Agent-drafted on 2026-10-03 (abstract-level build) and verified by a second agent session the same day with the network open (Crossref, OpenAlex, Unpaywall, Europe PMC, PubMed, arXiv). The author has not reviewed it, and none of the text below is the author's.

What this facet covers. The interface features of online betting and trading apps (push notifications, confetti and badges, live odds, in-play and micro-event betting, one-tap trading, leaderboards, streaks) and what the literature says about their effect on risk-taking and overtrading. It also covers dark patterns and deceptive design in financial and gambling interfaces, and the evidence on whether users of these interfaces learn from feedback or overfit to noise. The synthesis answers three questions. B1: what the research shows about interface features and risk-taking or overtrading. B2: what the dark-pattern literature establishes and how far it reaches gambling and finance. B3: whether outcome feedback produces learning, calibration or noise-fitting. A fourth block, B4, was added in verification: studies of event-contract platforms (Kalshi, Polymarket) and of named sports-betting app features.

Legend for read status (set in the 2026-10-03 verification session). Full text: I opened the whole paper from the URL given and quote from it. Partial: I opened part of the paper (named). Abstract only: I read the publisher's or an index abstract (source named) and no full text. Metadata only: the DOI resolves but no abstract was retrievable this session. Bearing on the Part 3 argument is marked supports, complicates or refutes. The argument being tested is that decision markets such as Polymarket and Kalshi are poor decision experience design.

Method note on peer review. Journal articles and refereed proceedings are marked as such. Working papers, SSRN postings and arXiv preprints are flagged. Where the first build carried an SSRN or reprint DOI, the bib now carries the journal DOI and records the preprint DOI in the note.

Counts for the original 55 entries after verification: full text 31, partial 2, abstract only 22 (of which 2 metadata only this session), not obtained 0. All 55 DOIs resolve in Crossref and OpenAlex.

---

## (a) Search log

All searches ran on 2026-10-03. Hits is the count the source reported. Rows 1 to 14 are from the first build (network blocked); rows 15 onward are from the local verification session.

| # | Source | Exact query or request | Hits | Notes |
|---|---|---|---|---|
| 1 | Scholar Gateway semanticSearch (topN 8) | Do gamification features in retail trading apps such as confetti, push notifications and leaderboards increase risk-taking and overtrading? | 0 | Failed: INVALID_QUERY, Could not resolve user identity from CONNECT. Not retried. Scholar Gateway was not usable this session. |
| 2 | Consensus | gamification retail trading app Robinhood risk-taking overtrading | 20 | Surfaced Chapkovski et al. 2024 and 2025, Hüller et al. 2023, Barber et al. 2022, Newall 2022, Chaudhry et al. 2021, Ridgeway et al. 2023 |
| 3 | Consensus | sports betting apps push notifications in-play betting microbetting harm | 20 | Surfaced Hing et al. 2022, 2023, 2025, Parke et al. 2019, Rockloff et al. 2026, Killick et al. 2018, Russell et al. 2018, Vieira et al. 2023, Farrell et al. 2026 |
| 4 | Consensus | dark patterns deceptive design e-commerce prevalence and effectiveness on consumers | 20 | Surfaced Mathur et al. 2019, Luguri and Strahilevitz 2019, Zac et al. 2025, Sin et al. 2022, OECD 2022, McGarrigle et al. 2026 |
| 5 | Consensus | Barber Odean trading is hazardous to your wealth; online investors overconfidence and overtrading | 20 | Surfaced Barber and Odean 2000, Barber and Odean 2002, Odean 2011 reprint, Mosenhauer et al. 2021, Bregu 2020 |
| 6 | Consensus | forecasting tournaments training probabilistic reasoning improves calibration; outcome feedback learning | 20 | Surfaced Mellers et al. 2014, Chang et al. 2016, Moore et al. 2016, Benson and Onkal 1992, Stone and Opel 2000, Hauenstein et al. 2024, Martin et al. 2024 |
| 7 | Consensus | Smart(phone) investing? within investor-time analysis of new technologies and trading behavior mobile app | 20 | Surfaced Kalda et al. 2021, Cen 2023, Liu et al. 2024. Most of the other hits were technology-adoption surveys and were not used. |
| 8 | Consensus | near-miss effect loss chasing gambling slot machines and online betting | 19 | Surfaced Clark et al. 2009, Barton et al. 2017, Pisklak et al. 2019, Palmer et al. 2024, Zhang et al. 2024 (two papers) |
| 9 | Consensus | prediction market traders learning from feedback, overfitting noise, trader experience and performance | 20 | Surfaced Seru et al. 2010, Barber 2019, Nicolosi et al. 2009, Cowgill and Zitzewitz 2014. Many hits were agent-based simulations and were not used. |
| 10 | Consensus (page_size 8) | Wisdom of the Robinhood crowd: herding, attention, and returns of Robinhood investors | 8 | Found Welch 2020 (NBER record). No Welch paper on gamification surfaced. |
| 11 | Consensus (page_size 8) | The dark (patterns) side of UX design taxonomy of manipulative interface strategies | 8 | Found Gray et al. 2018 |
| 12 | Consensus (page_size 10) | betting app features, gambling harm, loss chasing and responsible gambling tools effectiveness Gainsbury Newall | 10 | Found Harris et al. 2016, Edson et al. 2025 and 2026 (not used). No Gainsbury paper surfaced. |
| 13 | Crossref REST (curl through the configured proxy) | 9 query.bibliographic lookups (Welch; Gray; Luguri and Strahilevitz journal DOI; Odean 1999; Barber and Odean 2000; Gainsbury; Newall; Hing; Kalda) | 0 | Failed: curl exit 56, CONNECT tunnel failed, response 403. The status endpoint shows a policy denial. I did not try to get around it. |
| 14 | OpenAlex REST (curl through the configured proxy) | one request, /works?per-page=1 | 0 | Failed: CONNECT tunnel failed, response 403. Same policy denial. Not retried. |
| 15 | Crossref REST /works/{doi} and OpenAlex /works/doi:{doi} (local session) | all 55 DOIs in the bib, one request each, paced 0.6 s | 55/55 resolved | Full author lists, venue, volume, issue, pages, issue dates and OA locations recorded. Script: scratchpad/resolve.py. |
| 16 | Crossref query.bibliographic (local) | 9 lookups: Luguri and Strahilevitz JLA; Welch JF; Barber and Odean JF 2000; Barber and Odean RFS 2002; Odean AER 1999; Seru Shumway Stoffman RFS; Kalda Loos Previtero Hackethal; Cowgill Zitzewitz RES; Mosenhauer Newall Walasek | 3 each | Journal DOIs found for all but Kalda (NBER w28363 and two SSRN postings only; no journal record). |
| 17 | OpenAlex title search | Smart(Phone) Investing within investor-time | 6 | OpenAlex lists 10.1093/rfs/hhab048 among Kalda versions; Crossref shows that DOI is Andonov, Kräussl and Rauh, Institutional Investors and Infrastructure Investing. OpenAlex merge error. Kalda remains unpublished in Crossref. |
| 18 | Crossref query.bibliographic | Barber Huang Odean Schwarz Attention Induced Trading and Returns Evidence from Robinhood Users | 6 | SSRN 3715077 is the working paper; NBER w28686 (tried first) is an unrelated paper. |
| 19 | Europe PMC REST search by DOI | 28 health-journal DOIs | 14 with PMCID and OA full text | Full-text XML pulled for Rockloff 2026, Hing 2023, Hing 2025, Vieira 2023, Farrell 2026, Clark 2009, Barton 2017, Pisklak 2019, Zhang 2024 (both), Harris 2016, McGarrigle 2026, Newall 2022, Mosenhauer 2021. |
| 20 | Unpaywall REST | Rockloff; Hauenstein; Luguri JLA; Seru RFS; Chapkovski MS | 5 | Rockloff hybrid OA (Wiley, Bristol, PubMed); Hauenstein bronze (Sage PDF, 403 to curl); Luguri gold (OUP PDF, 403 to curl); Seru and Chapkovski closed. |
| 21 | Semantic Scholar Graph API | 27 DOIs, paced after a 429 | 24 records | Gave the OSF copy of Hauenstein (osf.io/z9pxk) and confirmed no OA copy of Chapkovski 2024 beyond SSRN. |
| 22 | PubMed E-utilities (esearch by DOI, efetch) | Oksanen; Quintero; Palmer; Hing 2019; Russell 2018; Mosenhauer; Stone and Opel; Sinclair 2024 | 8 abstracts | Used where the full text is behind Springer, Elsevier or APA. |
| 23 | NBER working-paper PDFs (direct) | w28363 Kalda; w27866 Welch; w35520 Baker et al. | 3 | All 200. |
| 24 | Author and repository hosts (direct curl) | faculty.haas.berkeley.edu/odean (Barber and Odean 2000, 2002; Odean 1999; Barber et al. 2017 day-trader WP); tylergshumway.org (Seru 2010 RFS scan); cs.cmu.edu/~chinmayk (Chaudhry 2021); arxiv.org (Mathur 1907.07032); real.mtak.hu (McGarrigle, Hing 2025, Hing 2024); osf.io (Hauenstein; Szászi); cronfa.swan.ac.uk (Torrance); irep.ntu.ac.uk (Killick; Harris); wrap.warwick.ac.uk (Mosenhauer); cambridge.org (Zac; Sin; Chang); escholarship.org (Mellers; Moore); repec.som.yale.edu (Nicolosi); dipot.ulb.ac.be (Banerjee 2025); zaguan.unizar.es (Coloma-Carmona 2025); journalqd.org (Dahlke 2026) | all 200 | PDFs saved in scratchpad/pdf_B; text in scratchpad/txt_B. |
| 25 | Hosts that refused curl and WebFetch (HTTP 403, 303 to login, or bot wall) | onlinelibrary.wiley.com (Rockloff, Martin); journals.sagepub.com (Hauenstein, Tetlock 2014); academic.oup.com PDF (Luguri); papers.ssrn.com (Chapkovski 2024 and all SSRN); pubsonline.informs.org (Chapkovski); researchgate.net; link.springer.com (Hing 2022; Parke; Pisklak); research-information.bris.ac.uk PDF (Hing 2022); repository.arizona.edu (Hüller); dl.acm.org (Gray; Chaudhry); mdpi.com; sciencedirect.com (Oksanen); oecd-ilibrary.org and oecd.org (OECD 2022); eprints.lincoln.ac.uk (Parke; 202 with empty body); helda.helsinki.fi and trepo.tuni.fi (Oksanen; Anubis bot wall); figshare.com (Hing 2019; Russell); business.columbia.edu (Cowgill); chicagounbound.uchicago.edu (Luguri) | — | Where a second host served the paper, the entry says so. Otherwise the entry is abstract only. |
| 26 | web.archive.org (Wayback and CDX) | Luguri OUP PDF; Chapkovski SSRN delivery; Sage PDFs | — | 429 rate limit on first tries; then "Internet Archive services are temporarily offline" for the rest of the session. No Wayback copy was obtained. |
| 27 | WebFetch | academic.oup.com/jla/article/13/1/43/6180579 (Luguri HTML); research-information.bris.ac.uk record page (Hing 2022) | 2 pages read | Luguri: Section 3.1 and 3.2 numbers extracted. Bristol: metadata and abstract only; the PDF link returned 403. |
| 28 | CORE API v3 (search/works) | 9 title queries (Chapkovski; Hing 2022; Parke; Tetlock 2014; Oksanen; Cowgill; Chaudhry; Martin; Hüller) | 0 | Returned non-JSON (HTML) for every call; unauthenticated use appears blocked. Not retried. |
| 29 | arXiv API | au:Chapkovski AND all:gamification | 0 | No arXiv version of either Chapkovski paper. |
| 30 | WebSearch | Seru Shumway Stoffman "Learning by Trading" pdf; Chapkovski Khapko Zoican "Trading Gamification and Investor Behavior" pdf; Martin Mandel Practical scoring rule preprint; Cowgill Zitzewitz Corporate Prediction Markets pdf (two forms); Chaudhry Kulkarni Design Patterns of Investing Apps pdf; Tetlock et al. Forecasting Tournaments 2014 pdf; Gray et al. Dark (Patterns) Side CHI 2018 pdf | — | Produced the Shumway, CMU and lukemuehlhauser.com links (the last returned 403). No open copy of Chapkovski 2024, Martin 2024, Cowgill 2015 or Gray 2018 was found. |
| 31 | Crossref query.bibliographic, filter from-pub-date:2015, rows 8 (gap search) | Kalshi event contracts user interface | 496,523 | Top hits: SSRN 7442661, 7485679, 7421260, 7435839; JBEF 10.1016/j.jbef.2026.101259 (Lee, Lee and Lee, Kalshi NBA and NFL hot-hand). |
| 32 | OpenAlex search, publication_year>2014, per-page 8 (gap search) | Kalshi event contracts user interface | 25 | Bürgi, Deng and Whelan CESifo (Facet A/D territory); Lei and Rossi SSRN 7461319 Manufacturing Speculation; arXiv 2608.16814 Sah et al. (r/Kalshi visualizations). |
| 33 | Crossref (gap) | Polymarket traders behavior | 690,336 | SSRN 6624899 Wang (273 top traders); SSRN 6870538 Polymarket-v1 database; SSRN 5103168. |
| 34 | OpenAlex (gap) | Polymarket traders behavior | 117 | Wang SSRN; KTH thesis on HFT on Polymarket; SSRN 6670318 copy trading; JQD 10.51685/jqd.2026.011 Dahlke et al. |
| 35 | Crossref (gap) | Polymarket user interface design | 1,778,703 | No relevant hit in top 8 (generic UI-design chapters). |
| 36 | OpenAlex (gap) | Polymarket user interface design | 78 | arXiv 2602.05181 Rohanifar, Ahmed and Sultana (Polymarket sociotechnical audit); SSRN 7344081 and 7344079 (resolution and settlement). |
| 37 | Crossref (gap) | PredictIt traders behavior survey | 1,039,262 | Only an R package and unrelated items. |
| 38 | OpenAlex (gap) | PredictIt traders behavior survey | 25 | Annual Review of Financial Economics 10.1146/annurev-financial-111424-023216 Baker et al., Retail Betting Markets (also NBER w35520 and SSRN 7118579). |
| 39 | Crossref (gap) | prediction market app gamification retail traders | 952,883 | Wang SSRN; SSRN 6582150 app-based stock rankings. |
| 40 | OpenAlex (gap) | prediction market app gamification retail traders | 88 | Lei and Rossi; Public Health 10.1016/j.puhe.2025.105742 Coloma-Carmona et al.; SSRN 7473598 Trading Gamification, Asset Prices, and Liquidity. |
| 41 | Crossref (gap) | event contracts sports CFTC retail bettors | 457,608 | No scholarly hit on event contracts in top 8. |
| 42 | OpenAlex (gap) | event contracts sports CFTC retail bettors | 15 | Baker et al.; SSRN 7239999 Perez, Optimal Taker Delays in In-Play Event Contract Markets; SSRN 7115858 Curtin; SSRN 7546718 Mace and Johnson, Adverse Selection in Sports Prediction Markets; BC Law Review Betting on Everything (2025). |
| 43 | Crossref (gap) | sports betting app push notifications experiment | 460,858 | Only generic push-notification studies and a 2023 Conversation piece. |
| 44 | OpenAlex (gap) | sports betting app push notifications experiment | 157 | JBA 10.1556/2006.2023.00073 Hing et al. 2024 (discrete choice experiment on platform features); Hing 2023 (already in bib); Baker et al. |
| 45 | Crossref (gap) | same game parlay bettors | 190,720 | EJOR 10.1016/j.ejor.2023.04.006 Michels, Ötting and Langrock, Bettors' reaction to match dynamics; nothing on same-game parlays as a feature. |
| 46 | OpenAlex (gap) | same game parlay bettors | 76 | J. Prediction Markets 2018 correlated parlays (college football pricing); CIFEr 2026 Prices, Probabilities, and Parlays; nothing on bettor behaviour with the feature. |
| 47 | Crossref (gap) | in-play betting cash out feature gambling harm | 472,762 | Frontiers in Psychiatry 10.3389/fpsyt.2020.574884 (in-play and problems, Australia). |
| 48 | OpenAlex (gap) | in-play betting cash out feature gambling harm | 1,142 | Addictive Behaviors 10.1016/j.addbeh.2024.108008 Sinclair et al. (cash outs); PsyArXiv 10.31234/osf.io/jq7pb Szászi et al. (cash-out registered report); IJMHA 10.1007/s11469-018-9876-x. |
| 49 | Crossref (gap) | one-tap betting friction gambling | 648,466 | Nothing relevant. OpenAlex call returned 429 on first try. |
| 50 | Crossref (gap) | sports bettors migrate prediction markets | 916,832 | SSRN 6350738 Holden, Turk and Edelman, Regulating Sports Prediction Markets; SSRN 4513239 Decentralized Prediction Markets and Sports Books. No empirical study of migration. |
| 51 | Crossref (gap) | prediction markets sports betting substitution Kalshi | 954,848 | Only Kalshi pricing and efficiency SSRN papers. |
| 52 | Crossref (gap) | streaks gambling app design | 1,568,266 | Int. Gambling Studies 10.1080/14459795.2025.2494598 Banerjee, Noël and Chen (outcome streaks and within-session chasing); a 2026 Conversation piece on Wealthsimple's prediction-market app. Nothing on streak mechanics as a designed feature. |
| 53 | OpenAlex (gap), second pass after 429s | one-tap betting friction gambling; sports bettors migrate prediction markets; prediction markets sports betting substitution Kalshi; streaks gambling app design; prediction markets gambling harm problem gambling; Kalshi sports event contracts bettors; prediction market interface price display probability users; Polymarket sports betting users survey | — | All eight returned HTTP 429 (rate limit) even after a 20 s pause. Not completed. Crossref versions of two of these (rows 54, 55) ran instead. |
| 54 | Crossref (gap) | prediction markets gambling harm problem gambling | 878,825 | Nothing on prediction markets in top 8. |
| 55 | Crossref (gap) | prediction market interface probability display users experiment | 1,200,628 | Nothing relevant. |
| 56 | OpenAlex /works/doi (gap candidates) | 18 candidate DOIs from rows 31 to 52 | 18 | Metadata and abstracts pulled; saved to scratchpad/gap_candidates.json. SSRN items carry no abstract in OpenAlex or Crossref. |

Consequence of rows 31 to 56. I found no empirical study of a Kalshi, Polymarket or PredictIt interface that measures user behaviour against an interface variable. The nearest items are Sah et al. (arXiv 2026; how r/Kalshi users read the platform's probability charts), Rohanifar et al. (arXiv 2026; a qualitative audit of Polymarket), and Baker et al. (2026; a review that names cross-platform substitution as an open question). I found no study of sports bettors migrating to prediction-market apps. Sports-betting feature studies exist for in-play betting, cash-out and platform features (rows 44, 47, 48) and are entered in B4. Nothing on same-game parlays, one-tap bets or streak mechanics as designed features was found in Crossref or OpenAlex.

---

## (b) Entries

Entries follow the facet's questions. Each gives the citekey, the verified reference, the read status with its source, what the source argues, and its bearing on Part 3. Where the full text changed the summary, the entry says what changed.

### B1. Interface features, risk-taking and overtrading

barber2000hazardous. Barber, B. M. and Odean, T. (2000). Trading is hazardous to your wealth: the common stock investment performance of individual investors. Journal of Finance, 55(2), 773–806. DOI 10.1111/0022-1082.00226 (SSRN 10.2139/ssrn.219228 is the preprint).
- Read status: full text (journal version, faculty.haas.berkeley.edu/odean/Papers current versions/Individual_Investor_Performance_Final.pdf).
- What it argues: among 66,465 households at a discount broker, 1991 to 1996, the households that traded most earned 11.4 percent a year against a market return of 17.9 percent, and overconfidence explains the high trading. All three figures appear in the published abstract and body.
- Bearing: supports. It is the baseline for overtrading before apps. It does not test any interface feature.

barber2002online. Barber, B. M. and Odean, T. (2002). Online investors: do the slow die first? Review of Financial Studies, 15(2), 455–488. DOI 10.1093/rfs/15.2.455 (SSRN 10.2139/ssrn.219242 is the preprint, posted 2000).
- Read status: full text (journal version, faculty.haas.berkeley.edu/odean/Papers current versions/Online RFS.pdf).
- What it argues: 1,607 investors who moved from phone to online trading traded more actively, more speculatively and less profitably afterwards. Lower costs and faster execution did not explain the change; overconfidence, self-attribution bias and illusions of knowledge and control did.
- Bearing: supports. It is the earliest within-investor evidence that a change of interface changes trading. It also separates friction from psychology, which matters for one-tap trading.

odean1999trade. Odean, T. (1999). Do investors trade too much? American Economic Review, 89(5), 1279–1298. DOI 10.1257/aer.89.5.1279. The first build carried the 2011 Princeton reprint DOI 10.2307/j.ctvcm4j8j.28 (Advances in Behavioral Economics, pp. 606–632).
- Read status: full text (author-hosted version, faculty.haas.berkeley.edu/odean/Papers current versions/DoInvestors.pdf).
- What it argues: the securities that 10,000 discount-broker accounts bought underperformed those they sold, even after liquidity and tax motives are considered.
- Bearing: supports. The AER article is now matched; the verify item is cleared.

barber2022attention. Barber, B. M., Huang, X., Odean, T. and Schwarz, C. (2022). Attention-induced trading and returns: evidence from Robinhood users. Journal of Finance, 77(6), 3141–3190. DOI 10.1111/jofi.13183 (SSRN 10.2139/ssrn.3715077 is the 2020 working paper).
- Read status: abstract only (publisher abstract via Crossref). Wiley full text not obtained; no OA copy in Unpaywall or OpenAlex.
- What it argues: Robinhood investors engage in more attention-induced trading than other retail investors; outages disproportionately reduce trading in high-attention stocks; the pattern is consistent with inexperienced users but "is also driven in part by the app's unique features"; average 20-day abnormal returns are −4.7 percent for the top stocks purchased each day. The abstract confirms every number in the first build.
- Bearing: supports. It ties app design to herding with a measured cost, but the abstract cannot say which feature does the work.

welch2020wisdom. Welch, I. (2022). The wisdom of the Robinhood crowd. Journal of Finance, 77(3), 1489–1527. DOI 10.1111/jofi.13128. NBER Working Paper 27866 (September 2020, DOI 10.3386/w27866) is the version read.
- Read status: full text (NBER w27866 PDF, nber.org); journal abstract via Crossref.
- What it argues: Robinhood investors collectively raised holdings in the March 2020 bear market, showed no collective panic or margin calls, tilted toward high-volume, mostly large stocks, and their consensus portfolio had good timing and alpha from mid-2018 to mid-2020.
- Bearing: complicates. The full text contains no analysis of gamification, confetti or nudges (a search of the 52-page text for those terms finds nothing). The first build's caution stands: Part 3 should cite Welch as a counterweight (retail crowds are not simply noise), not as a gamification source. The verify item on the journal DOI is cleared.

kalda2021smartphone. Kalda, A., Loos, B., Previtero, A. and Hackethal, A. (2021). Smart(phone) investing? A within investor-time analysis of new technologies and trading behavior. NBER Working Paper 28363, January 2021. DOI 10.3386/w28363. Also SSRN 10.2139/ssrn.3765652 and 10.2139/ssrn.3772602. No journal version exists in Crossref (OpenAlex's link to 10.1093/rfs/hhab048 is a merge error; that DOI is a different paper).
- Read status: full text (NBER PDF, 58 pages).
- Design and sample: transaction-level data from two German banks; investor-by-month fixed effects compare the same investor's trades across platforms in the same month. Sample windows 2010 to 2016 at one bank and 2013 to 2017 at the other; the second bank's raw data cover about twenty million transactions by 116,000 investors from 2003 to 2017 (Section 3).
- What it argues: smartphone trades are more likely to be in riskier and lottery-type assets and to chase past returns. After smartphone adoption, investors also buy riskier, lottery-type and hot assets on other platforms, so there is no substitution across platforms. Effects do not fade between the first and tenth quarter after first smartphone use.
- On nudges (Section 5.3, pp. 23–25, Tables 11 and 12). The authors could not observe how information was displayed in the apps, so they ran a falsification test: if digital nudges such as "top mover" lists drove the result, the smartphone effect should be stronger for individual stocks, which apps feature, and weaker or absent for mutual funds and options, which they do not. The effect is "similarly strong—if anything stronger" for mutual funds (p. 25), with positive and similar point estimates for options and warrants. They conclude that "digital nudges do not drive the smartphone effects we document," and add that even if nudges were a channel, "our results—not being driven by any specific nudge—are more likely to generalize to smartphone trading apps in general," and that regulating choice architecture alone "might not be as effective as hoped" (p. 25).
- On screen size (Section 5.4, Table 13): iPhone and iPad trades show similar effects, so the small screen does not drive the result.
- Bearing: complicates. What changed in verification: the first build said Kalda et al. "rule out nudges as the mechanism." The paper does not rule nudges out; it shows by falsification that no app-specific nudge is necessary for the effect, while conceding it could not observe the apps' displays. Part 3 should say the smartphone effect appears in asset classes the apps do not feature, so it is not explained by salience nudges alone; it must not credit confetti or notifications for this result.

cen2023smartphone. Cen, X. (2024). Smartphone trading technology, investor behavior, and mutual fund performance. Management Science, 70(10), 6897–6916. DOI 10.1287/mnsc.2021.02099 (online 2023).
- Read status: abstract only (publisher abstract via Crossref). INFORMS full text not obtained.
- What it argues: a natural experiment around a large adviser's app release. Adopters pay more attention and trade more; their flows become more sensitive to short-term fund returns and sentiment; funds more exposed to the shock lose abnormal returns; both adopters and non-adopters see lower mutual-fund returns.
- Bearing: supports, with an externality: the harm reaches non-adopters.

liu2024mobile. Liu, C.-W., Mithas, S., Pan, Y. and Hsieh, J. J. P.-A. (2025). Mobile apps, trading behaviors, and portfolio performance: evidence from a quasi-experiment in China. Information Systems Research, 36(2), 828–846. DOI 10.1287/isre.2020.0616 (online 2024).
- Read status: abstract only (publisher abstract via Crossref).
- What it argues: with archival data on 20,665 investors at a Chinese securities company, app adoption leaves portfolio performance unchanged on average. Lower time constraints help, a modest rise in trend chasing hurts, and app-use intensity has an inverted-U relation to performance.
- Bearing: complicates. The app effect is mixed, not uniformly harmful.

chapkovski2024gamification. Chapkovski, P., Khapko, M. and Zoican, M. (2026). Trading gamification and investor behavior. Management Science, 72(1), 32–56. DOI 10.1287/mnsc.2022.02650. Published online 2024; the facet and outline cite it as 2024. SSRN 10.2139/ssrn.3971868 is the working paper (first posted 2021 under the title "Does gamified trading stimulate risk taking?").
- Read status: abstract only (publisher abstract via Crossref). Full text not obtained: INFORMS, SSRN and ResearchGate returned 403; the author's site links only to SSRN; no arXiv, CORE or Semantic Scholar copy; Wayback was offline.
- What the abstract states (verbatim where the outline relies on it): "On average, hedonic gamification increases trading volume by 5.17%. However, the difference in trading activity between gamified and nongamified platforms is driven primarily by self-selection (70%) rather than gamification (30%)." Participants with lower financial literacy prefer platforms with confetti and achievement badges; those who prefer hedonic gamification trade noisily, those who prefer non-gamified platforms are more contrarian; "price trend notifications enhance learning for investors with accurate beliefs, but they reinforce trading mistakes for those with incorrect beliefs." Design: randomized online experiment.
- What the 70 percent is a percentage of: the difference in trading activity between participants on gamified and non-gamified platforms; 70 percent of that difference is attributed to who chooses which platform, 30 percent to the gamification treatment itself. Sample size, recruitment platform, number of rounds and the table that carries the decomposition are not in the abstract and remain unverified.
- Bearing: complicates and supports. The causal effect is real but small, and self-selection matters. The notification result is directly relevant to B3.

chapkovski2025gamified. Chapkovski, P., Khapko, M. and Zoican, M. (2025). Gamified risk-taking. Journal of Behavioral and Experimental Finance, 46, 101049. DOI 10.1016/j.jbef.2025.101049.
- Read status: abstract only (OpenAlex abstract). Elsevier full text not obtained.
- What it argues: a randomized online experiment with 605 participants from four countries trading a virtual asset. Digital nudges to hold volatile assets (achievement badges, motivational prompts) amplify risk-taking, most in high-volatility environments and most among inexperienced traders with low financial literacy; a one-standard-deviation rise in financial literacy cuts the effect by 56 percent.
- Bearing: supports. The author list is the same trio as the 2024 paper; the first build's "and others" is corrected.

huller2023gamified. Hüller, C., Reimann, M. and Warren, C. (2023). When financial platforms become gamified, consumers' risk preferences change. Journal of the Association for Consumer Research, 8(4), 429–440. DOI 10.1086/726431.
- Read status: abstract only (OpenAlex abstract). The Arizona repository copy returned 403 to curl and WebFetch; Chicago full text not obtained.
- What it argues: six experiments show that game elements such as leaderboards make investment choices riskier because they add a goal (winning the game); once the goal is reached, the extra risk-taking stops.
- Unverified: the first build's N = 3,766 is not in the abstract and could not be checked.
- Bearing: supports, and names a mechanism (goal pursuit) that a leaderboard on a decision market would trigger.

chaudhry2021design. Chaudhry, S. and Kulkarni, C. (2021). Design patterns of investing apps and their effects on investing behaviors. In Proceedings of the 2021 ACM Designing Interactive Systems Conference (DIS '21), pp. 777–788. DOI 10.1145/3461778.3462008.
- Read status: full text (author copy, cs.cmu.edu/~chinmayk/assets/pdfs/2021-DIS-TradingApps.pdf, 12 pages).
- What it argues: it derives design guidelines for healthy investing from finance research, dual-process theory and the literature on uncertain-reward interfaces, then audits popular apps (Robinhood, Public, Webull are named) and finds they follow few of them.
- Bearing: supports, as an audit rather than a causal test. The two-author list replaces "and others."

ridgeway2023predatory. Ridgeway, A. and Wason, N. (2023). From the poor to the rich: predatory inclusion and the Robinhood app. Technical Communication, 70(4), 60–72. DOI 10.55177/tc191789.
- Read status: abstract only (publisher abstract via Crossref).
- What it argues: a critical interface analysis (Sano-Franchini's method) of three microinteractions, depositing and withdrawing, browsing, and trading, finds that the interface frames users as informed investors without giving them the tools, and that "a manufactured sense of urgency encourages users to overtrade."
- Bearing: supports as interpretive evidence only. No behavior was measured.

newall2022gamblification. Newall, P. W. S. and Weiss-Cohen, L. (2022). The gamblification of investing: how a new generation of investors is being born to lose. International Journal of Environmental Research and Public Health, 19(9), 5391. DOI 10.3390/ijerph19095391.
- Read status: full text (Europe PMC, PMC9105963).
- What it argues: a gamblified product leads most users to lose, attracts people at risk of gambling harm, and uses gambling design principles (high frequency, lottery-like payoffs). High-frequency trading and high-risk derivatives qualify.
- Bearing: supports. It supplies a three-part test that Part 3 can apply to event contracts.

mosenhauer2021casino. Mosenhauer, M., Newall, P. W. S. and Walasek, L. (2021). The stock market as a casino: associations between stock market trading frequency and problem gambling. Journal of Behavioral Addictions, 10(3), 683–689. DOI 10.1556/2006.2021.00058 (PsyArXiv preprint 10.31234/osf.io/zqe9s).
- Read status: full text (Europe PMC, PMC8997227; also Warwick WRAP accepted version).
- What it argues: among 795 US adults who were both active gamblers and stock-market investors, self-reported relative portfolio turnover rises with Problem Gambling Severity Index scores, robust to financial literacy, overconfidence and demographics, and across portfolio sizes. Retrospective cross-section.
- Bearing: supports, but it is a retrospective cross-section.

oksanen2022gambling. Oksanen, A., Mantere, E., Vuorinen, I. and Savolainen, I. (2022). Gambling and online trading: emerging risks of real-time stock and cryptocurrency trading platforms. Public Health, 205, 72–78. DOI 10.1016/j.puhe.2022.01.027.
- Read status: abstract only (PubMed abstract, PMID 35247862). Elsevier, Helsinki and Tampere repositories blocked.
- What it argues: in a Finnish population survey (N = 1,530, ages 18 to 75), 22.29 percent were regular monthly investors only, 3.01 percent used real-time stock-trading platforms and 3.59 percent traded crypto; the latter two groups were younger, male, and showed more excessive behavior and distress, while regular investing did not.
- Bearing: supports as association only.

parke2019continuous. Parke, A. and Parke, J. (2019). Transformation of sports betting into a rapid and continuous gambling activity: a grounded theoretical investigation of problem sports betting in online settings. International Journal of Mental Health and Addiction, 17(6), 1340–1359. DOI 10.1007/s11469-018-0049-8.
- Read status: abstract only (OpenAlex abstract). Springer and the Lincoln repository blocked.
- What it argues: behavioural data and in-depth interviews with 19 online sports bettors meeting problem-gambling criteria yield an "Online Sports Betting Loop" sustained by live betting, cash out, micro-event betting and instant depositing; marketing ubiquity made control harder; the authors call for mechanisms that increase breaks in play.
- Bearing: supports. It is the closest description of a loop that continuous event contracts could reproduce.

hing2022smartphone. Hing, N., Thorne, H., Russell, A. M. T., Newall, P. W. S., Lole, L., Rockloff, M., Browne, M., Greer, N. and Tulloch, C. (2024). 'Immediate access … everywhere you go': a grounded theory study of how smartphone betting can facilitate harmful sports betting behaviours amongst young adults. International Journal of Mental Health and Addiction, 22(3), 1413–1432. DOI 10.1007/s11469-022-00933-8 (online 2022).
- Read status: abstract only (publisher abstract via Crossref; Bristol record page via WebFetch). The Springer and Bristol PDFs returned 303-to-login and 403.
- What it argues: interviews with 33 Australians aged 18 to 29 who bet regularly on sports, esports or fantasy sports, analysed by adaptive grounded theory, yield seven themes; smartphone betting's anywhere-anytime access facilitates more participation, frequency and spend, a wider variety of bets, impulsive betting, riskier bets with longer odds, chasing losses, and acting on social encouragement.
- Bearing: supports (qualitative).

hing2023situational. Hing, N., Browne, M., Rockloff, M., Russell, A. M. T., Tulloch, C., Lole, L., Thorne, H. and Newall, P. (2023). Situational features of smartphone betting are linked to sports betting harm: an ecological momentary assessment study. Journal of Behavioral Addictions, 12(4), 1006–1018. DOI 10.1556/2006.2023.00065.
- Read status: full text (Europe PMC, PMC10786227).
- What it argues: an ecological momentary assessment of 1,378 betting sessions finds that anywhere-anytime betting, privacy and exposure to more promotions are associated with more short-term harm.
- Bearing: supports.

hing2025direct and rockloff2026direct.
- hing2025direct. Hing, N., Browne, M., Russell, A. M. T., Rockloff, M. and Rawat, V. (2025). The high cost of direct marketing from wagering operators, tipsters and affiliates: an ecological momentary assessment of how wagering promotions drive betting, expenditure, and harm. Journal of Behavioral Addictions, 14(3), 1355–1367. DOI 10.1556/2006.2025.00067.
  - Read status: full text (Europe PMC, PMC12486272; also real.mtak.hu PDF).
  - What it argues: linear mixed models on 4,020 observations from 814 Australians who bet at least fortnightly on sports or races (seven EMA surveys over two weeks). Participants using each service received on average 12.7 messages from operators, 11.8 from free services and 21.7 from tipsters over the fortnight. Bets, expenditure and harm rose with each additional operator message; messages by email, text and app notification from any source came with higher expenditure and harm; operator messages were most potent for higher-risk bettors. Observational, not randomized.
- rockloff2026direct. Rockloff, M., Browne, M., Hing, N., Russell, A. M. T., Rawat, V. and Newall, P. (2026). Direct gambling marketing, direct harm: a randomised experiment. Addiction, 121(7), 1907–1919. DOI 10.1111/add.70369. Published online 18 March 2026.
  - Read status: full text (Europe PMC, PMC13291081; the Wiley PDF returned 403).
  - Design: stratified randomised field experiment, between participants, embedded in a 14-day EMA with seven surveys every 48 hours, Australia, July to August 2023, during a high-volume betting season. Stratified by PGSI category, age group and gender; 60 percent allocated to treatment.
  - Population and sample: regular Australian sports and race bettors from online panels who agreed in principle to opt out of all operator direct marketing. From a 1,015-person baseline, 615 were invited and 405 enrolled; 227 completed at least one EMA survey and form the analysed sample (opt-out n = 96, control n = 131; 61.7 percent men; mean age 45; 52.0 percent in the PGSI moderate-risk or problem range). The authors note "substantial post-randomisation attrition, particularly among participants allocated to the treatment group who did not provide proof of opting out" (Discussion, limitations).
  - Outcomes and analysis: self-reported number of bets, expenditure (AUD) and short-term harms (10-item adapted Short Gambling Harm Screen) in the previous 48 hours. Linear mixed models with participant random effects on Yeo–Johnson-transformed outcomes (λ = −1 for bets; λ = −0.1 for expenditure and harms). The methods state that no pre-registered analysis plan or a priori sample-size calculation was available and that "these analyses should be regarded as exploratory in nature."
  - The three numbers, confirmed verbatim: "The opt-out group placed 23% fewer bets [B = −0.11, 95% confidence interval (CI) = −0.20, −0.03, P = 0.011], spent 39% less money (B = −0.53, 95% CI = −0.84, −0.21, P = 0.001) and reported 67% fewer short-term gambling harms (B = −0.22, 95% CI = −0.36, −0.07, P = 0.004) compared with the controls" (Abstract, Findings; repeated in Results and in the first sentence of the Discussion). Locators: Table 3 (bets), Table 4 (expenditure), Table 5 (harms), each with models 1 to 3; Figures 2 to 4 show trimmed means by wave. Each percentage is the relative difference between the opt-out and control groups in the average per-48-hour outcome; the B coefficients are on the transformed scale, so the percentages are not exp(B). Adding wave and condition-by-wave terms (models 2 and 3) left the condition effect essentially unchanged.
- Bearing: supports, and Rockloff is the strongest causal evidence on notifications in this facet. What changed in verification: the first build gave n = 227 as the randomized sample; 227 is the analysed sample after attrition from 405 enrolled, and the authors label the analysis exploratory. Part 3 must carry both caveats with the three numbers. The sample is gamblers on Australian operators, not prediction-market users, and the treatment removed direct marketing of all kinds (email, text, push), not push notifications alone.

hing2019wagering. Hing, N., Russell, A. M. T., Thomas, A. and Jenkinson, R. (2019). Wagering advertisements and inducements: exposure and perceived influence on betting behaviour. Journal of Gambling Studies, 35(3), 793–811. DOI 10.1007/s10899-018-09823-y.
- Read status: abstract only (PubMed abstract, PMID 30604033). Springer and figshare blocked.
- What it argues: an EMA design in which 722 regular bettors completed up to 15 surveys on 5 days a week over three non-consecutive weeks; data analysed for 316 race and 279 sports bettors. Bettors report near-daily exposure; the most seen and most influential types were direct messages (emails, texts, calls, which Australian account holders are automatically opted into) and ads on betting sites and apps. Influence is self-reported.
- Bearing: supports, but the influence is self-reported.

killick2018inplay, russell2018microbets, vieira2023inplay, farrell2026live. In-play and micro-event betting.
- killick2018inplay. Killick, E. A. and Griffiths, M. D. (2019). In-play sports betting: a scoping study. International Journal of Mental Health and Addiction, 17(6), 1456–1495. DOI 10.1007/s11469-018-9896-6 (online 2018). Read status: full text (NTU repository accepted version). Scoped 16 papers and 338 gambling websites; judges in-play betting potentially more harmful because of its structural characteristics.
- russell2018microbets. Russell, A. M. T., Hing, N., Browne, M., Li, E. and Vitartas, P. (2019). Who bets on micro events (microbets) in sports? Journal of Gambling Studies, 35(1), 205–223. DOI 10.1007/s10899-018-9810-y (online 2018). Read status: abstract only (PubMed, PMID 30386964). Surveyed 1,813 Australian sports bettors: of those who bet on micro events, 78 percent met problem-gambling criteria and 5 percent were non-problem gamblers, against 29 and 28 percent for non-micro-event bettors; micro-event bettors were younger, educated, single, impulsive and broadly engaged.
- vieira2023inplay. Vieira, J. L., Coelho, S. G., Snaychuk, L. A., Parmar, P. K., Keough, M. T. and Kim, H. S. (2023). Who makes in-play bets? Investigating the demographics, psychological characteristics, and gambling-related harms of in-play sports bettors. Journal of Behavioral Addictions, 12(2), 547–556. DOI 10.1556/2006.2023.00030. Read status: full text (Europe PMC, PMC10316160). Ontario in-play bettors report higher severity and harm than single-event and traditional bettors.
- farrell2026live. Farrell, H., Bennett, D. and Myles, D. (2026). More frequent use of live sports-betting features is associated with increased risk of gambling harm: evidence from a case-control design. Journal of Behavioral Addictions, 15(1), 509–514. DOI 10.1556/2006.2025.00491. Read status: full text (Europe PMC, PMC13132358). 85 cases and 84 controls, exploratory; more in-play betting, cash-out and in-app streaming among higher-risk bettors.
- Bearing: supports, with one caution. All four are cross-sectional, scoping or exploratory, so they cannot separate feature effects from who chooses the feature.

torrance2023structural and quintero2023microbetting. Scoping reviews.
- torrance2023structural. Torrance, J., O'Hanrahan, M., Carroll, J. and Newall, P. (2024). The structural characteristics of online sports betting: a scoping review of current product features and utility patents as indicators of potential future developments. Addiction Research & Theory, 32(3), 204–218. DOI 10.1080/16066359.2023.2241350 (online 2023). Read status: full text (Swansea Cronfa submitted version). 26 records and 8 patents; instant access, rapid continuous betting, cash-out and instant deposit are the structural features.
- quintero2023microbetting. Quintero Garzola, G. C. and Vaccarino, A. L. (2024). Microbetting, fantasy sports and risk of gambling disorder: a scoping review. Journal of Gambling Studies, 40(2), 587–600. DOI 10.1007/s10899-023-10239-6 (online 2023). Read status: abstract only (PubMed, PMID 37452978). A rapid PubMed-only review, November 2014 to November 2019, 22 references included; links micro-betting to severe problem gambling and impulsivity.
- Bearing: supports as maps of the field. Both inherit the weak causal designs of what they review; Quintero Garzola and Vaccarino searched one database.

clark2009nearmiss, barton2017ldw, pisklak2019nearmiss, palmer2024nearmiss. Near-miss.
- clark2009nearmiss. Clark, L., Lawrence, A. J., Astley-Jones, F. and Gray, N. (2009). Gambling near-misses enhance motivation to gamble and recruit win-related brain circuitry. Neuron, 61(3), 481–490. DOI 10.1016/j.neuron.2008.12.031. Read status: full text (Europe PMC author manuscript, PMC2658737). Near-misses are rated less pleasant but raise the desire to play, only when the player has personal control over the gamble.
- barton2017ldw. Barton, K. R., Yazdani, Y., Ayer, N., Kalvapalle, S., Brown, S., Stapleton, J., Brown, D. G. and Harrigan, K. A. (2017). The effect of losses disguised as wins and near misses in electronic gaming machines: a systematic review. Journal of Gambling Studies, 33(4), 1241–1260. DOI 10.1007/s10899-017-9688-0 (erratum 10.1007/s10899-017-9696-0). Read status: full text (Europe PMC, PMC5663799). 51 studies; near-misses motivate continued play but effects on emotion and betting vary.
- pisklak2019nearmiss. Pisklak, J. M., Yong, J. J. H. and Spetch, M. L. (2020). The near-miss effect in slot machines: a review and experimental analysis over half a century later. Journal of Gambling Studies, 36(2), 611–632. DOI 10.1007/s10899-019-09891-8 (online 2019). Read status: full text (Europe PMC, PMC7214505). Reports failures to support the effect in pigeons and humans.
- palmer2024nearmiss. Palmer, L., Ferrari, M. A. and Clark, L. (2024). The near-miss effect in online slot machine gambling: a series of conceptual replications. Psychology of Addictive Behaviors, 38(6), 716–727. DOI 10.1037/adb0000999. Read status: abstract only (PubMed, PMID 38709628). Preregistered Prolific experiments on a three-reel simulator (Study 1a n = 169, 1b n = 148, Study 2 n = 170, Study 3 n = 172): near-misses raised motivation, were rated more positively than full misses (opposite to hypothesis), and produced faster spins and larger bets.
- Bearing: complicates. The near-miss effect is real in some paradigms and absent in others. Part 3 should cite it only for products with a skill or control framing, and then only as a hypothesis for event contracts. No study here involves a market interface.

zhang2024within and zhang2024between. Zhang, K., Rights, J. D., Deng, X., Lesch, T. and Clark, L. (2024). Within-session chasing of losses and wins in an online eCasino. Scientific Reports, 14, 20353. DOI 10.1038/s41598-024-70738-3. And: Between-session chasing of losses and wins in an online eCasino. Journal of Behavioral Addictions, 13(2), 665–675. DOI 10.1556/2006.2024.00022.
- Read status: full text (Europe PMC, PMC11368930 and PMC11220803).
- What they argue: within sessions, gamblers bet more and play longer after immediate losses but less after cumulative losses. Between sessions the evidence for loss chasing is limited and the evidence for win chasing is clear.
- Bearing: complicates. Loss chasing is not the uniform behavior the lay account assumes.

harris2016harmmin. Harris, A. and Griffiths, M. D. (2017). A critical review of the harm-minimisation tools available for electronic gambling. Journal of Gambling Studies, 33(1), 187–221. DOI 10.1007/s10899-016-9624-8 (online 2016).
- Read status: full text (Europe PMC, PMC5323476; also NTU accepted version).
- What it argues: it reviews breaks in play, pop-up messages, limit setting and behavioural tracking, and the evidence on whether each changes cognition and behavior.
- Bearing: complicates. A design remedy exists in the literature; the review gives no pooled effect sizes.

### B2. Dark patterns and deceptive design

gray2018dark. Gray, C. M., Kou, Y., Battles, B., Hoggatt, J. and Toombs, A. L. (2018). The dark (patterns) side of UX design. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems, Paper 534, pp. 1–14. DOI 10.1145/3173574.3174108.
- Read status: abstract only (OpenAlex abstract). ACM PDF returned 403; the arXiv ID returned by one search (1802.04050) is an unrelated statistics paper and was discarded.
- What it argues: a content analysis of practitioner-identified dark patterns finds a wide range of ethical concerns conflated under one term, and a shared worry that UX designers "could easily become complicit in manipulative or unreasonably persuasive practices."
- Bearing: supports. It is the design-ethics anchor for Part 3, and it concerns practice, not user outcomes.

mathur2019scale. Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M. and Narayanan, A. (2019). Dark patterns at scale: findings from a crawl of 11K shopping websites. Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), Article 81, 1–32. DOI 10.1145/3359183.
- Read status: full text (arXiv 1907.07032v2, 32 pages).
- What it argues (Abstract and Section 1): the crawler visited about 53K product pages on about 11K shopping websites and found 1,818 dark-pattern instances representing 15 types in 7 broader categories, on 1,254 sites (about 11.1 percent); 234 instances across 183 sites were deceptive; 22 third-party entities sell dark patterns as a turnkey service. Every number in the first build is confirmed; the 1,254-site prevalence figure is added.
- Bearing: supports as prevalence evidence. The sample is shopping sites, not financial or betting interfaces.

luguri2019shining. Luguri, J. and Strahilevitz, L. J. (2021). Shining a light on dark patterns. Journal of Legal Analysis, 13(1), 43–109. DOI 10.1093/jla/laaa006 (SSRN 10.2139/ssrn.3431205 is the 2019 working paper).
- Read status: partial (OUP full-text HTML read via WebFetch, Sections 3.1 and 3.2; the OUP PDF and Chicago Unbound copy returned 403).
- What it argues: Study 1, a census-weighted Dynata sample of 1,963 US adults: 11.3 percent accepted a dubious data-protection plan in the control, 25.8 percent under mild dark patterns and 41.9 percent under aggressive ones; the paper describes these as "more than doubled" and "nearly quadrupled" (a 228 and 371 percent increase on the control rate). Aggressive patterns produced a backlash; mild ones did not. Less educated participants were more likely to accept under both treatments. Study 2 (3,777 participants) found hidden information doubled acceptance (30.1 percent against a 14.8 percent control).
- Bearing: supports as effect-size evidence that design, not price, drives choice. The task was a data-protection subscription, not a trade. The verify item on the journal DOI is cleared.

zac2025vulnerability, sin2022darkpatterns, oecd2022dark. Susceptibility and policy.
- zac2025vulnerability. Zac, A., Huang, Y.-C., von Moltke, A., Decker, C. and Ezrachi, A. (2025). Dark patterns and consumer vulnerability. Behavioural Public Policy, first view, 1–50. DOI 10.1017/bpp.2024.49. Read status: full text (Cambridge Core PDF). Susceptibility across all groups; only weak support for income, education or age as vulnerability proxies; added friction (requiring payment details) reduces the effect, so dark patterns "are of greatest effect when the online interface requires a 'single click' to complete the purchase."
- sin2022darkpatterns. Sin, R., Harris, T., Nilsson, S. and Beck, T. (2025). Dark patterns in online shopping: do they work and can nudges help mitigate impulse buying? Behavioural Public Policy, 9(1), 61–87. DOI 10.1017/bpp.2022.11 (online 2022). Read status: full text (Cambridge Core PDF). Dark patterns raise purchase impulsivity and any tested intervention beats none.
- oecd2022dark. OECD (2022). Dark commercial patterns. OECD Digital Economy Papers No. 336. DOI 10.1787/44f5e846-en. Read status: abstract only (OpenAlex abstract). The OECD iLibrary PDF and oecd.org copy returned 403 and 404. Gives a working definition and reviews prevalence, effectiveness and harm.
- Bearing: supports. The single-click result bears directly on one-tap trading, though the experiments are shopping tasks. What changed: the first build wrote "one-click"; the paper's phrase is "single click."

mcgarrigle2026gambling. McGarrigle, J., Smith, J., Griffiths, J., Torrance, J., Quigley, M. and Dymond, S. (2026). Dark patterns in online gambling: a scoping review and classification of deceptive design practices. Journal of Behavioral Addictions, 15(1), 99–114. DOI 10.1556/2006.2025.00096.
- Read status: full text (Europe PMC, PMC13132400; also real.mtak.hu accepted version).
- What it argues: a preregistered scoping review that included 16 records published 2018 to 2025 (seven grey-literature reports and nine peer-reviewed articles; Results, Table 1). Patterns catalogued: hidden gambling-management tools, inducements with complex conditions, withdrawal minimums, account-closing friction, high defaults in stake, deposit, reality-check and limit settings, and urgency-based prompts. The authors map these to a transdisciplinary framework and state that "evidence on behavioural impacts is limited, hindered by restricted access to proprietary gambling operator data."
- Bearing: supports and sets the gap: gambling dark patterns are catalogued, not measured. The n = 16 is confirmed.

### B3. Feedback, learning and noise

seru2010learning. Seru, A., Shumway, T. and Stoffman, N. (2010). Learning by trading. Review of Financial Studies, 23(2), 705–739. DOI 10.1093/rfs/hhp060 (SSRN 10.2139/ssrn.891694 is the 2006 working paper).
- Read status: full text (published RFS scan, tylergshumway.org/Seru-LearningTrading-2010.pdf).
- Design and sample: all trades in all Finnish stocks over nine years, 1995 to 2003, from the Nordic Central Securities Depository; 322,454 accounts (Table 1, Panel A), 11,979 with disposition estimates (Panel B); survival analysis, disposition effect and performance at the account level with adjustment for individual heterogeneity and endogenous attrition.
- What it argues: two kinds of learning, "some investors become better at trading with experience, while others stop trading after realizing that their ability is poor," and "a substantial part of overall learning by trading is explained by the second type" (Abstract). After adjusting for survivorship, an extra 100 trades is associated with about 3.6 basis points better 30-day returns (about 30 bp a year) and about a 2 percent smaller disposition effect; measured by years rather than trades, the improvement is negligible; and "the magnitude of the learning estimates presented above is about two to four times higher when not adjusted for investor attrition" (Introduction).
- Bearing: complicates in a useful way. Aggregate improvement on a market can reflect who leaves. The outline's phrase "learning partly attrition" is confirmed and can now carry the two-to-four-times figure.

barber2019learning. Barber, B. M., Lee, Y.-T., Liu, Y.-J., Odean, T. and Zhang, K. (2020). Learning, fast or slow. Review of Asset Pricing Studies, 10(1), 61–93. DOI 10.1093/rapstu/raz006 (online 2019).
- Read status: partial (the 2017 working-paper version, "Do Day Traders Rationally Learn About Their Ability?", read in full from faculty.haas.berkeley.edu/odean; the published abstract read via Crossref). The 74 and 97 percent figures are in the published abstract and not in the 2017 draft.
- What it argues: among Taiwanese day traders, unprofitable traders quit more often, yet aggregate performance is negative, "74% of day trading volume is generated by traders with a history of losses; and 97% of day traders are likely to lose money in future day trading." This fits overconfidence and biased learning, not rational trading to learn.
- Bearing: supports. It is the strongest evidence here for the claim that repeated feedback does not cure speculation.

nicolosi2009learn. Nicolosi, G., Peng, L. and Zhu, N. (2009). Do individual investors learn from their trading experience? Journal of Financial Markets, 12(2), 317–336. DOI 10.1016/j.finmar.2008.07.001.
- Read status: full text (Yale ICF working-paper version, repec.som.yale.edu).
- What it argues: investors trade more when their history suggests stock-selection ability, and experience improves performance, with heterogeneity across investors.
- Bearing: complicates. Some learning does occur. Seru et al. (2010) argue that without attrition adjustment such estimates are inflated.

bregu2020feedback. Bregu, K. (2020). Overconfidence and (over)trading: the effect of feedback on trading behavior. Journal of Behavioral and Experimental Economics, 88, 101598. DOI 10.1016/j.socec.2020.101598.
- Read status: metadata only this session (Crossref and OpenAlex carry no abstract; Elsevier blocked; the first build's summary rests on the Consensus abstract of 2026-10-03 and was not re-read).
- What the first build recorded: in a laboratory design where overconfidence in information accuracy creates a reason to overtrade, feedback on accuracy changes how much overconfidence drives trading; overconfidence raises volume and weakly cuts profit.
- Bearing: supports a conditional claim: feedback on the right quantity can limit overtrading. What changed: the journal name is Journal of Behavioral and Experimental Economics, not Journal of Socio-Economics (its former title).

benson1992feedback and stone2000training. Feedback type.
- benson1992feedback. Benson, P. G. and Önkal, D. (1992). The effects of feedback and training on the performance of probability forecasters. International Journal of Forecasting, 8(4), 559–573. DOI 10.1016/0169-2070(92)90066-I. Read status: metadata only this session (no abstract in Crossref or OpenAlex; SSRN 1288057 copy blocked). First-build summary: simple outcome feedback had very little effect; calibration feedback improved calibration in one step.
- stone2000training. Stone, E. R. and Opel, R. B. (2000). Training to improve calibration and discrimination: the effects of performance and environmental feedback. Organizational Behavior and Human Decision Processes, 83(2), 282–309. DOI 10.1006/obhd.2000.2910. Read status: abstract only (PubMed, PMID 11056072). Performance feedback reduced overconfidence, environmental feedback improved discrimination, neither improved the other, and environmental feedback raised overconfidence; the authors read this as evidence that calibration and discrimination are dissociable.
- Bearing: supports. Plain win-or-lose outcome feedback, which is what a market position gives, is the weak kind. Calibration feedback needs a scoring rule and a record of many forecasts.

mellers2014psych, tetlock2014tournaments, chang2016champs, moore2016calibration. Tetlock-style training.
- mellers2014psych. Mellers, B., Ungar, L., Baron, J., Ramos, J., Gurcay, B., Fincher, K., Scott, S. E., Moore, D., Atanasov, P., Swift, S. A., Murray, T., Stone, E. and Tetlock, P. E. (2014). Psychological strategies for winning a geopolitical forecasting tournament. Psychological Science, 25(5), 1106–1115. DOI 10.1177/0956797614524255. Read status: full text (eScholarship copy). Training, teaming and tracking (top 2 percent from Year 1 placed in elite teams) improved calibration and resolution.
- tetlock2014tournaments. Tetlock, P. E., Mellers, B. A., Rohrbaugh, N. and Chen, E. (2014). Forecasting tournaments: tools for increasing transparency and improving the quality of debate. Current Directions in Psychological Science, 23(4), 290–295. DOI 10.1177/0963721414534257. Read status: abstract only (publisher abstract via Crossref). Tournaments as level-playing-field comparisons; the Good Judgment Project beat the crowd average by debiasing training, teams and prediction markets, talent skimming, and aggregation.
- chang2016champs. Chang, W., Chen, E., Mellers, B. and Tetlock, P. (2016). Developing expert political judgment: the impact of training and practice on judgmental accuracy in geopolitical forecasting tournaments. Judgment and Decision Making, 11(5), 509–526. DOI 10.1017/S1930297500004599. Read status: full text (Cambridge Core PDF). A training module of under an hour improved Brier accuracy by 6 to 11 percent over control.
- moore2016calibration. Moore, D. A., Swift, S. A., Minster, A., Mellers, B., Ungar, L., Tetlock, P., Yang, H. H. J. and Tenney, E. R. (2017). Confidence calibration in a multiyear geopolitical forecasting competition. Management Science, 63(11), 3552–3565. DOI 10.1287/mnsc.2016.2525 (online 2016; OSF preprint 10.31219/osf.io/xphfq). Read status: full text (eScholarship accepted version). Confidence roughly matched accuracy over three years with about 3 percent overconfidence; training reduced it, and teams plus training reduced it to 1 percent.
- Bearing: supports a design claim. Learning from forecasts is possible when questions resolve against probabilities, scores are returned and training is given. A trading interface offers prices and profit, not Brier scores.

hauenstein2024rethinking and martin2024practical. Limits on the training result.
- hauenstein2024rethinking. Hauenstein, C. E., Thomas, R. P., Illingworth, D. A. and Dougherty, M. R. (2025). Rethinking the role of teams and training in geopolitical forecasting: the effect of uncontrolled method variance on statistical conclusions. Psychological Science, 36(1), 3–18. DOI 10.1177/09567976241266481 (online December 2024). Read status: full text (accepted manuscript, osf.io/z9pxk; the Sage PDF returned 403). The authors re-analyse the Mellers et al. (2014) tournament data in an item response theory framework, comparing seven models over the first two tournament years under three ways of conditioning the data. "In all cases, the best-fit model included one or more extraneous variables, which substantially eliminated, reduced, and, in some cases, even reversed the effects of the experimental manipulations of teaming and training on latent forecasting ability" (Abstract). The Statement of Relevance adds that the results "raise the possibility that both teaming and training did not improve forecasting ability" and call for tightly controlled laboratory studies. The paper reports no single effect size for the reduction; it is a model-comparison result.
- martin2024practical. Martin, M. and Mandel, D. R. (2025). Calibration feedback with the Practical scoring rule does not improve calibration of confidence. Futures & Foresight Science, 7(1), e199. DOI 10.1002/ffo2.199 (online November 2024). Read status: abstract only (publisher abstract via Crossref). Two experiments (N1 = 610, N2 = 871) on a two-alternative city-population task found no calibration gain from either outcome feedback or Practical-score feedback relative to control.
- Bearing: complicates. The training literature is contested, and Part 3 should state it that way. The outline's "Hauenstein 2024" wording ("substantially reduces, eliminates or sometimes reverses") matches the abstract's order of verbs loosely; the exact phrase is "substantially eliminated, reduced, and, in some cases, even reversed."

cowgill2014corporate. Cowgill, B. and Zitzewitz, E. (2015). Corporate prediction markets: evidence from Google, Ford, and Firm X. Review of Economic Studies, 82(4), 1309–1341. DOI 10.1093/restud/rdv014. The first build's DOI 10.1145/2600057.2602901 is a one-page abstract in Proceedings of the Fifteenth ACM Conference on Economics and Computation (2014), p. 525.
- Read status: abstract only (OpenAlex abstract of the RES article). OUP full text not obtained; Columbia and Dartmouth pages returned 403 and 404.
- What it argues: markets at Google, Ford and an anonymous materials conglomerate were relatively efficient and improved on expert forecasts "by as much as a 25% reduction in mean-squared error." "The most notable inefficiency is an optimism bias in the markets at Google." Inefficiencies shrink over time; experienced and higher-performing traders trade against them, "suggesting that the markets' efficiency improves because traders gain experience and less skilled traders exit the market."
- Bearing: complicates. It shows learning by selection in low-stakes corporate markets, which differ from open retail markets. What changed: the first build placed the optimism bias at "Google and Ford"; the abstract names Google.

### B4. Event-contract platforms and named betting-app features (added in verification, 2026-10-03)

These entries come from the gap search (log rows 31 to 56). None measures user behaviour against an interface variable on Kalshi or Polymarket.

sah2026visualizations. Sah, S., Karduni, A., Markant, D. B. and Dou, W. (2026). Prediction market visualizations, betting, and uncertainty: a study of Reddit posts and comments. arXiv 2608.16814. Preprint, not peer reviewed.
- Read status: full text (arXiv PDF, 5 pages).
- What it argues: from about 12,000 posts and 96,000 comments on r/Kalshi, the authors identified 360 posts containing platform visualizations and ran a thematic analysis. Users infer uncertainty by reading chart values, "struggle with probability information displayed," bring in outside knowledge, question credibility and liquidity, critique the design, and connect the charts to betting decisions. One quoted commenter explains that displayed percentages "are usually either the last traded price or the midpoint of the order book," not probabilities that sum to 100 percent.
- Bearing: supports. It is the only study found of how users read a Kalshi price display, and it documents the price-versus-probability confusion that Part 3 section 3 describes. Qualitative, self-selected forum sample, preprint.

rohanifar2026laundering. Rohanifar, Y., Ahmed, S. I. and Sultana, S. (2026). Prediction laundering: the illusion of neutrality, transparency, and governance in Polymarket. arXiv 2602.05181 (manuscript submitted to ACM). Preprint.
- Read status: full text (arXiv PDF, 16 pages).
- What it argues: a qualitative sociotechnical audit of Polymarket (N = 27; digital ethnography, interpretive walkthroughs and interviews) argues that aggregation strips high-uncertainty bets, hedges and whale activity of their noise and presents the result as objective probability; the authors call this prediction laundering and trace a four-stage lifecycle.
- Bearing: supports the framing claim (the price presents as neutral knowledge) and complicates the design claim (the authors locate the problem in governance and aggregation, not in a bet-slip interface). Interpretive; no behaviour measured.

hing2024features. Hing, N., Russell, A. M. T., Tulloch, C., Lole, L., Rockloff, M., Browne, M., Thorne, H. and Newall, P. W. S. (2024). Feature preferences of sports betting platforms: a discrete choice experiment shows why young bettors prefer smartphones. Journal of Behavioral Addictions, 13(1), 134–145. DOI 10.1556/2006.2023.00073.
- Read status: full text (real.mtak.hu accepted version).
- What it argues: 616 Australians aged 18 to 29 who bet at least monthly rated 24 platform features and completed a discrete choice experiment. The most valued feature was the ability to bet instantly, 24/7, from any location, then electronic payments; smartphones were the only platform offering every preferred feature. The experiment found no difference in preferences by gambling severity, but the descriptive ratings showed that moderate-risk and problem gamblers placed more importance on privacy, in-play betting, cash and credit-card betting, frequent promotions and multiple operators.
- Bearing: supports. It is the only experimental study found of named sports-betting app features, and the feature it finds most valued, instant anywhere access, is one an event-contract app shares.

sinclair2024cashout. Sinclair, E. S.-L. L., Clark, L., Wohl, M. J. A., Keough, M. T. and Kim, H. S. (2024). Cash outs during in-play sports betting: who, why, and what it reveals. Addictive Behaviors, 154, 108008. DOI 10.1016/j.addbeh.2024.108008.
- Read status: abstract only (PubMed, PMID 38479082).
- What it argues: of 224 Ontario adults who bet in-play in the past three months, 51.8 percent used cash-out; users reported more problematic alcohol and cannabis use and more depression, anxiety and stress, and bet to make money; reasons given were immediate access to money, cutting losses, and cash-out feeling less risky.
- Bearing: supports as association only. Cash-out is the sports-betting analogue of selling an event contract before resolution.

szaszi2024cashout. Szászi, B., Hung, W. Y., Szécsi, P., Kolumbán, P., Kolozsvári, M., Bognár, M., Yesilöz, A., Griffiths, M. D. and Demetrovics, Z. (2024). The impact of cash-out availability on online betting behavior. Stage 1 Registered Report, PsyArXiv. DOI 10.31234/osf.io/jq7pb.
- Read status: full text (OSF PDF, 24 pages). Design only; the study had no results at the time of posting.
- What it proposes: a randomized online experiment with Hungarian residents who have gambled online, told they will bet real money on sports events, with half told they can cash out before the outcome; outcomes are the share placing bets, bet sizes and bet risk.
- Bearing: none yet; it marks that the causal test of cash-out is in progress, which Part 3 can say.

banerjee2025streaks. Banerjee, N., Noël, X. and Chen, Z. (2025). Effects of winning and losing streaks on within-session chasing in online gambling: a replication and extension study. International Gambling Studies, 25(3), 387–411. DOI 10.1080/14459795.2025.2494598.
- Read status: full text (ULB DI-fusion accepted version).
- What it argues: in 4,308 gamblers and about 71 million rounds of a commercial online dice game (Mystery Arena), gamblers reduced persistence and stake size as losing streaks lengthened and did not change speed; no clear pattern followed winning streaks. Exploratory analyses point to reduced funds and the expectation that losing will continue.
- Bearing: complicates. These are outcome streaks, not streak mechanics designed into an app; the search found no study of designed streaks. The result cuts against a simple loss-chasing story.

baker2026retail. Baker, S. R., Balthrop, J., Johnson, M. J., Kotter, J. D. and Pisciotta, K. J. (2026). Retail betting markets. Annual Review of Financial Economics (forthcoming; volume and pages not yet assigned). DOI 10.1146/annurev-financial-111424-023216. Also NBER Working Paper 35520 (DOI 10.3386/w35520) and SSRN 10.2139/ssrn.7118579.
- Read status: full text (NBER w35520 PDF, 40 pages).
- What it argues: a review of the convergence of sports betting, prediction markets and retail options trading. It documents Polymarket and Kalshi volumes, notes that sportsbooks' effective fee is about 4 percent on straight bets and nearly 20 percent on parlays (Illinois data), and states that "it is not yet clear the extent to which individual participants treat sports betting, prediction markets, and financial options as substitutes," with early evidence "consistent with a degree of substitution across markets." No in-play, dark-pattern or interface analysis.
- Bearing: complicates. It is the only source found that addresses migration between sports betting and prediction markets, and it frames the question as open. Part 3 cannot assert migration as fact from this source.

dahlke2026polymarket. Dahlke, R., Mine, N., Zhao, H., Huang, Y. and Shah, D. (2026). Electoral predictions on Polymarket: a quantitative description of trading, commenting, and reacting. Journal of Quantitative Description: Digital Media, 6, 1–92. DOI 10.51685/jqd.2026.011.
- Read status: partial (abstract and front matter read from the journal PDF; the 88-page body not read).
- What it argues: 778,634 wallet addresses over 846 days, 30,502,864 trades totalling 5.86 billion dollars, 384,586 comments and 571,523 reactions across 959 election events; trading and commenting are largely decoupled within events.
- Bearing: complicates. It is platform-scale behavioural data with no interface variable; Part 3 can cite it for scale only.

coloma2025traders. Coloma-Carmona, A., Carballo, J. L., Miró-Llinares, F. and Aguerri, J. C. (2025). Not all traders gamble, but some gamblers trade: a latent class analysis of trading and gambling behaviors among retail investors. Public Health, 244, 105742. DOI 10.1016/j.puhe.2025.105742.
- Read status: partial (abstract and front matter read from the Zaragoza repository PDF).
- What it argues: in a weighted sample of 1,429 Spanish adults, 28.6 percent traded non-professionally; latent classes separate traders who do not gamble from a class that both trades and gambles.
- Bearing: complicates. The trading-gambling overlap is a subgroup, not the population.

lee2026kalshi. Lee, S., Lee, Y. and Lee, J. (2026). Underreaction, salience, and hot-hand beliefs in sports prediction markets: evidence from Kalshi NBA and NFL event contracts. Journal of Behavioral and Experimental Finance, 52, 101259. DOI 10.1016/j.jbef.2026.101259 (SSRN 10.2139/ssrn.6964226).
- Read status: not obtained (metadata only; no abstract in Crossref, OpenAlex or PubMed; Elsevier and SSRN blocked).
- Bearing: unknown. The title says it studies behavioural biases in Kalshi sports contracts, which is the nearest peer-reviewed item to the essay's target. It cannot enter a draft until read.

lei2026manufacturing. Lei, Y. and Rossi, A. G. P. (2026). Manufacturing speculation: contract design and trader performance in prediction markets. SSRN 10.2139/ssrn.7461319. Working paper.
- Read status: not obtained (metadata only).
- Bearing: unknown. The title points at contract design as a driver of trader performance, which is Part 3's design claim stated from the market side. Lead only.

Leads logged and not entered (no abstract retrievable, or outside this facet): Wang (SSRN 6624899, 273 top Polymarket traders); Curtin (SSRN 7115858); Perez (SSRN 7239999, taker delays in in-play event contracts); Mace and Johnson (SSRN 7546718, adverse selection in sports prediction markets); Holden, Turk and Edelman (SSRN 6350738, Regulating Sports Prediction Markets); Michels, Ötting and Langrock (EJOR 2023, in-game betting reactions, no abstract retrieved); Bürgi, Deng and Whelan (CESifo 12122, Kalshi favorite-longshot bias; Facet A/D).

---

## (c) Synthesis

B1: what the interface literature shows. Three lines of evidence converge on a modest, real, contested effect. The classic overtrading results (Barber and Odean 2000, 2002) show that more active trading costs retail investors and that moving online made trading more speculative. The app-era studies show that smartphone trading raises risk-taking and return chasing (Kalda et al. 2021; Cen 2024), though Liu et al. (2025) find no net performance change. The experiments on gamification find that confetti, badges and leaderboards raise volume and risk-taking (Chapkovski et al. 2024, 2025; Hüller et al. 2023), but Chapkovski et al. attribute 70 percent of the gamified-versus-plain difference in trading activity to self-selection, and Kalda et al. show by falsification that the smartphone effect appears in asset classes the apps do not feature, so salience nudges alone do not explain it. The sports-betting literature supplies the most direct evidence on marketing messages: Rockloff et al. (2026) randomised 405 regular bettors to opt out of all operator direct marketing and, in the 227 who completed follow-up, found 23 percent fewer bets, 39 percent less spending and 67 percent fewer short-term harms, in analyses the authors call exploratory. Live, in-play and micro-event features are associated with higher problem-gambling severity, and young higher-risk bettors rate in-play betting and frequent promotions as more important (Hing et al. 2024), but every study of these features is cross-sectional, exploratory or a stated preference. The near-miss literature is split and was built on slot machines. For Part 3 this means one can say that gamified and continuous betting interfaces plausibly raise risk-taking, and that direct marketing has causal support from one field experiment. One cannot yet say which feature does the work in a prediction-market app.

B2: dark patterns. The general literature establishes prevalence (Mathur et al. 2019: 1,818 instances on 1,254 of about 11K shopping sites), large effects on choice (Luguri and Strahilevitz 2021: 11.3 to 25.8 to 41.9 percent acceptance across control, mild and aggressive conditions), broad susceptibility and a role for single-click completion (Zac et al. 2025). Gray et al. (2018) supply the design-ethics frame. For gambling, McGarrigle et al. (2026) catalogue the patterns across 16 records and report that behavioural evidence is thin. I found no study of dark patterns in a prediction-market or event-contract interface; Rohanifar et al. (2026) audit Polymarket's governance and aggregation, not its bet slip.

B3: learning versus noise. The evidence points both ways. Experience improves some investors (Nicolosi et al. 2009), but Seru et al. (2010) show that learning estimates are two to four times too high when attrition is ignored, because much of the aggregate improvement is low-ability traders leaving, and day traders keep losing despite many rounds of feedback (Barber et al. 2020). Simple outcome feedback does little for probability judgment (Benson and Önkal 1992, not re-read this session); calibration feedback and structured training do better (Stone and Opel 2000; Mellers et al. 2014; Chang et al. 2016), though Hauenstein et al. (2025) find the teaming and training effects eliminated, reduced or reversed once method variance is modelled, and Martin and Mandel (2025) find no calibration gain from scoring-rule feedback. Price-trend notifications can reinforce mistakes in people with wrong beliefs (Chapkovski et al. 2024, abstract). The design implication for Part 3 is that a market interface returns outcome feedback, which is the weak kind, and not the calibration feedback that the forecasting literature uses.

B4: event-contract platforms. One qualitative study shows r/Kalshi users struggling to read the platform's probability charts and explaining to each other that the displayed percentage is a last trade or a midpoint (Sah et al. 2026, preprint). One review names substitution between sports betting and prediction markets as an open question (Baker et al. 2026). One peer-reviewed paper on behavioural bias in Kalshi sports contracts exists but could not be read (Lee, Lee and Lee 2026). No study measures how an event-contract interface changes what users do.

---

## (d) Gaps

- No study in this facet measures user behaviour against an interface variable on Polymarket, Kalshi or any event-contract platform. The gap search (rows 31 to 56) found one qualitative reading study (Sah et al. 2026), one qualitative audit (Rohanifar et al. 2026), one review (Baker et al. 2026) and one unread paper on Kalshi sports contracts (Lee et al. 2026).
- No empirical study of sports bettors migrating to prediction-market apps was found; Baker et al. (2026) state the substitution question as open.
- Causal evidence on confetti, streaks and one-tap trading specifically is missing. Streak mechanics as a designed feature matched no record; Banerjee et al. (2025) study outcome streaks. Same-game parlays matched only pricing studies. Cash-out has one correlational study (Sinclair et al. 2024) and one registered experiment without results (Szászi et al. 2024).
- Full text was not obtained for 22 of 55 original entries, including Chapkovski et al. 2024, whose 5.17 percent and 70/30 decomposition are confirmed only at abstract level, and Hüller et al. 2023, whose N = 3,766 is unverified.
- Scholar Gateway failed in the first build and was not retried; CORE was unusable; Wayback was offline.

## (e) Verify list

All items from the first build are resolved.

- Luguri and Strahilevitz, Journal of Legal Analysis 2021: 13(1), 43–109, DOI 10.1093/jla/laaa006. Cleared.
- Welch, Journal of Finance 2022: 77(3), 1489–1527, DOI 10.1111/jofi.13128. Cleared.
- Barber and Odean, Journal of Finance 2000: 55(2), 773–806, DOI 10.1111/0022-1082.00226; Review of Financial Studies 2002: 15(2), 455–488, DOI 10.1093/rfs/15.2.455. Cleared.
- Odean, American Economic Review 1999: 89(5), 1279–1298, DOI 10.1257/aer.89.5.1279. Cleared.
- Kalda et al. published version: none in Crossref; NBER w28363 and SSRN 3765652 and 3772602 only. Full author list: Kalda, Loos, Previtero, Hackethal. Cleared as a working paper.
- Full author lists for every entry: all 55 now carry complete lists from Crossref.
- Gainsbury and Newall works on betting apps beyond the 2022 gamblification paper: Newall appears as co-author on Mosenhauer 2021, Hing 2022, 2023, 2024, Rockloff 2026 and Torrance 2024, all now in the bib. No Gainsbury paper was sought in verification; the gap search did not surface one.
- Any Welch paper on Robinhood gamification: none exists in Crossref under Welch's name; the NBER text has no gamification content. Closed.
- Streak mechanics in trading or betting apps: no study identified in Crossref or OpenAlex (row 52). Closed as a documented gap.
- Tetlock and Gardner, Superforecasting (book): not searched; not needed, since Tetlock et al. 2014 and Mellers et al. 2014 are in the bib.

Still open after verification: full text of Chapkovski et al. 2024 (for N, platform, rounds and the decomposition table); full text of Lee, Lee and Lee 2026 (Kalshi sports contracts); N = 3,766 in Hüller et al. 2023; abstracts of Bregu 2020 and Benson and Önkal 1992 were not re-read.

## (f) Changes in verification (2026-10-03, local session)

Metadata corrected in the bib:
- Fifteen entries now carry the journal issue year rather than the online-first year the first build used: Chapkovski et al. 2026 (not 2024), Cen 2024 (not 2023), Liu et al. 2025 (not 2024), Hing et al. 2024 (not 2022, the 'Immediate access' paper), Killick and Griffiths 2019, Russell et al. 2019, Pisklak et al. 2020, Harris and Griffiths 2017, Torrance et al. 2024, Quintero Garzola and Vaccarino 2024, Sin et al. 2025, Moore et al. 2017, Hauenstein et al. 2025, Martin and Mandel 2025, Barber et al. 2020 (Learning, fast or slow). Citekeys are unchanged; in-text years in the outline should follow the bib.
- Seven entries moved from a preprint, SSRN or reprint DOI to the journal DOI: Barber and Odean 2000 and 2002, Odean 1999, Seru et al. 2010, Luguri and Strahilevitz 2021, Welch 2022, Cowgill and Zitzewitz 2015 (the first build's EC 2014 DOI is a one-page abstract). Preprint DOIs are kept in the notes.
- Journal name corrected: Bregu 2020 is in the Journal of Behavioral and Experimental Economics.
- Full author lists replace "and others" in all 55 entries; author counts range from one (Welch, Cen, Bregu) to thirteen (Mellers et al.).
- Volume, issue and pages added to every journal entry that lacked them.
- Mathur et al. title completed with its subtitle; Gray et al. given its CHI paper number; Chaudhry and Kulkarni given DIS pages.
- Kalda et al.: OpenAlex's link to an RFS DOI is a merge error; the paper remains an NBER working paper.

Summaries corrected where full text or the publisher abstract differed:
- Kalda et al.: "rule out nudges" became "show by falsification that app-specific nudges do not drive the effect, while unable to observe the apps' displays."
- Rockloff et al.: n = 227 is the analysed sample after attrition from 405 enrolled; the authors call the analysis exploratory and had no pre-registered analysis plan; the treatment removed all direct marketing, not push notifications alone. The three percentages are confirmed verbatim and are relative differences in per-48-hour means.
- Chapkovski et al. 2024: the 70 percent is confirmed from the publisher abstract as the share of the gamified-versus-plain difference in trading activity due to self-selection; design details beyond "randomized online experiment" remain unverified.
- Seru et al.: the attrition claim now carries the paper's own quantification (estimates two to four times higher without adjustment; 3.6 bp per 100 trades after adjustment).
- Hauenstein et al.: the exact phrase is "substantially eliminated, reduced, and, in some cases, even reversed"; the paper reports no single effect size.
- Luguri and Strahilevitz: acceptance rates 11.3, 25.8 and 41.9 percent and the samples (1,963 and 3,777) added; the "doubled" and "quadrupled" phrasing is the authors'.
- Mathur et al.: 1,254 sites (11.1 percent) and 234 deceptive instances added.
- McGarrigle et al.: the 16 records split into 7 grey and 9 peer-reviewed, 2018 to 2025.
- Hing et al. 2025: 814 participants behind the 4,020 observations; message counts added.
- Cowgill and Zitzewitz: optimism bias is at Google in the abstract, not "Google and Ford."
- Zac et al.: "single click," not "one-click."
- Hing et al. 2019: 722 bettors, 316 race and 279 sports analysed; EMA design.
- Russell et al.: comparison rates (29 and 28 percent for non-micro-event bettors) added.
- Welch: confirmed from full text that the paper contains no gamification analysis.
- Hüller et al.: N = 3,766 flagged as unverified.

Added: section B4 with eleven entries from the gap search (nine with text read, two metadata only) and a list of seven leads not entered.
