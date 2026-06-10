# Q108 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 verdict over the 256-form family. Run on `~/iit-playground/venv-4.0/bin/python`.

## Construction (`forms.py`)

The read-recipient triad is (0,1, 0,1, 0,0,0,1) in the 8-bit encoding: worker read (bits 0-1), counterpart
read (bits 2-3), mediator function (bits 4-7). `control_sweep` varies one party's bits over all settings,
holding the rest fixed, and returns whether each setting is triadic. The worker and counterpart sweep 4
one-input functions each; the mediator sweeps 16 two-input functions.

## Decision rules (`probe_controllability.py`)

- H1 confirmed if the mediator sweep reaches both verdicts.
- H2 confirmed if each outer party's sweep reaches both verdicts.
- H3 confirmed if the mediator has more triadic settings than either outer party.
- H4 confirmed if each outer party has exactly one triadic setting.
