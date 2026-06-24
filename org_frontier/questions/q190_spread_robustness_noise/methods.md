# q190 methods

## Construct under test

The disagreement-Φ bridge (q183) scores the spread between two party accounts of one
coordination: verdict_agreement, phi_gap, and core_jaccard. This study asks whether that spread
survives noise in how each account's rules are elicited.

## Accounts and the noise model

Each account is a per-node Boolean rule list over labels (W, S, C). tpm_from_rules turns it into a
deterministic state-by-node TPM. Elicitation noise perturbs that TPM: each entry is gated by
Bernoulli(RATE = 0.10); a gated entry is pulled toward 0.5 by DELTA = 0.10, so a deterministic 1.0
becomes 0.9 and a 0.0 becomes 0.1. The table stays near-deterministic, modeling an imprecise but
honest elicitation. Whole-system max Φ_MIP of the perturbed (mildly stochastic) TPM is read by
max_phi_float, which infers the connectivity matrix numerically and calls the exact IIT-4.0 oracle.

This rate was calibrated once on the two anchor forms. At RATE = 0.10, DELTA = 0.10 a faithful
triad keeps Φ at or above about 0.65 across 30 draws and never falls to dyadic, while a clean dyad
stays at Φ near zero on most draws and lifts above the classifier's epsilon only occasionally. The
boundary is the only place a verdict can move.

## Pairs

Six pairs span the boundary. Two FAR pairs put two triads together (faithful triad vs an AND-triad
and vs an OR-triad), both with noiseless Φ = 2.0. Two NEAR pairs put a triad against a clean dyad
(Φ near zero). One pair puts two clean dyads together; both sit at the boundary, so it is NEAR by
the min-Φ test and is kept to show agreement can move on the agreeing side of the boundary too. One
pair is the bridge anchor: the faithful triad against itself.

A pair is NEAR-boundary iff min(Φ_A, Φ_B) at noise zero is within EPS_BOUNDARY = 1e-6 of zero,
i.e. at least one account is a clean dyad. Otherwise it is FAR.

## Measurements

Over SEEDS = 30 seeded draws per pair, the probe records how often verdict_agreement flips from its
noiseless value, how often the signed phi_gap (Φ_A − Φ_B) changes sign, and the mean and standard
deviation of |phi_gap|. H2 pools |phi_gap| over the pairs that disagree at noise zero.

## Decision rules

H1 is SUPPORTED if every agreement flip and every sign change falls on a NEAR-boundary pair and no
FAR pair ever flips. H2 is SUPPORTED if, pooled over the noiseless-disagreeing pairs,
sd(phi_gap) < mean(phi_gap), i.e. signal-to-noise above one.

## Instrument control

The control checks three things. The bridge anchor (faithful triad vs itself) reads
verdict_agreement 1, phi_gap 0.0, core_jaccard 1.0. The noiseless faithful triad reads max_phi
2.0. A near-boundary pair (triad vs clean dyad) flips its agreement at least once under noise while
a far pair (triad vs AND-triad) never does. The probe prints "CONTROL ... PASS" and aborts on
failure.

## Determinism

Every draw uses numpy.random.default_rng(seed) with a fixed seed loop, and the Φ oracle seeds its
state search with numpy.random.default_rng(seed). The run was repeated three times and the stdout
was byte-identical.

## Validation gap

Exact IIT-4.0 Φ on small synthetic Boolean coordination forms. "Account", "elicitation noise",
"spread", and "boundary" name rule-table-and-Φ quantities, not measured organizations. The accounts
are coder-supplied, so both arms report baselines on synthetic data. In-silico scope; the
Φ-to-organization bridge is open.
