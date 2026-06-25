---
citekey: goldstein2026crqa
title: Cross-recurrence quantification analysis captures inter-brain coupling during naturalistic negotiation: a new dynamic approach for hyperscanning
authors: Goldstein, Bear M. and Burns, Shannon M. and Peck, Frances C. and Dale, Rick and Lieberman, Matthew D.
year: 2026
doi: 10.3389/fnins.2025.1713357
arxiv: null
journal: Frontiers in Neuroscience
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://public-pages-files-2025.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1713357/pdf
sha256: dea9b17886c3be9f38560503968740ae6d6d52f1f9b9d5e455dd77fad76bc2b5
pdf_path: literature/pdfs/goldstein2026crqa.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether dynamic, nonlinear, time-lagged patterns of inter-brain coupling during free-flowing negotiation relate to objective decision outcomes and subjective experiences of collaboration — patterns that conventional stationary synchrony measures may miss. The authors introduce cross-recurrence quantification analysis (CRQA), which treats two partners' neural signals as a coupled dynamical system and quantifies how their joint trajectories revisit similar states over time. fNIRS data were recorded from dyads (final N = 96 dyads for complete behavioral/neural/subjective data; 101 dyads with viable neural data) who jointly allocated a hypothetical \$100 million budget across five Zika-epidemic programs, with coupling measured in the medial prefrontal cortex (mPFC) and bilateral temporal parietal junction (TPJ). Three CRQA metrics restricted to a ±20 s band around the line of synchronization — Entropy (complexity), Delay (temporal offset), and Balance (symmetry of leading/lagging) — were correlated (partial Spearman, controlling for conversation length) with two behavioral measures and six subjective composites. CRQA revealed systematic associations: Balance was the strongest predictor (e.g., TPJ Balance with shared understanding r = 0.34, p = 0.006; mPFC Balance with cooperation r = 0.27, p = 0.046), Delay in TPJ was linked to motivation (r = 0.31, p = 0.014), and mPFC Entropy was linked to stance movement parity (r = 0.27, p = 0.043). By contrast, the conventional benchmarks inter-subject correlation (ISC) and wavelet transform coherence (WTC) showed no significant associations with any outcome. The authors conclude CRQA captures dynamic, nonlinear coupling overlooked by stationary methods and opens new approaches for naturalistic hyperscanning.

## Key facts it relies on
- CRQA is a nonlinear timeseries method that treats two interacting signals as a coupled dynamical system; a recurrence point R_ij = 1 if the Euclidean distance between embedded neural state vectors x_i and y_j is ≤ a dyad-specific radius ε, else 0.
- Standard CRQA parameters used: Euclidean distance metric, embedding dimension of 2, and minimum diagonal/vertical line length of 2; the recurrence threshold (radius) was calibrated per dyad and brain region to ~3.5% recurrence (within the recommended 2–5% range, citing Coco et al., 2025).
- Analysis was masked to recurrence within ±20 s of the main diagonal (line of synchronization) to focus on real-time conversational coordination and exclude distant temporal echoes; three focal metrics were normalized Entropy (rENTR), Delay, and Balance (a 0–1 symmetry scale).
- Sample: N = 229 participants (mean age 20.32, SD = 2.60), paired into 110 same-gender dyads (71 female–female, 39 male–male); after exclusions, 101 dyads had viable neural/subjective data and 96 dyads had complete behavioral, neural, and subjective data.
- Task: dyads allocated a hypothetical \$100 million across five Zika-epidemic programs; discussion durations ranged 180 s to 1868 s, mean 516.33 s (SD = 290.31); the design was modeled after Keltner and Robinson (1993).
- fNIRS used a NIRScout (NIRx) unit with 32 source and 32 detector optodes split across dyad members (35 channels per participant), over prefrontal cortex and bilateral TPJ via 10–10 positioning, wavelengths 760 nm and 850 nm, sampling rate 3.91 Hz; HbO timeseries were resampled to 1 Hz and z-scored. CRQA was run with the R package crqa (Coco and Dale, 2014; Coco et al., 2021, 2025).
- Key CRQA results (partial Spearman): mPFC Entropy–stance movement parity r = 0.27 (p = 0.043); mPFC Balance–total stance movement r = 0.25 (p = 0.046), Balance–cooperation r = 0.27 (p = 0.046), Balance–liking r = 0.27 (p = 0.048); TPJ Balance–shared understanding r = 0.34 (p = 0.006); TPJ Delay–motivation r = 0.31 (p = 0.014).
- Conventional benchmarks failed: ISC produced no significant correlations with any outcome; WTC showed only marginal, non-surviving associations (cooperation r = 0.18, unadjusted p = 0.079, adjusted p = 0.523; total stance movement r = 0.17, unadjusted p = 0.092, adjusted p = 0.324). ISC was computed per Hasson et al. (2004); WTC via MATLAB wcoherence in the 0.02–0.08 Hz band.
- Multiple-comparisons control used a Westfall–Young step-down max-statistic permutation procedure (1,000 permutations) within each neural-metric × predictor-family block (behavioral block = 4 tests; subjective block = 12 tests), at adjusted α = 0.05; questionnaire composites had Cronbach's α from 0.763 (shared understanding) to 0.847 (satisfaction).

## Critical notes from the literature
- The authors state this is the first application of CRQA to naturalistic brain-to-brain coupling and frame their hypotheses and results as preliminary/initial expectations; several additional associations (e.g., TPJ Determinism–satisfaction, mPFC Trapping time–partner quality) reached only marginal unadjusted significance and did not survive multiple-comparisons correction, and are reported "for completeness."
- Scope is limited to a cooperative budget-negotiation task with same-gender dyads of California university students; the authors note the Balance/Delay/Entropy signatures should be tested across other contexts such as competitive bargaining, creative brainstorming, and hierarchical leader–follower dynamics before generalizing.
- The authors chose conventional CRQA parameters (embedding dimension 2, ±20 s band, min line length 2) to facilitate comparability and explicitly flag that systematic parameter exploration (delay, embedding dimension, minimum line length, temporal band) is needed; results may depend on these choices.
- The behavioral and neural measures are correlational and dyad-level; the paper offers alternative interpretations for some effects (e.g., Delay–motivation could reflect more effortful deliberation or more intentional articulation of complex ideas), so causal/mechanistic claims are not established.
- ISC and WTC were included only as diagnostic benchmarks, not as primary outcomes; their null results contextualize CRQA's added sensitivity rather than constituting a formal head-to-head power-matched comparison.

## Key topics covered
- Cross-recurrence quantification analysis (CRQA) for hyperscanning
- Cross-recurrence plots, recurrence points, time-delay embedding, line of synchronization
- CRQA metrics: Entropy, Delay, Balance, Determinism, Laminarity, Trapping time
- fNIRS hyperscanning; HbO; default mode network; mPFC and bilateral TPJ ROIs
- Naturalistic negotiation / joint resource allocation task
- Inter-brain coupling, neural synchrony, brain-to-brain coupling
- Benchmark comparison vs inter-subject correlation (ISC) and wavelet transform coherence (WTC)
- Partial Spearman correlations; Westfall–Young step-down multiple-comparisons control
- Behavioral measures: total stance movement, stance movement parity
- Subjective composites: cooperation, partner quality, liking, motivation, shared understanding, satisfaction
- Social cognition, theory of mind, mentalizing, collaborative decision-making
