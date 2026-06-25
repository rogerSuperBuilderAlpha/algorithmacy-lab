---
citekey: schmidt1998comparison
title: A comparison of intra- and interpersonal interlimb coordination: Coordination breakdowns and coupling strength.
authors: Schmidt, R. C. and Bienvenu, M. and Fitzpatrick, P. A. and Amazeen, P. G.
year: 1998
doi: 10.1037/0096-1523.24.3.884
arxiv: null
journal: Journal of Experimental Psychology: Human Perception and Performance
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://research.vu.nl/ws/files/2786346/111415.pdf
sha256: b1da337f8ac954de8288ae714e2796b0f74d08c258d78c5a0b3d1469486d58c2
pdf_path: literature/pdfs/schmidt1998comparison.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether rhythmic interlimb coordination established within one person (intrapersonal, coupled across the CNS) versus across two people (interpersonal, coupled visually across the optic array) obeys the same dynamical principles and, if so, which coupling is stronger. Using a wrist-pendulum paradigm, participants swung hand-held pendulums in-phase or anti-phase while three control parameters were manipulated: coordination mode (in/anti-phase), within-trial frequency scaling (0.6-2.0 Hz in 0.2-Hz steps), and frequency detuning (the eigenfrequency difference Aw between the two oscillating limbs). Experiment 1 studied one person coordinating two of their own wrist pendulums; Experiment 2 adapted the identical task to pairs of people visually coordinating pendulums. The relative phase angle (phi) time series was used to assess coordination stability (breakdowns, phi standard deviation) and fixed-point drift, and a regression of sin(phi) on Aw recovered the coupling strength K of a local dynamical model (phi-dot = Aw - K sin(phi)). In both cases coordination behaved as predicted by a coupled nonlinear-oscillator model (Haken-Kelso-Bunz / Equation 2): fixed-point drift increased with detuning and frequency, fluctuations rose with frequency, and coupling strength decreased with frequency. Critically, interpersonal coupling was substantially weaker than intrapersonal coupling (mean K = 0.27 vs. 0.57 Hz), with far more breakdowns (~26% vs. ~2% of plateaus) and larger phi fluctuations in the between-person case.

## Key facts it relies on
- The order parameter is the relative phase angle phi between two 1:1 frequency-locked limbs: phi = 0 deg for in-phase, 180 deg for anti-phase; control parameters are frequency of oscillation and eigenfrequency difference Aw = omega_1 - omega_2.
- The global model used is the Haken-Kelso-Bunz dynamic with detuning: phi-dot = Aw - a sin(phi) - 2b sin(2phi) + noise (Equation 2), with potential V = -Aw*phi - a cos(phi) - b cos(2phi) (Equation 3); the local single-mode model is phi-dot = Aw - K sin(phi) (Equation 4), where positive K gives a stable in-phase solution and negative K an anti-phase solution.
- The formal mapping between models is a = (K_0 - K_180)/2 and b = (K_0 + K_180)/2 (attributed to A. Fuchs, personal communication, 1994), allowing recovery of the whole attractor layout from in- and anti-phase K estimates.
- Apparatus: four aluminum-rod pendulums with 0.03-kg attached mass and rod lengths 0.20, 0.20, 0.36, and 0.50 m (Pendulums A-D); five pendulum combinations gave Aw values spanning roughly -0.30 to +0.30 Hz; movement captured at 90 samples/s with a sonic digitizer.
- Experiment 1 (5 participants, intrapersonal): only 27 of 1,200 frequency plateaus (~2%) were unstable; of these 23 were errors and 4 transitional, and all 4 transitional breakdowns occurred in anti-phase at the highest frequencies and largest |Aw| (+/-0.30).
- Experiment 1 coupling strengths K were all significant, positive for in-phase and negative for anti-phase, and decreased with frequency (r(7) = -.93, p < .001); in-phase and anti-phase K did not differ significantly; the derived coefficient a was zero at every frequency and b ranged 0.099-0.208 Hz.
- Experiment 2 (10 participants, 5 pairs, interpersonal): 307 of 1,200 plateaus (~26%) were unstable (187 transitional, 87 errors, 33 other mode); mean K decreased with frequency (r(7) = -.71, p < .05) and in-phase K exceeded anti-phase K (t(7) = 7.75, p < .001); anti-phase regressions were significant for only 4 of 8 frequencies.
- Direct comparison: mean coupling strength was significantly greater within-person than between-person (0.57 vs. 0.27 Hz, t(30) = 6.61, p < .001), holding separately for in-phase (0.57 vs. 0.34 Hz) and anti-phase (0.58 vs. 0.19 Hz); mean phi SD was larger interpersonally (21.1 deg vs. 16.2 deg, t(14) = 4.27, p < .001); breakdown rates at the four highest frequencies were 25%, 40%, 46%, 57% (Exp 2) vs. 1%, 4%, 3%, 6% (Exp 1).
- Coupling strength K correlated negatively with phi fluctuations (combined r(15) = -.87, p < .001), and the global normalized potential-well depths (0 deg minimum = -a - 2b; 180 deg minimum = a - 2b) correlated highly with the local index K (r(30) = .96, p < .001).

## Critical notes from the literature
- The range of Aw and frequency was deliberately small/circumscribed because the pendulums had to be light enough to swing at 2 Hz, which the authors note is near the limit of stable single-pendulum oscillation; they acknowledge this limited range likely weakened the predicted Aw (pendulum combination) effects, especially in Experiment 2 where that factor was nonsignificant.
- The model predicts greater fixed-point drift and weaker coupling for anti-phase than in-phase, but Experiment 1 did not find a significant phase-mode difference in K or drift; the authors attribute this to limited statistical power (citing Treffner & Turvey, 1995) and to anti-phase being unusually stable for sagittal-plane movements for postural reasons (center of gravity stays constant in anti-phase).
- The authors caution that the "stay in the original phase mode" instruction (rather than "do not intervene") may have introduced intentional stabilizing forces, especially in Experiment 2 where many phi SDs (11 of 16 means) exceeded 20 deg and some approached the 24-27 deg range Scholz & Kelso (1990) linked to intentional resistance; the intrinsic Equation 2 dynamics may need an added intentional forcing term, so the recovered high-frequency potential wells could partly reflect intention.
- They note a methodological limitation of the global regression: sin(phi) and sin(2phi) are not independent over restricted phi ranges (citing Fuchs & Kelso, 1994), motivating the use of the local single-mode model; they also argue the conventional b/a ratio fails as a strength index here because a was estimated as zero throughout.
- Causal claims about why visual (interpersonal) coupling is weaker (peripheral-only vs. higher-order CNS coupling, kinematic information availability in the optic array, efficiency of proprioceptive vs. visual information pickup, Bernstein's levels of synergy vs. space) are framed as speculation and open questions, not established results.

## Key topics covered
Interlimb rhythmic coordination; intrapersonal vs. interpersonal coordination; relative phase (phi) as order parameter; Haken-Kelso-Bunz coupled oscillator model; frequency scaling; frequency detuning (eigenfrequency difference Aw); fixed-point drift; basin-of-attraction distortion; coupling strength estimation via regression; local vs. global dynamical model (K vs. a, b); in-phase vs. anti-phase stability; coordination breakdowns (transitions, errors, other mode); phase fluctuations (phi SD); wrist-pendulum paradigm; visual/optical coupling; synergetics; intentional forcing terms; postural stability in the sagittal plane.
