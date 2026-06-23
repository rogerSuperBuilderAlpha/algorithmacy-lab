# Recurrence Plot Foundations and RQA Measures
<!-- run: 2026-06-23 | sources: 12 -->
Search method: academic search (Consensus, Scholar Gateway) plus WebSearch/WebFetch DOI verification; run 2026-06-23.

The recurrence plot (RP) was introduced as a graphical device for visualizing the recurrence of states of a dynamical system in reconstructed phase space, marking pairs of times whose trajectory points fall within a threshold distance (Eckmann, Kamphorst & Ruelle, 1987). The construction rests on phase-space reconstruction by time-delay embedding, so a single observed time series yields a square binary recurrence matrix whose texture encodes deterministic and stochastic structure (Marwan & Webber, 2015). Early RPs were read qualitatively: diagonal lines parallel to the line of identity signal deterministic, predictable dynamics, while isolated points and broken structure indicate stochasticity or fast transitions.

Quantification converted these visual textures into scalar measures. Zbilut and Webber derived embeddings and delays from recurrence structure and proposed the first quantifiers (Zbilut & Webber, 1992), formalized as recurrence quantification analysis (RQA) for physiological signals (Webber & Zbilut, 1994). The diagonal-line family includes the recurrence rate (RR, the density of recurrence points), determinism (DET, the fraction of recurrence points lying on diagonal lines), the average and maximal diagonal line lengths, divergence, and Shannon entropy of the line-length distribution. DET and line statistics track predictability and the inverse of the largest Lyapunov exponent. A second family, based on vertical structures, was added to capture laminar dynamics: laminarity (LAM, the fraction of points forming vertical lines) and trapping time (the mean vertical line length), which detect intermittency and chaos–chaos transitions invisible to diagonal measures alone (Marwan, Wessel, Meyerfeldt, Schirdewan & Kurths, 2002). The comprehensive synthesis of RPs, RQA, and their dynamical-invariant interpretation remains the standard reference (Marwan, Romano, Thiel & Kurths, 2007), with tutorial treatments aimed at practitioners (Goswami, 2019) and explicit mathematical/computational foundations (Marwan & Webber, 2015).

Interpretation carries known hazards. Embedding parameters, threshold choice, and noise distort diagonal and vertical statistics, inflating DET and LAM through thickened or broken lines, motivating careful parameter selection and surrogate testing (Marwan, 2011). Recent work refines the theoretical grounding of the quantifiers: DET is linked to "recurrence triangle" motifs that separate deterministic chaos from stochasticity measure-theoretically (Hirata & Shiro, 2023), and the density-based measures DET and LAM are reframed through recurrence microstates, recovering diagonal and vertical line histograms from small submatrices (da Cruz, Prado, Lopes, Marwan & Kurths, 2025). A survey of the past decade catalogs alternative recurrence definitions, new transition and causality quantifiers, correction schemes, and couplings to machine learning (Marwan & Kraemer, 2023). The trajectory of the field moves the core quantifiers from heuristic descriptors toward measures with explicit dynamical-systems interpretation.

## References
- da Cruz, F. E. L., Prado, T. L., Lopes, S. R., Marwan, N., & Kurths, J. (2025).
- Eckmann, J.-P., Kamphorst, S. O., & Ruelle, D. (1987).
- Goswami, B. (2019).
- Hirata, Y., & Shiro, M. (2023).
- Marwan, N. (2011).
- Marwan, N., & Kraemer, K. H. (2023).
- Marwan, N., Romano, M. C., Thiel, M., & Kurths, J. (2007).
- Marwan, N., & Webber, C. L. (2015).
- Marwan, N., Wessel, N., Meyerfeldt, U., Schirdewan, A., & Kurths, J. (2002).
- Webber, C. L., & Zbilut, J. P. (1994).
- Zbilut, J. P., & Webber, C. L. (1992).
