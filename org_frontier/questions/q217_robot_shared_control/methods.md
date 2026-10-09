# Methods — q217 robot shared control

- Three nodes, one bit each: Human operator `H` (x[0]), Autopilot / safety controller `P` (x[1]), Robot `R` (x[2]).
  A bit of 1 means "commanding / approving / moving".
- Four deterministic Boolean update rules (see `hypotheses.md`), one per control design. No rule was changed;
  none of the models was degenerate.
- Instrument control first: `python -m org_frontier.classifier.validate` must print `Instrument validated`.
- Script `probe_robot_shared_control.py` computes, for each model, the whole-system verdict
  (`org_frontier.probes.lib.verdict`, exact IIT-4.0 Φ over the minimum-information partition, PHI_EPS = 1e-9)
  and the major complex (`major_complex`, max over reachable states). Output is saved verbatim in `results.txt`.
