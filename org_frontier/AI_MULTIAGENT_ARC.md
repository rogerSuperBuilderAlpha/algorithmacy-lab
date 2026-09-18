# AI / multi-agent arc — #37–#41 synthesis

Exact binary IIT-4.0 Φ; in-silico Boolean / tabular / small neural
proxies (not live LLM calls; not MAPPO/QMIX unless a named follow-up).
Formal / stoch–temporal / estimation / construct-omit stay closed
except as pointers (COMMIT_READ, #69, #98/#107).

## Lane status: **CLOSABLE** (deep gap filled)

| # | study | verdict | one line |
|---|---|---|---|
| 37 | [`agent_protocol_triad/`](studies/agent_protocol_triad/) | **PROTOCOL_IS_COMMIT** | Protocol joins iff joint commit + read; no human required |
| 38 | [`agent_tool_core/`](studies/agent_tool_core/) | **TOOL_LIKE_INFERENCE** | Tool joins like #4/#9 blend; unused out; displaces C |
| 39 | [`hitl_rubber_stamp/`](studies/hitl_rubber_stamp/) | **HUMAN_COMMIT_READ** | HITL human in iff COMMIT_READ; stamps out |
| 40 | [`ai_fidelity_displace/`](studies/ai_fidelity_displace/) | **SHARP_FULL_DISPLACE** | Policy-model displaces C only at full fidelity |
| 41 | [`marl_emergent_learn/`](studies/marl_emergent_learn/) | **EMERGENT_NULL** | Emergent verdict ̸↔ learnability (tabular) |
| gap | [`marl_deep_replicate/`](studies/marl_deep_replicate/) | **NULL_SURVIVES** | Neural/FA + larger obs: null holds |

## What the lane shows

1. **Membership cuts transfer.** Protocol nodes, tools, and HITL
   humans enter the major complex by the same bidirectional
   constraining pattern (commit/act + read), not by label. Rubber
   stamps, unused tools, and conveyors stay out.
2. **Displacement is sharp.** Learned / inferred stand-ins for the
   counterpart join and eject C at a discrete fidelity threshold, not
   by a smooth Φ glide (#40 / #69).
3. **Structure ≠ learnability.** Designed (#98/#107), tabular emergent
   (#41), and **neural/FA emergent** (`marl_deep_replicate`) verdicts
   all fail to predict whether independent learners solve the commit.
   Open-loop success is the recurring witness.

## Exact limits

- In-silico Boolean abstractions; tabular Q and small NumPy MLP/linear
  FA — not production multi-agent RL, not field orgs, not
  consciousness claims.
- Association only; no causal identification.
- Optional curiosity only (not a lane blocker): MAPPO/QMIX or
  continuous-obs deep MARL.

## Reproduce

```
python org_frontier/studies/agent_protocol_triad/analyze_protocols.py
python org_frontier/studies/agent_tool_core/analyze_tools.py
python org_frontier/studies/hitl_rubber_stamp/analyze_hitl.py
python org_frontier/studies/ai_fidelity_displace/analyze_fidelity.py
python org_frontier/studies/marl_emergent_learn/analyze_marl.py
python org_frontier/studies/marl_deep_replicate/analyze_deep.py
```
