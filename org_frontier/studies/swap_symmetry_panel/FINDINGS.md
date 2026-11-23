# Findings: swap_symmetry_panel

Hypotheses were committed (622fe26a) before computing. Values seen beforehand: OR3 and MAJ3 on this grid
(`noise_swap_symmetry`), and these five forms at ε = 0 only.

## Scores

- **H1 SUPPORTED.** Largest swap difference: AND3 2.2e-15, ANY4 1.9e-14, ALL4 7.1e-15. AND3 matches OR3's
  table value for value; ALL4 matches ANY4.
- **H2 SUPPORTED.** 2of4 and 3of4 each have largest swap difference 0.035822 (the pair (0, 0.2) vs (0.2, 0)).
- **H3 SUPPORTED.** 2of4 and 3of4 have whole Φ exactly 0 at η = 0 for all five ε.

## ANY4 / ALL4 whole Φ (symmetric)

| η \ ε | 0 | 0.02 | 0.05 | 0.1 | 0.2 |
|---|---|---|---|---|---|
| 0 | 4.000000 | 3.581938 | 3.016929 | 2.225483 | 1.110953 |
| 0.02 | 3.581938 | 3.303866 | 2.782719 | 2.052715 | 1.024708 |
| 0.05 | 3.016929 | 2.782719 | 2.457308 | 1.812670 | 0.904878 |
| 0.1 | 2.225483 | 2.052715 | 1.812670 | 1.460139 | 0.728896 |
| 0.2 | 1.110953 | 1.024708 | 0.904878 | 0.728896 | 0.455046 |

## 2of4 / 3of4 whole Φ (rows η, columns ε)

| η \ ε | 0 | 0.02 | 0.05 | 0.1 | 0.2 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0.02 | 0.008094 | 0.008094 | 0.008094 | 0.008092 | 0.008062 |
| 0.05 | 0.018144 | 0.018144 | 0.018144 | 0.018141 | 0.018073 |
| 0.1 | 0.029591 | 0.029591 | 0.029591 | 0.029586 | 0.029476 |
| 0.2 | 0.035822 | 0.035822 | 0.035822 | 0.035817 | 0.035683 |

## Reading

Across the seven quorums now tested (with OR3 and MAJ3 from `noise_swap_symmetry`), the split is clean:
the four extreme rules (one-of-n or all-of-n) cannot tell input errors from output errors, and the three
interior rules get whole-group Φ only from input errors. Dual pairs give identical tables. This is a
pattern over seven forms, not a derivation.
