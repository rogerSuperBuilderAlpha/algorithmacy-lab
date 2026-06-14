# Q101 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 cause-effect structure via PyPhi's `phi_structure`, read at the all-ones integrating state.
Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Triadic: read_recipient, all_required market (k=2), required market (N=2). Dyadic controls: broadcast,
one_shot. For each, `binding_specified_state` finds the binding distinction (a single-party mechanism whose
purview spans two or more parties) and returns its purview and specified effect and cause states;
`max_joint_specified_state` returns the highest-order distinction's specified effect state.

## Decision rules (`probe_what_it_distinguishes.py`)

- H1 confirmed if the read-recipient binding distinction's purview has two or more parties.
- H2 confirmed if its specified effect state is all-ones.
- H3 confirmed if no dyadic form has a binding distinction.
- H4 confirmed if every triadic form's binding distinction specifies an all-ones effect state.
