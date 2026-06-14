# Coordination-logic atlas — pre-registered hypotheses

Fifty coordination forms, grouped in five themes. Each form is a Boolean dynamical system whose
nodes are the parties. The verdict is exact IIT-4.0 Φ over the minimum-information partition,
read on the whole system; the major complex is recorded alongside to locate the irreducible core.
Every prediction follows from two principles already established in this lab's logbook:

- **Bidirectionality.** A node joins the irreducible core only if it both feeds the shared
  determination and reads it back. An emit-only source or a read-only sink drops out.
- **Pivotality.** A node's place in the core rises with the determination's sensitivity to it.
  A node the determination can ignore — because others can substitute for it, or because its
  value is frozen — carries no irreducibility.

The decision rule is fixed before the run: a form is **triadic** when its whole-system Φ_MIP
exceeds 1e-9 in some reachable state, **dyadic** otherwise. The instrument validates on its two
controls (a decoupled form must read dyadic, a fully coupled form must read triadic) before any
verdict is trusted.

## Theme A — Quorum threshold (k-of-n)

A mediator fires when at least `k` of `n` parties are active; every party reads the mediator back.

**HA. A quorum binds the parties only at the extremes.** At `k=1` every party can trigger the
determination alone; at `k=n` every party can veto it; both make every party pivotal, so the form
is triadic. At any interior `k` each party is substitutable — the others can cross or miss the
threshold without it — so no party is individually pivotal and the form is dyadic. Prediction:
triadic at `k∈{1,n}`, dyadic for `1<k<n`, at every `n` from 2 to 5.

## Theme B — Topology at a fixed four nodes

The same four parties, wired as organizational forms.

**HB. Irreducibility tracks shared, two-way coupling.** A centralized star, a complete graph, an
AND-ring, a two-hub matrix, and a complete bipartite coupling each route every party through a
shared determination and should read triadic. Two independent dyads and a feed-forward star
(spokes that never read the hub) factor and should read dyadic. A star with one isolated node
should read triadic on the connected triad. A pure copy-cycle, carrying no joint determination,
should read dyadic.

## Theme C — Redundancy and degeneracy

Does duplicating an element preserve irreducibility or open a path the system factors through?

**HC. Redundancy every party reads is harmless; redundancy that adds an independent path
factors.** Duplicate mediators that the parties read, triple-modular voting, and a hot standby
should stay triadic. Parallel one-way relays, an independent backup pair, and substitutable
workers under OR should read dyadic. An unread duplicate should leave the original core intact.

## Theme D — Inhibition and valence

Three parties; the mediator's determination is inhibitory or mixed-sign.

**HD. The verdict is blind to the sign of a symmetric coupling.** NAND, NOR, mutual inhibition,
and inverting feedback are the De Morgan or negated images of AND and OR and should match their
triadic verdicts. A one-sided veto and material implication should also bind, since both parties
still determine the mediator. A veto whose source never reads back should drop that party.

## Theme E — Heterogeneity and bias

Asymmetric arity, memory, constant-policy and read-only roles.

**HE. Constant and read-only nodes shed; a party with zero influence drops the form to a dyad.**
Asymmetric arity, memory, and a policy node that can substitute for a party should stay triadic.
A constant-policy node, a read-only manager, and a one-way gate should leave the worker–system–
counterpart core intact while themselves dropping out. A party the determination ignores should
shed, leaving a dyad.

## Note on the instrument for spectator forms

Several Theme C and E forms add a node that the principles say should drop out (a constant, a
read-only manager, an unread copy). For these the prediction above is the **whole-system** verdict.
Where whole-system Φ and the major complex disagree, the disagreement is itself the result: the
spectator sinks the whole-system reading while the core stays irreducible, which is why membership
is read on the major complex. The run reports both.
