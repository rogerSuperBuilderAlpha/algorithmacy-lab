# q199 — Φ_coord moves with the construct within a person across waves

The baseline survey studies show a per-worker Φ-based coordination measure correlates with the
algorithmacy construct in a cross-section. A baseline correlation can ride entirely on stable selection:
persons whose coordination tends to commit also tend to score high on algorithmacy, and nothing about
the measure needs to move when a person changes. This study asks the harder question. Across waves, does
within-person change in Φ_coord track within-person change in algorithmacy?

The bridge is the study-1 module. Each worker's reported interdependence, system-authority commit, and
substitutability map to a W-S-C Boolean form, and the form's exact max Φ_MIP is the worker's Φ_coord:
2.0 for the irreducible commit form `S' = W AND C`, 0.0 for the factorizable convey form `S' = W`. The
panel is simulated: 300 persons, 5 waves. Each person has a stable coordination trait, and each wave adds
a within-person coordination state that moves the reported conditions and so moves Φ_coord. ACS-total
loads more on the within-person state than on the stable trait, so a person's algorithmacy rises in the
waves where coordination rises.

Φ_coord is person-mean-centered in the long file into a within-person deviation and a between-person
mean. A multilevel model regresses ACS-total on both. The within coefficient reads how a person's
algorithmacy moves with that person's own wave-to-wave Φ change; the between coefficient reads how
persons with higher average Φ stand on average algorithmacy. Confidence intervals come from a
person-level cluster bootstrap, so the dependence among a person's repeated waves is respected.

The within-person slope is +0.69 with a 95% CI of [+0.63, +0.75], which excludes 0 (H1). Φ_coord moves
together with the construct within a person, beyond the baseline cross-sectional link. The within slope
exceeds the between slope of +0.49, and the bootstrap CI on the difference, +0.20 [+0.09, +0.30],
excludes 0 (H2). The coupling is a person-level dynamic, not only stable selection. The instrument
control passed, and on the forced-dyadic control panel both slopes are 0.

Scope. The panel is simulated and no worker is measured. The within-person coupling is built into the
data-generating model; the test is whether the bridge and the within/between estimator recover it after
person-mean centering. The result is evidence about the instrument and the longitudinal estimator on
synthetic data, and it sets up the growth and sub-competence studies that follow.
