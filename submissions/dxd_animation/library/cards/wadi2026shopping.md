---
key: wadi2026shopping
apa: "Wadi, D., & Ma, Y. (2026). *Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer* (arXiv:2609.28372). arXiv. https://doi.org/10.48550/arxiv.2609.28372"
authors: "Wadi, Davood; Ma, Yu"
year: 2026
title: "Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer"
venue: "arXiv (econ.GN)"
volume: ""
issue: ""
pages: ""
doi: "10.48550/arxiv.2609.28372"
url: "https://arxiv.org/abs/2609.28372"
type: preprint
facets: [F10]
claims: [c1, c3]
role: support
load: load-bearing
read_depth: partial
object_read: "version: arXiv:2609.28372v2 [econ.GN], 13 Oct 2026, PDF with web appendix (about 58 pages); place: ~/iit-playground/dxd_animation_local/pdfs/wadi2026shopping/ (PDF + .txt + csl.json + openalex.json), fetched from https://arxiv.org/pdf/2609.28372; date: 2026-11-05; sha256: 2a0a762e0e3290b93bcb0c85e0dd190a4794c413eb78386580bf03516f891a09"
verified: corrected
verified_against: "10/10 loci in the arXiv v2 text layer and a pdftotext re-extraction (sha256 2a0a762e...); csl.json (DataCite) + OpenAlex records; PDF title page"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Wadi and Ma ask whether pricing tricks built for human shoppers (a price of $4.99 instead of $5.00, a "20% off" label) still work when an AI agent does the shopping for the consumer. They treat the agent as a "surrogate consumer", a buyer to whom the consumer hands over decision authority. They build "Tool-Lab", a test environment in which an agent must pay a cost, through a tool call, to see each product attribute, and they record what it looks at before it chooses. Across eight commercial language models from three providers (N = 33,704 trials), they find that when all attributes are visible the cues rarely mislead. When looking is costly and the user's instruction is vague ("find the best deal"), most models skip attributes needed to work out unit price, such as cents and weight, and pick the worse product. A specific instruction ("find the lowest price per ounce") mostly prevents this. Two validation studies show the failure lies mainly in what the agent looked at, not in how it calculated. The authors conclude that the agent's heuristic-like choices depend on the storefront's information architecture and on the consumer's instruction, not only on flaws inherited from training.

## What the paper uses it for

- **c1.** A vague versus a specific goal prompt changes what the agent searches for and what it buys, which fits the idea that the user's goal, not only the system, decides the outcome. The source stretches here. Its goal is fixed at the start of one run and does not move during the interaction, so it does not show a moving goal that breaks conversion-era design (raincoat to umbrella). It also treats the specific prompt as an upper bound, since "consumers rarely state such precise criteria" (locus 7).
- **c3.** It supports the claim that the platform's design shapes the outcome: the authors manipulate the cost of reaching each attribute and show that this, together with the prompt, decides which information the agent holds. The match is loose. The platform in the source is a simulated storefront with an explicit price per look, and the authors note this "differs from the internal costs AI agents encounter in deployment" (PDF p. 16). The source has no account of a platform that is opaque or that co-opts the user, and the user here is the principal who never sees the interaction (locus 5).

## Loci

Page locators are the PDF page numbers, which match the arXiv page numbers printed at the foot of each page. Each quotation was matched against the .txt text layer of the object read. Inner double quotes are rendered as single quotes in locus 4.

