# q198 — Baseline Φ_coord predicts the algorithmacy growth slope in the simulated panel

The survey arm fields an Algorithmacy Competence Scale (ACS) across three waves of a program, alongside
coordination scales: perceived task interdependence, perceived system authority (commit versus convey),
and perceived substitutability. Study q193 derived a per-worker Φ_coord — the exact IIT-4.0 max Φ_MIP of
the W-S-C Boolean form a worker's coordination row maps to — and showed it tracks the ACS construct
cross-sectionally. This study asks the longitudinal question: does a worker's baseline (W1) Φ_coord
predict how fast that worker's algorithmacy competence grows over the program?

The shared bridge module maps one worker's W1 row to a form. Worker and counterpart read the system. The
system rule is the switch: when the worker reports a binding, interdependent, non-substitutable
coordination — interdependence and commit authority above the 7-point midpoint, substitutability below it
— the system commits a joint determination, S' = W AND C, and the form is irreducible (Φ_coord = 2.0,
the faithful mediated triad up to a relabelling). Otherwise the system conveys one party's signal,
S' = W, the form factors along {W,S} | {C}, and Φ_coord = 0.0.

The simulated panel draws 300 workers from one latent coordination factor that fixes each worker's W1
form and W1 Φ_coord. ACS-total at each wave is a per-worker intercept (baseline competence on the latent
plus noise) and a per-worker linear slope times the time code (W1=0, W2=1, W3=2) plus measurement noise.
The per-worker slope mean is lifted by the worker's W1 Φ_coord, so an irreducible W1 form tends to grow
faster. A per-worker latent growth curve (intercept plus linear slope) is fit by OLS over the three
equally-spaced waves, and the recovered slope is regressed on W1 Φ_coord.

The instrument control passed: the faithful triad `[x1, x0&x2, x1]` reads triadic with max Φ_MIP = 2.0.
The recovered mean slope is +0.5232 for commit forms and +0.1953 for convey forms. Regressing the slope
on W1 Φ_coord gives β = +0.1639, 95% CI [+0.1173, +0.2106] — positive with an interval excluding 0, so
H1 is supported. Adding the W1 ACS intercept as a covariate leaves a positive partial coefficient,
β = +0.1894, 95% CI [+0.1388, +0.2400], so Φ_coord is incremental over baseline competence and H2 is
supported. A shuffled-Φ placebo predictor gives β = +0.0033, CI [-0.0469, +0.0536], a CI that includes 0,
and the forced-dyadic control cohort holds Φ_coord at 0 for every worker, leaving the predictor with no
variance. The association therefore rides on the form's irreducibility, not on a scale shared between
Φ_coord and the slope.

Scope. The panel is simulated; no worker is measured and no wave file exists. The growth structure and
the Φ-to-slope coupling are synthetic, built in on purpose, and the probe recovers them through the exact
Φ instrument and the LGC fit. The result is evidence about the bridge and the growth pipeline on synthetic
data, not a measured effect in a real cohort. Real waves (`wave{1,2,3}.csv` per the codebook) would
replace the simulation and convert this scaffold into a confirmatory test. The study extends the q193
bridge from a cross-sectional association to a longitudinal slope and supplies the growth scaffold the
later survey studies (measurement invariance, sub-competences) build on.
