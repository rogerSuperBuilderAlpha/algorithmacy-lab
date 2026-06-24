# Q146 — Stage 1 review: rewiring a ring from lattice to random

## The question

A conjunctive ring is a regular lattice: every node reads its two neighbours, and integration
runs around the loop. A random Boolean wiring is the opposite extreme. Watts and Strogatz
showed that interpolating between the two, by rewiring a fraction p of edges toward random
shortcuts, passes through a small-world regime where short path length coexists with high
clustering. Whether that regime is also where integrated information peaks is the question.
If Φ has an interior maximum in p, then the small-world topology integrates a Boolean system
better than either the lattice or the random graph.

## What the lab already knows that bears on this

- The verdict is structurally fragile: a single edge or read can toggle triadic to dyadic
  (Finding 1, `classifier/`). Rewiring moves many edges at once, so whether the verdict
  survives the sweep is not obvious from the single-edge result.
- The major complex can shift its membership without the whole-system verdict changing
  (Q74, Q94). Rewiring is a direct way to make the core churn while watching the verdict.
- Φ depends on the encoding and is at most an ordinal hint as a magnitude (classifier
  docstring). A peak in mean Φ across p is read as an ordinal comparison among topologies at
  one fixed coupling, not as a calibrated scale.

## The gap

No study in the corpus sweeps topology from lattice to random and reads Φ along the way. The
small-world peak is a hypothesis about where integration is maximised in connectivity space,
and it is untested here for Boolean systems under exact Φ.

## Scope

In-silico. Synthetic conjunctive Boolean networks on n=6, exact IIT-4.0 Φ, a coarse p grid
and a three-seed sweep. No empirical system is wired. The findings transfer to real
coordination data only through a validation step that is not taken here.
