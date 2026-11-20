---
citekey: parikh2025powering
title: Powering AI commerce with the new Agent Payments Protocol (AP2)
authors: Parikh, Stavan; Surapaneni, Rao
year: 2025
type: web
doi: null
venue: Google Cloud Blog, 16 Sep 2025
source_basis: full-text
pages_read: "whole post, including the partner quotations"
source_url: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/goog_ap2_blog/page.html
sha256: cfcbee107b4d3d2f0ad19763d35f7f0d0d3575f78d6c456da425bfd88d11790e
manuscript_lines: []
ledger_rows: [D03, D04, H07, H10]
premises: [A5, A4]
facet: N1
anthropic_authored: false
verified: corrected
written: 2026-10-24
---

## Summary
Google announces AP2, an open protocol, built with payment networks and merchants, for payments that AI agents make.
Its core instrument is the "Mandate": a cryptographically signed record of what the user authorised. In delegated
purchases the user signs an "Intent Mandate" in advance that "specifies the rules of engagement—price limits, timing,
and other conditions", and the chain intent → cart → payment forms "a non-repudiable audit trail". The blog does not
itself say that merchants verify purchases against the Intent Mandate; verification by counterparties is the spec's
(`google2026agentic`, Modes), and there only for the constraints relevant to the closed Mandates ("Only constraints
relevant to the closed Mandates are shared with the verifier"). This is the clearest case found of an operating
envelope that is declared in advance, signed by the person on whose behalf the agent acts, and checked in part by the
counterparty under the spec. Accessed
2026-10-24.

## Key facts it relies on
- Problems AP2 addresses include "Authenticity: Enabling a merchant to be sure that an agent's request accurately
  reflects the user's true intent" and "Accountability: Determining accountability if a fraudulent or incorrect
  transaction occurs" (section "Why is a protocol needed?").
- "AP2 builds trust by using Mandates—tamper-proof, cryptographically-signed digital contracts that serve as
  verifiable proof of a user's instructions" (section "How it works").
- Delegated tasks: "you sign a detailed Intent Mandate upfront. This mandate specifies the rules of engagement—price
  limits, timing, and other conditions" (same section).
- "This complete sequence—from intent, to cart, to payment—creates a non-repudiable audit trail that answers the
  critical questions of authorization and authenticity" (same section).

## Critical notes from the literature
- A launch post by the vendor; it reports no deployment data. Partner quotations are promotional.
- The protocol serves the counterparties' needs (merchant certainty, fraud and dispute liability) as much as the user's;
  the post names merchants, issuers and networks as the parties needing "clarity ... to effectively manage risk".

## Where the argument uses it
- A5 (refutation, found): this cuts A5 as a claim about LLM tools in general. Agentic payments already declare a
  user-signed envelope (the Intent Mandate) and give the user the signing role; under the spec (`google2026agentic`)
  the counterparty verifies the closed mandate against only the constraints relevant to it. The argument can
  keep A5 only as a claim about Nadella's post and Microsoft's agent controls, and should name AP2 as the
  counter-instance.
- M4(b) (no marked points of commitment): cuts it for payments. The mandate is a marked commitment point.
- D03 / D04 (the duties): AP2 is a working precedent for both, in a domain where the counterparty has commercial
  standing and liability rules already exist (card networks). The paper's duties section could name it.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
