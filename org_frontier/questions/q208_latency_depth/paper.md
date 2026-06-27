# Represented delay is benign: the single-buffer anomaly and the recovery of full integration

<code + data: org_frontier/questions/q208_latency_depth/ ; probe #362 in probes/PROBES.md>

## Abstract

q205 found that one represented buffer on a mediator's feedback path keeps a triad triadic while halving
its whole-system Φ and displacing the worker from the core. This sweeps the buffer depth k = 0..3 to test
whether that is a decay law. It is not. The triad stays triadic at every depth, but whole-system Φ_MIP runs
2.0, 1.0, 2.0, 2.0 — a single dip at depth one and full recovery thereafter — and the worker, displaced at
k=1, rejoins the core at k=2 and k=3, where the entire delay line and all three parties form one
irreducible complex at Φ = 2.0. The displacement and the halving q205 reported are artifacts of depth one,
not properties of represented latency. Set against q207, where slowing the mediator's commit rate dissolved
the triad, the result is that a mediator can be arbitrarily late and still bind every party.

## Introduction

The lab's instrument reads a one-step transition, so a lagged coupling can read as unintegrated unless the
lag is given explicit nodes (q205). q205 represented one step of delay as a buffer and found the triad
survived but with the worker displaced and Φ halved, and read this as latency relocating integration. It
tested one depth. Whether deeper represented delay erodes integration further, factors the triad, or leaves
it intact is the open question.

## Related work

q205 (latency feedback) is the direct predecessor and the k=1 point. q207 (slow mediator) is the companion
deformation, where commit rate rather than delay is varied. The conjunctive triad and its Φ_MIP = 2.0
verdict are the reference form.

## Hypotheses

H1 (control): F_0 reads triadic at Φ=2.0. H2: F_k is triadic at every k. H3: whole-system Φ_MIP decreases
strictly with k. H4: every buffer is in the major complex. H5: the worker stays out of the core for k ≥ 1.
Nulls are the negations, fixed in `hypotheses.md` before computing.

## Methods

F_k (n = 3 + k) is the conjunctive triad with k buffers in series: S' = W∧C every step, B1' = S,
Bj' = B(j−1), and the parties read the last buffer (W' = C' = Bk), so the mediator reaches them k steps
late. F_0 is the synchronous triad; F_1 is q205's form. The sweep is k = 0, 1, 2, 3 (n = 3, 4, 5, 6).
Verdicts use `probes/lib.verdict`, cores `major_complex`. The instrument control passed (triadic,
Φ = 2.000000) before any other number was read.

## Results

H1 confirmed. H2 confirmed: every depth is triadic. H3 refuted: whole-system Φ_MIP is 2.0, 1.0, 2.0, 2.0 —
a single dip at k=1, then full recovery, not a monotone decay. H4 confirmed: the entire delay line is in
the major complex at every depth. H5 refuted: the worker is excluded only at k=1, in a core that is one of
two W/C-symmetric three-node complexes; at k=2 and k=3 the worker rejoins and the major complex is the
whole system at Φ = 2.0.

## Discussion

Represented delay is benign for irreducibility. Once the lag has explicit nodes, the triad stays
irreducible at every depth tested, and its integration is undiminished except at the lone depth-one case.
That case is a small-structure coincidence: a single buffer driving both parties off the same delayed value
makes a proper three-node subset the maximal complex, which q205 read as the worker being displaced and Φ
halved. A second buffer turns the path into a clean multi-step feedback loop that binds every node, and the
full triad returns to the core at Φ = 2.0. The finding revises q205's interpretation and completes the
contrast with q207: delay, however deep, does not break binding, while a halved commit rate breaks it
outright. Lateness and intermittency are different, and only intermittency is fatal.

## Limitations

Full-Φ recovery is shown at k = 2 and k = 3; n = 6 is the compute ceiling, so k ≥ 4 is untested. The k=1
core is W/C-symmetric, so the displaced party is arbitrary. One reference triad, conjunctive coupling,
exact Φ. In-silico; no empirical coordination is modeled.

## References

q205 (org_frontier/questions/q205_latency_feedback/); q207 (org_frontier/questions/q207_slow_mediator/).
