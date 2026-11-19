---
citekey: microsoft2026responsible
title: 2026 Responsible AI Transparency Report
authors: {Microsoft}
year: 2026
type: report
doi: null
venue: Microsoft Corporation (PDF created 28 Aug 2026; 35 PDF pages, two printed pages per PDF page)
source_basis: partial-text
pages_read: "PDF pp. 7, 10-15, 18-21, 27 (printed pp. 12-13, 18-29, 34-41, 52-53); keyword search of all 35 PDF pages for T1.3, A5.4, interpret, realistic, oversight, end user, affected, recipient"
source_url: https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Responsible-AI-Transparency-Report-2026.pdf
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_rai_report_2026/page.pdf
sha256: edc324345c3d01bdd4ee09f408711df18ffa99309c96da0267fbdb09467a40a7
manuscript_lines: []
ledger_rows: [E14, E15, H24, D03]
premises: [A4, A5, A7, A8]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's third annual transparency report, centred on agentic AI. It announces a "re-engineered" Responsible AI
Standard with a new Deployer Chapter, lists agent governance infrastructure (identity, runtime policies, audit logs,
approval gates), and gives two product case studies with approval steps (Copilot Cowork) and a logging failure
(Copilot file access missing from Unified Audit Logs). Two points matter for this facet. First, the human oversight
it lists is configured by organisations and exercised by users of the agent; the one provision for people outside is
attribution on Cowork's outgoing content. Second, a search of all pages found no mention of the 2022 Standard's T1.3
or A5.4 tests and no evaluation result against them. Locators below give PDF page, then printed page; where two-column extraction on a spread leaves the printed page unclear, both printed pages are given.

## Key facts it relies on
- New Standard: "New chapters in the Standard clearly distinguish developer and deployer responsibilities" (PDF p. 11,
  printed p. 20); the Standard was re-engineered by "80+ employees representing 30+ teams" (PDF p. 11, printed p. 21).
- Governance infrastructure includes "Preserve meaningful human oversight, including to: - Configure authorization and
  policy settings, such as approval gates; - Activate, block, or delete agent instances; and - Review evaluation results
  and logs through user interfaces" (PDF p. 14, printed p. 26).
- "Copilot Cowork makes actions visible in the conversation and requires explicit approval for sensitive actions
  before execution. These approaches help ensure that as agents perform more consequential actions, people retain the
  ability to supervise and intervene as well as remain accountable" (PDF p. 14, printed p. 26).
- Cowork case study: "every action that sends or modifies content requires explicit user approval before execution if
  the user did not already give permission in the initial instructions" (PDF p. 18, printed p. 34); "Outputs include
  attribution indicating AI assistance, ensuring recipients know when they are interacting with AIproduced content"
  (PDF p. 18, printed pp. 34-35; "AIproduced" as extracted from a line break).
- Copilot Health: "over 250 licensed clinicians from over two dozen countries and members of the public undertook
  human evaluations to assess the product’s clarity, tone, helpfulness, and overall safety" (PDF p. 18, printed
  pp. 34-35). This is the nearest item to a T1.3-style test found; it rates the product, not whether users can
  interpret its responses.
- Logging failure: "External researchers found that attackers could exploit Copilot to access files without those
  access points being recorded in Unified Audit Logs" (PDF p. 19, printed p. 37); Microsoft's "enhanced logging"
  captured it, and "The underlying logging issue was remediated, restoring expected audit log coverage for Copilot
  interactions" (same page).
- Application and platform cards "reinforce shared responsibility between Microsoft and customers" (PDF p. 14, printed
  p. 27).
- Deployer Chapter: deployments involve "designing experiences so users interpret outputs correctly", and "guidance is
  provided for operators responsible for monitoring system behavior, detecting anomalies, and intervening when
  necessary" (PDF p. 21, printed p. 41).
- Agent Control Specification: "It allows organizations to define deterministic controls at key checkpoints in an agent’s
  lifecycle—such as before model calls, before tool execution, and before outputs are returned" (PDF p. 27, printed pp. 52-53); ASSERT ("Reproducible verification: ASSERT uses versioned") "test datasets and scoring methods, enabling
  auditors or third parties to re-run evaluations and verify results" (PDF p. 27, printed pp. 52-53; the two-column
  extraction splits the sentence).
- Foundry tracing gives "a production-grade trace of what an agent did, which tools it called, what other agent it
  delegated tasks to, what policies were enforced" (PDF p. 27, printed pp. 52-53).

## Critical notes from the literature
- A self-report by the firm. It gives counts (cases reviewed, red-team operations) and no outcome measures of oversight.
- The re-engineered Standard itself is not published in the pages read; the report describes it. Whether T1.3 and A5.4
  survive in it cannot be checked from this report.

## Where the argument uses it
- M7 and A7 (Microsoft's own T1.3 and A5.4): the gap is confirmed in Microsoft's latest report. I found no evaluation
  of whether people "can interpret the relevant system responses" or can perform oversight "in realistic conditions";
  the nearest are human ratings of Copilot Health's clarity and safety, a design aim ("designing experiences so users interpret outputs correctly") and operator guidance.
  Holds as absence in the pages read and the keyword search.
- A5: holds with one narrowing. The runtime envelope (ACS checkpoints, approval gates) is defined by "organizations"
  and reviewed through admin interfaces; the agent's user approves Cowork's actions; recipients get attribution only.
  Attribution is notice to the person acted on, not a declared envelope.
- M4 / P15 ("tamper-proof human readable evidence"): the Unified Audit Log gap shows Microsoft's own record missing
  agent actions until outsiders found it. Holds as a counter-example to completeness; the report says the gap was
  closed.
- M4(b): narrows it. Foundry traces mark tool calls, delegations and enforced policies, i.e. points of commitment, for
  developers and operators.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
