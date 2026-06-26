# Q204 review

**Claim.** Exact Phi can be computed on a real coordination (eyemovement gaze). Under honest per-person
codings the gaze streams factorize (Phi ~ 0, CI includes 0); a coding that folds the joint state into both
units manufactures integration (Phi 0.53, CI excludes 0). The verdict is decided by the coding, not the data.

**Holds up.**
- The instrument is validated on a coupled control (Phi 0.79) before the real data is read; the analysis
  stops if the control fails.
- Hypotheses were fixed before computing; both are supported. The bootstrap CI carries the verdict (per-person
  CIs include 0; folded CI clears 0), and the values are robust.
- The honest reading of the low per-person Phi is stated: it is "not integrated at the one-step grain," not
  "uncoordinated" — Richardson & Dale's coupling is lagged, which a one-step Phi cannot see. The folded coding
  is flagged as a cautionary artifact, not evidence the gaze is integrated.
- Output is deterministic (seeded) and the data is committed and refetchable.

**Limits, stated.**
- One dyad, one-step TPM at the recording grain; a worked real-data example, not a population. A system built
  at the coupling lag would test whether the lagged coordination reads as integrated.
- The binarizations are a small principled set, not exhaustive; the point is that the verdict moves across
  them, which two honest codings agreeing on "reducible" and the folded coding flipping to "integrated"
  establishes.
- This is the structural half of the bridge on real data; no claim about a worker, a competency, or money is
  made.

**Verdict.** A sound first exact-Phi-on-real-data study within its single-dyad scope. The contribution is
exact Phi computed on a real coordination and the coder-dependence of the verdict shown outside synthetic
data, with a concrete cautionary coding.
