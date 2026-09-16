# Spectral topology-invariant feature — findings

**Verdict: SPECTRAL_PARTIAL.** Transfer-operator spectral gap
(`P_spectral_gap`) is the best cross-family ranker on this panel
(**AUC=0.893**, ρ(Φ)=0.669), beating inverted coupling (mean MI
AUC=0.775, orient=−1). Lift **+0.118** clears chance but not the
pre-registered +0.15 H1 bar. No spectral feature fails as hard as
#134’s raw coupling on mono-archetype pools; none fully clears H1.

In-silico; exact IIT-4.0 labels; N=36 designed forms (25 tri / 11 dya)
across 8 families at n∈{3,4,5}. Hypotheses fixed in `hypotheses.md`.
Pointers: #134; `structure_aware_surrogate/` (#22);
`sample_complexity_screen/` (#23). Construct/omit/ladder/indeg closed.

## Ranking (oriented pooled AUC)

| feature | class | AUC | orient | ρ(Φ) |
|---|---|---:|---:|---:|
| **P_spectral_gap** | spectral | **0.893** | + | 0.669 |
| P_second_mod | spectral | 0.860 | − | 0.638 |
| adj_spectral_radius | spectral | 0.849 | + | 0.754 |
| graph_energy | spectral | 0.804 | + | 0.639 |
| mean_mi | coupling | 0.775 | − | 0.597 |
| tc_per_node | coupling | 0.775 | − | 0.594 |
| abs_oinfo | coupling | 0.673 | − | 0.225 |
| lap_gap | spectral | 0.647 | − | 0.373 |
| lap_lambda2 | spectral | 0.636 | + | 0.573 |
| vn_entropy | spectral | 0.518 | + | 0.275 |
| lap_lambda_max | spectral | 0.502 | − | −0.192 |

Coupling’s best orientation is **negative** (high MI → dyadic) — the
#134 inversion signature, softened here by broken/working pairs.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 spectral ranks (AUC≥0.70 and lift≥0.15) | **REFUTED** (AUC ok, lift +0.118 < 0.15) |
| H2 all spectral fail like coupling | **REFUTED** |
| H3 detect not magnitude | **REFUTED** (H1 failed; ρ=0.669 anyway) |

## Reading

A spectral descriptor of the noisy transfer operator **partially**
fills the topology-invariant gap: it ranks better than inverted
coupling and correlates with Φ, without a trained surrogate. It is not
yet a drop-in #122 replacement across families (lift short of H1;
family AUC still spreads). Estimation lane: useful baseline for #25
active learning / stop note — not a closed instrument.

## Limits

Designed N=36; one traj draw (T=2000); oriented AUC (feature or −feature).
No torch GNN. No organization measured.

## Best next experiment

Prefer agenda **#25** (active learning over forms to label) **or stop
the estimation lane** with a short note tying #21–#23: within-family MI
is cheap and fast; cross-topo needs something beyond coupling; spectral
gap is a partial, not sufficient, invariant. Do not reopen
construct/omit/ladder.

## Reproduce

```
python org_frontier/studies/spectral_invariant/analyze_spectral.py
```
(~32 s)
