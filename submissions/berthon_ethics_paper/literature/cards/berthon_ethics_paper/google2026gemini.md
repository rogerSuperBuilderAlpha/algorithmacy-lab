---
citekey: google2026gemini
title: Gemini API Additional Terms of Service
authors: {Google}
year: 2026
type: documentation
doi: null
venue: Google AI for Developers, terms effective 23 Mar 2026 (page last updated 2026-04-28)
source_basis: partial-text
pages_read: "sections on generated content, Agentic Services, Disclaimers; other sections skimmed"
source_url: https://ai.google.dev/gemini-api/terms
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/goog_gemini_api_terms/page.html
sha256: eba98401a94ff9626322807a95ecadc96e5b8fd66fedd29feb193cb3ad71c3af
manuscript_lines: []
ledger_rows: [E14, H19]
premises: [A4, A8]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Google's additional terms for developers using the Gemini API. A paragraph on agentic services, including the Computer
Use API, makes the developer "solely responsible for the actions and tasks performed by the service" and for
"exercising judgment and supervision", and forbids automatically bypassing "any requests for human confirmation". On
outputs: "Use discretion before relying on" generated content. Accessed 2026-10-24.

## Key facts it relies on
- "When using agentic services, including the Computer Use API, you are solely responsible for the actions and tasks
  performed by the service, such as determining whether the service is appropriate for your use case, authorizing the
  service's access and connection to data, applications, and systems, and exercising judgment and supervision when and
  if the service is used in production environments" (section "Agentic Services").
- "You will not automatically bypass any requests for human confirmation" (same section).
- "Use discretion before relying on generated content, including code. You're responsible for your use of generated
  content, and for the use of that content by anyone you share it with" (generated-content paragraph).

## Critical notes from the literature
- Developer terms; Google's consumer Gemini terms were not read.

## Where the argument uses it
- M10 / A4: holds. A third supplier assigns the actions of its agents wholly to the developer and the supervision duty
  with them. Corroborates microsoft2026copilot and anthropic2025consumer.
- M8: the human confirmation request is protected by contract against automation by the developer, which shows the
  supplier treats the confirmation as a control it requires; who confirms is left to the developer.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
