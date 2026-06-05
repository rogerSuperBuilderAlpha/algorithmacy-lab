# Q43 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on whether the IIT-4.0 dyadic/triadic verdict maps onto Thompson's (1967)
three interdependence types — pooled, sequential, reciprocal — when each type is built as a small
Boolean dynamical system, matched on node count and determination family, and read on its exact-Φ
verdict and major complex. Written and committed before any test runs. The review's prior probes
(#57, #58, #132, #40, #44/#52/#65/#105/#116, #25, #5/#39, #16/#26/#33) supply the structural priors
each null rests on.

## H1 — The naive Thompson ordering fails
- **Claim:** Under a single modeling convention applied uniformly to all three types at fixed n, the
  exact-Φ verdict does not reproduce Thompson's pooled < sequential < reciprocal ordering of
  coordination demand. At least one of the two ordering steps inverts or collapses: the most natural
  pooled model is not the lowest-Φ and the sequential model is not strictly between pooled and
  reciprocal.
- **H0:** The verdicts come out monotone in Thompson's order — pooled lowest Φ (and dyadic),
  sequential intermediate, reciprocal highest Φ (and triadic) — so the typology maps cleanly onto the
  IIT reading.
- **Predicted outcome:** Built as a matched triple at n=3, the pass-through chain reads triadic at
  Φ=2.0 (#57) and the all-required pool reads triadic at Φ≈n−1 (#116), so the chain is not strictly
  below reciprocal and the pool is not the dyadic floor. The naive ordering breaks; H0 is refuted.

## H2 — "Pooled" is verdict-ambiguous, and the split turns on joint determination
- **Claim:** Thompson's "pooled" has two defensible Boolean readings that land on opposite verdicts.
  Independent contributions sharing a common resource, with no joint determination over the shared
  node, factor into separate dyads (dyadic). An all-required joint output over the same parts is
  irreducible (triadic). The deciding structural feature is whether a single downstream node is
  jointly determined by all contributors, not the "pooled" label.
- **H0:** "Pooled" has one verdict regardless of how the shared resource is wired; the two Boolean
  encodings give the same verdict because they encode the same interdependence type.
- **Predicted outcome:** The independent-contribution pool (relay/broadcast with per-party channels,
  #25/#40) reads dyadic with major complex {W,resource}; the all-required pool (W∧C1∧C2…, #116) reads
  triadic with Φ rising as n−1 and group surplus at n≥4. Same node count, opposite verdicts. H0 is
  refuted and the joint-determination feature is identified as the switch.

## H3 — "Sequential" is verdict-ambiguous, and the split turns on the return path
- **Claim:** Thompson's "sequential" also has two readings on opposite verdicts. A pass-through
  mediator chain W→S→C, where the worker's effect propagates through and is read at the far end, is
  triadic. A one-way acyclic hand-off where each stage only sources the next and nothing returns
  reduces to a source→sink determination that factors (dyadic). The deciding feature is whether the
  chain forms an information-carrying path that is severed by every internal cut, versus a
  decomposable acyclic hand-off.
- **H0:** "Sequential" has one verdict; the chain's verdict is invariant to whether it is read as a
  propagating path or an acyclic hand-off, since both are "the chain."
- **Predicted outcome:** The propagating chain reads triadic at Φ=2.0 with a balanced near-middle MIP
  (#57); a pure acyclic source→sink hand-off reads dyadic (#39). The two sequential encodings split.
  H0 is refuted.

## H4 — Reciprocal interdependence requires a feedback cycle, not just bidirectional labels
- **Claim:** The reciprocal type reads triadic only when the coupling forms an actual feedback cycle
  through both parties (mutual/return flow), not merely when each party is nominally labeled as
  influencing the other. A reciprocal model whose "return" arrow does not close a determination cycle
  reads dyadic despite the bidirectional gloss.
- **H0:** Any model labeled reciprocal — any model with arrows drawn in both directions — reads
  triadic, because two-way arrows are sufficient for irreducibility.
- **Predicted outcome:** The cyclic reciprocal triad (bidirectional coupling closing a feedback loop,
  #5/#39) reads triadic at Φ>0 with the worker the weakest MIP seam {W,SC} (#16/#26/#33); a
  bidirectionally-labeled but acyclic variant reads dyadic. Irreducibility tracks the cycle, not the
  arrow count. H0 is refuted.

## H5 — Under a faithful convention only reciprocal is type-robustly triadic; pooled/sequential verdicts are encoding artifacts
- **Claim:** Across the full matched triple at fixed n and fixed determination family, the verdict is
  not a function of Thompson's type for pooled and sequential — each of those two types can be wired
  to either verdict by a defensible encoding choice (H2, H3) — whereas reciprocal is robustly triadic
  across its defensible encodings provided the feedback cycle is preserved (H4). So the IIT verdict
  tracks two structural primitives, joint determination and feedback cycle, and only reciprocal
  pins a primitive that forces triadicity.
- **H0:** The verdict is a clean function of Thompson's three-way type assignment: each type maps to a
  single verdict that is stable across its reasonable Boolean encodings, so the typology is the right
  carving for the IIT reading.
- **Predicted outcome:** Pooled spans dyadic↔triadic (H2) and sequential spans dyadic↔triadic (H3)
  depending on encoding, while reciprocal stays triadic whenever the cycle is intact (H4). The
  verdict is predicted by {joint determination present?, feedback cycle present?} and not by the
  Thompson label, so Thompson's typology is the wrong carving and a two-primitive structural account
  replaces it. H0 is refuted.
