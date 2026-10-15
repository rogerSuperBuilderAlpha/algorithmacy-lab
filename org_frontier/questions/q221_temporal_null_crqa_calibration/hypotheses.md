# Q221: prespecified rules (in place of Stage-3 hypotheses H1–H5)

Q221 did **not** fix five Stage-3 hypotheses. It is a draft feasibility and methods record, not a completed
question. The rules fixed before computation are:

- `EXACT_PHI_DECISION_RULES.md`: Hassan's 13 exact-Φ gate rules, committed in `82b3d80c` before the
  post-rules Φ runs and the bounded search. The chronology, including a quarantined pre-rules run, is
  disclosed in that file.
- `identifiability/baselines_survivors.py` docstring: the gate-3 baseline specification, with expected
  outcomes, committed in `35313d47` before that run.
- `BLUEPRINT_REQUIREMENTS.md`: the study requirements any confirmatory phase must meet.

Any confirmatory study must fix its hypotheses and nulls in a preregistration that is committed and pushed
before data collection (`FINDINGS.md`, "Future confirmatory work").
