# Ternary pivotality — findings

**Verdict: TWO_CONDITION_STATE_DEPENDENT.** Binary two-condition
control holds. Stock pin still rejects ternary SBS. Vendored overlay
`third_party/pyphi_iit4_mv` (M2) computes exact ternary Φ.

At all-engaged state `(2,2,2)`: two-condition **survives** (non-bidir
out; faithful `{W,S,C}`). At mid-grade `(1,1,1)`: faithful major
complex shrinks (not full triad) — pivotality is **state-dependent**.

In-silico. Cited: probes #11–#12; WAVE10 #5; `pyphi_iit4_mv` M2.
PE / AI / formal / stoch / estimation / construct-omit closed.

## Instrument

| path | decision |
|---|---|
| Stock `feature/iit-4.0` | rejects ternary `(27,27)` |
| Overlay M2 exact Φ | **green** — science runs here |
| (B) embeddings | rejected |

## Hypotheses

| H | result |
|---|---|
| H1 binary two-condition control | **SUPPORTED** |
| H2 stock pin accepts ternary | **REFUTED** |
| H2b overlay exact ternary Φ | **SUPPORTED** |
| H3 ternary non-bidir stays out `@(2,2,2)` | **SUPPORTED** |
| H4 ternary bidir parties in `@(2,2,2)` | **SUPPORTED** |
| H5 state changes pivotality | **SUPPORTED** |

## Ternary panel `@(2,2,2)` (overlay)

| form | core | reading |
|---|---|---|
| faithful | {W,S,C} | bidirectional triad |
| W_sticky / W_omitted | {S,C} | non-bidirectional W out |
| C_sticky | {W,S} | non-bidirectional C out |

Faithful `@(1,1,1)`: core ≠ {W,S,C} (state-dependent shrink).

## Best next

**#2** graded commit / **#3** mixed-radix mediator on the overlay.
Expand the ternary state sweep.

## Reproduce

```
python third_party/pyphi_iit4_mv/smoke_m2.py
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
```
