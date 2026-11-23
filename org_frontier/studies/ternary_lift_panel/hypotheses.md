# Ternary lifts of the three-node triad: does giving each node three states change the verdict?

Fixed before this study's computation.

## Gap

`ternary_pivotality` lifted the faithful conjunctive triad (W' = S, S' = W ∧ C, C' = S) to {0,1,2} with
S' = min(W, C) and found the full triad {W,S,C} is the major complex at (2,2,2) but not at (1,1,1).
`multivalued_iit4_port` reports φ_s = 3.169925 = 2 log₂ 3 at (2,2,2) for that lift. No other rule has
been lifted, and a binary rule has many three-valued extensions. This study asks whether the yes/no
verdict (is the whole triad one integrated unit?) depends on which extension is chosen.

## Model

W' = S, C' = S, S' = f(W, C), all nodes on {0,1,2}; the binary version of each rule on {0,1} with the
same code. Lifts:

| binary rule | lift | agrees with the binary rule on {0,1}? |
|---|---|---|
| AND | min(W,C) | yes |
| AND | 2 if W = C = 2, else 0 ("all top") | no (1,1 → 0) |
| OR | max(W,C) | yes |
| OR | min(W + C, 2) (capped sum) | yes |
| XOR | abs(W − C) | yes |
| XOR | (W + C) mod 3 | no (1,1 → 2) |
| copy (S' = W) | S' = W | yes |

Deterministic (r = 0) and with S misreading each input with probability r = 0.1 (uniformly to another
value; bit flip in binary). Whole Φ = largest full-system φ over reachable states; at every state
attaining it, the maximal complex. "Triadic" = the full triad {W,S,C} is the maximal complex at every
whole-Φ state.

Values already seen before this file: only those quoted above from `ternary_pivotality` and
`multivalued_iit4_port`.

## Controls (must pass)

- C1: binary AND at (1,1,1), r = 0 has Φ = 2.0 (stock-pin value in `smoke_m2.py`).
- C2: ternary min at (2,2,2), r = 0 has φ = 3.169925.

## Outcomes (threshold 1e-9)

- H1: every lift that agrees with its binary rule on {0,1} has the same verdict (triadic or not) as
  the binary rule, at r = 0 and at r = 0.1.
- H2: for those agreeing lifts, ternary whole Φ ≥ binary whole Φ at r = 0.
- H3: the two non-agreeing lifts (all-top AND, sum mod 3) also keep the binary verdict.
- H4: copy (S' = W) is not triadic in either alphabet (C reads S but nothing reads C, so a sanity check of the pipeline).
- H5: the two OR lifts (max, capped sum) give different whole Φ at r = 0 (the lift, not just the
  binary rule, sets the number).
