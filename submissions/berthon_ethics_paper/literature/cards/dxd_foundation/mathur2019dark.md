# Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. *Proceedings of the ACM on Human-Computer Interaction, 3*(CSCW), Article 81.

**Identifier:** doi:10.1145/3359183 · arXiv:1907.07032 · **Read depth:** full_text of arXiv v2 (20 September 2019), in the ACM layout; locators are section numbers, plus the article's page numbers (81:N) where I could read them. Appendix tables and the reference list skimmed · **Source-tier:** peer-reviewed proceedings paper (preprint read) · **Evidence basis:** direct_read · **Design and sample:** automated crawl of English-language shopping sites (11,286 sites, 53,180 product pages), text-segment clustering, manual coding by researchers; no user study · **Parties modeled:** other (a site's operator and its shoppers; a third-party vendor that supplies the operator) · **Facets:** X · **Read:** 2026-10-13

## What it argues
The authors define dark patterns as "user interface design choices that benefit an online service by coercing, steering, or deceiving users into making unintended and potentially harmful decisions" (abstract). Earlier work gave taxonomies built from anecdotes or user submissions; this paper measures prevalence (§1, §2.3).

Method (§4). They took 361,102 popular sites, classified shopping sites with WebShrinker, kept 19,455 in English, and crawled 11,286 of them. A product-page classifier reached 83% accuracy by cross-validation; the crawler returned legitimate product pages for 86 of 100 sampled sites and reached the checkout page on 66 of 100 sampled product pages. About 13 million text segments reduced to roughly 1.3 million unique ones and, after PCA and HDBSCAN, to 10,277 clusters. One researcher reduced these to 1,768 clusters of interest, and two researchers independently coded a sample of 200 (Cohen's kappa 0.74). Dynamic patterns such as countdown timers were revisited every four hours for five days to check for deception (§4.4).

Results (§5). They found 1,818 dark-pattern instances of 15 types in 7 categories on 1,254 sites, or 11.1% (§1, p. 81:2); this is a lower bound because only text on product, cart and checkout pages was examined. Popular sites carried more (Spearman's rho = −0.62 against Alexa rank, p < 0.0001). Most patterns the authors label "covert, deceptive, and information hiding" and many exploit defaults, framing or scarcity bias. Their taxonomy of characteristics has five dimensions: asymmetric, covert, deceptive, hides information, restrictive (§3, pp. 81:5–81:6). Scarcity messages were the most common type (632 low-stock messages on 581 sites); 234 instances on 183 sites were deceptive, including 157 deceptive countdown timers on 140 sites that reset or kept the offer alive after expiry (§5.1).

They also found a supply side. Twenty-two third-party entities, present on 1,066 of the 11K sites, provide social-proof pop-ups (the paper's own example: ‘Jane from Washington, DC just purchased this product’), and some also offer urgency and scarcity messages. Two advertise fakery: one plugin says it "will create fake orders" (§5.2.2). Shopify temporarily removed one vendor's plugin for enabling fake notifications.

## Relation to the argument
X facet, objection on who makes the move (and premise P10: the owner of an interface does not share its users' interests). Mathur et al. give measured evidence that interface design is used for the operator's gain and that vendors sell it as a service. The definition builds the conflict of interest in: the pattern is one that "benefit[s] an online service".

The study supports a limited reading of the facet's phrase that the designer is "the interested party's instrument". In the data, the instrument is the site's own page or a vendor hired by the operator, and the aggrieved party is the shopper. There are two parties, not a triad with a mediator serving both. The paper measures the operator's side only; it does not show what users did.

It also names a user-side fix and doubts it. A browser extension could flag patterns from their data set (Fig. 10, §6.1), but "finding the right incentives for browser vendors" may be hard because they may be "wary of policing content". That bears on the paper's question of who builds the artefact: a counter-artefact has to come from someone who is neither the operator nor a reluctant platform.

Facet check: the facet reads the study from the abstract and introduction. The full text agrees with its figures (1,818 instances, about 11K sites, 22 third parties). It adds the 11.1% prevalence figure, which is a lower bound and a small minority of sites, and the fact that the cognitive-bias links are unvalidated: the authors say these links "may be more nuanced or complex" (§6.4).

## In conversation with
- `gray2018dark` (Gray et al. 2018): the taxonomy source for the category names Sneaking, Obstruction and Forced Action, which Mathur et al. take and extend (§2.2, §5.1).

Leads from its list, not in the bib: Brignull (2018), darkpatterns.org, the taxonomy that Mathur et al. say coined the term in 2010; Calo (2013), "Digital market manipulation"; Bösch et al. (2016) on privacy "dark strategies"; Moser et al. (2019) on impulse-buying features; Norwegian Consumer Council (2018), *Deceived by Design*.

## Caution
Text-only detection of sites in English; patterns that rely on colour, size or layout were left out, and the checkout was never completed, so post-purchase patterns are missing (§6.4). Prevalence is 11.1% of the sites crawled, not of shopping in general. Coding by researchers with moderate agreement (kappa 0.74 on the validation sample). The paper makes no claim about effects on users. This is arXiv v2; check numbers against the published article before quoting.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened arXiv:1907.07032v2 PDF (title, authors, 20 Sep 2019 match). Checked 8 quotations and about 40 numbers (crawl funnel, classifier accuracy, clusters, kappa, instance counts, 11.1%, Spearman rho, scarcity and timer counts, third-party counts, Shopify removal, section and Fig. 10 locators, cited works).

**Findings:** One quote fixed: the card quoted the social-proof example as 'Jane from Washington just purchased this'. The source (section 5.2.2 discussion of the HAR-file method) reads 'Jane from Washington, DC just purchased this product'; corrected in place. Everything else matched. The 'interested party's instrument' phrase is the facet's wording, which the card attributes to the facet, not to the paper.
