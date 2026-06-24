# q159 — review

## What the probe does

It sweeps trajectory length over {150, 300, 600, 1200, 2400}, reads a CRQA triadic/dyadic verdict at
each length from a fixed spread threshold, and measures two things: agreement with the exact-Φ verdict,
and the length at which each form's verdict settles to its 2400-step reading. It bins forms by exact-Φ
tertile to test whether convergence length tracks Φ.

## Soundness checks

- **Instrument control passes.** The worker-system-counterpart triad reads triadic, max_phi 2.0,
  major-complex Φ 2.0, full 3-node core, and the length-parameterized spread feature is finite and
  nonnegative at every swept length.
- **Determinism confirmed.** Output is byte-identical across three runs. All ensemble draws and all
  trajectories are seeded with fixed seeds; exact Φ is deterministic.
- **No circularity in the length effect.** The decision threshold is fit once at the reference length,
  then frozen. The convergence measurement only asks whether the frozen reading moves with length.

## Weaknesses, stated

- The threshold is fit on the same labels it is later scored against, so the 0.81 agreement ceiling is
  optimistic for the fit length; it is reported as a within-corpus reading, not a held-out accuracy.
  The convergence claim does not depend on this, since it concerns stability of the verdict, not its
  correctness.
- H2 is underpowered by the corpus. Φ is nearly constant at 2.0 across most forms, so the tertile split
  straddles one value and cannot cleanly separate high-Φ from low-Φ forms. The refutation should be
  read as "no support, and a corpus too degenerate in Φ to test it," not as a strong null.
- A single spread cut is a coarse classifier (0.62 balanced accuracy). A richer behavioral verdict
  would move the agreement numbers, though likely not the fast-convergence finding.

## Scope

In-silico throughout. The bridge from a coded field organization to a transition matrix is not yet
validated against observed data, so the convergence lengths apply to these synthetic runs.
