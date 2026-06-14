# Q79 — Stage 4 methods (fixed before computation)

The agent's commit is a probabilistic mixture. Over the state-by-node TPM on (E=bit0, M=bit1, R=bit2):
E'=M and R'=M are deterministic, and P(M'=1) = p·(E∧R) + (1−p)·E, the p-mixture of reading the recipient
and ignoring it. Exact max-Φ is computed with `probes.lib.max_phi_float`, which accepts a stochastic TPM
and infers connectivity. p is swept over {0, 0.25, 0.5, 0.75, 1.0}. Run on `~/iit-playground/venv-4.0/bin/python`.

## Test (`probe_stochastic_threshold.py`)

- **Measure:** max-Φ at each p.
- **Decision rules:**
  - H1 confirmed if Φ=2.0 at p=1 and Φ=0 at p=0.
  - H2 confirmed if Φ is non-decreasing across the p grid.
  - H3 confirmed if Φ>0 at p=0.25, 0.5, 0.75.
  - H4 confirmed if Φ>0 at p=0.25.
