# Q221 progress — exploratory feasibility record

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
- [x] Retrospective `paper.md`, `methods.md`, `hypotheses.md`, and `review.md` updated to distinguish executed evidence from unperformed confirmatory work.
- [x] Targeted prior-art and formalism-version notes added under `literature/`; exhaustive novelty certification is not claimed.
- [x] GitHub `reproduce-the-numbers` succeeded on head `28c89ca8` after generated directory repair; newer documentation commits require a fresh final-head check.
- [ ] PR body still stale: upstream GitHub PR metadata update returned HTTP 403 `Resource not accessible by integration`; no bypass attempted.
- [ ] Maintainer scientific review and merge decision remain external; PR stays draft.
- The phase-0 audit, prospectively locked CRQA-null pilot protocol, and confirmatory CRQA pilot were **not executed**. They are not necessary to present the narrower exploratory case study, and must not be implied complete. The independent Pearson null pilot is separate (`independent_audit/`).
