# interior_ring_pool — hypotheses (fixed before computing)

**Question (agenda #19).** Is there a topology between the ring (Φ capped at 4
for n ≥ 4) and the pool (Φ = n(n−1)) whose law is **logarithmic or square-root
in n**, or do forms jump/collapse between those poles?

**Already known (cited, not reopened).**
- **#132 / q143:** ring Φ = 4.0 size-independent for n ≥ 4.
- **pool / #104 / spanning study:** all-required pool Φ = n(n−1) (12, 20, 30 at
  n=4,5,6).
- **q146 / `small_world_vs_hierarchy`:** random or hub-targeted rewires from a
  ring do **not** combine cap with hub growth — **PICK_ONE**; interiors
  collapse. q150: one chord keeps Φ = 4.0.
- **#119 / sym_multihub:** Φ rises with hub count toward the pool.
- Ternary TOOLING_GAP / residual-cascade noted only.

**Gap.** Small-world asked rewire-from-ring. #19 asks whether any *designed*
interior family (chordal rings, k-regular rings, multi-hub, lattice strip,
partial pools) carries a stable intermediate **scaling law in n** (log / √n),
versus only the two poles or collapse.

**Universe.** Binary exact IIT-4.0. Conjunctive AND. n ∈ {4,5,6}; n=6 cells
trimmed to decisive forms (exact-Φ cost ~45s each).

## Designed families

| family | parameter | poles |
|---|---|---|
| ring / pool | — | lower / upper anchors |
| sym_multihub | m hubs | m=1 ~ hub; m=n−1 ~ pool |
| chordal ring | c opposite chords | c=0 = ring; dense chords → pool-like |
| k-regular ring | degree radius d | d=1 = ring; d=⌊(n−1)/2⌋ = pool |
| lattice strip | 2×(n/2) grid (even n) | between cycle and denser grid |
| partial pool | clique size m < n | collapse control (q146 direction) |

**Intermediate (fixed n):** full-core triadic with ring < core Φ < pool.
**Intermediate law (in n):** for some family, core Φ across n=4,5,6 fits log(n)
or √n better than constant / linear / pole-jump (see H3).
**Collapse:** dyadic or incomplete core below the ring.

## H1 — anchors

Faithful triad. ring(n)=4.0 for n=4,5,6. pool(n)=n(n−1) for n=4,5,6.

## H2 — fixed-n interiors exist (not only poles)

At n=5 or n=6, at least one designed cell (multihub, chordal, k-regular, or
strip) is full-core triadic with ring < Φ < pool. Null: every non-pole cell is
at a pole or collapsed.

## H3 — no log / √n intermediate law

No census family with values at three n's has core Φ proportional to log(n) or
√n (correlation of Φ with log(n) and with √n both fail a strict monotone
match to those shapes against a constant or linear alternative — decision:
SUPPORTED iff no family is better described as log or √n than as stepwise /
linear-in-parameter; specifically, mh_m2 and chord ladders do not track log or
√n across n=4..6). Null: some family matches log or √n.

Operational rule: for each family series with ≥2 full-core points at distinct n,
compute ratios Φ/log(n) and Φ/√n; **log/√n law claimed** only if the ratio is
constant within 10% relative spread across those n **and** Φ is not constant
(ring) and not equal to n(n−1) (pool). H3 SUPPORTED iff no series meets that.

## H4 — partial pools collapse

partial_pool with m < n at n=5 yields dyadic whole or incomplete core (not a
stable intermediate law). Null: some partial pool is full-core between ring and
pool.

## H5 — discrete steps in a topology parameter

At fixed n=6, increasing chord count or k-regular degree (among full-core cells)
raises Φ in steps toward the pool, not a single jump from 4 to 30. Supports
"discrete interior" without a log/√n-in-n law.
