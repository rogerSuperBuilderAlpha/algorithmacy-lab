# q171 — findings

The two opacities do not stack. Both hypotheses about how drift and interest combine were fixed before
computing; the sweep refuted the super-additive one and supported the re-integration one.

## Φ over the drift x interest grid (approve agenda, a = 1)

| d \ k | k=0   | k=1   | k=2   | k=3   | k=4   |
|-------|-------|-------|-------|-------|-------|
| 0.0   | 2.000 | 0.500 | 0.000 | 0.000 | 0.000 |
| 0.1   | 0.719 | 0.500 | 0.000 | 0.000 | 0.000 |
| 0.25  | 0.452 | 0.500 | 0.000 | 0.000 | 0.000 |
| 0.5   | 0.207 | 0.415 | 0.000 | 0.000 | 0.000 |

The k = 0 row is the pure-drift PP4 ladder (Φ falls from 2.0 to 0.207). The d = 0 column is the
pure-interest Q126 ladder (Φ falls from 2.0 to 0). At k = 1 the two cross: drift barely moves Φ off
the 0.500 interest plateau.

## H1 — super-additive destruction: REFUTED

At every interior cell the combined Φ sits far above the multiplicative null Φ(d, 0)·Φ(0, k)/Φ(0, 0),
not below it. At approve d = 0.5, k = 1 the combined Φ is 0.415 against a null of 0.052. The erosions are
sub-additive: where interest has already overridden a state, drift on the rest cannot also erode it, so
the joint effect is milder than the product of the separate effects.

## H2 — drift re-integrates an interested mediator: SUPPORTED

| agenda | d    | k | Φ(d=0, k) baseline | Φ(d, k) with drift |
|--------|------|---|--------------------|--------------------|
| deny   | 0.1  | 1 | 0.000              | 0.074              |
| deny   | 0.25 | 1 | 0.000              | 0.193              |
| deny   | 0.5  | 1 | 0.000              | 0.415              |

Under the deny agenda at k = 1 the pure-interest baseline is Φ = 0: overriding the one state where the
parties warrant the commit kills party-dependence. Adding drift re-introduces it. Φ climbs from 0 to
0.415 as d rises to 0.5. Retraining partially re-integrates an interested mediator.

## Reading

One opacity masks the other. Interest erodes the binding by deleting party-dependence in the overridden
states; drift erodes it by averaging the faithful states toward a coin flip. When both act, drift can
only touch states interest has not already flattened, and on the deny agenda it restores dependence that
interest had removed. The result is on synthetic data: a property of how the two Boolean constructions
compose, not a measurement of a platform.
