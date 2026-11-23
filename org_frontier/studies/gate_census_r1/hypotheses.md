# Gate census, switch driven by R1: does the census change if the switch listens to a reader instead of the platform?

Fixed before this study's computation.

## Gap

`gate_census` ran all 16 two-input relayer rules under AND, OR and XOR platforms with the switch copying
the platform (G' = P). All five pre-registered hypotheses held on 48 forms. `gate_source` found that for
the AND gate it did not matter whether P, R1 or C1 drove the switch (whole Φ = 2.0 in each). Its BACKLOG
asked for the census with another driver.

## Model

As `gate_census` (P reads R1, R2; R1' = P; R2' = C1; C1' = f(P, G) for all 16 f; platform AND, OR or XOR),
but the switch copies R1: G' = R1. 48 forms, five members each. Exact IIT 4.0 φ of every reachable subset
in every reachable state; whole Φ = largest full-group φ over states; tie sets pooled.

Control: the AND gate under the AND platform gives whole Φ = 2.0 (`gate_source` and_from_R1).

## Outcomes (threshold 1e-9)

- H1: for every one of the 48 (platform, gate) pairs, whole Φ > 1e-9 here exactly when it was > 1e-9 in
  `gate_census` (same zero/non-zero pattern).
- H2: for every pair, whole Φ here equals the `gate_census` value within 1e-6.
- H3: output negation never changes whole Φ (gate codes c and 15 − c equal within 1e-6, all 24 pairs).
