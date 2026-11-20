---
citekey: openai2025gpt
title: gpt-oss-120b model card (README of the Hugging Face repository openai/gpt-oss-120b)
authors: {OpenAI}
year: 2025
type: documentation
doi: null
venue: Hugging Face model repository openai/gpt-oss-120b (repository created 4 August 2025, last modified 26 August 2025 per the Hugging Face API)
source_basis: partial-text
pages_read: "README sections: introduction, Highlights (bullet list), Reasoning levels; not read: inference and fine-tuning instructions"
source_url: https://huggingface.co/openai/gpt-oss-120b/raw/main/README.md
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/R2/hf_gptoss/README.md
sha256: 92b0408cf5dce04e4c5e4e5f2be0361da710d3650baefd7d7519badd1c687919
manuscript_lines: [350-356, 402-408]
ledger_rows: [E13]
premises: [A4]
facet: R2
anthropic_authored: false
verified: pending
written: 2026-10-24
---

## Summary
OpenAI's model card for its open-weight gpt-oss models states that they give "Full chain-of-thought: Gain complete access to the model’s reasoning process" and, in the same bullet, that the chain of thought is "not intended to be shown to end users". The card matters for A4 because the draft (ll. 351-356) reasons from OpenAI's and Anthropic's API documentation to the claim that "In the products, nobody outside the supplier receives" the chain of thought. OpenAI's own open-weight release hands the raw reasoning to any deployer who runs the weights, and addresses it to developers rather than to the people the model's outputs reach. Fetched 2026-10-24 from the raw README on the main branch; openai.com itself (the announcement page) was not fetched (known 403 to scripted requests, N1 row 14).

## Key facts it relies on
- Introduction: "Welcome to the gpt-oss series, OpenAI’s open-weight models designed for powerful reasoning, agentic tasks, and versatile developer use cases."
- Highlights: "**Full chain-of-thought:** Gain complete access to the model’s reasoning process, facilitating easier debugging and increased trust in outputs. It’s not intended to be shown to end users."
- Highlights: "**Configurable reasoning effort:** Easily adjust the reasoning effort (low, medium, high) based on your specific use case and latency needs."
- Reasoning levels: "The reasoning level can be set in the system prompts, e.g., "Reasoning: high"."
- Hugging Face API record (not in the README; retrieved 2026-10-24): createdAt 2025-08-04, lastModified 2025-08-26, author openai.

## Critical notes from the literature
- A model card on a hosting site, not a paper; the OpenAI announcement and the gpt-oss model card PDF were not opened. The README's claim of full chain-of-thought access is a statement of what the weights emit, verifiable by anyone running them.
- Microsoft's Foundry documentation (`microsoft2026tutorial`) shows the same for DeepSeek models on Microsoft's platform.

## Where the argument uses it
- A4 ("reasoning disclosed to no one outside the supplier"; draft ll. 351-356): **narrower**. The claim holds for the closed frontier APIs the draft cites (OpenAI's hosted reasoning models, Anthropic by default, Google's summaries). It fails for open-weight models from the same supplier. The surviving claim: where raw reasoning is available, the supplier addresses it to developers and states that it is "not intended to be shown to end users"; the person acted on is outside its intended audience by design.
- P9 (Nadella's "non-negotiable" CoT transparency): an enterprise can have it with open-weight models, including on Microsoft's own platform; the draft's statement that nobody outside the supplier receives it should be confined to hosted closed models.

## Verifier notes
