# Genuine bistability — findings

**Verdict: GENUINE_COEXISTENCE.** Fixed couplings host coexisting
triadic and dyadic attractors — beyond #109's sticky-mediator activity
hysteresis. On a 9-form n=3 panel, **6/9** are COEXIST (memoryless,
xor_memory, or_commit, sticky_or, sticky_parity, w_follows_c). The
#109 sticky form is **MULTI_SAME**: two dyadic fixed points (000, 111)
plus an activity hysteresis gap of **0.066** — path dependence without
cross-verdict bistability.

In-silico; exact IIT-4.0 Φ_MIP on attractor states; basin sizes over
the 8-state space. Hypotheses fixed in `hypotheses.md`. Cited: #109,
#43; #5 pointer only. Estimation / construct / omit / ladder closed.

## Regime map

| form | tag | n_attr | tri | dya | whole |
|---|---|---:|---:|---:|---|
| memoryless | **COEXIST** | 3 | 1 | 2 | tri Φ=2 |
| sticky (#109/#43) | MULTI_SAME | 2 | 0 | 2 | dya Φ=0 |
| xor_memory | **COEXIST** | 2 | 1 | 1 | tri Φ=2 |
| or_commit | **COEXIST** | 3 | 1 | 2 | tri Φ=2 |
| sticky_or | **COEXIST** | 2 | 1 | 1 | tri Φ=2 |
| sticky_parity | **COEXIST** | 2 | 1 | 1 | tri Φ=0.5 |
| parity_hub | SINGLE | 1 | 1 | 0 | tri Φ=0.5 |
| maj3 | MULTI_SAME | 2 | 0 | 2 | dya Φ=0 |
| w_follows_c | **COEXIST** | 2 | 1 | 1 | tri Φ=2 |

## Witness attractors (memoryless vs sticky)

| form | cycle | basin | Φmax | verdict |
|---|---|---:|---:|---|
| memoryless | 111 | 1 | 2.000 | **triadic** |
| memoryless | 000 | 3 | 0 | dyadic |
| memoryless | 010\|101 | 4 | 0 | dyadic |
| sticky | 000 | 3 | 0 | dyadic |
| sticky | 111 | 5 | 0 | dyadic |

## vs #109

| | sticky | memoryless |
|---|---:|---:|
| activity hysteresis area | 0.0712 | 0.0051 |
| attractor Φ pattern | both dyadic | triadic + dyadic |

Sticky latches activity under a drive ramp; it does not host a triadic
attractor. Cross-verdict coexistence is the memoryless / xor-memory
family's property, not the sticky loop's.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 coexistence regime exists | **SUPPORTED** (6/9 forms) |
| H2 only hysteresis, no coexistence | **REFUTED** |
| H3 multistable same-verdict (no H1) | **REFUTED** (sticky/maj3 remain MULTI_SAME witnesses) |

## Reading

The whole-form classifier's max-Φ label hides attractor structure.
Under the clean triad, initial condition selects a triadic fixed point
(111) or a dyadic basin (000 / period-2). Sticky memory erases the
triadic attractor and replaces coexistence with same-verdict
multistability plus activity hysteresis. Genuine dyadic↔triadic
bistability is therefore common on ordinary couplings and is not the
#109 phenomenon. Designed witnesses: memoryless COEXIST vs sticky
MULTI_SAME + #109 area gap.

## Limits

n=3 deterministic Boolean panel only; no continuous stickiness
parameter; Φ read on attractor states (not trajectory-averaged). No
organization measured.

## Best next experiment

Prefer agenda **#12** (continuous-time / stoch-temporal synthesis) or
**#14** (adaptive mediator toward higher Φ). Do not reopen estimation
/ construct / omit / ladder.

## Reproduce

```
python org_frontier/studies/genuine_bistability/analyze_bistability.py
```
(~3 s)
