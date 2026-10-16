# Q221 — Retrospective research review

> **Scope note (2026-10-15):** This retrospective Stage-1 review describes the earlier exploratory three-node work. A separate, later four-node target-A study and C2/C4 follow-up were prospectively registered and completed; see `confirmatory_4node/RESULTS.md`. Neither confirms an IIT bottleneck claim. Historical exploratory-only statements below apply to the original stage, not the entire current Q221 PR.


**Exploratory feasibility record. This is not a prospectively completed literature-first review.**

## Question

Can stationary categorical pairwise recurrence summaries uniquely identify the lab's IIT-4.0 leave-one-out bottleneck target in synthetic three-node Boolean networks? Separately, are recurrence-coupling nulls valid under temporal dependence?

## Repository context

q161 defines the deterministic-rule exact-Φ target and leave-one-out bottleneck. q220 examines timestamp-aware recurrence estimators, observation noise and bottleneck predictions. Q221 does not modify or retroactively adjudicate their historical results.

## Prior work

Surrogate-data testing, dependence-preserving inference, recurrence-analysis pitfalls, and higher-order structural information are established topics. The draft literature register records source-verification levels. The novelty of the precise IIT bottleneck counterexample has not been established by exhaustive prior-art search.

## Observed gap

The exploratory bounded search found three symmetry-distinct classes of non-isomorphic systems with equal tested stationary marginal and pairwise auto/cross recurrence profiles but different q161 bottleneck sets. Transition-aware classifiers distinguish the systems on held-out trajectories. The supported result is therefore **restricted representation insufficiency**, not full observational non-identifiability.

## Decision

Retain as an exploratory methods contribution. No prospective hypothesis or universal IIT theorem is claimed. A future confirmatory study requires a new preregistration, independent-form sampling and justified null procedures.

## Addendum (2026-10-15, executor)

Following `TARGET_AUDIT.md`:
- The q161 target difference vanishes under an IIT background-condition reading. The paper's structural claim
  must name the q161 freeze convention.
- The defensible results are:
  - pairwise statistical non-identifiability, proved for the invertible affine class (`THEORY.md`);
  - the exact process-law decision;
  - the measured q220 null FPRs.

See `GATES.md` and `FINDINGS.md`.

### Addendum 2 (2026-10-15, executor)

- **Headline:** target A, statistical non-identifiability from pairwise recurrence summaries. It is proved for
  the invertible affine class, and the paper now leads with it.
- **Target B** is convention-dependent; see `OPEN_QUESTION_FOR_MAINTAINER.md`.
- **Target C** is negative.
- **Target D** is at chance.
- **Comparators:**
  - Transfer entropy, joint recurrence and SHREC separate the survivors.
  - The MdRQA full-vector recurrence rate does not (it is exactly equal).
  - False-pair-calibrated q220 is near chance.
- **Decision:** unchanged. Exploratory methods contribution; keep the PR as a draft.
