# q181 — Methods

## Machinery

The study reuses the field bridge `org_frontier/field/rule_to_phi.py` (study 1 of the
field line). `rule_to_phi` encodes per-party Boolean determination rules into a TPM and
reads the exact IIT-4.0 Φ verdict over the MIP. `phi_ci` propagates coder disagreement
into a bootstrap-t Φ confidence interval. `major_complex` (from
`org_frontier/probes/lib.py`) reads the maximal complex and its Φ. Φ is not reimplemented.

## The 2x2 account

A single account is parameterised by two knobs, one per flipper. Pool size k sets the
substitutability flip: k = 1 is the specific irreplaceable worker, k >= 2 is the
substitutable pool (S = OR(D) & R, with each pool member reading off S). System mode sets
the pass-through flip: commit (S = OR(D) & R, the counterpart request gates the system) or
relay (S = OR(D), the counterpart is ignored). The grid over {specific, pooled} x {commit,
relay} gives four cells: the no-flipper baseline (k = 1, commit), each single flipper, and
the double flipper (k = 2, relay). H1 reads the verdict of every cell.

## Contested-case CIs

For H2, each coder independently decides whether to apply each flipper. A contested
flipper is applied by a randomly drawn subset of coders, with the split drawn from the
genuine-contest band [0.3, 0.7]; a non-contested flipper is off for everyone. A coder's Φ
reading is the verdict of the cell their two decisions select: 2.0 only when neither
flipper is applied, 0.0 otherwise. The panel of 24 coder readings runs through `phi_ci`
with its two-column coding matrix, giving a bootstrap-t CI and a Krippendorff alpha. The
substitutability panel contests only the pool flip; the pass-through panel contests only
the system flip; the joint panel contests both. The union CI is the envelope of the two
single-flipper CIs. The test compares the joint CI width to the union width: within 10%
supports composition, more than 25% over the union supports amplification.

## Determinism

Every random draw is seeded (`numpy.random.default_rng` with fixed seeds for the contest
splits and the bootstrap). The output is byte-identical across re-runs.

## Controls

The faithful triad (k = 1, commit) reads triadic at max Φ = 2.0 (the no-flipper baseline).
The double flipper must read dyadic. A spectator-only condition adds a node that reads the
system and feeds nothing back; the whole-system verdict drops because the spectator is
reducible, yet the major complex stays the triad (W, S, C) at Φ = 2.0. The spectator
isolates masking: a node that only observes does not collapse the irreducible core, so a
flip requires touching the cycle.

## Scope

All inputs are synthetic coded rule sets. The empirical arms report results on synthetic
data. Whether a coded account matches an observed coordination is not tested here.
