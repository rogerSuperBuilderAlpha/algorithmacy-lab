---
citekey: danilczuk2026integrate
title: The Integrated Information {$\Phi$} of an Integrate and Fire Network
authors: Danilczuk, Zuzanna and Pokropski, Marek and Suffczynski, Piotr
year: 2026
doi: 10.1371/journal.pcbi.1014085
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: plos-template
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pcbi.1014085&type=printable
sha256: f22fba42126eba7486bb2b1237e97a5fc31939c8454622f421bfe3783af13a2f
pdf_path: literature/pdfs/danilczuk2026integrate.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper applies Integrated Information Theory (IIT version 3.0) to a small simulated network of artificial integrate-and-fire (IAF) neurons to test how much integrated information (Φ) such a biophysically-motivated network can carry. The authors first validate their pipeline by configuring three connected IAF neurons to emulate the OR-AND-XOR logic-gate (ABC) system from the PyPhi literature, reproducing the published Φ values, then systematically vary the membrane time constant (τ) and connection weights (wᵢ) to map Φ across network states. They report three main empirical findings: a network of IAF neurons can possess non-zero Φ under certain conditions; the complexity of the network's dynamics does not correlate with its Φ value; and the amount of integrated information tends to grow with the IAF neurons' time constant, reflecting their integrative capacity. Finally, adding internal random (Poisson) fluctuations to one neuron shows that the IIT 3.0 Φ measure is not resilient to noise, with relative changes in Φ ranging from -400% to 420%, though averaging over parameters and states reveals only a weak dependence on the overall noise level. The authors conclude IIT can in principle be applied to a real-ish neuronal system, but emphasize key limitations of applying the theory to realistic, noisy, continuous neuronal models.

## Key facts it relies on
- The study uses IIT version 3.0; Φ is computed with the PyPhi Python library via `pyphi.compute_phi()`, with a network specified by a Transition Probability Matrix (TPM) and a Connectivity Matrix (CM); a custom TPM-calculation script is shared at github.com/mdanilczuk/IITfire.
- Pipeline validation: three IAF neurons with membrane time constant τ = 1Δt, all weights = 50 mV, V_rest = 0 mV, and selected thresholds emulate logic gates and reproduce the ABC-system Φ values from PyPhi (Table 1); e.g., state (0,0,0) gives Φ = 0.66667 (visual interface) vs 0.666668 (IAF network), and (1,0,0) gives 1.91667 vs 1.916665.
- The three-neuron IAF network was reduced to 2³ = 8 binary states (spike = '1', all other membrane potentials = '0'), giving an 8×8 TPM; in the noise case treated as a 4-element network the CM had 4² possible connections and the TPM 2⁴ states.
- Parameter sweep: τ varied from 1Δt to 8Δt in steps of Δt; wᵢ varied from 0 to 100 mV in steps of 12.5 mV; for the logic-gate emulation τ = 1Δt and wᵢ = 50 mV.
- Φ is zero at the lowest (12.5 mV, 25 mV) and highest (100 mV) weight values; the intermediate 37.5-87.5 mV range is the network's 'working range' where Φ is mostly non-zero; for τ = 1Δt and wᵢ in 50-87.5 mV all Φ values are constant.
- Mean Φ across states shows an increasing trend in Φ as τ increases, especially for τ > 2Δt with wᵢ in 62.5-87.5 mV; the membrane time constant τ governs how quickly information about the previous state and inputs decays over one time step, i.e., the neuron's integrative properties.
- The IAF neuron is governed by Equation (1): V_m(t) = V_m(t-1) + (Δt/τ)(V_rest - V_m(t-1)) + Σᵢ wᵢ Inputᵢ(t-1); with τ = 1Δt this simplifies to V_m(t) = V_rest + Σᵢ wᵢ Inputᵢ(t-1) (Equation 2), allowing neurons to act as logic gates.
- Spike thresholds (Table 2): OR uses V_m ≥ 50 mV, AND uses V_m ≥ 100 mV (2-input) or ≥ 150 mV (3-input), XOR uses 50 ≤ V_m < 100 mV; all weights 50 mV, V_rest = 0 mV, τ = Δt for logic-gate emulation.
- Noise analysis: a homogeneous Poisson process (states '0'/'1', rate λ) was added to the OR neuron; tested mean spike interval 1/λ ranged 2Δt-33Δt; simulation duration was increased from 200 to 1000 steps. When noise was a fourth feedforward element, Φ was always zero; when noise modified the OR neuron's state internally (still 3 elements), Φ changed, with maximal relative increase 420% at a mean Poisson interval of 3Δt (Fig 4).
- Membrane potentials are represented as 64-bit floating-point numbers; spanning 0-100 takes more than 2⁶² distinct numbers, so a fine-grained TPM is infeasible, motivating the binary spike/no-spike discretization (a two-step post-hoc coarse-graining approach).

## Critical notes from the literature
- The authors acknowledge IIT has been subject to strong criticism, including charges of implying a limited form of panpsychism, objections to the axioms, and concerns about the testability of IIT's predictions (refs 5-8).
- Limitations the authors raise: the two-step coarse-graining (high-resolution simulation then binary spike/no-spike discretization) may violate the Markov property for τ > 1Δt, since identical binary states ('no spike') can correspond to different membrane potentials, so the conditions under which the approach is valid remain to be determined.
- Small network size (only three neurons) makes the system prone to synchronization or trivial periodic dynamics; for coupling weight 100 mV the network converges within a single step, and for weights ≤ 37.5 mV activity decays within a few steps.
- The external-noise-as-internal-mechanism workaround is flagged as a tension with IIT 3.0 (where background conditions are fixed external constraints, not Poisson sources); the noise results are described as preliminary, since random spikes were added only to the OR neuron, and the authors note IIT 4.0 already addresses some IIT 3.0 limitations (incorporating degree of noise/determinism; refs 35).
- The authors note applying IIT to biophysical models like Hodgkin-Huxley is more challenging: preserving the Markov property would require the full state (V, m, h, n) plus synaptic variables, giving 2^15 × 2^15 TPM size for three HH neurons vs the much smaller three-IAF TPM; they also caution that the time-constant and noise findings may be specific to the OR-AND-XOR network analyzed.
- The authors stress that non-zero Φ does not imply such networks are conscious, citing Tononi and Koch that consciousness is an intrinsic property of physical systems and cannot exist within virtual or simulated environments.

## Key topics covered
Integrated Information Theory (IIT 3.0); integrated information Φ and Φ^max; integrate-and-fire (IAF) / leaky IAF neuron model; PyPhi library; Transition Probability Matrix (TPM) and Connectivity Matrix (CM); logic-gate (OR-AND-XOR / ABC) emulation; membrane time constant (τ) and connection-weight (wᵢ) parameter sweep; Markovian condition and conditional independence; coarse-graining / discretization of continuous state space; Poisson noise and robustness of Φ; network complexity vs Φ; consciousness and panpsychism critiques; comparison to Hodgkin-Huxley models; IIT 4.0.
