---
citekey: microsoft2026tutorial
title: "Tutorial: Get started with a DeepSeek reasoning model in Microsoft Foundry Models (classic)"
authors: {Microsoft}
year: 2026
type: documentation
doi: null
venue: Microsoft Learn (ms.date 2026-07-28)
source_basis: partial-text
pages_read: "introduction; expected output of the first request; the Python parsing example; section About reasoning models (Reasoning completions, Output completions, Reasoning content). Not read: deployment steps, SDK setup, other-language samples"
source_url: https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/tutorials/get-started-deepseek-r1
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/R2/ms_foundry_r1/page.html
sha256: e1c53b4b84e01bc994c7fbe657c9eb44c836df93a48c7c12869c055f0b24e317
manuscript_lines: [350-356, 402-408]
ledger_rows: [E13, E14]
premises: [A4]
facet: R2
anthropic_authored: false
verified: pending
written: 2026-10-24
---

## Summary
Microsoft's own tutorial for DeepSeek reasoning models on Foundry (the URL still names R1; the page now illustrates with DeepSeek-V4-Pro) tells the deployer that the response "contains content wrapped in <think>...</think> tags followed by the final answer" and shows how to parse the reasoning out of `message.content`. The page contrasts this with OpenAI's o1, which "output only the completions". For the paper, this is Microsoft, the author of the insider-risk post, delivering a model's raw reasoning to the deploying organisation through its own platform. It does not deliver it to anyone the deployer's application acts on. Fetched 2026-10-24; page text extracted locally.

## Key facts it relies on
- Introduction: "In this tutorial, you deploy the DeepSeek-V4-Pro reasoning model, send inference requests programmatically using code, and parse the reasoning output to understand how the model arrives at its answers."
- Expected output: "A JSON response containing the model's answer, reasoning process (within <think> tags), token usage statistics (prompt tokens, completion tokens, total tokens), and model information."
- "If the model generates reasoning, the response contains content wrapped in <think>...</think> tags followed by the final answer."
- About reasoning models: "Reasoning models produce two types of content as outputs: Reasoning completions; Output completions ... Some models, like DeepSeek-V4-Pro, might respond with the reasoning content. Others, like o1, output only the completions."
- Reasoning content: "Some reasoning models, like DeepSeek-V4-Pro, generate completions and include the reasoning behind them. The reasoning associated with the completion is included in the response's content within the tags <think> and </think>. The model can select the scenarios for which to generate reasoning content."
- Metadata: `ms.date` 2026-07-28.

## Critical notes from the literature
- The page is a tutorial for a "classic" portal; whether the newer Foundry portal returns reasoning the same way was not checked. The faithfulness literature (`chen2025reasoning`, `korbak2025chain`, dxd cards) warns that visible reasoning need not be faithful; Nadella's P9 says the same.
- "The model can select the scenarios for which to generate reasoning content": the supplier of the weights, not the deployer, decides when reasoning appears.

## Where the argument uses it
- A4 (draft ll. 351-356, "In the products, nobody outside the supplier receives it"): **narrower**. Microsoft's platform returns raw reasoning for DeepSeek models to the deploying organisation. The claim survives as: no hosted closed frontier API returns it by default, and no product read returns it to the person acted on.
- E14 (Microsoft's practice): the firm whose chief executive calls CoT transparency "a non-negotiable" (P9) already ships it for third-party open-weight models; the gap the paper describes is between the deployer, who may receive it, and the second party, who does not.

## Verifier notes
