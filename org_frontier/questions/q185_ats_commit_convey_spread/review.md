# q185 — review

## Claim

On one strict-mediator wiring diagram, the disagreement-Φ spread separates a commit account
(triadic, Φ = 2.0) from a convey account (dyadic, Φ = 0.0) with identical connectivity matrices,
and the separation tracks the manager-update rule rather than the topology.

## Checks

- Instrument control: the faithful triad reads triadic with max Φ_MIP = 2.0 before any result is
  read. The control passes on every run.
- Identical topology: `cm_from_rules` returns the same connectivity matrix for the commit and
  convey accounts and across both H2 settings. The probe asserts this and prints it.
- Determinism: a fixed-seed generator is set at load; the spread is exact over reachable states.
  Output is byte-identical across three runs.
- Reuse: Φ comes from the q183 bridge and the shared classifier. Nothing about Φ is reimplemented.

## Soft spots

- The convey account encodes "rules alone" as M = 1 - S. The negation is one defensible coding of
  a manager who overwrites the commit with an independent decision. A different coding (for
  instance M constant) would also break the dependence; the verdict that the manager-update rule
  is load-bearing does not hinge on the specific negation, but the exact phi_gap could differ.
- core_jaccard is 0.667 rather than 0 when the accounts disagree, because the dyadic account still
  retains a two-party core overlapping the triadic core. The spread reports partial core overlap,
  not disjoint cores, and the finding states the measured value.
- The whole study is synthetic. Two coded rule sets stand in for two stated accounts. No worker,
  manager, or system state is measured, so external validity is not claimed.

## Verdict

H1 SUPPORTED and H2 CONFIRMED on synthetic data. The result is reproducible and the controls hold.
