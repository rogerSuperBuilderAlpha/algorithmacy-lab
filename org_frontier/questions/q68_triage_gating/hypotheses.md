# Q68 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether a recipient-side triage agent (T) joins the irreducible coordination of an
outreach triad (sender E, message/system M, recipient R). Written and committed before any test runs.

## H1 — A monitoring-only triage agent stays out of the core

- **Claim:** When T reads the message but gates nothing (T'=M; R'=M unchanged), the major complex is the
  base triad {E, M, R} and T is excluded.
- **H0:** T is in the major complex of the monitoring-only form.
- **Predicted outcome:** core = {E, M, R}, T excluded. H0 refuted.

## H2 — A gating-only triage agent stays out of the core

- **Claim:** When T gates delivery but reads nothing (R'=M∧T; T'=T, frozen source), the major complex is
  the base triad and T is excluded.
- **H0:** T is in the major complex of the gating-only form.
- **Predicted outcome:** T excluded. H0 refuted.

## H3 — A bidirectional triage agent joins the core

- **Claim:** When T both reads the message and gates delivery (T'=M and R'=M∧T), T joins the major
  complex.
- **H0:** T is excluded from the major complex of the bidirectional form.
- **Predicted outcome:** T in the core. H0 refuted.

## H4 — The base coordination stays triadic in every configuration

- **Claim:** The major complex is triadic (Φ_MIP > 0) under all three triage configurations; adding the
  triage agent does not collapse the outreach triad.
- **H0:** Some configuration is dyadic on its major complex.
- **Predicted outcome:** triadic in all three. H0 refuted.
