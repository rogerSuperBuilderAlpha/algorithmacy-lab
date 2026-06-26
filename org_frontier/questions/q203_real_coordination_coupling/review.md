# Q203 review

**Claim.** On a real two-party coordination, CRQA reads strong symmetric structure (%DET 59.8) while transfer
entropy, Granger causality, and convergent cross mapping agree in sign (P2→P1) but none reaches significance
against surrogates. Behavioral coupling does not deliver a confident directional verdict on this real dyad.

**Holds up.**
- The instruments are validated on controls in their own domains before the real data is read, and the
  controls pass. CCM's failure on the linear control and pass on the deterministic one is reported, not
  hidden, and bounds where CCM applies.
- Hypotheses were fixed before computing; both the supported (H2) and the not-supported (H1) verdict are
  reported plainly. The channel was chosen before the analysis, not after seeing the result.
- The number that carries the claim — none of the three surrogate p-values below .05 (0.078, 0.510, 0.235) —
  is robust to small estimator changes; the agreement-in-sign is exact.
- Output is deterministic (seeded) and the data is committed and refetchable.

**Limits, stated.**
- One dyad, one channel: a worked real-data example, not a population. The agreement-in-sign on a single dyad
  is suggestive, not established; a population study is the next step.
- No exact Φ: real series carry no ground-truth transition function. This study runs the behavioral-recovery
  side of the bridge only, which is honest about what observed data supports.
- The surrogate is circular-shift, which preserves autocorrelation but not all higher-order structure; a
  twin-surrogate or IAAFT test could be added.
- The estimators are standard but not exhaustively tuned; the verdict is about whether a default head-to-head
  recovers a confident direction, which is the question a practitioner faces.

**Verdict.** A sound first-real-data study within its single-dyad scope. The contribution is the head-to-head
on real data that the recurrence program's gap named, with the honest result that the directed measures agree
in sign but not in significance.
