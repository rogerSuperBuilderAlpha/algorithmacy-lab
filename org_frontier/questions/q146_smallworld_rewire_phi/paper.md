# q146 — Rewiring a conjunctive ring lowers Phi; there is no small-world peak

## Question

A conjunctive ring is a regular lattice in which integration runs around the loop. Watts and
Strogatz showed that rewiring a fraction of a lattice's edges toward random shortcuts passes
through a small-world regime that combines short paths with high clustering. Whether that
regime maximises integrated information is the question. If Phi has an interior maximum in the
rewiring probability p, the small-world topology integrates a Boolean system better than
either the lattice or the random graph.

## Method

The system is a conjunctive ring on n=6 nodes: each node's next state is the AND of its two
ring neighbours' current states. Watts-Strogatz endpoint rewiring replaces each input edge's
source with probability p by a uniformly random distinct source, preserving in-degree 2 and
forbidding self-loops and duplicate inputs. The sweep is p in {0, 0.1, 0.25, 0.5, 1}. p=0 is
the deterministic lattice control, evaluated once; interior p and p=1 are averaged over seeds
0, 1, 2. p=1 is the random-wiring control. For each network the reusable machinery returns the
whole-system verdict (structure and max Phi_MIP over reachable states) and the major complex
(core membership and its Phi). All randomness is seeded so the run reproduces byte-for-byte.

## Results

Mean max-Phi_MIP falls monotonically across the sweep: 4.0 at p=0, 3.0 at p=0.10, 2.14 at
p=0.25, 0.67 at p=0.50, 0.47 at p=1.00. The lattice is the maximum; the random graph is the
minimum. The interior peak the small-world hypothesis predicted does not appear. The value at
the first interior point already sits below the ring.

The verdict collapses along with the magnitude. The ring and light rewiring (p<=0.25) stay
triadic across all seeds. At p=0.50 one of three seeds reads dyadic; at p=1.00 two of three
read dyadic. Random conjunctive wiring on six nodes often strands a node or a sub-block, and
the system factors along a party-respecting cut.

The major complex churns the whole way: eight distinct cores across thirteen networks, from
the full {N0..N5} at the lattice to scattered pairs at the random extreme. Rewiring relocates
the integration onto smaller cores and then dissolves it.

## Interpretation

In this family the lattice integrates best and disorder only subtracts. Both hypotheses fail.
H1's interior peak is absent and the trend is monotone; H2's stable triadic verdict gives way
to dyadic verdicts once enough edges are rewired. The reading is that a conjunctive ring's
integration depends on the closed loop of mutual reads, and a shortcut breaks the loop rather
than tightening it. The contrast with the original small-world result is informative: short
path length and high clustering, the quantities Watts and Strogatz tracked, are not the same
quantity as irreducible integrated information, and optimising the former does not optimise
the latter here.

## Scope and limits

In-silico. Synthetic conjunctive Boolean networks on n=6, exact IIT-4.0 Phi, a five-point p
grid and a three-seed sweep. The monotone decline is clear at this resolution. A finer grid,
larger n, or a different coupling (parity, threshold) could behave differently and is not
tested. Much of the p=1 collapse comes from degenerate random conjunctive wirings at small n.
No empirical system is wired; the findings are on synthetic data and reach real coordination
only through a validation step not taken here.
