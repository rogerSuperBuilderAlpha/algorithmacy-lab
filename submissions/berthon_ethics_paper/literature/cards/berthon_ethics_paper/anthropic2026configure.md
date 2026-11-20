---
citekey: anthropic2026configure
title: Configure permissions
authors: {Anthropic}
year: 2026
type: documentation
doi: null
venue: Claude Code Docs (code.claude.com)
source_basis: partial-text
pages_read: "opening (tiered permission system); permission modes table and bypassPermissions note; precedence among rules, hooks and mods (opening); Managed settings; Settings precedence. Not read: rule-syntax sections in detail"
source_url: https://code.claude.com/docs/en/permissions
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ant_cc_permissions/page.html
sha256: f7ebd215f1f5108e02c6a8731bd05dec5eff45fc55e82190edeed79fb916abad
manuscript_lines: []
ledger_rows: [H01, H11]
premises: [A4, A5]
facet: N1
anthropic_authored: true
verified: true
written: 2026-10-24
---

## Summary
Anthropic's reference for Claude Code permissions. Manual mode asks the user before actions; other modes ask less;
in auto mode "a classifier reviews actions instead of you"; bypassPermissions skips prompts. Organisations deploy
managed settings that "user and project settings can’t override", and "no other level ... can override a managed
permission rule". The permission envelope of a coding agent is thus layered: the administrator's rules on top, the
user's below, a classifier in place of the user in auto mode. Accessed 2026-10-24.

## Key facts it relies on
- "The other permission modes change which of these ask you; in auto mode a classifier reviews actions instead of
  you" (opening section).
- "In bypassPermissions mode, Claude Code skips permission prompts, including for writes to protected paths such as
  .git and .claude" and "Only use this mode in isolated environments like containers or VMs" (permission modes).
- "For organizations that need centralized control, administrators deploy managed settings that user and project
  settings can’t override, apart from a few security-sensitive keys" (section "Managed settings").
- "Permission rules follow the same settings precedence as all other Claude Code settings, with managed settings
  highest: no other level, including command line arguments, can override a managed permission rule" (section
  "Settings precedence").

## Critical notes from the literature
- Anthropic-authored; corroborate.
- The page describes the mechanism. Approval-rate evidence for the same product is in anthropic2026how (dxd card,
  93% of prompts approved) and anthropic2026measuring (auto-approve share rises with experience).

## Where the argument uses it
- A5: holds for coding agents. The binding envelope is set by the administrator and declared to the user through the
  settings files; nothing reaches people outside the organisation. Corroborated by openai2026agent (managed
  requirements "take precedence").
- M8: holds. The user's per-action gate can be replaced by a classifier (auto mode), as at OpenAI (Auto-review,
  openai2026agent).

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
