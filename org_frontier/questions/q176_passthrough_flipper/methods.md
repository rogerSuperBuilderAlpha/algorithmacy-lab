# q176 — Methods

## Machinery

The study reuses the field bridge `org_frontier/field/rule_to_phi.py`, study 1 of the
field line. `rule_to_phi(rules, labels)` encodes per-party determination rules into a
deterministic state-by-node TPM and reads the exact IIT-4.0 Phi verdict over the
minimum-information partition, returning the dyadic or triadic structure and the max
Phi_MIP. `phi_ci(coder_phis)` propagates a panel of per-coder Phi readings into a
studentized bootstrap-t confidence interval; identical readings collapse it to a point.
Phi is not reimplemented.

Labels are ("W", "S", "C") over the little-endian state x = (W, S, C). The system rules:
commit S = x0 & x2, relay S = x0, store S = x2.

## Instrument control

Three checks run before the result. The faithful triad
[x1, x0 & x2, x1] reads triadic with max Phi 2.0. A decoupled relay [x0, x0, x2] reads
dyadic with Phi 0. A fully committed account [x1, x0 & x2, x1] reads triadic with Phi 2.0,
and a panel of identical readings returns a degenerate zero-width CI. All three pass
before any result is computed.

## H1 — flip rate

The worker and counterpart rules range over a fixed source basis: single-source forms
(follows W, S, or C) and pairwise AND/OR couplings, five forms each. The system rule is
the manipulated bit. Each of the 25 worker-counterpart pairs is read under commit; pairs
that read triadic under commit are in scope. Each in-scope account is re-read with the
system rule switched to relay. The flip rate is the fraction of in-scope accounts that
read dyadic under relay.

## H2 — per-rule CI-sensitivity decomposition

Five synthetic accounts each name a set of plausible coder readings per party. The system
always carries the commit / relay / store ambiguity. The worker and counterpart each
carry a coupled reading and a decoupled-self reading, so a coder split on either could in
principle swing the verdict. The first reading of each party is the consensus.

For each party, a coder panel splits across that party's plausible readings while the
other two parties hold their consensus reading. The induced Phi-CI width is read from
`phi_ci` over the panel's Phi readings. Each party's width as a fraction of the total
across the three parties is its sensitivity share. The reported statistic is the median
system share over the accounts with nonzero induced width.

## Determinism

Every `phi_ci` call seeds a fresh `numpy.random.default_rng(0)`. The account family and
the basis are fixed lists. Output is byte-identical across runs.

## Scope

Synthetic coded rule sets, not measured worker states. The empirical arms report results
on synthetic data.
