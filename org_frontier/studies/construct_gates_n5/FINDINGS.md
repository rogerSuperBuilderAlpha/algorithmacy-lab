# Construct gate transfer at n=5 — findings

**Verdict: GATE_REGIMES_TRANSFER.** XOR (Regime B) and MAJ (Regime C)
full-bind regimes **transfer** from HMC anchors to CMC and AI-MC at
n=5. AND control stays Regime A (Φ=4 = n−1). No construct morph.

In-silico; binary exact IIT-4.0; n=5 full-bind only (~34 s). Hypotheses
fixed in `hypotheses.md`. Extends `encoding_ladder_gates`
GATE_SPLITS_LADDER, `construct_ladders_n5` BOUNDARY_TRANSFERS,
[`CONSTRUCT_LADDER_ARC.md`](../../CONSTRUCT_LADDER_ARC.md).

## Census

| family | gate | n_core | Φ | whole | regime |
|---|---|---:|---:|---|---|
| HMC† | AND | 5 | 4 | triadic | A |
| HMC† | XOR | 5 | 0.125 | triadic | B |
| HMC† | MAJ | — | — | dyadic | C |
| CMC | AND | 5 | 4 | triadic | A |
| CMC | XOR | 5 | 0.125 | triadic | B |
| CMC | MAJ | 0 | — | dyadic | C |
| AI-MC | AND | 5 | 4 | triadic | A |
| AI-MC | XOR | 5 | 0.125 | triadic | B |
| AI-MC | MAJ | 0 | — | dyadic | C |

† Cited from `encoding_ladder_gates` (not re-run).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 XOR → Regime B both families | **SUPPORTED** |
| H2 MAJ → Regime C both families | **SUPPORTED** |
| H3 some family morphs | **REFUTED** |

## Reading

GATE_SPLITS is construct-robust at full-bind: monotone extremal → A,
affine → B (flip Φ≪n−1), majority → C (no flip). Construct identity
lives in baselines; gate regime lives in the Boolean commit. Closes
the open cell in `CONSTRUCT_LADDER_ARC.md`.

## Limits

Full-bind only (no assist ladder). XOR and MAJ (≥3/4) only among
non-monotone. n=5; n=6 not repeated. No organization measured.

## Best next experiment

Done: [`construct_gates_seal/`](../construct_gates_seal/) GATE_SEAL_HOLDS.
**Arc closable.** Skip residual / cascade / ternary / omit-arc.

## Reproduce

```
python org_frontier/studies/construct_gates_n5/analyze_gates.py
```
(~34 s)
