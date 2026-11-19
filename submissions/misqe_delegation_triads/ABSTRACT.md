# Abstract: *MISQE* special issue on delegating work to AI agents (Insight format proposed)

[DRAFTED by Claude, 26 Oct 2026. For the author's read-aloud. Full paper due 1 Mar 2027. **MISQE requires evidence (FLAGS 1).**]

[Revised by Claude, 27 Oct 2026, against the CFP: the practices are framed as intervention mechanisms for agents acting with limited supervision, the call's first theme. See `../CFP_FIT_REVIEW_2026-10-27.md`.]

**Title:** When Your AI Agent Is Also Your Counterpart's: Managing Delegation That Creates a Third Party

## Abstract
Managers delegate work to AI agents as if they were hiring an assistant: the manager directs, the agent executes, and oversight catches errors. That picture holds while the agent's work stays with the person who delegated it. It breaks when the output crosses to someone else. A developer's coding agent produces changes a reviewer must approve. A sales team's agent drafts messages a customer answers through the same system. A manager's agent summarizes work that the employee will see and dispute. In each case the agent stands between two people, and its rules govern both. Those rules include when it asks, when it proceeds alone, and which decisions it shows, and the vendor, not either person, sets and changes them. Using the product documentation and release notes of a widely used coding agent, we show how such rules shift between releases. Settings that keep the agent working without stopping for clarifying questions, and questions that time out so the agent proceeds on its own judgement, change where the human decision points fall. We draw three management practices from this, each an intervention point for an agent that acts with limited supervision. Decide whose rules govern the agent when its output reaches another person. Decide who sees which outputs and decision points. Monitor vendor changes to the agent's behaviour as you would monitor a policy change. A one-page checklist turns each practice into questions a manager can ask before delegating.

**Keywords:** agentic AI; delegation; governance; third party; vendor change

## Citation check
| Claim | Source | Depth |
|---|---|---|
| The agent acts on one communicator's behalf; principal–agent analogy | `dxd_foundation/literature/library/hancock2020ai.md` (p. 4, advance access) | full text |
| Agents push humans out of the loop | `dxd_foundation/literature/library/mitchell2026agents.md` | full text (preprint) |
| "nudges Claude to keep working without stopping for clarifying questions" | `phd1750_spaces_in_stream/sec3/claudecode/permission-modes.md:335` | primary document |
| Unanswered questions time out and the agent proceeds | `phd1750_spaces_in_stream/sec3/claudecode/tools-reference.md:136` | primary document |
