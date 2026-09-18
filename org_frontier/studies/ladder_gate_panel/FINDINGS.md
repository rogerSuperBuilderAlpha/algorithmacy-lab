# Ladder-gate stratified panel — findings

**Verdict: RULE_HOLDS_PANEL.** MONO_EXTREMAL_VS_AFFINE holds on a
stratified panel of **448** four-input gates at n=5 full bind:
accuracy **448/448**, zero counterexamples, zero ambiguous full-flip Φ.

```
if alldep ∧ affine:                 → B
elif alldep ∧ monotone ∧ wt∈{1,15}: → A
else:                               → C
```

In-silico; binary exact IIT-4.0. Hypotheses fixed in `hypotheses.md`.
Extends `ladder_gate_properties`. Exhausted monotone / affine /
extremal-weight slices plus 64 random residual (seed 20260916).

## Panel

| stratum | n | accuracy |
|---|---:|---|
| A_pred (monotone extremal alldep) | 4 | 4/4 |
| B_pred (affine alldep) | 2 | 2/2 |
| monotone (remainder) | 330 | 330/330 |
| extremal_wt (remainder) | 28 | 28/28 |
| affine (remainder) | 20 | 20/20 |
| random residual | 64 | 64/64 |
| **total** | **448** | **448/448** |

## Confusion

| pred→obs | count |
|---|---:|
| A→A | 4 |
| B→B | 2 |
| C→C | 442 |

No A↔C or B↔C swaps. No `?` (triadic n_core=5 with Φ neither ≈4 nor ≪1).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 rule holds on panel | **SUPPORTED** |
| H2 counterexamples appear | **REFUTED** |
| H3 refinement needed | **REFUTED** |

## Reading

The designed-16 rule survives exhaustive monotone and affine slices of
the 4-input cube. Monotone non-extremal gates stay C. Extremal-weight
gates that are not fully monotone stay C. Affine gates that miss a
variable stay C. Random residual gates stay C (some partial-triadic
with incomplete cores — still not A/B).

## Limits

n=5 full-bind only; not all 2¹⁶ functions (random stratum is a sample).
Assist not re-run per gate. No organization measured.

## Best next experiment

Role-target grain on another indeg (`indeg_002122_grain` sibling). Skip
residual / cascade / ternary / omit-arc unless tooling lands. Optional:
5-input gate panel (costly).

## Reproduce

```
python org_frontier/studies/ladder_gate_panel/analyze_panel.py
```
(~5 min)
