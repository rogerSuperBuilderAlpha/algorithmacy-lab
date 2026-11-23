# Echo switch: does a switch that copies an echo the platform reads raise Φ in a new setting?

Fixed before this study's computation.

## Gap

Across `gate_census_r1`, `switch_delay` and `switch_loop_member`, the switch raised whole Φ only when it
copied R1. R1 is a pure echo of the platform (R1' = P) that the platform reads. An echo the platform does
not read (`switch_delay`, via D) and loop members that are not pure echoes (R2, C1) did not reproduce the
gain. Post-hoc reading: the switch must copy a pure echo of P that P reads. This study tests whether that
reading carries to a different platform.

## Model

Six nodes: P, R1, R2, R3, C1, G. Platform P' = R1 ∧ R2 ∧ R3 (three-way AND). R1' = P, R3' = P (two pure
echoes the platform reads), R2' = C1, C1' = f(P, G) with the gate convention of `gate_census` (bit 2·P + G).
Switch drivers: from_P (G' = P) and from_R3 (G' = R3). Gates: AND (code 8) and P ∧ ¬G (code 4). 4 forms.
Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest full-group φ over
states.

## Outcomes (threshold 1e-6)

- H1: P ∧ ¬G gate: whole Φ with G' = R3 is greater than with G' = P.
- H2: AND gate: whole Φ with G' = R3 equals whole Φ with G' = P.
- Echo reading: SUPPORTED if H1 holds (H2 is the analogue of the unchanged AND/AND case).
