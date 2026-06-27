# Q209 — findings

The conjunctive triad with its mediator gated by a mod-p counter, swept the commit period p = 1, 2, 3, 4
(n = 3, 4, 5, 5), exact IIT-4.0 Φ.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | F_1: triadic, Φ_MIP = 2.000000 |
| H2 rate-1 is the unique binding cadence | confirmed | p=2,3,4 all dyadic; only p=1 binds |
| H3 the triad leaves the core at every p≥2 | confirmed | no triad member in any p≥2 core |
| H4 the surviving counter's Φ is non-decreasing in period | confirmed (but flat) | core Φ is 1.000 at p=2, 3, 4 — invariant, not growing |
| H5 whole-system Φ_MIP is zero at every p≥2 | confirmed | Φ_MIP = 0 at p=2, 3, 4 |

Cores by period: p=1 {W,S,C} Φ=2.0; p=2 {K} Φ=1.0; p=3 {c0} Φ=1.0; p=4 {c1} Φ=1.0.

## Synchronous commitment is the only binding cadence, and the residual is period-invariant

Any slowing of the mediator's commit cadence dissolves the triad. At period one the conjunctive triad is
triadic at Φ_MIP = 2.0; at every period two, three, and four the whole system reads dyadic with Φ_MIP = 0,
no triad member in the major complex. q207's single point — period two factors the triad — is the whole
curve: there is no threshold and no recovery. Synchronous commitment is the unique cadence that binds the
parties.

The surviving structure is the same at every period. Whatever the counter's modulus, the major complex is a
single self-toggling bit at Φ = 1.0 — the toggle K at period two, one counter bit (c0, then c1) at periods
three and four. The two-bit counter does not form an integrated pair, because its carry runs one way: the
low bit flips every step regardless of the high bit, so the bits are not mutually irreducible and only one
of them stands as the complex. The prediction that a longer period would carry more residual integration is
wrong. The residual is invariant — exactly one oscillating bit, Φ = 1.0 — no matter how the cadence is
built.

This completes the mediator-deformation map against q208. Latency depth is benign: a represented delay,
however deep, leaves the triad triadic at Φ = 2.0. Commit period is uniformly fatal: any period above one
factors the triad to Φ = 0. The two deformations are opposite in outcome and both flat in it — depth keeps
full integration at every depth, period destroys it at every period. A mediator can be arbitrarily late and
still bind; it cannot be slowed at all and bind.

## Caveats

One model of a slow cadence — a mod-p counter gating the recompute so the mediator holds between resets.
n ≤ 5, periods up to four, one reference triad, conjunctive coupling, exact Φ. The counter bits' Φ = 1.0 is
a property of a deterministic toggle, not of the coordination. In-silico; evidence about how commit cadence
shapes irreducibility, not a measurement of any organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q209_commit_period.probe_commit_period`
