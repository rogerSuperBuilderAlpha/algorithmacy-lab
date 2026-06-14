# Agenda: continuing the program (Q74+)

Runnable next questions derived from the path forward in `RESEARCH_NARRATIVE.md`, ordered by priority.
Each states the question, the machinery to reuse, and the discriminator that would settle it. Entries
marked **(design)** need a tool or data the lab does not yet have and are stated as plans, not yet
computable. The rest run through the six-stage protocol (`protocol/RESEARCH_PROTOCOL.md`) like Q63–Q73:
pre-register five (or fewer) hypotheses before computing, validate the instrument on a control, report
nulls.

## Priority 1 — Harden the construct: whole-system verdict vs. maximal complex

The review of Q63–Q73 found that the deepest results (Q65 localization, Q69 displacement) read on the
maximal complex in ways that can overclaim, because the whole-system verdict and the complex diverge.
These questions pin the boundary.

- **Q74 — When do the two readings diverge, and which is right?** Build a labelled set of forms where the
  whole-system Φ_MIP and the maximal-complex verdict disagree (the Q65 chain, the Q68/Q69 frozen-spectator
  forms, feed-forward relays). Characterise the divergence by structural cause: spectators, frozen
  source/sink nodes, feed-forward fan-out. Reuse `classifier.classify_rules` (whole-system) and
  `probes.lib.major_complex`. *Discriminator:* a stated rule for which reading to report, as a function of
  whether non-core elements are bidirectionally coupled — extending Finding 8.
- **Q75 — Spectator robustness of the core.** Add k genuine spectators (idle, uncoupled parties) to the
  read-recipient triad and confirm the maximal complex stays {E, M, R} at Φ = 2.0 for k = 1..3. *Discriminator:*
  if a spectator ever joins the core, the major-complex reading is unstable and the whole-system verdict
  should govern.

## Priority 2 — Cross the validation gap (design)

The single largest gap: no result touches data. These are the cheapest anchors.

- **Q76 (design) — Behavioural test of the outreach verdict.** Re-run the dissertation's agent-based
  coordination experiment on the Q63 outreach forms: does coordinating through a triadic (Φ > 0) form
  produce a measurable difficulty gap over a dyadic one, after practice? *What is missing:* the
  behavioural harness wired to the outreach forms, and (for human subjects) ethics approval. *Discriminator:*
  a difficulty gap that tracks the verdict, not the party count.
- **Q77 (design) — Proxy against ground truth on real logs.** On real interaction or outreach logs,
  estimate a cheap proxy on the small coordination units and compare to the exact-Φ verdict computed on
  the same units. *What is missing:* a dataset of logged multi-party interactions with identifiable units.
  *Discriminator:* whether any cheap estimate tracks the exact verdict on real data, where Finding 7 and
  Q72 say it should not.

## Priority 3 — Richer state

- **Q78 (design) — Multivalued outreach.** Lift the read-recipient triad to ternary parties (a worker
  idle, engaged, or overcommitted) and recompute the verdict. *What is missing:* multivalued IIT; the
  installed PyPhi is the binary IIT-4.0 branch. *Discriminator:* whether the dyadic/triadic verdict
  survives graded states or whether graded states create partial irreducibility the binary cut hides.
- **Q79 — Stochastic determination threshold.** Make the agent's commit probabilistic: M reads the
  recipient with probability p, ignores it with 1−p. Sweep p and find where the triad emerges. Reuse
  `probes.lib.max_phi_float` on a stochastic TPM, as in Q71. *Discriminator:* a continuous emergence of
  Φ with p, or a threshold.
- **Q80 — Asynchronous update.** The program updates synchronously. Recompute the keystone forms under
  asynchronous or mixed update and test whether the verdict survives. *Discriminator:* whether
  synchronicity is load-bearing for the outreach law.

## Priority 4 — The estimation frontier (done)

- **Q81 — Learned surrogate for the outreach verdict.** *Done.* A random forest over ten size-invariant
  cheap features recovers the verdict perfectly in-distribution on the 256-form n=3 family (CV ROC-AUC
  1.000) and fails to generalize to held-out n=4,5,6 forms (accuracy 0.250, below chance). The exact-Φ
  size ceiling holds for a learned student; the estimation route past it does not. See
  `questions/q81_learned_surrogate/`.
- **Q82 — Surrogate vs. cheap proxy.** *Done.* The surrogate beats every single proxy on the n=3 family
  (CV AUC 1.000 vs edges 0.966, in-degree 0.707, Φ_R 0.621, Φ_WMS 0.547) and separates the verdict
  perfectly on the constant-in-degree collision subset. Total edge count is a stronger single rank than
  expected but an imperfect separator. See `questions/q82_surrogate_vs_proxy/`.

## Priority 5 — Multi-agent extensions

- **Q83 — Agent coalition core.** Two recipient-side agents that jointly gate delivery: do they form a
  coalition in the core, as the regulator-coalition probe found for oversight (Probe 111)? Reuse the
  Q68 triage machinery with two gating agents. *Discriminator:* whether both agents enter the major complex
  only when jointly required.
- **Q84 — Adversarial agent.** An agent positioned to stay out of the core (read-only) that nonetheless
  tries to move the verdict. *Discriminator:* whether a non-core agent can flip the dyadic/triadic verdict
  without joining the core, or whether influence requires membership.
- **Q85 — Market of interchangeable agents.** N interchangeable agents on one side, with the recipient
  routing through any one. Extend Q70 to larger N and ask whether the coordination ever stabilises as
  triadic, or whether interchangeability collapses it at every N. *Discriminator:* the breadth-dilution
  pattern (Finding 6) in the agent-market frame.

## Priority 6 — The organization-theory bridge (design)

- **Q86 (design) — Map the outreach law onto the platform-as-form claim.** Connect the five-pillar law to
  the dissertation's literacy/algorithmacy construct and to the account of the platform as a third
  coordination mechanism alongside market and hierarchy. *What is missing:* the formal correspondence
  between the structural pillars and the organizational constructs, written as a paper rather than computed.

## Sequencing

Q74–Q75 first (cheap, computational, hardens the foundation). Then Q79–Q85 as the computable backlog,
interleaving the estimation-frontier work (Q81–Q82) with the multi-agent extensions (Q83–Q85). Q76–Q78
and Q86 wait on a tool, a dataset, or a written correspondence, and are staged so the work is ready when
the anchor exists.

The computable backlog through Q85 is done. A second wave of ten gaps (Q89–Q98) is staged in
[`RESEARCH_AGENDA_Q89.md`](RESEARCH_AGENDA_Q89.md): size-generalization of the laws, a fragility metric,
heterogeneous agents, multiple complexes, composition, degraded reads, memory, contingency, and
coordinated adversaries, all runnable on the existing instrument.
