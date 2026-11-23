# The candidate split is refuted: a rule with a singleton-winning party still follows the factor exactly

Both pre-registered hypotheses were refuted. The candidate split failed because (1,1,1,3) quota 3 follows the factor exactly, even though one party can win the vote alone: Φ(0.2, 0) = 0.012971794290726172, Φ(0.2, 0.3) = 0.012548460149892644, Φ(0.2, 0.4) = 0.01083211688194662.

Hypotheses were committed (`8ff4fa78`) before computing. The twelve Φ(η, 0) values used as inputs for MAJ3, 2-of-4 and 3-of-4 were taken from `noise_swap_symmetry` and `swap_symmetry_panel` and disclosed in `hypotheses.md`. Φ(0.2, 0) for (1,1,1,3) quota 3 was measured in this study.

## Scores

- **H1 REFUTED.** At ε = 0.3, MAJ3, 2-of-4 and 3-of-4 all match the factor, as predicted for rules with no singleton-winning party and no veto. (1,1,1,3) quota 3 was predicted to miss, because the weight-3 party is singleton-winning, but it matches: measured 0.012548460149892644 against predicted 0.012548460149892643 (relative error 1.337e-16).
- **H2 REFUTED.** At ε = 0.4, MAJ3 matches the factor, and 2-of-4 and 3-of-4 miss it, as predicted. (1,1,1,3) quota 3 was predicted to miss (total weight 6 is even, and it has a singleton-winning party), but it matches: measured 0.01083211688194662 against predicted 0.010832116881946598 (relative error 1.605e-15).

## Exact numbers (whole Φ)

"pred" is the pre-registered value for MAJ3, 2-of-4 and 3-of-4, or Φ(η, 0) times the pre-registered factor for (1,1,1,3) quota 3. "rel" is |measured − pred| / Φ(η, 0).

| form | η | ε | Φ(η, 0) | predicted | measured | rel | result |
|---|---:|---:|---:|---:|---:|---:|---|
| MAJ3 | 0.05 | 0.3 | 0.015760636493609655 | 0.014610535992724626 | 0.014610535992724627 | 1.101e-16 | match |
| MAJ3 | 0.05 | 0.4 | 0.015760636493609655 | 0.012158205295070305 | 0.012158205295070307 | 1.101e-16 | match |
| MAJ3 | 0.2 | 0.3 | 0.03662371603136496 | 0.03395117459123833 | 0.03395117459123833 | 0.000e+00 | match |
| MAJ3 | 0.2 | 0.4 | 0.03662371603136496 | 0.028252580938481542 | 0.028252580938481646 | 2.842e-15 | match |
| 2-of-4 | 0.05 | 0.3 | 0.01814390272790656 | 0.017551776974094945 | 0.01755177697409494 | 1.912e-16 | match |
| 2-of-4 | 0.05 | 0.4 | 0.01814390272790656 | 0.015151094030519913 | 0.011757248967683449 | 1.871e-01 | miss |
| 2-of-4 | 0.2 | 0.3 | 0.03582202453611982 | 0.034652973775674334 | 0.034652973775674244 | 2.518e-15 | match |
| 2-of-4 | 0.2 | 0.4 | 0.03582202453611982 | 0.029913236983770162 | 0.023212671899405582 | 1.871e-01 | miss |
| 3-of-4 | 0.05 | 0.3 | 0.018143902727906575 | 0.01755177697409496 | 0.017551776974094956 | 1.912e-16 | match |
| 3-of-4 | 0.05 | 0.4 | 0.018143902727906575 | 0.015151094030519924 | 0.011757248967683445 | 1.871e-01 | miss |
| 3-of-4 | 0.2 | 0.3 | 0.0358220245361198 | 0.03465297377567431 | 0.03465297377567427 | 1.162e-15 | match |
| 3-of-4 | 0.2 | 0.4 | 0.0358220245361198 | 0.029913236983770145 | 0.023212671899405585 | 1.871e-01 | miss |
| (1,1,1,3) q3 | 0.2 | 0.3 | 0.012971794290726172 | 0.012548460149892643 | 0.012548460149892644 | 1.337e-16 | match |
| (1,1,1,3) q3 | 0.2 | 0.4 | 0.012971794290726172 | 0.010832116881946598 | 0.01083211688194662 | 1.605e-15 | match |

2-of-4 and 3-of-4 are yes/no mirrors and gave the same values.

The twelve pre-registered numeric claims for MAJ3, 2-of-4 and 3-of-4 all held (matches to relative error ≤ 2.9e-15; misses with relative error 0.187). The two claims for (1,1,1,3) quota 3 did not: both were predicted misses and both matched.

Where 2-of-4 and 3-of-4 missed the factor, at ε = 0.4, the measured / Φ(η, 0) ratio was 0.648 at both η. That ratio was noticed after the run and is not a claimed law.

## What it means

Whether a party can win the vote alone, or whether the rule is the unique majority of an odd total weight, does not tell you when the factor holds. (1,1,1,3) quota 3 has a singleton-winning party and even total weight, and it still follows the factor at both new rates. That is a contrast with (1,1,1,2) quota 2 from `party_noise_factor`, which also has a singleton-winning party and missed the factor at both rates. The contrast is noted; it is not a new rule.

## Limits

One run; the stated rules and rates only; independent party-side flips after probe 464 input noise. At ε = 0, (1,1,1,3) quota 3 has 4 reachable states; at ε ∈ {0.3, 0.4} it has 32, the same count as the matching (1,1,1,2) quota 3 cases in the previous study.

## Reproduce

```sh
python org_frontier/studies/majority_factor_split/run.py --quick   # CI subset, ~9 s
python org_frontier/studies/majority_factor_split/run.py --write   # full run, ~30 s on 8 cores
```
