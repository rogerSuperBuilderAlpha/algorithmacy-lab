---
citekey: microsoft2025multistage
title: Multistage and AI approvals in agent flows (preview)
authors: {Microsoft}
year: 2025
type: documentation
doi: null
venue: Microsoft Learn, Microsoft Copilot Studio documentation (ms.date 2025-09-04; prerelease documentation)
source_basis: full-text
pages_read: "whole page: What are multistage approvals; Key functionalities; Set up; Bringing it all together; Responding to approvals; More on AI stages"
source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_cs_advanced_approvals/page.html
sha256: f7a51a39978b8858094374d5be7e568408c723224ab9c52b2b63136b157a0fa3
manuscript_lines: []
ledger_rows: [H01, E15]
premises: [A4, A8]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's guide to approval workflows in Copilot Studio agent flows. A maker chains manual stages (named human
approvers), AI stages (a model returns "Approve or Reject" with a rationale) and conditions. The worked expense
example lets an AI stage approve a request under $5,000 and end the process "as approved" with no human stage. The
page advises human stages for sensitive decisions but does not require them. Approvers respond through Teams, Outlook
or the Power Automate portal. Accessed 2026-10-24; the feature is in preview.

## Key facts it relies on
- "Multistage approvals combine human and AI reviews to make approval decisions based on given instructions,
  documents, and images" (section "What are multistage approvals?").
- AI stage: "the AI produces a clear Approve or Reject decision with clear rationale based on your instructions"
  (section "AI approval stages").
- Example: "If the amount is under $5,000 and the AI stage approves it, the request can bypass manager approval and
  automatically end as approved" (section "Add and configure a condition").
- "By default, if the AI stage approves, the approval continues to the next stage. If the AI stage rejects, the
  approval ends as rejected. If the approval fails to give an approve or reject decision, it continues to the next
  stage" (section "Add and configure an AI stage").
- Advice only: "For these scenarios, ensure that human approval stages are reached in the flow so that humans remain
  in ultimate control of important decisions" (section "Using AI approvals for sensitive cases").
- "Where possible, favor the more powerful models for approval decisions" (section "Add and configure an AI stage").

## Critical notes from the literature
- Preview documentation; "subject to change".
- The approvers are the organisation's staff; the requester (an employee filing an expense) is the person decided
  about. Neither the page nor the flow gives the requester a view of the AI stage's instructions.

## Where the argument uses it
- M8 (the gate held by the few): holds, and adds a turn the post does not name. In Microsoft's own approval product
  the gate can be held by a model, with a human stage optional; the human "authorized person" of P19 is a design
  choice the maker may skip.
- A8 (the humans in P19–P20 left without capacity): supports. Where a human stage follows an AI stage, the human
  reviews an AI rationale, the reading task facet G's alert-review evidence bears on.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
