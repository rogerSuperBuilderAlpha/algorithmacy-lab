# Construct gate seal — findings

**Verdict: GATE_SEAL_HOLDS.** XNOR (Regime B) and mixed-polarity
AND_negE (Regime C) transfer on CMC and AI-MC full-bind at n=5.
GATE_REGIMES_TRANSFER is sealed. The construct/gate arc is **closable**.

In-silico; binary exact IIT-4.0; four cells (~24 s). Hypotheses fixed
in `hypotheses.md`. Extends `construct_gates_n5`,
`encoding_ladder_gates`, `ladder_gate_properties`,
[`CONSTRUCT_LADDER_ARC.md`](../../CONSTRUCT_LADDER_ARC.md).

## Census

| family | gate | n_core | Φ | whole | regime |
|---|---|---:|---:|---|---|
| HMC† | XNOR | 5 | 0.125 | triadic | B |
| HMC† | AND_negC | 2 | 2 | dyadic | C |
| CMC | XNOR | 5 | 0.125 | triadic | B |
| CMC | AND_negE | 2 | 2 | dyadic | C |
| AI-MC | XNOR | 5 | 0.125 | triadic | B |
| AI-MC | AND_negE | 2 | 2 | dyadic | C |

† Cited (XNOR from `encoding_ladder_gates`; AND_negC from
`ladder_gate_properties`).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 XNOR → Regime B | **SUPPORTED** |
| H2 AND_negE → Regime C | **SUPPORTED** |
| H3 surprise flip / morph | **REFUTED** |

## Reading

Affine dual (XNOR) and mixed-polarity extremal (AND_negE) match HMC
on both construct families. Gate regime is Boolean-commit, not
construct-identity. No further ladder/indeg churn needed on this
thread.

## Limits

Four designed cells; n=5 only. AND_negE negates the last outer (CMC/AI-MC
E), mirroring HMC AND_negC. No organization measured.

## Best next experiment

**Arc closable.** Stop construct/gate ladder churn on this thread.
Agenda items outside it (not more indeg/ladder unless a real gap):
empirical arm or survey packet; Paper-2 IIT affirmative case polish;
omit-tooling if residual/cascade ever lands. Skip residual / cascade /
ternary / omit-arc here.

## Reproduce

```
python org_frontier/studies/construct_gates_seal/analyze_seal.py
```
(~24 s)
