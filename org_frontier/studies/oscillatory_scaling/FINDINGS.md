# Oscillatory Φ scaling — findings

**Verdict: DIFFERENT_LAW.** The rotating-update ring (limit-cycle
traveling wave, period=n) carries a **constant Φ=2.0** law over
n=3..5 with a full core — separable from every #132 fixed-point
landmark at matched n: and_ring (6→4→4 cap), conjunctive hub (n−1),
parity hub (2^(2−n)). Both rot_ring and and_ring stay triadic, so the
split is a **magnitude law**, not a verdict split. Oscillation adds a
fifth shape the fixed-point zoo does not contain.

In-silico; exact IIT-4.0 major-complex Φ; candid N (n=3..5; n=6
deferred for cost). Hypotheses fixed in `hypotheses.md`. Cited: #10
DELAY_CORE_SHIFT (pointer); #132; Q11 prior. Estimation / construct /
omit / ladder closed.

## Φ vs n

| family | n=3 | n=4 | n=5 | period (n=3..5) | law |
|---|---:|---:|---:|---|---|
| **rot_ring** | **2.0** | **2.0** | **2.0** | 3,4,5 | **constant** |
| and_ring (#132) | 6.0 | 4.0 | 4.0 | 1,2,1 | cap / decay-to-cap |
| conjunctive_hub | 2.0 | 3.0 | 4.0 | 2,2,2 | linear |
| parity_hub | 0.5 | 0.25 | 0.125 | 1,2,1 | decay |

All four families triadic with full core at every listed n.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 different Φ law vs zoo | **SUPPORTED** |
| H2 same zoo landmark | **REFUTED** |
| H3 verdict split dominates | **REFUTED** (both triadic) |

## Reading

Closing a ring is not enough to fix the law — the **update rule**
matters. AND-neighbors collapse to a low-period attractor and cap at
Φ=4; pure cyclic shift keeps a size-tied period and a flat Φ=2. Designed
witness: rot_ring vs and_ring/hub/parity at n=3..5.

## Limits

n≤5; one oscillatory construction (rot_ring); period-as-term /
flip_ring left to Q11 prior. No organization measured.

## Best next experiment

Done: #5 **CORE_SHIFT_NO_FLIP** (`correlated_output_noise/`). Prefer
agenda **#13** (bistability) or **#12** (continuous-time /
stoch-temporal synthesis). Do not reopen estimation / construct /
omit / ladder.

## Reproduce

```
python org_frontier/studies/oscillatory_scaling/analyze_osc.py
```
(~60 s)
