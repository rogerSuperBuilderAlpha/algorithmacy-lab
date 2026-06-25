---
citekey: mayner2018pyphi
title: PyPhi: A Toolbox for Integrated Information Theory
authors: Mayner, William G. P. and Marshall, William and Albantakis, Larissa and Findlay, Graham and Marchman, Robert and Tononi, Giulio
year: 2018
doi: 10.1371/journal.pcbi.1006343
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1006343&type=printable
sha256: 1e55c0fca745c3518ec046b9b277c0e430c20e6ea572ea21dceb7ec01ae0f85d
pdf_path: literature/pdfs/mayner2018pyphi.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a PLOS Computational Biology software paper introducing PyPhi, a Python package that implements the mathematical framework of integrated information theory (IIT) for causal analysis. The software unfolds the full cause-effect structure (CES) of discrete Markovian dynamical systems of binary elements and computes the system's integrated information Φ. The authors first give an overview of the main algorithm by reproducing results from an example system (a three-node deterministic logic-gate network of OR, AND, and XOR gates), then describe the design and implementation, including TPM representations, calculation of cause/effect repertoires, and optimizations/approximations. The algorithm proceeds through the IIT postulates at both the mechanism level (information, integration via minimum-information partitions, exclusion via maximally-irreducible cause/effect) and the system level (system cuts, irreducible CES, complexes). PyPhi is open-source under GPLv3, installable via `pip install pyphi` on Linux and macOS with Python 3.4 or higher, with code hosted on GitHub and a web-based interface available online. The main limitation is that the algorithm is exponential in the number of nodes, limiting practical analysis to roughly 10-12 nodes.

## Key facts it relies on
- IIT posits five requirements ('postulates') for a substrate of consciousness: intrinsic existence, composition, information, integration, and exclusion; PyPhi's algorithm is organized around these postulates.
- The main measure of cause-effect power, integrated information (Φ), quantifies how irreducible a system's CES is to those of its parts; φ (lowercase) measures the integrated information of a single mechanism-purview pair.
- PyPhi can analyze both deterministic and stochastic discrete Markovian dynamical systems consisting of elements with two states; a system S is completely specified by its transition probability matrix (TPM).
- The software has two primary functions: `pyphi.compute.major_complex()`, which returns a `SystemIrreducibilityAnalysis` object, and `Subsystem.concept()`, which outputs `Concept` objects making up the CES.
- For the worked example system, Φ = 1.92 (computed as `sia.phi` = 1.916665), and the minimal partition removes the causal connections from AB to C (`Cut [A, B] --/ /--> [C]`); the whole system ABC is the major complex.
- The algorithm requires the conditional independence (Markov) property: Pr(S_{t+1} | S_t = s_t) = ∏ over nodes Pr(N_{t+1} | S_t = s_t) (Eq 1); IIT imposes a uniform (interventional/causal, not observed) marginal distribution over previous states.
- PyPhi supports three TPM representations: 2-dimensional state-by-node, multidimensional state-by-node, and state-by-state; state-by-node is canonical and uses 2^n × n entries instead of 2^n × 2^n. States are mapped to row indices in lexicographical order using a little-endian convention (first node = least-significant bit), so state (0,0,0,1) maps to index 8.
- Effect and cause repertoires are derived from the TPM by conditioning and marginalizing (Eqs 2-5); the cause repertoire applies Bayes' rule with a uniform marginal over previous states and is normalized via a factor K. Repertoires over multi-element purviews are computed as tensor products implemented with `numpy.multiply()`.
- PyPhi exploits an analytical solution to the earth mover's distance (EMD) between effect repertoires: the general EMD has time complexity O(n·2^{3n}), but for independent distributions the EMD equals the sum of EMDs over individual node marginals with complexity O(n), usable for half of all repertoire calculations.
- Two optional approximations are provided (disabled by default): `CUT_ONE_APPROXIMATION` (evaluates only 2n bipartitions severing a single node, giving an upper bound on Φ) and `ASSUME_CUTS_CANNOT_CREATE_NEW_CONCEPTS` (the "no new concepts" approximation, which provides neither a theoretical upper nor lower bound).

## Critical notes from the literature
- The authors state PyPhi's main limitation explicitly: the algorithm is exponential time in the number of nodes, O(n·53^n), limiting practical analysis to ~10-12 nodes. Reported runtimes for the exact major complex of three, five, and seven stochastic majority gates were ~1 s, ~16 s, and ~2.75 h respectively (parallel evaluation, 32 × 3.1GHz CPU cores); the "cut one" approximation reduced these to ~1 s, ~12 s, and ~0.63 h.
- The analysis can only be meaningfully applied to a system that is Markovian and satisfies conditional independence; the authors note these assumptions are reasonable for a causal TPM derived via the calculus of perturbations but are not guaranteed for TPMs derived from observed time series (e.g., EEG recordings), and should be carefully checked in novel contexts.
- Providing an incorrect connectivity matrix (CM) can result in inaccurate output; if no CM is given, PyPhi assumes full connectivity, which guarantees correct results but is slower.
- The current version assumes the `Network` represents the system at the single spatiotemporal scale at which Φ is maximized; a module for calculating Φ over multiple spatial/temporal scales (theoretically required by the exclusion postulate) and a module for "actual causation" were listed as future/preliminary work at time of publication.

## Key topics covered
Integrated information theory (IIT); integrated information Φ and φ; cause-effect structure (CES); cause/effect repertoires; mechanisms and purviews; minimum-information partition (MIP); maximally-irreducible cause (MIC) and effect (MIE); concepts and complexes; major complex / MICS; transition probability matrix (TPM) representations (state-by-node, state-by-state); little-endian state indexing; conditional independence / Markov property; connectivity matrix optimizations; earth mover's distance (EMD) analytical solution; cut-one and no-new-concepts approximations; Python/NumPy implementation; object-oriented API design; GPLv3 open-source distribution.
