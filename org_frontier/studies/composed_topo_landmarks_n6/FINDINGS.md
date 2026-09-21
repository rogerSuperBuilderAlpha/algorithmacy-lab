# Composed-topology landmarks at n≥6 — findings

**Verdict: LANDMARKS_HOLD_NGT6.** V3 #4–#7’s composed-topology class
families remain **discrete** at n≥6 under a denser random-AND draw: all
28 lean samples land on L6 (on_landmark=1.0; interstitial empty).
Designed densify/lifts keep the class family — hybrid closure, roh
factor, necklace compose — with chord densify morphing Φ=4→2 **inside**
L6, not inventing a new atom.

In-silico; binary exact IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Answers `RESEARCH_AGENDA_V4` #10. Extends V3 #4–#7 and V2 #18 past the
n=4 random-coupling window.

## Already known

| prior | result |
|---|---|
| V3 #4 local-triad necklace | COMPOSE_LANDMARK_OR_COLLAPSE (AND Φ=4 full) |
| V3 #5 ring-of-hubs | FACTORS_NO_COMBINE (hubs Φ=6 incomplete) |
| V3 #6 shared-mediator k | SCALE_2K_OR_REFUSES (AND Φ=2k) |
| V3 #7 hybrid FF+recurrent | CLOSURE_HOLDS_HYBRID (AND core recurrent) |
| V2 #18 random coupling | DISCRETE_LANDMARKS at n=4 (n=6 deferred) |

## Regime

| cell | method | note |
|---|---|---|
| V3 #4–#7 controls | committed panels | H1 |
| hybrid / necklace / roh n=6 densify | exact major complex | H2 |
| random AND n=6 N=28 | fixed_k∈{2,3} + ER p=0.35 | H3–H4 |
| n≥8 motif lifts | out of lean | cost; document only |

L6 = {2, 3, 4, 5, 6, 8, 9, 12, 30}.

## Panel

### V3 controls (reproduce)

| family | landmark class | Φ | full |
|---|---|---:|---|
| #4 neck_AND | compose | 4 | yes |
| #4 neck_OR_hub | collapse | 2 | no |
| #5 roh_leaf_ring | factor | 6 | no |
| #6 k2_AND / k3_AND | scale 2k | 4 / 6 | yes |
| #7 hy_triad_AND | closure | 2 (W\|S\|C) | — |

### Designed densify / lifts (n=6)

| cell | core Φ | full | class |
|---|---:|---|---|
| hy_n6_AND | 2 | no (W\|S\|C) | **closure holds** |
| hy_n6_OR | 2 | no (H1\|P1) | relocate (same as V3) |
| neck_AND | 4 | yes | **compose** |
| neck_AND_chord | **2** | yes | morph inside L6 |
| roh_leaf_ring | 6 | no (hubs) | **factor** |
| roh_dense_leaf | 6 | no (hubs) | **factor** |

### Random n=6 (N=28)

| Φ | count | on L6 |
|---:|---:|:---:|
| 2.0 | 14 | yes |
| 3.0 | 3 | yes |
| 4.0 | 2 | yes |
| 5.0 | 1 | yes |
| 6.0 | 8 | yes |
| other | **0** | — |

**on_landmark = 1.000.** interstitial = [].

## Hypotheses

| hypothesis | result |
|---|---|
| H1 V3 #4–#7 controls reproduce | **SUPPORTED** |
| H2 designed lifts keep class family | **SUPPORTED** |
| H3 random ≥90% on L6 | **SUPPORTED** (100%) |
| H4 no interstitial in lean random | **SUPPORTED** |

## Reading

**#10 hold or interstitial?** Hold. Denser random-AND at n=6 does not
paint a continuum between composed landmarks; it resamples the same
discrete L6 atoms V2 #18 / V3 #4–#7 already named. Designed densify
preserves class families: closure, factor, and compose survive; the
necklace chord softens Φ=4→2 without leaving L6. Exact n≥8 motif lifts
remain out of lean scope (cost), so this cell adjudicates the discrete-
landmark claim under denser n=6 coupling, not every large-n compose
geometry.

**Limits.** Conjunctive AND random generators; N=28 lean; standard
motif densify only; no organization measured.

## Best next

**V4 #11** — graded / continuous party channel on the joint-observation
cliff.

## Reproduce

```
python org_frontier/studies/composed_topo_landmarks_n6/analyze_composed_n6.py
```
(loads committed controls + lifts + random; `--rebuild-lifts` ~4 min;
`--rebuild-random` ~25–40 min)
