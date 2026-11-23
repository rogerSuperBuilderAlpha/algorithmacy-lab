# When does the party-noise factor hold? A candidate split

Fixed before this study's computation.

## Gap

`party_noise_factor` (PR #960) pre-registered and refuted the claim that
Φ(η, ε) = Φ(η, 0) / (1 + (ε / (1 − ε))^n) holds for new interior and weighted cases at
ε ∈ {0.3, 0.4}. The factor still matched some of those cases exactly (relative error ≤ 2.3e-14):
(1,1,1,2) quota 3 and 3-of-5 at both new ε; and (1,1,2,2) quota 3, 2-of-5 and 4-of-5 at ε = 0.3
only. It missed (1,1,1,2) quotas 2 and 4 at both new ε, and missed the other three rules at
ε = 0.4. Item 1 of `party_noise_factor/BACKLOG.md` asks why.

This study writes down a candidate split in advance and tests it on rules not used in that run:
MAJ3 (2-of-3), 2-of-4, 3-of-4, and (1,1,1,3) quota 3.

## Definitions (fixed)

- A party is *singleton-winning* if its weight alone is at least the quota.
- A party has a *veto* if the other parties' weights sum to less than the quota.
- A rule is the *unique majority of an odd total weight* if the total weight W is odd and the
  quota is (W + 1) / 2.

Applied to the already-run cases (disclosed, not new evidence): (1,1,1,2) quota 3 and 3-of-5 are
unique majorities of odd total weight and have neither a singleton-winning party nor a veto;
(1,1,1,2) quota 2 has a singleton-winning party (the weight-2 voter); quota 4 gives that voter a
veto; (1,1,2,2) quota 3, 2-of-5 and 4-of-5 have neither a singleton nor a veto, but are not
unique majorities of an odd total weight (W = 6 is even; 2-of-5 and 4-of-5 are not quota 3).

## Model

Same construction as `party_noise_factor`: probe 464 `input_tpm`, then party-side flips via
`noisy_tpm`. Whole Φ is the maximum, over reachable states, of the full group's raw φ (IIT 4.0,
PyPhi pin `b78d0e342`). n is the number of parties. A case *matches* the factor if
|measured − predicted| / Φ(η, 0) ≤ 1e-10 when Φ(η, 0) > 1e-9, and if measured whole Φ is 0
(≤ 1e-9) when Φ(η, 0) ≤ 1e-9. A case *misses* if it does not match.

## Values already seen (disclosed)

Committed Φ(η, 0) used as inputs, from `noise_swap_symmetry` (MAJ3) and `swap_symmetry_panel`
(2-of-4, 3-of-4), both at ε = 0:

- MAJ3, η = 0.05: 0.015760636493609655; η = 0.2: 0.03662371603136496.
- 2-of-4, η = 0.05: 0.01814390272790656; η = 0.2: 0.03582202453611982.
- 3-of-4, η = 0.05: 0.018143902727906575; η = 0.2: 0.0358220245361198.

No committed Φ(η, ε) exists for these rules at ε ∈ {0.3, 0.4}. No committed Φ(η, 0) exists for
(1,1,1,3) quota 3; that baseline is measured in this study.

The exact factors are 343/370 at n = 3, ε = 0.3; 27/35 at n = 3, ε = 0.4; 2401/2482 at n = 4,
ε = 0.3; and 81/97 at n = 4, ε = 0.4. Each predicted value below is the committed Φ(η, 0)
multiplied by that factor in ordinary floating-point arithmetic.

## Outcomes

- H1: at ε = 0.3, the factor matches if and only if the rule has no singleton-winning party and
  no veto. Concretely:
  - MAJ3, 2-of-4 and 3-of-4 match the predicted whole Φ below at both η = 0.05 and η = 0.2
    (no singleton, no veto).
  - (1,1,1,3) quota 3 misses the factor at η = 0.2, ε = 0.3 (the weight-3 party is
    singleton-winning). Φ(0.2, 0) for this rule is measured in this study.

- H2: at ε = 0.4, the factor matches if and only if the rule is the unique majority of an odd
  total weight (and so also has no singleton and no veto). Concretely:
  - MAJ3 (W = 3, quota 2) matches the predicted whole Φ below at both η = 0.05 and η = 0.2.
  - 2-of-4 and 3-of-4 miss the factor at both η (W = 4 is even).
  - (1,1,1,3) quota 3 misses the factor at η = 0.2, ε = 0.4 (W = 6 is even, and it has a
    singleton-winning party).

| form | n | η | ε | committed Φ(η, 0) | predicted Φ(η, ε) | H1/H2 claim |
|---|---:|---:|---:|---:|---:|---|
| MAJ3 | 3 | 0.05 | 0.3 | 0.015760636493609655 | 0.014610535992724626 | match |
| MAJ3 | 3 | 0.05 | 0.4 | 0.015760636493609655 | 0.012158205295070305 | match |
| MAJ3 | 3 | 0.2 | 0.3 | 0.03662371603136496 | 0.03395117459123833 | match |
| MAJ3 | 3 | 0.2 | 0.4 | 0.03662371603136496 | 0.028252580938481542 | match |
| 2-of-4 | 4 | 0.05 | 0.3 | 0.01814390272790656 | 0.017551776974094945 | match |
| 2-of-4 | 4 | 0.05 | 0.4 | 0.01814390272790656 | 0.015151094030519913 | miss |
| 2-of-4 | 4 | 0.2 | 0.3 | 0.03582202453611982 | 0.034652973775674334 | match |
| 2-of-4 | 4 | 0.2 | 0.4 | 0.03582202453611982 | 0.029913236983770162 | miss |
| 3-of-4 | 4 | 0.05 | 0.3 | 0.018143902727906575 | 0.01755177697409496 | match |
| 3-of-4 | 4 | 0.05 | 0.4 | 0.018143902727906575 | 0.015151094030519924 | miss |
| 3-of-4 | 4 | 0.2 | 0.3 | 0.0358220245361198 | 0.03465297377567431 | match |
| 3-of-4 | 4 | 0.2 | 0.4 | 0.0358220245361198 | 0.029913236983770145 | miss |
