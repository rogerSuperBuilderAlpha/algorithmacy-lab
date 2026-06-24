# q162 — Findings

The minimal CRQA feature set for the joint structural verdict keeps whole-system recurrence. On a
pooled corpus of curated forms plus a seeded random-wiring ensemble, a deterministic 1-nearest-
neighbor predicts the joint verdict (triadic/dyadic, membership count, bottleneck status) from each
feature set on one fixed held-out split.

## Held-out joint accuracy by feature set

| feature set | joint | td | msize | bneck |
|---|---|---|---|---|
| A — coupling prominence | 0.422 | 0.711 | 0.711 | 0.489 |
| B — md_recurrence | 0.244 | 0.422 | 0.422 | 0.467 |
| A+B — full CRQA | 0.489 | 0.756 | 0.756 | 0.578 |
| A+B+C — CRQA + transfer entropy | 0.444 | 0.667 | 0.667 | 0.578 |

Corpus: 16 curated forms plus 112 random-ensemble forms (sub-dyadic dropped); train 83, held-out
test 45 random forms (triadic 5/45, unique-bottleneck 27/45, msize classes {2, 3}).

- md_recurrence drop (A+B minus A) = 0.067 (6.7 points)
- transfer-entropy gain (A+B+C minus A+B) = -0.044 (-4.4 points)

## Verdicts

**H1 REFUTED.** Coupling prominence alone trails the full CRQA set by 6.7 points, past the
three-point band. Whole-system multidimensional recurrence carries non-redundant signal the
pairwise coupling statistics miss, so the minimal set that recovers the joint verdict includes
md_recurrence rather than coupling prominence alone.

**H2 CONFIRMED.** Adding transfer-entropy features moves held-out joint accuracy by -4.4 points,
within the three-point band and in the wrong direction. Transfer entropy adds no held-out
joint-accuracy gain beyond CRQA on this corpus, so CRQA and transfer entropy are behaviorally
redundant for the structural verdict here.

The instrument control passes: the faithful worker-system-counterpart triad reads triadic with
max_phi 2.0, full {W, S, C} core (msize 3), and the mediator S as the coupling-centrality argmax.

## Scope

Exact IIT-4.0 Φ on small synthetic Boolean coordination forms. No worker is measured. The
classifier is a deterministic 1-NN, weak by design, so the gaps read as a relative ablation on a
fixed estimator, not absolute ceilings. Every accuracy is a baseline on synthetic data, and the
Φ-to-organization bridge is open.
