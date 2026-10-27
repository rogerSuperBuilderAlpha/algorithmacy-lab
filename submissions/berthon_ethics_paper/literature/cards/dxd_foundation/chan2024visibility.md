# Chan, A., Ezell, C., Kaufmann, M., Wei, K., Hammond, L., Bradley, H., Bluemke, E., Rajkumar, N., Krueger, D., Kolt, N., Heim, L., & Anderljung, M. (2024). Visibility into AI agents. In *Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)* (pp. 958–973). ACM.

**Identifier:** doi:10.1145/3630106.3658948 · arXiv:2401.13138 · **Read depth:** full_text (arXiv v6, 17 May 2024; locators are PDF pages of this 16-page layout, not the proceedings pages 958–973; body and Appendix A read, reference list searched for the works named below) · **Source-tier:** proceedings paper (policy analysis) · **Evidence basis:** direct_read · **Design and sample:** none; a conceptual assessment of three governance measures, no data · **Parties modeled:** other: deployer, user, counterparty or tool provider, and regulator around one agent · **Facets:** G · **Read:** 2026-10-13

## What it argues
The authors define visibility as "Information about where, why, how, and by whom certain AI agents are used" (p. 1) and prefer it to "transparency" (footnote 5, p. 3). They assess three measures, each at several levels of intrusiveness: agent identifiers, real-time monitoring and activity logs (p. 3, Fig. 2).

- **Identifiers** mark which agent took part in an interaction. They can be visible to "the bank, the other party in the transaction, or the service provider" (p. 5), and can carry an "agent card" of evaluations, permissions, goals and responsible actors (pp. 6–7; Appendix A, p. 16).
- **Real-time monitoring** "is likely to be automated so as to be able to cope with the speed and scale of agent activities" (p. 7). It suits clear-rule violations. A user "could be given the opportunity to request human review", but the authors write: "We leave details about the implementation challenges of automation and human review to other work" and cite four works there, among them Green (2022) and three on algorithmic recourse (refs. 72, 95, 157, 166; p. 7).
- **Activity logs** support "post-incident attribution and forensics" (p. 7) and may need keeping long after an agent's life (p. 8).

All three assume a deployer: "Since deployers run agents, the inputs and outputs of agents are by default visible to the deployer" (Fig. 1 caption, p. 5). Section 4 extends the measures to agents that bypass deployers, through compute providers and through tool providers that refuse unidentified agents; the authors warn that both routes concentrate power and invite surveillance (pp. 8–9). They are not "advocating for immediate implementation" (p. 3). The conclusion limits the whole proposal: visibility "is not by itself sufficient", because those harmed "may not have the power to intervene and reduce risks", a point they take from Ananny and Crawford (p. 10).

Among their risks, agents "could also subtly benefit their developers, akin to the self-preferencing behaviour of large-scale digital platforms" (p. 2).

## Relation to the argument
**D3/D4 (disclosure versus control).** The paper is a disclosure-and-record proposal, and it states its own limit: knowing who runs which agent does not give the affected party power. That supports the author's D3 in spirit (visibility is a different thing from the ability to act), but it does not support D4's "his only move is disclosure": the AI-governance lineage that Nadella's post sits in pairs visibility with filtering and intervention (real-time monitoring, p. 7). The 2025 sequel (`chan2025infrastructure`) adds explicit control layers.

**P10/D8 (who holds the convention).** The architecture hands the deployer the data and the switch: identifiers are attached by the deployer, monitoring is run by the deployer, logs are kept by the deployer (p. 5). The self-preferencing line (p. 2) and the concentration warnings (pp. 8–9) name the conflict of interest that P10 needs, though only as a risk and without a test.

**P11/P12.** Chan separates automated monitoring from human review and leaves human review unexamined (p. 7). Nadella's P15 puts a person at that point; this paper supplies a gap, not a result.

**Triad (D9).** Counterparties appear only as recipients of an identifier (p. 5); the agent is assumed to serve its user.

**Facet check:** the facet reading (identifier visible to the other party; human review left to "other work", citing Green) holds. The facet says Chan reaches counterparties where the post faces the enterprise only; in Chan the counterparty sees the identifier and agent card, not the monitoring or logs. The bib note says sections 4–5 and the appendix were unread; I read them.

## In conversation with
- `green2022flaws`: cited for the unsolved problem of human review of flagged actions (p. 7).
- `ananny2018seeing`: cited for the point that those harmed may lack power to act on what they can see (p. 10).
- `greenblatt2024ai`: cited (with ref. 147) for the claim that real-time monitoring is likely to be automated (p. 7); the paper's own example of a preliminary monitoring system is Naihin et al.
- Leads not in the bib: Shavit et al. (2023) on practices for governing agentic systems; Raji et al. (2022) on outsider oversight and auditing; Kolt (2024) on governing AI agents.

## Caution
A policy analysis with no data; it lists options and says it does not choose among them. It covers agents run by deployers and, briefly, decentralised ones, not people coordinating through a platform's algorithm. Cite it for the measures and for the authors' admitted limit, not for any claim that visibility changes what people do. The arXiv v6 text may differ in small ways from the FAccT proceedings version.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** the arXiv v6 PDF (16 pages) from the cards folder; title, authors, version match. About 16 quotations with PDF-page locators (definition, footnote 5, deployer sentence, automated monitoring, human review deferral, advocating, "not by itself sufficient", self-preferencing), and the named references (Green, Ananny and Crawford, Greenblatt, Shavit, Raji, Kolt) against the text and reference list.

**Findings:** Two attribution errors fixed. (1) The human-review deferral cites four works (refs. 72, 95, 157, 166: Green 2022 plus three algorithmic-recourse papers), not Green alone. (2) Greenblatt et al. (ref. 74) is cited for the claim that monitoring will be automated, not as "an existing real-time monitoring scheme"; the paper's preliminary-implementation example is Naihin et al. All quotations are exact. I did not recheck the claim that the bib note said sections 4-5 were unread.
