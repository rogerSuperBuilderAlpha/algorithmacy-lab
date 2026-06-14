# Q94 — Stage 4 methods (fixed before computation)

Ground truth is the exclusion-resolved set of irreducible complexes (PyPhi `new_big_phi`), computed with
exact IIT-4.0 Φ. Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Two minimal mutual-determination units, {A,B} with A'=B, B'=A and {C,D} with C'=D, D'=C, coupled four
ways:
- **disjoint** — no coupling.
- **shared_spectator** — both units also AND in an idle fifth node E (E'=E), which reads nothing back.
- **one_way_bridge** — C also reads B (unit 2 reads unit 1), not the reverse.
- **mutual_bridge** — B reads C and C reads B (the units read each other).

`disjoint_complexes_at` resolves PyPhi's irreducible-complex lattice at a state into disjoint maximal
complexes, greedily by descending φ (a complex is skipped if it overlaps one already taken or has φ ≈ 0).
`max_disjoint_complexes` takes the tiling with the most complexes over reachable states.

## Decision rules (`probe_multiple_complexes.py`)

- H1 confirmed if the disjoint form has two complexes.
- H2 confirmed if the shared-spectator form has two complexes.
- H3 confirmed if the one-way-bridge form has two or more complexes.
- H4 confirmed if the mutual-bridge form has one complex spanning {A, B, C, D}.
