# Q89 — Stage 4 methods (fixed before computation)

Deterministic Boolean systems classified by exact IIT-4.0 Φ (`classifier`) and read on the major complex
(`probes.lib.major_complex`). Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Worker E (node 0), agents M1..MN (nodes 1..N), counterpart C (node N+1). Each agent reads by type:
full (E∧C), sender (E), or recipient (C). The outer parties read forward a chosen active set of agents
through AND (all-required) or OR (substitutable); agents outside the active set are passive (read their
inputs, but nothing reads them).

Configurations:
- **full_pair_required** — two full agents, both required (control; reproduces Q85 N=2 all-required).
- **one_passive** — two full agents, only M1 read forward; M2 is passive.
- **sender_only_req** — a full agent and a sender-only agent, both required.
- **recipient_only_req** — a full agent and a recipient-only agent, both required.
- **mixed3_required** — full, sender-only, and recipient-only agents, all three required.
- **hetero_substitutable** — a full and a sender-only agent read forward through OR.

## Decision rules (`probe_heterogeneous_market.py`)

- H1 confirmed if the passive agent is absent from the major complex and the core is {E, M1, C}.
- H2 confirmed if the sender-only required agent is in the core and the market is triadic.
- H3 confirmed if mixed3_required is triadic with core {E, M1, M2, M3, C} and the recipient-only required
  agent is in its core.
- H4 confirmed if hetero_substitutable is dyadic.
