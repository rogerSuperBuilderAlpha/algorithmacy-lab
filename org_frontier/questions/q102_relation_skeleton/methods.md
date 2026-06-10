# Q102 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 cause-effect structure via PyPhi's `phi_structure`, read at the all-ones integrating state.
Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Mediated: read_recipient, all_required market (k=2). Symmetric: ring (d=2), required market (N=2). For each,
`relation_skeleton` returns the relation count, the hub purview (the purview carrying the most relations) and
its share of all relations, and the maximal relation order (the most distinctions any one relation binds).
A relation's purview is keyed by its node indices.

## Decision rules (`probe_relation_skeleton.py`)

- H1 confirmed if both mediated triads have a hub purview with share above 0.5.
- H2 confirmed if the all-required market's relations-per-distinction exceeds the read-recipient triad's.
- H3 confirmed if both symmetric triads have no purview with share above 0.5.
- H4 confirmed if the all-required market's hub share exceeds 0.9 and its maximal relation order is at least 5.
