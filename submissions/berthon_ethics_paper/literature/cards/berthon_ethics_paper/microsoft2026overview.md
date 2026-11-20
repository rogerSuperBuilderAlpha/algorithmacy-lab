---
citekey: microsoft2026overview
title: Overview of Microsoft Agent 365
authors: {Microsoft}
year: 2026
type: documentation
doi: null
venue: Microsoft Learn (ms.date 2026-08-19; page footer "Last updated on 2026-08-20")
source_basis: full-text
pages_read: "whole page (sections Observe, Govern, Secure, Agent 365 availability and prerequisites, Plans and licensing)"
source_url: https://learn.microsoft.com/en-us/microsoft-agent-365/overview
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_agent365_overview/page.html
sha256: 885b6170bffaa496081f34ad601fc7e714eee1ae8522c0266ec088bf8a243049
manuscript_lines: []
ledger_rows: [E14, D03]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's product overview of Agent 365, the control plane it sells for agents across an organisation. The page
names three functions (observe, govern, secure) and, for each, names who sees and who decides: admins, "leaders and
AI admins", and "security and business leaders". It names no role for the people an agent acts on. Agent 365 became
generally available on 1 May 2026 and is licensed per user. Accessed 2026-10-24.

## Key facts it relies on
- Observe: Agent 365 "gives organizations real-time visibility into their agentic environment, helping admins
  understand how agents are used, identify performance or risk signals early, and take action before issues impact
  the business" (section "Observe").
- Observe: "Admins can now view all their agents in a single, centralized registry"; the insights "help leaders and AI
  admins stay in control"; "Role-specific oversight extends this visibility to security and business leaders"
  (section "Observe").
- Govern: "admins can intentionally manage the lifecycle of their organization’s agents while ensuring the right
  permissions, policies, and reviews are in place", so that agents "remain aligned with organizational policies and
  business needs" (section "Govern").
- Secure: "Microsoft Entra enforces consistent, risk‑based access controls for users and agents acting on their
  behalf" (section "Secure").
- Availability: "As of May 1, 2026, Microsoft Agent 365 is generally available for the Commercial segment on a per
  user basis" (section "Agent 365 availability and prerequisites").

## Critical notes from the literature
- A marketing-level product overview; it describes capabilities, not their use or effect.
- The audience of every control on the page is inside the deploying organisation. That matches the reading of P5 and
  P17 in facet G (C7(ii)) and facet V1 (Q1).

## Where the argument uses it
- A5 (outline, "The one move that resembles the correction"): Microsoft's own control plane for agents declares the
  agent registry, permissions and policies to admins and leaders; the page names no disclosure to the people acted
  on. Holds for this page; it is a product overview, not a full specification.
- A4 / M1 (custody with the deploying organisation): holds; alignment is to "organizational policies and business
  needs".

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
