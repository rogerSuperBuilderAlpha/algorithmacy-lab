---
citekey: microsoft2026tracing
title: Tracing and data handling
authors: {Microsoft}
year: 2026
type: documentation
doi: null
venue: Microsoft Learn, Microsoft Foundry observability documentation (ms.date 2026-06-02)
source_basis: full-text
pages_read: "whole page (what tracing records; default state; enable; disable; where data is stored; data sharing considerations; privacy; customer responsibilities; summary)"
source_url: https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-data
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_foundry_trace_data/page.html
sha256: f56deb56dbc768443d7e1fd68f3079e425df3845061d8255583e03219da68a18
manuscript_lines: []
ledger_rows: [H07, D04]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's statement of what Foundry agent traces contain and who controls them. Traces record user inputs, model
inputs and outputs, tool calls and intermediate steps. Tracing is off by default and starts only when a Foundry owner
connects Application Insights. The customer controls collection, storage, retention and who may read; readers are
staff holding Azure monitoring roles. The customer's duty toward end users is to inform them. Accessed 2026-10-24.

## Key facts it relies on
- Tracing records "User inputs and prompts", "Agent and model inputs and outputs", "Tool calls and intermediate steps"
  and "Execution metadata" (opening list).
- "Tracing is off by default." and "No trace data is collected or stored unless explicitly enabled by Foundry Account
  Owner or Foundry Owner" (section "Default state").
- "This ensures customers retain control over when data collection begins" (section "Default state").
- "Project members with the Log Analytics Reader role in AppInsights can view trace data, which might contain personal
  data and customer content" (Important box).
- "Customers are responsible for configuring access controls and ensuring compliance with their organizational
  policies" (section "Data sharing considerations").
- Customer responsibility: "Informing end users about data collection, including the types of data being collected,
  the purpose, who has visibility, their options" (section "Customer responsibilities").

## Critical notes from the literature
- Developer documentation; it describes the default and the controls, not how deployers set them.

## Where the argument uses it
- M4(a) / P15 (the record kept by one side): holds. In Microsoft's agent platform the trace exists only if the
  deployer turns it on, lives in the deployer's telemetry store, and is read by holders of the deployer's roles. End
  users are told about collection; the page gives them no access to the trace.
- A5: holds. The observability layer is declared and governed toward the deploying customer.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
