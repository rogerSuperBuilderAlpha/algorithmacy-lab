# q184 — methods

## The two accounts

Both accounts are rule sets over the same labels `(D, P, R)` = (Driver, Platform, Rider),
evaluated on the little-endian current-state tuple `x = (D, P, R)`.

**Platform commit account.** `[x1, x0 & x2, x1]`. The platform P commits the driver-rider match:
P turns on only when both the driver and the rider are on, and the driver and the rider each track
the platform. This is the worker-system-counterpart shape. It reads `triadic` with max Φ_MIP =
2.0, and its major-complex core is `{D, P, R}`.

**Driver suggestion account.** `[x1, x0, x1]`. Dispatch is a one-way suggestion: the platform P
tracks the driver D only, and the rider is not wired into the loop. It reads `dyadic` with
Φ_MIP = 0.0, and its core is `{D, P}`. The rider drops out.

## The bridge

The probe calls `spread(driver_suggestion, platform_commit, labels)` from
`org_frontier.qualitative.disagreement_phi`, built and validated in q183. The bridge runs each
account through `verdict()` and `major_complex()` from `org_frontier.probes.lib`, which wrap the
exact IIT-4.0 Φ classifier. Φ is not reimplemented. The spread returns verdict_agreement, phi_gap
(absolute difference of the two whole-system max Φ_MIP values), core_jaccard (Jaccard overlap of
the two major-complex cores), and both_verdicts.

## Controls

**Instrument control.** The faithful triad `[x1, x0&x2, x1]` with labels `(W, S, C)` reads
`triadic` with max Φ_MIP = 2.0. The probe aborts on failure.

**Consensus control.** Both parties narrate the same commit account:
`spread(platform_commit, platform_commit, labels)`. Expected to give zero spread
(verdict_agreement = 1, phi_gap = 0.0, core_jaccard = 1.0), confirming the metric anchors at zero
when the accounts agree.

## Decision rules

- H1 supported iff the driver account is not triadic, the platform account is triadic,
  verdict_agreement = 0, and |phi_gap − platform max Φ_MIP| < 1e-9.
- H2 supported iff R is in the platform core, R is absent from the driver core, and
  core_jaccard < 1.0.

## Determinism

The probe seeds `numpy.random.default_rng(0)`. The spread is exact (it reads classifier verdicts
over enumerated reachable states), so the output is byte-identical on re-run. This was confirmed
across three runs.

## Scope

The accounts are synthetic, coder-supplied rule sets, not measured driver or rider states. The
construct is divergence between two stated accounts of one dispatch. The empirical arms are on
synthetic data. The gap between a coded account and an observed dispatch is not closed here.
