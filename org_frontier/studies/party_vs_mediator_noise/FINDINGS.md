# Party vs mediator noise — findings

**Verdict: SAME_THRESHOLD_DIFF_CURVE.** Party-column and
mediator-column flip-noise collapse the triad at the **same** p*=0.5
on both hub families. The seat still matters: Φ curves separate
(conjunctive max |ΔΦ|=0.924 = **46%** of Φ(0); parity **64%**), and on
the conjunctive hub party noise shrinks the major complex to
**n_core=2** for all interior p>0 while mediator noise keeps
n_core=3. P1↔P2 overlay exactly (max|ΔΦ|=0).

In-silico; exact IIT-4.0; same forms as #6 (conjunctive + parity n=3);
51-point grid; flip-noise on hub vs P1 (P2 symmetry check).
Hypotheses fixed in `hypotheses.md`. Cited: `commit_noise_phase/`
(#6 SMOOTH_DECAY, pointer only); #27/#38; Q7 prior. Estimation /
construct / omit / ladder closed.

## Thresholds and gaps

| family | p*_mediator | p*_party | max‖Φ_p−Φ_m‖ / Φ(0) | interior n_core differ? |
|---|---:|---:|---:|---|
| conjunctive_hub | 0.50 | 0.50 | 0.462 | **yes** (3 vs 2) |
| parity_hub | 0.50 | 0.50 | 0.641 | no |

## Selected points (conjunctive)

| p | Φ_med | Φ_P1 | n_med | n_P1 |
|---:|---:|---:|---:|---:|
| 0.00 | 2.000 | 2.000 | 3 | 3 |
| 0.10 | 1.189 | 0.763 | 3 | 2 |
| 0.25 | 0.500 | 0.439 | 3 | 2 |
| 0.49 | 0.011 | 0.015 | 3 | 2 |
| 0.50 | 0 | 0 | 0 | 2 |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 thresholds differ (≥0.02) | **REFUTED** |
| H2 same threshold both families | **SUPPORTED** |
| H3 Φ/n_core differ at same p* | **SUPPORTED** |

## Reading

Collapse threshold is locus-blind on this panel — both seats hold the
verdict to the coin-flip endpoint, extending #6’s SMOOTH_DECAY reading.
Magnitude and core membership are locus-sensitive: party noise on the
conjunctive hub peels a party out of the major complex while Φ still
tracks a smooth decay to the shared flip. Designed witnesses: both
hubs; P1/P2 automorphism.

## Limits

n=3; single-party locus (not joint WC); state-by-node flip-noise only
(#5 is correlated TPM). No organization measured.

## Best next experiment

Prefer agenda **#8** (parity vs conjunctive verdict loss under noise) —
both families already on this panel. Alternate **#5** (correlated TPM)
or **#9** (timescale separation). Do not reopen estimation / construct /
omit / ladder.

## Reproduce

```
python org_frontier/studies/party_vs_mediator_noise/analyze_locus.py
```
(~60 s)
