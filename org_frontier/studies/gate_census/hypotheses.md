# Gate census: all 16 two-input rules for a switch-gated relayer under AND, OR and XOR platforms

Fixed before this study's computation.

## Gap

`relay_flips`, `gate_source`, `or_gate_source`, `gate_match_test`, `forcing_match` and `odd_input` tested
gated relayers one hand-picked rule at a time. `odd_input` supported a P-value rule for gates with one odd
input pattern. This study runs every two-input rule for the relayer, so the rules can be checked on all
cases at once.

## Model

P reads R1, R2; R1' = P; R2' = C1; C1' = f(P, G) for each of the 16 Boolean functions f; G' = P. Platform
P' = R1 ∧ R2 (AND), R1 ∨ R2 (OR) or R1 ⊕ R2 (XOR). 48 forms, five members each. Exact IIT 4.0 φ of every
reachable subset in every reachable state; whole Φ = largest full-group φ over states; tie sets pooled.

Gate classes:
- **single-odd** (8): AND, NAND, OR, NOR, P ∧ ¬G, its negation, ¬P ∧ G, its negation. The odd pattern is the
  one input (P, G) whose output differs from the other three.
- **constant** (2): 0, 1.
- **P-only** (2): P, ¬P (ignores G).
- **G-only** (2): G, ¬G (ignores P).
- **parity** (2): XOR, XNOR.

Controls: the AND gate under the AND platform gives whole Φ = 2.0 (`forcing_match` andP_and); the AND gate
under the XOR platform gives 0.5 (`gate_match_test` xorP_and_from_P).

## Outcomes (threshold 1e-9)

- H1 (P-value rule): for the 8 single-odd gates under AND and OR platforms (16 forms), whole Φ > 1e-9
  exactly when the odd pattern has P = 1 (AND platform) or P = 0 (OR platform).
- H2: constant and P-only gates give whole Φ ≤ 1e-9 under all three platforms (12 forms).
- H3: G-only gates give whole Φ = 2.0 under AND and OR platforms and 0.5 under XOR (6 forms, within 1e-6).
- H4: all 8 single-odd gates under the XOR platform give whole Φ > 1e-9.
- H5: parity gates give whole Φ > 1e-9 under all three platforms (6 forms).
