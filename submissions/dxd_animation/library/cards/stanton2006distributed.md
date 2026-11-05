---
key: stanton2006distributed
apa: "Stanton, N. A., Stewart, R., Harris, D., Houghton, R. J., Baber, C., McMaster, R., Salmon, P., Hoyle, G., Walker, G., Young, M. S., Linsell, M., Dymott, R., & Green, D. (2006). Distributed situation awareness in dynamic systems: Theoretical development and application of an ergonomics methodology. *Ergonomics*, *49*(12–13), 1288–1311. https://doi.org/10.1080/00140130600612762"
authors: "Stanton, Neville A.; Stewart, Rebecca; Harris, Don; Houghton, Robert J.; Baber, Chris; McMaster, Richard; Salmon, Paul; Hoyle, Geoff; Walker, Guy; Young, Mark S.; Linsell, Mark; Dymott, Roy; Green, Damian"
year: 2006
title: "Distributed situation awareness in dynamic systems: theoretical development and application of an ergonomics methodology"
venue: "Ergonomics"
volume: "49"
issue: "12-13"
pages: "1288–1311"
doi: "10.1080/00140130600612762"
url: ""
type: article
facets: [F8]
claims: [c3, c7]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "Author's pre-publication manuscript (Brunel BURA repository; the copy does not say whether it is the submitted or the accepted version), 34 numbered pages; it carries no journal pagination, so locators are the manuscript's own printed page numbers (the same as PDF page numbers); local folder ~/iit-playground/dxd_animation_local/pdfs/stanton2006distributed/ (stanton2006distributed.pdf, stanton2006distributed.txt, crossref.json, openalex.json); original URL https://bura.brunel.ac.uk/bitstream/2438/1419/1/Distributed_situation_awareness_in_dynamic_systems_Stanton_et_al.pdf (FETCH_LOG.tsv); read 2026-11-05; sha256 e9a9d751d1981152d79a1f538795b6a58085406bc47ce6c6ca336c45871c7e6b"
verified: corrected
verified_against: "stanton2006distributed.txt (Brunel manuscript text layer, pp. 1–34, read for all loci and third-party claims); crossref.json; openalex.json; sha256 of stanton2006distributed.pdf recomputed"
prior_cards: []
status: candidate
added: 2026-11-05
run: dxda-lib-2026-11
---

## What it argues

Stanton and twelve co-authors (the Human Factors Integration Defence Technology Centre) propose foundations for a theory of distributed situation awareness (DSA). They shift the unit of analysis from the individual to the system. Awareness is held by agents, both human and non-human, in subsystems, and each agent holds its own view, which may differ from the others' though compatible with them. A toy fire-fighting case in Table 1 shows this: a gas analyser, a fire-fighter and an Incident Commander each perceive, comprehend and project from a different standpoint. They list six tenets, including that artefacts as well as people hold situation awareness, that different agents see the same scene differently, that whether two agents' awareness overlaps "depends on their respective goals," and that one agent can compensate for another's degraded awareness.

They contrast DSA with "shared SA", which "implies shared requirements and purposes", while DSA "implies different, but potentially compatible, requirements and purposes." They conclude that it is the system, not a given person, that holds the relevant knowledge, and that forcing everyone to share everything may confuse. They illustrate the method on a Type 23 frigate operations room at HMS Dryad. The method elicits what each party knows (Critical Decision Method), extracts "knowledge objects", and draws propositional networks, alongside social and task networks. The paper reports an application and proposes hypotheses. It has no test of the theory.

### What the source counts as its third party

The author's Checkpoint B ruling asked for this record. The triage question was whether the agents' differing purposes ever conflict (an interested third party) or only differ by role. I report what the text shows.

- **Do the agents have interests of their own?** The text says "purposes" and "goals", not interests. In the worked example they are roles within one task: the analyser's goal is to detect gas, the fire-fighter's is to judge risk, the Commander's is to choose a response (p. 4). The paper calls them "different, but potentially compatible" (p. 5). I found no case where one agent's purpose works against another's. The only adversary in the frigate case appears as knowledge objects ("threat", "targets" among the twelve most connected, p. 26), not as an agent in the model.
- **Does any party act through the artefact on the user?** No. Artefacts feed information to people (the analyser's display is the fire-fighter's input, p. 3) and the command system controls weapons and sensors (p. 7). The text does not give a designer, owner or deployer who acts on the user through the artefact. It says the DSA approach has design implications for team structure and HCI (p. 29), but the designer is not an agent in the model.
- **Is anything modelled, or only named?** The agents in the frigate case are modelled: the paper draws a task network and propositional networks for them. It also says the social network is left out "in the interests of brevity" (p. 6). Artefacts are agents in the theory (tenet a, p. 4), though the knowledge network "makes no reference to any particular job roles, and technology is only referred to in a general sense" (p. 16).
- **Number of parties.** More than two throughout: the fire-fighting example has three, the frigate case has at least four named agents plus the command system (p. 7). The authors write that the theory and method "work equally well with single person-machine systems as well as large multi-person machine systems" (p. 28).

