---
citekey: zhang2024mutual
title: Mutual Theory of Mind in Human-AI Collaboration: An Empirical Study with LLM-driven AI Agents in a Real-time Shared Workspace Task
authors: Zhang, Shao and Yu, Xihuai and Chen, Keyang and Zhao, Junda and Zhang, Weinan and Wang, Ying
year: 2024
doi: null
arxiv: 2409.08811
journal: arXiv
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2409.08811
sha256: 3f73d37b1d9cc740633d7184b7762441cc2668eff6e7dc8d5cd4a3e586538f80
pdf_path: literature/pdfs/zhang2024mutual.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper studies the Mutual Theory of Mind (MToM) process in human-AI teams (HATs), where both a human and an AI agent reason about and attribute mental states to one another during real-time collaboration. The authors build a real LLM-driven agent (on GPT-4o mini) with Theory-of-Mind, Policy, and Communication modules, and embed it in a redesigned Overcooked-style burger-cooking shared-workspace task. Using a 4×2 mixed-design online experiment (n = 68 valid participants), they vary communication interactivity between groups (bidirectional, human-only, agent-only, no communication) and the agent's ToM capability within subjects. The main findings are that the agent's ToM capability does NOT significantly affect objective team performance, but it does increase the agent's contribution rate and strongly increases humans' feeling of being understood. Bidirectional communication yields the lowest team performance, and most participants found verbal communication burdensome and largely chose not to send messages, relying instead on the agent's actions (implicit/non-verbal communication) to infer its intentions. The authors conclude that in real-time shared-workspace tasks, non-verbal behavioral communication can be as effective as verbal communication for human-AI collaboration.

## Key facts it relies on
- The experiment was a 4×2 mixed design: 4 communication-interactivity levels (Bi-Comm, H-Comm [human-only], A-Comm [agent-only], No-Comm) as between-group variables, and agent ToM capability (w/ ToM vs. w/o ToM) as a within-subject variable; the within-subject ToM factor determines whether MToM exists.
- 80 participants were recruited; after excluding anomalous/passive/incomplete data, 68 valid participants remained (M = 46, F = 22, ages 18-34), distributed as Bi-Comm = 16, H-Comm = 17, A-Comm = 17, No-Comm = 18.
- Best team-performance means showed No-Comm highest and Bi-Comm lowest; e.g., No-Comm agent w/ ToM = 180.83 (SD 18.09) and w/o ToM = 177.22 (SD 25.62); Bi-Comm w/ ToM = 165.00 (SD 35.02) and w/o ToM = 163.75 (SD 26.17); within each group, ToM vs. no-ToM produced no significant difference in best performance.
- With MToM present (agent w/ ToM), the AI agent's contribution rate CR_A increased by 0.02 (p < 0.001, Cohen's d = 0.169) versus the no-ToM condition; communication interactivity had no significant effect on CR_A.
- For the statement "I feel the agent understands me," participants perceived the ToM agent understood them better (p < 0.001, Cohen's d = 0.336); for "I understand the agent" there was a significant main effect (p < 0.001) but only Cohen's d = 0.177 (below the small-effect threshold).
- The Bi-Comm group had a higher Failure Count than H-Comm, with an average increase of 0.77 (p < 0.01).
- In both Bi-Comm and H-Comm groups (where humans could send messages), the vast majority of participants sent fewer than one message on average; only one H-Comm participant sent many (>15 per game), and only one participant ever used a "Good Job" message.
- Most participants could distinguish the two agents (94% Bi-Comm, 94% H-Comm, 88% A-Comm, 77% No-Comm), and individual preferences were consistent across four preference questions (understands me better, I understand better, work better with, prefer).
- The agent is GPT-4o mini-driven with three modules: ToM (executes every 75 time-steps, outputs natural-language beliefs about the human), Policy (FSM-based initial policy + code-as-policy generator running every 25 time-steps + policy-reflection "Behavior Guideline" + A* path planning into atomic actions), and Communication (messages <10 words, runs every 25 time-steps). The task is formalized as a two-player DEC-MDP over 500 time-steps; rewards are +15 (LettuceBurger), +20 (BeefBurger), +25 (BeefLettuceBurger), -10 (wrong burger), -10 (missed order). Human communication uses 11 message templates.
- In a separate validation experiment (10 games each vs. a fixed rule-based teammate, 500 time-steps), the ToM agent averaged 136 (SD 25.77) vs. 115.5 (SD 30.04) without ToM, indicating the ToM module improves performance against a fixed partner.

## Critical notes from the literature
- The authors' own headline result is partly null: agent ToM did not significantly change objective team performance in the human study, even though it improved performance against a fixed rule-based teammate in validation — they attribute the human-study null to humans adapting and to the complexity of real-time interaction.
- Scope/sample limits: an online study with 68 valid participants drawn from a single university's internal platform, ~20-minute sessions, with three trials per agent; effect sizes for key perceptions are small (Cohen's d = 0.336 and 0.177), and the preference-vs-score trends (e.g., the opposite trend in A-Comm) were not statistically significant.
- Participants self-reported that sending messages increased workload and hurt performance, so the verbal-communication conditions are confounded by very low actual message usage; the "bidirectional communication is worse" finding is interpreted by the authors through this operational-burden lens rather than as a property of communication content.
- Findings are specific to a real-time, action-dependent shared-workspace (Overcooked-derived) setting where implicit action cues are rich; the authors caution that conclusions about non-verbal communication being as effective as verbal may not transfer to settings with less observable shared action.
- The agent's "ToM" is implemented as LLM-generated natural-language belief summaries about human behavior every 75 steps, not a validated cognitive ToM model; whether this constitutes genuine theory of mind is a framing the paper adopts rather than independently tests.

## Key topics covered
Mutual Theory of Mind (MToM); Theory of Mind in human-AI teams (HATs); LLM-driven AI agents; GPT-4o mini agent design; Overcooked / gym-cooking shared-workspace task; communication interactivity (bidirectional / unidirectional / none); verbal vs. non-verbal (implicit action) communication; mixed-design (4×2) HCI experiment; DEC-MDP formalization; code-as-policy and finite-state-machine policy; agent contribution rate, failure count, message count metrics; human perception and mental models of AI teammates; mixed-effects regression with bootstrapping and Bonferroni correction.
