# Q6 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether Φ_MIP undergoes a phase transition as commit noise rises, for the
triadic conjunctive mediated form S' = W∧C realized with reliability 1−p (the commit flips with
probability p). The sweep runs p on a fine grid from the clean limit p=0 to the random commit p=0.5,
reads Φ_MIP, its first derivative dΦ/dp, the dyadic/triadic verdict, and the MIP location at each
step. Written and committed before any test runs. The review's prior probes (#27, #38, #34, #81, #79,
#26/#33/#16) and the deep-research precedents (Mediano 2019; Niizato 2024, 2020; Popiel 2020;
Aguilera 2019; Danilczuk 2026; Kelso 1984) supply the structural priors each null rests on.

The probe computes IIT-4.0 exact Φ_MIP via PyPhi, with the commit flip modeled as continuous output
noise on the TPM (each clean transition row mixed toward the flipped output with weight p), so the
noise is part of the mechanism's TPM, not an initial-state injection. This modeling choice is fixed
here per Aguilera (2019), which shows initial-injection IIT can zero the critical signature.

## H1 — Mean Φ_MIP decays smoothly, with no kink and no interior discontinuity
- **Claim:** Φ_MIP(p) is a smooth, monotone-decreasing function of p on the open interval (0, 0.5),
  with no jump, no corner, and no interior critical point. On a fine grid the curve is well fit by a
  smooth low-order form (e.g. a quadratic or exponential decay), and the residual from such a fit
  shows no localized spike that a coarse 6–7-point sample would have hidden.
- **H0:** The fine sweep reveals a discontinuity or a sharp kink in Φ_MIP at some interior p* — a
  threshold the coarse reliability sweeps (#27, #38) could have stepped over — so mean Φ itself marks
  a phase transition.
- **Predicted outcome:** Φ_MIP falls smoothly from 2.0 at p=0 toward 0 at p=0.5, reproducing and
  refining the coarse #27 curve (2.0→1.54→1.19→0.68→0.35→0.14→0). The fit residuals stay flat across
  the grid. H0 is refuted: mean Φ is smooth, matching the Mediano (2019) continuous-decay precedent.

## H2 — The phase transition, if any, lives in the susceptibility, not in mean Φ
- **Claim:** The first derivative dΦ/dp (the discrete susceptibility of Φ_MIP) is non-flat and peaks
  at an interior p — Φ_MIP is locally steepest at some 0 < p_χ < 0.5 — even while H1 holds and mean Φ
  stays smooth. The sharp feature is a response/susceptibility feature, recoverable only by
  differentiating the fine sweep, and invisible to a reading of Φ alone.
- **H0:** dΦ/dp is monotone or flat across the interval with no interior peak; the steepest descent
  of Φ sits at an endpoint (p→0 or p→0.5), so there is no susceptibility peak to mark a critical p.
- **Predicted outcome:** |dΦ/dp| rises to a maximum at an interior p_χ and falls on either side,
  matching the Niizato (2020) / Popiel (2020) result that χ_Φ peaks at criticality while mean Φ does
  not. The clean-limit steepness hinted by #38 (2.0→0.88 over r_c 1.0→0.9) shows up as a near-zero-p
  bias of the peak. H0 is refuted: the sharp signal is in the derivative.

## H3 — The dyadic/triadic verdict flips only at the degenerate endpoint, with no interior p*
- **Claim:** The verdict stays triadic (Φ_MIP > 0, integrated) for every p in [0, 0.5) and collapses
  to dyadic/zero only at the random-commit endpoint p = 0.5. No finite interior critical p* exists
  below which the triad survives and above which it factors. The verdict transition is the trivial
  collapse at the degenerate maximum, not an order-parameter crossing at a critical "temperature."
- **H0:** There is a finite interior p* in (0, 0.5) where the verdict flips dyadic — the triad factors
  at a sub-degenerate noise level, an interior phase transition in the irreducibility classification.
- **Predicted outcome:** Φ_MIP > 0 holds at every sampled interior p and the major complex stays the
  full triad until p=0.5, reproducing the "verdict robust to the endpoint" pattern of #27, #34, #38,
  #79. The verdict crosses only at the coin-flip commit. H0 is refuted: no interior verdict transition.

## H4 — The verdict transition can be sharp even where mean Φ is smooth (verdict/Φ decoupling)
- **Claim:** The verdict is a discontinuous object in p even though Φ_MIP(p) is continuous: at the
  collapse point the verdict snaps from triadic to dyadic as a step, not as a graded fade, so a sharp
  feature appears in the binary classification that is absent from the smooth Φ curve. The verdict and
  the magnitude carry different information about the transition.
- **H0:** The verdict tracks Φ continuously — it degrades through the same smooth ramp Φ does, with no
  step that mean Φ lacks — so verdict-sharpness and Φ-smoothness cannot coexist; either both are sharp
  or both are smooth.
- **Predicted outcome:** Φ_MIP fades smoothly to 0 (H1) while the triadic/dyadic label holds and then
  drops in one step at the collapse, a verdict-level discontinuity sitting on a continuous Φ, matching
  the Niizato (2020) fish-school result where Φ marks a sharp structural transition that smoother
  measures miss. H0 is refuted: the verdict is sharp where Φ is smooth.

## H5 — Φ_MIP is monotone in commit noise, against the not-robust-to-noise caution
- **Claim:** Φ_MIP(p) is strictly monotone decreasing across the whole sweep — every step up in p
  lowers Φ_MIP, with no interior local maximum, no rebound, and no non-monotone excursion. Commit
  noise on this conjunctive form only ever destroys integration; it never transiently raises it.
- **H0:** Φ_MIP is non-monotone in p — it rises before it falls, or shows an interior bump or a
  critical Φ maximum at some intermediate p — so adding commit noise can increase integration on this
  form before degrading it.
- **Predicted outcome:** Φ_MIP decreases at every grid step from 2.0 toward 0, with no interior peak,
  echoing the symmetric trough (not peak) #81 found on the tracking axis and contradicting the
  Danilczuk (2026) caution that internal stochasticity can raise Φ. The curve is monotone. H0 is
  refuted: no critical Φ maximum on the commit-noise axis.
</content>
</invoke>
