# Q144 review — adversarial reading

## Claims and how they were tested

The probe computes exact IIT-4.0 major-complex Φ on a (depth, breadth) grid of balanced mediator trees and
on two scaling-zoo baselines. The instrument is validated on the faithful triad (reads triadic, Φ = 2.0)
before any tree is computed; the run aborts otherwise. All forms are deterministic Boolean rules and the
reachable-state scan is exhaustive, so the numbers are exact, not sampled.

## Strengths

- Depth and breadth are isolated cleanly. The depth axis fixes one leaf (b = 1) so n grows only by added
  layers; the breadth axis fixes one layer (d = 1) so n grows only by added leaves. Neither axis confounds
  the other.
- The depth result is unambiguous: Φ = 2.000 at d = 1, 2, 3, 4, byte-for-byte the chain baseline. The
  serial-bottleneck reading is well supported.
- Determinism is verified by re-running; the output is byte-identical across runs.

## Weaknesses and threats

- **H2 super-linearity refuted.** The breadth trend is 2, 3, 4 — linear, not the n(n-1) convex growth the
  hypothesis predicted. The pre-registered strong claim fails. Reported honestly as supported-but-linear,
  with the separability claim (breadth scales unlike depth) the part that survives.
- **Pool baseline imperfect.** The parity-coupling pool gives non-monotone Φ (1.5, 4.0, 2.5) and does not
  reproduce the published n(n-1) law at this size, so "toward the pool" is qualitative. A construction that
  reproduces the pool law cleanly at n <= 5 would sharpen the contrast.
- **Three breadth points.** b = 2, 3, 4 at n <= 5 is a short lever arm. Linearity is the reading over that
  range and could break at larger breadth, which the exact instrument cannot reach here.
- **One closure.** Leaves read the apex. The reachable-state set and magnitudes depend on that choice; the
  depth-flat, breadth-growing split is shown for this closure only.

## Verdict on the verdicts

H1 SUPPORTED is solid: exact, flat, matches the chain baseline. H2 is a split result and is reported as
such — separability holds, super-linearity does not. No number is over-claimed.

## In-silico scope

Boolean models, exact Φ, synthetic trees. No party is measured. The finding is about how Φ scales in these
constructions, not a fact about any fielded organization. The validation gap stands.
