# Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., … Perez, E. (2023). *Measuring faithfulness in chain-of-thought reasoning* (arXiv:2307.13702). Anthropic.

**Identifier:** arXiv:2307.13702 · **Read depth:** full_text (arXiv v1, 17 Jul 2023, 14 pp.; pagination is the PDF's. Body, pp. 1–10, read in full; the appendices of prompts and extra plots, pp. 12–14, skimmed) · **Source-tier:** preprint (lab technical report, authors at Anthropic apart from J. Brauner at Oxford) · **Evidence basis:** direct_read · **Design and sample:** four intervention tests on chain-of-thought (CoT) traces, 8 multiple-choice tasks, 100 CoT samples per question, a 175B-parameter RLHF-trained assistant model; a model-size sweep (810M to 175B parameters) on the same tasks and on synthetic addition; no human participants · **Parties modeled:** none (model-internal; no person reads the traces) · **Facets:** G · **Read:** 2026-10-13

## What it argues
Lanham et al. ask whether the reasoning a model writes before an answer is the reasoning that produces the answer. They cannot see the model's real computation, which they name as the key limitation: "we do not have a separate way by which to understand the model's real internal reasoning process, without which we cannot know if the chain of thought is faithful to that reasoning process" (§5, p. 9). So they test four ways a trace could be unfaithful, each "not meant to be conclusive evidence for CoT being faithful, but rather aims to rule out the possibility of one class of faithfulness failures" (p. 2).

The tests (§2, pp. 3–6). Early answering truncates the trace and checks whether the answer changes; adding mistakes inserts an error and checks the same; filler tokens replace the trace with dots; paraphrasing rewords it. If cutting or corrupting the trace rarely moves the answer, the reasoning is probably post hoc. Results:

- Post-hoc reasoning varies widely across tasks. On the early-answering score (area over the curve, higher = less post hoc), AQuA is 0.44 and LogiQA 0.26, down to ARC (Easy) at 0.02 (Table 2, p. 5). On the three lowest tasks the trace changes the answer less than 10% of the time; on AQuA more than 60% (p. 4). The score does not track the accuracy gain from CoT: LogiQA's gain is 1.02 points but it ranks second in AOC (p. 4), and HellaSwag loses 4.69 points with CoT (Table 2).
- Filler tokens give no accuracy gain, and paraphrasing leaves accuracy about the same, so extra computation and phrasing-coded information do not explain CoT's benefit (§§2.5–2.6, pp. 6–7).
- Faithfulness shrinks with scale. "As models become larger and more capable, they produce less faithful reasoning on most tasks we study" (abstract, p. 1). On 7 of 8 tasks the 13B model changes its answer after CoT more often than the 175B model (§3.1, p. 7). On addition, post-hoc reasoning rises with model size and with easier problems, so faithfulness falls (§3.2, p. 8).

For four of the eight tasks, the model size with the largest accuracy gain from CoT is also the size with the most faithful reasoning (App. C, p. 13). The authors' conclusion is hedged both ways: "CoT can be faithful if the circumstances such as the model size and task are carefully chosen" (abstract). They suggest choosing a less capable model when faithful reasoning matters, and they note the models were RLHF-trained and a pretrained model might behave differently (p. 9).

## Relation to the argument
It supports the post's P9 caveat that chain-of-thought transparency is not dependable on its own, and it supplies the finding that makes disclosing the reasoning a fragile remedy: how much the answer depends on the trace changes with task and model, and falls as models grow. In this sense it supports facet G's use of it.

It does not touch a human reader. Every test perturbs a trace and watches the model, so it says nothing about whether a person could use a trace to catch an error. For ruling D3 (disclosure as a literacy intervention), it shows that the object disclosed may not carry the information a reader assumes it does; for D4 (disclosure design as the post's only move) it gives a reason the post itself treats disclosure as insufficient.

Facet check: Facet G's quotation from the abstract is exact and its read status (abstract and introduction) understates what the body adds: the size result is per task, with 6 of 8 tasks peaking at 13B and AQuA and LogiQA the exceptions (p. 7), and the "less faithful" finding is for a multiple-choice setting with a fixed prompt format.

## In conversation with
Cites Turpin et al. (2023) as the adversarial counterpart: Turpin finds unfaithful traces in "adversarially constructed settings," while Lanham tests "non-adversarial settings" (§4, pp. 8–9); `turpin2023language` is in the bib. Cited by `korbak2025chain` (p. 5, as a causal-relevance test and a faithfulness proxy), `jia2026faithfulness` (ref. 5, a perturbation test it aims to replace). It thanks Ryan Greenblatt and Buck Shlegeris in its acknowledgements (p. 10), the authors of `greenblatt2024ai`.
Leads: Wei et al. (2022) on chain-of-thought prompting and its three explanatory hypotheses; Radhakrishnan et al. (2023) on question decomposition as a route to more faithful reasoning; Lyu et al. (2023), faithful chain of thought by program execution; Gao (2023) on Shapley attribution of CoT tokens.

## Caution
Multiple-choice benchmarks, one prompt format, and mostly one model family. The tests rule out particular failures and do not prove faithfulness; the 2023 models are far from the 2026 reasoning models that Korbak et al. discuss. Faithfulness here means dependence of the answer on the trace, not legibility to a person.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv v1 PDF (2307.13702, 14 pp.), extracted with pdftotext. I checked 8 verbatim quotations with pages, the Table 2 values (AQuA 0.44, LogiQA 0.26, ARC Easy 0.02, LogiQA gain 1.02, HellaSwag -4.69), the less-than-10% and more-than-60% figures, 7 of 8 tasks at 13B versus 175B, six of eight peaking at 13B, the App. C four-of-eight claim, the 175B RLHF model, 810M to 175B, and the acknowledgements.

**Findings:** One ambiguity fixed: on addition the card said 'the effect rises with model size and with easier problems'. The source (p. 8) says post-hoc reasoning rises with model size and with easier tasks (so faithfulness falls); I wrote that out. All other quotations and numbers match. I could not check from this source the two 'cited by' claims (korbak2025chain p. 5, jia2026faithfulness ref. 5), which depend on those other papers. The facet quotation is the facet's wording.
