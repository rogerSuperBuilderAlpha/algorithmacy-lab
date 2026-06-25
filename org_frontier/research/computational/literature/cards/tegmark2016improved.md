---
citekey: tegmark2016improved
title: Improved Measures of Integrated Information
authors: Tegmark, Max
year: 2016
doi: 10.1371/journal.pcbi.1005123
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005123&type=printable
sha256: d9742c2417eb790cf523ade3283a5ba9f4c5690044032b09ac0726f1005f8e39
pdf_path: literature/pdfs/tegmark2016improved.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses the problem that existing measures of integrated information (Φ) from Integrated Information Theory and related proposals are computationally infeasible to evaluate for large systems, hampering experimental tests of consciousness theories. Tegmark builds a unified taxonomy of integration measures by modeling a system's time-evolution as a Markov process and defining each Φ-measure through four independent choices: a recipe for approximately factorizing the Markov matrix into a tensor product of two subsystem matrices, which probability distributions to compare, what is treated as known about the current state, and a distance measure between the two distributions. He shows that the nominal hundreds of options (5 factorizations × 3×4 distribution/conditioning choices × 7 distance measures) collapse to about 21 distinct well-defined measures, of which only a handful lack major drawbacks, and several turn out to be identical to each other or to previously proposed measures (Barrett-Seth, mismatched-decoding, IIT2.0, IIT3.0). For the Kullback-Leibler distance he derives the optimal factorization analytically, yielding a "Markov measure" φᴹ equal to the mutual information across space minus mutual information across time. He further derives exact Gaussian (continuous-variable) formulas that reduce the cost from doubly exponential to polynomial in system size, and proposes a graph-theory approximation that finds the "cruelest cut" bipartition in polynomial time. The result is a set of exact and approximate formulas that can be applied to real-world time-series laboratory data without unreasonable computational demands.

## Key facts it relies on
- All Φ-measures are defined in two steps: (1) for an imaginary cut partitioning the system into two parts, define a measure φ of how much the two parts affect each other; (2) define Φ as the φ-value for the "cruelest cut" that minimizes φ; the number of cuts to minimize over grows super-exponentially with the number of bits.
- A Φ-measure is specified by four choices: a recipe for approximate factorization M ≈ Mᴬ ⊗ Mᴮ (5 options: noising n, mild noising m, optimal-not-knowing-state o, optimal-given-x₀ x, optimal-on-average a), which distributions p and q to compare (3×4 options across variable selection t/f/a/p and conditioning u/s/k), and a distance measure (7 options: KL d_KL, L₁ d₁, L₂ d₂, Hilbert-space d_H, Shannon-Jensen d_SJ, Earth-Movers d_EM, Mismatched-Decoding d_MD).
- The nominal 5 × 4 × 3 × 7 = 420 measures reduce because most are zero, undefined, or identical; this leaves 21 separate options shown in Table 2, and only a handful lack major drawbacks (Table 1).
- For the KL-divergence, the optimal factorization can be solved analytically (the only one of the distance options for which the author could do so), giving φᵒᵗᵘᵏ = I(xᴬ,xᴮ) − I(x₀ᴬ,x₀ᴮ), i.e. the mutual information across space minus mutual information across time (eq 33); this defines the "Markov measure" φᴹ.
- φᴹ relates to the Barrett-Seth measure φᴮ via φᴮ(p) = φᴹ(p) − I(x₁ᴬ,x₁ᴮ) (eq 40); φᴮ can be negative (e.g. φᴮ = −1 for two independent perfectly-correlated unchanging bits), violating positivity, whereas φᴹ is non-negative and equals the KL-divergence between the actual distribution and its best separable approximation.
- The time-reversed Markov measure φᵒᵗⁱᵘ is shown identical to Barrett-Seth's φ̃_E and to Ay's "stochastic interaction" measure (eq 38), and φᴹ is shown closely related to the mismatched-decoding measure φᴹᴰ of Oizumi et al.
- Under a Gaussian assumption the infinite-dimensional Markov matrix is replaced by a 2n × 2n covariance matrix T, reducing computation of φ to polynomial time O(b³) for b variables, rather than doubly exponential (Markov matrix of size n = 2ᵇ, minimizing over ≈ N = 2ⁿ bipartitions).
- A graph-theory approximation visualizes the A-matrix as a directed graph, zeroes elements |A_ij| < ε, and uses connected-component analysis (complexity between O(n) and O(n²)) to find the cruelest-cut bipartition; in 7,000 simulations of n=16 it gives exactly the correct answer 95% of the time when Φ_max/Φ > 2 and 99.96% of the time when Φ_max/Φ > 3, overestimating true Φ by up to about 15% (median) when Φ_max/Φ ≲ 2.
- Three "improved" minimum-based measures vanishing for both afferent and efferent systems are constructed: Φ²·⁵ = min{φⁿᵃᵏ, φⁿᵖᵏ}, Φ²·⁵′ = min{φᵐᵃᵏ, φᵐᵖᵏ} (defined even for continuous variables), and Φ²·⁵″ = min{φᵒᵃᵏ, φᵒᵖᵏ}.
- For the example dynamics that merely swaps the two subsystems, noising gives Mᴬ = 1/n, q = 1/n² and p a Kronecker delta, yielding Φ²·⁵ = log₂ n; maximum integration grows logarithmically (∼ log₂ n) with subsystem size, and for random distributions none of the measures exceeds 1 − 1/(2 ln 2) ≈ 0.28 bits on average.

