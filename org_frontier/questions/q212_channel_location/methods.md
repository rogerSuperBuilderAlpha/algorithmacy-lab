# Q212 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`), `classifier.classifier`
  (`PHI_EPS`).
- Python: run from the repo root with the project venv (`venv-4.0`), `PYPHI_WELCOME_OFF` set.

## Model (n=6)
Node order: W1, S1, C1, W2, S2, C2. Both triads are the standard conjunctive triad (W'=S, S'=W∧C, C'=S). A
single AND channel adds one cross-triad conjunct at one homologous node pair, swept over three locations:
- **mediator** (q211 AND baseline): S1'=(W1∧C1)∧S2, S2'=(W2∧C2)∧S1; workers and counterparts plain.
- **worker**: W1'=S1∧W2, W2'=S2∧W1; mediators and counterparts plain.
- **counterpart**: C1'=S1∧C2, C2'=S2∧C1; mediators and workers plain.

A core spans both triads when it contains a member of {W1,S1,C1} and a member of {W2,S2,C2}.

## Instrument control (run first)
The single conjunctive triad (W,S,C) with S'=W∧C, W'=S, C'=S. Must read triadic at Φ=2.000000 before any
other number is trusted.

## H1 test
- **Form:** single triad control; mediator-channel six-node form.
- **Measure:** verdict and `major_complex`.
- **Decision rule:** control triadic Φ=2.0; mediator-channel major complex spans both triads at Φ=3.0 (reproducing q211).

## H2 test
- **Form:** worker-channel form.
- **Measure:** `major_complex` membership.
- **Decision rule:** confirmed if the worker-channel major complex spans both triads.

## H3 test
- **Form:** counterpart-channel form.
- **Measure:** `major_complex` membership and Φ.
- **Decision rule:** confirmed if the counterpart-channel major complex spans both triads with the same Φ as the worker channel (leaf symmetry).

## H4 test
- **Form:** all three locations.
- **Measure:** core Φ per location.
- **Decision rule:** confirmed if mediator-channel core Φ exceeds both the worker and counterpart core Φ (by more than PHI_EPS).

## H5 test
- **Form:** all three locations.
- **Measure:** core span and Φ per location.
- **Decision rule:** confirmed if the three locations are not all identical in span and Φ.
