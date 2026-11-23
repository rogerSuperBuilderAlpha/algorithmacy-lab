# Alphabet ladder: two, three and four possible answers on the same vote hub

Fixed before this study's computation.

## Gap

`ternary_majority_noise` found two exact regularities on the mediator + three parties hub with uniform
input noise. (1) For the middle rule (MAJ3 on {0,1}, median on {0,1,2}), the best core φ at a
whole-Φ state is exactly 4 × whole Φ with two values and exactly 7 × with three, at every noisy rate.
(2) The min rule without noise has whole Φ 3 log₂ k (3.0 for k = 2; 4.754888 for k = 3). Both were
observed, not derived. Item 4 of its backlog asks why 7. A four-valued alphabet (k = 4) tests whether
these are patterns in k.

Values already seen before this file: all k = 2 and k = 3 numbers in
`ternary_majority_noise/FINDINGS.md`. For k = 4 only the run time of one φ evaluation (about 6 s) was
measured, not its value.

## Model

Same as `ternary_majority_noise`, alphabet {0,…,k−1}: S misreads each party with probability r,
uniformly to one of the k − 1 other values; S commits median or min of its readings; parties copy S.
k = 4 at r ∈ {0, 0.05, 0.1, 0.2} (median) and r ∈ {0, 0.1} (min). k = 2 and 3 at r = 0.1 rerun as
controls. Whole Φ = largest full-system φ over reachable states; the maximal complex is computed at one
whole-Φ state per case (the parties are symmetric, so the others are relabelings).

## Controls (must pass)

- C1: k = 2 median at r = 0.1 = 0.026981 and k = 3 median at r = 0.1 = 0.022209.

## Outcomes (threshold 1e-9; ratio tolerance 1e-6 relative)

- H1: k = 4 median at r = 0 has whole Φ ≤ 1e-9.
- H2: k = 4 median has whole Φ > 1e-9 at every noisy rate, and its maximal complex is never the
  full group.
- H3: the k = 4 median's best-core-to-whole ratio is the same at every noisy rate (as for k = 2, 3).
- H4: that ratio is 3k − 2 = 10 (the line through 4 and 7).
- H5: k = 4 min at r = 0 has whole Φ 3 log₂ 4 = 6.0, and the full group as its maximal complex at
  r = 0 and 0.1.
