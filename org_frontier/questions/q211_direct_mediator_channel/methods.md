# Q211 — Stage 4 methods

For each hypothesis: the form or ensemble (exact rules/parameters), the measure, the controls, and the
decision rule fixed before the run. A reader should reproduce every test from this file alone.

## Shared infrastructure
- Verdict / Φ / major complex: `probes/lib.py` (`verdict`, `major_complex`), `classifier.classifier`
  (`PHI_EPS`).
- Python: run from the repo root with the project venv (`venv-4.0`), `PYPHI_WELCOME_OFF` set.

## Model (n=6)
Node order: W1, S1, C1, W2, S2, C2. Each triad is the standard conjunctive triad:
W1'=S1, S1'=channel(W1∧C1, S2), C1'=S1 and symmetrically W2'=S2, S2'=channel(W2∧C2, S1), C2'=S2.
The channel couples the two mediators directly, swept three ways:
- **none** (control): S1'=W1∧C1, S2'=W2∧C2 — two separate triads, no channel.
- **AND**: S1'=W1∧C1∧S2, S2'=W2∧C2∧S1 — each mediator commits only if its own triad is ready and the other mediator fired.
- **OR**: S1'=(W1∧C1)∨S2, S2'=(W2∧C2)∨S1 — each mediator commits if its own triad is ready or the other mediator fired.

This mirrors q210's three-way bridge sweep, with the link moved from a shared counterpart to a direct
mediator-mediator channel.

## Instrument control (run first)
The single conjunctive triad (W,S,C) with S'=W∧C, W'=S, C'=S. Must read triadic at Φ=2.000000 before any
other number is trusted.

## H1 test
- **Form:** single triad control, plus the none-channel six-node form.
- **Measure:** verdict (structure, Φ_MIP) and `major_complex`.
- **Decision rule:** control triadic at Φ=2.0; none-channel whole system factors (Φ_MIP=0) with the major complex one triad at Φ=2.0.

## H2 test
- **Form:** AND-channel six-node form.
- **Measure:** `major_complex` membership.
- **Decision rule:** confirmed if the AND-channel major complex contains nodes from both triads (triad-1 ∩ core ≠ ∅ and triad-2 ∩ core ≠ ∅); refuted if it lies inside one triad.

## H3 test
- **Form:** AND-channel form.
- **Measure:** core Φ from `major_complex`.
- **Decision rule:** confirmed if AND-channel core Φ > 2.0 + PHI_EPS.

## H4 test
- **Form:** all three channel rules.
- **Measure:** `major_complex` membership per rule.
- **Decision rule:** confirmed if at least one rule produces a core spanning both triads (none did in q210).

## H5 test
- **Form:** AND and OR channel forms.
- **Measure:** core membership and Φ.
- **Decision rule:** confirmed if the AND core and OR core differ in membership or in Φ (by more than PHI_EPS).
