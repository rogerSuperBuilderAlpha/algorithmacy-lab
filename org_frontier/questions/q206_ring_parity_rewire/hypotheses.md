# Q206 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses, each with its null and predicted outcome, committed before any test runs. All
forms are six-node rings (n=6) with in-degree-2 Watts-Strogatz endpoint rewiring, the q146 machinery. A
**conjunctive** ring sets each node to the AND of its two current inputs; a **parity** ring sets it to the
XOR of its two inputs. Stochastic rewiring points are averaged over three seeds.

## H1 — Instrument control
- **Claim:** The faithful triad `[x1, x0&x2, x1]` reads triadic with Φ_MIP = 2.0.
- **H0:** —
- **Predicted outcome:** triadic, max_phi = 2.000000. No sweep number is trusted unless this passes.

## H2 — The conjunctive inflection sits in (0.25, 0.5)
- **Claim:** On a finer p-grid, the conjunctive ring's verdict first turns dyadic at some p* strictly
  between 0.25 and 0.5, and mean Φ_MIP keeps declining monotonically through the added points.
- **H0:** No dyadic verdict appears below p=0.5, or Φ is non-monotone across the finer grid.
- **Predicted outcome:** at least one added grid point in (0.25, 0.5) shows a dyadic seed; the mean-Φ
  sequence is non-increasing.

## H3 — The parity ring starts at a different Φ
- **Claim:** The parity ring at p=0 has a whole-system Φ_MIP different from the conjunctive ring's 4.0,
  because the parity family scales by a different law (#115).
- **H0:** The parity ring's p=0 Φ_MIP equals 4.0.
- **Predicted outcome:** |parity p=0 Φ_MIP − 4.0| > PHI_EPS.

## H4 — The decline is coupling-general
- **Claim:** The parity ring's mean Φ_MIP also declines under rewiring (monotone non-increasing across the
  swept p-grid): disorder subtracts integration regardless of the coupling family.
- **H0:** The parity ring's Φ holds flat or rises under rewiring.
- **Predicted outcome:** parity mean Φ_MIP at p=1 < parity mean Φ_MIP at p=0, with a non-increasing trend.

## H5 — Parity holds its verdict longer than conjunctive
- **Claim:** The parity ring's verdict turns dyadic at a higher p than the conjunctive ring's: XOR keeps a
  node sensitive to both inputs even after an input is rewired, so integration survives more rewiring.
- **H0:** The two couplings flip dyadic at the same p, or parity flips earlier.
- **Predicted outcome:** the smallest p with any dyadic seed is larger for parity than for conjunctive.
