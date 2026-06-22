# Distance to the dyad: the Φ margin as a continuous measure of mediation

The second deep dive from the [mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md),
taking Q4 from the [mediation-boundary thread](../mediation_boundary/QUESTIONS.md) twenty steps deep. Where
the first dive treated commit and convey as a binary verdict, this one makes the verdict continuous by
giving the mediator a commit probability and the parties a read fidelity, and maps how Φ measures the
distance from a real three-party coordination to a factoring dyad. The headline is that the margin is a
graded distance with structure: convex, thresholdless, set mostly by how reliably the determination is
actually committed, and bounded below by zero for any gate the co-monotonicity law forbids.

## Contents

- [`DEEP_DIVE.md`](DEEP_DIVE.md) — the twenty-step chain, each step's question drawn from the previous
  step's result, with the margin map.
- [`chain.py`](chain.py), [`_sphi.py`](_sphi.py) — exact Φ on stochastic coordination TPMs, and every
  computation in the chain.

## The margin, in one statement

A mediator that commits its determination with probability p, read by parties with fidelity q, sits at a
distance from the dyad that Φ measures continuously. The curve is convex and has no threshold: any nonzero
commitment gives a nonzero margin, fading smoothly to zero, so there is no weakest commit. The two knobs do
not separate, the least-live party gates the margin, and adding parties raises the full-commit value while
steepening its decay. The perturbations that erode a real arrangement have ordered fragilities, from
resilient to brittle: a back-channel tolerated to nearly half strength, then read fidelity, then the
commit, then substitutability, which tears the margin down at the first increment. A mixed-direction veto
gate is zero at every commit probability, so the first dive's co-monotonicity law is the floor of this
dive's margin.

## The compliance reading

The commit probability is a compliance rate. A merge gate where every change follows the rule sits at full
margin, which is why [v9](../../recurrence/event_series/)'s elicited merge triad measured Φ = 2; a process
where some changes bypass the gate sits lower on the curve. The margin is a measure of how far a gate's
actual practice sits from the determination it claims to make, a quantity the
[field protocol](../../field/PROTOCOL.md) could estimate from a determination's observed firing rate.
