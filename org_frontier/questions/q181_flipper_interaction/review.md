# q181 — Review

## What the probe does

Reads a 2x2 account grid through the field bridge and a contested-case CI comparison. The
instrument control validates three machinery points before any result: the faithful triad
reads triadic at Φ = 2.0, the double flipper reads dyadic at 0.0, and a spectator-only node
leaves the major complex at the triad (W, S, C) at Φ = 2.0. The control passes.

## Determinism

All draws are seeded with fixed generators. Three consecutive runs are byte-identical.

## Strength of the H1 claim

H1 rests on a clean enumeration: four cells, exact Φ on each, no triadic re-emergence in
the double-flipper cell. The masking reading follows directly from each single flipper
already reaching the Φ floor. The claim is strong and determinate at pool size k = 2; the
account family is one structure, not a basis sweep, so the generality across worker and
counterpart couplings is asserted for this account rather than enumerated. A wider basis
sweep (as in q176) would harden it.

## The H2 result is a real negative

H2 fails in an informative direction. The joint CI is 41.8% narrower than the union, which
is neither composition nor amplification. The mechanism is that contesting two redundant
flips concentrates coders on the Φ = 0 reading. The negative is reported honestly; the
amplification null is recorded as also failing, so the finding is not dressed as support
for the alternative. One caveat: the H2 statistic uses a single contest draw per panel with
fixed seeds, so the -0.418 gap is one realisation in the contest band, not a distribution
over splits. A sweep over many contest fractions would show whether contraction is generic
or seed-specific. The sign of the effect is structural (redundancy forces mass to 0), so
contraction is expected to hold, but its magnitude is a single point.

## Scope

Synthetic coded rule sets. No worker is measured. The empirical arms are on synthetic data.
The study tests how two coding flips combine in the instrument, not whether a coded account
matches an observed coordination.
