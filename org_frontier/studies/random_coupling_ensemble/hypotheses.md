# random_coupling_ensemble — hypotheses (fixed before computing)

**Question (agenda #18).** Across random coupling topologies at fixed n, what
is the distribution of Φ and the triadic rate, and does it match any standard
network ensemble — or only hit the discrete steps from `interior_ring_pool`?

**Already known (cited, not reopened).**
- **`interior_ring_pool` (#19):** NO_INTERMEDIATE_LAW; designed interiors sit on
  discrete Φ atoms (at n=4: ring 4, pool 12, incomplete/interior 6; at n=6:
  4→6→8→9→12→30).
- **q147:** random *truth-table* Boolean nets — cycle density predicts triadicity;
  core in-degree does not predict Φ. Different sampling axis than random
  *coupling graphs*.
- **q146 / small-world #17:** WS rewiring from a ring lowers/collapses Φ;
  PICK_ONE vs hub growth.
- Ternary TOOLING_GAP / residual-cascade noted only.

**Gap.** #19 designed specific interiors. #18 asks the **distribution** under
random topology generators (ER / fixed-in-degree / WS / BA-style), with
conjunctive AND on in-neighbors — whether mass fills the ring–pool gap or sits
on the same discrete landmarks, and whether triadic rates track ensemble type.

**Universe.** Binary exact IIT-4.0. Conjunctive AND of in-neighbors. Primary
fixed **n=4**, N=32 seeds per ensemble (exact-Φ feasible). Thin **n=5** check
(N=8, fixed_k=2 only). Candid: n=5 is ~5–10s/sample; n=6 out of budget here.

## Ensembles (structural generators, not claimed identity)

| name | construction |
|---|---|
| ER(p) | each directed edge i←j (i≠j) with prob p; empty in-nbr → one random input |
| fixed_k | each node chooses exactly k distinct in-neighbors uniformly |
| WS(p) | conjunctive ring; each input rewired with prob p (in-degree 2) |
| BA(m) | preferential-attachment grow; new node reads m older targets |

Coupling: node i' = AND(in-neighbors(i)).

**Landmark set at n=4:** {2, 4, 6, 12} (chain-like / ring / #19 interior /
pool). At n=5 add {3, 8, 20} from known families.

## H1 — instrument + poles

Faithful triad. ring(4) core Φ = 4; pool(4) core Φ = 12.

## H2 — Φ mass on discrete landmarks

Across all primary n=4 ensemble samples, ≥ 90% of core Φ values round to the
n=4 landmark set {2, 4, 6, 12}. Null: a continuous fill of the (4, 12) gap
(≥ 10% off-landmark).

## H3 — triadic rate is ensemble-dependent

Triadic rate of ER(p=0.3) < fixed_k=2 < fixed_k=3 (the last equals the pool
topology when k=n−1). Null: rates equal within 5 percentage points across those
three.

## H4 — no continuous intermediate band

Among n=4 samples with core Φ strictly between ring (4) and pool (12), either
the count is zero or every such value equals the #19 atom 6.0 (no other
between-band values). Null: some sample with 4 < Φ < 12 and Φ ≠ 6.

## H5 — WS vs ER clustering descriptor

At n=4, mean undirected clustering of WS(p=0.25) exceeds that of ER(p=0.5)
(matched roughly on mean degree band), the classic small-world *descriptor*
contrast. Not a claim that the sample is a Watts–Strogatz network in the
network-science sense — only that the generator leaves a WS-like clustering
footprint relative to ER.
