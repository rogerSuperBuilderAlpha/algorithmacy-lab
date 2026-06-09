# Q84 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems. The base triad is E'=M, M'=E∧R, R'=M. An agent X (index 3) is added in
three couplings, and per the Q74 rule the verdict is read on the maximal complex (`probes.lib.major_complex`),
with the whole-system verdict (`classifier.classify_rules`) reported alongside. Run on
`~/iit-playground/venv-4.0/bin/python`.

Couplings:
- **read_only**: X'=M (X reads M); M' unchanged. X is read by none.
- **emit_only**: X'=X (constant source); M' unchanged (does not depend on X).
- **bidir_pivotal**: M'=E∧R∧X (M reads X) and X'=M (X reads M).

## Test (`probe_adversarial_agent.py`)

- **Measure:** per coupling, the whole-system verdict and Φ, and the maximal complex (label set and Φ).
- **Decision rules:**
  - H1 confirmed if read_only has maximal complex {E, M, R} with Φ > 0.
  - H2 confirmed if emit_only has maximal complex {E, M, R} with Φ > 0.
  - H3 confirmed if bidir_pivotal's maximal complex is not {E, M, R}.
  - H4 confirmed if both read_only and emit_only have a triadic maximal complex (no flip to dyadic).
