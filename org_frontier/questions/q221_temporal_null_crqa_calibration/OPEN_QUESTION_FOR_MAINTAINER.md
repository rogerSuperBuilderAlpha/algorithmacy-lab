# Open question for the maintainer: which convention should q161's bottleneck target use?

**Status: open. q161 has not been changed.** This note records the evidence so the lab can decide.

## The two conventions

1. **Rule-freeze (q161 as implemented).**
   - `bottleneck_set` replaces node k's update rule with the constant 0 (`frozen[k] = lambda x: 0`).
   - It rebuilds the TPM and the connectivity matrix from the frozen rules, then recomputes the
     major-complex Φ of the whole 3-node network over its reachable states.
   - Node k stays a network element: PyPhi still perturbs its state, and the other nodes still read it.
2. **Background condition (closer to IIT's treatment of fixed external elements).**
   - The original network is kept. Node k is held at a fixed value v.
   - Residual Φ is the maximum over subsystems that **exclude** k, at states reachable with x_k = v.

## Evidence (pinned PyPhi `b78d0e34`, IIT 4.0)

| pair | rule-freeze B | background condition B (v = 0 and v = 1) |
|---|---|---|
| S1: P = aff(9,6,10) vs Q = aff(9,15,10) | {X,H} vs {H} | {X,H} vs {X,H} |
| S2: aff(9,6,10) vs aff(9,15,12) | {X,H} vs {H} | {X,H} vs {X,Y,H} (the latter is ineligible, \|B\| = 3) |
| S3: aff(9,6,11) vs aff(9,14,10) | {X,H} vs {H} | {X,H} vs {X,H} |

**Mechanism.** Under rule-freeze, freezing X in Q leaves a residual single-node complex {Y} with Φ = 1, so
X's drop is 1. In P, no complex survives, so the drop is 2. Y lies outside the intact major complex {X,H}.

**Further check.** If the frozen node's outgoing edges are also removed, both P and Q have the residual {H}
with Φ = 1.

**Unaffected by the convention.** Within every pair, the major complex ({X,H}) and Φ (2) are identical, and the
q161 target is node-permutation equivariant and value-flip invariant.

Sources:
- `TARGET_AUDIT.md`
- `identifiability/results/target_variants.txt`, `target_audit.txt`, `edge_removal_check.txt`
- `PYPHI_FORMALISM.md`
- tests in `identifiability/test_invariants_extra.py` (run with `Q221_SLOW=1`)
- CI check `q221-target-variants`

## Why it matters

- In the q221 survivors, the q161 "structural target" difference is **entirely a product of the convention**.
- Any study that uses q161's bottleneck as ground truth may contain the same artefact, including q220's
  eligibility rule and bottleneck scoring. This applies wherever a node outside the major complex can carry a
  residual complex once another node is frozen.

## Questions for the maintainer

1. Which convention is intended as the lab's definition: rule-freeze, edge removal, or background condition?
2. Should q161 or q220 report sensitivity to the alternative convention? A cheap check exists:
   `identifiability/target_variants.py` (about 4 s per form at n = 3).
3. If rule-freeze is kept, should the definition document that the frozen node remains a perturbed element?

## What q221 assumes

q221's headline result (target A) does **not** depend on this choice. It is a statement about recurrence
summaries and transition laws.
