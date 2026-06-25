---
citekey: balduzzi2008integrated
title: Integrated information in discrete dynamical systems: motivation and theoretical framework
authors: Balduzzi, David and Tononi, Giulio
year: 2008
doi: 10.1371/journal.pcbi.1000091
arxiv: null
journal: PLoS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1000091&type=printable
sha256: f3cb9a6bbf4ba56cd304ef2b1769d6c8aa54ce75d74de954c7605d7e7cfe71a7
pdf_path: literature/pdfs/balduzzi2008integrated.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces a time- and state-dependent measure of integrated information, phi, that quantifies how much information is generated when a discrete system enters a particular state through causal interactions among its elements, above and beyond the information generated independently by its parts. The measure is motivated by two phenomenological properties of consciousness drawn from the integrated information theory: a conscious experience generates a large amount of information by ruling out alternatives, and that information is integrated (cannot be decomposed into independent parts). The authors extend prior work, which had treated stationary multidimensional Gaussian systems, to discrete dynamical systems evolving in discrete time, applying the framework to small example systems of a dozen or fewer elements (e.g., AND-gates, COPY, XOR). Effective information is defined as the relative entropy (Kullback-Leibler divergence) between an a posteriori repertoire and a maximum-entropy a priori repertoire, and phi is effective information measured across the minimum information partition (the system's "weakest link"). Through worked examples they show phi depends on the entered state, on network dynamics, and on causal architecture: it is low for inactive, hyperactive, modular, and homogeneous systems, and high when functional specialization is conjoined with integration and when firing is balanced. They define complexes (and main complexes) as the subsets capable of integrating information, and argue phi is a useful metric for the capacity of any physical system to integrate information.

## Key facts it relies on
- Effective information is defined as the entropy of the a posteriori repertoire relative to the a priori repertoire: ei(X0 -> x1) := H[p(X0 -> x1) || p^max(X0)] (Equation 1A); given the a priori repertoire is the maximum-entropy distribution, this simplifies to a difference of entropies ei(X0 -> x1) = H(p^max(X0)) - H(p(X0 -> x1)) (Equation 1B).
- The a priori repertoire is the maximum-entropy (maxent) distribution over system states (complete ignorance); for a system of n binary elements it has entropy of at most n bits. The a posteriori repertoire is the repertoire of states that could have led to x1 through causal interactions, found by a perturbational approach intervening on the system and applying Bayes' rule.
- Integrated information phi is the entropy of the a posteriori repertoire of the whole relative to the combined a posteriori repertoires of the parts across the minimum information partition (MIP): phi(x1) = H[p(X0 -> x1) || prod p(M0^k -> mu1^k)] (Equation 2A); phi is zero if and only if the system can be decomposed into a collection of causally independent parts.
- Figure 1: a system of three connected AND-gates transitioning from state x0=110 to x1=001; the a priori repertoire entropy is 3 bits and the a posteriori repertoire entropy is 0 bits, so 3 bits of effective information are generated (1 of 8 perturbations specified, the other 7 ruled out).
- Figure 2 examples: a two-element COPY couple generates ei = 2 bits; the AND-gate system entering state 000 generates ei = 1 bit (four perturbations cannot be distinguished); systems that "always fire" (entering 111) or fire at random generate ei = 0 bits because no alternatives are ruled out (a posteriori repertoire equals the maxent a priori repertoire).
- Figure 3: a system of two disjoint couples generates effective information of 4 bits as a single entity, but phi = 0 bits across the minimum information partition P^MIP = {M^1, M^2} because the two couples do not interact (combined a posteriori repertoire of the parts coincides with that of the whole).
- The normalization is N_P = (m-1) * min_k {H^max(M0^k)}, where m is the number of parts; the MIP is the partition minimizing normalized effective information P^MIP = argmin_P {ei(X0 -> x1/P)/N_P}, and once found phi(x1) = ei(X0 -> x1/P^MIP) (Equation 2B).
- Integrated information is bounded: for a discrete system of n binary elements, phi(x1) <= n bits.
- A subset S of X forms a complex when phi(s1) > 0 and S is not contained in a larger set with strictly higher phi; a main complex additionally has phi strictly greater than any set containing it (Equations 3A, 3B). Only a complex can be considered to form a single entity.
- Figure 9: integrated information, computed by averaging over all states with a given number of elements firing, peaks for balanced states and is low for inactive (no elements firing) and hyperactive (all elements firing) states; in panels 9A and 9C no information is integrated when the system is hyperactive because it is "over-determined."

## Critical notes from the literature
- The authors state explicitly that their example systems "are too small to be considered at all realistic" (a dozen or fewer elements) and are chosen only to illustrate relationships between integrated information, causal architecture, dynamics, and noise.
- Elements are modeled as memoryless first-order Markov processes (output at time t depends only on inputs at t-1); the authors note that extending the framework to elements with memory, and explaining how the natural time frame for measuring phi is specified, is left to future work.
- Elements are assumed to be abstract, indivisible units with no accessible internal state (e.g., logic gates, threshold functions); the authors defer to future work the investigation of elements' internal structure and the conditions under which they can be considered indivisible.
- For computational reasons phi is measured across bipartitions rather than all partitions in the example analyses; the authors justify this by noting (Text S1, section 6) that restricting to bipartitions provides a lower bound on the expected value of integrated information.
- The paper acknowledges a related measure, stochastic interaction, and distinguishes its own approach by comparing the whole to the parts rather than the parts to one another (Text S1, section 8).

## Key topics covered
- Integrated information theory of consciousness; the "first problem of consciousness"
- Effective information; a priori vs a posteriori repertoires; maximum-entropy distribution
- Relative entropy / Kullback-Leibler divergence; perturbational approach; Bayes' rule
- Integrated information phi; minimum information partition (MIP); normalization
- Complexes and main complexes; ports-in and ports-out
- Discrete dynamical systems; logic gates (AND, XOR, COPY); first-order Markov processes
- Relationship of phi to network dynamics, firing rate, balanced states, and causal architecture
- Feedforward, lattice, modular, homogeneous, and bistable architectures; extrinsic inputs
- Photodiode and digital-camera thought experiments; thalamocortical relevance to consciousness
