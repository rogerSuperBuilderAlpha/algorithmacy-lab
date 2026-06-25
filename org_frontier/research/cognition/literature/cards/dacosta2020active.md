---
citekey: dacosta2020active
title: Active inference on discrete state-spaces: A synthesis
authors: Da Costa, Lancelot and Parr, Thomas and Sajid, Noor and Veselic, Sebastijan and Neacsu, Victorita and Friston, Karl
year: 2020
doi: 10.1016/j.jmp.2020.102447
arxiv: null
journal: Journal of Mathematical Psychology
programs: [cognition]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2001.07203
sha256: 66bfbf026448835f5f4641859794d2f766a50690778fd91738a3b45f88c3a6e9
pdf_path: literature/pdfs/dacosta2020active.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a tutorial-style synthesis paper, not an empirical study: it aims to bridge the gap between active inference as a normative principle and its practical process-theory implementation on discrete state-space models, because successive theoretical developments have made it hard to see how the principle relates to neuronal dynamics and code. The authors derive the entire process theory from first principles for the simplest model — a partially observable Markov decision process (POMDP) with prior over initial state D, transition matrix B, and likelihood matrix A — and frame behaviour as the minimisation of two objective functions: variational free energy (fitting the model to past observations, i.e., perception/state estimation) and expected free energy (scoring future policies against prior preferences, i.e., planning/action). They show that perceptual state-estimation reduces to a gradient descent on variational free energy implemented via a softmax of accumulated negative free-energy gradients, which they interpret as plausible neuronal (membrane-potential to firing-rate) dynamics, and that policy selection is a softmax of negative expected free energy that trades off risk (exploitation) against ambiguity (exploration). The expected free energy is shown to subsume many existing constructs — KL/risk-sensitive control, expected utility, Bayesian decision theory, information gain, intrinsic motivation, and Bayesian surprise — as special cases. Learning is cast as slower synaptic-plasticity dynamics (Dirichlet-parameter accumulation, formally identical to Hebbian plasticity), and structure learning is addressed via Bayesian model reduction and Bayesian model expansion. The paper positions itself as a building block for understanding mixed (discrete + continuous) generative models and as a practical guide for simulation and empirical prediction.

## Key facts it relies on
- Active inference rests on two complementary objective functions: a variational free energy measuring the fit between an internal generative model and past sensory observations, and an expected free energy scoring future courses of action against prior preferences.
- The variational free energy is the negative evidence lower bound (ELBO) optimised in variational Bayes; it is an upper bound on surprise (−log P(o)) and can be decomposed into complexity minus accuracy (Eq. 3), or equivalently into a KL divergence from the true posterior plus log evidence (Eq. 2).
- The process theory is derived for the simplest discrete model — a POMDP with three matrices: D (prior over initial state), B (state transition probabilities given an action), and A (likelihood mapping states to outcomes); see Figure 2 and the glossary in Table 2.
- Perception equates to state estimation; neuronal dynamics are a gradient descent on variational free energy with state estimates expressed as a softmax (σ) of accumulated negative free-energy gradients (Eqs. 8–9), interpreted as average membrane potentials (v) mapping to average firing rates (s) via softmax.
- These state-estimation dynamics coincide with variational message passing under the mean-field approximation, and with belief propagation under the Bethe approximation — both widely used approximate-inference algorithms.
- Policy posterior is a softmax of negative expected free energy, Q(π) = σ(−G(π)) (Eq. 10); expected free energy decomposes into risk plus ambiguity (Eq. 13), and equivalently into extrinsic value plus intrinsic value (salience over states and novelty over parameters) (Eq. 16).
- Action is selected as a Bayesian model average — the most likely action under all policies (Eq. 11) — and policy-independent state estimates are obtained by Bayesian model averaging over policies (Eq. 12).
- Learning the likelihood matrix A follows a gradient descent on variational free energy, yielding a one-step end-of-trial update of Dirichlet parameters a = a + Σ oτ ⊗ sτ (Eq. 21), which counts state-outcome co-occurrences and is formally identical to associative/Hebbian plasticity.
- The synthesised dynamics are claimed to reproduce a wide range of electrophysiological responses, including repetition suppression, mismatch negativity, violation responses, place-cell activity, phase precession, theta sequences, theta-gamma coupling, evidence accumulation, race-to-bound dynamics, and transfer of dopamine responses.
- The paper notes that visual saccadic sampling occurs at roughly 4 Hz, and that prior preferences (e.g., body temperature around 37°C) can be encoded as infinitely precise hyperpriors (Dirac delta) that are not updated.

## Critical notes from the literature
- The authors explicitly distinguish active inference as a principle (a consequence of fundamental assumptions about living systems — Markov blanket plus non-equilibrium steady state) from active inference as a process theory (a hypothesis about brain computation); the process-theory claims about neuronal implementation are hypotheses, not established facts.
- The paper states that full endorsement of the process theory requires rigorous empirical validation of the synthetic electrophysiological responses, which has not yet been done; it offers only "face validity" because predicted responses resemble empirical measurements.
- Scalability is a stated limitation: planning requires evaluating expected free energy for each policy, which suffers a combinatorial explosion; the Occam-window pruning of policy trees is biologically plausible but "cannot deal with large policy spaces" and only partially explains deep policy search.
- The key open challenge the authors identify is finding the generative model that best explains observed behaviour (the model-identification / structure-learning problem); a complete set of mechanisms for biological structure learning "has not yet been laid out."
- Inference quality depends on the chosen factorisation of the approximate posterior (mean-field vs marginal vs Bethe), each trading accuracy against computational cost; the authors note the marginal approximation (as in the spm_MDP_VB_X.m implementation) "currently stands as the most biologically plausible," implying the mean-field treatment used for didactic derivation is not the most accurate.

## Key topics covered
Active inference; free energy principle; variational free energy; expected free energy; variational Bayesian inference; evidence lower bound (ELBO); POMDP / Markov decision process; discrete state-space generative models; likelihood matrix A, transition matrix B, prior D; Dirichlet distribution; mean-field, marginal, and Bethe approximations; softmax / belief updating; perception as state estimation; planning and policy selection; risk and ambiguity; intrinsic vs extrinsic value (salience, novelty); Bayesian model average / model selection; variational message passing; belief propagation; Hebbian / synaptic plasticity learning; Bayesian model reduction; Bayesian model expansion / structure learning; Markov blanket; non-equilibrium steady state (NESS); predictive coding; dopamine / precision; mixed generative models; electrophysiological response synthesis.
