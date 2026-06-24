# q150 — review

## What was run

`probe_ring_chord_integration.py`. The instrument control runs the faithful triad and confirms it
reads `triadic` at max Φ_MIP 2.0 before any new computation. The study builds two six-node forms,
the unchorded `ring(6)` and the same ring with one chord across (A, D), and reads each with
`verdict`, `major_complex`, and `shapley` from existing machinery. Φ is not reimplemented.

## Robustness of the verdicts

H1 is a conjunction: Φ must rise and the cut must shift off the chord. The cut shift is real and is
read by parsing the classifier's cut string and testing whether A and D share a part. The Φ rise
does not occur (4.0 to 4.0), so H1 is refuted. The refutation is reported as such, with the cut
shift noted in the H1 detail line so the partial match is visible rather than hidden.

H2 is supported by a clean margin. The endpoints rise from 0.667 to 1.100 and the far arc falls from
0.667 to 0.450, well outside the 1e-3 tolerance. The total Φ is conserved at 4.0, so the effect is a
redistribution rather than a measurement artifact.

## Limits

The result is one topology at one size (n = 6) with one chord placement (the opposite pair). Whether
the flat-Φ, shifted-cut, concentrated-Shapley pattern holds for other ring sizes, other chord spans,
or multiple chords is not tested here. The Shapley value is read at the all-ones integrating state
only. Generalization across sizes and chord placements is the natural next study.

## Reproducibility

The RNG is seeded with `default_rng(0)`. The computations are exact enumerations over reachable
states. Two runs produced byte-identical output. `results/output.txt` is the captured stdout.

## Scope

In-silico. Synthetic Boolean models only. No real group is measured.
