# WHO BROKE PROD? × Φ — hypotheses (fixed before computing)

**Question.** Do exact IIT-4.0 readings of small Boolean forms of four incident-coordination steps (flat
reporting, hub forwarding, chain relay, deciding-mediator joint commit) correspond to investigative
accuracy measured in a matched run of the incident simulator?

**Already known (cited, not reopened).**
- Probe #88 (`probes/probe_mas.py`): relay and broadcast protocols are dyadic; joint commit
  `P'=A1∧A2` read by both agents is triadic, Φ=2.0, core {A1,P,A2}.
- `agent_protocol_triad/` (#37): PROTOCOL_IS_COMMIT. `hitl_rubber_stamp/` (#39): HUMAN_COMMIT_READ.
- `marl_emergent_learn/` (#41), #98, #107: designed and emergent verdicts do not predict learnability
  (nulls). Structure has not been shown to predict behavioural performance in this lab.
- `who_broke_prod/`: the preregistered 2400-run simulator study (flat, hub, chain). Its runs are not
  reused as evidence for any hypothesis here; they serve only as the docking check below.

**Universe / honesty.** Exact binary IIT-4.0 Φ on 3–4 node designed forms. The mapping from a
simulator topology to a Boolean form is an encoding choice, stated in full below. Association across
four designed conditions only; no causal claim. The simulator condition `hub_commit` is designed here,
by the same author who has seen the earlier study's results, before it has ever been run.

## Forms (rules little-endian; `x[i]` is node i's current bit)

| form | labels | rules | simulator condition |
|---|---|---|---|
| flat_report | (A1, A2, I) | A1'=A1, A2'=A2, I'=A1∨A2 | flat |
| hub_forward | (A1, M, A2, I) | A1'=A1, M'=A1∨A2, A2'=A2, I'=M | hub |
| chain_relay | (A1, A2, A3, I) | A1'=A1, A2'=A1, A3'=A2, I'=A3 | chain |
| hub_commit | (A1, M, A2, I) | A1'=M, M'=A1∧A2, A2'=M, I'=M | hub_commit |

Instrument controls, run first: probe #88's `joint_commit` (A1'=P, P'=A1∧A2, A2'=P) must read triadic
with Φ=2.0, and its `relay` (A1'=A1, P'=A1, A2'=P) must read dyadic.

**Measures.** Whole-system verdict and Φ_MIP (`verdict`), major complex and its Φ (`major_complex`).
**Integrated coordination core (primary binary reading):** the major complex has ≥3 nodes, includes at
least two agent nodes, and has Φ>0.

## Matched simulator condition `hub_commit` (fixed before running)

Agents report to a mediator M in round 1. Each round r=1..5, M holds every claim received so far; with
trace access it verifies one cited, unchecked claim per round (most repeated first; same rule as the
investigator) and commits an attribution by the investigator's rule over its claims. M broadcasts the
commitment to the agents (the read). In round r+1 every agent whose original stance is `witness` and
whose accused differs from M's round-r commitment re-sends its claim to M (one repeat per round). M
forwards to the investigator, in round r+1, each claim received in round r that it has not refuted. The
investigator, scoring, seeds (0..49), scenarios (4), incentives, access levels, budgets and deadline (5)
are unchanged from `who_broke_prod`. Grid: 4 topologies × 4 scenarios × 50 seeds × 2 incentives × 2
access = 3200 runs, written to `results/runs.csv`. The flat, hub and chain rows are a new run of the
vendored simulator, not copies.

**Docking gate.** The vendored flat/hub/chain code must reproduce all 2400 rows of
`../who_broke_prod/results/runs.csv` exactly. If it does not, no hypothesis is evaluated.

## H1 — non-commit forms have no integrated coordination core
- **Claim:** flat_report, hub_forward and chain_relay each read whole-system dyadic and have no
  integrated coordination core.
- **H0:** any of the three reads triadic or has an integrated coordination core.

## H2 — the commit form is integrated, with the investigator outside the core
- **Claim:** hub_commit has major complex exactly {A1, M, A2} with Φ = 2.0; its whole-system verdict
  is dyadic, because I only reads M.
- **H0:** a different core, a different Φ, or a triadic whole-system verdict.

## H3 — Φ structure corresponds to accuracy (self-protective agents, full access)
- **Claim:** accuracy(hub_commit) − max accuracy over the topologies without an integrated core ≥ 0.05,
  and the paired two-sided exact sign test against that best topology gives p < 0.01.
- **H0:** difference < 0.05 or p ≥ 0.01.

## H4 — same correspondence without trace access (self-protective, claims only)
- **Claim and decision rule:** as H3, in the claims-only cells.
- **H0:** as H3.

## H5 — commit versus convey at the hub (self-protective, full access)
- **Claim:** accuracy(hub_commit) − accuracy(hub) ≥ 0.05, paired sign test p < 0.01.
- **H0:** difference < 0.05 or p ≥ 0.01.

## H6 — ceiling control (neutral incentive)
- **Claim:** every topology reaches accuracy ≥ 0.99 under the neutral incentive at both access
  levels, so structure cannot separate the conditions there.
- **H0:** some topology falls below 0.99.

## Interpretation rule (fixed)

A supported H3/H4/H5 is reported as an association across four designed conditions. The simulator's
`hub_commit` mechanism and the Boolean form encode the same commit-and-read design, so a match is not
independent evidence that Φ causes or predicts investigative performance. Evidence about the model, not
about a real organization.
