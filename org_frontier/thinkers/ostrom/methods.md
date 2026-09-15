# Ostrom — Stage 4 methods

## Shared infrastructure

- Expression specs and evaluation from `org_frontier.thinkers.coleman.forms` (`V`, `NOT`, `AND`, `OR`,
  `compile_spec`, `delete`, `core_phi`, `fixed_points`); a deleted variable reads 0. Verdict via
  `probes.lib.verdict`; major complex via `probes.lib.major_complex`; subsystem Φ via
  `pyphi.new_big_phi.sia` on a `Subsystem` at a given reachable state.
- Run from the repo root on `~/iit-playground/venv-4.0/bin/python`.

## Instrument control (run first, in every probe)

The conjunctive triad by rules: Φ = 2.000000, core {A, M, B}.

## Forms

| form | rules |
|---|---|
| mutual | c_i' = (c_j ∧ c_k) ∨ (s_j ∧ s_k); s_i' = ¬c_j ∨ ¬c_k, for i ∈ {1,2,3}, {j,k} the others |
| coleman_closed | A' = B ∧ C; B' = ¬A ∨ C; C' = ¬A ∨ B |
| leviathan | L' = ¬(c1 ∧ c2 ∧ c3); c_i' = L |
| private | c_i' = c_i |
| self | c_i' = c_j ∧ c_k |
| nested | a2' = a1 ∧ a3; a3' = a1 ∧ a2; a1' = a2 ∧ a3 ∧ F; same for b; F' = a1 ∧ b1 |
| unnested | two copies of self, no F |
| bounded | self plus O' = c1 |
| breached | bounded with c1' = c2 ∧ c3 ∧ O |

## Decision rules

- **H1** CONFIRMED iff {c1, c2, c3} ⊆ core(mutual) and A ∉ core(coleman_closed). PARTIAL iff the first
  clause holds alone. REFUTED otherwise.
- **H2** CONFIRMED iff core(self) = {c1, c2, c3}, coreΦ(self) > coreΦ(leviathan) + 1e-6, advantage(L) > 1e-6,
  and private has no complex. PARTIAL iff two or three of four. REFUTED otherwise.
- **H3** CONFIRMED iff core(nested) = all seven, both local triads have subsystem Φ > 1e-6 at the state where
  the whole is maximal, and unnested's complexes are the two triads (core Φ of the whole equal to the triad's
  and core size three). PARTIAL iff two of three. REFUTED otherwise.
- **H4** CONFIRMED iff 111000 is fixed in mutual, all three single-defector states (c with one 0, s = 000)
  reach it, and coleman_closed's fixed point is 111. PARTIAL iff two of three. REFUTED otherwise.
- **H5** CONFIRMED iff core(bounded) = core(self) with |ΔΦ| < 1e-6 and V(O) = 0, and breached differs in
  core or has lower core Φ. PARTIAL iff the bounded clause holds alone. REFUTED otherwise.

## Reporting

Each probe prints the control, one line per form, and one verdict. Results in `results/<probe>.json`.
