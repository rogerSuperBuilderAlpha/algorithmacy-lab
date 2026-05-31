# Research question and pre-registered hypotheses

## Question (Tier A)

The Complex Brain Hypothesis (Mago et al. 2026) asserts, but does not compute, that **complexity rather
than entropy** indexes phenomenal richness, and that high entropy arises in two distinct regimes — a
fine-grained "rich" regime and a coarse-grained "contentless" regime — distinguishable by complexity
but not by entropy. The authors invoke the Ising model and the Aaronson coffee automaton as
illustrations and call for computational measures that can "disambiguate high-entropy states that
differ in complexity."

We ask: **On exactly-computable systems (the authors' own Ising example, and small systems where IIT Φ
is exact), do the CBH's two central claims hold?**

- **C1 (resolution of the conundrum).** Can two systems share high entropy yet be separated by a
  complexity measure (TSE neural complexity Cₙ, apparent complexity under coarse-graining, or exact
  IIT-4.0 Φ)? Does complexity, unlike entropy, peak at intermediate "structured" regimes and fall at
  maximal disorder?
- **C2 (grain-dependence).** Is the apparent complexity of a high-entropy disordered state high at fine
  grain (≈ entropy) but collapsing under coarse-graining, while a structured (critical) state retains
  complexity across grains — as the coffee/Ising picture predicts?

## Pre-registered hypotheses

- **H1 (CBH holds, as the authors expect).** Entropy is monotone in disorder, so it cannot separate the
  structured from the maximally-disordered regime. A complexity measure (Cₙ / apparent complexity / Φ)
  is non-monotone in disorder, peaking at an intermediate "critical/structured" regime, and so does
  separate them. Apparent complexity of the disordered state is grain-dependent (high fine, low coarse).
- **H0 (the dissociation fails on computable systems).** Either (a) the candidate complexity measures
  track entropy monotonically too (so they do not resolve the conundrum), or (b) they do not peak at an
  intermediate regime, or (c) the grain-dependence does not appear. Any of these would mean the CBH's
  resolution does not survive a concrete computational instantiation, at least with these measures.

We regard H1 as plausible — TSE complexity and Φ are designed to be non-monotone in disorder — but it is
not guaranteed for small systems, and a positive demonstration is itself the contribution the CBH lacks.
This is a **constructive** engagement: we build the model the hypothesis needs and report whether it
behaves as claimed, including any measure for which it does not.

## What a result establishes

- A positive result turns the CBH from a verbal hypothesis into a worked, reproducible computational
  model with exact numbers, on the authors' own example systems — and identifies *which* complexity
  measures realise the dissociation.
- A negative or partial result bounds the claim: it names the measures or regimes where the
  entropy–content dissociation does not hold on exactly-computable systems.

## Caveats fixed in advance

- "Apparent complexity" in the strict sense is Kolmogorov complexity (uncomputable); we use principled
  computable surrogates (TSE neural complexity; a description-length structure measure of coarse-grained
  configurations) and say so.
- Small/finite systems: a 4×4 Ising lattice has a finite-size crossover, not a sharp transition; exact-Φ
  systems are n ≤ 4. We claim the qualitative dissociation, not critical exponents.
- We test the information-theoretic content of the CBH (entropy vs complexity vs grain), not its
  neuroscientific or phenomenological claims about meditation or psychedelics.
