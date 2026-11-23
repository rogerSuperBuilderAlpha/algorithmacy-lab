# Findings: weighted_swap_symmetry

Hypotheses were committed (2c3b153e) before computing. Values seen beforehand: (1,1,1,2) at ε = 0 for
η ∈ {0.05, 0.1, 0.2}; no weighted values at ε > 0.

## Scores

- **H1 SUPPORTED.** Largest swap differences: quota 2 0.029299, quota 3 0.008897, quota 4 0.029299.
- **H2 SUPPORTED.** All three rules have whole Φ 0 at η = 0 for ε = 0, 0.05, 0.2.
- **H3 SUPPORTED.** From ε = 0 to 0.2, whole Φ drops by 0.389105% in every case (e.g. quota 3, η = 0.2:
  0.008897 → 0.008862).

## Exact numbers (whole Φ)

| rule | η | ε = 0 | ε = 0.05 | ε = 0.2 |
|---|---|---|---|---|
| (1,1,1,2) q2 | 0.05 | 0.014973 | 0.014972 | 0.014914 |
| (1,1,1,2) q2 | 0.2 | 0.029299 | 0.029299 | 0.029185 |
| (1,1,1,2) q3 | 0.05 | 0.003897 | 0.003897 | 0.003882 |
| (1,1,1,2) q3 | 0.2 | 0.008897 | 0.008897 | 0.008862 |
| (1,1,1,2) q4 | 0.05 | 0.014973 | 0.014972 | 0.014914 |
| (1,1,1,2) q4 | 0.2 | 0.029299 | 0.029299 | 0.029185 |

Quotas 2 and 4 give identical values (they are each other's yes/no mirror).

## Post-hoc pattern (not pre-registered)

The 0.389105% drop equals 1/257, and 257 = 4^4 + 1, with ε/(1 − ε) = 0.25 at ε = 0.2 and n = 4 parties.
That suggested Φ(η, ε) = Φ(η, 0) / (1 + (ε / (1 − ε))^n). Checked against every stored case with η, ε > 0
for the non-extreme rules in this study, `noise_swap_symmetry` (MAJ3, n = 3) and `swap_symmetry_panel` (2of4,
3of4): 60 points, largest relative error 2.0e-14. The formula was found by looking at these numbers, so it
is a conjecture until it predicts new cases (BACKLOG item 1).
