# Ring-of-hubs with private leaves — findings

**Verdict: FACTORS_NO_COMBINE.** A ring of hubs with private leaves does
**not** combine the ring’s Φ=4 cap with hub growth (Φ=n−1). On this n=6
panel every ring-of-hubs cell either **factors** (incomplete core — often
the three hubs alone at Φ=6) or **collapses**. No full-core hybrid sits
between ring and hub, and none beats hub6 with a full core.

In-silico; binary exact IIT-4.0; n=6. Hypotheses fixed in `hypotheses.md`
before computing. Grows from V3 #5 / V2 #17 `PICK_ONE` / V3 #4
`COMPOSE_LANDMARK_OR_COLLAPSE`. Ternary / residual-cascade / M3 noted only.

## Already known

| prior | result |
|---|---|
| V2 #17 small-world morphs | PICK_ONE — interiors collapse |
| V2 #18 / #19 | discrete landmarks; no log/√n law |
| V3 #4 local-triad necklace | COMPOSE_LANDMARK_OR_COLLAPSE |
| ring / single hub | Φ=4 cap; Φ=n−1 |

## Panel

| cell | structure | core Φ | full core | class |
|---|---|---:|---|---|
| triad | triadic | 2.0 | yes | control |
| ring6 | triadic | 4.0 | yes | landmark |
| hub6 | triadic | 5.0 | yes | landmark |
| roh_leaf_ring | triadic | 6.0 | **no** (hubs) | **FACTOR** |
| roh_hubs_ring | dyadic | 6.0 | no (hubs) | **FACTOR** |
| roh_2h2p | triadic | 3.0 | no | **FACTOR** |
| roh_OR_leaf | triadic | 6.0 | no (hubs) | **FACTOR** |
| roh_directed | triadic | 2.0 | no | **COLLAPSE** |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 controls + landmarks | **SUPPORTED** |
| H2 no combine on roh panel | **SUPPORTED** |
| H3 exclusive landmark \| collapse | **REFUTED** (factor residual) |
| H4 no combine; all cells classified | **SUPPORTED** |

## Reading

Ring geometry plus private leaves does not yield a hybrid law. Integration
stays in the hub ring (Φ=6 on {H0,H1,H2} in several cells) while private
leaves fall out of the major complex — **factoring**, not combining.
Directed / broken ring collapses locally. Same family as V2 #17 and V3 #4:
composed or morph topologies do not invent an intermediate ring–hub law.

Validation gap: Boolean models, not organizations.

## Best next (V3)

V3 #6 (k>2 triads sharing one mediator — Φ scaling), or V3 #1 (n=4
dual-mediator template census).

## Reproduce

```
python org_frontier/studies/ring_of_hubs/analyze_ring_of_hubs.py
```
