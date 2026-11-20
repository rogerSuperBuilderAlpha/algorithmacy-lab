---
citekey: anthropic2025commercial
title: Commercial Terms of Service
authors: {Anthropic}
year: 2025
type: documentation
doi: null
venue: Anthropic legal page, effective 17 Jun 2025
source_basis: partial-text
pages_read: "sections A (services, third-party features), D (customer obligations, including D.3), L.2 (disclaimer of warranties); other sections skimmed"
source_url: https://www.anthropic.com/legal/commercial-terms
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ant_commercial_terms/page.html
sha256: 6de1dbfceace63fd349bcc1c8ffc597969f2d2e3af684e9e32ee54120b14f6af
manuscript_lines: []
ledger_rows: [E14, H19]
premises: [A4, A5]
facet: N1
anthropic_authored: true
verified: true
written: 2026-10-24
---

## Summary
Anthropic's terms for business customers of its API. Clause D.3 puts the judgment about human review on the customer
and requires the customer to pass a verification duty down to its own users: they must be told that factual
assertions "should not be relied upon without independently checking their accuracy". The chain runs supplier to
deployer to user; the person acted on is not named. Accessed 2026-10-24.

## Key facts it relies on
- "It is Customer’s responsibility to evaluate whether Outputs are appropriate for Customer’s use case, including
  where human review is appropriate, before using or sharing Outputs" (D.3).
- "Customer acknowledges, and must notify its Users, that factual assertions in Outputs should not be relied upon
  without independently checking their accuracy" (D.3).

## Critical notes from the literature
- Anthropic-authored; corroborate.

## Where the argument uses it
- M10 / A4: holds. The supplier contract hands the verifying duty to the deployer and obliges the deployer to hand it
  on to users. Microsoft's Code of Conduct has the same structure (microsoft2026microsoft: oversight "so customers can
  find and mitigate undesirable behaviors").
- P3 ("A model provider's assurances do not relieve us"): the supplier's own terms agree; the provider gives none.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
