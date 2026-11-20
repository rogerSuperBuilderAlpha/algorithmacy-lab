---
citekey: microsoft2026enabling
title: "Microsoft Copilot Studio: Enabling makers to require human approval for tool calls (Microsoft 365 Roadmap ID 570434)"
authors: {Microsoft}
year: 2026
type: web
doi: null
venue: Microsoft 365 Roadmap item, published 1 Sep 2026, as archived by the Microsoft 365 Message Center Archive (mc.merill.net)
source_basis: full-text
pages_read: "whole item (Summary, Roadmap ID, Published, Status, Release, Description)"
source_url: https://mc.merill.net/message/RM570434
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_rm570434/page.html
sha256: bfb0f22eb97c33c6e72731ce772af26ceede9cbc990a092c1fad379aaffb798e
manuscript_lines: []
ledger_rows: [H01]
premises: [A4, A5]
facet: N1
anthropic_authored: false
verified: corrected
written: 2026-10-24
---

## Summary
A Microsoft 365 Roadmap entry, read through a third-party archive of Microsoft's roadmap and message-centre posts
(the key departs from surnameYEARfirstword because `microsoft2026microsoft` is taken by the Code of Conduct card). A
Copilot Studio maker can switch on, per tool and per agent, a requirement that a person approve a tool call before it
runs. The request appears "inline in the channel where the agent is deployed", so the approver is whoever is chatting
with the agent. Status at access: "In development", general availability "September CY2026". Accessed 2026-10-24.

## Key facts it relies on
- "With a per-tool, per-agent toggle, any gated tool call pauses and shows an approval request describing what the
  agent intends to do, so a person can approve, approve for the session, or deny before the action runs" (Summary).
- "This gives organizations a deterministic guardrail for high-stakes or sensitive operations like sending emails,
  closing tickets, or processing payments, independent of the agent's instructions" (Summary).
- "Approval requests appear inline in the channel where the agent is deployed, including Microsoft Teams and Microsoft
  365 Copilot" (Summary).

## Critical notes from the literature
- Secondary host: the archive reproduces Microsoft's roadmap text; I did not open the roadmap on microsoft.com. Cite
  the official record instead: Microsoft's release API for Roadmap 570434
  (`microsoft.com/releasecommunications/api/v1/m365/570434`, read by audit N7b on 2026-10-24 and saved at
  `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N7b/m365roadmap/rm.json`, sha256
  `bbb91cdeb8ffce726cc692f0c46866af3a6d5d792d09ccfb69b0bc9206b087b2`) returns the same title, description, status
  ("In development") and date ("September CY2026").
- Announced, not shipped, at the date of access.

## Where the argument uses it
- A5 (refutation sought): narrows it. Here an end user of the agent, not only an admin, gets a confirmation step
  before an email is sent or a payment processed. The guardrail is still "for organizations", set by the maker, and
  the email recipient or payee gets no step.
- M8: the approval belongs to the user in the channel, inside the deployer's configuration; "approve for the session"
  is built in.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
