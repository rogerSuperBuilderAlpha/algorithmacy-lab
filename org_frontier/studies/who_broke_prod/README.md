# WHO BROKE PROD? — incident attribution under coordination topologies

A deterministic simulation of multi-agent incident investigation. Five rule-based agents report who
caused a simulated outage; under a self-protective incentive the culprit deflects and bystanders
scapegoat. An investigator attributes the root cause from the claims and, when allowed, by checking cited
events against the ground-truth trace. This study packages one preregistered run of that simulator.

| file | role |
|---|---|
| `hypotheses.md` | H1–H6, verbatim from the prototype's preregistration (committed before the run) |
| `analyze_who_broke_prod.py` | recomputes every reported metric and decision from `results/runs.csv` |
| `results/runs.csv` | the 2400 saved runs (4 scenarios × 50 seeds × 3 topologies × 2 incentives × 2 access) |
| `FINDINGS.md` | H1–H6 verdicts, numbers, and the simulator mechanisms behind them |

```
python org_frontier/studies/who_broke_prod/analyze_who_broke_prod.py
```
(standard library only, under a second)

## Scope

Evidence about the model, not about a real organization. The simulator is a designed abstraction:
scripted agents, four hand-built scenarios, fixed parameters. No Φ is computed in this study and no
relationship between Φ and attribution accuracy is claimed. The study sits beside the lab's
AI / multi-agent arc (`AI_MULTIAGENT_ARC.md`, probe #88 `probes/probe_mas.py`, `agent_protocol_triad/`)
as a behavioural companion only; connecting it to exact Φ would be a separate, separately
preregistered study.

## Provenance

The simulator source is not vendored. It lives in the prototype repository
[Adhithyan245/who-broke-prod](https://github.com/Adhithyan245/who-broke-prod) (`whobrokeprod/` package; commits [`97dc432`](https://github.com/Adhithyan245/who-broke-prod/commit/97dc432d9e238fe63622b1ab5393f975780e8ce3) hypotheses,
[`b08a2c3`](https://github.com/Adhithyan245/who-broke-prod/commit/b08a2c34e74d0b956f70d5735ab0bf2983824be2) code, [`61ad8b0`](https://github.com/Adhithyan245/who-broke-prod/commit/61ad8b0a43528bb79a2085b042400784e19577a8) results, 2026-10-09; history published unmodified, including its
placeholder commit author). This directory reproduces every reported number from the saved run; regenerating
the run itself requires that prototype. Interactive demo of the simulator: <https://adhithyan245.github.io/who-broke-prod-demo/>.
