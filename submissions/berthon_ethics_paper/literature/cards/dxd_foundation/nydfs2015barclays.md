# New York State Department of Financial Services. (2015, November 17). *In the Matter of Barclays Bank PLC, Barclays Bank PLC, New York Branch: Consent Order under New York Banking Law § 44.*

**Identifier:** https://www.dfs.ny.gov/system/files/documents/2020/04/ea151117_barclays.pdf · **Read depth:** full_text (14-page consent order; the signature block is dated "/7 day of November, 2015" in the scan, and the DFS press release is dated 18 November 2015; the bib gives 18 November) · **Source-tier:** regulator order (consent order) · **Evidence basis:** direct_read · **Design and sample:** none; a negotiated settlement with stipulated facts, not an adjudicated finding · **Parties modeled:** two parties + a dealer-controlled mechanism (clients and Barclays as counterparty; the regulator as third party) · **Facets:** J · **Read:** 2026-10-13

## What it argues

Barclays operated BARX, an electronic FX platform; about 80% of its FX volume was electronic (¶4). Some orders were subject to "Last Look," "an automated function that delays the Bank's response to a counterparty's incoming client orders for a set period of time — called the 'hold time' — and rejects the order if the market price moves beyond a certain threshold" (recitals, p. 2). From at least 2009 to 2014 Barclays says it meant Last Look as a defence against stale prices and "latency arbitrage" (recitals). The recitals state that Barclays "failed to properly use Last Look due to the failure of systems and controls, including management oversight," employed it "broadly and indiscriminately," and "there was a lack of transparency both internally and with customers" (recitals, p. 2).

The facts stipulated: Barclays applied Last Look to all FIX/API trades and a few GUI clients, assigning an undisclosed hold time (¶¶10–12). It treated trades as toxic "[w]henever prices within this holding period moved against Barclays and in favor of the customer beyond a certain undisclosed loss threshold" (¶13), so it applied the rule "almost entirely in reference to the profit or loss the trade would bring to the Bank" (¶14), and "did not perform an analysis" to confine rejections to real toxic flow (¶15). In September–October 2014, after the investigation began, Barclays made the filter symmetric; one platform carrying 7% of volume stayed asymmetric until August 2015 (¶¶17–18). Stop-loss orders also faced Last Look holds (¶¶19–22).

On communication, a rejected client saw only "NACK" ("Not Acknowledged"), with no reason (¶24). The order quotes internal emails: a 2008 instruction to say the trade "WAS REJECTED BECAUSE OF LATENCY" and "DO NOT talk about P&L"; a 2013 instruction to name all rejects "NACK urgently . . . Clients are gonna come asking"; a 2014 line, "Our Team generally does not share this info with the client, and just say it was a business reject" (¶25). A client who wrote in 2010 about "over 300 rejected orders" in a day got no response on record (¶25b). A marketing deck said "No last look — what you see is what you get" without separating the GUI from FIX/API (¶27). Some sophisticated clients tracked their own rejection rates and, when they complained, got adjusted hold times (¶26).

Remedies: a $150,000,000 civil penalty (¶30); an employee suspended and ordered terminated (¶31); a monitor until 19 February 2016, with a remediation plan covering change management and periodic review of FX system settings (¶¶34–35). The order finds only that the Bank conducted business "in an unsafe and unsound manner" (¶29). Paragraph 38 states that no provision "is subject to review in any court or tribunal outside the Department."

## Relation to the argument

Under ruling D8 the paper compares who holds the convention in FX markets with platforms. This order is the clearest dated instance in the batch of a dealer using an unreviewable discretion against clients and the regulator, not the client, supplying the redress. It supports premise P10's logic in a financial setting: the intermediary's rule served its own profit, a client could not see the rule, and a convention was changed only after investigation. It also bears on ruling D3. The informed clients (those who tracked rejection rates) did get hold times adjusted, so some reading helped, but the asymmetric rule continued for years and ran in the Bank's favour; the fix was a change to the rule's symmetry, which the clients could not make themselves. That is mixed evidence for "disclosure is a literacy intervention."

Facet check: the J-facet reading of the recitals, ¶13, ¶24 and ¶25 matches the order. The facet describes the order as dated 18 Nov 2015; the order is signed in November 2015 (day unclear in the scan) and the Department announced it on 18 November.

## In conversation with

- `nydfs2015barclayspr`: the Department's press release of the same matter, which repeats the facts and adds a quotation from the Acting Superintendent.
- `fca2014fines` and `cftc2017fxcm`: other regulator actions on dealers' conduct toward clients in FX.
- The order refers to a May 2015 NYDFS consent order with Barclays on benchmark FX manipulation (recitals); not in the bib. The order cites no scholarship. `oomen2016last` (a paper on last look in the bib) concerns the same practice but is not cited here.

## Caution

A settlement: Barclays "states" its purpose was defensive (recitals), and the order makes no finding of fraud, only "unsafe and unsound" conduct (¶29). It covers one bank and 2009–2014. It does not give rejection rates, client losses or the size of thresholds. The remedy terms bind the Department and Barclays, not other agencies (¶39).

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the 14-page DFS PDF (consent order dated November 2015, signature day garbled as '/7' in the scan). Checked 13 quotations word for word and about 25 factual claims by paragraph number (80%, ,000,000, 7% until August 2015, monitor to 19 Feb 2016, NACK, 300 rejected orders, the 2008, 2013 and 2014 emails, paras 4, 10-15, 17-27, 29-31, 34-35, 38-39).

**Findings:** One overstatement fixed: the card said 'The Department finds that Barclays failed to properly use Last Look...'. Those statements are WHEREAS recitals in a negotiated consent order, not findings; the card now says 'The recitals state'. Quotations, numbers and paragraph locators match. The 'disclosure is a literacy intervention' phrase is the project's wording, not the order's.
