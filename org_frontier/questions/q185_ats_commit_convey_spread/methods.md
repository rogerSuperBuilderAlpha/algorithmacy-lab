# q185 — methods

## Forms

Three labelled parties: resume signal R, applicant tracking system S, hiring manager M
(little-endian current-state tuple x = (R, S, M)). The wiring is strict mediation: R reads S,
S reads R AND M, M reads S. There is no direct R<->M back-channel in either account.

The candidate's commit account is the validated `ats_strict_bottleneck` triad:

    COMMIT = [x1, x0 & x2, x1]

S commits iff the resume signal and the manager profile both fire, and the manager heeds the
commit (M = S). This reads triadic with whole-system max Φ_MIP = 2.0.

The manager's convey account keeps the identical wiring, but the manager rules alone on the
stored signal, so the manager update no longer carries the commit's content:

    CONVEY = [x1, x0 & x2, 1 - x1]

M still reads S (the S->M edge survives, so the connectivity matrix is unchanged), but M now
computes the negation of the commit instead of heeding it. This reads dyadic with max Φ_MIP = 0.0.

## Bridge

The disagreement-Φ bridge from q183 (`org_frontier.qualitative.disagreement_phi.spread`) takes
the two accounts as rule sets over the shared labels and returns the spread tuple:
verdict_agreement, phi_gap, core_jaccard, both_verdicts. Each account is run through the exact
IIT-4.0 classifier; nothing about Φ is reimplemented here.

## H1 test

Compute the spread between COMMIT and CONVEY and check the two connectivity matrices for
equality (`cm_from_rules`). H1 holds when the matrices are identical, phi_gap > 0, and the two
accounts disagree on structure.

## H2 control

Hold the topology fixed (S = R AND M, R = S) and vary only the manager-update rule, the
ATS->manager coupling. Two settings: the manager heeds the commit (M = S, dependence intact) and
the manager rules alone (M = 1 - S, dependence broken). The connectivity matrix is identical in
both settings. H2 holds when the broken-dependence setting gives verdict_agreement = 0 with a
positive gap while the intact-dependence setting collapses to agreement and zero gap.

## Determinism

A fixed-seed generator (`numpy.random.default_rng(0)`) is set at module load. The spread is exact
over reachable states, so the output is byte-identical on re-run. An instrument control validates
the classifier on the faithful triad (reads triadic, max Φ_MIP = 2.0) before any result is read.

## Scope

The accounts are coder-supplied rule sets, not measured worker states. The construct scored is
divergence between two stated accounts. The result is on synthetic data and does not measure a
real hiring coordination.
