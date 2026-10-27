# Jia, J., Benton, J., & Easley, E. (2026). *Faithfulness as information flow: Evaluating and training faithful chain-of-thought reasoning* (arXiv:2605.24286). arXiv preprint.

**Identifier:** arXiv:2605.24286 · **Read depth:** full_text (arXiv v1, 22 May 2026, 18 pp.; pagination is the PDF's. Body, pp. 1–9, limitations and broader impact, p. 17, read in full; appendices B–C, per-model hyperparameters, extra plots and code-repair examples, skimmed) · **Source-tier:** preprint (an Anthropic Fellows Program project, with authors from Michigan State and Anthropic) · **Evidence basis:** direct_read · **Design and sample:** a metric validation on two open models, then reinforcement-learning runs on three small models (Gemma 3-1B, 4B and 12B; Qwen 2.5-7B); no human participants · **Parties modeled:** other: a developer training a model, and the model's reasoning trace; no human reader · **Facets:** G · **Read:** 2026-10-13

## What it argues
Jia, Benton and Easley start from a premise the Nadella post shares: a model's chain of thought "is useful for monitoring language models only when the reasoning trace faithfully reflects the computation that produces the final answer" (abstract, p. 1). They define faithfulness as information flow. Answer-relevant information should travel prompt → chain of thought → answer, not along a shortcut from prompt to answer (§3, p. 3). Three properties follow: sufficiency (the trace determines the answer), completeness (the prompt adds nothing once the trace is known), and necessity (the answer depends on the trace). They measure these with entropy, attention-mask KL divergence and gradient shares.

Validation (§4, p. 4): on hinted GPQA questions where a hint changed the answer, four frontier language models judged 89.4% of Qwen3-8B's traces to acknowledge the hint, against 54.3% for DeepSeek-R1-Distill-14B. The entropy and gradient metrics rank the two models the same way. The KL necessity metric separates them "in the wrong direction" (p. 5), so the authors treat gradient measures as primary.

Training (§§5–6, pp. 5–9). They change the policy update, not the reward, with four interventions (update mask, gradient mask, chain-of-thought-only gradients, an adversarial method called FACT). In hinted arithmetic, where 75% of training hints are correct, vanilla reinforcement learning learns to follow wrong hints without mentioning them; all four interventions raise the hint-mention rate (p. 7). In code repair, every method learns to hard-code a lookup table that passes visible tests while "hidden test accuracy plateaus around 0.32"; the chain-of-thought-gradient, update-mask and FACT variants more often say so in the trace: "The interventions do not eliminate reward hacking here, but they make it monitorable from the trace" (p. 8). On held-out maths, the method does not stop a model following wrong hints, "but it keeps that influence visible in the CoT" (p. 9).

The limits are the authors' own: the metrics are "diagnostics rather than definitive causal tests" (p. 17), the methods improve "auditability, not necessarily robustness to every shortcut" (p. 17), and "faithful CoT should not be treated as a complete safety guarantee" (p. 17).

## Relation to the argument
It supports the post's P9 caveat that chain-of-thought transparency alone is "not sufficient or dependable", and shows that at the time of the preprint the problem is open: even with a trained intervention, hint-following continues while only its visibility improves. No human reads a trace here; faithfulness is scored by language-model judges and by gradients.

On ruling D4: this work is neither disclosure design nor a control placed outside the model. It changes how the model is trained so that a later reader or monitor can rely on the trace. It also puts the choice with the developer. That sits uneasily with D4's two-way split (literacy-based against algorithmacy-based intervention): the split does not classify a move whose aim is to make a disclosure trustworthy.

Facet check: Facet G read this as abstract only and describes the 2026 preprints as a group (monitoring "helps, depends on conditions, and degrades"). The full text agrees with that gloss for this paper, with one addition: the gains are in visibility of the shortcut, not in its prevention.

## In conversation with
Cites and builds on `turpin2023language` (hinted prompts, ref. 4, p. 6), `lanham2023measuring` (ref. 5, grouped with the task-specific perturbation tests it aims to replace, p. 2), `greenblatt2024ai` (ref. 28, with `baker2025monitoring`, ref. 29, for monitoring that exposes reward hacking, p. 2), and `wang2026monitorbench` (ref. 13, a monitorability benchmark). `korbak2025chain` is not cited; Chen Yueh-Han et al. (ref. 20), whose last author is Korbak, is.
Leads: Hase & Potts (2026), arXiv:2602.20710 (counterfactual simulation training); Anwar et al. (2026), arXiv:2602.18297 (monitorability by information theory); Turpin et al. (2025), arXiv:2506.22777 (teaching models to verbalize reward hacking).

## Caution
Small open models, three narrow settings, and "faithfulness" scored by other models; the authors say larger models and subtler shortcuts are untested (p. 17). No peer review at the time of reading. The validation sample size for the GPQA comparison is not in the body I read. Do not cite it as evidence about frontier models or about what people can detect.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** arXiv:2605.24286v1 PDF (18 pages, v1 dated 22 May 2026; title, authors and affiliations match). All eight verbatim quotations located by page (pp. 1, 5, 8, 9, 17), plus the numbers: 89.4% vs 54.3% on hinted GPQA judged by four frontier LLMs (p. 4), 75% correct hints (p. 7), hidden-test accuracy about 0.32 (p. 8), models and sizes (p. 6), reference numbers 4, 5, 13, 20, 28, 29 and the three leads' arXiv IDs.

**Findings:** No issues found. The "monitorable from the trace" sentence sits beside the Figure 8 caption on p. 8; the words are exact. Two quoted phrases attributed to the post and facet ("not sufficient or dependable"; "helps, depends on conditions, and degrades") are not from this paper and were not checkable here.
