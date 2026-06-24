# q185 — Commit and convey on one wiring diagram: a disagreement-Φ spread in algorithmic hiring

A resume signal feeds an applicant tracking system, and the system feeds a hiring manager. Two
parties describe this coordination and disagree about what the system does. The candidate's
account treats the system as committing a screening rule the manager must heed. The manager's
account treats the system as a store the manager rules on alone. Both descriptions trace the same
arrows: the resume reaches the manager only through the system, and the system reads both the
resume signal and the manager profile.

The disagreement-Φ bridge from q183 scores how far apart two accounts of one coordination sit. It
runs each account through the exact IIT-4.0 classifier and returns a spread tuple: whether the
two accounts agree on structure, the gap in whole-system Φ, and the overlap of the two integrated
cores. This study applies the bridge to the commit-versus-convey split.

## The two accounts

The candidate's commit account is the validated strict-bottleneck triad [x1, x0 & x2, x1]. The
system commits when the resume signal and the manager profile both fire, and the manager heeds
the commit. This reads triadic, with whole-system max Φ_MIP of 2.0 and a full resume-system-
manager core.

The manager's convey account keeps the identical wiring but changes one rule: the manager rules
alone on the stored signal rather than heeding its content, [x1, x0 & x2, 1 - x1]. The
system-to-manager edge survives, so the connectivity matrix is unchanged. The manager now
computes the negation of the commit. This reads dyadic, with max Φ_MIP of 0.0.

## What the spread shows

The two accounts share the connectivity matrix exactly, yet the spread reads a phi_gap of 2.0 and
disagreement on structure (triadic against dyadic). Identical topology does not force identical Φ.
The commit-convey distinction lives in the rules, and the bridge reads it. This answers H1: the
spread separates commit from convey on one topology.

The H2 control holds the wiring fixed and moves only the manager-update rule. When the manager
heeds the commit, the two accounts agree, the gap is zero, and the cores coincide. When the
manager rules alone, the accounts disagree, the gap opens to 2.0, and the core overlap falls to
0.667. The connectivity matrix is identical across both settings, so the move is the
manager-update rule and not the wiring. The spread tracks the load-bearing rule. This confirms H2.

The load-bearing rule is the manager's. Whether the manager keeps live to the system's commit or
overwrites it with an independent decision decides whether the coordination is irreducibly
three-party. The bridge turns the candidate-manager disagreement into a measured construct on the
two accounts.

## Scope

The accounts are coder-supplied rule sets, not measured worker states. The result is a property of
the two coded systems on synthetic data. It does not measure a real hiring coordination, and no
candidate, manager, or system state is observed. The validation gap between this construct and a
measured account remains open. The contribution is the principled reading the bridge enables on
the two stated accounts.
