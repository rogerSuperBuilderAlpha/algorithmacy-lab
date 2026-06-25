---
citekey: poppel2022resonating
title: Resonating Minds---Emergent Collaboration Through Hierarchical Active Inference
authors: P{\"o}ppel, Jan and Kahl, Sebastian and Kopp, Stefan
year: 2022
doi: 10.1007/s12559-021-09960-4
arxiv: null
journal: Cognitive Computation
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.1007/s12559-021-09960-4.pdf
sha256: 13cd382857d090beb832f5f740345212a3cbbc958add06653936eeb4c35c9aa7
pdf_path: literature/pdfs/poppel2022resonating.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether successful collaboration between artificial agents on complex situated tasks can emerge from minimal, distributed on-the-fly coordination rather than explicit joint planning. The authors propose HAICA (Hierarchical Active Inference for Collaborative Agents), a model that combines a predictive-processing/active-inference perception-action hierarchy (a goal layer and an intention layer, updated via Kalman-filter belief integration of top-down predictions and bottom-up evidence) with a lightweight Bayesian Theory of Mind (BToM) mentalizing module. The key mechanism, called "belief resonance," lets the inferred mental states (goals/intentions) of one agent influence another agent's own predictive beliefs, with the influence modulated by a susceptibility parameter (SP) realized as a Kalman gain. They implement and evaluate the model in the Overcooked domain (two agents preparing meal orders across five kitchen layouts), and in a second salad version replicating Wu et al.'s Bayesian Delegation setup. Results show HAICA achieves team performance comparable to a state-of-the-art deep RL approach (and better in the asymmetric layout), while being far cheaper computationally; belief resonance is especially beneficial when agents have asymmetric task knowledge (only one agent knows the orders), enabling an emergent leader-follower dynamic. The authors frame HAICA as a minimal "cognitive infrastructure" building block rather than a general solution, since it does not reach optimal-policy performance.

## Key facts it relies on
- HAICA uses two predictive layers for the Overcooked domain: a goal layer (which order to work on, e.g. Onion or Tomato soup) and an intention layer (high-level actions like picking up items); belief updates integrate top-down predictions and bottom-up evidence via Kalman filters, with prediction/evidence Kalman gains Kp and Ke both set to 0.5.
- Belief resonance is a two-step update (Eqs. 9-10): the inferred other-agent belief Qt is first integrated with the top-down prediction using a susceptibility-parameter Kalman gain K^SP, then validated against the agent's own bottom-up evidence; SP=0 reduces the model to the non-resonating baseline.
- The mentalizing module is a "satisficing" BToM approximation that sets the action likelihood P(a|i,g,o)=alpha if a equals the action the agent itself would take, avoiding full inverse planning; a softmax with parameter beta and additive noise mu is applied to keep beliefs responsive.
- Meta-parameters used: alpha=0.9 (ToM action likelihood), beta=2 (ToM softmax), mu=0.1 (ToM noise), Ke=Kp=0.5; the wait intention has a fixed pre-normalization likelihood of 1/|intention| (approx 0.08).
- Evaluation averaged team rewards over 20 episodes of 400 time steps each; rewards were 20 points for Onion soup and 15 for Tomato soup, corresponding to their cooking times; SP combinations were tested from 0 to 1 in 0.1 increments.
- In the soup domain with both agents knowing orders and SP=0, scores ranged from 123.75 (+/-4.75) in cramped to 268.5 (+/-3.55) in asymmetric; optimal SP combinations gave only marginal gains (asymmetric to 270.5 with SP 0 and 0.2; spacey to 136.75 with SP 0.1 for both).
- When only one agent knew the orders, team performance dropped at SP=0 but recovered with optimal SP combinations (typically a "leader" with SP <= 0.1 and a "follower" with SP up to 0.9), close to the both-informed level for most layouts except forced.
- In the salad domain vs. Bayesian Delegation (BD), aggregated across 9 scenarios (20 seeds each): HAICA (opt. SPs) reached 0.89 +/- 0.02 success vs BD-default 0.92 +/- 0.02; HAICA completed an episode in ~1.32-1.54 s and ~0.02 s per step, whereas BD-default took 2111.55 +/- 133.85 s per episode and 55.87 +/- 3.33 s per step (each BD agent ~28 s per action vs ~0.01 s for HAICA).
- HAICA performance is comparable to (marginally worse than) the deep RL population-based-training agents of Carroll et al. [11] in cramped, ring and forced, and significantly better in asymmetric (because HAICA uses both pots); but it does not reach the optimal coupled-planning (CP) scores.

## Critical notes from the literature
- The authors explicitly state HAICA is not designed to find optimal collaborative actions and is "not a general solution"; it is worse than optimal joint policies (BD / coupled planning) and is only meant as a minimal building block to be complemented by richer inference/planning.
- The low-level action planner (A* / best-first search) does not consider the other agent's future actions, causing agents to block each other or get "stuck" cycling (picking up/placing items) in the salad domain; a heuristic "punishment of aborted/repetitive intentions" was needed as a partial fix rather than principled coordination.
- Fixed high SP values for both agents degrade performance (in the worst case completing no orders), since agents overwrite their own goals each step; the authors argue this shows a need for dynamic, adaptive SP and complementary leader-follower roles, which they leave to future work.
- The model was only tested with two agents and with hand-specified intention likelihoods that "implicitly encode the agent's recipe knowledge" (deterministic inter-layer likelihoods assume each agent knows the steps for each order); scaling to multiple agents would require attention mechanisms to select whom to resonate with.
- Comparisons carry caveats the authors flag: the RL comparison [11] used a simpler single-order (Onion only) task averaged over 5 seeds (vs HAICA's 20), and the cramped layout differs slightly; in the single-order RL setting HAICA could only exercise mentalizing/resonance at the intention layer.

## Key topics covered
Hierarchical active inference; predictive processing; free-energy minimization; belief resonance; susceptibility parameter (leader-follower roles); Bayesian Theory of Mind (satisficing approximation); Kalman-filter belief integration; emergent / on-the-fly multi-agent coordination; Overcooked domain; comparison vs deep RL (population-based training) and Bayesian Delegation; runtime/computational efficiency; HPBU (Hierarchical Predictive Belief Update) lineage.
