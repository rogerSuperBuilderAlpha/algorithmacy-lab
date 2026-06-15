# Bidirectional coupling and pivotality decide major-complex membership in Boolean models of coordination

<code + data: org_frontier/studies/core_membership_law/ ; reproduce with
`python -m org_frontier.studies.core_membership_law.core_membership`>

## Abstract

Which parties of a coordination form belong to its irreducible core? Modeling a coordination form as
a small Boolean dynamical system and reading membership on the IIT-4.0 major complex, two conditions
decide it. A party must be bidirectionally coupled to the determination — it must both feed it and be
fed by it — and a party's probability of membership rises monotonically with the determination's
Boolean sensitivity to it. The first condition is IIT 4.0's own requirement for substrate membership,
confirmed here on coordination forms: in the strict-mediation family, non-bidirectional nodes enter
the major complex in 0 of 660 cases. The second is novel relative to IIT, whose exclusion postulate
makes membership per-form binary; a graded across-form membership law is the cause-effect-structure
analogue of pivotality in cooperative game theory, where a player's value is its average marginal
contribution and a null (fully substitutable) player contributes nothing. Inclusion rises from 38.9%
at low influence to 87.5% at high influence. A conjunctive all-required mediator gives Φ = n−1 with
every party in the core; substitutability of any party removes it. The verdict is in-silico, on small
Boolean models.

## Introduction

A coordination form binds a worker, a mediating system, and a counterpart. Some such forms are
irreducible across the parties — no partition along party lines preserves the determination — and the
question this paper answers is which parties are *in* that irreducible structure. The lab's instrument
reads the answer off the IIT-4.0 major complex, the maximally irreducible subset of nodes. A party can
be wired into a form and still sit outside its core; a corporate principal who owns the mediating
system need not be part of the coordination it owns.

Two prior literatures bear on the question. IIT 4.0 (Albantakis et al. 2023; Marshall et al. 2023)
defines membership in a complex and states a requirement for it. Cooperative game theory (Shapley
1953) defines which members are pivotal to a joint value. This paper asks whether the lab's
two-condition account of membership is implied by the first, rediscovers the second, or adds
something, and answers: it confirms the first, images the second, and contributes the bridge between
them.

## The instrument and the method

A coordination form is a Boolean dynamical system whose nodes are the parties; each party's next state
is a fixed function of the current states. Exact IIT-4.0 Φ over the minimum-information partition
classifies the whole form (triadic if irreducible, dyadic if it factors), and the major complex names
the maximally irreducible subset of nodes. Both are computed with PyPhi via the lab's classifier; the
instrument is validated on two controls before any run. A node is bidirectionally coupled if its
connectivity row and column each carry an off-diagonal edge — it feeds another node and is fed by one.
A node's influence is the determination's Boolean sensitivity to it: the fraction of (target, state)
pairs where flipping the node changes a target's next value.

Hypotheses were pre-registered after a literature pass and before any computation
(`hypotheses.md`, `literature/`). The pre-registered run was on the unconstrained 3-node family; a
labeled reconciliation re-ran the strict-mediation family, the construct's natural domain.

## Results

**Bidirectional coupling is necessary, and it is IIT's own requirement.** In the strict-mediation
family, non-bidirectional nodes appear in the major complex in 0 of 660 cases. This confirms IIT 4.0's
statement that a substrate unit must both affect and be affected by the rest of the system, enforced
by φ_s = min{φ_c, φ_e} and by directed partitions that cut inputs and outputs separately (Marshall et
al. 2023). The requirement is in fact enforced by the instrument: PyPhi draws candidate complexes only
from nodes with at least one input and one output, so a non-bidirectional node is never a membership
candidate, and the 0/660 is close to tautological by construction. The pre-registered unconstrained run
recorded a 15.8% exception rate; the run shows every exception to be a self-loop node — which has both
an input and an output to itself and so is causally significant to PyPhi, while the off-diagonal
structural definition misses it. The necessity holds; the exception is definitional.

**Pivotality grades membership, which IIT does not state.** Among coupled nodes, inclusion rises
monotonically with influence: 38.9%, 57.9%, 73.7%, 87.5% across influence quartiles (rank-AUC 0.629 in
the unconstrained family, higher in the strict-mediation family). IIT 4.0 membership is per-form
binary — the exclusion postulate selects a definite set by strict maximization of φ_s — so a graded
across-form membership law is not an IIT result. It is the cause-effect-structure analogue of the
Shapley value, where a player's importance is its average marginal contribution and a null player,
who changes no coalition's worth, receives zero (Shapley 1953).

**Triadicity is rare among mediated forms, and the conjunctive law is the witness against it.** The
strict-mediation triadic rate is 9.5%; the unconstrained rate is 55.7%, so rarity is specific to
mediated forms, not to Boolean systems generally. Against that rarity, a conjunctive all-required
mediator (the AND of all parties, each party reading it) is irreducible at Φ = n−1 with the full node
set in the core at n = 3, 4, 5 — the O-ring structure (Kremer 1993) in which every party is essential
and pivotal.

## Discussion

The contribution is a bridge, not a discovery of either condition. The necessity of bidirectional
coupling is IIT 4.0's existence-and-integration requirement, and finding it govern coordination forms
confirms the theory in a new domain rather than extending it. Pivotality is cooperative game theory's,
and finding membership graded by causal influence maps an information-theoretic membership criterion
onto a value-theoretic one. What is new is that IIT's per-form binary exclusion yields, across a
population of forms, a graded membership law that tracks pivotality — and that substitutability, which
sends a party's pivotality to zero, removes it from the core exactly as the Null Player axiom sends a
substitutable member's Shapley value to zero. The two frameworks meet on the coordination form: who is
in the irreducible cause-effect core is who is pivotal to the joint determination.

## Limitations

In-silico, on small Boolean models; Φ is read as the binary verdict and membership, not as a graded
scale. Influence is a single-node Boolean sensitivity that undercounts higher-order joint effects,
which is why the unconstrained AUC is moderate. The bidirectionality definition is structural; a
dynamical one over reachable states would absorb the self-loop case. The correspondence to the Shapley
value is made precise here only at the null-player corner; a full mapping between major-complex
membership and the Shapley value is the natural next study. And the validation gap stands: these are
models of coordination, not measurements of organizations.

## References

Albantakis L. et al. (2023). Integrated information theory (IIT) 4.0. *PLOS Comput. Biol.* 19(10):
e1011465.
Marshall W. et al. (2023). System Integrated Information. *Entropy* 25(2): 334. arXiv:2212.14537.
Shapley L. S. (1953). A value for n-person games. *Contributions to the Theory of Games* 2: 307–317.
Shapley L. S. & Shubik M. (1954). A method for evaluating the distribution of power in a committee
system. *Am. Polit. Sci. Rev.* 48(3): 787–792.
Kremer M. (1993). The O-ring theory of economic development. *Q. J. Econ.* 108(3): 551–575.
