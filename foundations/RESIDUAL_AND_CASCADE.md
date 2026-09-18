# Cheap features, the holistic residual, and selective exact Φ

*A short synthesis of the 2026-09 residual→cascade arc on branch
`cursor/triad-template-census-6ac4` (PR toward `contrib`). In-silico throughout:
exact IIT-4.0 Φ on small Boolean forms. Evidence about models, not organizations.*

## Throughline

No single cheap signal recovers the dyadic/triadic (Φ_MIP = 0 vs > 0) verdict.
Combining Probe-125/131-style cheap features recovers most of it, but a
**holistic residual** remains. Under controlled base rates that residual
**widens from n=3 to n=4 and then holds near 9% at n=5**. The missed cases sit
on a **phase boundary** with other near-margin forms, not deep in confident
interiors. Expanding the cheap feature set does not close the triadic
false-negative (FN) tail. What does close it, at fixed exact-Φ budget, is a
**margin cascade**: trust the cheap RF except on the most uncertain
`|p−0.5|` band, and spend exact Φ there.

This continues the foundations story in `foundations/SYNTHESIS.md`: structure
beats proxies; combinations beat singles; detection can transfer better than
magnitude — and now, when detection still fails, **when** you call exact Φ
matters more than which new cheap column you add.

## What this arc established

### 1. A fifth catalog template: parity

Among the 24 triadic forms in the 256-form strict-mediation n=3 family, **8
(33%)** sit outside relay / conjunctive / additive / free. They are exactly the
XOR/XNOR commits (Φ_MIP = 0.5). That residual is now the catalog template
**parity** (necessary under the bypass-counterfactual; contingency margin −1.5,
unlike conjunctive’s 0). See `org_frontier/studies/template_coverage_census/`
and the updated `irreducibility_catalog` (51 → 54 entries).

Separately, agenda F27 is **refuted**: the ~4.8% holistic residual on the 4096
wiring panel is **not** the affine/GF(2) class (affine ∩ residual misses =
0/196). Two different residues must not be conflated.

### 2. Size series for the cheap residual (base rate controlled)

| panel | N | triadic rate | RF miss rate |
| --- | ---: | ---: | ---: |
| n=3 Probe 131 | 4096 | 55.9% | **4.8%** |
| n=4 unc k=2 | 1000 | 29.7% | **7.5%** |
| n=5 unc k=2 | 500 | 17.0% | **9.0%** |

Strict-mediation n=4’s apparent “shrink” to 2.4% was a **majority-class
artifact** (triadicity itself 2.4%). Under unconstrained k=2 sampling the forest
predicts both classes; the miss rate steps up n=3→n=4 then holds within a
±2 pp band at n=5. Misses skew toward **triadic false negatives** as triads
get rarer (24.7% FN|tri at n=5 vs 5.8% FP|dya).

Studies: `holistic_residual_n4/`, `holistic_residual_n4_unconstrained/`,
`holistic_residual_n5_unconstrained/`.

### 3. F28 — residual lives on a phase boundary

On the 75 n=4 unc residual misses × 16 one-bit neighbours, mean flip rate of
the exact verdict is **0.371** (100% of forms flip at least once), matching
near-hit controls (0.392) and far above far-hits (0.152). The residual is the
near-boundary band, not a special extra-fragile class beyond other near-hits.
Directions are mixed. See `residual_phase_boundary_unc/`.

### 4. Hand-feature redesign — honest null

F28-motivated fragility features plus algebraic table counts failed
pre-registered thresholds (`fn_tail_feature_redesign/`): n=4 miss 7.5%→7.1%,
FN|tri 10.1%→9.8%; n=5 FN|tri slightly worse. The FN set churned. Missed triads
are nearer the margin and more fragile, but **less** parity-heavy than true
positives — not a parity blind spot. Adding cheap columns under the same RF
protocol does not close this tail.

### 5. Margin cascade — the lever that works

Gating exact Φ by smallest OOF `|p−0.5|` at fixed budget beats always-cheap;
random spend does not; fragility gating adds nothing over margin
(`margin_cascade_phi/`):

| operating point | FN\|tri | miss | exact calls |
| --- | ---: | ---: | ---: |
| always-cheap | 10.1% | 7.5% | 0 |
| B=10% top-B% | **3.7%** | **3.2%** | 100/1000 |
| B=20% top-B% | **0.7%** | **0.9%** | 200/1000 |

n=5: FN|tri 24.7%→10.6% at B=10%.

### 6. Calibration and tooling default

Nested τ-matching ≈ top-B% at matched budget on n=4. **Do not freeze τ across
sizes** (n=4 τ\*=0.2876 overspends on n=5). Lab default:

> **B=10% top-B% ranking on OOF `|p−0.5|`, recomputed per panel.**

Shipped as `org_frontier/cascade/` (`python -m org_frontier.cascade.run`;
`from org_frontier.cascade import margin_cascade`). See
`margin_cascade_tau/` and the cascade README.

## Implications for the foundations program

1. **Exact Φ remains the instrument** on the thin margin. Cheap screening is
   real; cheap closure of the residual is not, under present features.
2. **Size extrapolation** of always-cheap detection should quote the controlled
   series (4.8→7.5→9.0), not the SM base-rate artifact.
3. **Practice:** for larger panels, default to the cascade rather than always
   exact or always cheap. Report always-cheap, cascade@10%, and exact-call count.
4. **Catalog science** and **estimation science** parted cleanly: parity filled
   a template hole among known triads; the holistic residual is a different
   object and needed a different fix (selective exact Φ).

## Open edges (not claimed closed)

- Surrogate *magnitude* prediction remains open; agenda E22 structure-aware
  LOFO screen tested negative on a designed panel
  (`studies/structure_aware_surrogate/` NO_STRUCTURE_GAIN). Spectral
  topology-invariant features (E21) and sample complexity (E23) remain.
- Beyond-binary state, two-triad merger, and further templates past parity are
  structural next gaps, orthogonal to cascade tooling.
- F28 at n=5 was deferred on compute; the n=4 phase-boundary pattern is the
  warrant used here.

## Reproduce pointers

```bash
python org_frontier/studies/template_coverage_census/census.py
python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py
python org_frontier/studies/holistic_residual_n5_unconstrained/analyze_unconstrained_n5.py
python org_frontier/studies/residual_phase_boundary_unc/analyze_phase_boundary.py
python org_frontier/studies/fn_tail_feature_redesign/analyze_fn_redesign.py
python org_frontier/studies/margin_cascade_phi/analyze_cascade.py
python org_frontier/studies/margin_cascade_tau/analyze_tau.py
python -m org_frontier.cascade.run --panel path/to/panel.csv
```

Exact module entry points may vary slightly by PR revision; prefer each study’s
FINDINGS.md reproduce block.
