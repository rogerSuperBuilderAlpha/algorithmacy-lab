---
citekey: microsoft2026audit
title: Audit logs for Copilot and AI applications
authors: {Microsoft}
year: 2026
type: documentation
doi: null
venue: Microsoft Learn, Microsoft Purview documentation (ms.date 2026-08-26)
source_basis: full-text
pages_read: "whole page, including the common-properties table, the AppHost tables (skimmed row by row), Identifying if Copilot accessed the web, Accessing Copilot audit logs"
source_url: https://learn.microsoft.com/en-us/purview/audit-copilot
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_purview_audit_copilot/page.html
sha256: 23c5922a3127e465ca78af89a06a2c1b538b8be3c27f66b672db7802bd281000
manuscript_lines: []
ledger_rows: [H07, D04]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's reference for the audit records that Copilot, Cowork, Copilot Studio agents and other AI applications
write into Microsoft Purview. A record names the user, the time, the host application, the agent, the resources
Copilot accessed (with sensitivity labels, the access action, any blocking policy and a prompt-injection flag) and
message IDs for the prompt and response. It does not carry the prompt or response text. Admins reach the records
through the Purview portal's Audit search and export. Audit of non-Microsoft AI applications is pay-as-you-go with
180-day retention. Accessed 2026-10-24.

## Key facts it relies on
- "These audit records contain details about which user interacted with Copilot, when the interaction took place, and
  where it occurred. Audit records also include references to files, sites, or other resources Copilot, Cowork, and AI
  applications accessed to generate responses to user prompts" (section "User activities with Copilot, Cowork, and AI
  applications").
- AccessedResources includes "Action refers to the nature of access which Copilot performed on the resource. Common
  values include read, create, modify" and "XPIADetected is a boolean that denotes whether there was an XPIA (Cross
  Prompt Injection Attack) detected" (common-properties table).
- Messages: "A single audit record typically contains a prompt-response pair" and the example lists only message IDs
  and an `isPrompt` flag (common-properties table, "Messages").
- "Access Copilot audit logs by using the Microsoft Purview portal and selecting Audit" (section "Accessing Copilot
  audit logs").
- "Audit logs for non-Microsoft AI applications use pay-as-you-go billing ... retains for 180 days" (section "Billing
  for auditing non-Microsoft AI applications").
- "Currently, Cowork doesn't show provider details" (section "Accessing Copilot audit logs").

## Critical notes from the literature
- The page describes the schema; it says nothing about how often anyone reads these records or how well.
- The 2026 Transparency Report (microsoft2026responsible, PDF p. 19) records an incident in which external researchers
  found Copilot could access files "without those access points being recorded in Unified Audit Logs"; the audit
  record was not complete until Microsoft fixed it.

## Where the argument uses it
- A4 / M4(a) (the record kept by one side): holds. The record of each Copilot or agent action is the tenant's, read
  by its admins in Purview. The person whose email or document the agent read or modified does not appear as a
  reader.
- M4(b) (no marked points of commitment): narrows it. The schema does mark the action type on each resource (read,
  create, modify) and a policy block, which is a partial marking of commitments, though for the admin reader.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
