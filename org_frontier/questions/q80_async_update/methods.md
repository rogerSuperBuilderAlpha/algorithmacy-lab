# Q80 — Stage 4 methods (fixed before computation)

Asynchronous update is modelled as a stochastic state-by-node TPM: P(element j' = 1) = (1/n)·f_j(state) +
(1 − 1/n)·current_j, where f_j is the element's synchronous rule and the hold term is its current value.
The synchronous deterministic TPM comes from `classifier.tpm_from_rules`; the asynchronous TPM is built
from it. Synchronous verdicts come from `classifier.classify_rules`; asynchronous max-Φ from
`probes.lib.max_phi_float`. Run on `~/iit-playground/venv-4.0/bin/python`. Keystones: read_recipient
(E'=M, M'=E∧R, R'=M), broadcast (E'=M, M'=E, R'=M), all_required (M'=E∧R1∧R2).

## Test (`probe_async_update.py`)

- **Measure:** per keystone, the synchronous verdict and the asynchronous max-Φ and verdict.
- **Decision rules:**
  - H1 confirmed if asynchronous read_recipient is triadic (Φ>0).
  - H2 confirmed if asynchronous broadcast is dyadic (Φ~0).
  - H3 confirmed if asynchronous all_required is triadic.
  - H4 confirmed if every keystone's synchronous and asynchronous verdict agree.
