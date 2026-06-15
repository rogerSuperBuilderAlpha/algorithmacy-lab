# A coordination-logic atlas: the determination logics that make a coordination form irreducible, and the extremes-only quorum law

<code + data: org_frontier/studies/coordination_logic_atlas/ ; reproduce with
`python -m org_frontier.studies.coordination_logic_atlas.run`>

## Abstract

Fifty Boolean coordination forms, classified by exact IIT-4.0 Φ across five axes — quorum thresholds,
four-node topology, redundancy, inhibition, and heterogeneity — map which determination logics make a
coordination irreducible. The headline result is a quorum law: a mediator that fires when at least k of
n parties are active, with the parties reading it back, is irreducible only at the extremes (k = 1,
any-one; k = n, unanimity) and reducible at every interior threshold, where the parties become mutually
substitutable. The law is novel as an IIT result and has two external parallels: the quorum-sensing
literature describes only AND-like and OR-like signal-integration gates — the two extremes — and never
an interior k-of-n gate, and Granovetter's threshold models show collective threshold dynamics break
discontinuously at the margin. Two further results are framed as rediscoveries: parity mediators bind
more readily than monotone ones (the known XOR-vs-AND/OR irreducibility contrast), and a directed cycle
is irreducible (prior lab work). The verdicts are in-silico, on small Boolean models.

## Introduction

A coordination form's verdict — does it factor along party lines or not — is decided by the mediator's
determination logic and the wiring, not by the number of parties. This paper sweeps the
determination-logic space systematically and reports the laws at its boundary. The motivating gap is
that the lab's logbook had tested the conjunctive (AND) and disjunctive (OR) extremes of threshold
coordination but never the interior, and never the determination-logic space as an atlas.

Two literatures frame the results. Boolean-network theory studies threshold, canalizing, and
non-monotone update functions (Manicka et al. 2022; Noual et al.). Threshold models of collective
behaviour (Granovetter 1978) and quorum sensing study exactly the read-back threshold structure a
quorum mediator has. The paper places the atlas's results against both.

## Method

Each form is a Boolean dynamical system; exact IIT-4.0 Φ over the minimum-information partition gives
the verdict and the major complex gives membership, computed with the lab's PyPhi classifier and
validated on two controls. The fifty experiments and their pre-registered predictions are in
`hypotheses.md` and `methods.md`; the run is committed and CI-gated. Predictions were fixed before
computation.

## Results

**The extremes-only quorum law.** A k-of-n quorum mediator is triadic at k = 1 and k = n (Φ = n−1,
full core) and dyadic at every interior threshold, across n = 2…5, with no gradient — interior
thresholds give Φ = 0 and no irreducible core at all. The mechanism is substitutability: at an
extreme every party is individually pivotal (each can trigger alone at k = 1, or veto at k = n); at an
interior quorum the others can cross or miss the count without any one party, so no party is pivotal
and the form factors. This is novel as an IIT result. Its standing comes from two parallels: the
quorum-sensing literature, where nature combines signals only into AND-like (k = n) or OR-like (k = 1)
gates and never an interior k-of-n gate; and Granovetter's threshold models, where the aggregate
depends on the exact threshold and a one-unit change flips the equilibrium discontinuously.

**Parity binds more readily — a rediscovery.** Across the inhibition theme, parity mediators (XOR,
XNOR) yield a triadic verdict where monotone ones (AND, OR) factor, reproducing the established
contrast between parity as the canonical synergistic/irreducible function and AND/OR as reducible
(Griffith & Koch 2014; the IIT logic-gate examples). The atlas confirms it on coordination forms; it
is not a new finding.

**Topology and the rest.** Among four-node wirings the star, complete, AND-ring, two-hub matrix, and
bipartite forms bind, while two independent dyads and the feed-forward star factor; a directed cycle
(pure rotation) is irreducible, reproducing the lab's oscillatory-scaling result. Redundancy that adds
a substitute path factors the form; a spectator node sinks the whole-system verdict while the core
survives, reproducing the verdict-versus-complex distinction. Of the fifty, 36 matched their
pre-registered prediction; the misses resolve into substitutability, spectators, and
synchronization/absorption.

## Discussion

The atlas's contribution is the systematic IIT-irreducibility map over the determination-logic space
and, within it, the extremes-only quorum law. The law says that of all the ways a mediator could
require its parties — any threshold from 1 to n — only the two extremes produce an irreducible
coordination, and the interior, where parties are substitutable, does not. That nature's quorum-signal
integration uses only those two extremes, and that threshold models of collective behaviour break
discontinuously at the margin, are independent reasons the result is not an artifact. The parity and
rotation results are honest rediscoveries that the atlas confirms in this setting.

## Limitations

In-silico, small Boolean models; Φ is read as the binary verdict and membership. The quorum forms use
a clean threshold count; weighted or noisy quorums are untested and are the natural next experiment to
check whether extremes-only survives perturbation. The parallels to quorum sensing and threshold
models are analogies, not derivations. The validation gap stands.

## References

Griffith V. & Koch C. (2014). Quantifying synergistic mutual information. In *Guided Self-Organization:
Inception*, 159–190.
Granovetter M. (1978). Threshold models of collective behavior. *Am. J. Sociol.* 83(6): 1420–1443.
Manicka S., Marques-Pita M. & Rocha L. M. (2022). Nested canalizing functions minimize sensitivity and
simultaneously promote criticality. *J. R. Soc. Interface*.
Noual M., Regnault D. & Sené S. Non-monotony and Boolean automata networks.
Albantakis L. et al. (2023). Integrated information theory (IIT) 4.0. *PLOS Comput. Biol.* 19(10):
e1011465.
Pratt S. C. et al. (2002). Quorum sensing, recruitment, and collective decision-making during colony
emigration. *Behav. Ecol. Sociobiol.* 52: 117–127.
