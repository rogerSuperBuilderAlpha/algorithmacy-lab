---
citekey: kim2018estimating
title: Estimating the Integrated Information Measure Phi from High-Density Electroencephalography during States of Consciousness in Humans
authors: Kim, Hyoungkyu and Hudetz, Anthony G. and Lee, Joseph and Mashour, George A. and Lee, UnCheol
year: 2018
doi: 10.3389/fnhum.2018.00042
arxiv: null
journal: Frontiers in Human Neuroscience
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fnhum.2018.00042/pdf
sha256: a316cb040856f7d31da8f3de2fe84c0a78afc61bdd9a6ec0daab85e3463b1c81
pdf_path: literature/pdfs/kim2018estimating.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether integrated information (Φ), the central measure of integrated information theory (IIT), can be practically estimated from high-density EEG and whether it tracks levels of consciousness in humans. Because computing exact Φ for a 128-channel EEG would require searching ~1.8×10^38 bipartitions to find the minimum information partition (MIP), the authors introduce a tractable surrogate: a mean integrated information (denoted Φ̄) estimated by averaging Φ over many small, randomly and globally sampled subsets of EEG channels (8 channels per sample unit, 600 sample units), using Barrett and Seth's auto-regressive estimator (Φ̂_AR) for non-Gaussian continuous time series. They reanalyzed 128-channel EEG from 19 healthy volunteers across states induced by ketamine and by propofol-isoflurane (baseline, sedation/sub-anesthesia, general anesthesia, burst suppression, recovery). They find that Φ̄ is not simply reduced with loss of consciousness; instead different anesthetics produce complex, frequency-band-specific configurations of Φ̄, power, and connectivity. Only the alpha band showed consistently decreased Φ̄ in both anesthetics, and only the deep-anesthesia suppression period had near-zero Φ̄ across all bands. Φ̄ alone was insufficient to discriminate all anesthetic states, but a four-dimensional parameter space combining Φ̄-related and EEG-connectivity measures differentiated all states of consciousness.

## Key facts it relies on
- Exact Φ for 128-channel EEG is computationally infeasible: the number of possible bipartitions is sum_{k=1}^{64} C(128,k) ≅ 1.8×10^38.
- The surrogate mean integrated information Φ̄ was estimated from 600 sample units of 8 randomly/globally sampled EEG channels each; for 8 channels the number of possible bipartitions is sum_{k=1}^{4} C(8,k) = 162.
- Regional Φ̄ (Φ̄_R) for each of the 96 retained EEG channels was estimated from 30 sample units of 8 channels including that channel.
- Φ̄ is defined (Eq. 8) as the mean MIP-based Φ over sample units minus the median Φ of randomly shuffled (surrogate) 20-EEG datasets, so it reflects integrated information surpassing spurious integration.
- Reliability: with 600 sample units (k=600) the coefficient of variance of Φ̄ over 300 iterations was <0.01 (i.e., <1% of the mean); for Φ̄_R, k=30 sample units gave a coefficient of variance <0.05.
- 19 subjects, 128-channel HydroCel nets, EEG digitized at 500 Hz; 32 lower face/head channels removed leaving 96 channels; clean 2-min epochs per state segmented into 6-s epochs; five frequency bands used (delta 0.1–4 Hz, theta 4–8 Hz, alpha 8–13 Hz, beta 13–25 Hz, gamma 25–45 Hz).
- Φ was estimated with Barrett and Seth's (2011) auto-regressive Φ̂_AR (substituting linear-regression prediction error for covariance), applicable to non-Gaussian continuous time series; functional connectivity used weighted Phase Lag Index (wPLI) with a 0.35 threshold after subtracting the median wPLI of 20 surrogate shuffled datasets.
- Result: only the alpha band showed consistently decreased Φ̄ in both ketamine and propofol-isoflurane; only the suppression period in deep anesthesia had Φ̄ approaching zero in all frequency bands.
- Strong negative correlation between Φ̄ and the number of network modules in the alpha band (R = −0.87, p = 0.0045); theta, alpha, and beta bands showed significant negative correlations (R = −0.78, −0.87, −0.78, p < 0.05), while delta and gamma did not.
- Burst suppression was separated into burst and suppression periods using a burst suppression ratio (BSR) of 0.3; 20 burst suppression epochs (each >10 s) were used from the 5 of 9 isoflurane subjects who showed burst suppression; bursts occupied ~20% of deep anesthesia.

## Critical notes from the literature
- The authors only interpret relative changes of Φ̄ referenced to baseline, not absolute Φ, because scalp EEG is superficial and spatially imprecise and cannot capture the true Φ of the brain.
- They acknowledge Barrett and Seth's algorithm (Φ̂_AR) can fail to satisfy the theoretical upper/lower bounds of Φ; Oizumi et al. (2016a) pointed out this theoretical problem, and Oizumi's own "mismatched decoding" alternative (Φ*) is itself subject to a Gaussian-assumption limitation. The random channel selection is argued to reduce correlated (volume-conduction) noise.
- Φ̄ alone could not discriminate all anesthetic states; the large Φ̄ of some frequency bands during general anesthesia and relatively low Φ̄ during recovery do not match the IIT-based prediction that Φ should track consciousness.
- The high Φ̄ during EEG bursts (similar to or larger than wakefulness) complicates interpretation: bursts are hypersynchronous with high spatial integration but low differentiation/temporal integration (Li et al., 2013), so time-averaging over burst suppression conflates active and electrocortically silent segments; the authors argue Φ and related variables are only meaningful if burst and suppression are estimated separately.
- It remains an open question (Mudrik et al., 2016) whether Φ measures specifically conscious integration or also unconscious integration; recovery of responsiveness occurred without full recovery of integrated information, suggesting a possible integration threshold.

## Key topics covered
Integrated information theory (IIT); Φ / integrated information estimation; minimum information partition (MIP); effective information; Barrett–Seth auto-regressive Φ (Φ̂_AR); empirical/Markovian/mismatched-decoding Φ variants; mean integrated information Φ̄ via random channel subsampling; regional Φ̄_R topography; high-density (128/96-channel) EEG; ketamine, propofol, isoflurane anesthesia; states of consciousness (baseline, sedation, anesthesia, burst suppression, recovery); burst suppression ratio; EEG spectral power across delta/theta/alpha/beta/gamma; weighted Phase Lag Index (wPLI) functional connectivity; graph-theoretic network analysis (node degree, modularity); multi-dimensional parameter space for consciousness; linear mixed-effects model statistics.
