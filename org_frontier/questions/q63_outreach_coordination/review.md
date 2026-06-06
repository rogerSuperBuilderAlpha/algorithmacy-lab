# Q63 — Stage 1 review: outreach as a coordination form

## The question

An autonomous agent prepares and sends a message on a sender's behalf. The sender, the agent, and the
recipient form a three-party arrangement. Is that arrangement triadic, so the agent jointly determines a
message from the sender's intent and a specific recipient's state and the coordination is irreducible, or
is it dyadic, so the agent broadcasts past the recipient and the form factors into a sender talking
through a passive channel? The design is in `designs/OUTREACH_COORDINATION.md`. This study computes the
verdict for the canonical outreach forms and tests four conditions the design predicts will move it.

The parties map to three elements: the sender's intent (E), the agent or mediator (M), the recipient (R).
The agent's commit is M's update rule. Strict mediation holds: E and R interact only through M.

## What the lab already knows that bears on this

- **A mediator that reads both outer parties is necessary, not sufficient (Findings 1–3).** Strict
  mediation alone leaves 90.6% of the n=3 family dyadic; Φ > 0 needs the mediator to jointly determine
  from all sources and the outer reads to keep each source live to the commit. Outreach inherits this:
  whether M reads R, and whether E and R stay live, should decide the verdict.
- **Substitutability of any role collapses the triad (Finding 5).** A counterpart bound through
  `W ∧ (C1 ∨ C2)` factors; only the all-required `W ∧ C1 ∧ C2` stays triadic (`multiparty/`). Mass
  outreach to interchangeable recipients is the same structure, so it should factor even when each
  message looks personalized.
- **The verdict lives in the cause-effect structure, not the label (q43, probes 135–139).** Thompson's
  interdependence labels did not predict the verdict; a directed cycle in the wiring was a different
  object from a closed loop in the causal structure. A disclosure flag is a label, so it should leave the
  verdict unchanged.
- **Cheap proxies do not recover the verdict (Finding 7).** A ΦID or whole-minus-sum proxy separates
  dyadic from triadic only near chance (rank-AUC ≤ 0.63; `proxy_bridge/`). A cost-like proxy for outreach
  should fail the same way, because a substitutable form can read many sources and still factor.
- **Liveness, not the bare presence of a back-channel, carries irreducibility (q49–q51).** The seam
  studies found a form is triadic only when each source stays live to the mediator's commit; a frozen or
  one-shot read drops it. One-shot outreach should factor; a form where the recipient's response stays
  live should not.

## The gap

The lab has the structural results above but has never built the outreach forms and read their verdicts
head to head. The mapping from "broadcast versus read-the-recipient," "substitutable recipients,"
"disclosure," "cost," and "reciprocity" onto the corpus has not been computed. No prior probe answers
whether agent-mediated outreach is triadic, so the question is open.
