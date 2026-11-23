# Mixed reads at three parties: does flipping how a party reads the hub change anything?

Fixed before this study's computation.

## Gap

`consensus_pivotality` ran all 256 commit rules S' = h(P1, P2, P3) with every party copying S. Two
backlog items stay open: (a) `lockstep_symmetry` handled a party that reads NOT S by "aligning" it
(renaming that party's 0/1 values), but that was only checked with two parties, where PyPhi's state
ties never mattered (`tie_audit`: 0 of 4,096 three-node forms). (b) With three identical parties,
24 of 256 verdicts depend on PyPhi's arbitrary tie-break, and 20 rules disagree with their global 0/1
renamed twin. Renaming a node's values is an exact symmetry of the system, so any difference between a
form and its renamed twin can only come from the tie-break.

## Family

Four nodes P1, P2, P3, S. Read pattern r in 0..7: party i reads NOT S when bit i of r is set
(P_i' = S XOR r_i), otherwise copies S. Commit S' = h(P1, P2, P3) for all 256 h. 8 x 256 = 2,048 forms.
Aligned twin: Q_i = P_i XOR r_i gives copy reads and commit h_r(q) = h(q XOR r). So every mixed form is
a per-party renaming of a copy-read form from `consensus_pivotality`.

## Predictions (threshold 1e-9; verdict = max whole-system Phi over reachable states)

- H1: Under PyPhi's default tie-break, per-party renaming is NOT invariant: at least one mixed form
  (r != 0) gets a different max Phi from its aligned twin, and every such form's aligned twin is one of
  the 24 tie-dependent rules of `consensus_pivotality`.
- H2: Scored over all tied state choices, renaming is exact: for all 2,048 forms the pair
  (max over states of min over ties, max over states of max over ties) equals the aligned twin's
  pair to 1e-9.
- H3: "Triadic under some tie choice" for every one of the 2,048 forms equals rule R (every party
  pivotal at some consensus) applied to the aligned rule h_r: 0 mismatches.
- H4: Each of the 8 read patterns has exactly 24 forms whose verdict depends on the tie choice.

## Controls

- C1: r = 0 reproduces `consensus_pivotality`: AND3 Phi = 3.0, MAJ3 Phi = 0, 50/256 triadic by default.
