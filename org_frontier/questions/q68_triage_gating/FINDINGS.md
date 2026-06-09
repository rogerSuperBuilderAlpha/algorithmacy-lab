# Q68 findings — a recipient-side triage agent

All four hypotheses confirmed. Instrument control passed (dyadic relay Φ=0.000, triad Φ=0.830).

| H | Test | Result | Verdict |
|---|------|--------|---------|
| H1 | monitoring-only triage | core {E,M,R}, T excluded, Φ=2.0 | confirmed |
| H2 | gating-only triage | core {E,M,R}, T excluded, Φ=2.0 | confirmed |
| H3 | bidirectional triage | core {M,R,T}, T included, Φ=2.0 | confirmed |
| H4 | base coordination | triadic (Φ=2.0) in all three configs | confirmed |

All from `probe_triage_gating.py`.

## What it says

A recipient-side triage agent is part of the irreducible coordination only when it is bidirectionally
coupled. A triage agent that only monitors the message, or only gates delivery without reading, stays out
of the major complex; the core remains the sender-message-recipient triad. A triage agent that both reads
the message and gates delivery joins the core. This confirms the bidirectional core-membership condition
in the triage frame: gating alone or monitoring alone is not enough.

The bidirectional case carries a further result. When the triage agent joins, the major complex becomes
{M, R, T}, and the sender E drops out. A bidirectionally-coupled recipient-side gatekeeper does not merely
add itself to the coordination; it displaces the sender from the irreducible core, the same contraction
the program found when a heavily-coupled principal displaces the parties it sits among. The core stays
size three and triadic at Φ = 2.0; its membership shifts from the sender end to the triage agent.

## Caveats

- **Whole-system vs core.** The verdicts are read on the major complex. The monitoring-only and
  gating-only forms are whole-system dyadic (Φ_MIP=0): T hangs off as a read-only or emit-only spectator,
  and only the {E,M,R} complex inside is triadic. The bidirectional form's whole-system Φ is also below
  its major-complex Φ=2.0. Reading the core is the right call when there are spectators; the whole-system
  numbers are noted here for completeness.
- **Confirmatory.** The four predictions followed from the principal/gating finding applied to triage;
  none was refuted. The displacement of the sender is the notable detail.
- **In-silico.** Boolean models, evidence about the models. Φ read ordinally.
- **One triage topology.** The triage agent gates a single recipient over the base read-recipient triad;
  multi-recipient or chained triage is untested.
