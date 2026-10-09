# Q217 — Stage 4 methods

This file was written after the probes ran, as documentation of what was implemented. The original
specifications are the hypotheses in `hypotheses.md`, committed before each run (H1–H5 at 4b4f3d9e, before
probe 453; H6 before probe 454; H7–H8 before probe 455). Each section below marks which parts were specified in
advance and which were added later. Probe 456 was not pre-specified; it was added after independent review.

## Shared infrastructure
- Whole-system verdict and max Φ: `classifier.classifier.classify_rules` via `probes/lib.py:verdict`
  (max Φ_MIP over reachable states; triadic iff > PHI_EPS).
- Peak core: `probes/lib.py:major_complex`, the IIT-4.0 maximal complex at the reachable state with the highest Φ.
- Per-state maximal complex: `pyphi.new_big_phi.maximal_complex(net, state)` for each reachable state.
- Coalition φ_s: `threads/coalition_structure/_harness.py` (`phi_s_at` per state, `phi_s_maxstate` over states);
  integrating coalitions and veto sets: `threads/veto_player/_harness.py`.
- All forms are deterministic Boolean networks; node order is parties first, then clock bits.

## Instrument control (run first)
`python -m org_frontier.classifier.validate` must print `Instrument validated` before any number is trusted.
It passed before the runs and again when this file was written.

## Forms (implemented rules)
Parties A, B, C (and D) and clock bits T (and U). Unless stated, a non-chair party copies the current chair,
and the chair's next state is the AND of all other parties.

| Form | Probe | Chair schedule | Chair rule | Specified in advance? |
|---|---|---|---|---|
| F_fixed | 453 | A always; idle clock T' = ¬T (control) | B∧C | yes (H1–H5) |
| F_rot2 | 453 | T'=¬T; chair A when T=0, B when T=1; C copies the chair | AND of the other two | yes |
| F_rot3 | 453 | mod-3 clock on (T,U), phase p = T + 2U (state 11 read as phase 0), p' = p+1 mod 3; chair = party p | AND of the other two | yes |
| F4_fixed | 454 | A always; mod-4 clock on (T,U) runs but is unread (control) | B∧C∧D | yes (H6) |
| F4_rot | 454 | mod-4 clock on (T,U), chair = party p | AND of the other three | yes (H6) |
| F_rot3_OR / F_rot3_XOR | 455 | as F_rot3 | OR / XOR of the other two | yes (H7) |
| F_earned3 | 455 | endogenous: p' = p if the chair is inactive, else p+1 mod 3 | AND | yes (H8) |
| F_earned3_XOR | 455 | endogenous, as F_earned3 | XOR | added with probe 455 alongside H8; not named in H8 |

Controls: the fixed-chair forms (with an idle or unread clock) are the baselines for every rotating form at the
same party count.

## Measures and decision rules
- **H1** (pre-specified): whole-system structure == triadic for rotating forms.
- **H2** (pre-specified): clock bit(s) in the peak core for rotating forms and not for F_fixed.
- **H3** (pre-specified): veto set over parties {A} for F_fixed and containing no party for rotating forms.
  As implemented in probes 453–455, coalitions included clock nodes and the veto was the intersection of
  integrating coalitions with φ_s > 0 at any reachable state (`phi_s_maxstate`).
- **H4** (pre-specified): whole-system max Φ(F_rot2) ≥ max Φ(F_fixed).
- **H5** (pre-specified): {A,B,C} ⊆ peak core of F_rot3.
- **H6** (pre-specified before 454): no party in the veto set of F4_rot; veto set {A} for F4_fixed.
- **H7** (pre-specified before 455): no party veto and {A,B,C} ⊆ peak core for OR and XOR rotation.
- **H8** (pre-specified before 455): for F_earned3, a clock bit in the peak core and whole-system triadic.

## Probe 456 — per-state, party-only audit (added after review; not pre-specified)
For every reachable state of all nine forms: the maximal complex and its Φ; party-only coalitions (subsets of
the parties of size ≥ 2) with φ_s > 0 at that state; their intersection (per-state party veto). The
cross-state party veto is the intersection of per-state veto sets over states that have at least one
integrating party coalition; states with none are excluded. State coverage is the number of distinct
reachable states whose maximal complex is exactly the party set, divided by the number of reachable states,
counted uniformly. It is not weighted by trajectory and does not measure temporal persistence.

## Commands (from the repo root, venv active, `PYPHI_WELCOME_OFF=true`)
```bash
python -m org_frontier.classifier.validate
python -m org_frontier.questions.q217_rotating_chair.probe_453_rotating_chair
python -m org_frontier.questions.q217_rotating_chair.probe_454_rotating_chair_n4
python -m org_frontier.questions.q217_rotating_chair.probe_455_rotating_chair_ext
python -m org_frontier.questions.q217_rotating_chair.probe_456_per_state_veto
python ci/reproduce.py q217-rotating-chair q217-rotating-chair-n4 q217-per-state-veto
```
Saved outputs: `run_453.txt`, `run_454.txt`, `run_455.txt`, `run_456.txt`.
