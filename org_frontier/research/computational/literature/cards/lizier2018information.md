---
citekey: lizier2018information
title: Information Decomposition of Target Effects from Multi-Source Interactions: Perspectives on Previous, Current and Future Work
authors: Lizier, Joseph and Bertschinger, Nils and Jost, Jürgen and Wibral, Michael
year: 2018
doi: 10.3390/e20040307
arxiv: null
journal: Entropy
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: http://publikationen.ub.uni-frankfurt.de/files/51480/entropy-20-00307-v2.pdf
sha256: ba7bc3d44b1ccf68d9333c54155474af26e4b842905c832140b1101ddc7febb2
pdf_path: literature/pdfs/lizier2018information.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is an editorial for the Entropy Special Issue "Information Decomposition of Target Effects from Multi-Source Interactions," reviewing the field of Partial Information Decomposition (PID) and introducing the issue's contributions. PID, formulated by Williams and Beer in 2010, decomposes the mutual information that a set of source variables provides about a target into redundant (shared), unique, and synergistic (complementary) components. The editorial first reviews prior work: the original Williams-Beer axioms (symmetry, self-redundancy, monotonicity) and their Imin measure, the controversies it provoked (notably the Two-bit-copy example and the proposed identity axiom), and subsequent measures such as those of Harder et al., Griffith and Koch, and Bertschinger et al., along with the impossibility result of Rauh et al. that no measure can satisfy identity plus the original axioms with non-negative atoms for more than two sources. It then categorizes the special-issue articles into three themes: proposals of new redundancy measures, theoretical investigations (including numerical estimators), and applications (predominantly to neuroscience, plus computational biology and complex systems). The authors conclude with an outlook noting that finding the "right" redundancy measure has proven harder than expected but that community activity is strong.

## Key facts it relies on
- PID was formulated by Williams and Beer in 2010; for two sources S1, S2 and target T it relates the joint and individual mutual informations to redundant R(S1,S2→T), unique U(S1\S2→T) and U(S2\S1→T), and complementary/synergistic C(S1,S2→T) terms, e.g., I({S1,S2};T) = R + U(S1\S2) + U(S2\S1) + C.
- The PID framework proposed three axioms for a redundancy measure—symmetry, self-redundancy, and monotonicity—which specify a partial ordering and a partial information lattice but do not uniquely determine a redundancy measure.
- Williams and Beer's own measure Imin satisfied the axioms but was criticized for not distinguishing "the same information or just the same amount of information" and for failing a chain rule across target variables; on the Two-bit-copy example (target copies two IID input bits) Imin gave 1 bit redundant and 1 bit synergistic, while critics argued "the wires don't even touch."
- Harder et al. proposed a 4th "identity" axiom requiring redundancy in copying situations to equal the mutual information between the two source variables.
- Later measures included Ired (Harder et al., information-geometry based), I_SVK (Griffith and Koch), and Ũ_I (Bertschinger et al.); the latter two were found equivalent. Bertschinger et al.'s measure derived from "Assumption (*)" (existence of unique information depends only on pairwise source-target marginals) and carried a decision-theoretic operational interpretation.
- Rauh et al. proved no redundancy measure can satisfy the identity property together with the original Williams-Beer axioms while keeping non-negative partial information atoms for more than two source variables.
- Barrett showed the minimum mutual information (MMI) is a unique redundancy form for linearly coupled Gaussian variables (two sources) under the Williams-Beer axioms and Bertschinger et al.'s Assumption (*).
- The special issue was seeded by an informal PID workshop held in December 2016 at FIAS / Goethe University, Frankfurt; its papers are classified into new measures, theoretical investigations, and applications.
- New-measure contributions include Rauh et al.'s extractable shared information (satisfying target/left monotonicity), Ince's ICCS (pointwise, treating positive vs. negative pointwise information separately, introducing redundant misinformation), and Finn and Lizier's pointwise specificity/ambiguity decomposition with a "Pointwise Unique" example.
- Pica et al. identify only seven non-negative information subatoms needed to construct the three PIDs of a two-source one-target system (one per variable as target), given the ordering of the three redundancy terms.

## Critical notes from the literature
- The editorial itself stresses that finding a "completely satisfactory" redundancy measure remains unsolved—called "arguably the most fundamental missing piece in classical information theory"—and that the search has proven "far more difficult to solve than may have been expected."
- It acknowledges the impossibility tension (Rauh et al.): satisfying the intuitively appealing identity axiom forces dropping non-negativity or other original axioms for more than two sources, so candidate measures necessarily make trade-offs.
- The Bertschinger et al. measure is noted to be on rigorous mathematical footing but to face computational difficulties in solving the required convex optimization; Makkeh et al. in the same issue found only two software packages that solve it satisfactorily.
- Two of the new pointwise measures (Ince; Finn and Lizier) independently depart from the status quo by allowing negative partial information terms and dropping the identity axiom, signaling the field had not converged on a single accepted measure.
- As an editorial, this is a review/synthesis rather than a primary methodological contribution; its empirical and theoretical claims are summaries of the cited special-issue and prior articles.

## Key topics covered
Partial Information Decomposition (PID); redundant/unique/synergistic information; Williams-Beer axioms (symmetry, self-redundancy, monotonicity); Imin; identity axiom; Two-bit-copy example; partial information lattice; interaction information / net synergy; Bertschinger et al. measure and Assumption (*); decision-theoretic and game-theoretic operational interpretations; minimum mutual information (MMI); Gaussian and Gács-Körner constructions; pointwise/specificity-ambiguity measures (Ince ICCS, Finn-Lizier); Blackwell order; convex-optimization estimators; applications in neuroscience (neural cultures, EEG/epilepsy, receptive fields, RBMs), computational biology (MAPK cross-talk), and complex systems (2D Ising model, elementary cellular automata).
