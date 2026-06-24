# q184 — review

## What was run

Study 2 of the qualitative disagreement line. The probe imports the q183 bridge
`org_frontier.qualitative.disagreement_phi.spread` and applies it to the gig_false_dyad setting:
a driver suggestion account against a platform commit account of one dispatch. Φ is not
reimplemented; the bridge reuses `verdict()` and `major_complex()` from
`org_frontier.probes.lib`.

## What holds

- Instrument control passes: the faithful triad reads triadic with max Φ_MIP = 2.0.
- Consensus control gives zero spread: both parties narrating the same commit account return
  (1, 0.0, 1.0).
- H1 supported: driver account dyadic (Φ_MIP = 0), platform account triadic (Φ_MIP = 2.0),
  verdict_agreement = 0, phi_gap = 2.0 = the platform account's Φ.
- H2 supported: the rider R is in the platform core `{D, P, R}` and absent from the driver core
  `{D, P}`, so core_jaccard = 0.666667 < 1.
- Output is byte-identical across three runs (deterministic, seeded).

## Limits and open points

- The accounts are synthetic. The probe scores divergence between two coded rule sets, not a real
  dispatch. The coded-account-to-observation gap is not addressed.
- The driver account's Φ_MIP = 0 makes phi_gap equal the platform account's Φ by construction.
  This is the expected reading for a dyad-vs-triad split, but it means phi_gap and "platform Φ"
  are not independent quantities here; a richer pair where both accounts carry positive Φ would
  test the gap separately.
- The two accounts are a single hand-built pair chosen to instantiate the false-dyad contrast. The
  spread is read off this one encoding; a later study can vary the rule sets and check the spread
  is stable across encodings of the same narrated disagreement.

## Verdict

Both hypotheses supported on synthetic accounts. The bridge transfers cleanly from q183's
validation controls to a settings application.
