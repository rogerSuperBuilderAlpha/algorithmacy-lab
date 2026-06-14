# Q8 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether the parity (XOR-family) hub loses its dyadic/triadic Φ_MIP verdict
faster under noise than the conjunctive hub at matched size n. The sweep injects the same flip-noise model
Q6/Q7 used — a probabilistic-TPM commit that flips the hub's output with probability p, each clean
transition row mixed toward its flipped output with weight p, so the noise rides in the mechanism's TPM —
applied to the XOR-all hub and the AND-all hub at fixed n=3 and n=4. The grid runs p from the clean limit
p=0 to the random output p=0.5. At each step the sweep reads Φ_MIP, its first derivative dΦ/dp, the
dyadic/triadic verdict, and the MIP location, for both hub forms at both sizes. The clean baselines are
fixed: Φ = 2^(2−n) for the parity hub (0.5 at n=3, 0.25 at n=4; Probe 115) and Φ = n−1 for the conjunctive
hub (2.0 at n=3, 3.0 at n=4; Probe 116). Written and committed before any test runs. The review's prior
probes (#115, #116, #120, #140–144, #145–149, #56, #114, #61) and the deep-research mechanisms
(Albantakis 2023b; Garban–Steif / BKS 1999 / O'Donnell 2014; Mediano–Rosas 2019; Popiel 2020;
Orio–Mediano–Rosas 2023) supply the structural priors each null rests on.

## H1 — The parity verdict flips at an interior p; the conjunctive verdict holds to the endpoint
- **Claim:** At fixed n, rising flip-noise collapses the parity hub's triadic verdict (Φ_MIP > 0 →
  dyadic) at a finite interior p_par* strictly inside (0, 0.5), while the conjunctive hub's verdict
  survives until the degenerate p=0.5 coin-flip endpoint, exactly as Q6 found for the conjunctive mediator
  (#140–144). The parity hub flips early; the conjunctive hub flips only at the maximum.
- **H0:** Both forms flip the verdict only at p=0.5. The flip point is a property of the degenerate
  endpoint — a unit XORed with a fair coin carries zero information regardless of the commit function — so
  the parity verdict, like every prior stochastic sweep on the conjunctive form (#140–149, #27, #34), rides
  smoothly to zero and crosses dyadic only at the coin-flip maximum. The small clean Φ is a magnitude fact
  the binary verdict does not inherit (#114).
- **Predicted outcome:** The conjunctive Φ_MIP stays positive at every interior p and crosses dyadic only
  at 0.5; the parity Φ_MIP crosses dyadic at some p_par* < 0.5 at both n=3 and n=4. This realizes the
  pure-higher-order fragility mechanism (#56): the parity hub's irreducibility lives only in the whole with
  no lower-order seed beneath it, so noise that thins the top-level structure has nothing to fall back on,
  the Garban–Steif maximal-noise-sensitivity ordering carried into the verdict. H0 is refuted: the parity
  verdict breaks first.

## H2 — Parity Φ decays faster than conjunctive Φ in flip fraction, not just in absolute magnitude
- **Claim:** Rescale each form's curve to its own clean value — Φ_MIP(p) / Φ_MIP(0) — to remove the
  starting-magnitude difference (0.5/0.25 vs 2.0/3.0). The normalized parity curve still falls faster than
  the normalized conjunctive curve: at matched n the parity hub has lost a larger *fraction* of its clean
  Φ at every interior p, and |d log Φ / dp| near p=0 is larger for parity than for conjunctive. The
  fragility is in the decay rate of the form, not merely in where it starts.
- **H0:** Once normalized to clean Φ, the two forms decay at the same fractional rate — the parity hub only
  *looks* more fragile because its clean Φ is smaller, and both forms shed the same proportion of their
  integration per unit flip probability. The intrinsic-information ceiling (Albantakis 2023b) lowers φ for
  both commits through the same determinism-loss channel, so the normalized curves coincide.
- **Predicted outcome:** The normalized parity curve sits below the normalized conjunctive curve across the
  interior grid and its clean-limit log-slope is steeper, at both n=3 and n=4. This is the IIT analogue of
  the Boolean-function decay law — parity's signal decays as (1−2p)^n versus the conjunctive hub's gentler
  mixed-order decay (O'Donnell 2014; Garban–Steif), read on Φ_MIP rather than on Fourier correlation. H0 is
  refuted: parity decays faster in fraction, so fragility is a rate property, not only a starting-point one.

## H3 — The verdict-flip gap widens with n
- **Claim:** The size axis amplifies the fragility gap. The distance between the parity flip point and the
  conjunctive flip point, measured at matched n, is larger at n=4 than at n=3: parity's p_par* moves to a
  *lower* p as n grows (the verdict gets more fragile with size), while the conjunctive flip point stays
  pinned at or near 0.5. The clean-Φ gap (2^(2−n) shrinking against n−1 growing; #115/#116/#120) projects
  onto a widening noise-threshold gap.
- **H0:** The flip-gap does not widen with n over n=3→4 — either both forms flip at 0.5 at both sizes (the
  H1 null, no gap to widen), or the parity flip point is n-independent because the fixed-n
  Stab_ρ(χ_S)=ρ^|S| ordering already separates the forms and the single n=3→4 step is too short to move the
  threshold beyond grid resolution. The asymptotic noise-sensitivity result is an n→∞ property
  (Garban–Steif caveat (a)), not a claim about two small sizes.
- **Predicted outcome:** p_par*(n=4) < p_par*(n=3), the conjunctive flip stays at ~0.5 at both sizes, and
  the gap (p_conj* − p_par*) is strictly larger at n=4. This is the dynamical analogue of the size-axis
  collapse Probe #120 found at n≈22 in clean arithmetic, brought down to small n by noise. H0 is refuted:
  the gap is size-dependent and grows.

## H4 — The parity collapse threshold tracks the Boolean-function prediction (1−2p)^n
- **Claim:** The parity hub's flip point is *quantitatively* predicted, not merely ordered, by the
  Fourier-decay law. p_par* falls where the retained top-level signal (1−2p)^n drops below the MIP
  resolution that separates triadic from dyadic — i.e. p_par* solves (1−2p_par*)^n ≈ (Φ floor) / 2^(2−n),
  so the measured collapse p sits within grid tolerance of the value this closed form gives at each n. The
  cross-framework analogy predicts the number, not only the direction.
- **H0:** The partition-minimization structure of Φ_MIP shifts the collapse off the Boolean-function
  prediction — the measured p_par* does not match (1−2p)^n within tolerance, because Φ_MIP is a non-linear
  minimization over partitions of an earth-mover / intrinsic-difference distance, not a linear Fourier
  correlation, and the two functionals need not share a threshold (report caveat 7, open question 2). The
  analogy gives the direction (H1/H2) but the wrong p.
- **Predicted outcome:** The measured parity flip p at n=3 and n=4 lands within grid spacing of the
  (1−2p)^n closed-form prediction. This would promote the Boolean-function mechanism from a directional
  analogy to a quantitative predictor of the IIT verdict-collapse threshold, the strongest possible form of
  the report's central inference. H0 is refuted only if the numbers match; a directional-but-not-numerical
  result leaves H1/H2 standing while refuting H4 specifically — the deliberately sharper, more falsifiable
  claim.

## H5 — Parity collapses as a cliff, conjunctive as a glide (qualitative shape of the decay)
- **Claim:** The two forms differ not only in where Φ crosses zero but in the *shape* of the approach. The
  parity Φ_MIP(p) has a sharp knee — a region of rapid drop where the lone top-level structure gives way at
  once, with a large peak in |dΦ/dp| at an interior p — because there is no lower-order seed to cushion the
  fall (#56). The conjunctive Φ_MIP(p) glides: monotone, with |dΦ/dp| maximal at p=0 and no interior peak,
  exactly the smooth decay Q6 measured (#140–144). The collapse is a phase-transition-like knee for parity,
  a featureless slide for conjunctive.
- **H0:** Both curves are smooth and monotone with |dΦ/dp| maximal at p=0 and no interior susceptibility
  peak — the parity curve is just a scaled-down version of the conjunctive glide, the standing
  smooth-decay pattern (#140–144, #27, #34, #14, #38) holding for both forms. No knee, no
  phase-transition signature distinguishes the parity collapse.
- **Predicted outcome:** The parity dΦ/dp shows an interior extremum (a susceptibility-like peak) that the
  conjunctive dΦ/dp lacks, marking the parity collapse as the order-parameter phase transition Popiel
  (2020) reports for Φ at criticality, while the conjunctive curve stays monotone-decreasing from p=0. A
  weaker corroborant the sweep must also check: a non-monotone excursion in either curve, the
  Orio–Mediano–Rosas (2023) caution that intermediate noise can transiently raise high-order structure, so
  monotonicity is not assumed for either form before measurement. H0 is refuted: parity collapses with a
  knee the conjunctive form does not have.
