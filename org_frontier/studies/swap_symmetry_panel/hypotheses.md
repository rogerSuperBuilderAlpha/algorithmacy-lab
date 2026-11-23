# Which quorums cannot tell input noise from party noise?

Fixed before this study's computation.

## Gap

`noise_swap_symmetry` found OR3's whole Φ unchanged when input noise η and party-side noise ε swap rates
(all 10 pairs, max difference 4e-15), while MAJ3 is not symmetric and has whole Φ 0 under party noise alone.
Items 1–2 of `noise_swap_symmetry/BACKLOG.md`: which other quorums share OR3's symmetry? Values already
seen: OR3 and MAJ3 on the grid below; AND3, ANY4, 2of4, 3of4, ALL4 only at ε = 0 (`quorum_noise_sweep`).

## Model

As in `noise_swap_symmetry`: probe 464 `input_tpm` then party-side flips, grid η, ε ∈ {0, 0.02, 0.05, 0.1,
0.2}, whole Φ = max over reachable states of the full group's raw φ. Forms AND3, ANY4, ALL4, 2of4, 3of4.

## Outcomes

- H1: the extreme quorums AND3, ANY4 and ALL4 are swap-symmetric (within 1e-6 at all 10 pairs).
- H2: the interior quorums 2of4 and 3of4 are not swap-symmetric (some pair differs by more than 1e-6).
- H3: 2of4 and 3of4 have whole Φ 0 (≤ 1e-9) at η = 0 for every ε.
