# Does the post-hoc party-noise factor predict new cases?

Fixed before this study's computation.

## Gap

`weighted_swap_symmetry` (PR #958) found, after looking at its numbers, that interior and weighted
rules so far obey

Φ(η, ε) = Φ(η, 0) / (1 + (ε / (1 − ε))^n)

with n the number of parties, η the input-noise rate, and ε the party-side (output) noise rate. It
matched 60 already-stored points to relative error ≤ 2.0e-14. That formula was not pre-registered.
Item 1 of `weighted_swap_symmetry/BACKLOG.md` asks that it be written down in advance and tested on
new cases: ε ∈ {0.3, 0.4}, five-party interior rules, and weights (1,1,2,2) at quota 3.

## Model

Same construction as `weighted_swap_symmetry`: probe 464 `input_tpm`, then party-side flips via
`noisy_tpm`. Whole Φ is the maximum, over reachable states, of the full group's raw φ (IIT 4.0,
PyPhi pin `b78d0e342`). n = 4 for the four-party rules and n = 5 for the five-party rules.

## Values already seen (disclosed)

Committed Φ(η, 0) used as inputs to the predictions, not as new measurements:

- (1,1,1,2) from `weighted_swap_symmetry/results/results.json` (ε = 0):
  q2, η = 0.05: 0.014972604668929156; q2, η = 0.2: 0.02929897282509204;
  q3, η = 0.05: 0.0038968042400468897; q3, η = 0.2: 0.008896660359373351;
  q4, η = 0.05: 0.014972604668929098; q4, η = 0.2: 0.029298972825091963.
- (1,1,2,2) quota 3 from `five_six_node_quorum_ties/results/results.json` (input noise only, so ε = 0):
  η = 0.05: 0.015392814378989862; η = 0.2: 0.03247030028231149.
- 3-of-5 from the same file: η = 0.1: 0.0017702875158729103; η = 0.2: 0.004260017707949414.

No committed Φ(η, ε) exists at ε ∈ {0.3, 0.4}. No committed Φ(η, 0) exists for 2-of-5 or 4-of-5.

The exact factors used below are 2401/2482 at n = 4, ε = 0.3; 81/97 at n = 4, ε = 0.4;
16807/17050 at n = 5, ε = 0.3; and 243/275 at n = 5, ε = 0.4. Each predicted value is the committed
Φ(η, 0) multiplied by that factor in ordinary floating-point arithmetic.

## Outcomes

A case matches if |measured − predicted| / Φ(η, 0) ≤ 1e-10 when Φ(η, 0) > 1e-9, and if measured
whole Φ is 0 (≤ 1e-9) when Φ(η, 0) ≤ 1e-9.

- H1: each of the twenty cases below, whose Φ(η, 0) is a committed number, matches its predicted
  whole Φ:

| form | n | η | ε | committed Φ(η, 0) | predicted Φ(η, ε) |
|---|---:|---:|---:|---:|---:|
| (1,1,1,2) q2 | 4 | 0.05 | 0.3 | 0.014972604668929156 | 0.014483974137831951 |
| (1,1,1,2) q2 | 4 | 0.05 | 0.4 | 0.014972604668929156 | 0.012502896682301666 |
| (1,1,1,2) q2 | 4 | 0.2 | 0.3 | 0.02929897282509204 | 0.02834280167326591 |
| (1,1,1,2) q2 | 4 | 0.2 | 0.4 | 0.02929897282509204 | 0.024466152565283044 |
| (1,1,1,2) q3 | 4 | 0.05 | 0.3 | 0.0038968042400468897 | 0.003769632143574773 |
| (1,1,1,2) q3 | 4 | 0.05 | 0.4 | 0.0038968042400468897 | 0.003254032406637094 |
| (1,1,1,2) q3 | 4 | 0.2 | 0.3 | 0.008896660359373351 | 0.00860631809945827 |
| (1,1,1,2) q3 | 4 | 0.2 | 0.4 | 0.008896660359373351 | 0.007429169990816923 |
| (1,1,1,2) q4 | 4 | 0.05 | 0.3 | 0.014972604668929098 | 0.014483974137831895 |
| (1,1,1,2) q4 | 4 | 0.05 | 0.4 | 0.014972604668929098 | 0.012502896682301618 |
| (1,1,1,2) q4 | 4 | 0.2 | 0.3 | 0.029298972825091963 | 0.028342801673265836 |
| (1,1,1,2) q4 | 4 | 0.2 | 0.4 | 0.029298972825091963 | 0.02446615256528298 |
| (1,1,2,2) q3 | 4 | 0.05 | 0.3 | 0.015392814378989862 | 0.014890470315856026 |
| (1,1,2,2) q3 | 4 | 0.05 | 0.4 | 0.015392814378989862 | 0.012853793450496689 |
| (1,1,2,2) q3 | 4 | 0.2 | 0.3 | 0.03247030028231149 | 0.03141063294836015 |
| (1,1,2,2) q3 | 4 | 0.2 | 0.4 | 0.03247030028231149 | 0.02711437446254877 |
| 3-of-5 | 5 | 0.1 | 0.3 | 0.0017702875158729103 | 0.001745057025177476 |
| 3-of-5 | 5 | 0.1 | 0.4 | 0.0017702875158729103 | 0.00156429042311679 |
| 3-of-5 | 5 | 0.2 | 0.3 | 0.004260017707949414 | 0.004199303086070716 |
| 3-of-5 | 5 | 0.2 | 0.4 | 0.004260017707949414 | 0.003764306556478937 |

- H2: for 2-of-5 and 4-of-5 at η = 0.2, the ratio Φ(0.2, ε) / Φ(0.2, 0) equals 16807/17050 at ε = 0.3
  and 243/275 at ε = 0.4, at the same tolerance as H1. Φ(0.2, 0) for these two rules is measured in
  this study; it has not been published.
