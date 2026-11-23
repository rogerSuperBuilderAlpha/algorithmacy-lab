# Does a never-pivotal party always zero whole Φ in OR3 and AND3, with and without party-side noise?

Fixed before this study's computation.

## Gap

`weighted_equivalence` found that (1,2,2,2) at quotas 2 and 4 (one party never pivotal) has whole Φ exactly
0 at η = 0.05, 0.1, 0.2, with the top φ equal to the matching three-party form (quota 2 = OR3 values on
{S,P2,P3,P4}). Item 3 of `weighted_equivalence/BACKLOG.md`: does this hold for AND3 plus a dummy, and when
the parties also misread S? Values already seen: (1,2,2,2) quota 2 at party noise 0 (whole 0; tops
2.381786, 1.854569, 1.041518), OR3/AND3 whole Φ at party noise 0, and `negative_phi_survey`'s confirmation
that those zeros are exact at every state.

## Model

Probe 464 `input_tpm` (S misreads each party with probability η), then party-side noise: each party copies
S but flips with probability ε, independently. η ∈ {0.05, 0.1, 0.2}, ε ∈ {0, 0.05, 0.1}.

- OR3 + dummy: weights (1,2,2,2), quota 2. AND3 + dummy: weights (1,2,2,2), quota 6. P1 is never pivotal.
- Controls: OR3 = (1,1,1) quota 1, AND3 = (1,1,1) quota 3, same noise.

Whole Φ = max over reachable states of the full group's raw φ; top = max over states and subsets.

## Outcomes

- H1: both dummy forms have whole Φ exactly 0 (|φ| ≤ 1e-9 at every reachable state) at all 9 (η, ε).
- H2: each dummy form's top φ equals its control's whole Φ (within 1e-6) at every (η, ε), and the top tie
  set is exactly {S,P2,P3,P4}.
- H3: OR3 + dummy and AND3 + dummy have identical whole Φ and top φ at every (η, ε) (bit-flip duality).
