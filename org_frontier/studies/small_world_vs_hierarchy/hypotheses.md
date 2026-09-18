# small_world_vs_hierarchy — hypotheses (fixed before computing)

**Question (agenda #17).** At fixed n, does rewiring a ring toward hubs
**combine** the ring's size-independent Φ cap (#132 / q143: Φ = 4 for n ≥ 4)
with a hub's growth (single_hub Φ = n−1), or **pick one**?

**Already known (cited, not reopened).**
- **#132 / q143:** conjunctive ring — triadic; Φ = 4.0 size-independent for n ≥ 4.
- **single_hub / #116:** Φ = n−1 (grows with n).
- **q146:** Watts–Strogatz *random* rewiring of a ring lowers Φ monotonically;
  no small-world peak. Disorder destroys integration.
- **q150:** one chord keeps Φ = 4.0 (redistributes Shapley; no raise).
- **`mediator_hierarchy_census`:** recurrent breadth grows Φ; feedforward top-local.
- **`spanning_mediator_multihub`:** spanning top does not beat the pool; recurrent
  hub-span merges membership. Ternary / residual-cascade noted only.

**Gap.** q146 rewires toward *random* shortcuts. #17 asks for rewires *toward
hubs* and for an explicit combine-vs-pick-one verdict against the ring-cap /
hub-growth pair, including a size contrast (n=5 vs n=6) where hub Φ exceeds the
ring cap. Hierarchy is the named contrast family (breadth growth without ring
geometry).

**Universe.** Binary exact IIT-4.0. Conjunctive AND. Primary morph at n ∈ {5,6};
in-degree-preserving hub-targeted rewires at n=5 (exact-Φ feasible). Candid:
n=6 cells are slow (~40–50s each at endpoints).

## Architectures

| cell | construction |
|---|---|
| ring(n) | each node = AND of two ring neighbours (cap baseline) |
| single_hub(n) | hub = AND(all parties); parties copy hub (growth baseline) |
| morph(n,k) | k parties hub-gated (P'=H); hub = AND(those k); remaining nodes keep ring AND; k=0→ring, k=n−1→hub |
| hub_rewire(n,r) | ring; r non-hub nodes each replace one ring input with hub 0 (in-degree 2 preserved) |
| hierarchy star | recurrent tree d=1, b=n−1 (apex AND leaves; leaves read apex) — hierarchy contrast at n=5 |

**Combine** = some interior morph/rewire cell has core Φ strictly between ring(n)
and hub(n) when those differ, *or* exceeds the ring cap while staying below hub,
with a triadic full-core reading. **Pick one** = interiors match an endpoint or
factor below both; only pure ring / pure hub recover their family laws.
**Neither** = even endpoints fail to replicate.

## H1 — instrument + family anchors

Faithful triad control. ring(5)=ring(6)=4.0 (size-independent cap).
single_hub(5)=4.0, single_hub(6)=5.0 (growth). morph endpoints equal the
matching baselines.

## H2 — interiors do not combine

On every interior morph cell (0 < k < n−1) at n=5 and n=6, core Φ is **not**
strictly between ring(n) and hub(n) under a triadic full-core reading. Null:
some interior combines (between / partial raise with full core).

## H3 — interiors collapse below both anchors

Every interior morph cell has whole structure dyadic **or** core Φ ≤ min(ring,
hub) with incomplete core. (Collapse / factor, not a hybrid law.)

## H4 — pick-one across the size contrast

At n=6 (where hub Φ > ring Φ), no interior morph cell reaches hub Φ = 5.0 or
sits in (4, 5). Endpoints alone realize cap vs growth. Verdict: **PICK_ONE**
(not COMBINE).

## H5 — in-degree-preserving hub rewires also fail to combine (n=5)

On hub_rewire(5, r) for r=1..3, no cell exceeds ring Φ = 4.0 with a new hybrid
law; light rewire either holds the ring or drops below it (q146 direction,
hub-targeted).
