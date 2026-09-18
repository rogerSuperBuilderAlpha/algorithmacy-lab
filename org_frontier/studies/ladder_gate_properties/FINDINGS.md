# Ladder-gate Boolean properties — findings

**Verdict: MONO_EXTREMAL_VS_AFFINE.** Over a designed 16-gate set at n=5
(anchors + property probes), regime membership is predicted exactly by:

```
if depends_on_all ∧ affine:                 → B   (Φ≪n−1 flip)
elif depends_on_all ∧ monotone ∧ wt∈{1,15}: → A   (Φ=n−1 flip)
else:                                       → C   (no flip)
```

Accuracy **16/16**. Weaker filters (canalizing alone, extremal weight
alone, unate∧canalizing∧extremal without full monotonicity) **fail** —
witnesses AND_negC / OR_negC / AND_negAB / OR_negAB (extremal + canalizing
+ unate, but mixed polarity → Regime C, Φ=2 or none).

In-silico; binary exact IIT-4.0; n=5 full-bind census. Hypotheses fixed
in `hypotheses.md`. Extends `encoding_ladder_gates` GATE_SPLITS_LADDER.

## Property → regime

| gate | obs | mono | aff | canal | ext wt | wt | rule |
|---|---|---|---|---|---|---:|---|
| AND / OR / NAND / NOR | **A** | Y | N | Y | Y | 1/15 | A |
| XOR / XNOR | **B** | N | Y | N | N | 8 | B |
| MAJ3 / T2 / MIN1 / MIXED / AND_of_ORs | **C** | Y | N | N | N | — | C |
| AND_negC / OR_negC / AND_negAB / OR_negAB | **C** | N | N | Y | Y | 1/15 | C |
| XOR3_and_D | **C** | N | N | Y | N | 4 | C |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 A ↔ monotone∧extremal∧alldep | **SUPPORTED** |
| H2 B ↔ affine∧alldep | **SUPPORTED** |
| H3 residual → C | **SUPPORTED** |
| H4 weaker props fail to predict A | **SUPPORTED** |

## Reading

PHI_TRACKS_NM1 is not “any joint bind.” It is the **monotone extremal**
slice of the Boolean cube — AND/OR of all inputs, or their negations
(NAND/NOR). Affine full dependence (parity) still flips but collapses Φ.
Monotone non-extremal (majority, threshold-2, mixed) and mixed-polarity
extremal (AND with a negated literal) do not flip. Canalization without
full monotonicity is not enough.

## Limits

Designed n=5 set (16 gates), not all 2¹⁶ functions. Properties are
classical Boolean; no organization measured. Assist is secondary
(2-arg freeze restriction).

## Best next experiment

Done: [`ladder_gate_panel/`](../ladder_gate_panel/) RULE_HOLDS_PANEL
(448/448 stratified). Next: role-target grain on another indeg. Skip
residual / cascade / ternary / omit-arc.

## Reproduce

```
python org_frontier/studies/ladder_gate_properties/analyze_properties.py
```
(~1 min)
