# Findings: which candidate Φ measures track exact IIT‑4.0 Φ?

**TL;DR.** Across the same 270 networks used in the proxy audit, the
*theoretically motivated* candidate measures track exact IIT‑4.0 Φ **markedly
better than the empirical proxies** — but still only moderately. The
whole‑minus‑sum Φ and the co‑information "integrated synergy" lead (Spearman
ρ ≈ 0.47 / 0.41, AUC ≈ 0.79 / 0.75), and both **improve with system size**.
Measures of mere statistical dependence — total correlation, time‑delayed mutual
information — *anti*‑correlate with Φ. So the measures that share IIT's
"irreducibility across a partition" structure are the ones that track it; the
ones that only capture coupling do not.

## Main result

270 networks (`n ∈ {3,4}`), 72 with Φ>0, Φ range 0–2.0. Identical ground truth
and ensemble to [`../proxy_audit/`](../proxy_audit/).

| Candidate measure | Spearman ρ | Pearson r | AUC (Φ>0) |
|-------------------|-----:|-----:|-----:|
| **Φ whole‑minus‑sum** | **0.465** | 0.457 | **0.786** |
| **Integrated synergy** (co‑information) | **0.414** | 0.143 | 0.748 |
| Total correlation | −0.355 | −0.136 | 0.278 |
| Time‑delayed MI | −0.211 | 0.142 | 0.357 |
| Stochastic interaction | 0.135 | 0.220 | 0.575 |
| Causal density | 0.032 | 0.178 | 0.527 |

## Robustness (by system size)

The two leaders are consistent and **strengthen** from `n=3` to `n=4`:

| Measure | ρ (n=3) | ρ (n=4) | AUC n=3 | AUC n=4 |
|---------|----:|----:|----:|----:|
| Φ whole‑minus‑sum | 0.413 | 0.553 | 0.758 | 0.828 |
| Integrated synergy | 0.324 | 0.521 | 0.721 | 0.786 |
| Total correlation | −0.280 | −0.457 | 0.321 | 0.228 |
| Time‑delayed MI | −0.190 | −0.218 | 0.348 | 0.373 |

## How this compares to the empirical proxies

Putting the two audits side by side (same data, same exact‑Φ ground truth):

| | best \|Spearman ρ\| | best AUC(Φ>0) |
|---|----:|----:|
| Empirical proxies ([proxy_audit](../proxy_audit/)) — LZ, correlation, edge count | 0.355 (total correlation, **negative**) | 0.638 (edge count) |
| Candidate Φ measures (this audit) | **0.465** (Φ whole‑minus‑sum) | **0.786** (Φ whole‑minus‑sum) |

The theoretically‑grounded measures are clearly better — Φ whole‑minus‑sum is a
genuinely useful (if imperfect) detector of integrated systems (AUC 0.79),
whereas the best empirical proxy only *anti*‑correlated.

## Interpretation

- **Structure matters.** The winners (Φ_WMS, integrated synergy) are the two
  measures built on IIT's own move — *whole minus the sum of its parts across a
  partition*. The losers (total correlation, time‑delayed MI) measure raw
  statistical dependence or predictability, which IIT‑4.0 Φ does not reward.
- **Φ whole‑minus‑sum is the best cheap stand‑in tested**, and it gets better
  with system size — encouraging for its use as a screen, though ρ ≈ 0.47 is far
  from a substitute for exact Φ.
- **Total correlation is actively misleading** (ρ = −0.36): highly
  statistically‑integrated stationary distributions tend to have *lower* IIT Φ
  here, consistent with the proxy‑audit finding.
- **Surprisingly weak:** stochastic interaction and causal density — both
  popular dynamical "integration" measures — barely track Φ (ρ ≤ 0.14).

## Caveats

- Small systems (`n ∈ {3,4}`); the discrete, exact‑Φ regime is exactly where this
  can be checked, and generalization to large/real systems is not claimed.
- Specific Boolean‑gate ensemble.
- We audit **system‑level** IIT‑4.0 Φ (mean over reachable states). Per‑state or
  Φ‑structure‑level comparisons may differ.
- Φ_WMS and integrated synergy are reported signed; the minimum‑information
  bipartition is found by enumeration (feasible for these sizes).
- **Deferred measures** that need optimisation / external packages — geometric Φ
  (Φ_G), Φ*, decoding‑Φ, full ΦID, and M‑information (Liardi et al. 2025) — are
  the natural next additions and may rank differently.

## Reproduce

`python -m candidate_audit.run 15 1 && python -m candidate_audit.analyze`
