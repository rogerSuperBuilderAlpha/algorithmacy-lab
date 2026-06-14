# Q91 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 Φ on a stochastic state-by-node TPM (`probes.lib.max_phi_float`). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Form (`forms.py`)

The read-recipient triad with a binary symmetric channel of error e on the mediator's read of the
recipient. Worker E (0), mediator M (1), recipient R (2):
- E' = M, R' = M (deterministic).
- P(M'=1 | E, R) = E · [(1-e)·R + e·(1-R)] — the mediator ANDs the worker with the recipient as seen
  through the channel.

Channel errors swept: 0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5.

## Decision rules (`probe_lossy_channel.py`)

- H1 confirmed if Φ > 0 at e = 0.
- H2 confirmed if Φ = 0 at e = 0.5.
- H3 confirmed if Φ is non-increasing across the sweep and strictly lower at e = 0.5 than at e = 0.
- H4 confirmed if Φ > 0 at e = 0.4.
