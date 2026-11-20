---
citekey: hleg2019ethics
title: "Ethics Guidelines for Trustworthy AI"
authors: High-Level Expert Group on Artificial Intelligence
year: 2019
type: report
doi: null
venue: European Commission, Brussels (made public 8 April 2019)
source_basis: full-text
pages_read: "whole document, 41 PDF pages (printed page = PDF page minus 2)"
source_url: https://ec.europa.eu/newsroom/dae/document.cfm?doc_id=60419
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/R8/hleg2019ethics/hleg2019ethics.pdf
sha256: 4a89863a96551bb3b9ce786afb1b1d58e8062f5a7fa3ed6748922550dde35e25
manuscript_lines: []
ledger_rows: []
premises: [A7, A8, CA]
facet: R8
supersedes: null
anthropic_authored: false
verified: pending
written: 2026-10-25
---

Downloaded on 2026-10-25 at the author's request from the Commission's newsroom document URL (the digital-strategy
page returned 403 and was not retried). Read in full. Quotations below were checked word for word against `pdftotext`
output; locators are printed page numbers.

## Summary
The Commission's High-Level Expert Group sets out "trustworthy AI" as lawful, ethical and robust, grounds it in four
ethical principles (respect for human autonomy, prevention of harm, fairness, explicability), and turns those into
seven requirements: human agency and oversight; technical robustness and safety; privacy and data governance;
transparency; diversity, non-discrimination and fairness; societal and environmental well-being; accountability
(p. 14). It closes with an assessment list. It is soft law: "Nothing in this document shall create legal rights nor
impose legal obligations towards third parties" (p. 6). Members include Coeckelbergh, Floridi, Google, IBM and SAP;
Microsoft is not listed (p. 39).

## Key facts it relies on
- "Nothing in this document shall create legal rights nor impose legal obligations towards third parties." (p. 6)
- Harm can arise from "asymmetries of power or information, such as between employers and employees, businesses and
  consumers or governments and citizens" (p. 12).
- "The procedural dimension of fairness entails the ability to contest and seek effective redress against decisions
  made by AI systems and by the humans operating them. In order to do so, the entity accountable for the decision must
  be identifiable, and the decision-making processes should be explicable." (p. 13)
- Explicability: decisions should be "explainable to those directly and indirectly affected. Without such information,
  a decision cannot be duly contested." (p. 13)
- "End-users and the broader society should be informed about these requirements and able to request that they are
  upheld." (p. 14). Same page defines deployers and end-users and lists requirement 7, Accountability, "Including
  auditability, minimisation and reporting of negative impact, trade-offs and redress".
- Human agency: "Key to this is the right not to be subject to a decision based solely on automated processing…"
  (p. 16, citing GDPR art. 22 at n. 36); human-in-command includes "the ability to override a decision made by a
  system" (p. 16). The override sits with humans overseeing the system, not with the affected person.
- "Whenever an AI system has a significant impact on people's lives, it should be possible to demand a suitable
  explanation of the AI system's decision-making process." (p. 18)
- "the option to decide against this interaction in favour of human interaction should be provided where needed to
  ensure compliance with fundamental rights" (p. 18).
- "When unjust adverse impact occurs, accessible mechanisms should be foreseen that ensure adequate redress." (p. 20)
- "Certification can however never replace responsibility. It should hence be complemented by accountability
  frameworks, including disclaimers as well as review and redress mechanisms." (p. 23)
- Stakeholders include "other impacted groups (those who may not purchase or use an AI system but for whom decisions
  are made by an AI system, and society at large)" (p. 23).
- On scoring: "Note that transparency cannot prevent non-discrimination or ensure fairness, and is not the panacea
  against the problem of scoring." and "Ideally the possibility of opting out of the scoring mechanism when possible
  without detriment should be provided – otherwise mechanisms for challenging and rectifying the scores must be given.
  This is particularly important in situations where an asymmetry of power exists between the parties." (p. 34)
- n. 72: "consumers typically give consent without meaningful consideration" (p. 34).
- Glossary, AI practitioners: "excluding those that use AI systems in the capacity of end-user or consumer" (p. 36).

## Critical notes
This is our reading for the Nadella paper, not the group's claims.

- **It names the second party.** The guidelines name the person "for whom decisions are made" without being a user
  (p. 23) and the business-consumer power asymmetry (p. 12). Nadella's essay does not. Use as a public standard
  alongside Microsoft's own (route 1, A7 i).
- **Contest, redress, explanation on demand: duties stated, holder unassigned.** The person may "demand" an
  explanation (p. 18) and contest and seek redress (p. 13), but the override and the oversight sit with the operator
  (p. 16). The record the contest needs is not given to the person. This is the gap D02/D03 fill.
- **Against Mentxaka's certification remedy.** "Certification can however never replace responsibility" (p. 23)
  answers Mentxaka et al.'s "certifying compliance" mitigation from inside the source they map onto (§4.8).
- **Partial precedent for D02.** Opt-out "without detriment", else challenge and rectification, where power is
  asymmetric (p. 34). Limited to scoring; "ideally".
- **Soft law.** It binds no one (p. 6). Do not present it as an obligation on Microsoft; Microsoft was not a member
  (p. 39).

## Where the argument uses it
- **§4.8 "The Requirements Already Cover It" (S-381–S-387):** cite p. 23 against certification; p. 13 for contest
  needing an identifiable accountable entity and an explicable process.
- **§2 route 1 (A7 i):** a published standard the deployer's own industry helped write that names the second party.
- **§5 D02:** p. 34 as partial precedent ("if any").
