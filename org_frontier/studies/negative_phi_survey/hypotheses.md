# Does PyPhi return negative φ anywhere in the noisy-quorum panels, and does it change any reported number?

Fixed before this study's computation.

## Gap

`high_noise_tie_onset` found that PyPhi returns a negative full-group φ at the all-zero state for OR3 at
η ≥ 0.36 (−0.181471 at 0.36) and ANY4 at η ≥ 0.33 (−0.184887 at 0.33). The noisy-quorum studies compute
whole Φ as `max(0, max over states of full-group φ)`, which silently floors negatives to 0. Item 2 of
`high_noise_tie_onset/BACKLOG.md`: survey negative φ across the earlier panels. Values already seen: the
OR3/ANY4 all-zero values above (η 0.31–0.39) and every number published in the studies listed below.

## Model

Raw `new_big_phi.sia(...).phi` for every reachable subsystem at every reachable state, no filtering, for:

- Panel A: the seven `quorum_noise_sweep` forms (OR3, MAJ3, AND3, ANY4, 2of4, 3of4, ALL4) at η = 0.01,
  0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45 (probe 464 `input_tpm`).
- Panel B: the `weighted_equivalence` dummy-party cases, (1,2,2,2) quotas 2 and 4 at η = 0.05, 0.1, 0.2,
  whose whole Φ was reported as exactly 0.

A value counts as negative if φ < −1e-9.

## Outcomes

- H1: no subset has negative φ at any state in panel A for η ≤ 0.3.
- H2: in panel A, the published whole Φ, top φ and top tie set are unchanged if negatives are kept (every
  case with published whole Φ > 0 has its max full-group φ > 0, and no negative value enters a tie set).
- H3: in panel B, the full group's raw φ is exactly 0 (|φ| ≤ 1e-9) at every reachable state; none negative.
