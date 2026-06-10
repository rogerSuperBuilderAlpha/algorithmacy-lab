# Q106 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict (`probes.lib.verdict`) before and after each operation. Run on
`~/iit-playground/venv-4.0/bin/python`.

## Operations (`forms.py`)

Six operations on three levers:
- **binding** — add_binding (broadcast → read_recipient, the mediator reads the recipient) and
  remove_binding (the inverse).
- **liveness** — restore_liveness (one_shot → read_recipient, the recipient reads the mediator) and
  break_liveness (the inverse).
- **requirement** — require_all (substitutable → all_required at k=2) and substitute (the inverse).

Each entry gives the before and after forms; the build and break of a lever are inverses.

## Decision rules (`probe_design_operations.py`)

- H1 confirmed if every build operation takes a dyadic form to triadic.
- H2 confirmed if every break operation takes a triadic form to dyadic.
- H3 confirmed if, per lever, the build's output verdict equals the break's input verdict and vice versa.
- H4 confirmed if the operations span exactly three levers, each with one build and one break.
