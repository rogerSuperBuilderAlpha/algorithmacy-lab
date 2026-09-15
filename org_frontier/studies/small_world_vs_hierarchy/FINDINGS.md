# Small-world rewire vs hierarchy — findings

**Verdict: PICK_ONE.** Rewiring a ring toward hubs does **not** combine the
ring's size-independent Φ = 4 cap with hub growth (Φ = n−1). Interior morphs
**collapse** (dyadic, incomplete cores). Only the pure ring and the pure hub
recover their family laws. Hub-targeted in-degree-preserving rewires either
hold the ring briefly or drop below it — same direction as q146's random WS.

In-silico; binary exact IIT-4.0; n ∈ {5,6}. Hypotheses fixed in `hypotheses.md`.
Extends q146 / #132 / q143; cites hierarchy census and spanning multi-hub WIN.
Ternary TOOLING_GAP / residual-cascade noted only.

## Already known

| prior | result |
|---|---|
| #132 / q143 ring | Φ = 4.0 size-independent for n ≥ 4 |
| single_hub | Φ = n−1 (grows) |
| q146 random WS | Φ falls monotonically; no small-world peak |
| q150 one chord | Φ stays 4.0 |
| hierarchy census | recurrent breadth grows; feedforward top-local |

## Census

| cell | n | whole | core Φ | full core | note |
|---|---:|---|---:|---|---|
| ring | 5, 6 | triadic | **4.0** | yes | size-independent cap |
| single_hub | 5 | triadic | **4.0** | yes | = ring at n=5 |
| single_hub | 6 | triadic | **5.0** | yes | growth |
| morph interiors (k=1..n−2) | 5, 6 | **dyadic** | 2–4 | **no** | collapse |
| hub_rewire r=1 | 5 | triadic | 4.0 | yes | still ring |
| hub_rewire r=2,3 | 5 | triadic | 2.0 | no | below ring |
| hierarchy star d=1 | 5 | triadic | 4.0 | yes | = hub / ring at n=5 |

At n=6, where hub Φ exceeds the ring cap, no interior morph sits in (4, 5) or
reaches 5.0 with a full core.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 anchors + morph endpoints | **SUPPORTED** |
| H2 interiors do not combine | **SUPPORTED** |
| H3 interiors collapse | **SUPPORTED** |
| H4 pick-one at n=6 size contrast | **SUPPORTED** |
| H5 hub-rewire ≤ ring at n=5 | **SUPPORTED** |

## Reading

**Combine?** No. There is no hybrid law that keeps the ring's flat Φ = 4 while
borrowing hub growth. Partial hub-gating factors the system: the major complex
shrinks to the hub plus converted parties at Φ ≈ core size − 1 (or 2), and the
whole reads dyadic.

**Pick one?** Yes — at the endpoints only. Pure ring → cap. Pure hub → n−1.
The recurrent hierarchy star at n=5 matches the hub (same conjunctive star),
not a third intermediate.

**vs q146.** Random WS lowers Φ from the ring. Hub-targeted rewiring does the
same once enough spokes are bent: the ring is fragile to partial hub-ization,
not a path that climbs toward hub Φ.

## Limits

Exact Φ through n=6. Morph changes hub in-degree (AND of k parties); the
in-degree-2 hub_rewire ladder is the degree-preserving check at n=5 only.
No organization measured.

## Best next experiment

**Interior topology between ring and pool** (agenda #19): is there a law
between the ring's Φ = 4 cap and the pool's n(n−1) — logarithmic or
square-root in n — or only the known family endpoints?

## Reproduce

```
python org_frontier/studies/small_world_vs_hierarchy/analyze_small_world.py
```
(~2.5 min; n=6 ring/hub dominate)
