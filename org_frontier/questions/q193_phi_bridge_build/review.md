# q193 — review

## What the probe shows

A per-worker Φ_coord, derived from each simulated worker's W-S-C coordination form, correlates with the
ACS-total factor score at r = +0.42 (95% CI [+0.33, +0.51]) in the bridge cohort and at 0.00 in the
forced-dyadic control. H1 and H2 hold on the synthetic panel. The instrument control passed at the
canonical faithful triad.

## Stress tests a reader should apply

- **Built-in association.** The cohort is simulated so that reported conditions and the ACS-total factor
  score load on one latent. The correlation is a recovery of a planted structure, not a discovery in field
  data. The contribution is that exact Φ recovers it through the Boolean-form bridge, and that the control
  shows the recovery depends on irreducibility.
- **Two-valued Φ_coord.** Φ_coord takes one of two values here (0 or 2), since the bridge maps every
  worker to one of two forms. The correlation is therefore close to a point-biserial between commit-form
  membership and ACS. A richer form family with graded Φ_coord is the next refinement; the magnitude of Φ
  is at most an ordinal hint, per the classifier's standing caveat.
- **Thresholds.** The commit gate uses fixed midpoint thresholds on TI, SA, and SU. The commit rate (49 of
  300) and thus the correlation depend on those cutoffs. A sensitivity sweep over thresholds belongs in a
  follow-up.

## Validation gap

The cohort is simulated and no worker is measured. The study validates the bridge module and the recovery
pipeline, not a measured effect in a real cohort. It supplies the shared `phi_bridge.py` for the later
survey studies on invariance, growth, and sub-competences.
