---
citekey: marwan2002cross
title: Cross recurrence plot based synchronization of time series
authors: Marwan, Norbert and Thiel, Marco and Nowaczyk, Norbert R.
year: 2002
doi: 10.5194/npg-9-325-2002
arxiv: null
journal: Nonlinear Processes in Geophysics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://npg.copernicus.org/articles/9/325/2002/npg-9-325-2002.pdf
sha256: 3877857d49ffcf35784015e367502d55d498f4dcc4f5e572438a9e5b2a30b7e3
pdf_path: literature/pdfs/marwan2002cross.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper extends recurrence plots (RP) to cross recurrence plots (CRP), in which two time series are embedded in the same phase space and tested for mutual closeness, producing an N x M recurrence matrix. The authors observe that a CRP of two related-but-rescaled series contains a distorted "main diagonal" they call the line of synchronization (LOS), which encodes the rescaling (transfer) function between the two time scales. By non-parametrically fitting the LOS (using a simple two-step search algorithm given in the appendix), one can rescale one series' time axis to synchronize the two series, with no parametric assumptions about the underlying dynamics. They validate on a toy example (two sine functions whose time scales differ by a quadratic term, recovering the expected parabolic rescaling t = 0.01 t''^2) and on real rock-magnetic data from two Arctic Makarov Basin sediment cores (PS 2178-3 and PS 2180-2), comparing CRP synchronization against manual visual wiggle matching. The CRP-adjusted data show correlation coefficients with the reference of about 0.70-0.80 versus 0.71-0.87 for wiggle matching, but with less variation (smaller chi-squared), suggesting a more balanced, objective, automatic, multivariate adjustment.

## Key facts it relies on
- An RP is the N x N matrix R_{i,j} = Theta(epsilon - ||x_i - x_j||) (Eq. 1), where epsilon is a cutoff distance, ||.|| a norm (e.g. Euclidean), and Theta the Heaviside function; RPs were introduced by Eckmann et al. (1987).
- The CRP generalizes this to two trajectories: CR_{i,j} = Theta(epsilon - ||x_i - y_j||) (Eq. 2), an N x M array with x_i (i=1..N) from the first series and y_j (j=1..M) from the second; expansion follows Zbilut et al. (1998).
- Unlike the RP, the CRP generally has no main diagonal because (i,i)-states are not identical; if the series are merely rescaled versions of each other, a distorted diagonal (the LOS) appears that carries the rescaling information.
- For two sine functions f(t)=sin(phi t + alpha), g(t)=sin(psi t + beta), the LOS gives t2 = phi(t1) = (phi/psi) t1 + gamma with gamma=(alpha-beta)/psi (Eq. 12); the LOS slope is the frequency ratio and its ordinate intercept the phase difference.
- The method assumes the two systems are essentially the same dynamics up to a time rescaling (f = g up to a rescaling function); normalization by mean and standard deviation lets it handle observations differing by an affine transform f = a*fbar + b (Eqs. 7-8).
- Toy example: f(t)=sin(phi t), g(t)=sin(psi t^2) with psi = 0.01 phi; CRP used embedding dimension m=2, delay tau=pi/2, varying threshold for constant recurrence density 20%; recovered rescaling function t = phi(t'') = 0.01 t''^2.
- Real-data case: two Makarov Basin cores; PS 2178-3 (data length N=436) adjusted to PS 2180-2 (N=251); phase space built from six normalized rock-magnetic parameters (kappa_LF, ARM, kappa_ARM/kappa_LF, PJA, MDF_ARM, INC), with embedding m=3 and delay tau=1 giving an 18-dimensional phase space and recurrence criterion epsilon = 5% nearest neighbours.
- Results (Table 1): CRP-reference correlation coefficients ~0.70-0.80 vs. interactive wiggle-matching 0.71-0.87; total chi^2 deviation is 49.1 for CRP matching vs 141.4 for wiggle matching; data lengths N=170 (wiggle) and N=250 (CRP); the depth-depth-function differs by up to 20 cm from wiggle matching.
- The LOS-fitting algorithm (Appendix) grows a stepwise (w x w) sub-matrix to find the next recurrence point, then locates the center of mass of recurrence-point clusters; good LOS should maximize targeted points N1 and minimize gaps N0, with correlation correlating most strongly with the ratio N1/N0. Matlab code is at http://www.agnld.uni-potsdam.de/~marwan.

## Critical notes from the literature
- The authors stress that if f(.) != g(.) the method generally cannot decide whether differences are due to different dynamics or simple rescaling; the assumption of identical dynamics up to time rescaling is essential.
- Embedding is acknowledged as difficult: the Takens Embedding Theorem holds only for closed, deterministic, noise-free systems; for stochastic time series embedding is "in general, not justified," and a single embedding lag may be correct for one section but wrong for another in non-stationary data.
- The LOS-fitting algorithm is repeatedly described as "still not mature" / "weak"; some differences in the toy result are attributed to "meandering of the LOS" caused by partial weak embedding, and the authors flag future optimization of the LOS searching algorithm and study of dynamical noise.
- The authors note conspicuous similarity to Thompson and Clark's (1989) sequence slotting (both start from a distance matrix), distinguishing their approach by the recurrence threshold, fixed nearest-neighbour amount, and the ability to increase embedding dimensions; they explicitly do not provide a full comparison among alignment methods.
- Although CRP correlation values can be smaller than wiggle matching, they vary less, which the authors interpret as the human/interactive method not producing balanced adjustment while the automatic method does; they also note human eyes are usually better at assessing complex structures.

## Key topics covered
Cross recurrence plots (CRP); recurrence plots (RP); line of synchronization (LOS); time-series synchronization / rescaling; transfer/rescaling function; phase space embedding (Takens delay embedding); recurrence quantification analysis (RQA); sediment-core / rock-magnetic data alignment; wiggle matching; sequence slotting; geophysical/paleoclimate time-scale adjustment; nonlinear time series analysis.
