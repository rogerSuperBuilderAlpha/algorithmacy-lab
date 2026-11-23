# Is whole Φ unchanged when input noise and party noise swap rates?

Fixed before this study's computation.

## Gap

`dummy_party_noise` found, without predicting it, that OR3 under input noise η and party-side noise ε gives
whole Φ 1.590061 at both (η, ε) = (0.05, 0.1) and (0.1, 0.05). Item 1 of `dummy_party_noise/BACKLOG.md`.
Values already seen: OR3/AND3 whole Φ at η ∈ {0.05, 0.1, 0.2} × ε ∈ {0, 0.05, 0.1} (that study's table),
and OR3/MAJ3 at ε = 0 for the `quorum_noise_sweep` rates.

## Model

Probe 464 `input_tpm` (S misreads each party with probability η), then each party copies S but flips with
probability ε. Grid η, ε ∈ {0, 0.02, 0.05, 0.1, 0.2} (25 points, 10 swapped pairs). Forms OR3 and MAJ3.
Whole Φ = max over reachable states of the full group's raw φ (no floor).

## Outcomes

- H1: OR3 whole Φ is equal (within 1e-6) at (η, ε) and (ε, η) for all 10 swapped pairs.
- H2: the same holds for MAJ3.
- H3: OR3 whole Φ depends only on the combined flip rate c = η + ε − 2ηε: at every grid point with η, ε > 0
  it equals the value at (c, 0) within 1e-6 (computed at those extra points).
