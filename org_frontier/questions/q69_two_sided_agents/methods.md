# Q69 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems on four elements (E, As, Ar, R), synchronous update, read on the maximal
complex (`probes.lib.major_complex`) and classified by exact IIT-4.0 Φ (`classifier.classify_rules`).
Instrument validated on a decoupled relay (dyadic) and a fully-coupled triad (triadic) first. Run on
`~/iit-playground/venv-4.0/bin/python`. State tuple x = (E, As, Ar, R). Decision rules fixed here.

Configurations:
- **live_chain:** E'=As, As'=E∧Ar, Ar'=As∧R, R'=Ar.
- **delegated:** E'=E, As'=E∧Ar, Ar'=As∧R, R'=R. (humans frozen source/readout; agents mutual)
- **closed_ring:** E'=R∧As, As'=E∧Ar, Ar'=As∧R, R'=Ar∧E.

## Test (`probe_two_sided.py`)

- **Measure:** per configuration, the major complex (label set, size) and its Φ.
- **Decision rules:**
  - H1 confirmed if the live_chain major complex is a size-two pair containing a human (E or R).
  - H2 confirmed if the delegated major complex is exactly {As, Ar}.
  - H3 confirmed if the delegated major complex has Φ > 0.
  - H4 confirmed if the closed_ring major complex is the full set {E, As, Ar, R} with Φ > 2.0.
