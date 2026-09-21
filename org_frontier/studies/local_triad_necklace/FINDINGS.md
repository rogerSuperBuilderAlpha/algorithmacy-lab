# Local-triad necklace — findings

**Verdict: COMPOSE_LANDMARK_OR_COLLAPSE.** Composing three local conjunctive
triads on a cycle does **not** invent a new Φ law. The closed AND necklace
recovers the **ring landmark** (full six-node core, Φ=4.0). OR-hub, OR-party,
and directed-read variants **collapse** (dyadic whole or incomplete core at
Φ=2). Composition on this panel picks a known landmark or collapses — the same
family of outcomes as V2 #17 `PICK_ONE` / #18 `DISCRETE_LANDMARKS` / #19
`NO_INTERMEDIATE_LAW`, not a sixth topology law.

In-silico; binary exact IIT-4.0; n≤6. Hypotheses fixed in `hypotheses.md`
before computing. Grows from V3 #4 / V2 #16–#19. Ternary / residual-cascade /
M3 noted only.

## Already known

| prior | result |
|---|---|
| V2 #16 shared-mediator AND | merges; five-node core Φ=4.0 |
| V2 #17 small-world morphs | PICK_ONE — interiors collapse |
| V2 #18 random couplings | DISCRETE_LANDMARKS |
| V2 #19 ring–pool interiors | NO_INTERMEDIATE_LAW |
| ring / single hub | Φ=4 cap; Φ=n−1 |

## Panel

| cell | structure | core Φ | full core | note |
|---|---|---:|---|---|
| triad | triadic | 2.0 | yes | control |
| ring6 | triadic | 4.0 | yes | landmark |
| hub6 | triadic | 5.0 | yes | landmark |
| mh6_m3 | triadic | 12.0 | no | multi-hub contrast |
| shared_S_AND | triadic | 4.0 | yes | #16 merge ref |
| **neck_AND** | **triadic** | **4.0** | **yes** | **= ring landmark** |
| neck_OR_hub | dyadic | 2.0 | no | collapse |
| neck_OR_party | dyadic | 2.0 | no | collapse |
| neck_directed | triadic | 2.0 | no | collapse (local dyad) |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 controls + landmarks + shared-S Φ=4 | **SUPPORTED** |
| H2 AND necklace = landmark, not new law | **SUPPORTED** |
| H3 OR/directed necklaces collapse | **SUPPORTED** |
| H4 no new compose law on panel | **SUPPORTED** |

## Reading

Local-triad composition on a cycle is not a new integration law. Closing the
AND necklace is structurally a ring in Φ (Φ=4, full core). Breaking symmetry
(OR on hubs or parties; directed primary-hub read) returns the collapse mode
already seen when morphing between ring and hub. Shared-mediator merge (#16)
remains a different motif: one global integrator, not a cycle of local ones.

Validation gap: evidence about Boolean models, not about real organizations.

## Best next (V3)

V3 #5 ring-of-hubs with private leaves, or V3 #1 n=4 dual-mediator template
census. Do not reopen V2 #15–#20.

## Reproduce

```
python org_frontier/studies/local_triad_necklace/analyze_necklace.py
```
