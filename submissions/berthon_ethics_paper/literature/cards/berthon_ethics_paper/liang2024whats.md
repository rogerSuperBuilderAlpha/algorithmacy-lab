---
citekey: liang2024whats
title: "What's documented in AI? Systematic Analysis of 32K AI Model Cards"
authors: Liang, Weixin; Rajani, Nazneen; Yang, Xinyu; Ozoani, Ezinwanne; Wu, Eric; Chen, Yiqun; Smith, Daniel Scott; Zou, James
year: 2024
type: article
doi: 10.1038/s42256-024-00857-z
venue: Nature Machine Intelligence 6, 744-753 (published as "Systematic analysis of 32,111 AI model cards characterizes documentation practice in AI"); arXiv 2402.05160 read
source_basis: partial-text
pages_read: "arXiv 2402.05160 version, pp. 1-3 (abstract, introduction, section-completion results)"
source_url: https://arxiv.org/pdf/2402.05160
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/nadella/R5/liang2024/liang2024_arxiv.pdf
sha256: e7a5f40a2e3de5d4344a9422402cbb56709bf4e846d65f8319dbd6f6b1e98d5a
manuscript_lines: [521, 522, 523]
ledger_rows: [D03]
premises: [A5, CB]
facet: R5
supersedes: null
anthropic_authored: false
verified: pending
written: 2026-10-24
---

## Summary
The largest audit of model cards in practice: 32,111 cards on Hugging Face (of 74,970 models). More than half the
models have no card; where cards exist, the Training section is filled in 74.3 percent of them and the Limitations
section in 17.4 percent, Evaluation in 15.4 percent. The study is the empirical record for ledger row D03's remark
that "a model card declares but binds no one": the declaration itself is mostly about how the model was built, not
what it may do or where it fails. The version of record (NMI) is closed; the arXiv preprint was read. Verified:
Crossref 10.1038/s42256-024-00857-z; OpenAlex lists the NMI title.

## Key facts it relies on
- Abstract (arXiv p. 1): "environmental impact, limitations, and evaluation exhibit the lowest filled-out rates, while
  the training section is the most".
- Introduction (arXiv p. 2): "significant gaps persist in the completeness and quality of the provided documentation,
  with more than half of the models lacking a model card."
- Results (arXiv p. 3): "Across all the model cards, Environmental Impact (2.0%, or 639 out of 32,111 model cards),
  Citation (14.4%), Evaluation (15.4%), and Limitations (17.4%) sections exhibit the lowest filled-out rates, while the
  Training section (74.3%) is most frequently filled out".

## Critical notes from the literature
- The cards studied are voluntary, community-written documents on a model hub; the Agent Control Specification and the
  Responsible AI Standard (N1) are a different genre (enterprise-facing, with a reviewing team). The finding transfers
  as a warning about declaration without a party who checks it, not as a measurement of Microsoft's documents.

## Where the argument uses it
- **D03 (draft lines 521-523).** The duty asks for an envelope "stated as outcomes and known to both sides". The
  nearest existing instrument, the model card, is in practice a description of inputs, with limits declared in fewer
  than one card in five. Verdict: D03 **holds** as a duty; its claim to a "working precedent" rests on AP2 alone
  (`google2026agentic`, `parikh2025powering`), since the model card is a failed precedent for the declaring half.

## Verifier notes
