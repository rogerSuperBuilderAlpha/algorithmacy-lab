# Forcing match: a sharper rule for when a switch-gated relayer stays bound

Fixed before this study's computation.

## Gap

`gate_match_test` found that "the relayer's gate rule must match the platform's rule" holds for AND and OR
platforms (14 inside-driven forms, no exception) but fails for XOR (whole Φ = 0.5 with matched and
mismatched gates). Its BACKLOG proposed a narrower rule tied to platforms where one input can settle the
output.

## Proposed rule (stated before running)

An AND platform is settled by an input of 0; an OR platform by an input of 1. A gate is settled by its
switch when one switch value fixes the gate's output regardless of P: for AND and NOR gates the fixed output
is 0; for OR and NAND gates it is 1. **Forcing-match rule:** with an AND or OR platform, the whole group is
bound (Φ > 0) exactly when the gate's fixed output equals the input value that settles the platform. This
reproduces all 14 AND/OR results so far (AND gate → 0 matches AND platform; OR gate → 1 matches OR
platform). It says nothing about XOR.

## Model

P reads R1, R2; R1' = P; R2' = C1; C1' = gate(P, G); G' = P. Five members P, R1, R2, C1, G.

- **andP_and** (control, = `gate_source` and_from_P): AND platform, AND gate. Whole Φ = 2.0.
- **andP_nor**: AND platform, NOR gate C1' = ¬(P ∨ G) (fixed output 0: match).
- **andP_nand**: AND platform, NAND gate C1' = ¬(P ∧ G) (fixed output 1: no match).
- **orP_nand**: OR platform, NAND gate (fixed output 1: match).
- **orP_nor**: OR platform, NOR gate (fixed output 0: no match).
- **xorP_or**: XOR platform, OR gate.

Exact IIT 4.0 φ of every reachable subset in every reachable state; whole Φ = largest full-group φ over
states; tie sets pooled.

## Outcomes (threshold 1e-9)

- H1: andP_nor whole Φ > 1e-9.
- H2: andP_nand whole Φ ≤ 1e-9.
- H3: orP_nand whole Φ > 1e-9.
- H4: orP_nor whole Φ ≤ 1e-9.
- H5: xorP_or whole Φ > 1e-9 (XOR platform bound regardless of gate, as in `gate_match_test`).
- Forcing-match rule: SUPPORTED only if H1–H4 all hold.
