---
citekey: alfrink2022contestable
title: Contestable AI by Design: Towards a Framework
authors: Alfrink, Kars and Keller, Ianus and Kortuem, Gerd and Doorn, Neelke
year: 2022
doi: 10.1007/s11023-022-09611-z
arxiv: null
journal: Minds and Machines
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.1007/s11023-022-09611-z.pdf
sha256: 2d9f5424f022b095e303d0ad116cd13800b321d8995112cd0872f2fb4ba6f326
pdf_path: literature/pdfs/alfrink2022contestable.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper addresses how to make AI systems used for automated decision-making "contestable by design," i.e., open and responsive to human intervention throughout the system lifecycle, as a guard against unfair, illegitimate, and unaccountable automated decisions. It argues that existing responsible/ethical-AI knowledge is too abstract and principle-level to be directly usable by designers, and that "intermediate-level generative design knowledge" in the form of design frameworks is a better vehicle. Methodologically, the authors conduct a systematic literature review (Scopus search plus backward/forward snowballing) and apply reflexive thematic analysis (Braun and Clarke) in Atlas.ti, then use visual mapping to synthesize the results. From 19 included sources they extract five system "features" and six development "practices" that contribute to contestability. The five features are built-in safeguards against harmful behavior, interactive control over automated decisions, explanations of system behavior, human review and intervention requests, and tools for scrutiny by subjects or third parties; the six practices are ex-ante safeguards, agonistic approaches to ML development, quality assurance during development, quality assurance after deployment, risk mitigation strategies, and third-party oversight. Two diagrams map features to actors (developers, controllers, decision subjects, third parties) and practices to AI lifecycle phases. The authors present this as a preliminary framework requiring future testing and validation in specific application contexts.

## Key facts it relies on
- The framework consists of exactly five system features and six development practices contributing to contestable AI; the features include built-in safeguards, interactive control, explanations, human review/intervention requests, and tools for scrutiny, and the practices include ex-ante safeguards, agonistic ML approaches, QA during development, QA after deployment, risk mitigation strategies, and third-party oversight.
- Systematic review used Scopus, restricted to journal articles and conference papers published between 2016 and 2021 (Scopus filter PUBYEAR>2015 and PUBYEAR<2022), mentioning "AI", "contestability" and "design" in title/abstract/keywords, with contestability synonyms drawn from the Merriam-Webster thesaurus.
- PRISMA flow (Fig. 1): 1600 records identified from Scopus, 1128 identified by snowballing, 21 duplicates removed, 2707 records screened, 2581 excluded, 126 full texts assessed for eligibility, 107 full texts excluded, leaving 19 full texts included in the review.
- Analysis adapted reflexive thematic analysis (Braun and Clarke, 2006) and was performed in Atlas.ti (version 22 on MacOS), coding "active ingredients" (actionable sociotechnical system properties), then using visual mapping with existing diagrams as a foundation.
- Contestability is defined drawing on prior work: Hirsch et al. (2017) frame it as "humans challenging machine predictions"; Vaccaro et al. (2019) call it a "deep system property" and a form of procedural justice; Sarra (2020) holds it requires an "articulate act of defense," a "procedural relationship," and a "dialectical exchange," so a mere "human in the loop" is insufficient.
- AI is defined broadly following Suchman (2018): "a cover term for a range of techniques for data analysis and processing, the relevant parameters of which can be adjusted according to either internally or externally generated feedback."
- The paper situates contestability against principle-level surveys: Jobin et al. (2019) identify eleven ethical principles (transparency, justice/fairness, non-maleficence, responsibility, privacy, beneficence, freedom/autonomy, trust, dignity, sustainability, solidarity, with the first five in over half of sources); Shneiderman (2020) offers 15 recommendations in a three-layer governance structure.
- Features are mapped to actors (Fig. 2) and practices are mapped to the AI lifecycle phases of the Information Commissioner's Office (ICO) auditing framework (Binns and Gallo, 2019) (Fig. 3): business/use-case development, design and data procurement, building and testing, deployment and monitoring, with risk mitigation and third-party oversight spanning all phases.
- A "design framework" is defined following Obrenović (2011) as describing "the characteristics that a design solution should have to achieve a particular set of goals in a particular context," and as "generative intermediate-level design knowledge" (Löwgren et al., 2013; Höök and Löwgren, 2012).

## Critical notes from the literature
- The authors explicitly call the framework "preliminary" and note its validation "was not part of this paper"; it is a starting point for subsequent testing in specific application contexts.
- They acknowledge the framework is built on a small sample (19 academic papers), risking gaps from lack of coverage, that the source papers come from specific fields (ethics of technology, computer science, law), and that "many of these papers are not based on empirically validated interventions" and remain largely "context-free."
- They concede limited usability: the offering is diagrams ("one step up from lists"), with recommendations at the level of features/practices rather than principles, but with no directions for actually using the framework to design contestable AI; they cite Morley et al. (2019) noting AI ethics tools often lack actionable usability.
- Scope conditions are stated: the framework assumes a generic "automated decision-making" setting with "significant impact" and relatively low time-sensitivity, so it likely does not cover extreme high-stakes cases (e.g., lethal autonomous weapons) or time-critical shared control (e.g., autonomous vehicles), which fall under the related field of meaningful human control; much of the authors' own empirical work is situated in (local) government public services in OECD countries.
- The paper itself flags (footnote) Sloane et al. (2020)'s critique that participation is not a panacea for AI harms, and warns participatory/agonistic efforts risk becoming "participation theater" or a box-ticking exercise, and that adversarial procedures could be abused to cover negligence unless decision chains remain traceable.

## Key topics covered
Contestable AI; contestability by design; automated decision-making; responsible/ethical AI; sociotechnical systems; design frameworks; intermediate-level generative design knowledge; systematic literature review; PRISMA flow; reflexive thematic analysis; agonistic approaches to ML; participatory design; human-in-the-loop; explainability and justification; due process; human review and intervention; third-party oversight; AI system lifecycle; procedural justice; meaningful human control.
