# q221 progress log (checkpoint; resume from the last unchecked step)

Worktree `/workspace/algorithmacy-q221`, branch `q221-temporal-null-calibration` off `upstream/contrib` 44f9b491.
Python: `/workspace/algorithmacy-827-venv/bin/python` (numpy 2.5.4, scipy 1.18.1).

- [x] 0. Setup: worktree, scaffold (`new_question --id 221`), plan moved to `design/FEASIBILITY_PLAN.md`, blueprint summary
- [~] 1. Phase 0 repo audit → `PHASE0_AUDIT.md`
- [~] 2. Prospective literature review → `literature/` (commit before any pilot code)
- [ ] 3. Pilot spec + null validity certificates → `PILOT_SPEC.md` (commit before pilot code)
- [ ] 4. Pilot code + tests, run via box-run
- [ ] 5. `PILOT_RESULTS.md` with GO/NO-GO
- [x] Identifiability priority (Hassan): A/B exact profiles, exact Φ (REJECTED: degenerate targets), CMI, isomorphism → `IDENTIFIABILITY_NOTE.md` (draft)
- [x] Bounded pair search (rule 3): completed 2823/2823 in 290 s → `identifiability/SEARCH_RECORD.md`
- [x] Adjudication + stricter exact screen (7488 → 180 raw / 3 unique survivors) → `results/screen_exact.txt`
- [x] Lead pair P/Q: exact Φ (pinned), profiles to lag 40, Hassan's finite-sample script (pinned)
- [x] A/B/C reconciliation (`variants_abc.py`); pinned-env rerun of Hassan's modules (bit-identical; 4/4 tests)
- [x] FINDINGS.md (narrowed scope)
- STOPPED here per Hassan's finish line. Not done (deferred to any future study): Phase 0 audit write-up, pilot spec,
  CRQA-statistic pilot, PILOT_RESULTS.md. The exploratory null pilot is Hassan's (`independent_audit/`).
