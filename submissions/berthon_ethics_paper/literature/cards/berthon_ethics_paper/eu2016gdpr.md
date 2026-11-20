---
citekey: eu2016gdpr
title: "Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)"
authors: "{European Parliament and Council of the European Union}"
year: 2016
type: statute
doi: null
venue: Official Journal of the European Union, L 119, 4.5.2016, p. 1
source_basis: partial-text
pages_read: "Arts 33, 34, 77(1), 79(1), 80(1), 82(1)-(3); recital 86 (OJ text)"
source_url: http://publications.europa.eu/resource/celex/32016R0679
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N4/gdpr/32016R0679.txt
sha256: c4d76ae2214f2a29ce3ac9d03d89bb5f2ad0e95c98b6d3444ab6be3e444b7df8
manuscript_lines: []
ledger_rows: [O02, K12]
premises: [A4, A8]
facet: N4
supersedes: berthon_ethics_course/eu2016gdpr.md
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Upgrade card for the breach-notification articles; the superseded card read Arts 1-3, 22, 77-79 and 99. Copy: Publications Office CELLAR XHTML fetched 2026-10-24.

The GDPR is the contrast case the brief asks for: a regime in which an incident reaches the affected person directly and comes with standing. A controller notifies the supervisory authority of a personal data breach within 72 hours (Art 33(1)). Where the breach "is likely to result in a high risk", the controller must also tell the data subject, "in clear and plain language", what happened, the likely consequences, the measures taken and a contact point (Art 34(1)-(2), with Art 33(3)(b)-(d)). Recital 86 states the purpose: "to allow him or her to take the necessary precautions". The notice is backed by remedies the data subject holds: complaint (Art 77), an effective judicial remedy against the controller (Art 79), representation by a not-for-profit body (Art 80), and compensation for material or non-material damage (Art 82). The exceptions are real: no notice where the data were encrypted, the risk is no longer likely, or notice would take "disproportionate effort", in which case a public communication substitutes (Art 34(3)).

## Key facts it relies on
- Art 33(1): notify the supervisory authority "without undue delay and, where feasible, not later than 72 hours after having become aware of it".
- Art 34(1): "When the personal data breach is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall communicate the personal data breach to the data subject without undue delay."
- Art 34(2): the communication "shall describe in clear and plain language the nature of the personal data breach and contain at least the information and measures referred to in points (b), (c) and (d) of Article 33(3)".
- Art 34(3)(a)-(c): exceptions for encryption, subsequent measures, and "disproportionate effort", where "there shall instead be a public communication or similar measure".
- Art 34(4): the supervisory authority "may require it to do so".
- Recital 86: the communication allows the data subject "to take the necessary precautions" and should include "recommendations for the natural person concerned to mitigate potential adverse effects".
- Art 79(1): "each data subject shall have the right to an effective judicial remedy where he or she considers that his or her rights under this Regulation have been infringed".
- Art 80(1): the data subject may "mandate a not-for-profit body, organisation or association" to lodge complaints and exercise Arts 77-79 rights on his or her behalf.
- Art 82(1): "Any person who has suffered material or non-material damage as a result of an infringement of this Regulation shall have the right to receive compensation from the controller or processor".

## Critical notes from the literature
- Veale and Zuiderveen Borgesius (2021, p. 111; `veale2021demystifying`) use these GDPR rights (arts 77-78, 80) as the benchmark the draft AI Act lacked: "Collectives such as consumer groups also lack any rights, such as representative complaints possible under the GDPR."

## Where the argument uses it
- A4, M9 (P20): refutation sought and found, but in a neighbouring regime. Disclosure to those affected *with* standing exists in EU law, where the incident is a personal data breach. It does not exist in the AI Act's incident regime (`eu2024aiact`). The paper's claim must be "the AI incident regime, and the post, give notice without standing", not "the law never pairs notice with remedy".
- O02: the objection is partly right. An AI incident that is also a personal data breach triggers Art 34 notice and Art 79/82 remedies. The objection's reach ends where the harm involves no personal data or falls below "high risk".

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
