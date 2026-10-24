# Chan, A., Wei, K., Huang, S., Rajkumar, N., Perrier, E., Lazar, S., Hadfield, G. K., & Anderljung, M. (2025). *Infrastructure for AI agents* [Preprint]. arXiv:2501.10114.

**Identifier:** arXiv:2501.10114 · **Read depth:** full_text (arXiv v3, 19 Jun 2025; 31 PDF pages, locators are PDF pages; body read in full, reference list searched for the works named below) · **Source-tier:** preprint (policy and design analysis) · **Evidence basis:** direct_read · **Design and sample:** none; a catalogue of research directions · **Parties modeled:** other: user, agent, counterparties (services, humans, other agents) and the legal system, with infrastructure external to the agent · **Facets:** G · **Read:** 2026-10-13

## What it argues
The authors propose "agent infrastructure": "technical systems and shared protocols external to agents that are designed to mediate and influence their interactions with and impacts on their environments" (abstract, p. 1). Their reason is that changing the agent's own behaviour "may not be sufficient" (p. 2). The traffic analogy: driver training is a system-level intervention; "traffic lights, roundabouts, emergency lanes, and camera-enforced speed limits" are infrastructure (p. 4).

They sort nine kinds of infrastructure into three functions (Table 1, p. 3):
- **Attribution:** identity binding (tie an agent to a legal person), certification, agent IDs (pp. 6–10).
- **Interaction:** agent channels that separate agent traffic, oversight layers, inter-agent communication, commitment devices (pp. 11–17).
- **Response:** incident reporting and rollbacks (pp. 17–19).

Each entry has the same headings: description, functions, existing alternatives, adoption, limitations, research questions. The text is a research agenda; it reports no experiment.

The parts most relevant here are the human-attention and incentive limits:
- *Oversight layers* (p. 13) are a monitoring system plus an interface for an actor to intervene. The actor "could be a human user, but not necessarily". Limitation: "Active attention is required if oversight layers flag potentially problematic behaviour. Humans could ignore such flags if they are too frequent or present information in a complex manner" (p. 14). On supply: "it is unclear if the market will provide them to a socially optimal degree", with social-feed controls as the example (p. 14).
- *Certification* says agents "with more regular human oversight could be, but are not necessarily" more trustworthy, citing Parasuraman and Riley, Skitka et al. and Green (2022) (p. 8).
- *Rollbacks* raise moral hazard: "users could have weaker incentives to properly monitor their agents" (p. 19).
- *Interoperability and lock-in* (p. 20): a developer can limit its reputation system's interoperability to shut out competitors, and a bad protocol is hard to leave.
- The accountability example wants "at least one human that can answer for the agent's actions" (p. 5).

The conclusion calls infrastructure "not itself a complete solution, but ... a platform for policies and norms" (p. 21).

## Relation to the argument
**D4 and P11.** The post shares this paper's premise (controls outside the model) and part of its architecture: Nadella's P11–P12 and P17 resemble oversight layers, P19 a rollback or halt, P15 an activity log. This is the closest academic counterpart to the post, and it shows that the control-outside-the-agent move is a design programme, not mere disclosure. That supports the SOURCE.md flag on D4 (the post is not "only" disclosure).

**P12.** Chan names the weak point itself: a human who must attend to flags. It cites automation-bias work but reports no data (p. 14), so it supports P12 as a stated risk only.

**P10/D8.** Pages 14 and 20 argue that those who build the controls may not supply the ones users need, and that interoperability and lock-in favour dominant players. That is the nearest published support for the step the argument map marks `[inf]`, from conflict of interest to "cannot withdraw alone". It is an argument by analogy, not a finding.

**Triad (D9).** Counterparties are in the figure (Fig. 1, p. 2). The agent is still the user's agent, so the mediator with an objective of its own is not modelled.

**Facet check:** the facet cites this paper only for the definition (abstract-only read). The full text also carries the oversight-layer, moral-hazard and lock-in material above, which bears on P10 and P12 more than the facet shows.

## In conversation with
- `chan2024visibility`: the earlier paper, which the Agent ID section draws on (p. 10); Section 7 says it proposed infrastructure for visibility whereas this paper takes "a broader view" (p. 21).
- `green2022flaws`: cited on the point that more human oversight is not necessarily more trustworthy (p. 8).
- `greenblatt2024ai`: cited for trusted automated monitors replacing the human in an oversight layer (pp. 13–14).
- Leads not in the bib: Parasuraman and Riley (1997) on use, misuse, disuse and abuse of automation; Shavit et al. (2023) on governing agentic systems; Kolt (2024) on governing AI agents.

## Caution
A preprint agenda with no data. It treats the agent as the user's agent and does not address a mediator that serves its owner. Its human-factors claims rest on citations, not tests. Version 3 is not necessarily the version of record if the paper is later published.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** the arXiv v3 PDF (31 pages, 19 Jun 2025) from the cards folder; title, authors, version match. About 14 quotations with PDF-page locators (definition, "may not be sufficient", traffic analogy, oversight-layer and moral-hazard passages, certification, "at least one human", conclusion, "broader view"), the nine-item structure of Table 1, the interoperability passage (Section 6.2), and the named references (Parasuraman and Riley, Skitka, Green 2022, Greenblatt, Shavit, Kolt, Chan 2024a;b).

**Findings:** One quotation used American spelling where the source has "behaviour" (oversight-layer limitation, p. 14); fixed to the source's spelling. All other quotations, locators and attributions match, including the Greenblatt citation for trusted automated monitors replacing the user (p. 13).
