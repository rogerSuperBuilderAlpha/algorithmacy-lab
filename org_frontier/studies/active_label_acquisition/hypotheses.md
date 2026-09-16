# active_label_acquisition — hypotheses (fixed before computing)

**Question (agenda #25).** Which forms are most informative to label
first when training a surrogate (active learning over the corpus)?

**Already known (cited, not reopened).**
- Estimation lane: [`ESTIMATION_ARC.md`](../../ESTIMATION_ARC.md) —
  #22 NO_STRUCTURE_GAIN, #23 FAST_WITHIN_FAMILY, #21 SPECTRAL_PARTIAL.
- Bottleneck is topology, not T or GNN-style structure.
- Exact Φ is the oracle; labels are expensive.

**Universe.** Exact binary IIT-4.0 labels already on the
`spectral_invariant` panel (N=36; features = spectral + coupling).
Simulate acquisition; no new Φ compute. Surrogate = logistic
regression on those features (fit budget). Honest N; multiple seeds.

**Acquisition policies.**
- **random** — uniform among unlabeled.
- **uncertainty** — smallest `|p−0.5|` under logistic fit on labeled.
- **diversity** — farthest (euclidean, standardized) from nearest labeled.
- **topo_balance** — prefer underrepresented families; tie-break by
  uncertainty.

**Protocols.**
1. **Pooled holdout:** stratified 24-pool / 12-test; seed 4 labeled;
   acquire until pool exhausted; track test AUC vs n_labeled.
2. **Topology holdout:** each family as fixed test; acquire from other
   families; mean test AUC vs n_labeled.

## H1 — uncertainty beats random (pooled)

Mean test AUC over the budget curve (after seed) for uncertainty
≥ random + **0.05**, or labels to first reach AUC≥0.85 is ≤ **0.80×**
random’s count (when both hit).

Null: neither bar clears.

## H2 — topo_balance beats uncertainty under topology holdout

At mid-budget (half of available train labels), mean LOFO test AUC for
topo_balance ≥ uncertainty + **0.05**.

Null: advantage < 0.05.

## H3 — no policy beats random

All non-random policies stay within **0.03** mean-AUC of random on the
pooled curve (after seed).

Null: some policy clears +0.03 over random.
