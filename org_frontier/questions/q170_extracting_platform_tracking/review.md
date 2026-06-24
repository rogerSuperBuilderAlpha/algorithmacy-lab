# Q170 review

## What the study claims

After equal probing, the worker's recovered model of an interested mediator is less faithful than her
model of a faithful one (H1), and the fidelity loss peaks at the k where the mediator's Shapley share
equalizes with the parties (H2). Both verdicts read off the printed numbers.

## Checks

- Instrument control: the faithful triad reads `triadic` with `max_phi` 2.0 before any sweep. Pass.
- Determinism: the probing loop is seeded with `numpy.random.default_rng(0)`; three runs are
  byte-identical.
- The value-equalization k is computed from Q131's Shapley split, not assumed, and lands at k = 1
  independently of the probing measures.
- KL and recoverable fraction agree: the KL peak (1.00 bits) and the steepest recoverable-fraction drop
  both fall at k = 1.

## Threats and how the study handles them

- Budget dependence: a finite budget could let sampling noise drive the KL ordering. At 4000 probes the
  recovered marginals sit within 0.02 of their exact values, so the ordering reflects the gates, not
  noise. The closed-form residual (Q168, `residual_surprise_under_mediator`) gives the same shape.
- Agenda choice: only the approve ladder is charted because the deny agenda collapses at k = 1, leaving
  no graded comparison. This is stated, not hidden.
- Reading the peak as "extraction": the alignment of the KL peak with the Q131 equalization k is a
  numerical coincidence on this triad until shown on richer forms. The claim is about the construct under
  the model.

## Scope

Synthetic probing data and exact Φ on three nodes. No worker is measured. The empirical claim is about the
construct, not a real platform; the Φ-to-economic-value bridge is open (Q122).
