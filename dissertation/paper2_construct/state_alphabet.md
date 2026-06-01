# The state alphabet: the pre-registered individuation rule (Paper 2 §3–§4)

This is the paper's single empirical commitment, fixed by definition **before any Φ is computed**, in
the same spirit Paper 1's instrument was validated on controls before any comparison. Φ is not
invariant to how the application-layer states are individuated, so the rule that carves them is
load-bearing: get it wrong and the triadic/dyadic verdict becomes an artifact of post-hoc state-carving
rather than a fact about the coordination. Pre-registering the rule is what lets two analysts apply it
to the same interaction logs, individuate the same states, and reach the same Φ.

## 1. Where the measure runs: the application layer, not the mechanism

The measure does not run over the algorithm's internal mechanism. It runs over the **application
layer** — the states the two parties move through and the determinations the mediator commits between
them — all of which are observable in ordinary interaction logs (a driver's logins, positions,
accept/decline events and the dispatches and prices returned; a résumé's submission, the
forward/reject the system commits, the manager's callback).

This is what resolves the opacity problem. The mechanism is epistemically opaque: the analyst cannot
see the proprietary internals, and need not. Φ over the application-layer transition matrix is a
property of the **observable** dynamics the parties operate in, not of the hidden mechanism that
produces them. The claim is the precise formal one and no more: the cause-effect structure of the
observed application-layer transition matrix is irreducible over its minimum-information partition.
That is a computable fact about the dynamics — distinct from epistemic opacity (the analyst cannot see
the mechanism) and from any metaphysical claim about emergence.

## 2. The individuation rule (the commitment)

> **A new application-layer state begins when the mediator commits a determination that alters its
> causal disposition toward the parties.**

A *determination* is a commitment the mediator makes — a forward or a reject, a match or no match, a
price, a rank, a score — that changes how it will subsequently constrain what passes between the two
parties. The rule individuates states by these commitments, and by nothing else.

In the imported vocabulary, the rule has an exact reading. A determination is a transition that moves
the mediator's **cause repertoire and effect repertoire together**: it changes both what could have
led the system here and what the system now constrains downstream. That joint movement is what makes a
transition *irreducible* rather than cosmetic, and it is exactly the quantity Φ is built to register. A
change that moves neither repertoire — a re-rendering of a value already committed — is not a new
application-layer state, however much it may look like one on the interface.

## 3. The rule defended against the two criteria it absorbs

Two rival criteria feel like state boundaries, and the rule deliberately rejects both.

**Action availability** ("a new state begins whenever a party *can* act differently"). The availability
of an action is not a commitment. An action a worker could take but that commits nothing — a button
she may or may not press, a field she may or may not fill — leaves the mediator's causal disposition
toward the parties unchanged, so it does not begin a new application-layer state. Availability is a
property of the interface; the rule individuates on commitment, not option.

**Visibility / disclosure** ("a new state begins when a value becomes visible to a party"). Disclosing
a value the mediator has already committed changes *who can read it*, not *what it constrains*. The
cause and effect repertoires are unmoved by the disclosure, so it does not begin a new state. Reading
is not committing.

Both criteria conflate the surface of the interaction with its causal structure. The rule individuates
on the causal structure — the committed determination — which is why it can be applied to a log without
the analyst's judgment entering, and why the resulting Φ is a fact rather than a choice.

## 4. Building the transition matrix from observable logs

Under the rule, the application-layer transition matrix is constructible from interaction logs without
any proprietary internals. The procedure:

1. **Nodes.** The parties at the application layer: the worker (W), the mediating system (S), and the
   counterpart (C). Each node carries a determination-bearing value — for the worked examples, a binary
   state in {0, 1} (the relevant signal present or absent, the determination committed or not, the
   counterpart engaged or not).
2. **States.** A system state is the joint configuration of the nodes between determinations; a new
   state is entered when, and only when, the rule fires (the mediator commits a determination that
   moves its disposition toward the parties).
3. **Transitions.** From the logs, the application-layer transition matrix records how each node's next
   determination-bearing value follows from the current system state — who constrains whom, which the
   committed determinations make observable. This is a state-by-node TPM of the exact form the
   instrument consumes (`proxy_audit.exact_phi`).

Nothing in this construction requires seeing the mechanism. It requires only the record of what the
mediator committed and what each party did in response — the application layer, by definition observable
to its participants and reconstructible from logs.

## 5. Granularity is the discipline, not a defect

Φ is super-exponential in the number of states, so the state alphabet must stay small. The individuation
rule is what keeps it small in a principled way: only determination-bearing transitions count, so the
alphabet is governed by how often the mediator actually commits, not by every cosmetic change on the
interface. The tractability limit and the individuation rule are the same discipline seen from two
sides — the rule that makes the verdict well-defined is also the rule that keeps it computable.

## 6. The hardest case, pre-registered as open: the continuous stream

The rule's stress test is the platform that commits in a near-continuous stream. Uber commits
determinations constantly — every repositioning re-weighted, every surge tick re-priced, every match
re-evaluated — and a continuous stream has no natural discrete boundary at which one application-layer
state ends and the next begins. The rule says "a new state per committed determination," but when
determinations arrive without pause, the analyst must choose a window, and Φ depends on that choice.

The paper does not resolve this; it pre-registers it as the rule's open boundary and hands it to Paper
3. There, an **observed coordination outcome** supplies the anchor the continuous case lacks: the
granularity is fixed not by fiat but by the window at which Φ best tracks the outcome it is meant to
predict. Until that anchor is in hand, the instrument is honest about where the rule is sharp (discrete,
log-reconstructible determinations, as in the worked examples) and where it is not yet (the continuous
stream).
