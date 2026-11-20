---
citekey: google2026agentic
title: Agentic Payment Protocol (v0.2)
authors: {AP2 project (google-agentic-commerce)}
year: 2026
type: documentation
doi: null
venue: GitHub, google-agentic-commerce/AP2, docs/ap2/specification.md (v0.2 released in commit b4587ac1d0, 28 Apr 2026)
source_basis: partial-text
pages_read: "specification.md in full (Roles; Agentic vs Non-Agentic; Mandates; Modes; Direct; Autonomous; Dispute Evidence; Verification; Extension Points). Linked files (checkout_mandate.md, payment_mandate.md, flows.md, agent_authorization.md) not read"
source_url: https://raw.githubusercontent.com/google-agentic-commerce/AP2/main/docs/ap2/specification.md
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/goog_ap2_spec/page.md
sha256: 32c3be5011f481d2760e56e7b9935b0842c3da0d5f7d7b8a68402a599f1e6aa3
manuscript_lines: []
ledger_rows: [D03, D04, H07]
premises: [A5, A4]
facet: N1
anthropic_authored: false
verified: corrected
written: 2026-10-24
---

## Summary
The normative AP2 specification. Five roles: Shopping Agent, Credential Provider, Merchant, Merchant Payment Processor
and a "Trusted Surface" that obtains "informed user consent". In "Human Not Present" mode the user "sees and approves
a set of constraints"; the agent then signs a closed mandate, and verifiers check it against the constraints of the
user-signed open mandate that are relevant to it; only those constraints are shared with the verifier. In a dispute the mandates and receipts "provide a non-repudiable picture of the transaction",
retrievable from the agent's side as well as the merchant's. Accessed 2026-10-24.

## Key facts it relies on
- "Trusted Surface (TS): The Trusted Surface role is a UI surface that is trusted to get informed user consent for an
  Intent before creating a user-signed Mandate" (Roles).
- "Human Not Present (Autonomous): The User sees and approves a set of constraints over what closed Checkout and
  Payment would meet their intent" (Modes).
- "Constraints in these Mandates allow the verifier to verify that the Checkout and Payment match the User's intent.
  Only constraints relevant to the closed Mandates are shared with the verifier." (Modes).
- "In the case of a dispute, the Checkout Mandate and Receipt, and Payment Mandate and Receipt can be brought together
  to provide a non-repudiable picture of the transaction" (Dispute Evidence); the Checkout Mandate may be provided by
  the Shopping Agent or the Merchant (same section).
- "Specific details of how this is used for dispute resolution, retention, and retrieval requirements are outside the
  scope of this specification" (Dispute Evidence).

## Critical notes from the literature
- A draft protocol (v0.2); adoption not shown. "Roles MAY always delegate their responsibilities to another party"
  (Roles), so the user's record may in practice sit with the Shopping Agent's provider.
- The spec (v0.2) has no "Intent Mandate"; it speaks of "open" Checkout and Payment Mandates. "Intent Mandate" is the
  2025 blog's term (parikh2025powering).
- The copy was fetched from the `main` branch on 2026-10-24, which can change without notice; the commit hash of the
  fetched copy was not recorded (the v0.2 release commit named in `venue` is b4587ac1d0).

## Where the argument uses it
- A5 and M4: the refutation in its normative form (see parikh2025powering). The envelope (constraints) is approved by
  the user, and the verifier checks the closed mandate against the constraints relevant to it, which are all it is
  shown; the record of commitments exists on both sides. Narrower than it looks: the
  person signs through a "Trusted Surface" someone else runs, and dispute use is out of scope.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
