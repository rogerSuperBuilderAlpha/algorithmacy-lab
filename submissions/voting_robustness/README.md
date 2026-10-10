# Voting/Quorum Robustness to Temporal Grain and Update Schedule

**Probe 462** — Extends Probes 32/62 (grain/schedule relativity) to the voting/quorum rule set (Probes 67, 122, 457).

## Status
- ✅ Probe implemented and CI-gated (`probe-voting-robustness`)
- ✅ Hypotheses fixed before computing (in probe docstring)
- ✅ Paper written (`paper.md`)
- ✅ Findings documented (`FINDINGS.md`)
- ✅ PR submitted to `contrib`

## Key Finding
The voting/quorum structural law ("only extreme thresholds bind the full core") holds **only at synchronous 1-step grain**. At 2-step grain and under sequential update, **all rules collapse to dyadic Φ=0** — including the extreme AND/OR rules. No voting rule is robust. At 3-step grain, AND/OR/parity recover triadic verdicts; majority/weighted do not.

## Files
- `paper.md` — Full paper
- `FINDINGS.md` — Summary of results
- `../org_frontier/probes/probe_voting_robustness.py` — Probe implementation (Probe 462)
- `../ci/reproduce.json` — CI check `probe-voting-robustness`

## Run
```bash
python -m org_frontier.probes.probe_voting_robustness
python ci/reproduce.py probe-voting-robustness
```