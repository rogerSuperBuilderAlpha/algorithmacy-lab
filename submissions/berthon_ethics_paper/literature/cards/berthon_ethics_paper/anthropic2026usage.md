---
citekey: anthropic2026usage
title: Usage Policy
authors: {Anthropic}
year: 2026
type: documentation
doi: null
venue: Anthropic legal page, stated effective date 12 Nov 2026 (posted ahead of that date; read 24 Oct 2026)
source_basis: partial-text
pages_read: "opening; high-risk use case requirements (Requirements; High-risk AI Recommendations; High-risk Physical Actions; exceptions); additional guidelines for chatbots and agentic use. Universal Usage Standards skimmed"
source_url: https://www.anthropic.com/legal/aup
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ant_aup/page.html
sha256: 4bcd401940e13fe823cdb1372d2adc9e79d7750c00537968bfdf968c34bb5666
manuscript_lines: []
ledger_rows: [H24, D02, D03, E15]
premises: [A4, A5, A8]
facet: N1
anthropic_authored: true
verified: corrected
written: 2026-10-24
---

## Summary
Anthropic's usage policy, in a version effective 12 November 2026. For "High-risk AI Recommendations" (legal, medical,
financial, employment and similar) it requires a qualified human reviewer "with the authority to change or modify" the
output, who "remains responsible", and requires that the person advised or decided about "be clearly told that AI
was used". For physical actions it requires operating limits "enforced by the equipment or a controller independent of
model output". This is the most specific vendor rule found that names the affected person; what it gives that person
is notice. Accessed 2026-10-24.

## Key facts it relies on
- "we require that a qualified person remain accountable for what is delivered or decided, and that the impacted
  individual knows AI was involved in the advice or decision" (opening of the high-risk section).
- "A qualified person must meaningfully review a High-risk AI Recommendation, with the authority to change or modify
  it, before it is delivered as advice to an individual who might rely on it or before it is used to implement a
  decision" and "The qualified person remains responsible for the accuracy and appropriateness of what is delivered or
  decided" (Requirements).
- "An individual who receives advice or who is the subject of a decision based on a High-risk AI Recommendation must
  be clearly told that AI was used to produce it" (Requirements).
- "Any operating limits to keep the equipment within safe bounds ... must be enforced by the equipment or a controller
  independent of model output" (Requirements, physical actions).
- "Users are responsible for ensuring that agents they build or deploy, including actions those agents take through
  tools, browsers, or connected systems, comply with this Usage Policy" (agentic use).

## Critical notes from the literature
- Anthropic-authored; corroborate.
- "Meaningfully review" is not defined; no test of the reviewer's capacity is required beyond "training or
  experience" and any licence.

## Where the argument uses it
- A5 (refutation sought): narrows it. The policy requires controls independent of the model for physical actions (the
  P11 move) and names the affected individual. But the controls are declared to the operator, and the affected
  individual gets notice, not the envelope. Corroboration for the notice duty: microsoft2026microsoft (disclosure of
  AI "decisions, or actions"); eu2024aiact (EU AI Act art. 50 and 26(11); facet V1).
- A8 (the humans in P19–P20 left without capacity): supports. The "qualified person" carries responsibility for the
  output; this is the liability placement Elish and Crootof et al. describe (facet G B4). No corroborating vendor rule
  that tests that person's capacity was found.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
