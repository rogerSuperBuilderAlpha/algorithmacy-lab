---
citekey: aguilera2019integrated
title: Integrated information in the thermodynamic limit
authors: Aguilera, Miguel and Di Paolo, Ezequiel A.
year: 2019
doi: 10.1016/j.neunet.2019.03.001
arxiv: null
journal: Neural Networks
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1806.07879
sha256: bf23106840ab917e4cf1f09f5ee80b116bfd117a4170163ea2d2db46ec1d93d3
pdf_path: literature/pdfs/aguilera2019integrated.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how integrated information (Φ/φ) scales when systems become very large, a regime that the high computational cost of standard Integrated Information Theory (IIT) normally precludes. The authors introduce a kinetic Ising model of infinite size with quasi-homogeneous connectivity that admits an exact mean-field solution, and they define a simplified measure of integrated information φ (using the Wasserstein/earth mover's distance and a minimum information partition) that can be computed in this thermodynamic limit and over an arbitrary number τ of update steps. They show that, although integrated information is bounded over most of the parameter space, it diverges at certain critical points, so a system that must grow its integration as it scales has to be poised near criticality. Applying the measure to agent–environment couplings, they find that both a system and its system–environment compound can diverge together near a shared critical point, and the relative speed of divergence delimits the dominant integrated unit (the boundary between agent and environment). In a final model with internal self-regulation (tuned by a genetic algorithm plus Nelder–Mead), an agent generates a critical surface that preserves its integration across a range of environments. The work argues IIT must be modified—chiefly by not treating elements outside a mechanism as pure noise—to remain consistent in the thermodynamic limit.

## Key facts it relies on
- The base model is a kinetic Ising model of N binary spins with synchronous parallel discrete-time dynamics, update probability p(s_i(t)|s(t-1)) = e^{βs_i(t)h_i(t)} / (2cosh(βh_i(t))), with inverse temperature set to β = 1 without loss of generality.
- The infinite-size case takes local fields H_i = 0, divides the system into 1 to 3 regions, and uses homogeneous couplings J_ij = (1/N_R) J_SR, yielding an exact mean-field update m_S(t) = tanh(Σ_R J_SR m_R(t-1)).
- Integrated information φ_M(τ) of a mechanism M is defined as the Wasserstein (earth mover's) distance D between the system's behaviour and that of a system with a partition applied, computed after τ updates with noise injected at partitioned elements; IIT itself uses this same distance metric.
- The minimum information partition (MIP) is the partition with least difference from the original; in the quasi-homogeneous mean-field system, applying the MIP reduces to removing one connection between regions, and the MIP corresponds to whichever region's single-node isolation least affects future states.
- In the homogeneous single-parameter (J) model, φ_{M_N}(τ→∞) shows an apparent divergence around J = 1; near J→1^+ a Taylor expansion of tanh gives F_cut(m_0,τ→∞,x) = ±sqrt(3(J(1-x)-1)/(J(1-x))^3) and φ_{M_N}(τ→∞) = (1/2)|sqrt(3)(2J-3) / (2 sqrt(J^3(J-1)))|, confirming divergence as J→1^+.
- The integrated-information derivative is defined analogously to magnetic susceptibility in Ising models for identifying critical points, here differentiating the mean field along the parametric direction of the MIP.
- For a mechanism of size M as a fraction of N, φ_M(τ→∞) still diverges but is smaller than φ_{M_N} of the whole system, indicating the whole system is irreducible.
- In the asymmetric two-region (agent A, environment E) model with symmetric couplings J_AE = J_EA = J_c and J_AA = J_r, the system shows a pitchfork bifurcation; the critical point satisfies J_AA + J_AE J_EA = 2, and near (J_AA + J_AE J_EA)→2^+ both φ_A and φ_AE diverge, with their relative divergence (constants K_A, K_AE) determining which is the dominant integrated unit.
- The adaptive three-region (A, B, E) agent, with parameters tuned by a microbial genetic algorithm (τ = 10^4) then Nelder–Mead (τ = 10^5), reached J_AA = 0.09973671, J_AB = -0.85774049, J_BA = -0.8995672, J_BB = 0.14326043 (negative cross-weights, positive self-couplings), maintaining divergence of φ_AB across J_c in [-1.21, 1.21].

## Critical notes from the literature
- The authors stress IIT must be modified for the thermodynamic limit: treating elements outside the mechanism as unconstrained noise (as standard IIT does) creates an artifact that provokes spurious divergences at points other than the true critical point (Fig. B2), so they instead let outside elements operate normally.
- The approximation that applying the MIP equals removing one connection (injecting uniform noise equivalent to a zero mean field) is stated to be valid only when the system is infinite and τ > 1 (footnote 16/17).
- The authors acknowledge a key limiting assumption is the homogeneity of elements within each region; biological systems cannot be assumed so homogeneous, and heterogeneity (which can generate extended critical-like regions, cf. Griffiths phases) is left to future work.
- Results are limited to models with stationary solutions where the stable solution can be evaluated as the temporal span tends to infinity; more realistic systems with cyclic or chaotic dynamics could be harder to interpret though in principle tractable.
- The measure is a simplified version of IIT: it considers only effects (not causes), coincides mechanism and purview, and omits the second-level computation of integrated conceptual information Φ, justified by the homogeneity of the system (Appendix B).

## Key topics covered
Integrated Information Theory (IIT 3.0); integrated information φ and Φ; kinetic Ising model; mean-field approximation; thermodynamic limit; criticality and critical points; phase transitions and pitchfork bifurcation; minimum information partition (MIP); Wasserstein / earth mover's distance; magnetic susceptibility analogy; agent–environment boundaries and asymmetry; autonomy and individuality; self-organized criticality; adaptive self-regulation; genetic algorithm and Nelder–Mead optimization; regions of viability; consciousness and biological autonomy as motivations.
