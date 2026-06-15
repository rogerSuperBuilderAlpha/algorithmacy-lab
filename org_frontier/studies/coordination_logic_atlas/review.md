# Coordination-logic atlas — Stage 1 review

## The question

Across the space of small Boolean coordination forms, which determination logics and topologies yield
an irreducible (triadic) verdict, and what laws govern the boundary? The atlas answers it with 50
pre-registered experiments in five themes: quorum thresholds, four-node topology, redundancy and
degeneracy, inhibition and valence, and heterogeneity.

## What is already here

This study was built with the protocol's pre-registration discipline in place: `hypotheses.md`
states the five theme predictions and the per-form expectations, `methods.md` fixes the design, the
run is committed and CI-gated (`coordination-logic-atlas`), and `FINDINGS.md` reports the results,
including the misses. The headline result — a k-of-n quorum mediator is irreducible only at the
extremes (k=1, k=n) and dyadic at every interior threshold — is the cleanest novel-looking law in the
set, alongside the spectator/verdict-complex distinction (a reproduction of q74/q75) and the
rotation-is-irreducible result (a reproduction of q11).

## The gap

The study never had a Stage-2 literature pass or a `paper.md`. Without the literature it is unknown
whether the standout results are novel or rediscoveries:

1. **The extremes-only quorum law.** Threshold/quorum functions and their dynamics are heavily studied
   in Boolean-network theory (Kauffman, canalizing functions), threshold-network criticality, and the
   quorum-sensing literature. Is the qualitative split between interior and extreme thresholds known?
2. **Parity maximizes integration.** The atlas reproduces (from q54 and the inhibition theme) that
   XOR/XNOR mediators bind more readily than monotone ones. Is "parity maximizes integration" an
   established IIT or Boolean-complexity result?
3. **Rotation is irreducible.** The directed-cycle result echoes q11. Is the irreducibility of a
   permutation/rotation known in the integration literature?

The deep-research report (`literature/deep_research_report.md`) resolves these before the paper frames
the contribution. The hypotheses were already fixed before the run; the paper's job is the literature
grounding and the honest novelty assessment, not new pre-registration. Any new experiment (weighted or
noisy quorums to test whether extremes-only survives perturbation) will be pre-registered separately.
