# Switch delay: is the stronger binding with an R1-driven switch just the extra time step?

Fixed before this study's computation.

## Gap

`gate_census_r1` found that driving the switch from the reader R1 instead of the platform P keeps the same
zero/non-zero pattern on all 48 forms but raises 16 values: off-diagonal single-odd AND/OR forms from
0.415037 to 0.830075, non-zero XOR-platform forms from 0.5 to 2.0. Since R1 copies P, an R1-driven switch
holds P from two steps back instead of one. Its BACKLOG asked whether the extra step alone explains the
change.

## Model

P reads R1, R2; R1' = P; R2' = C1; C1' = f(P, G). Three drivers for the switch G:

- **from_P**: G' = P (n = 5, as `gate_census`).
- **from_R1**: G' = R1 (n = 5, as `gate_census_r1`).
- **via_D**: G' = D, D' = P, where D is an extra copier that only feeds G (n = 6). G holds P from two steps
  back, as with from_R1, but G does not read a member of the platform's reading set.

Gates and platforms: AND gate (code 8) and P ∧ ¬G (code 4) under the AND platform; AND gate (code 8) under
the XOR platform. 3 × 3 = 9 forms. Exact IIT 4.0 φ of every reachable subset in every reachable state;
whole Φ = largest full-group φ over states.

Controls: from_P and from_R1 reproduce `gate_census` and `gate_census_r1` (AND_g08 2.0/2.0, AND_g04
0.415037/0.830075, XOR_g08 0.5/2.0).

## Outcomes (threshold 1e-6 for equality)

- H1: via_D AND_g04 whole Φ = 0.830075 (the from_R1 value).
- H2: via_D XOR_g08 whole Φ = 2.0 (the from_R1 value).
- H3: via_D AND_g08 whole Φ = 2.0.
- Delay explanation: SUPPORTED only if H1 and H2 both hold.
