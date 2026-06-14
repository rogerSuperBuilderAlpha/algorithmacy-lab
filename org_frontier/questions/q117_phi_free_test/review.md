# Q117 — Stage 1 review: a Φ-free test for triadicity

## The question

The program reads the verdict with exact IIT-4.0 Φ, an exponential oracle. This asks whether a predicate
computed without Φ, from the truth tables alone, reproduces the verdict on the whole 256-form
strict-mediation family, and whether the feedback cycle suffices or a logical condition is also needed.

## What the lab already knows that bears on this

- **Triadic forms carry a feedback cycle (probes 25, 39); the n=3 minimum is 4 edges (probe 35).** The cycle
  is the standing candidate for a necessary condition.
- **Cheap dependence proxies fail to separate the verdict (probes 45-47).** A sufficient condition, if one
  exists, is unlikely to be correlational and more likely logical.
- **The 256-form family is enumerable and holds both classes (Q93, Q105).** It splits 24 triadic / 232
  dyadic, with single-bit flips moving across the boundary, so it is the natural test bed for a Φ-free law.

## The gap

The program has a candidate necessary condition and a warning that connectivity will not suffice, but has
never tested a Φ-free predicate against the oracle on a complete family, nor found the logical condition that
would close necessity into sufficiency. Whether the exact oracle is replaceable here is untested.
