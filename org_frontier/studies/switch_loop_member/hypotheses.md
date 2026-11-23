# Switch loop member: does any loop member raise Φ when it drives the switch?

Fixed before this study's computation.

## Gap

`gate_census_r1` found that a switch copying R1 (instead of the platform P) raises whole Φ in 16 forms.
`switch_delay` refuted the explanation that this is only the extra time step: a switch fed P through an
outside copier D gives different values (1.0, 1.0, 0.5). A post-hoc reading was that what matters is that
R1 is a member of the platform's loop. R2 and C1 are also loop members (P reads R2, R2' = C1, C1 is the
relayer). This study tests that reading.

## Model

P reads R1, R2 (platform rule AND or XOR); R1' = P; R2' = C1; C1' = f(P, G). Switch drivers:
from_R2 (G' = R2) and from_C1 (G' = C1), n = 5. Forms as in `switch_delay`: AND platform with AND gate
(code 8) and with P ∧ ¬G (code 4); XOR platform with AND gate (code 8). 2 × 3 = 6 forms.
Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest full-group φ over
states. Reference values with G' = R1: 2.0, 0.830075, 2.0.

Control: from_R2 and from_C1 with the AND gate under the AND platform give 2.0 (`or_gate_source`
and_from_R2; `gate_source` and_from_C1).

## Outcomes (threshold 1e-6)

- H1: from_R2 AND_g04 = 0.830075 and from_C1 AND_g04 = 0.830075.
- H2: from_R2 XOR_g08 = 2.0 and from_C1 XOR_g08 = 2.0.
- Loop-member reading: SUPPORTED only if H1 and H2 both hold.
