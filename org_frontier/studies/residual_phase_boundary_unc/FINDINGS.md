# Residual phase boundary on unc k=2 misses — findings (F28)

**F28 verdict (n=4 unc primary): PHASE BOUNDARY vs confident forms; not residual-specific.**
One-bit truth-table flips flip the exact Φ verdict for **37.1%** of neighbours of the 75 n=4
unconstrained k=2 RF misses; every miss has at least one flipping neighbour. Far-hit controls flip
at **15.2%** (+21.8 pp). Near-hit controls flip at **39.2%** (−2.1 pp) — same pattern as the n=3
Probe-131 F28 study.

In-silico; exact IIT-4.0 Φ. Hypotheses fixed in `hypotheses.md` before computing. Size series
4.8% → 7.5% → 9.0% and F27's affine refutation are cited, not reopened.

## Perturbation family

Holding each node's chosen input pair fixed, flip one bit in one node's 2-input truth table
(Hamming-1 in table space). At n=4: **16 neighbours/seed**. Exact Φ before/after; flip = structure
change (triadic ↔ dyadic).

## Census table (n=4 unc)

| set | n | mean one-bit flip | frac ≥1 flip | tri→dya | dya→tri |
|---|---|---|---|---|---|
| residual misses | 75 | **0.371** | **1.000** | 200 | 245 |
| near-hit control (`\|p−0.5\|<0.25`) | 40 | 0.392 | 1.000 | 205 | 46 |
| far-hit control (`\|p−0.5\|≥0.40`) | 75 | 0.152 | 0.587 | 69 | 114 |

| hypothesis | result | detail |
|---|---|---|
| H1 mean ≥ 0.25 and ≥80% any-flip | **SUPPORTED** | 0.371; 100% |
| H2 residual − far-hit ≥ 10 pp | **SUPPORTED** | +21.8 pp |
| H3 residual − near-hit ≥ 5 pp | **REFUTED** | −2.1 pp |

Near-boundary residual subset (n=42): mean flip 0.376 — same sheet as the full residual set.

## Reading

The n=4 unc residual is locally unstable in Boolean function space relative to classifier-confident
forms, and both flip directions occur (slightly more dya→tri among residual neighbours). It is
**not** a residual-only boundary: uncertainty-matched near-hits are at least as unstable. Together
with n=3 F28 (`residual_phase_boundary/`), the holistic residual across the size series lives on a
near-boundary unstable sheet of function space, not on a sharper residual-specific cliff.

## n=5 secondary — deferred

A full n=5 sweep (45 misses + controls × 20 neighbours) was started but stopped after ~25 residual
seeds: exact Φ at n=5 averaged ~2–3 s/neighbour (~1–1.5 h projected for the full controlled design).
Not cheap enough for this turn. The n=4 primary answers F28 for the size-series residual; n=5
replication remains a follow-up.

## Best next experiment

**Done next:** `fn_tail_feature_redesign/` — F28-motivated fragility + algebraic features vs
Probe-131 baseline; honest null (H1–H4 REFUTED). Follow-on there: margin-cascade / selective
exact Φ on low-\|p−0.5\| forms rather than more hand features.

## Reproduce

```
python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_unc.py
python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_unc.py --rebuild      # n=4 ~17 min
python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_unc.py --rebuild --n5 # +n=5, costly
```
