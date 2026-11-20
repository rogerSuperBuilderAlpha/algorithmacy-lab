---
citekey: microsoft2026connect
title: Connect agents to MCP server endpoints
authors: {Microsoft}
year: 2026
type: documentation
doi: null
venue: Microsoft Learn, Microsoft Foundry Agent Service documentation (ms.date 2026-09-29)
source_basis: partial-text
pages_read: "sections Considerations for using non-Microsoft services and servers; best practices for MCP servers; First-success route: connect, approve, verify, and clean up; the Python and C# approval samples. Not read: authentication, toolbox and long-running-tool sections in detail"
source_url: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_foundry_mcp/page.html
sha256: 1e50a2ee685495e34c0858a3170180efaa3bd4541d7b3e786f74b50d3696d6ec
manuscript_lines: []
ledger_rows: [E14]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's developer guide for connecting Foundry agents to MCP tool servers. The approval mechanism is a developer
setting (`require_approval="always"`); when it fires, the agent returns an `mcp_approval_request` and the developer's
code must send back an approval response. The sample approves at a console prompt and comments "In production,
implement your own approval UX and policy." Microsoft disclaims responsibility for third-party MCP servers and places
responsibility for data and tool selection on the customer. Accessed 2026-10-24.

## Key facts it relies on
- "Third parties, not Microsoft, create the remote MCP servers that you decide to use ... Microsoft doesn't test or
  verify these servers. Microsoft has no responsibility to you or others in relation to your use of any remote MCP
  servers" (section "Considerations for using non-Microsoft services and servers").
- "You're responsible for your use of non-Microsoft services and data, along with any charges associated with that
  use" (same section).
- Best practices: "Require approval for high-risk operations, especially tools that write data or change resources";
  "Review the requested tool name and arguments before you approve"; "Log approvals and tool calls for auditing and
  troubleshooting" (best-practices list).
- Sample code comments: "# Approve only after you review the tool call." and "# In production, implement your own
  approval UX and policy." (Python sample).

## Critical notes from the literature
- Developer documentation; it shows what the platform leaves to the deployer, not what deployers do.

## Where the argument uses it
- A5 (the envelope declared to the deployer alone): holds for this platform. The allow-list, the approval setting and
  the approval interface are all the deploying developer's to define; Microsoft supplies the hook, not the reviewer.
- M10 (the burden on the reader): holds in a narrower form. The reviewing duty ("Review the requested tool name and
  arguments") falls on whoever the deployer makes approver.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
