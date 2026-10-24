# Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). *Training large language models to reason in a continuous latent space* (arXiv:2412.06769). arXiv preprint.

**Identifier:** arXiv:2412.06769 · **Read depth:** full_text (arXiv v4, 23 Aug 2026, "Last updated: August 25, 2026", 18 pp.; this is not the December 2024 text that Korbak et al. cite, since it discusses 2025 follow-up work on p. 3; pagination is the PDF's. Body, pp. 1–11, and appendices A–C, pp. 12–18, read; example prompts in Appendix A skimmed) · **Source-tier:** preprint · **Evidence basis:** direct_read · **Design and sample:** training experiments on GPT-2 with three benchmarks (GSM8k, ProntoQA, and the authors' own ProsQA), plus Llama 3.2-3B and Llama 3-8B on GSM8k; no human participants · **Parties modeled:** none (a model-architecture paper) · **Facets:** G · **Read:** 2026-10-13

## What it argues
Hao et al. propose "Coconut" (Chain of Continuous Thought). Instead of writing each reasoning step as word tokens, the model feeds its last hidden state back in as the next input, so its reasoning stays in a continuous vector space. The motivation is that "language space may not always be optimal for reasoning" (abstract, p. 1). They train it with a curriculum that replaces language reasoning steps with latent ones, one stage at a time (§3, p. 4).

Results (Table 1, p. 9; GPT-2). On GSM8k (grade-school maths) language chain of thought scores 42.9% and Coconut 34.1%, against 16.5% with no chain of thought. On ProntoQA, Coconut 99.8% against 98.8% for chain of thought. On ProsQA, a graph-search set the authors built, Coconut 97.0% against 77.5%, using 14.2 against 49.4 generated tokens. Without the curriculum Coconut falls to 14.4%, 52.4% and 76.1% on the three sets, so "the LLM still needs guidance to learn latent reasoning" (§5.3, p. 11). The authors conclude that Coconut "does not surpass CoT on GSM8k" but "offers a superior trade-off between reasoning efficiency and accuracy" (p. 10).

A headline claim is about what the latent thoughts do: "the continuous thought can encode multiple alternative next reasoning steps" (abstract, p. 1). Probing the model by forcing it to emit language after a given latent step shows probability spread over several candidate nodes before it narrows, which the authors read as a breadth-first search (§4.3, pp. 6–8). The probe works because the model can still compute a word distribution from a latent state "for probing purposes", even though "the latent thought is not intended to be mapped back to language space" (p. 4).

The larger-model check is thin. On GSM8k, Llama 3.2-3B gets 31.7% with Coconut against 26.0% with no chain of thought, and Llama 3-8B gets 43.6% against 42.2% (Table 5, p. 17). The table has no language chain-of-thought column. The authors say the paper's "primary goal" is "to highlight the promising attributes of latent-space reasoning" (p. 18).

## Relation to the argument
The paper has no safety content: it does not mention monitoring, oversight or readability as a concern, and it never uses the word "neuralese". Its only human-facing element is that latent states can sometimes be decoded into tokens (Figure 9, p. 10). So it cannot be cited for any claim about oversight. What it does is show that a model can be trained to reason through a channel a person cannot read, at small scale (GPT-2) and on synthetic and arithmetic tasks.

That matters for the Nadella post and for ruling D4. The post's P9 uses "neuralese" without a source. Korbak et al. cite this paper, with Geiping et al. (2025), as an architecture by which chain-of-thought monitoring could be lost. Where ruling D4 has the author read the post as an argument against neuralese, this is the technical paper behind the word, and it supports only that such models are being built and can work at small scale, not that frontier labs deploy them. On whether a text trace is a reliable thing for a person to read, see `lanham2023measuring` and `jia2026faithfulness`.

Facet check: Facet G's summary (train models to reason in a continuous latent space) is accurate. The body adds that Coconut trails language chain of thought on GSM8k (34.1% against 42.9%), which an abstract-only reading would miss.

## In conversation with
Cited and in the bib: `turpin2023language` (as "Turpin et al., 2024", p. 3) for the point that a model's chain of thought may not reflect the computation it actually runs. Cited by: `korbak2025chain` (pp. 5–6, as a latent-reasoning architecture that "naturally limit[s] our visibility"). It cites Fedorenko et al. (2024) and neuroimaging work on the language network (p. 1) to argue that language is "optimized for communication rather than reasoning"; none of that is in the bib.
Leads: Deng et al. (2024), arXiv:2405.14838 (internalized chain of thought); Geiping et al. (2025), arXiv:2502.05171 (recurrent-depth latent reasoning); Goyal et al. (2023) on pause tokens; Zhu et al. (2025) on the superposition account of Coconut.

## Caution
Small models, narrow tasks and no evaluation of interpretability or oversight. Do not cite it for the performance of frontier reasoning models or for any claim that reasoning in vectors is a safety problem; that is Korbak et al.'s inference, not this paper's. Cite the arXiv version number with any quotation.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened cards/hao2024training.pdf (arXiv 2412.06769v4, 23 Aug 2026, 18 pp.). Checked the 8 in-source quotations by exact match, every Table 1 number (all three datasets, CoT, No-CoT, Coconut and the w/o-curriculum row; p. 9) and Table 5 (p. 17), the page locators 1, 3, 4, 9-11, 17-18, the Turpin and Fedorenko citations, and that the word 'neuralese' and any monitoring/oversight/safety language are absent from the source (zero hits).

**Findings:** No issues found. The unmatched strings ('neuralese', 'naturally limit', 'our visibility') are quotations of the post and of Korbak et al., which are outside this source, as the card says. The card's statements about Korbak et al. citing this paper were not checked here (other card).
