---
citekey: anthropic2026thinking
title: Thinking
authors: {Anthropic}
year: 2026
type: documentation
doi: null
venue: Claude Platform Docs (platform.claude.com)
source_basis: partial-text
pages_read: "opening sections on thinking blocks; supported-model notes; Controlling thinking display; Summarized thinking. Not read: streaming, tool-use and encryption sections beyond the summary points"
source_url: https://platform.claude.com/docs/en/build-with-claude/thinking
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/ant_thinking_overview/page.html
sha256: a7fbf5dd1bc5438ed2d6da018939cd97a32d2409b3a7215bc71475e7e993f877
manuscript_lines: []
ledger_rows: [H24, H22]
premises: [A4, A8]
facet: N1
anthropic_authored: true
verified: corrected
written: 2026-10-24
---

## Summary
Anthropic's developer documentation on Claude's thinking. The text in a thinking block is "a summary of Claude's
reasoning", written by a different model; "No display setting returns the raw chain of thought." On current models
the default is "omitted", which returns an empty thinking field with an encrypted signature. The developer, and so
any end user downstream, sees either nothing or a summary through the API settings; the same section offers full
thinking output to some customers by arrangement with Anthropic sales. Accessed 2026-10-24.

## Key facts it relies on
- "You don't always see this text, and what you see is never the raw chain of thought: the text in a thinking block
  is a summary of Claude's reasoning" (opening section).
- "Each thinking block also carries a signature field, an encrypted copy of the full reasoning that you pass back
  unchanged" (opening section).
- "display defaults to "omitted" on these models, so the thinking text is hidden until you opt in" (supported-model
  notes; quotation marks as on the page).
- "Summarized thinking provides the full intelligence benefits of thinking while preventing misuse. No display
  setting returns the raw chain of thought" (section "Summarized thinking").
- "Summarization is processed by a different model from the one you target in your requests. The thinking model does
  not receive the summarized output" (section "Summarized thinking").
- "In rare cases where you need access to full thinking output, contact Anthropic sales." (section "Summarized
  thinking", its last sentence; "contact Anthropic sales" is a mailto link on the page).

## Critical notes from the literature
- Anthropic-authored; corroborate. The drafting model of this facet is an Anthropic model.
- The stated reason for withholding the raw reasoning is "preventing misuse".

## Where the argument uses it
- M3 / P9: holds, narrowed. No API setting returns the raw chain of thought; full thinking output is available to
  some customers by arrangement with Anthropic sales. The readable artefact a deployer gets through the API is a
  summary by another model. Corroborated by openai2026reasoning (OpenAI: "we don’t expose the raw reasoning
  tokens") and by palod2026evaluating (p. 2, describing OpenAI, Google and Anthropic).

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
