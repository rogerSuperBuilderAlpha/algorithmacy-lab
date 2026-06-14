# Q68 — Stage 1 review: a recipient-side triage agent

## The question

A recipient increasingly runs an agent that triages incoming messages, gating whether a sender's message
reaches the human. This study asks whether that triage agent is part of the irreducible coordination, and
what its membership depends on. Parties: sender intent (E), the message/system (M), recipient (R), and a
triage agent (T) on the recipient side. Is T in the major complex, and does it matter whether T only
gates delivery, only monitors, or both reads the message and gates delivery?

## What the lab already knows that bears on this

- **Core membership needs bidirectional constraining coupling (STRUCTURAL_FINDINGS #8, principal/gating).**
  A principal joins the major complex iff the coupling is bidirectional: the system reads it (gating) and
  it reads a party. Gating-only or monitoring-only leaves the principal outside the core. The triage agent
  is a recipient-side principal, so the same condition should decide its membership.
- **The single-mediator outreach triad is triadic (Q63, probes 215-219).** The base E-M-R coordination is
  triadic at Φ = 2.0; adding a triage agent should not break it, and the verdict is read on the major
  complex when there are spectators.
- **Read-only sinks and emit-only sources stay out of the core (probe loop).** A monitoring-only triage
  (reads but affects nothing) and a gating-only triage (affects but reads nothing) should both stay out.

## The gap

The lab has the principal/gating finding for a corporate principal but has not built the recipient-side
triage agent and tested its core membership under gating-only, monitoring-only, and bidirectional
coupling. No prior probe answers whether a triage agent joins the irreducible coordination, so the
question is open.
