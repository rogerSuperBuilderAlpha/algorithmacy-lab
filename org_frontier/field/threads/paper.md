# Platform position as cause-effect membership: an exact-Φ restatement of the competitive bottleneck and the outside-option principle

<code + data: org_frontier/field/threads/ ; reproduce with
`python -m org_frontier.field.threads.mediator_in_core` and
`python -m org_frontier.field.threads.enricher_regime`>

## Abstract

Modeling a mediated coordination as a Boolean dynamical system and reading membership on the IIT-4.0
major complex, a platform occupies one of four positions — indispensable bottleneck, dispensable
enricher, captor of one side, or bypassed — and which one is fixed by the parties' outside options:
the major complex is the platform plus exactly the parties with no outside option. Asymmetric options
give capture of the dependent side; symmetric options give bypass; a substitute direct channel
disintermediates the platform while a complement keeps it. A literature pass establishes that this is,
in its economic content, a rediscovery: capture of the dependent side is Armstrong's competitive
bottleneck, the asymmetric/symmetric split is the Binmore–Shaked–Sutton outside-option principle, and
the dependence-and-exclusion membership law is network-exchange power (Easley & Kleinberg). The paper's
only contribution is the cross-method restatement — that these value-theoretic results appear as an
exact cause-effect membership law computed from Φ — together with one minor re-description, the rare
and fragile enricher regime. The verdicts are in-silico, on small Boolean models.

## Introduction

Two field threads explored when a mediating system belongs to the irreducible coordination it sits in.
They produced a clean theory: a trichotomy of platform positions, a disintermediation rule, and an
outside-option law for membership. Before claiming any of it as new, the determining question is what
platform economics, bargaining theory, and network-exchange theory already say. The answer, established
by a deep-research pass, is that they say nearly all of it. This paper therefore makes a deliberately
small claim and is explicit about the boundary between the established economics and the restatement.

## Method

Each arrangement is a Boolean dynamical system whose nodes are the parties; exact IIT-4.0 Φ over the
minimum-information partition gives the verdict, and the major complex names the irreducible core, both
computed with the lab's PyPhi classifier and validated on two controls. A party's outside option is
encoded as the ability to coordinate through a peer instead of the platform (none / conditional /
full). The two thread scripts are deterministic and CI-gated; the hypotheses (`hypotheses.md`) are
fixed, and the runs are the confirmatory test.

## Results

**The trichotomy and the outside-option core law.** A mediator in the major complex is a bottleneck
(no party fallback; indispensable), an enricher (a fallback exists but a conjunctive complement still
deepens integration; dispensable), or bypassed. Across a 4-node battery the major complex is the
platform plus exactly the parties with no outside option (60/60). This is network-exchange power —
"a node is powerful precisely when its partners have no alternative while it has several" (Easley &
Kleinberg) — and the competitive bottleneck (Armstrong 2006), restated as cause-effect membership.

**Disintermediation requires a substitute.** A platform is bypassed when the parties' direct tie is a
substitute (either path works), kept when it is a complement (both needed). This is the
fee-competition / diversion mechanism: an alternative route collapses platform power, and removing it
restores the bottleneck (Armstrong; Bakos & Halaburda 2020 for the symmetric-multi-homing collapse).

**Asymmetry gives capture, symmetry gives bypass.** Asymmetric outside options lock the dependent
party into the core with the platform; symmetric options bypass it. This is the outside-option
principle (Binmore, Shaked & Sutton 1989): a binding option pins one party and makes the other the
residual claimant, while non-binding options give the equal split. Empowering one captive party
transfers the lock-in to the other rather than dissolving it — the same asymmetry, relocated.

**The enricher is rare and fragile.** Genuine enrichment — in the core yet dispensable, the platform
that enables its own fallback — is a small minority of in-core forms (≈6%) and degenerates into capture
under perturbation. This is the one framing the economics does not state in these terms, and it is, at
bottom, the knife-edge between the competitive-bottleneck and both-multi-home regimes.

## Discussion

The economic content of the platform-position theory is established. Capture of the side without an
alternative, disintermediation by a substitute channel, lock-in of the dependent party, and the
collapse of platform power under symmetric outside options are the competitive bottleneck, the
outside-option principle, and network-exchange power. The contribution is not these results but their
appearance, unbidden, as an exact IIT-4.0 cause-effect membership law: a platform's place in the
irreducible structure of a Boolean coordination model is the platform plus the parties with no outside
option. A bargaining-power result and an information-theoretic irreducibility result coincide on the
coordination form. That coincidence is the paper, and the enricher knife-edge is its only new
description.

## Limitations

In-silico, small Boolean models; Φ is read as the binary verdict and membership. Outside options are
encoded coarsely (none / conditional / full), and the law is sharpest for the conjunctive platform. The
correspondence to the outside-option principle and the competitive bottleneck is structural, not
derived — the paper shows the regimes coincide, not that one implies the other. The validation gap
stands: these are models, not measurements of platforms.

## References

Armstrong M. (2006). Competition in two-sided markets. *RAND J. Econ.* 37(3): 668–691.
Armstrong M. & Wright J. (2007). Two-sided markets, competitive bottlenecks and exclusive contracts.
*Econ. Theory* 32(2): 353–380.
Binmore K., Shaked A. & Sutton J. (1989). An outside option experiment. *Q. J. Econ.* 104(4): 753–770.
Easley D. & Kleinberg J. (2010). *Networks, Crowds, and Markets*, ch. 12. Cambridge Univ. Press.
Bakos Y. & Halaburda H. (2020). Platform competition with multihoming on both sides. *Manag. Sci.*
66(12): 5599–5607.
Farrell J. & Klemperer P. (2007). Coordination and lock-in. *Handbook of Industrial Organization* 3:
1967–2072.
Williamson O. E. (1985). *The Economic Institutions of Capitalism*. Free Press.
