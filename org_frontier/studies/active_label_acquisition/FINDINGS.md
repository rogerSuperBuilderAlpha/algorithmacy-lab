# Active label acquisition — findings

**Verdict: AL_NO_GAIN.** On the spectral+coupling panel (N=36 exact Φ
labels), no acquisition policy beats random by the pre-registered
pooled bar. Uncertainty’s mean AUC after seed is **0.901** vs random
**0.886** (Δ=+0.015 < 0.05); labels-to-AUC≥0.85 are 8 vs 6. Under
family holdout, topo_balance does not help — mid-budget AUC **0.518**
vs uncertainty **0.690**. Label order is secondary on this panel;
the topology bottleneck from [`ESTIMATION_ARC.md`](../../ESTIMATION_ARC.md)
stands.

In-silico; exact IIT-4.0 oracle labels reused from
`spectral_invariant/results/panel.csv`; logistic surrogate on 11
spectral+coupling features. Hypotheses fixed in `hypotheses.md`.
Construct/omit/ladder/indeg closed.

## Label-efficiency (pooled holdout)

| policy | mean AUC (>seed) | labels to AUC≥0.85 |
|---|---:|---:|
| random | 0.886 | **6** |
| uncertainty | 0.901 | 8 |
| topo_balance | 0.880 | 6 |
| diversity | 0.854 | 12 |

Seed = 4 labeled; ~24/12 stratified holdout; 20 seeds.

## Topology holdout (usable: chain, majority, single_hub)

| policy | AUC @ mid (n≈17) | mean AUC (>seed) |
|---|---:|---:|
| uncertainty | **0.690** | 0.671 |
| diversity | 0.601 | 0.545 |
| random | 0.590 | 0.586 |
| topo_balance | 0.518 | 0.592 |

Uncertainty leads mid-budget under LOFO but does not clear pooled H1.
Topo-aware acquisition **hurts** relative to margin sampling.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 uncertainty ≻ random (pooled Δ≥0.05 or labels ≤0.80×) | **REFUTED** |
| H2 topo_balance ≻ uncertainty (LOFO mid Δ≥0.05) | **REFUTED** |
| H3 no policy beats random by ≥0.03 pooled | **SUPPORTED** |

## Reading

Active learning does not unlock a privileged labeling order that
repairs cross-topology generalization. Within the pooled panel the
cheap features already discriminate well after a few random labels;
margin and family-balance sampling add little. Under holdout,
forcing family balance under-samples the margin cases that help, and
uncertainty’s LOFO edge stays an observation outside H1. Practice
stays family-matched cheap screens plus selective exact Φ — not a
smarter acquisition loop on this corpus.

## Limits

N=36 designed forms; only three mixed-class families for LOFO; logistic
(not RF) for fit budget; simulated acquisition on a fixed labeled panel.
No organization measured.

## Best next experiment

**Estimation lane closable.** Working picture in
[`ESTIMATION_ARC.md`](../../ESTIMATION_ARC.md) is stable after #21–#23
and #25: topology is the bottleneck; sample length, GNN-style
structure, spectral gap, and label order are not the missing lever.
Optional later (outside this lane): agenda **#24** partial observation.
Do not reopen construct/omit/ladder.

## Reproduce

```
python org_frontier/studies/active_label_acquisition/analyze_active.py
```
(~2 min)