## What the paper uses it for

- **c3 (contrast).** The paper says HF models of automation take one operator and one aid. Stanton et al. are a published HF model with many agents, human and non-human, and the paper has to meet it. The source does not cover an interested third party. The agents' purposes differ by role and are meant to fit together. This supports the triage agent's softer wording (where HF admits more parties they share a goal), which is Claude's wording for the author to rule on. It also cuts against any sentence of the paper that says HF has no many-agent models.
- **c7 (contrast).** The paper says animation is triadic (viewer, character, animator) against the dyad. DSA is a many-agent model, not a dyad, so it narrows the claim that HF is dyadic. It has no agent that stands to the user as the animator stands to the viewer, a maker who shapes what the user sees for the maker's own ends.

## Loci

Quotation marks inside quotations are single, as printed. Locators are the manuscript's printed page numbers (1–34), because this pre-publication version has no journal pagination; the journal's 1288–1311 appears only in the registry record. Each quotation was matched against stanton2006distributed.txt, the text layer of the Brunel PDF. Hyphenation at line ends is repaired.

- "The purpose of this paper is to propose foundations for a theory of situation awareness based on the analysis of interactions between agents (i.e., both human and non-human) in subsystems." — p. 1, abstract; matched against stanton2006distributed.txt.
- "It is argued that we should not always hope for, or indeed want, sharing of this awareness, as different system agents have different purposes." — p. 1, abstract; matched against stanton2006distributed.txt.
- "technological artefacts (as well as human operators) have some level of situation awareness (at least in the sense that they are holders of contextually-relevant information)" — p. 4, tenet a; matched against stanton2006distributed.txt.
- "Whether or not one agent’s SA overlaps with that of another depends on their respective goals." — p. 4, tenet c; matched against stanton2006distributed.txt.
- "the goal of the gas analyser is to detect the level of toxic gas in the environment, the goal of the fire fighter is to determine the level of risk present in the environment and the goal of the Incident Commander is to decide on the appropriate response for his/her crew" — p. 4, tenet c; matched against stanton2006distributed.txt.
- "Shared SA implies shared requirements and purposes whereas distributed SA implies different, but potentially compatible, requirements and purposes." — p. 5; matched against stanton2006distributed.txt.
- "The knowledge network makes no reference to any particular job roles, and technology is only referred to in a general sense" — p. 16, section on Part 3; matched against stanton2006distributed.txt.
- "the system as a whole, rather than a given individual, that holds all relevant knowledge" — p. 28, Conclusions (the manuscript reads "we claim that it the system as a whole, rather than a given individual, that holds all relevant knowledge", with "is" missing; I quote from "the system"); matched against stanton2006distributed.txt.
- "we argue that the theory and method work equally well with single person-machine systems as well as large multi-person machine systems" — p. 28, Conclusions; matched against stanton2006distributed.txt.

## Caution

- Version: this is an author's pre-publication manuscript, not the typeset article; nothing in the copy says whether it is the submitted or the accepted version. Its text refers to papers "in this issue" and to Stanton et al. 2004 as the source of the tenets, and it has no journal pagination. Page and quotation details may differ in the published Ergonomics 49(12–13), 1288–1311. A 2017 reprint in *Situational Awareness* (10.4324/9781315087924-25) is the same paper per the triage note; cite the 2006 article. I did not check the published version.
- Authors: the manuscript's byline lists thirteen authors, and `crossref.json` also lists all thirteen (the triage note says Crossref stops at McMaster; the local record does not). The card's author list follows the manuscript byline and the Crossref record, which agree.
- The question "do the purposes ever conflict" has this answer from the text: not shown. The paper says different purposes are "potentially compatible" (p. 5). The text does not rule out conflict, but nothing in the paper treats it.
- DSA is a descriptive, system-level framework. Its "agents" include artefacts that hold information, so the sense of "agent" is thinner than the paper's "character" or "animator". I read "agent" in the source as "holder of contextually relevant information" (tenet a).
- Endsley (2017), which states the operator-plus-autonomy unit, is a separate card (`endsley2017from`).

## Verification

2026-11-05 · S6 verifier, batch b05 (opus; not the writer) · verdict: corrected · checked: loci 9/9 found in stanton2006distributed.txt (the p. 1 abstract quotation joins "non-" and "human" across a line break), each on the printed manuscript page the card gives (form-feed page n = printed page n); 13 authors, title, Ergonomics 49(12-13), 1288–1311 and DOI agree with crossref.json (Crossref gives initials only; full given names come from the manuscript byline, p. 1); year 2006 matches Crossref issued and published-print, so no registered_year is needed; third-party section present and each claim traced (pp. 3, 4, 5, 6, 7, 16, 26, 28, 29); full_text depth honest; sha256 e9a9d751… recomputed and matches · changed: object_read, the Loci preamble and Caution called the copy a "submitted manuscript"; nothing in the copy or FETCH_LOG.tsv says submitted rather than accepted, so all three now say "pre-publication manuscript" and record that the stage is not stated
