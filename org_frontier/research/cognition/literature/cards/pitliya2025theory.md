---
citekey: pitliya2025theory
title: Theory of Mind Using Active Inference: A Framework for Multi-Agent Cooperation
authors: {Pitliya
year: 2025
doi: 10.48550/arXiv.2508.00401
arxiv: null
journal: arXiv preprint
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2508.00401
sha256: 98ef3545afb76562c541614fa7245fd1d3176ce361afc366d787c2146ae981e8
pdf_path: literature/pdfs/pitliya2025theory.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how active-inference agents can cooperate without the restrictive assumption, common to prior work, that all agents share identical generative models or communicate explicitly. The authors (from VERSES) implement Theory of Mind (ToM) inside the planning stage of active inference by having a "focal" agent maintain distinct belief representations for itself and for each other agent, and by extending the sophisticated-inference recursive expected-free-energy (EFE) tree search into a deep tree that alternates between the focal and other agent's policies and observations. Information about how another agent's anticipated action changes the world is integrated into the focal agent's beliefs via likelihood message passing, while perspective separation is preserved. The method is validated in a 3x3 grid on two tasks—collision avoidance (agents swap corners without colliding) and apple foraging (resource competition under partial observability)—each run in a baseline (both agents non-ToM) versus a ToM condition (one red ToM agent, one purple non-ToM agent). In collision avoidance the non-ToM agents both take the central shortest path and deadlock, whereas the ToM agent anticipates the other's path and takes a longer collision-free route. In foraging the non-ToM agents both converge on the known apple (only one succeeds), whereas the ToM agent explores an uncertain location so both agents end up consuming apples. The authors present this as the first generalisable ToM implementation for multi-agent cooperation in active inference, achieved without shared generative models, explicit communication, or pre-set strategies.

## Key facts it relies on
- The framework builds on sophisticated inference (Friston et al. 2021, Neural Computation 33(3):713–763), which extends standard active inference from "what would happen if I did that?" to the recursive "what would I believe about what would happen if I did that?".
- In a two-agent scenario the focal agent's state beliefs are s = {s^{f,self}, s^{f,world}, s^{o,self}, s^{o,world}}, separating its own self/world beliefs from its beliefs about the other agent's self states and about what the other agent believes about the world; this lets the model represent asymmetric knowledge.
- Planning is a deep tree search with five stages per horizon: (1) other-agent policy expansion, (2) focal-agent policy expansion (with likelihood message passing to update world beliefs from the other's anticipated action), (3) focal-agent observation expansion, (4) other-agent observation expansion, (5) backwards pass and policy selection; the other agent's policy probabilities are marginalised for the focal agent's policy selection.
- The ToM EFE (Eq. 2) is expressed over focal and other actions/observations (a^f, o^f, a^o, o^o); the focal utility uses the focal agent's preferences C^f, distinct from the other agent's preferences C^o used to compute the posterior over the other's actions.
- All simulations run on a 3x3 grid with deterministic dynamics and perfect observability of agent locations, using the JAX-based Python package pymdp (Heins et al. 2022); each task has a baseline condition (both agents non-ToM) and a ToM condition (one ToM agent = red, one non-ToM = purple).
- Collision-avoidance generative model: two state factors—own location (9 discrete states plus a null state for boundary violations) and other agent's location (also 10 states); 9-option action space (up/down/left/right, four diagonals, no-op); other agent's location is uncontrollable, so its transition dynamics use a uniform distribution over valid actions (e.g., probability 1/4 from location 1); planning horizon = 3 time steps; no explicit collision-avoidance preference is encoded (coordination must emerge from ToM).
- Apple-foraging generative model: three state-factor types—agent locations, binary reward feedback, and environmental items (wasteland / apple / empty orchard); partial observability (apples visible only at the current location); apples spawn probabilistically at 25% per time step in orchard locations; both agents start with certainty of an apple at the bottom-right corner (location 9) and uncertainty elsewhere; planning horizon = 3 time steps.
- In the foraging planning-tree appendix, the non-ToM focal (red) agent over a 2-step horizon selects going to location 9 with P=1.0 based on expected utility G=10.00, but ends up with no apple because the purple agent arrives first; the ToM agent instead chooses to explore.
- The two efficiency mechanisms borrowed from sophisticated inference are policy pruning (removing unlikely policy nodes) and observation pruning (focusing on probable outcomes) to limit combinatorial explosion.

## Critical notes from the literature
- The authors state results are qualitative; they explicitly flag the absence of "systematic quantitative evaluation using aggregated performance metrics across random seeds and statistical comparisons against non-ToM baselines," which future work should add to assess robustness. Results in the paper are illustrated via single example trajectories (Figure 2) rather than aggregate statistics.
- Scope is deliberately narrow: a simple 3x3 grid with deterministic dynamics and perfect observability of agent locations; the authors note real-world settings would involve noisier sensory information and more complex dynamics.
- The ToM agents assume knowledge of the other's goals and operate with fixed generative models of the other agent; the authors propose future online learning (e.g., Dirichlet counts) to learn others' models, preferences, and capabilities when initially unknown.
- The implementation is dyadic and uses only first-order ToM ("what does the other agent believe?"), not higher-order recursion ("what do I think the other agent thinks I believe?"); the authors note computational complexity grows exponentially with the number of agents, a scalability challenge, and that the framework is validated only in cooperative (complementary-goal) scenarios, not competitive/adversarial ones.
- In the reported ToM conditions only one agent (red) is ToM-equipped while the other (purple) is non-ToM, so dynamics between multiple mutually-reasoning ToM agents are not tested.

## Key topics covered
Theory of Mind; active inference; sophisticated inference; expected free energy (recursive EFE); multi-agent cooperation; tree-based / deep tree search planning; joint policy spaces; likelihood message passing / belief sharing; perspective separation and distinct belief representations; heterogeneous generative models; collision avoidance task; apple foraging task; partial observability; pymdp / JAX; policy and observation pruning; first-order vs higher-order ToM; false belief and ToM cognitive science background.
