---
citekey: zhao2026agentgui
title: "AgentGUI: An Interface for Observing and Steering Long-Running AI Agents"
authors: Zhao, Xuan; Sohn, Jiwoong; Zheng, Qinyue; Moor, Michael
year: 2026
type: article
doi: null
venue: arXiv preprint arXiv:2607.26300v2 (July 2026)
source_basis: partial-text
pages_read: "pp. 1, 4 (user study: design and results), 6 (limitations); system description skimmed"
source_url: https://arxiv.org/pdf/2607.26300v2
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/arx_agentgui2026/page.pdf
sha256: dafff9931d4a752c5d9a1b4fda46b9acc84988406b9d4aecc5232b7bb9a8cf77
manuscript_lines: []
ledger_rows: [H07]
premises: [A4]
facet: N1
anthropic_authored: false
verified: true
written: 2026-10-24
---

## Summary
An interface for watching and steering long-running coding and research agents, with structured trajectory views. In a
within-participant study (N = 8) participants answered lookup questions about agent traces (overall activity, time
breakdown, output artifacts) 38% faster than with the agent framework's native dashboard (90 s against 145 s per
question) and more accurately (93% against 80%). The questions came with guidance on where to look, and the authors
call the sample small and homogeneous.

## Key facts it relies on
- "Participants completed questions 38% faster with AgentGUI than with the baseline interface, taking on average 90 s
  rather than 145 s per question (p = 0.023" (p. 4; the parenthesis continues with an appendix reference).
- "Accuracy improved to 93% from 80% (p = 0.031" (p. 4), "although this was impacted by a low (50%) score on the
  baseline interface" in one question type (p. 4).
- "each participant was given five minutes of UI exploration, and the quiz included guidance on the location of
  relevant information" (p. 4).
- "the small and rather homogeneous user study limits the statistical test power and may not be fully generalizable"
  (p. 6).

## Critical notes from the literature
- Preprint; N = 8; lookup questions with location hints, not detection of misbehaviour.

## Where the argument uses it
- M4 (refutation sought): narrows it. With a structured view and guidance, people find facts in agent traces fast and
  accurately (80% even with the baseline dashboard). That is lookup of stated facts, not reconstruction of whether an
  action was right; set beside kutasov2025shade (dxd card: AUC 0.65 after about 103 minutes per transcript) it shows
  the reading task Nadella's P15 implies is the hard one.

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** confirmed

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** No issues found.
