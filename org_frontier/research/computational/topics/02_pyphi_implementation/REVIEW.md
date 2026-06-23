# PyPhi and Reference Computation
<!-- run: 2026-06-23 | sources: 9 -->
Search method: WebSearch and WebFetch plus the Consensus and Scholar Gateway academic tools, with every identifier confirmed against Crossref; run date 2026-06-23.

PyPhi is the canonical open-source reference implementation for computing exact cause-effect structures and integrated information (Φ) on small discrete networks (Mayner et al., 2018). The package operates on a transition probability matrix describing a discrete, Markovian system of binary elements, and exposes two core operations: unfolding the full cause-effect structure of a subsystem and computing its Φ, and identifying the maximally-irreducible cause and effect repertoires of an individual mechanism (Mayner et al., 2018). Its formalism follows IIT 3.0, where Φ measures the irreducibility of a system's conceptual structure to its minimum information partition (Oizumi et al., 2014). The implementation is a faithful encoding of that mathematics, which makes it a shared baseline for empirical and methodological work.

The defining property of reference computation here is intractability. The algorithm runs in time O(n⁵·3ⁿ) because states, subsystems, mechanisms, purviews, and partitions each grow exponentially with system size, confining exact analysis to roughly ten to twelve nodes (Mayner et al., 2018). This wall motivates two responses. One extends the data structures: the multi-valued update generalizes elements beyond two states to ternary, quaternary, and mixed nodes, and applies the tooling to a p53-Mdm2 regulatory model while examining binarization choices (Gomez et al., 2020). The other develops approximations and surrogates. Heuristic and approximate measures have been benchmarked against exact Φ3.0 on small binary networks to assess which correlate well enough to substitute (Sevenius Nilsen et al., 2019), prior-guided random search has been used to find high-Φ graph structures as node count grows (Garrido-Merchán and Sánchez-Cañizares, 2022), and graph neural networks with transformer convolutions have been trained to estimate system-level integrated information and the major complex where exact computation is infeasible (Hosaka, 2025).

The theory the software targets has since advanced. IIT 4.0 reformulates the postulates mathematically, introduces an intrinsic-difference measure, and characterizes Φ-structures as compositions of distinctions and relations with their own integrated information (Albantakis et al., 2023a), a formalism tracked in PyPhi's iit-4.0 development branch. The same framework has been pushed onto quantum mechanisms, computing the integrated information of a CNOT gate (Albantakis et al., 2023b). Methodological scrutiny of the toolbox continues, with testing and improvement strategies proposed for the implementation itself (Guerrero et al., 2024). Across these strands the pattern is consistent: PyPhi anchors exact computation on small systems while extensions trade exactness for reach.

## References

Albantakis, L., et al. (2023a). Integrated information theory (IIT) 4.0. PLOS Computational Biology, 19(10), e1011465.

Albantakis, L., Prentner, R., and Durham, I. (2023b). Computing the Integrated Information of a Quantum Mechanism. Entropy, 25(3), 449.

Garrido-Merchán, E. C., and Sánchez-Cañizares, J. (2022). Optimizing Integrated Information with a Prior Guided Random Search Algorithm. arXiv:2212.04589.

Gomez, J. D., et al. (2020). Computing Integrated Information (Φ) in Discrete Dynamical Systems with Multi-Valued Elements. Entropy, 23(1), 6.

Guerrero, L. E., et al. (2024). Integrated Information Theory with PyPhi: Testing and Improvement Strategies. Lecture Notes in Networks and Systems.

Hosaka, T. (2025). Graph neural networks for integrated information and major complex estimation. PLOS One, 20(11), e0335966.

Mayner, W. G. P., et al. (2018). PyPhi: A toolbox for integrated information theory. PLOS Computational Biology, 14(7), e1006343.

Oizumi, M., Albantakis, L., and Tononi, G. (2014). From the Phenomenology to the Mechanisms of Consciousness: IIT 3.0. PLoS Computational Biology, 10(5), e1003588.

Sevenius Nilsen, A., Juel, B. E., and Marshall, W. (2019). Evaluating Approximations and Heuristic Measures of Integrated Information. Entropy, 21(5), 525.
