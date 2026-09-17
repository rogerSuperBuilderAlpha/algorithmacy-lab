# Ternary pivotality — findings

**Verdict: NOT_TESTABLE.** Instrument path **(C)**. Exact IIT-4.0 on
this lab’s PyPhi pin **rejects** ternary n=3 SBS `(27,27)`. Paths (A)
port and (B) embeddings were evaluated and rejected for #1 (see
`INSTRUMENT.md`). Binary two-condition control **holds**. Ternary
pivotality (H3–H5) remains **open**, not a scientific null.

In-silico. Hypotheses fixed after the instrument decision. Cited:
probes #11–#12; WAVE10 #5; `shared_mediator_ternary/` pointer. PE / AI /
formal / stoch / estimation / construct-omit closed.

## Instrument

| path | decision |
|---|---|
| (A) multivalued IIT-4.0 port | not this turn (pin-level) |
| (B) embedding/proxy | rejected — does not answer party-level exact Φ |
| **(C) NOT_TESTABLE** | **chosen** |

Capability error: no `num_states_per_node`; SBS `(27,27)` broadcast
fails against binary `(16,16)`. Same pin class as
`shared_mediator_ternary/`.

## Hypotheses

| H | result |
|---|---|
| H1 binary two-condition control | **SUPPORTED** |
| H2 IIT-4.0 accepts ternary n=3 | **REFUTED** |
| H3 ternary non-bidir stays out | **NOT_TESTABLE** |
| H4 ternary bidir parties in | **NOT_TESTABLE** |
| H5 graded changes pivotality | **NOT_TESTABLE** |

## Binary control (witnesses)

| form | core | reading |
|---|---|---|
| faithful | {W,S,C} Φ=2 | bidirectional triad |
| W_sticky / W_omitted | {S,C} | non-bidirectional W out |
| C_sticky | {W,S} | non-bidirectional C out |

## Reading

Agenda #1 / WAVE10 #5 needs multivalued IIT-4.0 before any claim that
ternary idle/engaged/overcommitted parties change (or preserve)
pivotality. The binary two-condition account is healthy on this
instrument; the graded question is blocked, not answered.

## Best next

**#2–#4** share the same pin gate. Residual: path **(A)** multivalued
IIT-4.0. Do not run #2–#4 science until the instrument opens.

## Reproduce

```
python org_frontier/studies/ternary_pivotality/analyze_pivot.py
```
(<1 s)
