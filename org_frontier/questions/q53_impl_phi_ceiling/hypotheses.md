# Q53 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether back-channel topology or graded coupling can restore matched-read
implication commits {2,4,11,13} to Φ=2.0. Written and committed before any test runs. Grows from Q51
probes #155, #159 and Q52 probe #164.

## H1 — Counterpart-side AND back-channel restores Φ=2.0
- **Claim:** A minimal counterpart-side AND gate (C' = old_C & W) lets at least one matched-read implication
  form reach Φ=2.0, exploiting the C-centric distinguishing state W=0,C=1 that the worker-side topology
  under-serves.
- **H0:** Zero of eight matched forms reach Φ≥2.0 − 1e−9 under counterpart-side AND.
- **Predicted outcome:** At least one form at the ceiling. H0 is refuted if any form hits 2.0; H0 is
  confirmed if none do.

## H2 — OR-graded worker-side back-channel restores Φ=2.0
- **Claim:** Weaker OR coupling on the worker channel (W' = old_W | C) passes the counterpart bit more
  freely than AND and can recover the four-edge ceiling for matched implication.
- **H0:** Zero of eight matched forms reach Φ≥2.0 − 1e−9 under worker-side OR.
- **Predicted outcome:** At least one form at the ceiling. H0 is refuted if any form hits 2.0.

## H3 — XOR parity gates exceed the 0.830075 symmetric-AND equilibrium
- **Claim:** XOR gates on back-channel edges (worker-side, counterpart-side, or symmetric) raise max_phi
  above 0.830075 for at least one matched-read implication form.
- **H0:** No matched form under any of the three XOR topologies exceeds 0.830075 + 1e−6.
- **Predicted outcome:** At least one form above 0.830075. H0 is refuted if any exceed; H0 is confirmed if
  all stay at or below.

## H4 — No tested topology restores Φ=2.0
- **Claim:** Across the finite back-channel panel — worker-AND, counterpart-AND, symmetric-AND, worker-OR,
  counterpart-OR, symmetric-OR, cross (W-OR/C-AND), cross (W-AND/C-OR) — zero matched-read implication
  forms reach Φ=2.0.
- **H0:** At least one (topology, form) pair reaches Φ≥2.0 − 1e−9.
- **Predicted outcome:** Zero at ceiling across the full 8×8 = 64 pair panel. H0 is refuted if any pair hits
  2.0.

## H5 — Supremum is exactly 0.830075 and symmetric-AND saturates it
- **Claim:** The maximum max_phi over all eight topologies and all eight matched forms equals 0.830075; the
  symmetric-AND panel achieves that value on all eight forms with zero spread.
- **H0:** Some pair exceeds 0.830075 + 1e−6, or fewer than eight symmetric-AND forms land at 0.830075.
- **Predicted outcome:** Global max = 0.830075; symmetric-AND: eight of eight at 0.830075, spread 0. H0 is
  refuted if any exceed or symmetric-AND deviates.
