# OR-gate source: is the OR-gated relayer's split specific to the switch copying the platform?

Fixed before this study's computation.

## Gap

`gate_source` found that an AND-gated relayer (C1' = P ∧ G) rejoins the whole (Φ = 2.0) when any group
member (P, R1 or C1) drives the switch G. With an OR gate (C1' = P ∨ G), a switch driven by P left whole Φ
at 0, against the pre-registered prediction. Its BACKLOG asked whether that holds for other drivers.

## Model

P reads R1, R2; R1' = P; R2' = C1. Five members P, R1, R2, C1, G.

- **or_from_P** (control, = `gate_source` or_from_P): P' = R1 ∧ R2, C1' = P ∨ G, G' = P.
- **or_from_R1**: as control with G' = R1.
- **or_from_R2**: G' = R2.
- **or_from_C1**: G' = C1.
- **and_from_R2**: AND gate C1' = P ∧ G with G' = R2 (fills in the AND series).
- **orP_and_from_P**: OR platform P' = R1 ∨ R2, AND gate C1' = P ∧ G, G' = P.
- **orP_or_from_P**: OR platform P' = R1 ∨ R2, OR gate C1' = P ∨ G, G' = P.

Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest full-group φ over
states; top tie sets pooled over all states where top φ is reached.

Control: or_from_P whole Φ = 0, top φ = 2.0 (reproduces `gate_source`).

## Outcomes (threshold 1e-9)

- H1: or_from_R1 whole Φ > 1e-9.
- H2: or_from_R2 whole Φ > 1e-9.
- H3: or_from_C1 whole Φ > 1e-9.
- H4: and_from_R2 whole Φ = 2.0 (within 1e-6).
- H5: orP_and_from_P whole Φ > 1e-9.
- H6: orP_or_from_P whole Φ > 1e-9.
