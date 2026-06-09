# Q83 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems, read on the maximal complex (`probes.lib.major_complex`). Base triad E'=M,
M'=E∧R, R'=M. Gating agents Ti read the message (Ti'=M) and gate delivery to R. Run on
`~/iit-playground/venv-4.0/bin/python`. State tuple in label order.

Forms:
- **both_required** (E, M, R, T1, T2): R'=M∧T1∧T2; Ti'=M.
- **either_suffices** (E, M, R, T1, T2): R'=M∧(T1∨T2); Ti'=M.
- **single_bidir** (E, M, R, T): R'=M∧T; T'=M (the Q68 bidirectional triage).

## Test (`probe_agent_coalition.py`)

- **Measure:** the maximal complex (label set and Φ) for each form.
- **Decision rules:**
  - H1 confirmed if both T1 and T2 are in the both_required major complex.
  - H2 confirmed if not both agents are in the either_suffices major complex.
  - H3 confirmed if T is in the single_bidir major complex.
  - H4 confirmed if every form's maximal complex has Φ > 0.
