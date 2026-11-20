---
citekey: elmergawi2026introducing
title: "Introducing Agent Control Specification: Portable runtime governance for AI Agents"
authors: Responsible AI at Microsoft; Elmergawi, Mohamed; Abuomar, Mohammad; Crumm, Liam; Sameki, Mehrnoosh
year: 2026
type: web
doi: null
venue: Command Line (Microsoft publication), 2 June 2026
source_basis: full-text
pages_read: "whole post (Why the existing playbook breaks; Introducing ACS; interception policies; canonical policy input; worked example; Get started; relationships with Agent Framework and Agent Governance Toolkit)"
source_url: https://commandline.microsoft.com/agent-control-specification-runtime-governance/
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ms_acs_blog/page.html
sha256: 9367fe9fd82cf29e7debfec61e475db7c8e0ee98e842c2ba0b22f3504dc11b1d
manuscript_lines: []
ledger_rows: [D03, H11]
premises: [A5, A4]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
Microsoft's Responsible AI team announces the Agent Control Specification (ACS), an open, MIT-licensed manifest format
for runtime controls on agents. ACS defines eight interception points (startup, input, before and after each model
call, before and after each tool call, output, shutdown) at which a policy engine returns allow, warn, deny or escalate.
It is the closest engineering counterpart to Nadella's P11–P12: controls that "sit outside the model". The post names
who writes and audits those controls: "a security or compliance team". The people an agent emails or pays appear only
as objects of policy (an example denies messages to external recipients). Accessed 2026-10-24.

## Key facts it relies on
- "As agents gain autonomy, the question is no longer just what they can do, but what they should be allowed to do
  and who defines those boundaries" (opening section).
- "There is no standard mechanism by which a security or compliance team can define, enforce, and audit policy across
  agents" (opening section).
- "System prompts are often the first line of defense ... They’re useful, but they aren’t enforceable" (section "Why
  the existing playbook breaks").
- "pre_tool_call: inspect tool name and parameters before execution" (section "ACS: Open standard interception
  policies").
- The snapshot passed to the policy "can include the actor, roles, conversation state, prior tool calls, data
  sensitivity, approval status, or anything else the policy may need" (section "The canonical policy input").
- Worked example: "Consider an email agent that must not send messages to external recipients" (section "A worked
  example").
- "a security team gets one place to author, version, and audit controls regardless of the runtime underneath"
  (section "Relationship with Agent Framework Toolkit").

## Critical notes from the literature
- An announcement by the authors of the specification; it reports no deployment or evaluation.
- Open specification: anyone can read the format. The policies a given organisation writes in it are that
  organisation's files.

## Where the argument uses it
- A5 (the envelope declared to the deployer alone): holds, and this is the strongest primary statement found. Microsoft
  names the question ("who defines those boundaries") and answers it with the organisation's security or compliance
  team, who author and audit the manifest. Nothing in the post declares a manifest to the people the agent acts on.
- M6 (the correction held by the wrong party): supports the concession too. ACS moves enforcement out of prompts into
  a deterministic layer, which is the spacing kind of move (work moved from a reader to the artefact).
- M4(b): narrows it. The interception points are tool-call boundaries, i.e. marked points of commitment, though marked
  for the policy engine and its authors.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
