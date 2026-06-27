# Q208 — findings

The conjunctive triad with a delay line of k buffers on the mediator's feedback path, swept k = 0, 1, 2, 3
(n = 3..6), exact IIT-4.0 Φ.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | F_0: triadic, Φ_MIP = 2.000000 |
| H2 represented latency never factors | confirmed | F_1, F_2, F_3 all triadic |
| H3 whole-system Φ_MIP decays monotonically | refuted | Φ_MIP by depth is **2.0, 1.0, 2.0, 2.0** — a single dip at k=1, not a decay |
| H4 every buffer is load-bearing | confirmed | the full delay line is in the core at every depth |
| H5 the worker stays excluded | refuted | the worker is excluded only at k=1; it rejoins the core at k=2 and k=3 |

Cores by depth: k=0 {W,S,C}; k=1 {S,C,B1}; k=2 {W,S,C,B1,B2}; k=3 {W,S,C,B1,B2,B3}. Major-complex Φ is
2.0 at every depth.

## The single-buffer case is an anomaly, not a law

Represented latency does not factor the triad and does not erode its integration. At depths 0, 2, and 3 the
whole system — all parties and the entire delay line — is one irreducible complex at the full Φ_MIP = 2.0.
The expectation going in, set by q205, was a decay curve: each buffer dilutes the whole-system Φ, and the
worker stays displaced. Neither holds. Whole-system Φ_MIP dips to 1.0 at k=1 and returns to 2.0 at k=2 and
k=3, and the worker, displaced from the core at k=1, rejoins it at every deeper depth.

The depth-one form q205 studied is therefore a special case. At k=1 a single buffer feeds both parties the
same delayed value while the mediator reads both parties, and the maximal complex is a proper three-node
subset — one of the two symmetric triples {S,C,B1} or {S,W,B1}, the tie broken arbitrarily — with the third
party left out and whole-system Φ_MIP at 1.0. q205 read this as the worker being displaced and integration
halved. The sweep shows the displacement and the halving are artifacts of depth one. Add a second buffer and
the delay line becomes a clean k-step feedback loop that binds every node at once, restoring the full triad
to the core at Φ = 2.0.

The lesson for the mediator-deformation thread: represented delay is benign for irreducibility. It sits
opposite q207, where slowing the mediator's commit rate dissolved the triad outright. A mediator can be
arbitrarily late and still bind every party; it cannot be intermittent and bind any.

## Caveats

The full-Φ recovery is shown at k=2 and k=3 only; exact Φ at n=6 (k=3) is the compute ceiling here, so
k ≥ 4 is untested and a different pattern at greater depth is not excluded. The k=1 core is one of two
W/C-symmetric three-node complexes, so "worker" and "counterpart" are interchangeable there. n ≤ 6, one
reference triad, conjunctive coupling, exact Φ. In-silico; evidence about how represented delay shapes
irreducibility, not a measurement of any organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q208_latency_depth.probe_latency_depth`
