# Margin-cascade selective exact Φ — findings

**Verdict: WIN.** A margin-cascade — Probe-131 cheap RF as screen, exact IIT-4.0 Φ only on
out-of-fold uncertain forms — cuts FN-among-triads sharply at fixed exact-Φ budget.
On n=4 unc at **B=10%** (100 exact calls): FN|tri **10.1% → 3.7%** (−6.4 pp); miss
**7.5% → 3.2%**. At **B=20%**: FN|tri **0.7%**, recovering **93%** of the gap to
always-exact. Margin gating beats matched-budget random; **struct_fragility does not
add** gating value over `|p−0.5|` (H4 REFUTED). n=5 validates (24.7% → 10.6% at B=10%).

In-silico; unc k=2. Hypotheses fixed in `hypotheses.md` before computing. Size series
4.8% → 7.5% → 9.0%, F28, and the FN-redesign honest null are cited, not reopened. Exact Φ
is ground truth on the called subset; cheap OOF predictions elsewhere.

## Protocol

RF(400, seed 0) on Probe-125/131 features; gating scores from **5-fold `cross_val_predict`**
(no leakage). Calling exact Φ = substituting the cached `triadic` label. Gates compared:
margin uncertainty `1−2|p−0.5|`, `struct_fragility`, rank-average combined, random
(20 seeds).

## Cost–error curve (n=4 unc, margin gate)

| B | exact calls | miss | FN\|tri | FP\|dya |
|---|---|---|---|---|
| 0% (always-cheap) | 0 | 7.5% | 10.1% (30/297) | 6.4% |
| 5% | 50 | 5.0% | 6.4% | 4.4% |
| **10%** | **100** | **3.2%** | **3.7% (11/297)** | **3.0%** |
| 15% | 150 | 1.7% | 1.7% | 1.7% |
| **20%** | **200** | **0.9%** | **0.7% (2/297)** | **1.0%** |
| 30% | 300 | 0.2% | 0.0% | 0.3% |
| 100% (always-exact) | 1000 | 0.0% | 0.0% | 0.0% |

Random at B=10%: FN|tri mean **9.3%** (margin 3.7% — **+5.6 pp** advantage).
Fragility-only at B=10%: FN|tri still **10.1%** (no help). Combined rank-avg at B=10%:
**6.4%** — worse than margin alone.

## Hypotheses

| hypothesis | result | detail |
|---|---|---|
| H1 B=10% FN\|tri drop ≥5 pp | **SUPPORTED** | −6.4 pp |
| H2 B=20% recover ≥60% of FN gap | **SUPPORTED** | 93.3% |
| H3 margin beats random ≥3 pp @10% | **SUPPORTED** | +5.6 pp |
| H4 combined beats margin ≥2 pp @10% | **REFUTED** | −2.7 pp (combined worse) |
| H5 n=5 B=10% FN drop ≥5 pp | **SUPPORTED** | −14.1 pp (24.7%→10.6%) |

**Operating point:** B=10% — first pre-registered budget that halves FN|tri (actually cuts
it by ~63%) at one-tenth the exact-Φ cost of always-exact.

## Reading

Misses concentrate near the RF margin, as F28's phase-boundary picture predicted. Selective
exact Φ on that sheet closes most of the FN tail; expanding hand features did not
(`fn_tail_feature_redesign`). Fragility without the probability margin is a poor gate —
local structural instability alone does not rank which cheap errors to buy back.
The cascade is a **compute allocation** result, not a claim that cheap features replace Φ
magnitude.

## Best next experiment

**Done next:** `margin_cascade_tau/` — nested τ ≈ top-B% on n=4; lab default **B=10% top-B%**
(recompute ranks per panel). Frozen τ\* from n4 drifts call rate on n=5 (H2 REFUTED). Follow-on:
wire cascade@10% into the next large unc sweep as dual residual.

## Reproduce

```
python org_frontier/studies/margin_cascade_phi/analyze_margin_cascade.py
```
