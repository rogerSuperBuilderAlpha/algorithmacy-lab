---
citekey: microsoft2022responsible
title: "Microsoft Responsible AI Standard, v2: General Requirements (For External Release)"
authors: "{Microsoft}"
year: 2022
type: report
doi: null
venue: Microsoft Corporation, June 2022
source_basis: full-text
pages_read: "all (27 pp.)"
source_url: https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/V1/ms/Microsoft-Responsible-AI-Standard-v2-General-Requirements-3.pdf
sha256: 66a41b79c894791f1776fb2d8403f3e2b8e75db06ec8f7dbde615aa6972f2b6c
manuscript_lines: []
ledger_rows: []
verified: true
written: 2026-10-14
---

**Key made for this facet** (`surnameYEARfirstword`, corporate author). Printed page numbers match PDF pages.

## Summary
The Standard turns Microsoft's six AI principles into product-development requirements, grouped as Accountability (A1–A5), Transparency (T1–T3), Fairness, Reliability & Safety, Privacy & Security, and Inclusiveness goals. Each goal states who it applies to, requirements, and recommended tools. The transparency goals go beyond disclosure. T1 requires teams to identify both the people who use a system's outputs to decide and "stakeholders who are subject to decisions informed by the system", to design UX, features and "educational materials" so both can interpret system behaviour and resist automation bias, and to define and run an evaluation of whether each "can interpret the relevant system responses reasonably well", with release criteria and a gap plan. T2 requires published documentation (a Transparency Note for platform services) for customers who decide whether to employ a system or who build on it. T3 requires disclosure of AI interaction and an evaluation that people are informed. A5 requires the elements overseers need to understand, interpret, override and interrupt a system, and an evaluation that oversight "can be accomplished by stakeholders in realistic conditions of system use". The Standard recommends the Guidelines for Human-AI Interaction (Amershi et al. 2019) for design. It is a self-governance document "edited for external release" (p. 27); it reports no compliance data.

## Key facts it relies on
- T1 (p. 9): applies to "All AI systems when the intended use of the generated outputs is to inform decision making by or about people."
- T1.1 (p. 9): identify "stakeholders who will use the outputs of the system to make decisions, and ... stakeholders who are subject to decisions informed by the system."
- T1.2 (p. 9): design "the system UX, features, reporting functions, and educational materials" so they can understand intended uses, "interpret relevant system behavior effectively", and "remain aware of the possible tendency of over-relying on outputs ... ('automation bias')".
- T1.3 (p. 9): evaluate "whether each stakeholder who will make decisions or be subject to decisions based on the behavior of the system can interpret the relevant system responses reasonably well."
- T1.2.1 and A5.3.1 (pp. 10, 8): "Follow the Guidelines for Human-AI Interaction when designing the system."
- T2.2 (p. 11): "When the system is a platform service made available to external customers or partners, a Transparency Note is required."
- T3 (p. 12): inform people "that they are interacting with an AI system"; T3.3 evaluates whether they are informed.
- A5.4 (p. 8): evaluate "whether each oversight or control function can be accomplished by stakeholders in realistic conditions of system use."

## Critical notes from the literature
- A company standard, not law; I found no audit of compliance with it in this round.
- Facet V1: the October 2026 Nadella post contains neither the T1.3 comprehension test nor the A5.4 oversight test; the post is thinner than this Standard.
- The competence the Standard tests is interpretation of outputs through "educational materials" and UX, i.e. reading the system; it tests at release and makes no commitment to grow a person's competence over time (facet V1).

## Key topics covered
intelligibility, stakeholders subject to decisions, educational materials, automation bias, comprehension evaluation, Transparency Notes, disclosure of AI interaction, human oversight

## Where the manuscript uses it
- v4 (not yet drafted): proposed use — Microsoft's own 2022 standard already asked more than the post: test whether people subject to decisions can interpret outputs (T1.1–T1.3, p. 9) and whether overseers can oversee "in realistic conditions" (A5.4, p. 8). Holds.
- v4 (not yet drafted): proposed use — even so, the competence it asks for is interpretation of the system, delivered by "educational materials" (T1.2, p. 9): the literacy frame. Holds as reading; the inference is the paper's.

## Verifier notes
- 2026-10-14. sha256 matches; the PDF has 27 pp. Exact-checked T1 ("Applies to"), T1.1, T1.2, T1.3 (p. 9), the Recommendation T1.2.1 (p. 10) and A5.3.1 (p. 8) wording, T2.2 and the Transparency Note sentence (p. 11), T3 (p. 12), A5.4 (p. 8) and "edited for external release" (p. 27). All pass.
- The source uses double quotes for ("automation bias"). The card nests it as ('automation bias') inside its own quotation, which is a convention, not a misquote.
- Both uses hold.
- Bib: the card title adds "(For External Release)", which the facet .bib puts in its `type` field. No other disagreement.
