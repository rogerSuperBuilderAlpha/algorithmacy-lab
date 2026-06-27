# Q205 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses, each with its structurally-expected null and the outcome it predicts. Written and
committed before any test runs.

The reference form is the conjunctive-mediator triad **F0**: `W'=S, S'=W∧C, C'=S`, known triadic with
Φ_MIP=2.0. Latency is added by inserting a buffer node **B** that holds the mediator's last output, so the
parties read the mediator one step late: **F1** (represented latency, n=4) is `S'=W∧C, B'=S, W'=B, C'=B`
over labels (W,S,C,B). **F2** (hidden latency) runs F1's dynamics but estimates a one-step state-by-node
TPM over only (W,S,C), marginalizing B, and classifies that.

## H1 — Instrument control
- **Claim:** The immediate triad F0 reads triadic with Φ_MIP = 2.0.
- **H0:** —
- **Predicted outcome:** `verdict(F0).structure == "triadic"` and `max_phi == 2.0`. No comparison number is
  trusted unless this passes.

## H2 — Represented latency preserves integration
- **Claim:** With the delay given its own node, the integrated triad stays integrated: F1 reads triadic
  with Φ_MIP > 0.
- **H0:** Adding a delay buffer factors the form, so F1 reads dyadic.
- **Predicted outcome:** `verdict(F1).structure == "triadic"`, Φ_MIP > 0.

## H3 — The delay node is load-bearing
- **Claim:** The buffer carries the integration rather than sitting inert beside it: the major complex of
  F1 includes the buffer node B.
- **H0:** The buffer is excluded from the core; the irreducible part is still {W,S,C}.
- **Predicted outcome:** `B in major_complex(F1).core`.

## H4 — Hidden latency hides integration
- **Claim:** The same dynamics, observed only on (W,S,C) and read as a one-step TPM, factor: F2 reads
  dyadic (Φ_MIP ≤ PHI_EPS) even though F1 is triadic. The one-step instrument misses lagged coupling when
  the delay is not represented.
- **H0:** The estimated one-step verdict matches the represented one; F2 reads triadic.
- **Predicted outcome:** `verdict(F2).structure == "dyadic"`, Φ_MIP ≈ 0, while F1 is triadic.

## H5 — It is the representation, not the estimation, that breaks integration
- **Claim:** The dyadic reading in H4 is caused by unrepresented latency, not by the TPM-estimation
  procedure: estimating a one-step TPM the same way from F0 (no latency) still reads triadic.
- **H0:** Estimation alone destroys integration; estimated-F0 reads dyadic too, so H4 shows nothing
  specific to latency.
- **Predicted outcome:** `verdict(estimated F0).structure == "triadic"`, Φ_MIP > 0.
