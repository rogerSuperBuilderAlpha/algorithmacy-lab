# Gate match test: does a gated relayer stay bound exactly when its gate rule matches the platform's?

Fixed before this study's computation.

## Gap

`or_gate_source` noticed, after the run, that across ten inside-driven gated-relayer forms the whole group
was bound (Φ = 2.0) in every form where the relayer's gate rule matched the platform's rule (AND–AND, OR–OR)
and had Φ = 0 in every form where they differed. Only one OR–OR form was tested. This study tests that
matching rule on new forms, with the predictions fixed first.

## Model

P reads R1, R2; R1' = P; R2' = C1; the relayer C1 combines P with a switch G; G copies a group member.
Five members P, R1, R2, C1, G.

- **orP_or_from_P** (control, = `or_gate_source`): P' = R1 ∨ R2, C1' = P ∨ G, G' = P.
- **orP_or_from_R1**, **orP_or_from_R2**, **orP_or_from_C1**: as control with G' = R1, R2, C1 (matched).
- **orP_and_from_R1**: P' = R1 ∨ R2, C1' = P ∧ G, G' = R1 (mismatched).
- **xorP_xor_from_P**: P' = R1 ⊕ R2, C1' = P ⊕ G, G' = P (matched).
- **xorP_and_from_P**: P' = R1 ⊕ R2, C1' = P ∧ G, G' = P (mismatched).

Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest full-group φ over
states.

Control: orP_or_from_P whole Φ = 2.0.

## Outcomes (threshold 1e-9)

- H1: orP_or_from_R1, orP_or_from_R2 and orP_or_from_C1 each have whole Φ = 2.0 (within 1e-6).
- H2: orP_and_from_R1 whole Φ ≤ 1e-9.
- H3: xorP_xor_from_P whole Φ > 1e-9.
- H4: xorP_and_from_P whole Φ ≤ 1e-9.
- Matching rule overall: SUPPORTED only if H1–H4 all hold.
