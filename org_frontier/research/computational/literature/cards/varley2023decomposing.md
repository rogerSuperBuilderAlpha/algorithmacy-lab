---
citekey: varley2023decomposing
title: Decomposing past and future: Integrated information decomposition based on shared probability mass exclusions
authors: Varley, Thomas F.
year: 2023
doi: 10.1371/journal.pone.0282950
arxiv: null
journal: PLOS ONE
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:publisher
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0282950&type=printable
sha256: 2220589bb6fdd9820de51ecd2faa779a2892aedf0301d1b381ad28fb472712ba
pdf_path: literature/pdfs/varley2023decomposing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to compute the integrated information decomposition (ΦID/"FID") of a dynamical system, which decomposes the excess entropy (total information flowing from a system's past to its future) into non-overlapping "atoms" describing how elements and ensembles of elements store, transfer, and modify information, but which lacks an operational definition of multivariate (double) redundancy needed to compute values from data. Varley proposes a new multi-target temporal redundancy function, Iτsx, by generalizing the single-target redundancy measure Isx of Makkeh et al. (based on the logic of local probability mass exclusions) to multiple sources and multiple targets. The measure is localizable (yielding a value per configuration/moment), avoids arbitrary thresholds and non-differentiable min/max functions, satisfies Mediano et al.'s compatibility criterion (reducing to the classic PID when one side is univariate), and can be rewritten as a sum/difference of "union entropy" terms hsx that separate static instantaneous structure from dynamic transition structure. Varley demonstrates the decomposition on three constructed two-element Boolean Markov systems (disintegrated, integrated, heterogeneous) and on spontaneous spiking recorded from 31 dissociated rat cortical cultures, computing 16 ΦI atoms per neuron pair. Across cultures, element-wise information storage atoms had the highest normalized value (0.417 ± 0.422) and were strongly negatively correlated with the whole-minus-sum integrated information ΦWMS (Spearman ρ = −0.8), while information transfer atoms were the strongest positive correlate (ρ = 0.57). A time-resolved (local) analysis of neuronal avalanches found that information atoms are "front-loaded," with most non-trivial information dynamics occurring before the first half of the avalanche/cascade completes.

## Key facts it relies on
- The excess entropy E(X) = I(X−∞:t ; Xt:∞) measures total past-to-future statistical dependency; for Markovian systems it reduces to the lag-τ mutual information between a moment and its immediate past, E0(X) = I(X−τ; Xt) (Eq 2).
- Iτsx generalizes Makkeh et al.'s single-target Isx measure (PLOS ONE), built on Finn & Lizier's interpretation of local mutual information as exclusions of probability mass; it was chosen because it links information sharing to formal logic, requires no arbitrary thresholds (unlike Iccs) nor non-differentiable min/max functions (unlike Immi / I±), and is localizable.
- Iτsx can be rewritten as itsx(α→β) = hsx(α) + hsx(β) − hsx(α∩β), where hsx(α) = log2(1/P(a1 ∪ … ∪ ak)) is a "union entropy"; the first two terms capture static instantaneous structure at t−τ and t, and the hsx(α∩β) term captures the dynamic transition structure (negativity of iτsx occurs when transition structure exceeds the instantaneous structures).
- The framework follows Mediano et al.'s ΦID, which builds a product lattice A² = A × A; the double-redundancy function must satisfy a compatibility axiom (reducing to a single-target redundancy / ordinary mutual information when |X| = 1 or |Y| = 1) and a partial-ordering criterion consistent with the lattice.
- Three synthetic two-element binary Markov systems were used: disintegrated (E(X) = E(X1)+E(X2) = 2 bit), integrated (parity-check, E(X) = 1 bit while each E(Xi) = 0 bit), and heterogeneous (transition probabilities drawn from N(0,1) per Varley & Hoel; whole excess entropy 0.422 bit vs element temporal mutual informations 0.017 and 0.001 bit). The heterogeneous system had 11 informative vs 5 misinformative ΦI atoms; Table 1 reports all 16 atom values for each system.
- Empirical data: 31 dissociated cultures of rat cortex; spontaneous activity recorded on 60-electrode arrays (8×8, 200 μm spacing, 30 μm diameter) at 20,000 Hz for ~1 hour, spike-sorted with wave_clus, rebinned to 3 ms bins; lag-1 excess entropy computed per node pair within avalanches, with full ΦID performed only when excess entropy was significant at α = 10⁻⁶ (Bonferroni corrected).
- Across all cultures, normalized element-wise information storage atoms ({x}→{x}) had the highest mean (0.417 ± 0.422), followed by element-wise transfer ({x}→{y}, 0.097 ± 0.195); information copy and erasure atoms ({x}→{1}{2}, {1}{2}→{x}) each averaged 0.011 ± 0.0325; every atom was on average positive (informative).
- Spearman correlations with ΦWMS (Balduzzi & Tononi whole-minus-sum integrated information): storage atoms ρ = −0.8, transfer atoms ρ = 0.57, double-synergy {12}→{12} ρ = 0.41 (all p < 10⁻⁶, Bonferroni corrected).
- Local avalanche analysis aggregated avalanches of length k > 4 (≥ 50 instances required); cumulative information profiles climb much faster than spike accumulation, with excess entropy "almost entirely saturated before halfway through the avalanche," and front-heaviness more pronounced for larger avalanches.

## Critical notes from the literature
- Scope limitation acknowledged: Iτsx is only well-defined for discrete random variables (inherited from Isx); continuous generalization remains active research, and prior continuous PID/ΦID work on fMRI or cardiac data used Gaussian redundancy measures that lack intuitive interpretation, are non-localizable, or require thresholds/optimizations.
- Scalability is severe: the PID lattice has D(k)−2 atoms (Dedekind numbers), and the ΦID lattice grows as (D(k)−2)² — a five-element system yields a lattice of 57,471,561 elements — making complete decomposition of large natural systems infeasible; heuristics like ΦWMS and O-information are noted as efficient but imprecise alternatives.
- The author notes that, unlike single-target Isx, Iτsx cannot inherit provable properties such as global non-negativity of its informative/misinformative components because the ΦID lattice lets single sources appear multiple times; he suggests a return to the mathematical foundations and new desiderata may be needed.
- Negative local atoms are pervasive and hard to interpret (e.g., negative "stored" partial information {2}{2} despite a non-negative active information storage I(S²−τ; S²t) = 0.001 bit); the author's contextual interpretation (information actually arising from interaction with other elements) is explicitly described as "speculative," and the local avalanche findings are framed as qualitative and requiring replication.
- No operational/biological mechanism is established for the more exotic atoms (copy, erasure, downward/upward causation); the avalanche profile findings (e.g., the S-shaped double-synergy profile) are flagged as "well worth revisiting and replicating in a future data set."

## Key topics covered
Integrated information decomposition (ΦID/FID); partial information decomposition (PID, Williams & Beer); redundancy/synergy/unique information; excess entropy; multi-target temporal redundancy; local information theory; probability mass exclusions (Finn & Lizier); shared-exclusions redundancy Isx (Makkeh et al.); union entropy hsx; partial information lattice and Möbius inversion; information storage/transfer/copying/erasure, causal decoupling, upward/downward causation; whole-minus-sum integrated information ΦWMS (Balduzzi & Tononi); Boolean Markov systems; dissociated neural cultures; neuronal avalanches and criticality; Dedekind-number scaling.
