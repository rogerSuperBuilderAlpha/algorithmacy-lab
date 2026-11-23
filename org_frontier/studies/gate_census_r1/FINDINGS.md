# Moving the switch's driver from the platform to a reader keeps who binds, but changes how much

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `92605378` before computation. Control passed: the AND gate under the AND platform gives whole
Φ = 2.000000 (`gate_source` and_from_R1).

## Setup

As `gate_census`, with G' = R1 instead of G' = P. Gate code: output for (P, G) is bit 2·P + G.

Whole Φ by platform and gate class (G' = R1; `gate_census` G' = P value in brackets where different):

| gate class (codes) | AND platform | OR platform | XOR platform |
|---|---|---|---|
| constant (0, 15) | 0 | 0 | 0 |
| P-only (3, 12) | 0 | 0 | 0 |
| G-only (5, 10) | 2.0 | 2.0 | 2.0 [0.5] |
| parity (6, 9) | 2.0 | 2.0 | 2.0 [0.5] |
| single-odd at (1, 1) (7, 8) | 2.0 | 0 | 2.0 [0.5] |
| single-odd at (1, 0) (4, 11) | 0.830075 [0.415037] | 0 | 2.0 [0.5] |
| single-odd at (0, 1) (2, 13) | 0 | 0.830075 [0.415037] | 2.0 [0.5] |
| single-odd at (0, 0) (1, 14) | 0 | 2.0 | 2.0 [0.5] |

Whole Φ > 0 in 28 of 48 forms, the same 28 as `gate_census`. 16 values differ. With G' = R1 the
reachable state counts are larger (12–32 vs 8–16). Per-form tie sets are in
[results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Zero/non-zero whole Φ matches `gate_census` on all 48 forms.
- **H2 REFUTED.** 16 of 48 values differ (listed above and in `results.json` under `differences`).
- **H3 SUPPORTED.** Gate codes c and 15 − c give equal whole Φ on all 24 pairs.

## Reading

Which (platform, gate) pairs make the whole group irreducible does not depend on whether the switch
follows the platform or a reader. The rules found in `gate_census` carry over unchanged: output negation
never matters, gates that ignore the switch give 0, and for AND/OR the P-value rule holds. The amount does
change. The off-diagonal forms double from 0.415037 to 0.830075, and the XOR platform goes from 0.5 to
the full 2.0 in every non-zero form. Following R1 puts the switch one step further from P (G = P two steps
back), and the larger reachable state space may account for the change. That was not tested.

## What it means

Whether a switch-dependent go-between stays bound with the platform is set by the rules involved. It does
not depend on which group member works the switch, at least between the platform and a direct reader. How
tightly the whole holds together does depend on who works the switch.

## Limits

Binary, deterministic, synchronous; n = 5; drivers P (in `gate_census`) and R1 only. Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/gate_census_r1/run.py --quick   # CI subset, ~25 s
python org_frontier/studies/gate_census_r1/run.py --write   # full run, ~9 min (reads gate_census results)
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
