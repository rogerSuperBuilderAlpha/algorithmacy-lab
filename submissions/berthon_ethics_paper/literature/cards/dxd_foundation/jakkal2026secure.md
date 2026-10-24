# Jakkal, V. (2026, March 9). Secure agentic AI for your Frontier Transformation. *Microsoft Security Blog*. https://www.microsoft.com/en-us/security/blog/2026/03/09/secure-agentic-ai-for-your-frontier-transformation/

**Identifier:** URL above · **Read depth:** full_text (saved web page, labelled "6 min read"; the year comes from the text's May 1, 2026 availability date, since the byline shows only "March 9"; locators are section headings) · **Source-tier:** vendor product announcement (corporate blog) · **Evidence basis:** direct_read · **Design and sample:** none · **Parties modeled:** organisation's IT, security and business teams and their agents · **Facets:** G · **Read:** 2026-10-13

## What it argues
Jakkal, Corporate Vice President of Microsoft Security, announces Microsoft Agent 365 and Microsoft 365 E7 ("The Frontier Suite"), generally available May 1, 2026. Customers ask "How do I track and monitor all these agents? How do I know what they are doing?" (opening). Agent 365 is "the control plane for agents": a registry (an inventory of agents), behaviour and performance reports, and "agent risk signals across Microsoft Defender, Entra, and Purview" that help security teams "block agent actions based on agent compromise, sign-in anomalies, and risky data interactions" (section "Agent 365"). Entra "Agent ID gives each agent a unique identity", and Identity Governance "limit[s] agent access to only resources they need" (section "Secure and govern agent access"). Purview "Insider Risk Management extends insider risk protection to agents", with risky interactions "blocked and flagged to data security admins"; "Audit and eDiscovery" treats agents "as auditable entities alongside users and applications"; Communication Compliance detects "and enable[s] human oversight of risky AI communications" (section "Prevent data oversharing"). Prices: Agent 365 $15 per user per month; E7 $99 per user per month.

## Relation to the argument
Premise P11, ruling D5. The page is the product line behind the practices the post names in P8 (identity, least privilege, logs, containment) and the "insider risk" vocabulary of P7. It predates the post by seven months, so the insider framing was Microsoft's product language before Nadella's essay. Every human role it names is an administrator: IT, security, business teams, data security admins. Nothing in it concerns the people an agent acts toward. It describes no approval step for agent actions; it describes blocking on risk signals.

## In conversation with
Context for `nadella2026models`. No citations in the text.

## Caution
Facet check: the bib note says it was read via a WebFetch summary; the full page text was read here. The facet's "blocking after compromise signals is automated" is not stated: the page says security teams use the signals to "block agent actions" and does not say whether a person or the system blocks. A marketing page; no evidence of effect is offered, and "double agents" is its risk metaphor.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The saved HTML page (text extracted). All 14 quotations, the section headings, the prices ($15 and $99 per user per month), the May 1, 2026 date, the "6 min read" and "March 9" byline strings, and the "double agents" phrase.

**Findings:** No factual issues. I fixed one typo ("signals,." became "signals."). The page text shows "March 9" with no year and gives May 1, 2026 for availability, as the card says. The "seven months before the Nadella post" comparison depends on a document I did not open.
