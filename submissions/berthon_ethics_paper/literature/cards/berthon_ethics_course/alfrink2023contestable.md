---
citekey: alfrink2023contestable
title: "Contestable AI by Design: Towards a Framework"
authors: Alfrink, Kars and Keller, Ianus and Kortuem, Gerd and Doorn, Neelke
year: 2023
type: article
doi: 10.1007/s11023-022-09611-z
venue: Minds and Machines, 33(4), 613-639 (online 2022)
source_basis: partial-text
pages_read: "PDF pp. 2-3 (abstract, introduction), p. 3 (opening of section 2), pp. 11-13 (sections 6.1.4-6.1.5), p. 17 (6.2.6, 6.3), pp. 17-18 (section 7, opening)"
source_url: https://doi.org/10.1007/s11023-022-09611-z
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/N5_prior_work_gap/alfrink2022contestable.txt
sha256: 9082eddc70386e224804800cd59c354b43f7470f222edab728731c138bbe547c
manuscript_lines: [223]
ledger_rows: [P6-N07]
verified: corrected
written: 2026-10-14
---

Page note: the copy is the TU Delft repository file of the published online-first version (PDF sha256 15ccb0bd…, `alfrink2022contestable.pdf`, 28 pages including the repository cover). It carries no volume page numbers, so locators below are PDF pages; the issue pages 613–639 come from the repository's citation line and FIX_CHECK_C.md (Crossref).

## Summary
Alfrink and colleagues argue that harmful automated decision-making can be guarded against by making AI systems "contestable by design": "responsive to human intervention throughout the system lifecycle" (abstract, PDF p. 2). Finding the existing research hard to apply, they review the literature systematically and synthesise a design framework of five system features and six development practices (PDF p. 3). The features are built-in safeguards, interactive control over automated decisions, explanations of system behaviour, human review and intervention requests, and tools for scrutiny by subjects or third parties; the practices are ex-ante safeguards, agonistic approaches to ML development, quality assurance during development, quality assurance after deployment, risk mitigation, and third-party oversight (PDF p. 3). Their intervention-request feature lets subjects "ask questions and record disagreements" and holds that "Reliance on out-of-system mechanisms for contestation is insufficient" (PDF p. 11). They want third parties to represent subjects, collective appeals, and trusted intermediaries who can see proprietary models (PDF pp. 12, 17). The framework is preliminary, meant for later testing in specific contexts (PDF p. 3). The development practices "are primarily performed by system developers" (PDF p. 17).

## Key facts it relies on
- Definition: contestable AI systems "are open and responsive to human intervention throughout their lifecycle: not only after an automated decision has been made, but also during its design and development" (PDF p. 3).
- The five features and six practices, listed in the introduction and again in section 7 (PDF pp. 3, 17–18).
- Section 6.1.4: the feature "gives subjects the ability to 'ask questions and record disagreements', both on the individual and the aggregate scale"; "Reliance on out-of-system mechanisms for contestation is insufficient"; "Due process mechanisms should be designed into the AI systems itself" (PDF pp. 11–12).
- "A risk of appeal procedures is that burdens are shifted to individual subjects", met by synchronous contact with decision makers "or to have third parties represent subjects"; "Mechanisms for contestability should allow for collective action" (PDF p. 12).
- Contestation needs "a dialectical exchange between subject and controller" and "should include a right to a new decision, compensation of harm inflicted, or reversal" (PDF p. 13).
- Section 6.1.5: tools for scrutiny "mainly take the form of a range of information resources", such as documentation of the system and how it was built (PDF p. 13).
- Section 6.2.6: third-party oversight strengthens "trusted third party actors such as government agencies, civil society groups, and NGOs"; where operators claim secrecy, "third parties can act as trusted intermediaries to whom sensitive information is disclosed" (PDF p. 17).
- Section 6.3: the practices "are primarily performed by system developers" (PDF p. 17).

## Critical notes from the literature
- FIX_CHECK_C.md (P6-N07, pass) notes that Alfrink's features are built by the system operator and that §6.1.4 calls out-of-system contestation insufficient, whereas the manuscript's counter-delegation puts the record on the user's side and the dispute before a party the operator does not control.
- Facet N5_prior_work_gap.md (l. 122, 187) found each half of counter-delegation separately in prior work but no work pairing a user-side record and reader with a binding independent adjudicator. It lists Alfrink among the contestability-by-design works for §§4.4 and 5.4.
- Facet M2_algorithm_studies.md (l. 89) had only the record; N5 raised it to Part. The issue year (2023) against the online year (2022) follows the list's practice (FIX_CHECK_C.md).
- The framework is a literature synthesis, not tested in a deployment (PDF p. 3, "preliminary").

## Key topics covered
contestability, automated decision-making, design framework, human intervention, appeals, explanations, third-party oversight, collective contestation, agonistic design, systematic literature review

## Where the manuscript uses it
- l. 223: "Others have proposed the technical half (Alfrink et al., 2023)." Takes a design proposal for the record-keeping side of counter-delegation (a person keeping her own record and bringing her own reader, l. 221). Source PDF pp. 11–13 (subjects "record disagreements"; tools for scrutiny by subjects or third parties; third parties representing subjects). **narrower**: Alfrink et al. propose contestation features that the operator designs into its own system, and call out-of-system mechanisms insufficient (PDF p. 11); they do not propose a record held on the user's side. They do allow that intervention requests "could be facilitated through auxiliary platforms, or be part of the system itself" (PDF p. 11), which is the closest they come to an out-of-operator channel; it is a request route, not a user-held record, so the verdict stays narrower.

## Verifier notes
- 2026-10-14. sha256 of `alfrink2022contestable.txt` recomputed: matches. Crossref (10.1007/s11023-022-09611-z): authors, title, *Minds and Machines* 33(4), 613-639 match the card, `references.bib` and v3 l. 265; Crossref gives online 13 Aug 2022 and the issue as December 2023, so "2023" is the issue year. No bib disagreements.
- Ran every quotation on the card as an exact string against the text: all present, on the PDF pages the card gives ("Due process mechanisms should..." is on PDF p. 12, inside the card's "pp. 11-12").
- Corrected the Summary on two points: the practices list garbled "quality assurance during development" and "quality assurance after deployment" into "during and after deployment"; and the summary said "most features" are built by developers, where §6.3 (PDF p. 17) says the *practices* "are primarily performed by system developers".
- Use l. 223 (v3 text unchanged): verdict **narrower** confirmed. Added that §6.1.4 allows intervention requests "through auxiliary platforms" (PDF p. 11); that is still not a user-held record.
