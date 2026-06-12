# Q7 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether the locus of stochastic output-flip noise changes the Φ collapse, for
the triadic conjunctive mediated form S' = W∧C. The matched sweep injects the same flip-noise model Q6
used — each clean transition row mixed toward the flipped output with weight p, so the noise rides in the
mechanism's TPM rather than the initial state — but moves the flip off the mediator's commit (S) and onto
the parties' updates (W and C). The sweep runs p on a fine grid from the clean limit p=0 to the random
output p=0.5, reads Φ_MIP, its first derivative dΦ/dp, the dyadic/triadic verdict, and the MIP location at
each step, for three injection sites: S alone (the Q6 baseline), W alone, and W and C together. Written and
committed before any test runs. The review's prior probes (#140–144, #27, #38, #34, #81, #16, #26/#33, #55,
#61) and the deep-research precedents (Danilczuk 2026; Marshall 2023; Harush 2019; Russo 2016; Mediano 2021;
Mayner 2018; Schwitzgebel 2018) supply the structural priors each null rests on.

## H1 — Party noise and mediator noise trace different Φ(p) curves
- **Claim:** Injecting the matched flip-noise into the parties (W, or W and C) yields a Φ_MIP(p) curve
  that differs measurably from the mediator-noise curve (#140–144) at the same p — the two sites do not
  collapse the triad along the same decay. Sampled on the same fine grid, the party and mediator curves
  separate beyond grid noise at one or more interior p, so the locus of the flip changes its effect on Φ.
- **H0:** The party and mediator curves coincide pointwise (within numerical tolerance) across (0, 0.5).
  The conjunctive commit reads W, C, and the S-feedback through structurally even roles, so equal output
  noise at any input site loads on Φ_MIP identically — one curve, not two, per the balanced-influence
  result (#16) and the W↔C verdict automorphism (#55).
- **Predicted outcome:** The party curve sits off the mediator curve at interior p, the two are
  distinguishable on the fine grid, and the gap exceeds the per-point numerical spread. This realizes the
  locus-dependent asymmetry Danilczuk (2026) found between internal and external noise placements and the
  MIP-fault-line mechanism of Marshall (2023). H0 is refuted: party noise and mediator noise are two curves.

## H2 — W-noise and C-noise give the same curve as each other
- **Claim:** Within the party site, injecting the flip-noise into W alone and into C alone produces
  identical Φ_MIP(p) curves, identical dΦ/dp, and identical verdict-flip points at every grid step, so
  "party noise" can be reported as a single curve. The worker and the counterpart are interchangeable
  noise sites even when the mediator is not.
- **H0:** W-noise and C-noise curves differ — the worker and counterpart load on Φ_MIP unequally, so the
  party site is itself two curves and cannot be collapsed to one. The MIP cut at {W,SC} (#26, #33) places
  W on the separable seam and C inside the tight {S,C} block, which would make C-noise act more like
  mediator noise than W-noise does.
- **Predicted outcome:** The W-only and C-only sweeps overlay exactly (0/N flips, zero Φ difference at
  every p), confirming the W↔C swap is an exact automorphism of the noise response, not only of the clean
  verdict (#55). H0 is refuted: the party site is one curve, justifying a single party-vs-mediator contrast.

## H3 — The party verdict flips at an interior p below the degenerate endpoint
- **Claim:** Party noise collapses the triadic/dyadic verdict at a finite interior p* in (0, 0.5), strictly
  below the p=0.5 coin-flip endpoint where mediator noise flips it (#140–144). The triad factors at a
  sub-degenerate party-noise level — there is a noise budget the parties can carry that is smaller than the
  one the mediator can carry, and the gap between the two flip points is the order-parameter signature of
  the asymmetry.
- **H0:** The party verdict flips only at p=0.5, exactly as the mediator verdict does. Both sites are
  trivial collapses at the degenerate maximum, where a unit XORed with a fair coin carries zero information
  regardless of which unit it is (Mayner 2018), so neither site flips the verdict at any interior p.
- **Predicted outcome:** Φ_MIP > 0 holds for the mediator at every interior p and crosses only at 0.5,
  while the party sweep crosses dyadic at some p* < 0.5, a verdict-flip gap between the two sites. This
  matches the Φ non-robustness warning (Schwitzgebel 2018) that perturbation site can flip the verdict
  sharply rather than only at the degenerate limit. H0 is refuted: the party verdict flips early.

## H4 — Party noise decays Φ faster than mediator noise (asymmetry direction)
- **Claim:** Near the clean limit the party-noise curve is steeper than the mediator-noise curve —
  |dΦ/dp| at small p is larger for the party site than for the mediator site — so party noise destroys
  integration faster per unit of flip probability. The asymmetry has a definite sign: the worker sits on
  the weak seam of the {W,SC} cut, the noise there straddles the fault line the MIP already reads, and a
  flip on the separable side moves Φ_MIP more than a flip buried inside the tightly-bound {S,C} block.
- **H0:** Either the curves coincide (no asymmetry, the H1 null) or the asymmetry runs the other way —
  mediator noise is steeper than party noise, because the mediator sits at the recurrent junction whose
  commit every party reads, so degrading it should cost more integration than degrading a single peripheral
  input (the Harush 2019 core-versus-periphery reading).
- **Predicted outcome:** The clean-limit slope is steeper for the party site, the party curve drops below
  the mediator curve immediately off p=0, and the ordering holds across the interior grid. This fixes the
  sign the review's two structural predictions left open. H0 is refuted: party noise is the steeper site.

## H5 — Two simultaneously-noised parties interact, moving the joint collapse off p=0.5
- **Claim:** Injecting independent flip-noise into W and C together is not the same as twice one party's
  noise — the conjunctive commit S' = W∧C makes the two noised inputs interact, so the joint-party
  Φ_MIP(p) curve is not the simple sum or scaling of the single-party curves, and its effective collapse
  point moves off the degenerate p=0.5. Conjunction couples the two party flips, so the joint endpoint
  shifts below 0.5.
- **H0:** The joint-party curve is separable into the single-party contributions and its collapse still
  sits at p=0.5 — two independent party flips noise the commit no differently in kind than one, and the
  conjunction does not move the endpoint. Equivalently, the open question carried by the report (whether
  conjunction moves the effective flip point off 0.5) resolves negative.
- **Predicted outcome:** The W-and-C-together sweep departs from the single-party sweep beyond additive
  scaling, and its Φ_MIP reaches the dyadic/zero collapse at an effective p strictly below 0.5, the
  conjunction-induced shift the report flagged as open. A weaker corroborant: a non-monotone excursion in
  the joint curve, the Danilczuk (2026) caution that internal stochasticity can transiently raise Φ. H0 is
  refuted: conjunction couples the two party noises and moves the joint endpoint.
