# Q206 — findings

Six-node rings under in-degree-2 Watts-Strogatz rewiring, exact IIT-4.0 Φ_MIP. Conjunctive (AND) ring on
an eight-point grid, two seeds; parity (XOR) ring on three diagnostic points, one seed (parity Φ at n=6
costs ≈ 416 s/network, so the parity grid is deliberately coarse — see methods).

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | faithful triad: triadic, Φ_MIP = 2.000000 |
| H2 conjunctive inflects in (0.25,0.5), Φ monotone | refuted | first-dyadic p = 0.35 (in range), but Φ is **non-monotone**: 4.0→2.0→1.0→0(dyadic)→0(dyadic)→2.71→2.62→1.0 |
| H3 parity ring starts at Φ ≠ 4.0 | confirmed | parity p=0: triadic, Φ_MIP = 0.500 — eight-fold below the conjunctive ring's 4.0 |
| H4 parity also declines under rewiring | refuted | parity Φ_MIP rises overall: 0.50 (p=0) → 0.25 (p=0.35) → 1.00 (p=1.0); the disorder extreme is the most integrated |
| H5 parity holds its verdict to a higher p than conjunctive | confirmed | conjunctive first-dyadic p = 0.35; parity stays triadic at every tested p (0, 0.35, 1.0) |

## The coupling family, not just the topology, governs the rewiring response

q146 swept a conjunctive ring and reported a clean monotone Φ decline to a dyadic random graph, and named
two open edges: the grid was coarse, and only one coupling was tried. Both turn out to matter. On the finer
grid the conjunctive decline is **not monotone**: Φ falls from 4.0 at the lattice to 0 at p=0.35–0.40,
where the verdict reads dyadic, then **recovers** to 2.7 at p=0.45–0.50 before falling again. q146's
five-point grid sampled p=0.25 and then jumped to p=0.5, both triadic, and missed the dyadic window between
them. The "clean monotone decline" is an artifact of coarse sampling.

The parity ring behaves oppositely. It starts far less integrated than the conjunctive ring — Φ = 0.5
against 4.0 on the identical topology with the identical full-system core — so the coupling sets the
integration scale (H3). But it never factors: it is triadic at p=0, at the conjunctive collapse point
p=0.35, and at the random extreme p=1.0, where its Φ is actually highest (H5, H4). The mechanism is plain.
A conjunctive node can be driven constant or cut off when rewiring hands it the wrong inputs, and the
system factors; an XOR node stays sensitive to whatever two inputs it has, so rewiring relocates a
dependence without removing one, and irreducibility survives. Disorder destroys integration under AND and
leaves it intact under XOR. The decline q146 found is specific to the conjunctive family, not a general
property of rewiring.

## Caveats

- **Compute-limited sampling.** Conjunctive uses two seeds per stochastic point; parity uses one seed and
  three points, because a parity Φ at n=6 costs ≈ 416 s against ≈ 26 s conjunctive. The cost asymmetry is
  itself a result (parity rings are far more expensive, consistent with #115's different parity law), but
  it means the precise extent of the conjunctive dyadic window and the full parity curve are not mapped
  here. A fuller seed and grid sweep is the open edge.
- The non-monotonicity is established (both seeds dyadic at p=0.35–0.40, both triadic at p=0.45–0.50); the
  window's exact boundaries are not.
- n=6, one ring topology, two coupling families, in-degree-2 endpoint rewiring. In-silico exact Φ; evidence
  about how topology and coupling shape integration, not a measurement of any organization.

**Reproduce.** Full sweep (conjunctive ~7 min, parity ~21 min, run the two `--coupling` workers then
`--report`); fast check: `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q206_ring_parity_rewire.probe_ring_parity_rewire --ci`
