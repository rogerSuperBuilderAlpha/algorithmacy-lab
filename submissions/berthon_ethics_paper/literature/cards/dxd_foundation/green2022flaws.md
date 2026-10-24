# Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review, 45*, Article 105681.

**Identifier:** doi:10.1016/j.clsr.2022.105681 · arXiv:2109.05067 · **Read depth:** full_text (the publisher's open-access PDF, 22 pages, CC BY; the article has no journal page numbers beyond its article number, so locators are PDF pages; the 41-policy appendix and the reference list skimmed). The bib note records an earlier read of arXiv v3; this card is from the published version · **Source-tier:** peer-reviewed article (legal and policy analysis with a literature synthesis) · **Evidence basis:** direct_read · **Design and sample:** a survey of 41 policy documents (23 proposed or passed laws, 8 guidance documents, 10 on two US risk-assessment tools) coded inductively, then a synthesis of experimental and field studies of human–algorithm decision-making (Section 4, pp. 7–9; the article does not describe how those studies were selected) · **Parties modeled:** person–system (a human overseer of an algorithm) inside an agency, with the people decided about as a third party · **Facets:** G, Z · **Read:** 2026-10-13

## What it argues
Green says human-oversight rules "rest on an uninterrogated assumption: that people are able to effectively oversee algorithmic decision-making" (abstract, p. 1). By "human oversight" he means "human judgment at the moment an algorithm renders a specific prediction or decision", not democratic governance (n. 1, p. 2). The policies take three approaches (pp. 4–6): restrict "solely" automated decisions (20 of 41 documents, as in GDPR Art. 22), require human discretion (14 of 41, with the Allegheny family screening tool and COMPAS as the US cases), or require "meaningful" human input (7 of 41).

Flaw 1, people cannot do the oversight (pp. 7–9). "Solely automated" rules are avoided by token human involvement. On discretion, he cites automation bias, skill decay, and studies in which people judge algorithmic quality badly. London police judged facial-recognition matches correct at three times the real rate (p. 8, citing Fussey and Murray), and US judges override release recommendations in ways that raise detention and racial gaps (p. 8). On "meaningful" input, no policy defines the term (p. 8); explanations raise trust in wrong advice, and "Algorithmic transparency similarly reduces people's ability to detect and correct model errors" (p. 8, citing Poursabzi-Sangdeh et al.); automation bias survives training (p. 8).

Flaw 2, the rules legitimise bad algorithms and shift blame (pp. 9–10): the human becomes the "scapegoat" while agency leaders and vendors "have it both ways" (p. 10). He cites the Detroit facial-recognition arrest, where the police chief blamed the investigation, and Wisconsin v. Loomis as examples (pp. 9–11).

Remedy (pp. 11–15). Bainbridge's point applies: "Human overseers are left with a task that is more difficult than their original charge" (p. 11). Better human–algorithm design remains "an open empirical question", with cognitive forcing functions and decision-support tools as directions (p. 11). But he proposes "institutional oversight" in two stages: the agency must justify the algorithm and any proposed human oversight with empirical evidence, including pre-deployment experiments with laypeople and practitioners, and then the justification faces public review and approval, modelled on Cambridge, Massachusetts's surveillance ordinance (pp. 12–14). "The default assumption should be that human oversight is likely to be ineffective, unless proven otherwise" (p. 15).

## Relation to the argument
**P12.** This is the policy-level statement of P12. The argument map lists Green 2022 under "mixed for the rest"; the full text supports P12 for decision-time oversight. The evidence base is secondary: advisory algorithms in courts, policing and child welfare, mostly lab studies and field audits. It covers decision-time oversight, not after-the-fact audit of agent logs, so the map's stated gap (reconstruction by trained auditors, the post's P15) stays open.

**D3/D4 and H.** Green's reading of transparency is severe: explanation and transparency "appear to hinder" overseers (p. 8). This supports D3's direction, with a scope limit. The studies concern a decision-maker given an algorithm's advice, not disclosure of an algorithm to the people it acts on. It also fits the post's P9 and its own D4 flag, but Green does not discuss chain-of-thought.

**P11/P19.** Nadella's person who reads evidence and halts is Green's overseer, and Green's Flaw 2 (blame moves to the frontline human) is the Elish argument applied to policy; he cites `elish2019moral` for it (n. 17, p. 10).

**P10/D8.** Green offers a candidate holder: public approval by a democratically accountable body, with agency justification as the entry condition (pp. 12–14). That belongs in facet J's comparison next to courts and markets. It addresses adoption of an algorithm, not a convention of interface.

**Facet check:** the facet's reading (41 policies; people unable to perform oversight; remedy institutional, "not user engagement") holds. One qualification: Green says better oversight design is possible and an "open empirical question" (p. 11), so he does not say oversight can never work.

## In conversation with
- `bainbridge1983ironies`: the "impossible task" frame, p. 11.
- `parasuraman2010complacency`: automation bias and its persistence after training (pp. 7–8, 11).
- `elish2019moral`: the long pattern of blaming operators (n. 17, p. 10).
- `bucinca2021trust`: cited for cognitive forcing functions (p. 11).
- `poursabzi2021manipulating`: transparency reduces error detection (p. 8).
- `perrow1999normal`: operator error as a product of system structure (p. 11).
- Cited by `chan2024visibility` and `chan2025infrastructure`, both of which leave human review of agent actions to this paper.
- Leads not in the bib: Green and Chen (2019, 2021) on risk assessments and human decisions; Skitka et al. (1999) on automation bias; Veale and Edwards (2018) on GDPR Art. 22; Bansal et al. (2021) on explanations and team performance.

## Caution
Scope is government decision algorithms in street-level bureaucracies; the author says much of the analysis extends to non-government settings (n. 4). The 41 documents were collected by search, not a systematic protocol. The literature synthesis is selective and advocates a position. The author's 2022 survey predates LLM agents.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened cards/green2022flaws.pdf (publisher PDF, CLSR 45, 105681; doi and title match). Checked the 10 in-source quotations by exact match (layout and raw text), the 41 / 23 / 8 / 10 and 20 / 14 / 7 counts, the London facial-recognition three-times figure and Detroit and Loomis passages, footnotes 1, 4 and 17, and the page locators 2, 4-6, 7-11, 12-15 (PDF pages equal the card's locators).

**Findings:** One fix: the Design line called the literature part a 'non-systematic synthesis ... (p. 4)'. The article never uses that label and says nothing about how studies were chosen; p. 4 is the policy-search section. Reworded to a synthesis in Section 4 (pp. 7-9) whose selection method the article does not describe. The three non-matching quotations are the argument map's and the facet's phrases, not the source's. All counts, quotations and locators otherwise match.
