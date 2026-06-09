# Q75 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, synchronous update. The base triad is E'=M, M'=E∧R, R'=M (Q63
read_recipient). Spectators are added and the maximal complex is read with `probes.lib.major_complex`. Run
on `~/iit-playground/venv-4.0/bin/python`. Decision rules fixed here.

Forms:
- **uncoupled(k)** (E, M, R, S1..Sk): the triad plus k frozen spectators Si'=Si with no edges to the
  triad, for k = 1, 2, 3 (n = 4, 5, 6).
- **read_only** (E, M, R, T): the triad plus T'=M (T reads M; read by none).
- **emit_only** (E, M, R, G): the triad plus a constant source G'=G that the commit does not depend on.

## Test (`probe_spectator_robustness.py`)

- **Measure:** the maximal complex (label set and Φ) for each form.
- **Decision rules:**
  - H1 confirmed if every uncoupled(k) has maximal complex {E, M, R} at Φ=2.0.
  - H2 confirmed if read_only has maximal complex {E, M, R}.
  - H3 confirmed if emit_only has maximal complex {E, M, R}.
  - H4 confirmed if every form's maximal-complex Φ is 2.0.
