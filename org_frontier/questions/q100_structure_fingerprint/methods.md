# Q100 — Stage 4 methods (fixed before computation)

Exact IIT-4.0 cause-effect structure via the `structure_suite` and PyPhi's `phi_structure`, read at the
integrating state. Run on `~/iit-playground/venv-4.0/bin/python`.

## Forms (`forms.py`)

Six keystone triads, one per coordination kind: read_recipient (joint determination, mediated); all_required
market at k=2 (breadth); open chain at depth 2; ring at depth 2; required market at N=2; the Q68 triage
bidirectional form (delegation). For each, `fingerprint` returns the Φ-structure suite (distinction count,
relation count, maximal order) read at the integrating state, plus the dual type from Q99 and the system Φ.

## Decision rules (`probe_structure_fingerprint.py`)

- H1 confirmed if at least four of the six keystones have pairwise-distinct fingerprints on
  (n_distinctions, n_relations, max_order, dual_type).
- H2 confirmed if at least two dual types appear among the keystones.
- H3 confirmed if two keystones have equal Φ but different fingerprints.
- H4 confirmed if the Spearman correlation of relation count with Φ across the keystones exceeds 0.5.
