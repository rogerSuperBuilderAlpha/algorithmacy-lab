---
citekey: wallot2016mdrqa
title: Multidimensional Recurrence Quantification Analysis (MdRQA) for the Analysis of Multidimensional Time-Series: A Software Implementation in MATLAB and Its Application to Group-Level Data in Joint Action
authors: Wallot, Sebastian and Roepstorff, Andreas and M{\o}nster, Dan
year: 2016
doi: 10.3389/fpsyg.2016.01835
arxiv: null
journal: Frontiers in Psychology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01835/pdf
sha256: 4beab78ff9990ad3c7df8c9949552d3c2bde74f9a97895250bb54a3f28494d61
pdf_path: literature/pdfs/wallot2016mdrqa.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces Multidimensional Recurrence Quantification Analysis (MdRQA), a recurrence-based technique that quantifies the coordination/dynamics of multiple variables over time by constructing a single shared phase-space from N measured observables (each used as a dimension), rather than embedding a single one-dimensional signal as in standard RQA. The motivation is joint-action research, where most studies treat groups via averages of pairwise (dyadic) analyses, which both fail to capture genuine group-level dynamics and create degrees-of-freedom problems from non-independent pairs. The authors situate MdRQA relative to RQA, Cross-RQA (CRQA), and Joint-RQA (JRQA), illustrating differences with the Lorenz system and two coupled van der Pol oscillators, and showing that MdRQA-based measures track coupling strength more sensitively and with more convergent correlations than CRQA in their example. They then re-analyze skin-conductance data from an origami-boat teamwork study (groups of three over five sessions) and find that only group-level dynamics (MdRQA on all three signals, MdRQA3) predict task performance (boats built), reaching R^2 above 0.2 in later trials, whereas individual- and dyadic-level analyses (R^2 around 0.1) did not. The paper supplies a MATLAB implementation and discusses parameter-estimation and phase-space-dimensionality baseline-correction caveats. The authors interpret the group-level finding as possible evidence of interpersonal synergy not reducible to individuals or dyads.

## Key facts it relies on
- MdRQA generalizes RQA: instead of reconstructing a D-dimensional phase space from one observable via time-delayed embedding (Takens' theorem, embedding dimension and time-lag tau), it builds the phase space from N separately measured observables y1..yN as the columns of the data matrix W (Eq. 5).
- A point is recurrent when the distance between two phase-space points is below threshold T, via the Heaviside step function RPij = Theta(T - ||Vi - Vj||) (Eq. 4); thresholds are stated relative to a Euclidean distance norm of the phase-space.
- Four standard recurrence measures are used throughout: recurrence rate (RR), determinism (DET), average diagonal line length (ADL), and longest diagonal line length (LDL) (Table 1; Webber and Zbilut, 1994).
- Lorenz-system demonstration uses sigma=10, rho=28, beta=8/3, integrated over 0<=t<=20, resampled at sampling interval Delta t = 0.0162, giving 1234 samples; reconstructions used embedding dimension D=3 and time delay tau=4; recurrence thresholds T=0.1 for reconstructed attractors and T=0.08 for the original attractor.
- Table 2 (Lorenz, D=3, tau=4, T=0.01 for RQA / T=0.008 for MdRQA): RQA(x) RR 0.69% DET 99.4% ADL 9.12 LDL 131; RQA(y) RR 0.84% DET 97.4% ADL 7.84 LDL 118; RQA(z) RR 0.68% DET 99.5% ADL 10.3 LDL 82; MdRQA RR 0.69% DET 99.9% ADL 16.4 LDL 167 — diagonal line structures are consistently longer in MdRQA than RQA.
- Van der Pol comparison fixed mu=100 with asymmetric coupling epsilon2 = 5*epsilon1 (D=2, tau=1, T=0.01); Table 3 reports MdRQA measures correlate more strongly/convergently with coupling epsilon1 than CRQA (e.g., RR: CRQA r=0.48 vs MdRQA r=0.99; DET: CRQA r=-0.86 vs MdRQA r=0.89).
- Table 4 (Lorenz, multivariate JRP vs MdRP): values comparable except RR, which is a factor ~6 smaller for the JRP (RR 0.14% JRP vs 0.84% MdRP), because JRP structure requires recurrence in all three constituent RPs simultaneously.
- Origami teamwork re-analysis: teams of three participants, five consecutive sessions, 4-min building sessions; MdRQA1 = individual (single observable, equals RQA), MdRQA2 = averaged dyadic (two signals), MdRQA3 = group level (three signals); embedding parameters tau=6, D=6 (a 3-dimensional signal embedded once, 3*2=6), T=0.12, Euclidean norm.
- Regression result: MdRQA3 (group level) predicted boats built with R^2 increasing to above 0.2 in later trials, while individual and dyadic levels hovered around R^2 ~0.1; all models had predictor DF=4 and residual DF=95, and significance at alpha=0.05 required R^2 > 0.096 (p<0.05).
- Phase-space distance scales with dimensionality as L_D^2 = 2D for equal-variance random variables (uniform [0,1]), giving baseline-correction relation L_D = sqrt(L_{D+n}^2 - 2n) (Eq. 11, Figure 8) — required when comparing RQA measures across phase-spaces of different dimensionality.

## Critical notes from the literature
- The authors explicitly caution that the van der Pol example does NOT generally imply MdRQA is more sensitive than CRQA, since they did not systematically test different systems and coupling properties.
- Stated limitation: in its present form MdRQA cannot compute time-lagged coupling between signals, so it cannot investigate leader-follower relationships the way CRQA can, nor test the directed influence of one component signal on another (unlike convergent cross-mapping).
- Comparing MdRPs/RQA measures across phase-spaces of differing dimensionality requires baseline correction (Eq. 11) or holding percent recurrence constant, because average phase-space distance grows with the number of dimensions regardless of whether they are surrogates or genuine separate observables.
- Whether and how to embed before MdRQA is not conclusively answerable by estimation procedures; the authors cite that unembedded "parent plots" can suffice under some conditions (March et al., 2005; Iwanski and Bradley, 1998), but note embedding can substantially affect results in their experience.
- Interpretation is dual and unresolved: MdRQA measures can be read either as the dynamics of one multidimensional system (an attractor manifold) or as a multivariate correlation/synergy strength between distinct systems; the group-level origami finding is offered as possible evidence of interpersonal synergy but the causal mechanism is not established.

## Key topics covered
Multidimensional Recurrence Quantification Analysis (MdRQA); RQA; Cross-Recurrence Quantification Analysis (CRQA); Joint Recurrence Quantification Analysis (JRQA/JRP); recurrence plots; phase-space reconstruction; time-delayed embedding; Takens' theorem; recurrence measures (RR, DET, ADL, LDL); threshold parameter; Lorenz system; van der Pol oscillators; self-similarity matrices; joint/collective action; group-level vs dyadic vs individual dynamics; skin conductance / physiological synchrony; interpersonal synergy; phase-space dimensionality baseline correction; MATLAB implementation.
