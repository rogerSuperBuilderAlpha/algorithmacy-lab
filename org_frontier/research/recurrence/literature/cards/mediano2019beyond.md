---
citekey: mediano2019beyond
title: Beyond integrated information: A taxonomy of information dynamics phenomena
authors: Mediano, Pedro A. M. and Rosas, Fernando and Carhart-Harris, Robin L. and Seth, Anil K. and Barrett, Adam B.
year: 2019
doi: null
arxiv: 1909.02297
journal: arXiv
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/1909.02297
sha256: a23c34890d7f9c34ea8a8d8860dd0ce08a7bdb4664d93f17ffcbc25071a79fdf
pdf_path: literature/pdfs/mediano2019beyond.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to characterise the variety of information-dynamics phenomena in interdependent multivariate time series, arguing that the standard view that causal interactions are intrinsically pairwise (single cause -> single effect, as in directed-graph / Granger-causality analyses) is too coarse and that one-dimensional measures of "dynamical complexity" or "integrated information" conflate qualitatively distinct effects. The method combines partial information decomposition (PID) with integrated information to produce Integrated Information Decomposition (ΦID), which decomposes the excess entropy E of a Markovian bivariate process into 16 atoms arranged on a "double-redundancy" product lattice built over forward (cause) and backward (effect) PIDs. From these atoms the authors propose an extended taxonomy of six disjoint information-dynamics phenomena (storage, copy, transfer, erasure, downward causation, upward causation), generalising Lizier's storage/transfer/modification view, and surface modes — notably upward causation and synergistic storage — that they say had not been previously reported. They show that mutual information and transfer entropy each conflate several atoms and miss synergistic-effect atoms entirely, and use ΦID to dissect four existing measures (ΦWMS, ψ, ΦG, and causal density CD), demonstrating each captures a different combination of atoms. ΦID also explains pathologies such as why whole-minus-sum Φ (ΦWMS) can go negative (a negative double-redundancy term) and why unnormalised causal density can exceed the total mutual information (double-counting of a downward-causation atom). The authors conclude that "integration" is an aggregate of heterogeneous phenomena and that no single scalar can fully capture dynamical complexity, while ΦID enables tailored, multi-dimensional measures.

## Key facts it relies on
- ΦID decomposes the excess entropy E = I(X1, X2; Y1, Y2) of a Markovian process, where X and Y are states at times t and t+1; it builds a forward PID (info from X1,X2 about future Y1Y2) and a backward PID (info from Y1,Y2 about past X1X2), tied to cause vs. effect information in IIT.
- The construction uses a product lattice over A × A, where A := {{1},{2},{1,2},{{1},{2}}}; this product lattice has 16 nodes (Fig. 2), giving 16 ΦID atoms computed as a linear (Moebius-inversion) transform over 16 redundancies via the recursion in Eq. (5).
- A double-redundancy function I∩^{α→β} is assumed to satisfy two axioms (compatibility — reducing to PID redundancy or mutual information when J=1 or K=1 — and partial ordering / monotonicity); Proposition 1 states the 16 atoms are uniquely determined once a single-target redundancy function Red(·) and the bottom atom I∂^{{1}{2}→{1}{2}} are specified (i.e. specifying the double-redundancy gives 15 atoms "for free").
- Proposed taxonomy has 6 disjoint phenomena: Storage, Copy, Transfer, Erasure, Downward causation, Upward causation — generalising Lizier's storage/transfer/modification (information modification) framework.
- Mutual information / transfer entropy limitation: in the transfer-entropy decomposition I(Xi; Yj | Xj) = I∂^{{12}→{1}{2}} + I∂^{{i}→{1}{2}} + I∂^{{12}→{j}} + I∂^{{i}→{j}}, only I∂^{{i}→{j}} is a "genuine" transfer term; standard methods cannot capture synergistic-effect atoms of the form I∂^{α→{12}}.
- Three example logic-gate systems (copy transfer, downward XOR, parity-preserving random PPR) all have ΦWMS = 1 yet differ in their only non-zero ΦID atom: transfer (I∂^{{1}→{2}}=1), downward causation (I∂^{{12}→{1}}=1), and synergistic storage (I∂^{{12}→{12}}=1) respectively (Fig. 3).
- ΦWMS = I(X1,X2;Y1,Y2) − I(X1;Y1) − I(X2;Y2) (Eq. 9); ΦID shows it includes the negative of the bottom double-redundancy atom, so highly redundant systems can give negative ΦWMS; a corrected measure ΦWMS,c := ΦWMS + I∂^{{1}{2}→{1}{2}} is proposed and computed for a noisy-AND system with correlated noise (Fig. 4), where ΦWMS,c tends to 0 at high noise correlation.
- Unnormalised causal density uCD = I(X1;Y2|X2) + I(X2;Y1|X1) double-counts the atom I∂^{{12}→{1}{2}} (appears with coefficient 2), which lets uCD exceed the total mutual information; example x1,x2 max-entropy with y1=y2=x1⊕x2 gives uCD = 2 bit > I(X1,X2;Y1,Y2) = 1 bit.
- Table I tabulates, for each measure (Φ/ΦWMS, CD, ψ, ΦG), whether it is positive (+), negative (−), or 0 when a single ΦID atom is the only non-zero atom, showing the four measures capture different atom combinations.

## Critical notes from the literature
- The paper states ΦID inherits PID's limitations: several distinct redundancy functions exist for evaluating PID atoms and there is no consensus on a universally preferable one (citing James et al.); forthcoming work is said to address redundancy-function selection.
- Scope is restricted to bivariate (two-variable) systems with Markovian dynamics; the authors explicitly leave extensions to processes with memory (non-Markovian / non-trivial excess entropy) for future work.
- For results to be interpreted in a strict causal (rather than dynamical) sense, additional assumptions must hold: p(Y|X) must equal a Pearl do()-distribution and the system must satisfy faithfulness and the causal Markov condition.
- The authors frame their work as a response to prior findings (Refs. cited as [9–11], esp. [10]) that existing Φ / causal-density measures behave inconsistently both in practice and "in principle"; ΦID is offered as an explanatory dissection rather than a single replacement measure, and they argue (following Feldman and Crutchfield) there is no theoretical basis for an all-encompassing scalar complexity measure.

## Key topics covered
Integrated Information Decomposition (ΦID); partial information decomposition (PID); redundant/unique/synergistic information; redundancy lattice and product (double-redundancy) lattice; Moebius inversion / atoms; excess entropy; forward vs. backward (cause/effect) decomposition; integrated information theory (IIT) and Φ measures; whole-minus-sum Φ (ΦWMS) negativity; causal density (CD/uCD); transfer entropy and mutual information limitations; Lizier's information storage/transfer/modification; taxonomy of storage, copy, transfer, erasure, upward and downward causation; synergistic storage; logic-gate examples (copy, XOR, PPR, noisy AND); causal vs. dynamical analysis; faithfulness and causal Markov conditions.
