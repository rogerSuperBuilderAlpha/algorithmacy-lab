---
citekey: openai2026agent
title: Agent approvals & security
authors: {OpenAI}
year: 2026
type: documentation
doi: null
venue: OpenAI Codex documentation (developers.openai.com)
source_basis: partial-text
pages_read: "sections opening; Migrate from the retired untrusted approval policy; Sandbox and approvals; Safety monitoring and paused tasks; Automatic approval reviews; Common sandbox and approval combinations. Not read in full: network access, dangerous settings, configuration reference"
source_url: https://developers.openai.com/codex/agent-approvals-security
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/oai_codex_approvals/page.html
sha256: 50d40da338fe26812f6f41375f3e65e6be84c5b4e93573950e95154faa701fb1
manuscript_lines: []
ledger_rows: [H01, E15, D03]
premises: [A4, A5, A8]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
OpenAI's security guide for Codex, its coding agent. Controls come in two layers: a sandbox (what the agent can touch)
and an approval policy (when it must ask). Approvals go to the user by default, but a setting routes them to an
"Auto-review" reviewer agent "instead of surfacing to the user". The reviewer's default policy is public in the
open-source repository; enterprises may replace its tenant-specific section through managed requirements that
override local settings. Asynchronous safety monitoring can pause a task, possibly after the triggering action.
Accessed 2026-10-24.

## Key facts it relies on
- "Approval policy: When Codex must ask you before it executes an action (for example, leaving the sandbox, using the
  network, or running commands outside a trusted set)" (section "Sandbox and approvals").
- "By default, approval requests route to you" (section "Automatic approval reviews").
- Auto-review mode: "eligible approval requests are reviewed by Auto-review instead of surfacing to the user"
  (combinations table).
- "The reviewer policy checks for data exfiltration, credential probing, persistent security weakening, and
  destructive actions. Low-risk and medium-risk actions can proceed when policy allows them" (section "Automatic
  approval reviews").
- "The default reviewer policy is in the open-source Codex repository. Enterprises can replace its tenant-specific
  section with guardian_policy_config in managed requirements" and "managed requirements take precedence" (same
  section).
- "A pause can arrive after the activity that triggered it; monitoring doesn’t replace sandboxing, permissions, or
  review of the result" (section "Safety monitoring and paused tasks").
- "Dangerous full access ... No sandbox; no approvals (not recommended)" (combinations table).

## Critical notes from the literature
- Developer documentation; no data on how often each mode is used.
- The Anthropic counterpart (anthropic2026configure: "in auto mode a classifier reviews actions instead of you")
  corroborates the same design move at a second vendor.

## Where the argument uses it
- M8 (the gate): holds with a new turn. In coding agents the approval prompt, the human gate, is being handed to a
  reviewer model; the human reviews what that reviewer escalates.
- A5 (refutation sought): narrows it slightly. OpenAI publishes the default reviewer policy, so its envelope is
  readable by anyone; but enterprises may replace it, and the replacement is not declared to anyone outside.
- P15 / M4: the monitor's pause "can arrive after the activity", a vendor admission that after-the-fact records and
  alerts lag the action.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
