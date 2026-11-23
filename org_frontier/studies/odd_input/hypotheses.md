# Odd input: which input pattern of the relayer's gate decides whether the group binds?

Fixed before this study's computation.

## Gap

`forcing_match` showed that negating a gated relayer's output changes nothing (NAND = AND, NOR = OR), and
that an AND platform binds with AND/NAND gates but not OR/NOR, and an OR platform the reverse. Each of these
gates has one "odd" input pattern (P, G) where its output differs from the other three: AND/NAND at (1, 1),
OR/NOR at (0, 0). So far, "odd pattern at P = 1, G = 1" binds with AND platforms and "odd pattern at
P = 0, G = 0" binds with OR platforms. That leaves open whether P's value or G's value at the odd pattern
decides. Gates with the odd pattern at (1, 0) or (0, 1) separate the two.

## Rule under test (stated before running)

**P-value rule:** with an AND platform the whole group is bound exactly when the gate's odd pattern has
P = 1; with an OR platform, exactly when it has P = 0. (The rival G-value rule predicts the opposite on the
four new forms.)

## Model

P reads R1, R2; R1' = P; R2' = C1; C1' = gate(P, G); G' = P. Five members P, R1, R2, C1, G.

- **andP_and** (control, = `forcing_match` andP_and): AND platform, C1' = P ∧ G. Whole Φ = 2.0.
- **andP_p_notg**: AND platform, C1' = P ∧ ¬G (odd at P = 1, G = 0).
- **andP_notp_g**: AND platform, C1' = ¬P ∧ G (odd at P = 0, G = 1).
- **orP_p_or_notg**: OR platform, C1' = P ∨ ¬G (odd at P = 0, G = 1).
- **orP_notp_or_g**: OR platform, C1' = ¬P ∨ G (odd at P = 1, G = 0).

Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest full-group φ over
states; tie sets pooled.

## Outcomes (threshold 1e-9)

- H1: andP_p_notg whole Φ > 1e-9.
- H2: andP_notp_g whole Φ ≤ 1e-9.
- H3: orP_p_or_notg whole Φ > 1e-9.
- H4: orP_notp_or_g whole Φ ≤ 1e-9.
- P-value rule: SUPPORTED only if H1–H4 all hold. G-value rule: SUPPORTED only if all four are reversed.
