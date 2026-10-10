# Ergodic richness vs Φ on the strict-mediation census (B5)

On the complete strict-mediation family at n=3, does whole-form Φ_MIP
rank-correlate with basin entropy or with the number of attractors?

Track home: [`../../ergodicity/`](../../ergodicity/). Designed-panel predecessor:
[`../ergodic_components_vs_phi/`](../ergodic_components_vs_phi/) (B1–B3, run;
`NO_ERGODIC_SIGNATURE`).

## Status

**RUN.** Results in `results/forms.csv` and [`FINDINGS.md`](FINDINGS.md).
Verdict `NO_ENSEMBLE_LINK`. H1 and H2 refuted under |ρ| ≥ 0.20. H3
supported on the class-mean entropy gap. Hypotheses committed before the
analysis script existed (`67f408ee`, then `12954695`).

## Question (one line)

Across all 256 strict-mediation three-node forms, is exact Φ_MIP positively
rank-correlated with basin entropy and with attractor count, past a
pre-registered margin and a permutation null?

## Run

```
python org_frontier/studies/ergodic_ensemble_richness/analyze_ensemble.py
```
