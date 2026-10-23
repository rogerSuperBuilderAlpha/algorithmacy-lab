# chen2026cua: Comparing Human Oversight Strategies for Computer-Use Agents
Full citation: Chen, C., Zhang, Z., Chen, Z., Xu, E., Yang, Y., Khalilov, I., Gebreegziabher, S. A., Ye, Y., Xiao, Z., Yao, Y., Li, T., & Li, T. J.-J. (2026). arXiv:2604.04918v2 [cs.HC], 12 Sep 2026. PREPRINT — venue placeholder "Conference'17", no DOI. | Read: full text body (pp. 1–9, §1–§7); appendices not read.

Question: How do four oversight strategies for LLM computer-use agents (Action Confirmation, Risk-Gated, Supervisory Co-Execution, Structurally Enriched) shape experience, occurrence of problematic actions, and intervention? (§4, RQ1–3)

Claim: Strategy changed whether problematic actions occurred, not whether users caught them; failures came from mistimed authority, judging procedural correctness rather than content appropriateness, and plan approval reducing runtime scrutiny (Abstract; §5).

Method: within-subjects, N = 48 (Prolific), 192 live sessions on researcher-built sites, each with one embedded problematic action (privacy leakage, prompt injection, dark pattern) (§4.1–4.2; Table 1). Gemini 3.1 Flash-Lite agent (§3.4). GEE for binary outcomes; two coders, κ = 0.92 on 192 episodes (§4.2.5). Follow-up interviews n = 10 (§4.3).

Key results:
- Users blocked 29 of 138 problematic actions that reached execution (21%), no reliable difference across strategies (§1 contributions; Table 3: intervention χ²(3) = 3.17, p = .366).
- Plan-based strategies cut odds of occurrence by 76%, OR = 0.24, 95% CI [0.14, 0.42] (§1; §5.2).
- Of 109 failure episodes, 61 (56.0%) had a timing mismatch: risk emerged before or without a decision point (§5.2.1).
- 74 of 109 (67.9%) failures showed little observable deliberation at the decision point (§5.2.1).
- A risk cue was present in 100 of 109 failures (91.7%) (§5.2.2).
- Coins "judgment alignment": temporal, interpretive, scope (§6.2).

Stated limitations: context confounded with risk type; intervention conditional on occurrence; fictional profile; no autonomous baseline (§6.5).
My concerns (mine): preprint, not yet peer reviewed; no eye tracking — attention inferred from video coding and interviews.

Quotes, verbatim:
- "oversight depends less on maximizing control than on aligning authority, timing, and attention with decision-critical moments." (Abstract)
- "Effective oversight should therefore trigger judgment before a consequential transition when possible" (§6.2)

Cited by me for: the decision-space proposal — strongest recent evidence that WHERE in a stream human judgment is requested matters more than how often. Directly supports placing breaks at decision units rather than arbitrary points.
