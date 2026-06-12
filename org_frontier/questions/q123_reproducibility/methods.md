# Q123 — Stage 4 methods (fixed before computation)

The verdict recomputed under config overrides, over the full 256-form strict-mediation family. Run on
`~/iit-playground/venv-4.0/bin/python`; the audit computes in ~8s.

## Build and config (`forms.py`)

`BUILD_COMMIT` records the pinned PyPhi commit (b78d0e342d37175cbd55cf35a6d52ae035b4c50f), which replaces the
moving-branch line in `requirements.txt`. `live_config()` reads the verdict-relevant config keys from the
running environment, so the recorded values are verifiable against the build.

## Checks (`probe_reproducibility.py`)

- `family_verdicts(override)` returns the structure verdict for all 256 forms (`classify_rules`), under an
  optional `pyphi.config.override`.
- `disagreements` counts forms whose verdict differs from the baseline under each override: SYSTEM_CUTS =
  CONCEPT_STYLE, SHORTCIRCUIT_SIA = False, PARALLEL = True, and a plain rerun.
- `alt_measure_admissibility` tries every registered repertoire-distance measure other than
  GENERALIZED_INTRINSIC_DIFFERENCE on the canonical triad, counting those that both run without error and
  return Φ > 0.

## Decision rules

- H1 confirmed if SYSTEM_CUTS = CONCEPT_STYLE gives zero verdict disagreements over 256 forms.
- H2 confirmed if SHORTCIRCUIT_SIA = False gives zero disagreements.
- H3 confirmed if PARALLEL = True and a rerun each give zero disagreements.
- H4 confirmed if zero alternative measures are both admissible and non-degenerate on the triad.
