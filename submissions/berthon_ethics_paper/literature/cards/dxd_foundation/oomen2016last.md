# Oomen, R. (2017). Last look. *Quantitative Finance, 17*(7), 1057–1070 (online 2016).

**Identifier:** doi:10.1080/14697688.2016.1262545 · **Read depth:** full_text of the accepted manuscript dated November 2016 (LSE Research Online, eprints.lse.ac.uk/68811; 28 PDF pages; locators are the manuscript's own page numbers, not the journal's). Sections 1–5 read; the appendix proofs of Proposition 1 and Theorem 1 skimmed · **Source-tier:** peer-reviewed article (accepted version) · **Evidence basis:** direct_read · **Design and sample:** an analytical model with simulated parameters; no market data · **Parties modeled:** two parties plus a rule-holder (a trader, N competing liquidity providers, and an aggregator; the provider that wins the request decides whether it is filled) · **Facets:** J · **Read:** 2026-10-13

## What it argues
In over-the-counter foreign exchange, a trader shows a deal request to the liquidity provider (LP) whose quote looks best. Because prices move during the round trip, the LP applies a "last look" rule that accepts or rejects the request. Oomen's starting point is that "the liquidity provider owns finality of the deal" (p. 1). The accepted manuscript carries a footnote saying he is global co-head of electronic FX spot trading at Deutsche Bank.

The model follows his earlier "Execution in an aggregator" (§2, not read). The true price follows a random walk. Each of N identical LPs observes it with persistent error, and the uninformed trader sends each request to the LP showing the best price. That routing selects the LP whose error is largest in the trader's favour, so the LP "is adversely selected" (§3.1). The trader sees an inside spread tighter than any single LP's, and with enough LPs it turns negative; without last look that would be a sure arbitrage (§2).

He defines one-sided last look (reject only on moves against the LP) and two-sided last look (also reject, or rebate, on moves in the LP's favour), and two protocols: trade "on rate" (certain price, uncertain fill) or "on latest" (certain fill, uncertain price). "Symmetric" last look turns out to have four rival meanings: equal tolerance levels, equal reject rates, equal incurred costs and revenues, equal foregone costs and revenues. Only equal tolerance is always available, and under adverse selection the four cannot hold together (§3.1). His worked case uses N = 15 LPs, nominal spread 1, one time unit of latency buffer, and measurement-error and price volatility of 0.5. A tolerance of 0.5 on the LP's side rejects 28.5% of requests, and a second tolerance of 0.5 on the trader's side rejects another 14.1%. Raising both tolerances to 1 cuts those rates to 8.1% and 2.9% (§3.1).

The two findings in his abstract: the choice of design and protocol sets execution risk, but the trader's effective transaction cost "need not be affected by it". When the trader's flow strongly selects against the LP (his stress case: N = 25), the symmetric and asymmetric designs converge and the choice of protocol dominates (§4). He concludes that the choice of last look "is not an issue of fairness, but one of preference over liquidity access, trading style, and tolerance to execution risk" (p. 4), and that no single design is superior or inferior (§5).

## Relation to the argument
Ruling D8 (courts, FX markets, platforms; where does the convention bend). The paper is the rule-holder's account of a rule that gives one party the last word. Two points matter for the paper.

First, it reports that the rule is configurable and negotiable per client: liquidity "is bespoke to the trader" (§2), and a trader can remove uncertainty of rate, of execution, or both by choosing protocol and configuration (§1, p. 4). That shows a convention in a market that is neither fixed nor imposed whole. Second, it recasts a dispute about fairness as one about risk allocation, from the party that benefits. The same recasting would suit a platform defending its terms. The paper offers no evidence on who gains in practice.

Facet check: the facet says the paper "contradicts a reading in which last look is simply a dealer privilege". Fully read, the claim is narrower. Under the model, equal effective spreads can be reached by any combination of design and protocol. In the benign-flow case of Figure 8 (§4), Oomen says the designs "can lead to materially different execution risk profiles despite attaining the same effective spread", so the trader's risk is where the rules differ. The equivalence also depends on competing LPs and uninformed flow. The facet gives the published year as 2017, which fits the volume; the bib says 2016, the online date.

## In conversation with
Oomen cites no work in `references.bib` (the 2016 manuscript predates the FX Global Code, `globalfxc2024code`, and the Barclays consent order, `nydfs2015barclays`, which concern the same practice but are not cited here). Leads from his list, not in the bib: Bank of England, H.M. Treasury and FCA (2015), the Fair and Effective Markets Review; Norges Bank Investment Management (2015) on last look; Cartea, Jaimungal and Walton (2015), "Foreign exchange markets with last look"; Budish, Cramton and Shim (2015) on the high-frequency arms race; Kyle (1985) for the noise-trader assumption.

## Caution
A model with identical LPs, an uninformed trader, a random-walk price and invented parameters (figures are simulations, not observed FX data). The author's employer is a dealer that uses last look. This is the accepted manuscript, whose cover notice (LSE) says "There may be differences between this version and the published version"; I did not check the published pages. I did not work through the proofs.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The LSE accepted manuscript (cards/oomen2016last.pdf, 29 PDF pages; manuscript page = PDF page minus 2). Eight quotations (p. 1 "owns finality", p. 4 "not an issue of fairness", "need not be affected by it", "is adversely selected", "bespoke", "materially different execution risk profiles...", no single design superior), all of the worked numbers (N = 15, 28.5%, 14.1%, 8.1%, 2.9%, N = 25 stress case), the four-symmetry claim, the Deutsche Bank footnote and the cited leads checked.

**Findings:** No issues found. The only caveat: the card says full_text with the appendix proofs skimmed; that is about three of 28 pages and the card states it, so I left the label. The published volume and page numbers (17(7), 1057-1070) are not in the manuscript and were not checked.
