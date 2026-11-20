---
citekey: microsoft2026use
title: Use Copilot Cowork
authors: {Microsoft}
year: 2026
type: documentation
doi: null
venue: Microsoft Learn, Microsoft 365 Copilot documentation (ms.date 2026-09-14)
source_basis: partial-text
pages_read: "sections Start a session; Follow along as Cowork works; Approve actions; Review and respond to an approval request; Work with files (to Supported file types). Not read: preview formats and later sections"
source_url: https://learn.microsoft.com/en-us/copilot/microsoft-365/cowork/use-cowork
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_cowork_use/page.html
sha256: 2af382de235218777bd3ff19304cca40ee8f9da7e4015c0e11c56286f6e8f56d
manuscript_lines: []
ledger_rows: [H19, E15]
premises: [A4, A5, A8]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's user guide to Copilot Cowork, the M365 agent that sends email, posts in Teams, schedules meetings and edits
files on a user's behalf. It shows what the user sees while the agent works (a "Thinking indicator" animation,
step-by-step status updates, some background steps hidden) and how approvals work. Sensitive actions require the
user's approval; the dialog offers one-time approval, "don't ask again" options for the session, and "Approve All"
for pending approvals. The guide tells the user to "Always review the details before you approve." Accessed 2026-10-24.

## Key facts it relies on
- "Thinking indicator: An animation lets you know Cowork is processing your message" (section "What displays while
  Cowork is working").
- "Some background operations, like script execution, run without displaying individual steps. This approach keeps
  the session focused on results" (same section, Note).
- "Cowork asks for your permission before taking sensitive actions, like sending an email or posting a message in
  Teams" (section "Approve actions").
- Options: one approval "this one time"; a dropdown that "Approves the action and skips the prompt for similar actions
  for the rest of the current session", for email by recipient, domain or "Always allow"; and "Approve All": "When
  multiple approvals are pending, allows all of them to proceed at once" (approval options table).
- "Always review the details before you approve. Cowork shows you exactly what it plans to do. Check that the
  recipients, content, and other details are correct" (section "Review and respond to an approval request",
  Important).
- "To show the technical details of the action, select Show parameters" (same section).

## Critical notes from the literature
- A how-to page; it reports no data on approval rates. The 2026 Transparency Report describes the same approval rule
  (microsoft2026responsible, PDF p. 18).

## Where the argument uses it
- M3 / P9 (who reads reasoning): holds for this product. The user sees an animation and status lines, not the model's
  reasoning; background script steps are not shown.
- M8 and A8: holds. The confirmation step belongs to the agent's user, and the product supplies the means to stop
  reviewing (session-wide skip, "Approve All"); the review duty is stated as the user's ("Always review").
- A5 (refutation sought): narrows it for the user. The agent's user gets a binding pre-action check on sensitive
  actions. The recipient of the email gets attribution only (microsoft2026responsible).

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