## Critical notes from the literature
- The author states explicitly that the analysis is focused only on integration, not on consciousness; a true measure of consciousness may involve additional requirements (e.g. IIT's cause-effect power, composition, exclusion postulates) that the paper does not consider, and notes Scott Aaronson's blog-post criticism of IIT's claim that integration is sufficient for consciousness.
- Measures based on the x-factorization (state known) vanish for any deterministic system: if dynamics are deterministic and x₀ is known, x₁ is also known so all entropies in φˣᵗᵏᵏ = I(x₁ᴬ,x₁ᴮ|x₀) vanish, giving φ = 0; the only source of integration is then correlated system-generated noise — described as a striking and arguably undesirable feature.
- φᴹ (and its time-reverse) is criticized (citing Oizumi et al. and Griffith) for being able to exceed the past-present mutual information I(x₀,x₁): e.g. a two-bit system evolving "00"→"00" or "11" with equal probability gives φᴹ = 1 bit even though I(x₀,x₁)=0, meaning φᴹ counts correlated random noise as integration — debatable whether this should count.
- The Earth-Movers distance d_EM (used by IIT3.0) rates poorly on tractability: its definition is a linear programming problem growing faster than quadratically with the number of system states (which grows exponentially in bits) and is formally infinite for continuous variables; consequently all the paper's recommended options except Φ³·⁰ and φᴹᴰ use the KL-divergence.
- The faster Φ-measures still leave open challenges the author flags: how to best handle asymmetric partitions (deliberately sidestepped), and practical issues hindering computation from real brain data including non-stationarity, statistical bias, overfitting from short data windows, and numerical instabilities.

## Key topics covered
Integrated information (Φ); Integrated Information Theory (IIT 2.0, 3.0); taxonomy of integration measures; Markov-process model of system evolution; tensor-factorization / "cruelest cut" bipartition; KL-divergence and alternative probability distances (L₁, L₂, Hilbert-space, Shannon-Jensen, Earth-Movers, mismatched decoding); noising vs optimal factorizations; afferent/efferent pathway vanishing; Barrett-Seth measure φᴮ; mismatched-decoding measure φᴹᴰ; stochastic interaction (Ay); Gaussian / continuous-variable closed-form formulas; autoregressive processes and Lyapunov equation; graph-theory approximation for polynomial-time Φ; consciousness and neural correlates of consciousness.
