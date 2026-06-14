# Q104 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 cause-effect structure (`phi_structure` via Q99's `ces`) and the verdict
(`probes.lib.verdict`). Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

The read-recipient triad (E'=M, M'=E∧R, R'=M). `distinctions_by_phi` ranks its distinctions by φ_d.
`KNOCKOUTS` removes each of the four reads in turn — the mediator's read of R (M'=E), the mediator's read
of E (M'=R), the worker's read of M (E'=E), and the recipient's read of M (R'=R) — and `knockout_verdicts`
recomputes the verdict for each.

## Decision rules (`probe_load_bearing.py`)

- H1 confirmed if the maximal-φ_d distinction has a mechanism or purview spanning two or more parties and
  its φ_d equals the system Φ.
- H2 confirmed if every single-party-to-single-party distinction has φ_d below Φ.
- H3 confirmed if knocking the mediator's read of a party makes the form dyadic.
- H4 confirmed if every edge knockout makes the form dyadic.
