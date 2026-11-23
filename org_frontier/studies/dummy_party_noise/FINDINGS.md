# Findings: dummy_party_noise

Hypotheses were committed (d92b78c0) before computing. Values seen beforehand: (1,2,2,2) quota 2 at ε = 0
(from `weighted_equivalence`) and OR3/AND3 whole Φ at ε = 0.

## Scores

- **H1 SUPPORTED.** OR3 + dummy and AND3 + dummy: the full group's raw φ is 0 within 1e-9 at every
  reachable state for all 9 (η, ε) (4 states at ε = 0, all 32 at ε > 0).
- **H2 SUPPORTED.** At every (η, ε), the top tie set is exactly {S,P2,P3,P4} and its φ equals the plain
  form's whole Φ within 1e-6 (in fact to six decimals).
- **H3 SUPPORTED.** OR3 + dummy and AND3 + dummy have identical whole Φ (0) and top φ everywhere.

## Exact numbers (top φ with dummy = whole Φ without)

| η \ ε | 0 | 0.05 | 0.1 |
|---|---|---|---|
| 0.05 | 2.381786 | 2.042084 | 1.590061 |
| 0.1 | 1.854569 | 1.590061 | 1.351981 |
| 0.2 | 1.041518 | 0.892972 | 0.759267 |

## Descriptive, not pre-registered

The one swapped pair on the grid gives the same value: (η, ε) = (0.05, 0.1) and (0.1, 0.05) both give
1.590061. Whether whole Φ is symmetric in input and party noise in general is not tested here (one pair).

## Reading

A party S reads but ignores has no effect on S, so it only receives. A group containing a node that only
receives can be cut at no cost, so the full group's φ is 0. The rest of the system is the three-party rule,
and that is what IIT 4.0 (via PyPhi) picks out, at the same value it would have alone. Party-side noise
does not change this.
