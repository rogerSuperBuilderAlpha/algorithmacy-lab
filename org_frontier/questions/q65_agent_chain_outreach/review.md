# Q65 — Stage 1 review: agent-to-agent outreach (depth)

## The question

Outreach increasingly runs agent to agent: a sender's agent prepares a message that a recipient's agent
receives and triages before any human reads it. This is a chain of mediators between the two humans:
E (sender intent) → A1 → A2 → … → Ad → R (recipient). Q63 and Q64 covered one mediator and the breadth
of recipients under one agent. This study covers depth: as agents are chained between sender and
recipient, does the coordination stay triadic, and does the verdict survive the chain lengthening?

## What the lab already knows that bears on this

- **Depth preserves irreducibility (Finding 6, `multiparty/chains.py`).** A mediation chain
  W → S1 → … → Sk → C, where each mediator commits jointly from its two neighbours (Sj' = S_{j-1} ∧
  S_{j+1}), stays triadic at Φ = 2.0 at every length tested (n = 3–6). An agent chain in outreach is this
  structure relabelled, so it should stay triadic at every depth.
- **Breadth and depth act independently (Finding 6).** Adding parties (breadth) dilutes the random
  triadic rate to zero, while adding mediation depth does not, and the two do not undo each other. A chain
  feeding a multi-recipient commit should stay triadic.
- **Joint determination is the condition (Findings 1–3).** Each mediator must read all its sources. An
  agent that relays only its upstream neighbour, ignoring the downstream one, breaks the joint
  determination, so the chain should collapse where the relay gap sits.
- **Breadth grows Φ as n−1 (Q64); depth holds Φ constant (the chain result).** The two axes scale Φ
  differently, which this study contrasts directly.

## The gap

The lab has the abstract mediation-chain result but has not built the agent-to-agent outreach forms,
contrasted depth against Q64's breadth, tested a relay-gap agent, or combined depth with breadth in the
outreach frame. No prior probe answers whether agent-to-agent outreach stays triadic as the agent chain
lengthens, so the question is open.
