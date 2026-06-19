# Thread — a mediated triad degrades gracefully under noise, and parity degrades slower

A prior for the catalog. Real coordination is noisy. This thread perturbs a mediated triad — each node's
output flips with probability epsilon — and watches its integration fall. Two findings. The integration
decays smoothly and stays positive through heavy noise, with no abrupt collapse at a threshold, so the
triadic verdict is robust, not brittle. And a parity mediator keeps a larger fraction of its
integration at every noise level than a monotone one, so parity coordination is the more noise-robust of the
two. Reproduce with `python org_frontier/threads/noise/noise.py`.

## Setup

Two canonical triads, the AND mediator S = W ∧ C and the XOR mediator S = W ⊕ C, with the parties reading
the mediator. Each is taken to its exact Φ, then perturbed by flipping every node's output with probability
epsilon, and the Φ recomputed. The grid runs from no noise to a thirty-percent flip rate. The measure is the
maximum Φ across reachable states, and the fraction of the noiseless value it retains.

## The arc

**The integration decays smoothly and never collapses.** The AND triad starts at Φ = 2.0 and falls through
1.80, 1.53, 1.16, 0.61 to 0.28 as the flip rate rises from 2% to 30%, retaining 90%, 77%, 58%, 31% and 14%
of its noiseless value. The fall is gradual and the value stays positive throughout. A mediated triad lacks a noise threshold past which it factors all at once; it loses integration in proportion to the
perturbation, and a heavily perturbed triad is a weaker triad, still irreducible.

**Parity holds a larger fraction at every level.** The XOR triad starts lower, Φ = 0.5, but it keeps more of
itself under noise: 95%, 88%, 75%, 51% and 29% retained across the same grid, against the AND triad's 90%,
77%, 58%, 31% and 14%. At a ten-percent flip rate the monotone triad has lost 42% of its integration and the
parity triad only 25%. The parity mediator's symmetric, bijective dependence on both parties is the more
noise-robust coordination, even where its noiseless integration is smaller.

## What the thread establishes

A mediated triad degrades gracefully under noise instead of collapsing at a threshold, losing integration
smoothly in proportion to the perturbation and staying irreducible through a thirty-percent flip rate. And
the coordination logic sets the rate of decay: a parity mediator retains a larger fraction of its
integration at every noise level than a monotone one. As a prior for reading real coordination: a noisy
mediated arrangement should still read as integrated, weaker but unbroken, and an arrangement whose
mediator combines its parties symmetrically should tolerate more noise before it does.

## Limits, honestly

The noise model flips each node's output independently with a fixed probability, one of several ways to
perturb a system; correlated or input-dependent noise would have its own profile. The two forms are
canonical representatives of the monotone and parity classes, not a population, so the decay rates are exact
for these forms and not averages. Everything is in-silico, and a prior is to be tested against data.
