# q161 — Findings

Both hypotheses were fixed before computing. Both fail, and the way they fail reverses the
expected ranking of the three verdicts.

## Corpus-mean agreement vs flip

| flip | 0.02 | 0.05 | 0.08 | 0.12 | 0.18 | 0.30 | best−worst |
|------|------|------|------|------|------|------|-----------|
| triad/dyad | 0.619 | 0.531 | 0.487 | 0.456 | 0.478 | 0.484 | 0.162 |
| membership | 0.436 | 0.462 | 0.484 | 0.524 | 0.539 | 0.553 | 0.117 |
| bottleneck | 0.753 | 0.809 | 0.822 | 0.838 | 0.838 | 0.844 | 0.091 |

Bottleneck recovery is both the highest-agreement verdict and the flattest across flip. It rises
with flip rather than degrading. The triadic/dyadic verdict has the widest spread across flip and
sits near chance once the flip leaves its low end.

## Verdicts

H1: REFUTED. The triadic/dyadic call is correct at every swept flip for only 5 of 16 forms
(0.312), far below the 0.80 the hypothesis required. Bottleneck recovery degrades by 0.091 across
flip, below the 0.20 the hypothesis required, and the degradation runs the wrong way: bottleneck
recovery is the most robust verdict, not the most fragile.

H2: NOT SUPPORTED. The per-form optimal flip varies across forms (four distinct optima among the
swept rates), so a single flip is not optimal for all forms. The optimum does not track intrinsic
update entropy: the Spearman correlation is -0.148, weak and the wrong sign for the predicted
positive relation. The variation in optima is real, but entropy does not explain it.

## Reading

The verdict that names a single node (the bottleneck) survives flip-rate misspecification best,
because the argmax of coupling centrality is a rank statistic that holds while every centrality
value shifts with noise. The verdict that reads a corpus-wide threshold (triadic/dyadic via the
prominence spread) is the most fragile, because the threshold is calibrated at one flip and the
spread it reads moves with the flip. Robustness here is a property of how the verdict is decoded,
not of how much structure the form has.

These are agreement rates on synthetic Boolean forms. The number that survives misspecification is
the rank-based articulation pick; the threshold-based labels do not. The Phi-to-organization
bridge is open, so the practical lesson is for the CRQA decoding step, not for any measured field
case.
