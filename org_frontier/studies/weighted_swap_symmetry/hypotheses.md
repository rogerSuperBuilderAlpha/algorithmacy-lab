# Are weighted rules with a heavy voter lopsided between input and party noise?

Fixed before this study's computation.

## Gap

`swap_symmetry_panel` and `noise_swap_symmetry` found that the four extreme quorums (OR3, AND3, ANY4, ALL4)
give the same whole Φ when input noise η and party-side noise ε swap, while the three interior quorums
(MAJ3, 2of4, 3of4) do not and have whole Φ 0 under party noise alone. Item 3 of
`swap_symmetry_panel/BACKLOG.md`: do weighted rules with one heavy voter follow the interior pattern?
Values already seen: (1,1,1,2) at ε = 0 for η ∈ {0.05, 0.1, 0.2} (`weighted_ratio_law`,
`weighted_equivalence`); no ε > 0 values for weighted rules.

## Model

As in `swap_symmetry_panel`: probe 464 `input_tpm` then party-side flips. Weights (1,1,1,2) at quotas 2, 3
and 4 (none is one-of-n or all-of-n). Grid η, ε ∈ {0, 0.05, 0.2} (3 swapped pairs per rule). Whole Φ = max
over reachable states of the full group's raw φ.

## Outcomes

- H1: none of the three rules is swap-symmetric (each has some pair differing by more than 1e-6).
- H2: each rule has whole Φ 0 (≤ 1e-9) at η = 0 for every ε.
- H3: at every grid point with η > 0, each rule's whole Φ changes by less than 5% (relative) between ε = 0
  and ε = 0.2, as for the interior quorums.
