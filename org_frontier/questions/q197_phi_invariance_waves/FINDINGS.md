# q197 — findings

The Φ_coord-to-ACS bridge holds metric and scalar invariance across the three simulated panel waves. A
fixed Φ_coord maps to the same expected ACS level at every wave.

## Per-wave bridge structure (Φ_coord recomputed from wave-specific reports)

| wave | n   | mean Φ | var Φ  | r(Φ, ACS) | slope b | intercept a |
|------|-----|--------|--------|-----------|---------|-------------|
| W1   | 240 | 0.3667 | 0.5989 | 0.4589    | 0.5917  | -0.2170     |
| W2   | 240 | 0.3750 | 0.6094 | 0.3681    | 0.4705  | -0.1765     |
| W3   | 240 | 0.2917 | 0.4983 | 0.4650    | 0.6573  | -0.1917     |

## Invariance of ACS-on-Φ (CFI and ΔCFI)

| step                      | bridge CFI | ΔCFI    | control mean ΔCFI |
|---------------------------|------------|---------|-------------------|
| configural                | 1.0000     | —       | —                 |
| metric (common slope)     | 0.9937     | +0.0063 | +0.0036           |
| scalar (common intercept) | 1.0000     | -0.0063 | -0.0026           |

ΔCFI(configural -> metric) = +0.0063 <= .01: the slope is stable across waves. ΔCFI(metric -> scalar) =
-0.0063 <= .01: adding the common-intercept constraint does not worsen fit, so the intercept is stable.
The permuted-wave-label control holds invariance trivially (mean ΔCFI metric +0.0036, scalar -0.0026,
both within the cutoff), confirming the test does not flag non-invariance only because the panel is
synthetic.

## Verdicts

- H1 (metric invariance, slope equal across W1-W3, ΔCFI <= .01): SUPPORTED.
- H2 (scalar invariance, intercept equal across W1-W3, ΔCFI <= .01): SUPPORTED.

## Scope

Simulated cohort. No worker is measured. The verdicts are a property of the bridge instrument on
synthetic data; the same pipeline on real waves is the unperformed validation step.
