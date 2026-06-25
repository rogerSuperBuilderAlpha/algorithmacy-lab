---
citekey: tajik2026disagreement
title: Disagreement as Data: Reasoning Trace Analytics in Multi-Agent Systems
authors: Tajik, Elham and others
year: 2026
doi: 10.1145/3785022.3785101
arxiv: null
journal: 
programs: [qualitative]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2601.12618
sha256: c5090a149a89331650d46248906829c67313a3b4a73c628eaf194f8944c89946
pdf_path: literature/pdfs/tajik2026disagreement.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how disagreements among LLM agents performing qualitative coding can be systematically detected and used as analytic signals (RQ1), and what patterns in agent disagreement reasoning reveal hidden interpretive uncertainty (RQ2). The authors run a multi-agent system (two "discussion" agents plus a consensus agent, built on DeepSeek-R1-32B) over 3,538 tutor-student dialogue segments from high-dosage Algebra I tutoring, coding each segment against an eight-category hybrid human-AI codebook. They embed each agent's reasoning trace with BERT and compute pairwise cosine similarity (CS) between Agent 1 and Agent 2, comparing this continuous reasoning-similarity signal to categorical code agreement. Across 9,746 agent-agent pairs, CS shows a moderate positive correlation with label agreement (rho = .54), and agreement pairs have significantly higher reasoning similarity than disagreement pairs (Welch's t(9746) = 60.33, p < .001, Cohen's d = 1.16). The metric is robust across temperature settings (0, 0.5, 1) and its per-code spread mirrors prior human inter-coder reliability (kappa) on the same dataset. Qualitative review of sampled disagreement cases shows single code labels encompass diverse instructional sub-functions (within-code misalignment) and that some codebook boundaries are fuzzy/overlapping (between-code alignment), so the authors argue disagreement is a meaningful signal for prioritizing human review and refining codebooks rather than noise to discard.

## Key facts it relies on
- Dataset: 3,538 tutor-student dialogue segments extracted from three distinct 60-minute virtual tutoring sessions with 9th-grade Algebra I students in high-poverty urban northeastern US schools (2022-2023), originating from Barany et al. [4]; each segment treated as an independent data point.
- Codebook: a hybrid human-AI codebook (from Barany et al. [4]) with eight binary categories: Greeting, Instruction, Guiding Feedback, Aligning to Prior Knowledge, Understanding/Engagement-Tutor, Technical or Logistics, Encouragement, Time Management.
- Multi-agent system: a Dual-Agent Discussion module (two agents with distinct personalities, e.g., bold vs. empathetic, who independently code in Round 1 and critique/revise in Round 2 if no consensus) plus a neutral Consensus Agent; built on Borchers et al. [7] and using DeepSeek-R1-32B [15], chosen because it outputs reasoning traces and activates ~37 billion parameters per token.
- Method: reasoning traces parsed from `<think>...</think>` sections, embedded with BERT (averaging token embeddings; sequences truncated at BERT's 512-token limit), then compared via pairwise Cosine Similarity between Agent 1 and Agent 2.
- Main RQ1 result: across 9,746 agent-agent pairs, CS correlated with binary label agreement at rho = .54 (95% CI [.52, .55], p < .001).
- Statistical validation: agreement pairs (M = 0.957, SD = 0.025) had significantly higher reasoning similarity than disagreement pairs (M = 0.904, SD = 0.058); Welch's t(9746) = 60.33, p < .001, Cohen's d = 1.16 (large effect).
- Agreement decomposition (Table 1): within-align 47.0% (N=4598, mean cosine 0.965), between-misalign 28.0% (N=2680, 0.863), within-misalign 23.0% (N=2193, 0.916), between-align 3.0% (N=275, 0.954).
- Robustness: similarity patterns hold across temperature settings 0, 0.5, 1; agreement pairs cluster ~0.95-0.97 and disagreement pairs stay lower (~0.87-0.92) with median values stable across temperatures.
- CS spread mirrors prior human kappa on the same dataset [4]: tightly concentrated CS for high-reliability codes (Greeting kappa = 0.85, Encouragement kappa = 0.80) vs. flatter CS for lower-reliability codes (Aligning to Prior Knowledge kappa = 0.66, Checking Understanding/Engagement kappa = 0.60, Instruction kappa = 0.66, Guiding Feedback kappa = 0.66).
- Qualitative sampling: 120 within-code misalignment cases (15 from each of 8 categories, CS 0.55-0.78) and 45 between-code alignment cases (CS 0.95-0.99), reviewed by two coders under double-blind conditions; Understanding/Engagement and Technical/Logistical Issues were dropped as not surfacing pedagogical points.

## Critical notes from the literature
- The authors explicitly caution (citing Kambhampati et al. [17]) that reasoning traces should not be mistaken for genuine human-like reasoning or authentic cognition; they treat traces as structured textual artifacts, not evidence of epistemic transparency, given LLMs' probabilistic pattern-matching nature.
- Stated limitations: evaluation on a single learner-tutor dialogue dataset and single coding schema limits generalizability; only a modest number of disagreement cases were qualitatively sampled; agent rationales were not systematically compared against codebook definitions.
- The MAS processes one dialogue segment at a time, which the authors note risks ambiguity from limited conversational context and may itself contribute to divergent codings; they suggest multi-turn or session-level context as future work.
- The correlation between CS and label agreement is only moderate (rho = .54), and key exception categories (within-code misalignment, between-code alignment) show that reasoning similarity and label agreement can diverge; the authors frame the method as requiring structured human oversight, not standalone evidence.
- Integrating disagreement signals into practical human-AI workflows and tooling remains future work; the validity claims rest on alignment with prior human reliability metrics rather than an independent accuracy gold standard in this study.

## Key topics covered
Multi-agent LLM systems; reasoning traces as process data; qualitative/deductive coding; cosine similarity on BERT sentence embeddings; inter-rater reliability (kappa); disagreement as analytic signal; within-/between-code agreement and alignment taxonomy; DeepSeek-R1-32B; codebook refinement; human-AI collaborative analysis in learning analytics; tutoring dialogue annotation; temperature robustness.
