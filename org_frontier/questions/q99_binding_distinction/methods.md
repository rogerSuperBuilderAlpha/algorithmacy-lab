# Q99 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 cause-effect structure via PyPhi's `new_big_phi.phi_structure`, read at the integrating
state (all-ones if reachable and integrating, else the reachable state of maximum structure Φ). Run on
`~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Triadic: read_recipient (M'=E∧R); all_required market at k=2 (Q64); open chain and ring at depth 2 (Q66);
required agent market at N=2 (Q85). Dyadic controls: broadcast (M'=E); one_shot; substitutable at k=2.

For each form, `ces` returns the distinctions as (mechanism, effect purview, φ_d) and the structure Φ.
`dual_pair` searches for a spanning distinction (single-party mechanism, purview of two or more parties)
paired with a higher-order distinction whose mechanism equals that purview and whose purview is the
spanning mechanism.

## Decision rules (`probe_binding_distinction.py`)

- H1 confirmed if every triadic form has a dual pair.
- H2 confirmed if, for every triadic form, the maximal-φ_d distinction is a higher-order mechanism with
  φ_d equal to the system Φ.
- H3 confirmed if no dyadic form has a dual pair.
- H4 confirmed if, for every triadic form, the dual pair's mechanisms and purviews cover every party.
