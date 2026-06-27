# Coupling sets the rewiring response: a parity ring resists what a conjunctive ring cannot

<code + data: org_frontier/questions/q206_ring_parity_rewire/ ; probe #360 in probes/PROBES.md>

## Abstract

q146 found that rewiring a conjunctive ring lowers integrated information monotonically toward a dyadic
random graph, and left two questions open: whether the decline holds on a finer grid, and whether it holds
for a different coupling. Both fail. On a finer grid the conjunctive decline is non-monotone — Φ drops to a
dyadic window at p≈0.35–0.40 and recovers to triadic at p≈0.45–0.50, a structure the coarse grid skipped
over. A parity (XOR) ring starts eight-fold less integrated than the conjunctive ring on the identical
topology (Φ 0.5 vs 4.0) yet never factors: it stays triadic at the lattice, at the conjunctive collapse
point, and at the random extreme, where its Φ is highest. The coupling family, not the topology alone,
governs how rewiring changes integration.

## Introduction

Whether a coordination form is irreducible (triadic) or factors (dyadic) is read from its cause-effect
structure. q146 asked how that verdict moves as a ring is rewired toward a random graph and reported a
clean monotone collapse with the verdict turning dyadic at high rewiring. It closed with two caveats: the
five-point p grid could hide structure between samples, and the conjunctive (AND) coupling was a fixed
choice that other couplings might not share. #115 had already shown the parity family scales by a different
law. This probe tests both edges.

## Related work

q146 is the direct predecessor (conjunctive ring, n=6, Watts-Strogatz endpoint rewiring). #132 and q143
establish the conjunctive ring as the integrated reference topology with Φ constant in n. #115 shows the
parity family scales differently, motivating the coupling comparison.

## Hypotheses

H1 (control): the faithful triad reads triadic at Φ=2.0. H2: on a finer grid the conjunctive verdict first
turns dyadic in (0.25, 0.5) and Φ stays monotone. H3: the parity ring starts at Φ ≠ 4.0. H4: the parity
ring also declines under rewiring. H5: the parity ring holds its triadic verdict to a higher p than the
conjunctive ring. Nulls are the negations, fixed in `hypotheses.md` before computing.

## Methods

Both forms are six-node rings; a node is the AND (conjunctive) or XOR (parity) of its two current input
sources, with q146's in-degree-2 endpoint rewiring. Verdicts and Φ_MIP use `probes/lib.verdict`. The
conjunctive arm sweeps p ∈ {0, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 1.0} at two seeds; the parity arm uses
three diagnostic points {0, 0.35, 1.0} at one seed, because a parity Φ at n=6 costs ≈ 416 s against ≈ 26 s
conjunctive and a full parity sweep is infeasible here. This reduction from the pre-registered grid is a
compute constraint discovered at run time, documented in `methods.md`; the hypotheses are unchanged. The
instrument control passed (triadic, Φ = 2.000000) before any sweep number was read.

## Results

H1 confirmed. H2 refuted: the first dyadic verdict appears at p=0.35, inside (0.25, 0.5), but Φ is
non-monotone — 4.0, 2.0, 1.0, 0 (dyadic), 0 (dyadic), 2.71, 2.62, 1.0 — with a dyadic window at 0.35–0.40
and a triadic recovery at 0.45–0.50 that q146's grid jumped over. H3 confirmed: the parity ring at p=0 is
triadic at Φ = 0.5, eight-fold below the conjunctive 4.0 on the same topology and same full-system core. H4
refuted: parity Φ does not fall under rewiring; it runs 0.50, 0.25, 1.00 across p = 0, 0.35, 1.0, with the
random extreme the most integrated. H5 confirmed: the conjunctive ring's verdict turns dyadic at p=0.35
while the parity ring stays triadic at every tested point.

## Discussion

The coupling family governs the rewiring response. A conjunctive node can be driven constant or
disconnected when rewiring assigns it the wrong inputs, and the system factors; an XOR node remains
sensitive to whichever two inputs it holds, so rewiring relocates a dependence rather than removing one,
and irreducibility persists. q146's monotone decline to a dyadic random graph is therefore specific to the
conjunctive family, and even there it is an artifact of coarse sampling — the finer grid shows a
non-monotone curve with a dyadic window and a recovery. The general lesson is that a rewiring study's
verdict trajectory is sensitive both to the grid resolution and to the coupling, and that integration
magnitude (low for parity) and integration robustness (high for parity) are independent: a form can be
barely integrated yet hard to disintegrate.

## Limitations

n=6, one topology, two couplings. The conjunctive arm has two seeds and the parity arm one seed and three
points, so the exact extent of the dyadic window and the full parity curve are unmapped; the compute cost
that forces this (parity ≈ 416 s/network) is itself reported. In-silico exact Φ on synthetic Boolean rings;
no empirical coordination is wired, and the findings transfer to real systems only through a validation step
not taken here.

## References

q146 (org_frontier/questions/q146_smallworld_rewire_phi/); #115, #132, q143 (org_frontier/probes/PROBES.md).
