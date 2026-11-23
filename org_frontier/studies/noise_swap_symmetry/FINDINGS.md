# Findings: noise_swap_symmetry

Hypotheses were committed (3db908d6) before computing. Values seen beforehand: OR3/AND3 at η ∈ {0.05, 0.1,
0.2} × ε ∈ {0, 0.05, 0.1} from `dummy_party_noise`, and OR3/MAJ3 at ε = 0.

## Scores

- **H1 SUPPORTED.** OR3 whole Φ at (η, ε) equals (ε, η) for all 10 swapped pairs; largest difference
  3.9968e-15. Example: (0.02, 0.2) and (0.2, 0.02) both 0.980269; (0, 0.1) and (0.1, 0) both 1.854569.
- **H2 REFUTED.** MAJ3 is not symmetric (largest difference 0.036624). With η = 0 its whole Φ is 0 at every
  ε, while with ε = 0 it is 0.006851–0.036624.
- **H3 REFUTED.** OR3 whole Φ is not a function of the combined flip rate c = η + ε − 2ηε. Example:
  (0.05, 0.05) gives 2.042084, but (c, 0) = (0.095, 0) gives 1.903424. Largest difference 0.171454.

## OR3 whole Φ (symmetric table)

| η \ ε | 0 | 0.02 | 0.05 | 0.1 | 0.2 |
|---|---|---|---|---|---|
| 0 | 3.000000 | 2.741279 | 2.381786 | 1.854569 | 1.041518 |
| 0.02 | 2.741279 | 2.580070 | 2.241718 | 1.745506 | 0.980269 |
| 0.05 | 2.381786 | 2.241718 | 2.042084 | 1.590061 | 0.892972 |
| 0.1 | 1.854569 | 1.745506 | 1.590061 | 1.351981 | 0.759267 |
| 0.2 | 1.041518 | 0.980269 | 0.892972 | 0.759267 | 0.533257 |

## MAJ3 whole Φ (rows η, columns ε)

| η \ ε | 0 | 0.02 | 0.05 | 0.1 | 0.2 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0.02 | 0.006851 | 0.006851 | 0.006850 | 0.006842 | 0.006746 |
| 0.05 | 0.015761 | 0.015761 | 0.015758 | 0.015739 | 0.015518 |
| 0.1 | 0.026981 | 0.026980 | 0.026977 | 0.026944 | 0.026566 |
| 0.2 | 0.036624 | 0.036623 | 0.036618 | 0.036574 | 0.036060 |

## Reading

For OR3, an error on the way in (S misreads a party) and an error on the way out (a party misreads S) cost
exactly the same whole Φ, rate for rate, but two errors do not simply add up to one bigger error. For MAJ3,
only errors on the way in create whole-group Φ; errors on the way out slightly reduce it. We have not
derived why OR3 is symmetric; that is open.
