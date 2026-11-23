# Deal links between buyers and sellers decide whether the platform binds a pair or is left out

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `0effcf7c` before computation. Controls passed: conjunctive triad whole Φ = 2.000000;
`asymmetric_sides` side_link_and reproduces whole Φ = 0.830075.

## Setup

Platform P, buyers B1, B2, sellers S1, S2; P' = (B1 ∨ B2) ∧ (S1 ∨ S2) except strict_buyers_4.
"Top" is the largest subset φ over reachable states; ties are within 1e-9 at the first state where it
occurs.

| form | party rules | states | whole Φ | top φ | top ties |
|---|---|---:|---:|---:|---|
| side_link_and (control) | Bi' = P ∧ Bj, Si' = P ∧ Sj | 17 | 0.830075 | 2.000000 | B1B2, S1S2 |
| cross_and | B1' = P ∧ S1, S1' = P ∧ B1 (same for pair 2) | 17 | 0.830075 | 6.000000 | PB1S1 |
| cross_or | B1' = P ∨ S1, S1' = P ∨ B1 (same for pair 2) | 17 | 1.192645 | 2.000000 | B1S1, B2S2 |
| one_pair_off | B1' = S1, S1' = B1; B2, S2 copy P | 14 | 0 | 2.000000 | B1S1 |
| one_pair_and | B1' = P ∧ S1, S1' = P ∧ B1; B2, S2 copy P | 9 | 0 | 2.000000 | PB2, PS2, B1S1, PB2S2 |
| strict_buyers_4 | P' = (B1 ∧ … ∧ B4) ∧ (S1 ∨ S2); copy P | 4 | 0 | 4.000000 | PB1B2B3B4 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** cross_and is integrated as a whole (Φ = 0.830075, in 2 of 17 states) but its top unit is
  not the pairs alone: it is the platform with one trading pair, {P, B1, S1} at φ = 6.0 (state P=1, B1=1,
  S1=1, others 0), and {P, B2, S2} in the mirror state. In the other seven states with positive top φ, the
  pairs {B1, S1}, {B2, S2} tie at φ = 2.0.
- **H2 REFUTED.** Under cross_or the top units are the pairs without P ({B1, S1}, {B2, S2}, φ = 2.0), in
  every state where top φ is positive; whole Φ is 1.192645 in two states and 0.415037 in five.
- **H3 SUPPORTED as scored, with a caveat.** The off-platform pair {B1, S1} is a unit at φ = 2.0 in all 14
  states, and the first top tie set has no P. But in state P=1, B2=1, S2=1 (B1=S1=0), {P, B2}, {P, S2} and
  {P, B2, S2} tie with it at 2.0; pooled over states, P does appear in a top tie.
- **H4 REFUTED.** one_pair_and has whole Φ = 0.
- **H5 SUPPORTED.** Four strict buyers give top φ = 4.0 with {P, B1, B2, B3, B4} as the only top tie.

## Reading

Compare with `asymmetric_sides`, where links ran *within* a side:

| link | within a side (`asymmetric_sides`) | across sides (this study) |
|---|---|---|
| "and" | sides bind alone (φ 2.0); whole 0.830075 | platform + one pair (φ 6.0); whole 0.830075 |
| "or" | platform + idle side (φ 6.0); whole 0 | pairs bind alone (φ 2.0); whole up to 1.192645 |

The type of link and its direction swap which unit is tightest. Under "and" deal links a trade needs both
the platform's signal and the partner, so in the state where only one pair is active the platform and
that pair are bound tightly. Under "or" deal links the pair can keep itself going without the platform,
and the pair becomes its own unit. The whole system is never the tightest unit in any form here.

The strict-side series now reads 2.0, 3.0, 4.0 for two, three, four strict buyers, the hub law Φ = n − 1
applied to the platform plus its strict side.

## What it means

When buyers and sellers can deal directly, whether the platform stays inside the tightest-bound unit
depends on the kind of link. If a deal needs both the partner and the platform, the platform binds that
pair hard. If either is enough, the pair holds together without the platform. For algorithmacy this
separates a platform that is a binding third party to a relationship from one that the relationship can
route around.

## Limits

Binary, deterministic, synchronous; n ≤ 7; one platform rule (side_match) for the link forms. Ties at the
1e-9 cutoff and read at the first top state. The φ = 6.0 three-node units are reported as computed; we
have not derived them.

## Reproduce

```sh
python org_frontier/studies/off_platform_deals/run.py --quick   # CI subset, ~25 s
python org_frontier/studies/off_platform_deals/run.py --write   # full run, ~90 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
