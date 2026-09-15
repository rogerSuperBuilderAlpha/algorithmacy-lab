# FN-tail feature redesign — findings

**Verdict: honest null on pre-registered thresholds (H1–H4 all REFUTED).** Adding
F28-motivated cheap fragility and algebraic table features to the Probe-125/131
panel does not cut the triadic false-negative (FN) rate by the pre-registered 5 pp,
nor the overall miss rate by 1 pp. On n=4 the redesign moves miss 7.5%→7.1% and
FN-among-triads 10.1%→9.8% — directionally tiny, below threshold, and accompanied
by FN-set churn (13 rescued, 12 new). On n=5 FN-among-triads worsens slightly
(24.7%→25.9%). Exact Φ remains the label; magnitude is not claimed.

In-silico; unc k=2 panels. Hypotheses fixed in `hypotheses.md` before computing.
Size series 4.8% → 7.5% → 9.0% and F28 phase-boundary conclusions are cited, not
reopened.

## Characterization (n=4 unc; baseline RF FN vs TP)

| | FN (n=30) | TP (n=267) |
|---|---|---|
| mean \|p−0.5\| | 0.23 | 0.42 |
| n_bidir | 4.0 | 4.0 |
| struct_fragility | **0.75** | 0.66 |
| n_parity | 0.30 | 0.81 |
| n_affine | 1.13 | 1.81 |
| n_reachable | 8.0 | 10.0 |
| max_period | 2.0 | 3.6 |

Missed triads sit nearer the decision boundary, are fully bidirectional, and show
higher structural one-bit fragility — consistent with F28's local-instability
constraint. They are *less* parity/affine-heavy than true positives: the FN tail
is not a parity blind spot. `syn_fragility` is degenerate on this panel (constant
1.0 for every form) and contributes nothing.

## Comparison table

| setting | miss | FN\|tri | FP\|dya | AUC |
|---|---|---|---|---|
| n=4 baseline | 7.5% (75/1000) | 10.1% (30/297) | 6.4% | 0.981 |
| n=4 redesign | 7.1% (71/1000) | 9.8% (29/297) | 6.0% | 0.979 |
| n=5 baseline | 9.0% (45/500) | 24.7% (21/85) | 5.8% | 0.963 |
| n=5 redesign | 9.0% (45/500) | 25.9% (22/85) | 5.5% | 0.967 |
| transfer n4→n5 baseline | 8.6% | **0.0%** (0/85) | 10.4% | 0.958 |
| transfer n4→n5 redesign | 8.8% | **0.0%** (0/85) | 10.6% | 0.969 |

| hypothesis | result | detail |
|---|---|---|
| H1 n4 FN\|tri drop ≥5 pp | **REFUTED** | +0.3 pp |
| H2 n4 miss drop ≥1 pp | **REFUTED** | +0.4 pp |
| H3 n5 FN\|tri drop ≥5 pp | **REFUTED** | −1.2 pp |
| H4 transfer FN drop ≥5 pp | **REFUTED** | 0.0 pp (both FN=0 via over-calling triads) |

Top redesign importances remain the baseline graph/dynamics block
(`strongly_connected`, `n_reachable`, `n_bidir`); among new features only
`dyn_fragility` enters the top eight (~0.08). Hand features that mark
neighborhood instability do not close the FN tail under the same RF protocol.

## Reading

The cheap redesign respects F28's constraint (fragility features) and the FN
characterization (algebraic counts), yet fails the pre-registered win criteria.
Net FN reduction on n=4 is one form; the FN set mostly turns over. Transfer
eliminates FN for *both* feature sets by raising FP among dyads — a calibration
artifact, not an FN-tail cure. Exact Φ remains necessary where the cheap margin
is thin.

## Best next experiment

**Margin-cascade / selective exact Φ:** keep the Probe-131 cheap RF as a screen;
run exact IIT-4.0 Φ only on forms with low \|p−0.5\| (or high `struct_fragility`).
Pre-register the abstention band and the Φ budget; primary metric = FN-among-triads
at fixed exact-Φ call count vs always-cheap and always-exact baselines. Hand-feature
expansion is closed for this FN tail; the next lever is *when* to call exact Φ,
not which cheap column to add.

## Reproduce

```
python org_frontier/studies/fn_tail_feature_redesign/analyze_fn_redesign.py
python org_frontier/studies/fn_tail_feature_redesign/analyze_fn_redesign.py --rebuild  # ~25s, no exact Φ
```
