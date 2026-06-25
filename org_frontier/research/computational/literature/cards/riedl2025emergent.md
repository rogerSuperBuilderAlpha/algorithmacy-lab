---
citekey: riedl2025emergent
title: Emergent Coordination in Multi-Agent Language Models
authors: Riedl, Christoph
year: 2025
doi: 10.48550/arXiv.2510.05174
arxiv: 2510.05174
journal: 
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2510.05174
sha256: e87be0141277bd3ef4e641a72b7ec2bd5c117b5539b23d6b88ae346db3585de3
pdf_path: literature/pdfs/riedl2025emergent.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks when multi-agent LLM systems are merely a collection of individual agents versus an integrated collective with higher-order structure. It introduces an information-theoretic framework, based on partial information decomposition (PID) of time-delayed mutual information (TDMI), to test in a purely data-driven way whether dynamical emergence is present, to localize it, and to distinguish performance-relevant cross-agent synergy from spurious temporal coupling. The framework is applied to LLM agents (GPT-4.1, Llama-3.1-8B, Llama-3.1-70B, Gemini 2.0 Flash, Qwen3) solving a "group binary search" guessing game without direct agent communication and with only group-level feedback, under three interventions: a Plain control, a Persona condition, and a theory-of-mind (ToM) condition ("think about what other agents might do"). Groups in the control condition show strong temporal synergy but little coordinated cross-agent alignment; assigning a persona introduces stable identity-linked differentiation; and combining personas with the ToM instruction produces identity-linked differentiation and goal-directed complementarity, operating as a dynamically stable, integrated unit. The authors conclude that multi-agent LLM systems can be steered with prompt design from mere aggregates into higher-order collectives, with results robust across emergence measures and entropy estimators and not explained by coordination-free baselines or temporal dynamics alone. The observed patterns mirror established principles of collective intelligence in human groups: effective performance requires both alignment on shared objectives and complementary contributions across members.

## Key facts it relies on
- The framework operationalizes emergence via partial information decomposition (PID) of time-delayed mutual information (TDMI), building on Rosas et al. (2020) and Mediano et al. (2022a); it implements three tests: an emergence capacity criterion, a practical criterion, and a coalition test (triplet extension).
- The emergence capacity test computes a two-source PID decomposing predictive information as I({X_i,t, X_j,t}; T_ij,t+ell) = UI_i + UI_j + Red_ij + Syn_ij, taking pairwise dynamical synergy Syn_ij > 0 as evidence; it is limited to detect synergy of order k = 2.
- The task is the "group binary search" guessing game developed by Goldstone et al. (2024), played without communication: agents propose integers whose sum must match a randomly generated hidden target, receiving only group-level feedback "too high" or "too low."
- Preliminary experiments used OpenAI gpt-4.1-2025-04-14, varying group size from 3 to 15 and temperature from [0,1] in steps of 0.1 (13 group sizes x 11 temperature settings x 50 groups = 7,150 experiments); each additional group member decreased odds of success by roughly 8% (OR = 0.92, p < 10^-16) and each unit increase in temperature increased odds of success by about 50% (OR = 1.50, p < 10^-7).
- Main experiments used groups of N = 10 at temperature T = 1 with GPT-4.1 (version 2025-04-14), replicating each group experiment 200 times per treatment condition (600 experiments total); overall success rate was not significantly different across the three interventions.
- For the practical emergence criterion, about 3.5% of experiments individually showed a p-value below 0.05; a joint Fisher test of all p-values was highly significant (below 10^-16), and bias-corrected estimates were above 0 in all conditions (Plain: p = 1.5 x 10^-16; Persona: p = 6.6 x 10^-7; ToM: p = 0.02).
- Time-trend demeaned bias-corrected triplet mutual information I_3 was around 0 in Plain (Wilcoxon p = 0.974) and Persona (p = 0.846), but the ToM condition showed significant positive mutual information (p = 3.5 x 10^-14); Total Stability was indistinguishable from zero in Plain (p = 0.976) and Persona (p = 0.858) but sharply increased under ToM (p = 2.9 x 10^-14).
- Regression analysis found higher levels of either synergy or redundancy alone do not predict success, but when both are present performance improves significantly (interaction beta = 0.24, p = 0.014); in marginal-effect terms redundancy amplifies the benefit of synergy by 27% and vice versa; causal mediation gives ACME = 0.034 [95%CI: -0.000 - 0.07], p = 0.053.
- The framework was repeated across four other models (Llama-3.1-8B, Llama-3.1-70B, Gemini 2.0 Flash, Qwen3); Llama 70B, Gemini, and Qwen3 achieved success rates on par with GPT-4.1, while the smaller Llama 8B largely failed to break oscillatory cycles, and Qwen3 exhibited a failure mode termed "paralysis under coordination ambiguity."

## Critical notes from the literature
- The authors state that evidence of higher-order synergy should not be interpreted as implying sophisticated cognition or consciousness; synergy is treated as a structural property of part-whole relationships, and they do not attribute human-like cognition to the agents.
- A footnote clarifies the paper explores conditional, cross-agent synergy (coordinated differentiation given the multi-agent constraint) and does not attempt to establish team-over-solo superiority on this task.
- Limitations acknowledged: the work focuses on developing/characterizing/localizing emergence; linking synergy and redundancy to performance is challenging because they are often co-dependent, and reaching only marginal significance (ACME p = 0.053) in the causal mediation; results rest on a single task; and the information-theoretic measures are limited to dynamic emergence on order k = 2, which is bound to miss higher-order synergy.
- The paper notes the small-data setting makes finite-sample entropy estimation challenging (bias grows with more bins, dimensionality, and small N), motivating multiple bias-correction steps (Williams-Beer I_min PID, order k=2 instead of n, quantile binning, Jeffreys prior, Miller-Madow estimator, MMI redundancy).

## Key topics covered
Multi-agent LLM systems; emergent coordination; collective intelligence; partial information decomposition (PID); time-delayed mutual information (TDMI); dynamical emergence; synergy and redundancy; role specialization and agent differentiation; theory-of-mind (ToM) prompting; personas; group binary search guessing task; hierarchical/mixed modeling; falsification tests and surrogate null distributions; Total Stability / Lyapunov stability proxy; coalition test and triadic information gain; causal mediation analysis; cross-model generalization (GPT-4.1, Llama, Gemini, Qwen3); reasoning failure modes in multi-agent systems.
