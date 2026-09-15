# Unconstrained n=4 holistic residual — findings (F26 asterisk fix)

**Verdict: H2 — the cheap-feature residual grows at n=4 once base rate is controlled.** On N=1000
unconstrained k=2 n=4 forms (seed 40), Probe-131 RF miss rate = **7.5% (75/1000)**, above the
pre-registered hold band [3.3%, 6.3%] and **+2.7 pp** over the n=3 baseline of 4.8%. The forest
predicts both classes (H3 supported) — the F26 strict-mediation failure mode is gone.

In-silico; exact IIT-4.0 Φ. Hypotheses fixed in `hypotheses.md` before computing. F27 not reopened.

## Why this universe

| candidate | triadic rate | issue |
|---|---|---|
| F26 strict-mediation n=4 | 2.4% | RF never predicted triadic (majority floor) |
| Full 3-input unconstrained n=4 | ~93% | inverts the asterisk (always-triadic floor) |
| **k=2 unconstrained n=4 (this study)** | **29.7%** | Probe-131 analogue; both classes learnable |

At n=3 the 4096 panel has each node read the other two (k=2 of 2). The n=4 lift keeps k=2: each
node reads two randomly chosen others. Full k=3 coupling is too dense for a residual comparison.

## Census table

| quantity | n=3 Probe 131 | F26 SM n=4 | **this study (unc k=2)** |
|---|---|---|---|
| N | 4096 | 3000 | **1000** |
| triadic rate | 55.9% | 2.4% | **29.7% (297)** |
| RF miss rate | **4.8%** | 2.4% | **7.5% (75)** |
| majority-class miss | — | 2.4% | 29.7% |
| predicted triadic / dyadic | — | 0 / 3000 | **312 / 688** |
| FP / FN | — | 0 / 71 | **45 / 30** |
| miss among triadic / dyadic | — | 100% / 0% | **10.1% / 6.4%** |
| near-boundary among misses | 0.91 | 0.38 | **0.56** |
| F26 band verdict | — | H1 shrinks\* | **H2 grows** |
| H3 (both classes predicted) | — | failed | **SUPPORTED** |

\*F26 shrink equaled the majority floor and does not survive base-rate control.

## Reading

The F26 SM result was an asterisk, not a size law. With triadicity common enough for the forest to
call both classes, the unreachable fraction **rises** from 4.8% at n=3 to 7.5% at n=4. Errors are
two-sided (45 FP, 30 FN), and miss rates within each class are modest (10% / 6%), so the residual is
a real cheap-feature ceiling, not a rare-class collapse. Relative to the majority floor (29.7%), the
panel still captures most of the verdict — the last 7.5% stays holistic.

Panel build: ~263s for N=1000 exact Φ on this host.

## Best next experiment

Section F's rate question at n=4 is settled under base-rate control (grows). Natural next:
**unconstrained k=2 residual at n=5** (does growth continue?), or characterize the n=4 residual set
(near-boundary / F28-style perturbations on the 75 misses). Agenda G remains open for a different
gap.

## Reproduce

```
python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py
python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py --rebuild
```