1. "Imposing acquisition costs under a vague goal prompt leads LLMs to omit diagnostic attributes required to compute unit price and make suboptimal choices resembling human heuristics." Abstract, p. 1.
2. "This research demonstrates that the efficacy of marketing cues in delegated AI shopping is governed by storefront information architecture combined with consumers’ instructions, not necessarily immutable LLM characteristics." Abstract, p. 1.
3. "Across two primary studies, several robustness tests, and two validation studies (N = 33,704 total trials), we evaluate eight commercially deployed LLMs from three major providers (Google, OpenAI, and Anthropic)." Introduction, p. 2.
4. "a vague goal prompt, such as the colloquial ‘Find the best deal’, leaves the objective open to multiple valid interpretations (e.g., price per weight or price) and leaves objective specification partly to the LLM." Conceptual development, p. 5.
5. "In surrogate consumption, however, the consumer transfers decision authority to an agent (Solomon, 1986) and never encounters the cue." General discussion, Theoretical implications, p. 14.
6. "Tool-Lab observes the information acquisition and choice, but not the internal mechanisms of the neural network." General discussion, p. 15.
7. "Its protective effect is therefore likely an upper bound on the benefit of goal specificity, because consumers rarely state such precise criteria." Limitations, p. 16.
8. "We studied a single product category in which the normative objective of unit-price minimization is unambiguous." Limitations, p. 16.
9. "Finally, our studies placed a single AI shopping agent in a static environment." Limitations, p. 16.
10. "Under the vague goal prompt, the same cost produced a substantial reduction in diagnostic acquisition (M = 3.81) and choice optimality (M = 0.29)." Study 1 Results, p. 8.

## Caution

- Partial read: PDF pp. 1–6 (abstract, introduction, literature review, conceptual development, hypotheses, start of the Tool-Lab description), the opening of Study 1 Results on p. 8, and pp. 13–16 (General discussion, implications, limitations). I did not read the method and results of Studies 1 and 2 in full, the robustness and validation studies, or the main-text figures and tables (PDF pp. 22–23) and the Web Appendix (PDF pp. 24–58). Every statistic above comes from the abstract, the introduction or the discussion.
- This is a preprint, version 2 of 13 October 2026 (OpenAlex dates the record 23 September 2026 and lists one citation). It has not been peer reviewed as far as the object read shows.
- The triage table (F9-F10 row 2) quotes the abstract as "governed by storefront information architecture, not necessarily immutable LLM flaws". The abstract in the object read (v2) is worded differently (locus 2: "...governed by storefront information architecture combined with consumers’ instructions, not necessarily immutable LLM characteristics"). The older wording is close to the registry abstract in `csl.json`; I did not establish which version that abstract belongs to. [Verifier, S6] `csl.json` itself carries `"version": "2"`, yet its abstract differs from the v2 PDF (it also reads "choose suboptimal choices" where v2 has "make suboptimal choices"). The DOI is version-independent, so that field does not settle which text the registry abstract came from. Cite v2's wording, and note that v2 adds the consumer's instruction as a second determinant.
- No Crossref record exists; the identifier is the arXiv DOI (10.48550/arxiv.2609.28372, shown upper-case in `csl.json`) and OpenAlex W7214217042. The authors' affiliations on the title page are McGill University, Desautels Faculty of Management.
- The agent in the source is the decision maker; the human consumer is the principal who delegates and "never encounters the cue" (locus 5). That is the reverse of the paper's c2, which fixes attention on the human user and brackets the agent. Nothing in this source touches animation.
- Scope: one product category (packaged coffee in the examples I saw), two or three alternatives per trial, a monetary cost per look, and a static storefront (loci 8, 9). The authors say the evidence separating "objective substitution" from omission is "suggestive rather than conclusive" (PDF p. 15).

## Verification

2026-11-05 · S6 verifier, batch b06 (opus; not the writer) · verdict: corrected · checked: loci 10/10 found on the stated pages; metadata vs csl.json and openalex.json (Wadi and Ma, 2026, title, arXiv DOI 10.48550/arxiv.2609.28372, W7214217042, one citation) and the PDF header (arXiv:2609.28372v2 [econ.GN] 13 Oct 2026; McGill); sha256 recomputed and matches; depth partial honest; summary facts (N = 33,704, eight LLMs from three providers, validation studies point to acquisition rather than utilization on PDF p. 13, two alternatives in Study 1 and three in Study 2 on p. 16, "suggestive rather than conclusive" p. 15) found in the pages read · changed: Web Appendix page range corrected (figures/tables pp. 22–23, appendix from p. 24); added a Caution note on the csl.json version field
