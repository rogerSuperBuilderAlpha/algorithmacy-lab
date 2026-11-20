---
citekey: nist2024artificial
title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1"
authors: "{National Institute of Standards and Technology}"
year: 2024
type: report
doi: 10.6028/NIST.AI.600-1
venue: National Institute of Standards and Technology, U.S. Department of Commerce
source_basis: partial-text
pages_read: "pp. 1-2 (Introduction), p. 38 (MEASURE 3.3), pp. 52-53 (Appendix A.1.8 Incident Disclosure); search for 'voluntary', 'incident disclosure', 'end user'"
source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N4/nist600/NIST.AI.600-1.pdf
sha256: 6e73620ab6b64e90ef2c04bf0e0d6246185a2f4b1b13cab0df494496cff89b6a
manuscript_lines: []
ledger_rows: [O02]
premises: [A4]
facet: N4
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
NIST's companion profile for generative AI (July 2024), issued under Executive Order 14110. It names "Incident Disclosure" as one of four primary considerations (p. 2). Its appendix on incident disclosure states that no formal reporting channel exists and recommends that organisations "could consider" guidelines for public reporting and information sharing "with relevant AI Actors". The people harmed are named in the definition of an incident; the disclosure it describes flows among AI actors and to public databases. MEASURE 3.3 asks for feedback processes "for end users and impacted communities to report problems and appeal system outcomes" (p. 38). All of it is voluntary. I did not check whether EO 14110's revocation in 2025 changed the profile's status; NIST still served the PDF on 2026-10-24. Printed page numbers are four lower than PDF page numbers.

## Key facts it relies on
- p. 1: the AI RMF "is intended for voluntary use".
- p. 2: four primary considerations: "Governance, Content Provenance, Pre-deployment Testing, and Incident Disclosure".
- p. 52: an AI incident is an "event, circumstance, or series of events where the development, use, or malfunction of one or more AI systems directly or indirectly contributes to one of the following harms: injury or harm to the health of a person or groups of people ...".
- p. 52: "Formal channels do not currently exist to report and document AI incidents. However, a number of publicly available databases have been created to document their occurrence. These reporting channels make decisions on an ad hoc basis about what kinds of incidents to track. Some, for example, track by amount of media coverage."
- p. 53: "organizations could consider developing guidelines for publicly available incident reporting which include information about AI actor responsibilities."
- p. 38: "MEASURE 3.3: Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics."

## Critical notes from the literature
- None read this round.

## Where the argument uses it
- A4, M9: holds for the US federal layer. Incident disclosure is a voluntary recommendation among organisations; the appeal route of MEASURE 3.3 is the closest thing to standing, and it is the organisation's own process.
- M2: holds; voluntary.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
