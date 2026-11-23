# Four identical parties: does PyPhi's tie-break matter more as the group grows?

Fixed before this study's computation.

## Gap

PyPhi breaks ties among maximal cause/effect states arbitrarily. With two identical parties
(`tie_audit`, 4,096 three-node forms) no verdict depended on it. With three identical parties
(`consensus_pivotality`, `mixed_reads`) 24 of 256 commit rules did, all of them rules where every party is
pivotal at exactly one of the two consensus states (24 of the 56 such rules), and no symmetric rule was
affected. Rule R (every party pivotal at some consensus) matched "triadic under some tie choice" exactly.
Four identical parties have not been run.

## Family and sample

Five nodes P1..P4, S; every party copies S; S' = h(P1..P4). There are 65,536 rules h, too many to run, so:
- all 30 non-constant symmetric rules (output depends only on how many parties are on);
- 128 rules drawn (seed 0) from those where every party is pivotal at exactly one consensus ("one-sided");
- 64 rules drawn uniformly (seed 1) from all 65,536.
For each rule: default max Φ and, per reachable state, Φ under every tied (cause, effect) choice.

## Predictions (threshold 1e-9; verdict = max whole-system Phi over reachable states)

- H1: Rule R matches "triadic under some tie choice" for every sampled rule: 0 mismatches.
- H2: No symmetric rule's verdict depends on the tie choice.
- H3: Tie-dependence grows with group size: among the 128 one-sided rules, the share whose verdict
  depends on the tie choice is above the three-party share 24/56 = 0.43.

## Controls

- C1: AND4 (output 1 only when all four are on) has Φ = 4.0. This value was seen once while timing the
  run before this file was written; it is a control, not a prediction.
