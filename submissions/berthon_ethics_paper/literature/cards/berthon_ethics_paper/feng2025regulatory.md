---
citekey: feng2025regulatory
title: On the Regulatory Potential of User Interfaces for AI Agent Governance
authors: Feng, K. J. Kevin; Kim, Tae Soo; Pang, Rock Yuren; Huq, Faria; August, Tal; Zhang, Amy X.
year: 2025
type: article
doi: null
venue: arXiv preprint arXiv:2512.00742v1 [cs.CY], 30 Nov 2025
source_basis: full-text
pages_read: "pp. 1-4 (all main text) and appendix pp. 8-10 (figures of examples); references pp. 5-8 skimmed"
source_url: https://arxiv.org/pdf/2512.00742
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/arx_regulatory_ui/page.pdf
sha256: 3b1935311d11805ff71353c61cd55d4be2f9c5950e97324008e70072d5962f5f
manuscript_lines: []
ledger_rows: [D03, D04, H24]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
The authors analyse the user interfaces of 22 publicly available agentic systems and derive six design patterns they
propose as targets for regulation: visible thoughts, plans and actions; control transfer (interrupt and take over);
watch mode; customisable rule-based governance; inspectable and editable memory; and sandboxes with visible health.
Every pattern addresses the agent's user. None addresses the people or parties the agent acts on. They note that
visible reasoning depends on faithfulness and that "watching" does not guarantee attention.

## Key facts it relies on
- "we analyze 22 existing agentic systems to identify UI elements that play key roles in human-agent interaction and
  communication" (abstract, p. 1).
- Visible thoughts: "these benefits depend on the faithfulness of the expressed reasoning to the agent’s actual
  internal processes"; "too little detail undermines oversight, while too much risks overwhelming users" (p. 2).
- Rule-based governance: "User-specified rules override any “self-approval” settings where the agent approves its own
  actions (e.g., Cursor’s auto-run" (p. 3); "agents might subtly nudge users toward approval" (p. 3).
- Watch mode: "requiring user simply “watching” does not guarantee meaningful attention or control — users may become
  complacent or distracted" (p. 3).
- "many developers have voluntarily made an agent’s thoughts visible, but few currently communicate sandbox health"
  (p. 4).

## Critical notes from the literature
- A short workshop-style paper; the system sample and coding are summarised, not tabulated, in the main text.

## Where the argument uses it
- A4 (how current tools present traces and approvals): holds as a survey. Traces, interrupts and approvals in 22 tools
  are user-facing controls for the agent's principal.
- A5 (refutation sought): narrows it for the user. "Customizable rule-based governance" lets the user declare rules
  that bind the agent, an envelope declared by and to the principal. No pattern declares an envelope to a third party.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
