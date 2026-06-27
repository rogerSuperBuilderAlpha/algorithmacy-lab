# Only synchronous commitment binds: the commit-period sweep

<code + data: org_frontier/questions/q209_commit_period/ ; probe #363 in probes/PROBES.md>

## Abstract

q207 found that a mediator recomputing every second step factors a triad. This sweeps the commit period
p = 1, 2, 3, 4, gating the conjunctive mediator with a mod-p counter, and finds that synchronous commitment
is the unique binding cadence: the triad is triadic at Φ = 2.0 at p=1 and dyadic at Φ = 0 at every p ≥ 2,
with no threshold and no recovery. The surviving structure is period-invariant — a single self-toggling bit
at Φ = 1.0 at every period, never the multi-bit counter, because the counter's carry is one-directional.
Read against q208, where represented latency of any depth left the triad triadic at Φ = 2.0, the two
mediator deformations are opposite and both flat: a mediator can be arbitrarily late and still bind, but it
cannot be slowed at all and bind.

## Introduction

A mediating system binds a triad when its commitment is irreducible across the parties. q207 showed that
slowing the mediator to every second step dissolves that binding, leaving only a clock. It tested one
period. Whether the dissolution is a threshold at period two or holds at every period, and how the residual
structure scales, were open.

## Related work

q207 (slow mediator) is the single-period predecessor. q208 (latency depth) is the companion sweep on the
other deformation. The conjunctive triad and its Φ_MIP = 2.0 verdict are the reference form.

## Hypotheses

H1 (control): F_1 reads triadic at Φ=2.0. H2: every period p ≥ 2 is dyadic. H3: the triad leaves the core
at every p ≥ 2. H4: the surviving counter's Φ is non-decreasing in period. H5: whole-system Φ_MIP is zero
at every p ≥ 2. Nulls are the negations, fixed in `hypotheses.md` before computing.

## Methods

F_p gates the mediator with a mod-p counter: S' = W∧C only when the counter reads zero, S' = S otherwise,
with W' = C' = S every step. F_1 is the synchronous triad (n=3); F_2 a 1-bit toggle (n=4, q207's form); F_3
and F_4 a 2-bit counter cycling mod 3 and mod 4 (n=5). Verdicts use `probes/lib.verdict`, cores
`major_complex`. The instrument control passed (triadic, Φ = 2.000000) before any other number was read.

## Results

H1 confirmed. H2 confirmed: p=2, 3, 4 are all dyadic; only p=1 binds. H3 confirmed: no triad member sits in
any p ≥ 2 core. H5 confirmed: whole-system Φ_MIP is zero at every p ≥ 2. H4 is confirmed in the weak sense
that the core Φ does not fall — but it does not rise either: it is exactly 1.0 at p = 2, 3, 4. The surviving
complex is a single self-toggling bit at every period (K, then c0, then c1), never the two-bit counter,
because the counter's low bit flips independently of the high bit and the pair is not mutually irreducible.

## Discussion

Synchronous commitment is the only cadence that binds the parties, and the residual after binding fails is
the same at every period. The commit-period axis is therefore flat and fatal: any slowing dissolves the
triad completely, and a longer period does not deepen or soften the dissolution. Set beside q208, the
mediator-deformation picture is complete. Latency depth is flat and benign — the triad holds at Φ = 2.0 at
every depth. Commit period is flat and fatal — the triad is gone at Φ = 0 at every period. The operative
distinction is between when a commitment arrives and how often it is made. Lateness is free; intermittency,
at any degree, is total.

## Limitations

One model of a slow cadence, a mod-p counter gating the recompute. n ≤ 5, periods to four, one reference
triad, conjunctive coupling, exact Φ. The counter bit's Φ = 1.0 is a property of a deterministic toggle.
In-silico; no empirical coordination is modeled.

## References

q207 (org_frontier/questions/q207_slow_mediator/); q208 (org_frontier/questions/q208_latency_depth/).
