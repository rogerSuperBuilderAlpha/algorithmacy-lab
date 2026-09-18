# Parity vs conjunctive under noise — findings

**Verdict: SAME_P_STAR.** At matched n=3 and n=4, parity and
conjunctive hubs lose the triadic verdict at the **same** p*=0.5 under
hub flip-noise. Parity does **not** flip earlier, and it does **not**
shed normalized Φ faster — the conjunctive hub is below parity on
Φ̂=Φ/Φ(0) at **49/49** interior points (mean Φ̂_c−Φ̂_p = −0.133 at n=3,
−0.239 at n=4). Small clean Φ (2^(2−n)) is not a fragility certificate.

In-silico; exact IIT-4.0; hub-column flip-noise as in #6/#7;
N=4 designed forms (2 families × 2 sizes) × 51-point grid. Hypotheses
fixed in `hypotheses.md`. Cited: #6 SMOOTH_DECAY, #7
SAME_THRESHOLD_DIFF_CURVE (pointers only); #115; Q8 prior.
Estimation / construct / omit / ladder closed.

## Thresholds and normalized decay

| n | p*_conj | p*_parity | parity Φ̂ lower | conj Φ̂ lower | mean(Φ̂_c−Φ̂_p) |
|---:|---:|---:|---:|---:|---:|
| 3 | 0.50 | 0.50 | 0/49 | **49/49** | −0.133 |
| 4 | 0.50 | 0.50 | 0/49 | **49/49** | −0.239 |

## Selected points (n=3)

| p | Φ_conj | Φ̂_c | Φ_par | Φ̂_p |
|---:|---:|---:|---:|---:|
| 0.00 | 2.000 | 1.000 | 0.500 | 1.000 |
| 0.10 | 1.189 | 0.594 | 0.382 | 0.763 |
| 0.25 | 0.500 | 0.250 | 0.219 | 0.439 |
| 0.49 | 0.011 | 0.006 | 0.007 | 0.015 |
| 0.50 | 0 | 0 | 0 | 0 |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 parity flips earlier (≥0.02) | **REFUTED** |
| H2 same p* at n=3 and n=4 | **SUPPORTED** |
| H3 parity faster Φ̂ at same p* | **REFUTED** (direction inverted) |

## Reading

Verdict robustness to commit noise until the coin-flip endpoint is
shared across the small-Φ parity family and the Φ=n−1 conjunctive
family. Relative speed lives in magnitude only, and there the
prediction flips: conjunctive sheds the larger fraction of clean Φ.
Designed witnesses: both hubs at n=3 and n=4.

## Limits

Hub-column flip-noise only; n≤4; no party-locus re-open (#7). No
organization measured.

## Best next experiment

Done: #9 **FACTORS_LIKE_62** (`timescale_separation/`). Prefer agenda
**#10** (commit→response delay). Alternate **#5** correlated TPM. Do
not reopen estimation / construct / omit / ladder.

## Reproduce

```
python org_frontier/studies/parity_vs_conjunctive_noise/analyze_families.py
```
(~60 s)
