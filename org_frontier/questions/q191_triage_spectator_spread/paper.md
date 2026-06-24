# q191 — Φ spread between an agent's party account and a system's spectator account of a triage

A customer-service agent and the system that routes the work describe the same triage two ways. The
agent counts the supervisor who watches the queue as a party to the coordination: someone the work
answers to. The system counts that supervisor as a read-only spectator: a dashboard, present but
inert. Qualitative research treats that gap as data. This study scores the gap with the q183
disagreement-Φ bridge, on synthetic rule sets that encode each account.

The accounts run over labels `(A, C, S)` = (Agent, Customer, Supervisor). The live coordination is
the Agent-Customer dyad, and the supervisor monitors it: the supervisor reads the Agent and the
Customer. The premise of the control is that the supervisor reads but is read by no node. Under
that premise neither account can wire an edge into the supervisor, so both accounts share one
wiring `[x1, x0, x0&x1]` and differ only in whether they name the supervisor a party. The wiring
reads dyadic with Φ_MIP = 0, and its integrated core is `{A, C}`. The supervisor, a sink, is out.

The bridge returns zero spread on this pair: verdict_agreement = 1, phi_gap = 0.0, core_jaccard =
1.0. An unread node carries no integrated information, so it cannot sit in any major-complex core.
Calling it a party and calling it a spectator describe the same causal structure, and Φ reads
structure. The membership disagreement leaves no trace. H1 holds.

The back-edge variant wires one inbound edge: the Customer node now reads the supervisor. That
single edge moves the supervisor from a sink to a read party. The faithful-triad shape binds all
three, and both accounts adopt the conceded edge. The pair reads triadic with Φ_MIP = 2.0, the
core is `{A, C, S}`, and the supervisor sits inside it for both accounts. verdict_agreement = 1 and
core_jaccard = 1. H2 is confirmed.

The two results read together give a clean rule. What separates a party from a spectator, for Φ, is
not the membership claim but the wiring: a party is read by some node, a spectator is read by none.
The disagreement about the supervisor is invisible to whole-system Φ exactly when the supervisor is
unread, and it resolves the moment one back-edge makes the supervisor read. The bridge locates the
disagreement in one edge.

The accounts are synthetic, coder-supplied rule sets, not measured agent, customer, or supervisor
states. The empirical arms are on synthetic data. The construct is divergence between two stated
accounts of one triage. The gap between a coded account and an observed triage stays open; later
studies in this line apply the bridge across more settings.
