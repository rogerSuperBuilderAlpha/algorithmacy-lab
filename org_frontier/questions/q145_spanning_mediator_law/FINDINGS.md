# q145 — findings

A single mediator that spans every party binds the whole set into the core, and Φ rises one
step per spanned party. Cutting the mediator's span removes the uncovered parties from the
core and stops Φ at the span. The controlling quantity is the spanned count, not the spanned
fraction.

## Sweep

| n | k spanned | f     | core size | Φ   | core |
|---|-----------|-------|-----------|-----|------|
| 4 | 0         | 0.000 | 1         | 1.0 | P3 |
| 4 | 1         | 0.333 | 2         | 2.0 | H, P1 |
| 4 | 2         | 0.667 | 3         | 2.0 | H, P1, P2 |
| 4 | 3         | 1.000 | 4         | 3.0 | H, P1, P2, P3 |
| 5 | 2         | 0.500 | 3         | 2.0 | H, P1, P2 |
| 5 | 4         | 1.000 | 5         | 4.0 | H, P1..P4 |
| 6 | 3         | 0.600 | 4         | 3.0 | H, P1, P2, P3 |
| 6 | 5         | 1.000 | 6         | 5.0 | H, P1..P5 |

(Full sweep in `results/output.txt` and `results/sweep.csv`.)

## Verdicts

- H1 spanning-mediator law: SUPPORTED. Full span holds all n nodes; Φ at full span is n-1
  (3, 4, 5 at n = 4, 5, 6). Partial span caps the core at k+1, holding exactly the hub and its
  k spanned parties, and excludes every unspanned party.
- H2 Φ(f) collapses across n: REFUTED. At f = 1 the Φ values are 3.0, 4.0, 5.0 — distinct by
  n, not a single collapsed curve. The span count k = round(f·(n-1)) sets Φ ≈ k+1, so at fixed
  fraction Φ still depends on n. The collapse variable is the count of spanned parties, not the
  fraction. At f = 0 the three n agree at Φ = 1, but that is the trivial isolated-singleton
  case.

## Scope

Synthetic Boolean forms. The law describes how the model's core membership and Φ respond to
one mediator's span. No organization is measured, and the empirical reach of the law is not
established here.
