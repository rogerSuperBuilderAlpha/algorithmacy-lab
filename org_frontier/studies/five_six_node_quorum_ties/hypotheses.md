# Weighted and five-party quorums under input noise, read as tie sets: hypotheses and methods

Fixed before this study's computation. Disclosure: while timing, one value was computed first: 3of5,
independent errors, e = 0.2, state all-zero, full-system φ = 0.004260 (12.7 s). It enters H3 below;
readers can discount it.

## Gap

`shared_share_ties/` showed the single complex PyPhi returns for a noisy quorum hides multi-way ties.
Its backlog asks for (1) weighted quorums under noise reported as tie sets, and (2) the five-party test
of the regularity seen on three- and four-party interior quorums: the largest subset φ equals the node
count times whole-system Φ (22 of 24 cases in `quorum_noise_sweep`, 14 of 14 in `quorum_correlated_noise`).

## Model

Probe 464's construction and `input_tpm` (independent reading errors e; parties copy S). For each
reachable state, φ (`new_big_phi.sia`) of every subset `new_big_phi.reachable_subsystems` yields. Whole Φ
= maximum full-group φ over reachable states. Tie set = subsets within 1e-9 of the state's maximum.

- Part A: weights (1,1,2,2) (S, P1..P4; P3, P4 heavy), quotas 2, 3, 4, 5; e ∈ {0, 0.05, 0.2, 0.4}. 16 cases.
- Part B: 3of5 (five equal parties, quota 3); e ∈ {0.1, 0.2}. 2 cases.

Control: Part A whole Φ at e = 0.1 is not in the grid, so as a control quotas 2 and 5 are also run at
e = 0.1 and must reproduce probe 464's whole Φ 0.015905 (1e-6). The run stops if it does not.

## Outcomes (threshold 1e-9)

- H1: for quotas 2 and 5, {S,P3,P4} is in the tie set at the state of largest φ at every noisy rate.
- H2: for all four quotas, whole Φ > 1e-9 at every noisy rate.
- H3: for 3of5 at both rates, largest subset φ (over states) = 6 × whole Φ within 1e-6 relative.
- H4: for 3of5 at both rates, at the state of largest φ the tie set is exactly the five {S,Pi} pairs.
- H5: at no noisy rate, in any Part A or Part B case, is the full group in the tie set at the state of
  largest φ.

Descriptive: e = 0 whole Φ and tie sets per quota; ratio largest-subset φ / whole Φ for every case.
