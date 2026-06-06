# Outreach as a coordination form: design for a new experiment set

A discussion about agent-mediated outreach raised a question the lab's instrument can address. When an
autonomous agent prepares and sends a message on a sender's behalf, the sender, the agent, and the
recipient form a three-party arrangement. The question is whether that arrangement is triadic or dyadic.
It is triadic when the agent jointly determines a message from the sender's intent and a specific
recipient's state, so the coordination is irreducible and demands algorithmacy. It is dyadic when the
agent broadcasts past the recipient, so the form factors into a sender talking through a passive
channel. The same surface, an email arriving in an inbox, sits on top of both structures, so the
verdict cannot be read from the surface. This is the lab's standard question in a new application.

The motivating intuition was about cost and credibility: a message that cost the sender something, time
to write or compute to prepare, reads as more worth answering than a free mass-send. The structural
reframing is that the cost tracks whether the agent did the joint-determination work. A message tailored
to one recipient's state is a joint determination of two sources and costs the compute to read and fit.
A templated blast is a one-source broadcast and costs almost nothing. So the economic signal and the
structural verdict are predicted to move together, and exact Φ reads the structure directly.

## The mapping

Three parties as Boolean elements: the sender's intent (E), the agent or mediator (M), the recipient
(R). The agent commits a message as a determination from what it reads. The reads are the modeling
commitment, stated per experiment.

- **Dyadic (broadcast / spam).** M's commit is a function of E alone, or of a constant template, and it
  ignores R. The form factors along {E, M} | {R}: Φ_MIP = 0. Literacy suffices, because the recipient
  faces a medium.
- **Triadic (genuine agent-mediated coordination).** M's commit is a joint determination of E and R's
  state, and R's response stays live to M's commit. No party-respecting cut survives: Φ_MIP > 0.
  Algorithmacy is demanded, because two parties coordinate through an interpreting third.

This reuses the lab's established machinery: the classifier (`classifier/`), the broadcast and
substitutability forms (`multiparty/`, `corpus/`), the label-versus-structure result (q43), and the
proxy bridge (`proxy_bridge/`). No new tooling is required.

## The experiments

Each is a matched comparison at fixed size and rule family, with the instrument validated on its control
first. The hypotheses here are candidates, to be pre-registered before computing when the set enters the
protocol as a question.

### E1 — Broadcast versus read-the-recipient

Question. Does an agent that reads the recipient's state produce triadic coordination where a templated
broadcast does not?
Candidate hypothesis. A commit M = f(E) alone is dyadic (Φ_MIP = 0); a commit M = g(E, R) with R live is
triadic (Φ_MIP > 0). Null: both factor, or both are irreducible.
Procedure. Build the two forms at n = 3, identical except for whether M's commit reads R. Reuse
`classifier.classify_rules` and validate on the canonical triad control.
Expected discriminator. One edge, whether M's determination depends on R, flips the verdict, as it does
across the corpus.

### E2 — Substitutable recipients collapse the form

Question. Does mass outreach to interchangeable recipients factor even when each message is personalized
on its surface?
Candidate hypothesis. When the commit binds the recipient only through a substitutable disjunction
(M reads R1 ∨ R2 ∨ …), the form is dyadic; only an all-required joint determination on a specific
recipient stays triadic. Null: substitutability leaves Φ_MIP > 0.
Procedure. Reuse the substitutability sweep in `multiparty/` (the W ∧ (C1 ∨ C2) versus W ∧ C1 ∧ C2
contrast) with the recipient in the substitutable role.
Expected discriminator. Interchangeability of the recipient collapses the triad, matching the standing
finding that substitutability of any role factors the form.

### E3 — Disclosure is a label, not a read

Question. Does the agent identifying itself as automated change the structure of the coordination?
Candidate hypothesis. Self-identification is a label on the message and leaves M's read function alone,
so Φ_MIP is unchanged. Null: the verdict moves when a disclosure flag is added.
Procedure. Add a disclosure bit to the message with no change to the commit's dependence on E and R, and
recompute. Compare to E1's forms.
Expected discriminator. The verdict lives in the cause-effect structure, not in the label. This is the
q43 lesson, where a directed cycle in the wiring was a different object from a closed loop in the causal
structure. Disclosure is an ethical and economic variable; it is not a structural one.

### E4 — Cost as a proxy for the verdict

Question. Can a cheap signal of invested cost stand in for the structural verdict?
Candidate hypothesis. A cost proxy (compute or tailoring depth, estimated without exact Φ) separates
dyadic from triadic outreach only weakly, the way the time-series proxies do. Null: the cost proxy
recovers the verdict at high AUC.
Procedure. Reuse the `proxy_bridge/` estimator over the outreach forms, scoring a cost-like statistic
against the exact verdict.
Expected discriminator. If the proxy tracks the verdict, cost is a usable field signal. If it fails as
the ΦID proxy did (rank-AUC ≤ 0.63), then cost correlates with structure without recovering it, and the
exact computation stays the only reliable read.

### E5 — Reciprocity and response-liveness

Question. Is one-shot outreach ever triadic, or does irreducibility require the recipient's response to
feed back?
Candidate hypothesis. A one-shot send with no live return path factors. The form is triadic only when
R's response stays live to M's next commit, closing a real loop. Null: the one-shot send is already
irreducible.
Procedure. Compare a one-shot mediated send to a two-turn form with a return edge, reusing the
back-channel and liveness forms from `corpus/` and the q49–q51 seam studies.
Expected discriminator. The liveness condition from the structural findings, that each source must stay
live to the mediator's commit, should decide it, separating a campaign from a conversation.

## What this set does and does not claim

- **Structural, not normative.** Φ reads whether the coordination is irreducible. It does not say
  whether a given piece of outreach is welcome, ethical, or worth a reply. The credibility intuition is
  an economic layer the structural verdict only informs.
- **In-silico.** The sender, agent, and recipient are small Boolean models. Results are evidence about
  the models, separated from claims about real inboxes by the usual validation gap.
- **The cost claim is narrow.** The structural condition for a triad is a genuine joint determination of
  sender intent and a specific recipient's state. That work costs compute, so cost is a correlate of the
  verdict, not a cause of it.

## How it enters the program

This is a design at proposal stage, without pre-registered hypotheses. It enters the logbook as a
question (the next free q-number) through the six-stage protocol: review, literature, hypotheses fixed
before computing, methods, a run against the exact-Φ instrument, and a paper. It also sits on the lab's
standing rule that the program drafts and stages outreach while a human sends it. The structure studied
here is the structure that rule governs.
