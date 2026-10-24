# Alfrink, K., Keller, I., Kortuem, G., & Doorn, N. (2023). Contestable AI by design: Towards a framework. *Minds and Machines, 33*(4), 613–639. https://doi.org/10.1007/s11023-022-09611-z

**Identifier:** doi:10.1007/s11023-022-09611-z · **Read depth:** full_text (published open-access PDF, 27 pages; online 13 Aug 2022, in print volume 33 (2023); pagination is the journal's, 613–639; I read the whole text, including Tables 2–4 and the reference list, and saw Figure 1 as an image; Figures 2 and 3 are diagrams I looked at only through the captions and the text that describes them) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** literature synthesis. A Scopus search (2016–2021; terms for contestability, AI and design), backward and forward snowballing, and reflexive thematic analysis in Atlas.ti with visual mapping; 19 sources included; no data from users and no test of the framework · **Parties modeled:** other (a decision subject, a human controller, a system developer and a third-party overseer around an automated decision system) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Alfrink and colleagues want contestability, the property of being "open and responsive to human intervention throughout their lifecycle", to be usable by designers (p. 614). The paper turns the literature into a design framework: five system features and six development practices. The features are built-in safeguards, interactive control over decisions, explanations of system behaviour, human review and intervention requests, and tools for scrutiny by subjects or third parties (p. 614). The practices are ex-ante safeguards, agonistic approaches to ML development, quality assurance during development and after deployment, risk mitigation, and third-party oversight (p. 614).

The method is a systematic review. Figure 1 (p. 620) counts 1,600 Scopus records and 1,128 more from snowballing, 21 duplicates removed, 2,707 screened, 2,581 excluded, 126 full texts assessed, 107 excluded, and 19 included. Table 2 maps those 19 sources to the features and practices (pp. 633–634). Figure 2 (p. 629) ties the features to actors, and Figure 3 (p. 630) ties the practices to the lifecycle stages of an audit framework.

Several statements bear on this project. Contestation takes more than a person at the end: "A 'human in the loop' is insufficient if there is no possibility of a 'dialectical exchange' between decision subject and human controller" (p. 615, the authors summarising Sarra 2020). Contest depends on explanation, since a defence is "an articulate act of defense" that requires arguments, and "arguments need information" (p. 615), and the explanations they ask for describe "the decision rules", a "behavioral model of the AI system as a whole", not only the computation (p. 621). They name user education as one strategy within the risk-mitigation practice (p. 628), and name third-party oversight, including trusted intermediaries who hold sensitive material (p. 628). They note that certification schemes "are typically run in a for-profit manner and depend on voluntary participation by organizations. As such they struggle with enforcement" (p. 625).

On evidence, the authors say plainly: "The framework has been developed based on a small sample of academic papers," many "not based on empirically validated interventions," and "The validation itself was not part of this paper" (p. 631). They exclude "extreme high stakes" and time-critical settings (p. 631).

## Relation to the argument

**Ruling D3 and premise P9.** The framework treats explanation as an input to contest, not as a means of navigating. That fits D3's wording: disclosure serves a different purpose from the ability to steer through the system. It also shows that the contestability literature does not sort cleanly into D3's two layers. Explanations and user education (literacy-side) sit beside independent adversarial systems, formal constraints and third-party audit (closer to the algorithmacy side) in a single list. Nothing here measures whether any of the ten elements changes what people do, so it cannot support or undercut P9's claim about weaker effects of read-or-tune aids.

**Ruling D8 and premise P10.** The framework names who holds the safeguard: developers, controllers, and above all third parties. Its remark on for-profit certification is the nearest statement in this batch to the question the paper leaves open ("we just dont know yet" who holds the convention). It supplies a candidate, third-party oversight, and one stated weakness of a particular version of it. It does not test either.

**What it cuts.** The "human in the loop" is called insufficient without authority and a dialogue (p. 615, p. 623). That bears on how the Nadella post leaves a person to read and halt (P11).

**Facet check:** the facet says "abstract only... No measured effects." The full text confirms there are no measured effects and adds the screening counts above. The facet's note that Crossref dates the paper 2022 while the key says 2023 is right: online 2022, volume year 2023.

## In conversation with

- `lyons2021conceptualising` — in the reviewed set; cited on the need for contest channels and for due process designed into the system (pp. 621–625).
- `vaccaro2020end` — in the reviewed set (Vaccaro, Sandvig & Karahalios 2020); used for scaffolding and for aids that ease appeals (p. 623).
- `vaccaro2021contestability` — in the reviewed set; cited on third-party representation and channels for contest (p. 623).
- `kroll2021outlining` — the framework cites Kroll et al. (2016) on zero-knowledge proofs (p. 625), a different work; do not equate.
- Not in the bib, as leads: Vaccaro et al. (2019), "Contestability in algorithmic systems"; Hirsch et al. (2017), "Designing contestability"; Almada (2019) on human intervention in automated decisions; Sarra (2020) on contest and explanation; Henin & Le Métayer (2021).

## Caution

A conceptual framework drawn from 19 papers, most of them not empirical, by the authors' own account. No test with users or designers. The framework assumes a generic automated decision with a significant impact on a subject; it is not about platforms mediating between two parties, and it does not address cases where the system's owner has a stake in the outcome beyond the decision.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the published open-access PDF (27 pp.; pdf page 1 = journal p. 613); extracted text page by page; viewed Figure 1 as an image. Checked 12 quotations with locators, the Figure 1 counts (1,600; 1,128; 21; 2,707; 2,581; 126; 107; 19), the five features and six practices, and the named works in the reference list.

**Findings:** (1) Overstated claim: the card said the authors 'list educating users as one of six practices (p. 628)'. The six practices are ex-ante safeguards, agonistic approaches, QA during development, QA after deployment, risk mitigation, third-party oversight; user education is one strategy under 'Risk Mitigation Strategies' (6.2.5, p. 628). Corrected. (2) Locator: the second 'human in the loop' passage ('mere presence of a human at the very end of the chain') is on p. 623, not p. 622. Corrected. All other quotations and the Figure 1 numbers match. Lyons/Vaccaro relations confirmed from the text and reference list; Kroll et al. (2016) is cited for zero-knowledge proofs, as the card says.
