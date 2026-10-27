# Argument: delegation that creates a third party

[DRAFTED by Claude, 26 Oct 2026.]

**P1.** Delegating work to an AI agent is usually framed as a principal–agent relation: the delegator directs, the agent executes, and oversight closes the gap. In AI-mediated communication, the agent acts on behalf of one communicator.
- *Sources:* `dxd_foundation/literature/library/hancock2020ai.md` (autonomy dimension "similar to the principal–agent relationship", p. 4, advance-access pagination); `dxd_foundation/literature/library/mitchell2026agents.md` (approval fatigue; humans pushed out of the loop).

**P2.** When the agent's output reaches a second person (a reviewer, a customer or a colleague), and that person also acts on or through the same agent, the agent stops being only the delegator's agent. It becomes a third party whose rules both people face, and the vendor sets and changes those rules. Agent products already change how often they ask, when they proceed alone, and which decisions they surface.
- *Sources (primary product documentation, quoted with line numbers in `../phd1750_spaces_in_stream/sec3/claudecode/`):*
  - `permission-modes.md:335`: auto mode "nudges Claude to keep working without stopping for clarifying questions"
  - `tools-reference.md:136`: an unanswered question times out and Claude "proceeds on its own judgment"
  - `CHANGELOG.md:8561`: "Claude will now ask you questions more often in plan mode"

**C.** Managers delegating to AI agents should treat delegation as creating a triad when outputs cross to another person. They need three practices: decide whose rules govern the agent, decide who sees which outputs and decision points, and detect when the vendor changes the agent's behaviour. They also need a practitioner checklist for each.
