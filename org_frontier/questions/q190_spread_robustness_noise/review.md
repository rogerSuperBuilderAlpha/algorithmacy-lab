# q190 review

## What the probe shows

Bounded elicitation noise on each account's rule table moves verdict_agreement only for pairs at
the dyad/triad boundary. The three pairs of two triads (Φ = 2.0 each) never flipped across 30
draws; the three pairs containing a clean dyad flipped 2, 3, and 4 times. The signed phi_gap never
changed sign. For the disagreeing pairs the gap had signal-to-noise 2.44. H1 and H2 both hold.

## Reuse and determinism

The probe reuses the q183 disagreement-Φ bridge, tpm_from_rules, and max_phi_float. It does not
reimplement Φ. The run is seeded with numpy.random.default_rng per draw and reproduced
byte-identically three times.

## Limits a referee should press

The noise rate (0.10) and pull (0.10) were calibrated once on the anchor forms to keep triads
triadic and clean dyads near the boundary. A heavier rate degrades triads enough to push them
across as well, at which point FAR pairs would also flip. The claim is therefore conditional: under
mild elicitation noise the spread is boundary-local. The probe reports the rate explicitly so the
condition is visible.

The deterministic Boolean forms here give Φ that is either 0 or 2.0, so "near the boundary" means a
clean dyad whose Φ noise can lift, not a form with intrinsically small positive Φ. The study does
not exhibit a form sitting at small positive Φ; that case is left open.

Six pairs is a small panel. The result is a clean separation on a curated span of the boundary, not
a corpus-wide rate. Later studies in this line apply the bridge across settings.

## Scope

Synthetic accounts; exact IIT-4.0 Φ on small Boolean forms. Baselines on synthetic data. The
Φ-to-organization bridge is open.
