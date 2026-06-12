# Q9 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether a slow mediator over fast parties factors a triadic conjunctive
mediated form (worker W, mediator/system S, counterpart C) the way sequential update did in Probe 62.
The construction runs the parties on a fast clock and stretches S's effective clock by a timescale ratio
k. Two commit models are swept: a deterministic hold-for-k (S reads its own previous value for k−1 of
every k steps, committing the conjunctive update on the k-th), and a probabilistic 1/k commit (each step
S updates with probability 1/k and holds with probability 1−1/k, which lives in a probabilistic TPM the
state-by-node form may not express, the #61 flag). The grid sweeps k from 1 (the synchronous baseline) up
through the form's natural attractor period and beyond. At each k the sweep reads Φ_MIP, its derivative
dΦ/dk, the dyadic/triadic verdict, the MIP location, and major-complex membership, against the k=1
synchronous baseline that #112 fixed as the reporting grain. Written and committed before any test runs.
The review's prior probes (#62, #43, #57, #63, #32, #60, #112, #109, #27, #61, #3) and the deep-research
mechanisms (Hoel 2013/2016; Albantakis 2023a/2023b; Marshall 2026 update-grain τ_J; Mayner 2018;
Kuramoto 2019 adiabatic elimination; Comolatti 2025) supply the structural priors each null rests on.

## H1 — A slow mediator flips the verdict, it does not only grade Φ down
- **Claim:** Stretching S's clock collapses the triadic verdict to dyadic at a finite ratio k* on the
  deterministic hold-for-k construction, the way coarse grain (#32, #60) and sequential update (#62) both
  did, rather than sliding Φ_MIP smoothly toward zero with the verdict intact the way mediator
  unreliability (#27) and chain depth (#57) did. The hold-for-k composition lets the parties' fast
  determination pass while S sits frozen, so at some k the joint determination factors and the W–C pair
  reads dyadic.
- **H0:** The timescale ratio behaves like reliability and depth, not like grain and schedule: Φ_MIP falls
  monotonically with k but the verdict holds triadic at every finite k, crossing dyadic only in the
  degenerate k→∞ limit where S is a static constant and carries no information. A slower-but-still-coupled
  mediator stays in the loop (#57), so k grades the magnitude and leaves the binary verdict fixed.
- **Predicted outcome:** On the hold-for-k construction the dyadic/triadic verdict flips at a finite
  interior k* < ∞ at the synchronous-baseline corpus form, with Φ_MIP dropping to the dyadic reading there
  rather than approaching it only asymptotically. This realizes the clock-stretching mechanism the report
  names (Comolatti 2025: a faster description can be lossy about causation; Kuramoto 2019: fast parties
  slave to the slow mediator), carried onto the verdict. H0 is refuted: timescale separation is a fourth
  verdict-flipping timing axis, not a magnitude-only knob.

## H2 — Slowing S ejects S from the major complex, it does not eject the parties
- **Claim:** At the ratio where the verdict moves, the major complex sheds the mediator: membership goes
  from {W,S,C} to {W,C}, the question's own proposal, because a slow S contributes less irreducible
  cause–effect power per fast step than the W–C pair that updates every step. The element pushed out is S,
  not the parties.
- **H0:** Slowing S reproduces the sticky-mediator collapse (#43): a mediator that holds its value is a
  self-referential S, and #43 found inertia ejects the *parties* into a self-absorbed {S} core, the
  opposite direction. The held value makes S a memory device whose own state dominates, so the major
  complex contracts to {S} and W, C factor out.
- **Predicted outcome:** At k ≥ k* the major complex is {W,C} with S excluded, S's own φ_s below the φ_s of
  the W–C subsystem at the same grain, and S never forms a {S} core over the swept k. This is the
  update-grain membership shift Marshall (2026) makes formal — a complex is defined across grains by the
  exclusion postulate, so a slow unit can drop below an overlapping fast subsystem. H0 is refuted: the
  timescale hold ejects S, it does not eject the parties the way the OR-stick #43 did, distinguishing soft
  clock-inertia from hard rule-stickiness.

## H3 — Hold-for-k and probabilistic-1/k disagree on the verdict
- **Claim:** The two faithful-looking models of a slow commit part ways. The deterministic hold-for-k
  flips the verdict at a sharp k* (H1), while the probabilistic 1/k commit grades the verdict softly and
  flips at a different ratio, or not at all over the same grid, because the 1/k mixture keeps a fraction
  1/k of every step fully synchronous and re-injects the joint determination the hold-for-k removed. The
  modeling choice is load-bearing, not cosmetic.
- **H0:** The two constructions agree: at matched effective slowdown they cross the dyadic/triadic boundary
  at the same k within grid resolution and return the same major-complex membership, because both encode
  the same fast/slow ratio and IIT reads the ratio, not its stochastic dressing. Any difference is grid
  noise.
- **Predicted outcome:** The hold-for-k flip ratio k*_det and the probabilistic flip ratio k*_prob differ
  by more than one grid step, or the 1/k commit holds triadic across the whole grid while hold-for-k flips,
  with the 1/k commit also requiring the probabilistic-TPM construction the state-by-node form cannot
  express (#61). This answers the report's open question 3 — which is the faithful model of a slow commit,
  and whether conditional independence survives. H0 is refuted: the verdict depends on which slow-commit
  model is chosen, adding a construction axis beneath the timing axis.

## H4 — The verdict flip arrives at k tied to the form's attractor period
- **Claim:** The flip ratio k* is not arbitrary: it lands at or just past the corpus form's natural
  attractor period, the way the grain-collapse threshold #60 arrived at grain k near the period (periods
  1–2 there). A hold that is shorter than one full cycle of the synchronous dynamics leaves the triad
  intact; a hold that spans a full cycle freezes S across the coordination it would otherwise mediate and
  factors it. The period sets the threshold.
- **H0:** The flip ratio, if one exists at all (H1), does not track the attractor period. It sits at a
  fixed small k (e.g. k=2, where any composition of two fast steps lets information pass, the #32/#60
  grain-2 collapse point) independent of the form's period, or it is governed by the Φ-maximizing grain IIT
  selects on its own (Albantakis 2023b) rather than by the analyst-imposed ratio, so k* does not move with
  the period across forms of differing period.
- **Predicted outcome:** Across two or more conjunctive corpus forms with different synchronous attractor
  periods, k* moves with the period — the longer-period form flips at a larger k — rather than staying
  pinned at a period-independent constant. This sharpens #60's threshold-equals-period prior from grain
  onto the timescale ratio. H0 is refuted: the flip point is a period-locked quantity, predictable in
  advance from the synchronous dynamics, not a fixed grain-2 artifact.

## H5 — Clock-stretching is a different factorization from sequential update (#62)
- **Claim:** When the slow mediator does factor the triad, it does so by a *different* mechanism than
  Probe 62's sequential update, and the difference is visible in the MIP cut and the surviving structure.
  Sequential update factored by desynchronizing within a step, letting information pass through S in one
  step; clock-stretching factors by freezing S across steps. The two leave distinguishable fingerprints:
  the MIP partition that achieves the slow-mediator collapse, the residual Φ at the flip, or the set of k
  over which the collapse holds will not match what within-step reordering produces on the same form.
- **H0:** The two are the same factorization read through different parameters. Both compose several fast
  steps into one effective transition and route the parties' determination around a mediator that cannot
  respond inside the composed window, so they cut the triad at the identical MIP — the W↔C boundary that
  isolates S — and the slow-mediator collapse is just #62's collapse re-indexed by k. No fingerprint
  distinguishes them.
- **Predicted outcome:** The slow-mediator MIP at k* differs from the #62 sequential MIP on the matched
  corpus form — a different cut, a different residual Φ_MIP at the flip, or a collapse that holds over a k
  band rather than at every sequential order #62 found — establishing clock-stretching and within-step
  desynchronization as two distinct routes to the dyadic verdict. This answers the report's open question 2
  (same factorization or different). H0 is refuted: the two timing axes factor the triad by different
  internal partitions, even when they agree on the binary verdict, extending the #112 catalogue with a
  genuinely new mechanism rather than a re-parameterization of #62.
