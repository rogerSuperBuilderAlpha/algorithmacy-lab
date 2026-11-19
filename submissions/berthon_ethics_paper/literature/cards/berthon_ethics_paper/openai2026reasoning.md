---
citekey: openai2026reasoning
title: Reasoning models
authors: {OpenAI}
year: 2026
type: documentation
doi: null
venue: OpenAI API documentation (developers.openai.com; platform.openai.com/docs/guides/reasoning redirects here)
source_basis: partial-text
pages_read: "sections How reasoning works; Preserve reasoning across calls; encrypted reasoning items (stateless mode); Reasoning summaries. Not read: prompting advice, phase parameter, code samples in other languages"
source_url: https://developers.openai.com/api/docs/guides/reasoning
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/N1/oai_reasoning_guide/page.html
sha256: 7a4701cc6b275da6a04f682f9da492dbf33f4c970f03f5acb6894ff1715847da
manuscript_lines: []
ledger_rows: [H24, H22]
premises: [A4, A8]
facet: N1
anthropic_authored: false
verified: corrected
written: 2026-10-24
---

## Summary
OpenAI's developer guide to its reasoning models. Reasoning tokens are generated, billed and, on some models, carried
between turns, but the API never returns them. A developer can opt in to a summary of the reasoning; summaries on the
latest models may require "organization verification". Reasoning items passed between calls are opaque or encrypted.
So the deploying developer, not only the end user, sees at most a summary written by the provider's system.
Accessed 2026-10-24.

## Key facts it relies on
- "While reasoning tokens are not visible via the API, they still occupy space in the model’s context window and are
  billed as output" (section "How reasoning works"; line breaks in the page).
- "Persisted reasoning provides continuity; it does not expose the model’s raw reasoning. The reasoning items remain
  opaque, and the API does not return their reasoning text" (section "Preserve reasoning across calls").
- Stateless mode: reasoning items "include an encrypted_content property containing encrypted reasoning tokens that
  you can pass to future calls" (encrypted reasoning section).
- "While we don’t expose the raw reasoning tokens emitted by the model, you can view a summary of the model’s
  reasoning using the summary parameter" (section "Reasoning summaries").
- "This output will not be included unless you explicitly opt in to including reasoning summaries" (same section).
- "Before using summarizers with our latest reasoning models, you may need to complete organization verification"
  (same section).

## Critical notes from the literature
- Developer documentation for the API; ChatGPT's consumer display was not read (openai.com pages served a 403 page).
- URL: `source_url` (developers.openai.com) and the `SOURCE_URL.txt` beside the saved copy
  (`https://platform.openai.com/docs/guides/reasoning`) differ. Audit N7b's fresh fetch of `source_url` on 2026-10-24
  is byte-identical to the saved file, so `source_url` is the page read; `SOURCE_URL.txt` still needs aligning.
- Palod et al. (palod2026evaluating, p. 2) report the same practice across OpenAI, Google and Anthropic: users are
  shown "what seems like a summarized version of the reasoning traces".

## Where the argument uses it
- M3 / P9 (who is meant to read chain of thought): holds, and sharpens it. In OpenAI's product the raw chain of thought
  is withheld from the deployer as well as the user; what anyone outside the provider reads is a provider-written
  summary, an account of the reasoning in the jurat's sense (H22), not the reasoning.
- A8: supports the P9 concession reading. P9's "non-negotiable" transparency is not on offer from the model
  suppliers an enterprise deploys (anthropic2026thinking corroborates for Anthropic; google Gemini "thought summaries"
  read in `goog_thinking/page.html`, not carded).

## Verifier notes

---

## S2 adversarial verification (2026-10-24)

**Verdict:** corrected

**What was checked:** existence against Crossref or the official record; sha256 of the file at `local_path` recomputed; every quotation string-matched against that file with its locator; each quotation read against the claim hung on it. Audit: `nadella/facets/AUDIT_N7b.md`.

**Findings:** Fixes from the audit applied to this card's body; the lead accepted them (`nadella/facets/ADJUDICATION.md` §3).
