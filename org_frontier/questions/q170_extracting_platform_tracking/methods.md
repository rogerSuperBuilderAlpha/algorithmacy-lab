# Q170 methods

## The worker's probing loop

The worker runs the pp2 active-inference channel against a mediator gate. She sets her own input W
uniformly and observes the output, with the counterpart C hidden and drawn uniformly. After a fixed
budget of 4000 probes she fits her recovered generative model P̂(out=1 | W) from Laplace-smoothed
counts. The probing loop and the model-fidelity measures live in the shared bridge
`org_frontier.cognition.predictive_processing` (`probe_recover_marginal`, `recovered_model_kl`,
`recoverable_fraction`), seeded for determinism with `numpy.random.default_rng(0)`.

## The mediator and the interestedness ladder

The true rule is the Q126 mediator S'(W, C): the agenda a on the k input states where the parties
least warrant it, the faithful joint determination W ∧ C elsewhere. The approve agenda (a = 1) is used
because it degrades gracefully; the deny agenda collapses at k = 1. The ladder runs k = 0..4, with
k = 0 the faithful AND control.

## Model-fidelity measures

The recovered model assigns P̂(out|W) to each W. The true output at each (W, C) is deterministic, so the
KL of the recovered model from the true rule at a state is the surprise the recovered model places on
the realized output. The average over the four (W, C) states is the model-fidelity loss in bits. The
recoverable fraction is the fraction of states where the MAP read of the recovered model matches the
true output.

## The value-equalization k

The Shapley split of subsystem-Φ among the three parties comes from Q111's value function (all-ones
background), read at each k from `interested_rules` (Q131). The value-equalization k is the level where
the three Shapley values become equal (mediator share ≈ 1/3) while the coordination still carries
value. It is computed from the Shapley split, not assumed.

## Instrument control

The faithful triad `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` is classified before any
sweep; it must read verdict `triadic` with `max_phi` 2.0. The probe stops if the control fails.

## Scope

Exact Φ and a synthetic probing loop on a three-node Boolean model. The probing data are simulated. The
empirical-arm result is on synthetic probing data, not a measured worker. "Agenda", "extraction", and
"fidelity" name output values and recovered-model quantities, not measured intent. The Φ-to-economic-
value bridge is the lab's open question (Q122).
