---
citekey: eu2016gdpr
title: "Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)"
authors: "{European Parliament and Council of the European Union}"
year: 2016
type: statute
doi: null
venue: Official Journal of the European Union, L 119, 4.5.2016, p. 1
source_basis: partial-text
pages_read: "header; Arts 1-3, 22, 77-79, 99; Recital 71 (OJ text)"
source_url: http://data.europa.eu/eli/reg/2016/679/oj
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/audit5/M2/32016R0679.txt
sha256: 8e5d737c8081e86bc0e661d9675f3923aa2a588fe44c87031c573d7cdff82343
manuscript_lines: [167, 173, 205, 237]
ledger_rows: [P5-019, P5-021, P5-023, P5-029, P6-005, P6-036, P6-037]
verified: true
written: 2026-10-14
---

**Copy used.** The EUR-Lex OJ text already saved in `pdfs/audit5/M2/` (file header "L_2016119EN.01000101.xml";
"4.5.2016 ... Official Journal of the European Union L 119/1"). EUR-Lex blocks automated access, so it was not
refetched. The `.pdf` and `.html` files beside it are 214-byte stubs; the `.txt` is the text read.

## Summary
The GDPR lays down rules for protecting natural persons in the processing of personal data and for its free
movement (Art 1), applies to processing wholly or partly by automated means (Art 2(1)), and reaches controllers
established in the Union and, for data subjects in the Union, some controllers outside it (Art 3). It entered
into force on the twentieth day after publication and applies from 25 May 2018 (Art 99). Article 22 gives the
data subject "the right not to be subject to a decision based solely on automated processing, including
profiling," with legal or similarly significant effects (Art 22(1)), subject to three exceptions: contract
necessity, authorisation by law, and explicit consent (Art 22(2)). In the contract and consent cases the
controller must provide safeguards, "at least the right to obtain human intervention on the part of the
controller, to express his or her point of view and to contest the decision" (Art 22(3)). Recital 71 names
"automatic refusal of an online credit application or e-recruiting practices without any human intervention"
as examples. Remedies run to a supervisory authority (Art 77) and to the courts, against the authority (Art 78)
and against the controller or processor (Art 79).

## Key facts it relies on
- Art 22(1): "The data subject shall have the right not to be subject to a decision based solely on automated
  processing, including profiling, which produces legal effects concerning him or her or similarly significantly
  affects him or her."
- Art 22(2): para. 1 does not apply where the decision (a) is necessary for a contract, (b) is authorised by
  Union or Member State law with suitable safeguards, or (c) rests on explicit consent.
- Art 22(3): "In the cases referred to in points (a) and (c) of paragraph 2, the data controller shall implement
  suitable measures ..., at least the right to obtain human intervention on the part of the controller, to
  express his or her point of view and to contest the decision."
- Recital 71: examples "automatic refusal of an online credit application or e-recruiting practices without any
  human intervention"; safeguards include "to obtain an explanation of the decision reached after such
  assessment and to challenge the decision" (both read this session).
- Art 77(1): every data subject may complain to a supervisory authority.
- Art 79(1): "each data subject shall have the right to an effective judicial remedy" against a controller or
  processor for infringement of the Regulation.
- Art 99(2): applies from 25 May 2018.
- Header: Regulation (EU) 2016/679 of 27 April 2016, OJ L 119, 4.5.2016.

## Critical notes from the literature
- Facet N2 (`literature/facets/N2_platform_law.md:55-62, 88-97`) reads Art 22 with CJEU *SCHUFA* (C-634/21,
  paras 52, 61, 64): Art 22(1) "lays down a prohibition in principle", and a credit bureau's score is itself a
  decision where a lender "draws strongly" on it in a three-party case. On that reading Art 22 acts before the
  decision, not only after it; facet N2 says this "challenges §4.4's framing".
- Facet N2 (`:99-108`) adds *Dun & Bradstreet* (C-203/22, para. 57): Art 15(1)(h) gives "a genuine right to an
  explanation", and trade-secret claims go to a supervisory authority or court (para. 74).
- Kaminski and Urban (2021, p. 2039), via facet N2 (`:207`): "Neither our archetype contestation schemes nor
  Article 22 feature a neutral arbiter."
- Wachter, Mittelstadt and Floridi (2017) argue there is no GDPR "right to explanation", at most a "right to be
  informed" (facet N2:179); the arm knows it through the abstract and an accepted manuscript.
- Ledger P5-019: the Art 22(3) safeguards are not a general right of everyone subject to a solely automated
  decision; they attach only to the 22(2)(a) and (c) exceptions.

## Key topics covered
automated individual decision-making, profiling, right not to be subject to solely automated decisions, human
intervention, contestation, controller, supervisory authority complaint, judicial remedy, data protection

## Where the manuscript uses it
- **Line 167**, "The General Data Protection Regulation gives a person subject to a solely automated decision the
  right to obtain human intervention and to contest it (Regulation (EU) 2016/679, art. 22(3))." Source: Art 22(1)–
  (3). **narrower**: the Art 22(3) rights arise only where a solely automated decision is allowed under the
  contract or explicit-consent exceptions; the general right is Art 22(1)'s right not to be subject to such a
  decision.
- **Line 167**, "courts and regulators stand behind all of these". Source for the GDPR: Arts 77–79. **holds**
  for the GDPR (complaint to an authority; judicial remedy against controller).
- **Line 173, quotation check**: "the human intervention the GDPR guarantees is intervention 'on the part of the
  controller.'" Exact-string check: **exact**, Art 22(3) (`32016R0679.txt:764`). **holds.**
- **Line 205**, "the GDPR's article 22 already gives a narrow right not to be subject to solely automated
  decisions." Source: Art 22(1)–(2). **holds.**
- **Line 237**, each provision "confined to a sector or a jurisdiction" and "places the first review inside the
  firm". Source: Arts 3, 22(3); Recital 71. **holds**: territorial scope (Art 3) and review by the controller
  (Art 22(3)). Facet N2's *SCHUFA* reading means the Art 22(1) rule also binds before any review.
- **Line 365, reference entry** "Regulation (EU) 2016/679 ... of 27 April 2016 (General Data Protection
  Regulation). *Official Journal of the European Union*, L 119, 4.5.2016." **holds** against the OJ header.

## Verifier notes
- 2026-10-14. Recomputed sha256 of `audit5/M2/32016R0679.txt`: matches. Header confirms OJ L 119/1, 4.5.2016, Regulation of 27 April 2016.
- Checked Art 3, Art 22(1)-(3) (l. 756-764), Recital 71 (l. 162), Arts 77(1), 78, 79(1), and the 25 May 2018 application date: all quotations exact.
- Use verdicts confirmed: l. 167 narrower (22(3) safeguards attach only to the 22(2)(a) and (c) exceptions); l. 167 courts holds; l. 173 "on the part of the controller" exact; l. 205 and l. 237 hold.
- Bib disagreements: bib title is abbreviated and its note says Art 22 was read on springlex.eu rather than the OJ text; manuscript entry matches the OJ header.
