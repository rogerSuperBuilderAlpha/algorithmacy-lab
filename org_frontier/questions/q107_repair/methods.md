# Q107 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict over the 256-form family, with repair distance computed as the construction distance
(Q105). Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

The read-recipient triad encoded as (0,1, 0,1, 0,0,0,1) — worker read bits 0-1, counterpart read bits 2-3,
mediator function bits 4-7. Two damaged forms:
- **binding_damaged** — the mediator function made independent of the counterpart (the broadcast),
  (0,1,0,1,0,1,0,1).
- **liveness_damaged** — the counterpart's read of the mediator made constant, (0,1,0,0,0,0,0,1).

`repair` returns the minimal Hamming distance to a triadic form and the bits achieving a distance-1 repair.

## Decision rules (`probe_repair.py`)

- H1 confirmed if both damaged forms have a finite repair distance.
- H2 confirmed if the binding-damaged form's distance-1 repair bits are all mediator bits.
- H3 confirmed if the liveness-damaged form's distance-1 repair bits are all counterpart-read bits.
- H4 confirmed if neither damaged form's distance-1 repair touches the other lever's bits.
