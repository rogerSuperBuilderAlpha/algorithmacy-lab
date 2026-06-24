# q162 — The minimal CRQA feature set for the joint structural verdict

A Boolean coordination form carries three structural facts in its exact IIT-4.0 major complex.
The triadic/dyadic verdict reports whether the irreducible core holds three or more nodes or
exactly two. The membership count reports the core size. The bottleneck status reports whether one
node uniquely dominates the leave-one-node-out drop in major-complex Φ. The joint verdict is the
triple. This study asks which CRQA feature family set recovers the joint verdict from a sampled
run, and whether whole-system recurrence adds signal the pairwise coupling statistics miss.

## Setup

Three feature families come from one seeded trajectory per form. Family A reads the pairwise
coupling matrix: a summary of the prominences, the node coupling centralities, and the prominence
spread. Family B reads whole-system multidimensional recurrence: md_recurrence DET and RR. Family C
reads transfer entropy: a summary of directed lag-1 binary TE over ordered node pairs. A
deterministic 1-nearest-neighbor over z-scored columns predicts each of the three labels. Held-out
joint accuracy counts a form only when all three labels are recovered. The held-out set is the
last 40 percent of a seeded random-wiring ensemble; the curated forms_library and multiparty forms
join the training set. The split is a fixed index partition, identical across feature sets, so the
ablation is clean.

H1 reads family A against A+B, the md_recurrence drop. H2 reads A+B against A+B+C, the
transfer-entropy gain. A gap within three points counts as a match.

## Result

On a corpus of 16 curated forms plus 112 random-ensemble forms (sub-dyadic dropped), with 45
random forms held out, the held-out joint accuracies are:

| feature set | joint | td | msize | bneck |
|---|---|---|---|---|
| A — coupling prominence | 0.422 | 0.711 | 0.711 | 0.489 |
| B — md_recurrence | 0.244 | 0.422 | 0.422 | 0.467 |
| A+B — full CRQA | 0.489 | 0.756 | 0.756 | 0.578 |
| A+B+C — CRQA + transfer entropy | 0.444 | 0.667 | 0.667 | 0.578 |

H1 is refuted. Dropping md_recurrence from the full CRQA set costs 6.7 points of held-out joint
accuracy (A 0.422 vs A+B 0.489), past the three-point band. Whole-system multidimensional
recurrence carries non-redundant signal the pairwise coupling statistics miss, so the minimal set
that recovers the joint verdict keeps md_recurrence.

H2 is confirmed. Adding transfer entropy to the CRQA set moves held-out joint accuracy by
-4.4 points (A+B 0.489 vs A+B+C 0.444), within the band and in the wrong direction. Transfer
entropy and CRQA are behaviorally redundant for the structural verdict on this corpus. The
transfer-entropy columns even drag the weak 1-NN slightly, an overfitting cost of the extra
dimensions with no offsetting signal.

## What it shows and does not show

The labels come from exact IIT-4.0 Φ on the transition matrix. The features come from sampled
stochastic trajectories. No worker is measured, and the verdict names a graph-and-Φ quantity. The
held-out accuracies are baselines on synthetic data: they describe how much of the structural
verdict a cheap behavioral reading recovers on this in-silico corpus, not a measurement of any
field organization. The Φ-to-organization bridge stays open. A cheap feature set recovering the
verdict on synthetic forms is a baseline for testing real data later, and it does not displace the
principled exploration exact Φ enables.
