# Granovetter — Stage 3 hypotheses (fixed before computing the forms of H2–H5)

## The rendering that all five share

A **tie** is symmetric and has a **strength** p ∈ [0, 1], read as Granovetter's first dimension, time: each
step, each endpoint reads the other with probability p, independently. **Strong** p = 1, **weak** p = 0.5,
**absent** p = 0. A node's next state is the AND of the inputs it read this step; a node that read nothing
holds its state. Weak ties make the network stochastic and Φ is exact IIT-4.0 on the probabilistic TPM.

**Transmission** (Granovetter's "path") is the number of ordered pairs joined by a path of ties of any
strength. **Integration** is Φ and membership in the major complex. The paper's question is where the two
come apart.

## H1 — Strength is graded (C1)

- **H1 (Granovetter).** The Φ of a dyad is strictly increasing in tie strength p over {0.25, 0.5, 0.75, 1}.
- **H0.** Φ is flat, or non-monotone, in p.
- **Lab prior.** With Granovetter. The machinery check run before these hypotheses were fixed already showed
  Φ = 0.252, 0.658, 1.236, 2.000; H1 is retained as the calibration the other four rest on.

## H2 — The forbidden triad (C2)

- **H2 (Granovetter).** With A–B and A–C strong, the open triad (B–C absent) is less integrated than the
  triad closed by a weak B–C tie, which is less integrated than the triad closed by a strong one: Φ(open) <
  Φ(weak-closed) < Φ(strong-closed); all three members are in the core in each.
- **H0.** Closure of some strength does not raise Φ, or drops a member.
- **Lab prior.** With Granovetter on the ordering of open and strong-closed (the conjunctive triad at 2 and
  the conjunctive clique at 6). Open on the weak closure.

## H3 — The bridge (C3)

- **H3 (Granovetter).** A weak bridge between two strong dyads joins them as a strong bridge does: the
  transmission count is the same (12 ordered pairs), and the major complex spans both dyads in both cases.
- **H0.** Transmission equal but the major complex does not span both dyads under a weak bridge (or under
  either).
- **Lab prior.** Against on integration. The machinery check showed both bridges leave a single dyad as
  the major complex at Φ = 2.000; the weak-bridged whole has Φ_MIP = 0.830 and the strong-bridged 2.000. The
  bridge transmits and does not integrate; H3 is retained so the divergence is on record as a verdict.

## H4 — Damage (C4)

- **H4 (Granovetter).** In the two dyads joined by a weak bridge, removing the bridge does more damage than
  removing a within-dyad strong tie, on transmission (pairs lost) and on integration (major-complex Φ lost).
- **H0.** The strong tie's removal costs at least as much on one measure.
- **Lab prior.** With Granovetter on transmission; against on integration — the bridge is not in the
  complex, the strong tie is.

## H5 — Local cohesion, overall fragmentation (C5)

- **H5 (Granovetter).** Three strong dyads joined by weak ties in a chain (a~b~c) or a ring (a~b~c~a) are one
  whole — a major complex spanning all three dyads — where the same dyads unjoined are three complexes of
  two. Transmission rises from 6 pairs to 30.
- **H0.** The weak chain or ring leaves the major complex within one dyad.
- **Lab prior.** Against on integration for the chain; open on the ring, where every dyad is read and
  returns.

## Not tested here

The job-finding evidence, the diffusion-study critique, adopters, the 1983 qualifications (`exegesis.md`).
