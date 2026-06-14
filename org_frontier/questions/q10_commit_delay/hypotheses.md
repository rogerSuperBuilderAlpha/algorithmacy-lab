# Q10 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether a fixed commit→response transport delay flips the dyadic/triadic
verdict of a triadic conjunctive mediated form (worker W, mediator/system S, counterpart C) or only grades
Φ down. The construction inserts d pass-through buffer nodes carrying S's already-committed value forward d
steps before the parties respond (b' = b_prev, no self-OR, verified as transport and not inertia), for
d = 0, 1, 2, 3 against the d=0 synchronous baseline. A second implementation is swept in parallel: the
parties reading S at lag d without explicit buffer nodes, which may compile to a composed or strided map.
At each d the sweep reads Φ_MIP, its trend in d, the dyadic/triadic verdict, the MIP location, and the
major complex via `pyphi.compute.major_complex()`, both at the micro grain and after black-boxing the
buffers over d steps. The review's prior probes (#57, #62, #9/#155–159, #32, #60, #112, #43, #109, #27) and
the deep-research mechanisms (Marshall 2018 COPY-delay regrade-and-relocate; Hoel 2016 Φ-maximizing grain;
Oizumi 2014 / Tononi 2015 / Hanson 2019 feed-forward Φ=0; Albantakis 2023 fault-line sensitivity; Mayner
2018 major_complex) supply the structural priors each null rests on. Written and committed before any test
runs.

## H1 — Transport delay grades Φ down but does not flip the verdict
- **Claim:** Adding a pass-through buffer pipeline of length d leaves the dyadic/triadic verdict triadic at
  every d = 0, 1, 2, 3, lowering Φ_MIP at the synchronous grain without crossing the boundary. A delay line
  is added depth, and depth was verdict-neutral in the chain theorem (#57), so transport delay joins
  reliability (#27) and depth (#57) on the magnitude-soft, verdict-robust side rather than the
  verdict-flipping side of grain (#32, #60) and schedule (#62).
- **H0:** Transport delay flips the verdict like the other timing axes. Carrying the commit through d steps
  desynchronizes the loop the way coarse grain and sequential update do, so at some d the joint
  determination factors and the form reads dyadic, the same collapse #32, #62 and the Q9 hold (#9) all
  produced.
- **Predicted outcome:** The buffer-pipeline verdict stays triadic across d = 0..3 while Φ_MIP at the
  synchronous grain falls monotonically with d (or holds at the #57 chain value of 2.0), with no d at which
  the W–C pair reads dyadic. This confirms the report's directional prediction (Marshall 2018:
  regrade-and-relocate, not abolish) on the conjunctive triad. H0 is refuted: pure transport delay is
  verdict-stable depth, categorically unlike a slowed clock.

## H2 — The buffer nodes sit outside the major complex at the micro grain
- **Claim:** The pass-through buffers fall outside the W–S–C major complex at the micro grain. A buffer that
  passes a commit forward and takes no integrated feedback is feed-forward, and a feed-forward element
  carries Φ = 0 and is excluded from a complex (Oizumi 2014; Tononi 2015; Hanson 2019). The verdict object
  is recovered on the W–S–C core, with the buffer pipeline as an excluded appendix.
- **H0:** The buffers sit inside the major complex as chain intermediaries, the #57 reading. A delay line is
  a mediator chain, and #57 found the balanced MIP cuts *through* the intermediaries, placing them inside
  the complex rather than ejecting them.
- **Predicted outcome:** `major_complex()` at the micro grain returns a complex on {W,S,C} (plus at most the
  buffer adjacent to S as a weakly-integrated appendix), with the interior buffer nodes excluded and their
  individual φ measured rather than assumed zero (the refuted-claim flag, report open question 4). After
  black-boxing the buffers over d steps the complex may instead absorb them at a higher Φ (Marshall 2018).
  H0 is refuted at the micro grain: the buffers are excluded feed-forward, not included chain links, and the
  grain decides their membership.

## H3 — The buffer pipeline and the lagged read disagree
- **Claim:** The two implementations of the same delay part ways on the verdict. The explicit buffer
  pipeline behaves like depth and holds the verdict triadic (H1), while the lagged read — parties reading S
  at lag d with no buffer nodes — compiles to a composed or strided map and behaves like a grain change
  (#32, #60), flipping the verdict at some d. The implementation is load-bearing, not cosmetic.
- **H0:** The two implementations agree. Both encode the same d-step transport lag and IIT reads the lag,
  not its representation, so the buffer pipeline and the lagged read return the same verdict and the same
  major-complex membership at every d within grid resolution.
- **Predicted outcome:** At some d in 1..3 the lagged-read verdict is dyadic while the buffer-pipeline
  verdict at the same d is triadic, or the two return different major complexes, with the lagged-read map
  expressible as a composed/strided TPM that the buffer pipeline is not. This realizes the review's two
  hazards as a measured split. H0 is refuted: a transport delay's verdict depends on whether it is built as
  explicit depth or as a lagged read, so the two must be reported separately.

## H4 — No d=2 threshold under transport delay
- **Claim:** Transport delay carries no special d=2 status. The Q9 hold-for-k flipped deterministically at
  k=2 (#155) and the grain collapse landed at grain 2 (#32, #60), but those thresholds are properties of the
  hold and grain mechanisms, not of d-step latency. The buffer-pipeline Φ_MIP trend in d is smooth with no
  discontinuity at d=2, and any verdict change (if H1's null held) would not be pinned to d=2.
- **H0:** Transport delay reproduces the d=2 threshold, mirroring Q9's k=2 flip and the grain-2 collapse. A
  delay of 2 steps composes two transitions into the observed window the way grain-2 does, so d=2 is the
  point at which the determination passes and the verdict (or a sharp Φ drop) appears, coinciding with the
  sibling Q9 flip point.
- **Predicted outcome:** Φ_MIP versus d shows no kink, jump, or verdict change uniquely at d=2 on the
  buffer pipeline; the d=2 reading lies on the same smooth trend as d=1 and d=3, with any threshold (in the
  lagged-read implementation, H3) tied to the form's attractor period (#60) rather than fixed at 2. This
  answers the report's open question 2. H0 is refuted: the k=2 threshold is specific to the slowed-clock and
  grain mechanisms and does not transfer to transport latency.

## H5 — Transport delay and the slowed clock leave distinguishable fingerprints
- **Claim:** Transport delay (this probe) and the Q9 slowed clock (#9) are mechanistically distinct, and
  the difference is visible in the surviving structure, not only in whether the verdict flips. The slowed
  clock holds S's value and ejects the parties into a self-absorbed {S} core (#156); the transport delay
  carries a fresh commit through pass-through buffers and, where it touches the complex at all, ejects the
  buffers (H2) while keeping W–S–C intact. The MIP cut, the residual Φ, and the major-complex membership
  under transport delay will not match what the hold-for-k produced.
- **H0:** Transport delay and the slowed clock are the same factorization read through different parameters.
  A buffer carrying a delayed value is a memory cell, so a delay line is a stickiness construction (#43) and
  reproduces the hold's {S}-core collapse — same MIP, same surviving {S} core, the transport label a
  re-parameterization of the clock.
- **Predicted outcome:** Where transport delay touches the verdict it leaves a major complex on {W,S,C} or
  {W,C} with the buffers excluded, never the self-absorbed {S} core the hold-for-k produced (#156), and its
  MIP cut differs from the hold's; the pass-through buffers are verified to carry no self-OR, so no
  stickiness (#43) arises. This separates pure transport delay from the slowed update clock of Q9 and the
  within-step factorization of #62, extending the #112 catalogue with a fourth, verdict-stable timing axis.
  H0 is refuted: transport delay and slowed clock are two mechanisms with distinct fingerprints, not one
  mechanism under two names.
