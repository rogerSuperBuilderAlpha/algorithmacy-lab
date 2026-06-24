# q193 — A per-worker Φ coordination measure for the algorithmacy panel

The survey arm fields an Algorithmacy Competence Scale alongside coordination scales: perceived task
interdependence, perceived system authority (commit versus convey), and perceived substitutability. The
classifier line, separately, reads a coordination form as a small W-S-C Boolean system and grades its
irreducibility with exact IIT-4.0 Φ over the minimum-information partition. This study joins the two. It
asks whether a per-worker Φ-based coordination measure, derived from each simulated worker's coordination
form, predicts the latent algorithmacy construct in the panel.

The bridge module `phi_bridge.py` maps one worker's row to a form. Worker and counterpart read the
system. The system rule is the switch. When the worker reports a binding, interdependent, non-substitutable
coordination — interdependence and commit authority above the scale midpoint, substitutability below it —
the system commits a joint determination, S' = W AND C, and the form is irreducible (Φ_coord = 2.0). This
is the faithful mediated triad up to a relabelling. Otherwise the system conveys a single party's signal,
S' = W, the form factors along {W,S} | {C}, and Φ_coord = 0.0. Φ_coord is the form's max exact Φ_MIP,
computed by reusing `classifier.tpm_from_rules` and `probes.lib.max_phi_float`.

The simulated cohort draws 300 workers from one latent coordination factor. The reported conditions load
on that factor and the ACS-total factor score loads on the same factor plus independent noise, so an
irreducible form tends to co-occur with higher algorithmacy. Across the cohort, Φ_coord correlates with
ACS-total at r = +0.42, 95% CI [+0.33, +0.51]. The 49 workers on the commit form score above the 251 on
the convey form.

A control cohort forces every system rule to the pass-through S' = W, so Φ_coord is identically 0. The
correlation falls to 0. The bridge association rides on the form's irreducibility, since removing the
irreducibility while holding the scales fixed removes the association.

The result establishes the bridge as a working measure and supplies the shared module the later survey
studies use. Those studies test measurement invariance, growth across waves, and the sub-competences. The
cohort here is simulated and no worker is measured, so the correlation is evidence about the instrument
and the bridge on synthetic data. It shows the pipeline recovers a built-in structure through exact Φ, and
marks where a real panel's responses would enter.
