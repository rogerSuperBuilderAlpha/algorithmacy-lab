# q162 — Review notes

## What the probe establishes

The probe compares four feature sets on one fixed held-out split for recovering the joint
structural verdict (triadic/dyadic, membership count, bottleneck status). The two ablation reads
are the md_recurrence drop (A vs A+B) and the transfer-entropy gain (A+B vs A+B+C). The instrument
control passes: the faithful triad reads triadic, max_phi 2.0, full core, mediator-as-centrality.

H1 is refuted: the md_recurrence drop is 6.7 points (A 0.422 vs A+B 0.489), past the three-point
band, so whole-system recurrence is non-redundant against coupling prominence. H2 is confirmed:
the transfer-entropy gain is -4.4 points (A+B 0.489 vs A+B+C 0.444), within the band, so transfer
entropy adds nothing beyond CRQA here. The held-out base rates are skewed (triadic 5/45,
unique-bottleneck 27/45), so the joint accuracies are modest in absolute terms; the load-bearing
quantities are the two ablation gaps, which are stable to that skew because every feature set runs
the identical split.

## Threats and limits

The corpus is small and synthetic. The random ensemble drives the held-out set; the curated forms
sit in training, so the test distribution is the random-wiring family, not the curated motifs. The
1-NN classifier is deterministic and weak by design: a stronger learner could close or widen any
gap, so the ablation reads as a relative comparison on a fixed estimator, not an absolute ceiling.
The msize and bneck labels are coarsened (count and uniqueness), which keeps the feature vector
n-agnostic but discards which specific node is the bottleneck. A three-point tolerance sets the
match band; a gap near the band edge should be read as inconclusive.

## Scope

Exact IIT-4.0 Φ on synthetic Boolean forms. No worker is measured. Every accuracy is a baseline on
synthetic data. The result speaks to feature redundancy on this in-silico corpus, not to any field
organization, and it does not bear on whether Φ is necessary: a cheap feature set matching the
verdict on synthetic forms is a baseline for later tests on real data.
