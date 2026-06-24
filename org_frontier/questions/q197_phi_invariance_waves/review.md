# q197 — review

## What the probe shows

The Φ_coord-to-ACS bridge is metric- and scalar-invariant across three simulated panel waves. ΔCFI is
+0.0063 for freeing the slope and -0.0063 for adding the common intercept, both within the .01 cutoff.
The instrument control passes (faithful triad reads verdict triadic, max_phi 2.0). Output is deterministic
and byte-identical across re-runs under seed 0.

## Strengths

- Φ_coord is recomputed independently at each wave from that wave's reports, so the test is a genuine
  across-wave comparison of the bridge, not a single pooled fit reused three times.
- The permuted-wave-label control, averaged over 200 seeded splits, separates "the test always says
  invariant" from "the test says invariant because the data are invariant." The control's mean ΔCFI sits
  near zero and inside the cutoff.
- Reuses the study-1 bridge module and the exact-Φ machinery rather than reimplementing Φ.

## Limitations

- The cohort is simulated and the Φ-ACS association is built in through a shared stable latent, so
  invariance across waves is expected by construction. The probe confirms the machinery recovers it; it
  does not establish invariance in real data.
- CFI is computed from a hand-rolled normal-theory ML fit on bivariate sufficient statistics rather than
  a full SEM package. The single-predictor case makes the closed-form fits exact, but a real-data run
  should cross-check against semopy or lavaan.
- ΔCFI(metric -> scalar) is negative because the df correction in CFI can favor the more constrained model
  when the added constraint costs almost no fit. The verdict reads "within cutoff," which is correct here,
  but the negative sign should not be read as the scalar model fitting strictly better.
- With Φ_coord taking two values (0 or 2), the predictor distribution is coarse; a real panel with a
  continuous Φ-derived score could behave differently.

## Verdict

H1 and H2 both supported on synthetic data. The result is a property of the bridge instrument; real-wave
validation remains the open step.
