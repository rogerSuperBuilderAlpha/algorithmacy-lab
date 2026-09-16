# Agent protocol triad — findings

**Verdict: PROTOCOL_IS_COMMIT.** Protocol design sets dyadic vs triadic
the same way the commit does (COMMIT_READ / probe #88): conveyors and
read-without-commit stay out; full joint-commit protocols with both
agents determining and reading P are **protocol-triadic** with P in the
core. A negotiation protocol **can** be triadic without a human —
joint AND/OR/NAND/XOR on (A,P,B) match the classical (W,S,C) cut.

In-silico; candid N (designed Boolean panel). Hypotheses fixed in
`hypotheses.md`. Cited: #88/#50; `hmc_algo_boundary`; encoding ladders
as pointers. Formal / stoch–temporal / estimation / construct-omit
closed.

## Hypotheses

| H | result |
|---|---|
| H1 protocol encoding flips like commit | **SUPPORTED** |
| H2 always dyadic without human | **REFUTED** |
| H3 some protocols triadic with only A+P+B | **SUPPORTED** |

## Panel (no-human unless noted)

| form | whole | Φ | core | protocol-triadic |
|---|---|---:|---|:---:|
| relay / broadcast | dyadic | — | singleton | no |
| read_not_in_commit | dyadic | 2 | {A,P} | no |
| side_channel / blackboard / turn_token | dyadic | — | ≤2 | no |
| joint_AND / OR / NAND | triadic | 2 | {A,P,B} | **YES** |
| joint_XOR | triadic | 0.5 | {A,P,B} | **YES** |
| offer_accept | triadic† | 2 | {P,B} | no |
| classical_WSC | triadic | 2 | {W,S,C} | **YES** (= joint_AND) |

† Whole-triadic with incomplete core — not protocol-triadic.

## Reading

LLM-style agents do not need a human in the loop for triadicity. They
need a **committing protocol**: both agents feed P and both read P.
Relay, broadcast, side-channel, and schedule-only tokens are conveyors.
Asymmetric “offer/accept” morphs can look whole-triadic while dropping
an agent from the major complex — the COMMIT_READ test is the right
filter. Classical human joint commit is the same Boolean object under
relabeling.

## Limits

Boolean abstractions of protocol design; n=3; no live LLM calls; no
organization measured.

## Best next

**#38** — tool-in-core (does a tool an agent calls join the core when
the agent acts on its output, like inference #4/#9)? Alternate: **#39**
HITL rubber-stamp.

## Reproduce

```
python org_frontier/studies/agent_protocol_triad/analyze_protocols.py
```
(~2 s)
