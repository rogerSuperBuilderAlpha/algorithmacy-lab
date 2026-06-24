# q185 — findings

The disagreement-Φ spread separates the candidate's commit account from the manager's convey
account while both accounts carry the identical wiring diagram. The separation is driven by the
manager-update rule, not by the topology.

## H1: commit vs convey on one topology

| account | structure | max Φ_MIP |
|---------|-----------|-----------|
| commit  | triadic   | 2.000000  |
| convey  | dyadic    | 0.000000  |

Connectivity matrices identical: True. Spread: verdict_agreement = 0, phi_gap = 2.000000,
core_jaccard = 0.666667, both_verdicts = ('triadic', 'dyadic').

The two accounts share the wiring (R reads S, S reads R AND M, M reads S) yet read different
structures, so phi_gap = 2.0 > 0 with identical connectivity. H1 SUPPORTED.

## H2 control: vary only the manager-update rule

| manager rule          | cm identical | verdict_agreement | phi_gap  | core_jaccard |
|-----------------------|--------------|-------------------|----------|--------------|
| heeds commit (M = S)  | True         | 1                 | 0.000000 | 1.0000       |
| rules alone (M = 1-S) | True         | 0                 | 2.000000 | 0.6667       |

The connectivity matrix is identical in both rows. Breaking the ATS->manager dependence (manager
rules alone) opens the spread; restoring it (manager heeds the commit) collapses it to agreement
and zero gap. The spread tracks the load-bearing rule. H2 CONFIRMED.

## Verdicts

- H1 commit/convey spread on identical topology: SUPPORTED
- H2 spread tracks the manager-update rule, not the wiring: CONFIRMED

## Scope

Synthetic accounts. The result is a measured property of the two coded rule sets, not a
measurement of a real hiring coordination. No worker state is observed.
