# q148 — Findings

A feedforward chain of gating hubs does not hold a core that spans its groups. At every tested depth the
major complex is the first hub and its group alone. Every downstream group drops out.

## Result (synthetic, exact Φ; group size g = 1)

| L | n | core | groups in core | whole-system Φ | break location |
|---|---|------|----------------|----------------|----------------|
| 2 | 4 | H0, p0_0 | 1 of 2 | 0.000 | H0–H1 seam |
| 3 | 6 | H0, p0_0 | 1 of 3 | 0.000 | H0–H1 seam |
| 4 | 8 | H0, p0_0 | 1 of 4 | 0.000 | H0–H1 seam |

Control: a single all-spanning hub binds every node into one complex. At n = 4 its core spans all 4 nodes
(Φ = 3.000). The all-spanning hub is fully integrated, so its maximal complex grows costly fast; n >= 6 is
skipped to keep the probe deterministic and re-runnable. A built-to-span hub spans every node at n = 4, where
the chain holds one group; that contrast is fixed at n = 4 and holds as n grows.

## Verdicts

- H1 (depth caps integrable group size): SUPPORTED. The chain never spans all groups; it holds one group at
  every depth from L = 2 to L = 4. The cap is not a graded critical length but an immediate one: the core
  stops at the first seam. The null — core span equal to the full chain and independent of L — is rejected.
- H2 (the break falls at a hub seam): CONFIRMED. The surviving core is a whole group, hub plus its party, and
  the break sits at the H0–H1 hub-to-hub link, not inside a group. Hub-to-hub gating is the bottleneck.

## Why

A downstream hub computes hub_{k-1} AND its group. The AND gate breaks the two-way constraint that
irreducibility needs across the seam: only the first hub and its own party form a mutually constraining loop,
so only that group integrates. Whole-system Φ is 0 because the rest factorizes off that loop.

## Scope

Synthetic Boolean forms under exact IIT-4.0 Φ at g = 1. "Core", "span", and "seam" are graph-and-Φ quantities,
not measured organizations. Whether real hierarchies behave this way is not shown here; the
Φ-to-organization bridge is open.
