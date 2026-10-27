# Evans, M. D. D. (2018). Forex trading and the WMR Fix. *Journal of Banking & Finance, 87*, 233–247.

**Identifier:** doi:10.1016/j.jbankfin.2017.09.017; MPRA Paper No. 81583 · **Read depth:** partial (changed from full_text at S2: main text and references read, but the model derivation and about 40 pages of appendix tables were skimmed) of the **accepted manuscript** (MPRA Paper No. 81583, dated 25 Sept 2017, marked "forthcoming"), 82 PDF pages. Locators are the manuscript's own page numbers (PDF page minus 1); the journal's pagination is not in the file. Read in full: main text (pp. 1–37) and references. Read: the investigations and WMR-methodology notes of the online appendix (PDF p. 42). Skimmed: the model derivation (PDF pp. 43–53) and the extra tables and figures (PDF pp. 54–82) · **Source-tier:** peer-reviewed article (accepted manuscript) · **Evidence basis:** direct_read · **Design and sample:** a microstructure model with a Fix round, tested on tick data for 21 currency pairs, 2004–2013 (Gain Capital quotes, the 4 pm Fix from Datastream, three months of EBS data in each of 2007, 2010 and 2013); windows of 1–60 minutes against a bootstrap of 10,000 random windows away from the Fix, the ECB Fix and US data releases (pp. 19–20) · **Parties modeled:** other (dealer banks, hedgers and investors, with a benchmark administrator whose rule they all trade against) · **Facets:** J · **Read:** 2026-10-13

## What it argues

Evans asks what banks' trading around the 4 pm London WM/Reuters Fix did to prices. Regulators had fined banks more than $5.6 billion (p. 2), but nobody had measured the market-wide effect. His competitive model has dealers take "Fix orders" from hedgers, trade among themselves and fill the orders at the benchmark. It predicts that Fix orders add volatility only after the Fix, and create no pre-Fix price move and no link between pre- and post-Fix changes (pp. 2–3).

The data disagree. A price change above the bootstrap's 95th percentile should occur one day in twenty (p. 21). Just before the Fix on month-end days it occurs four to twelve times that often at the one-minute horizon, and on JPY/USD and USD/GBP more than ten times (p. 23; Table 2, p. 22 gives 61.5% and 51.7%). Intra-month, the four major pairs run above three times normal (p. 23). He says they "appear to be pervasive across all currency pairs and throughout the decade covered by the sample" (p. 3), though Table 3 has pair-years without them (CHF/EUR in 2012 shows none). Pre- and post-Fix changes correlate negatively: projection coefficients run from -0.07 to -0.61 and are significant at 5% for all but three pairs at one horizon at least, with R² mostly under 0.2 (p. 28). A reversal strategy at month-end Fixes shows Sharpe ratios above one for some horizon in 15 pairs and above two in eight, drawdowns mostly under 2% (p. 33). Evans calls these "economically attractive" but grants that traders could not have known Table 6 at the time. Taking each pair's best pre-2010 specification and measuring it after 2010 gave 3.25% on average (p. 35).

On cause he stops short. Banks' trading data are proprietary, so he cannot test the collusion the FCA and DOJ described. The model fails where information sharing among dealers would matter, and front-running could explain a pattern that survived discovery; he calls this "indirect evidence" (pp. 35–36).

## Relation to the argument

D8 and facet J. The Fix is a convention in the plainest sense: a rule that sets one price which index providers, asset managers and derivatives then use. The method sampled a one-minute window with medians and "took no account of trading volume" (p. 7). Evans shows it coexisted for a decade with a regularity its users could trade on, and records that WM announced a methodology change in October 2014, after the investigations became public (p. 7, n. 9). The FX instance of "who holds the convention" is then a commercial administrator, users as the parties, and an interested participant that moves the price. It does not show that dealers broke a convention; Evans cannot tell competitive trading from collusion.

Facet check: facet J marked this metadata only. (1) The appendix lists the Financial Stability Board among the authorities "investigating the forex trading activities" of banks; the FSB's report says its work "was completely independent of the various conduct investigations" (`fsb2014foreign`, p. 1). (2) Evans finds extraordinary pre-Fix volatility; the FSB, with seven currencies and April–September 2013, finds the rise in average volatility at the Fix "not especially large" (`fsb2014foreign`, p. 18). The measures differ (tail frequency against mean), so they do not strictly conflict.

## In conversation with

- `fca2014fines`: the appendix cites the FCA press release on the £1.1 billion fines (PDF p. 42).
- `fsb2014foreign`: same object, the 4 pm Fix. Neither cites the other.
- Not in the bib: Melvin and Prins (2015), *J. Financial Markets* 22 (the hedging-flow account he extends); Ito and Yamada (2015), NBER WP 21518 (confirms his result on the Tokyo Fix); Saakvitne (2016); Cushing and Madhavan (2000); Vitale (2000).

## Caution

Evans disclosed expert advice to a law firm in an active US case on the Fix (p. 1). The manuscript may differ from the print. The paper never shows who traded. Retail-platform quotes stand in for the interbank market; he checks mid-points against the Fixes and uses EBS spreads for costs (pp. 19, 32). Trading returns are ex post, with half the average EBS inside spread as the cost (p. 32).

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the MPRA accepted-manuscript PDF (83 PDF pages; manuscript page = PDF page minus 1). Searched the 4 quotations from Evans (the other 3 flagged strings are facet or FSB wording) and checked the numbers: $5.6bn, one-day-in-twenty, 61.5% / 51.7% (Table 2), four to twelve times, ten times, three times, projection coefficients -0.07 to -0.61 with three insignificant pairs, R2 below 0.2, Sharpe above one in 15 pairs and above two in eight, drawdowns below 2%, 3.25%, October 2014 WM change (n. 9), the appendix FSB and FCA 1.1bn lines, the expert-advice disclosure (p. 1), and Table 3 (CHF/EUR 2012 = 0).

**Findings:** Three fixes. (1) The card said he 'reports excess tail events in all 21 pairs and every year'; the text (p. 3) says they 'appear to be pervasive across all currency pairs and throughout the decade covered by the sample'; reworded to the source. (2) Table 2 is on p. 22, not p. 21 (p. 21 introduces it); corrected. (3) Read depth changed from full_text to partial because the card itself says the model derivation and about 40 pages of appendix tables were only skimmed. The FSB quotations in the facet check ('was completely independent...', 'not especially large') belong to fsb2014foreign and are checked in that card.
