# Q67 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems on four elements (E, A1, A2, R), synchronous update, classified by exact
IIT-4.0 Φ over the minimum-information partition (`classifier.classify_rules`) and read on the maximal
complex (`probes.lib.major_complex`). The instrument is validated on a decoupled relay (dyadic) and a
fully-coupled triad (triadic, Φ = 0.83) first. Run on `~/iit-playground/venv-4.0/bin/python`. Decision
rules fixed here.

The four reciprocity levels (rules over state tuple x = (E, A1, A2, R)):
- **L0 relay:** E'=E, A1'=E, A2'=A1, R'=A2.
- **L1 end-loop:** E'=E, A1'=E, A2'=A1∧R, R'=A2.
- **L2 open chain:** E'=A1, A1'=E∧A2, A2'=A1∧R, R'=A2.
- **L3 closed ring:** E'=R∧A1, A1'=E∧A2, A2'=A1∧R, R'=A2∧E.

## Test — one probe over the four levels (`probe_reciprocity_gradient.py`)

- **Measure:** per level, the whole-system verdict and Φ_MIP, and the maximal complex (label set, size, Φ).
- **Decision rules:**
  - H1 confirmed if L0 is dyadic.
  - H2 confirmed if L1 is triadic and its maximal complex has two elements.
  - H3 confirmed if the maximal complex has two elements at L2 and four at L3.
  - H4 confirmed if Φ_MIP(L0) < Φ_MIP(L2) < Φ_MIP(L3).
