---
citekey: niizato2024information
title: Information structure of heterogeneous criticality in a fish school
authors: Niizato, Takayuki and Sakamoto, Kotaro and Mototake, Yoh-ichi and Murakami, Hisashi and Tomaru, Takenori
year: 2024
doi: 10.1038/s41598-024-79232-2
arxiv: null
journal: Scientific Reports
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:publisher
source_url: https://www.nature.com/articles/s41598-024-79232-2.pdf
sha256: 20865414f451e930943635e897e3b1191880b4ee746afa84ae4bb0d0436d6f8b
pdf_path: literature/pdfs/niizato2024information.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks what distinguishes "empirical" criticality in real collective animal behaviour from the homogeneous theoretical criticality of standard models. The authors apply Integrated Information Theory (IIT 2.0, using the mismatch-decoding Φ* of Oizumi et al.) to tracked schools of ayu sweetfish (Plecoglossus altivelis, N=10, seven samples), computing group "integrity" ΦMIP separately over fish orientation (turning rate dθ) and speed (acceleration ds). They find that ΦMIP peaks at the critical state and that, unlike the self-propelled particle (SPP) model where the maximum main complex (MMC) spans the whole group (indecomposable critical state), the real fish MMC is fragmented into subgroups of size 2–10, indicating multiple coexisting local critical states (heterogeneous criticality) alongside whole-group (global) criticality. The MMC distribution is heterogeneous in time and space, with MMC lifespans following a stretched-exponential (long-tailed, non-random) distribution. "Core" fish that frequently belong to the MMC have low variance in direction and speed (negative correlation between core rate and movement deviation), i.e. they are less affected by internal/external stimuli, distinct from leadership. The authors argue empirical criticality is a mixture of more-affected (supercritical) and less-affected (subcritical) individuals, paralleling coexisting local critical states in gene-expression networks, and cannot be reproduced by simple SPP or Boid models.

## Key facts it relies on
- Data: trajectories of ayu (Plecoglossus altivelis) schools, group size N=10, seven samples, recording length 8–12 min; frames analyzed at 1/20 s giving ~12,000 frames per sample (camera recorded at 100 fps, spatial resolution 640×480, 3×3 m² arena, water ~15 cm deep so schools are quasi-2D).
- Method: IIT version 2.0 with the mismatch-decoding integrated information Φ* (Oizumi et al.), implemented via the "Practical Φ Toolbox for MATLAB"; ΦMIP is computed via the minimum information partition (MIP), and main complexes are subsets with local-maximum ΦMIP (the maximum main complex, MMC, is the global maximum).
- Two IIT variables: orientation/turning rate dθ (giving Φdir_MIP) and speed/acceleration ds (giving Φsp_MIP), computed for window sizes Tmax = {200, 400, 600} frames (10, 20, 30 s); time delay τ chosen as ~3 frames (0.15 s), matching the species' response time.
- In the SPP model the MMC was not fragmented (size 10/10 in most cases), i.e. the critical state is indecomposable; in real fish the MMC size ranged from 2 (minimum) to 10 (maximum), and each fragmented MMC had Φdir_MIP significantly larger than SPP critical states.
- Whole-set integrity of real fish exceeded SPP critical states: ⟨Φdir,S_MIP⟩ = 0.038 (Welch t-test t(148.6) = −19.2, p < 10⁻³⁰), supporting coexistence of global (homogeneous) and local (heterogeneous) criticality.
- Time-series character: ΦMIP (sum over main complexes) showed long-range correlation with generalised Hurst exponent H ≈ 0.25 for both dθ and ds (pink/1-f noise, scale-invariant); max{ΦMIP} of the single top complex was Brownian (H ≈ 0.5 for direction, ≈0.46 for speed).
- MMC lifespan fits a cumulative Weibull (stretched-exponential) distribution; real data shape parameters ⟨αdir⟩ = 0.61 ± 0.03 and ⟨αsp⟩ = 0.61 ± 0.02 (α<1, long-tailed, memory effect), versus shuffled controls αdir = 0.96 and αsp = 1.30 (≈ memoryless exponential).
- Core fish: the "core rate" ci (fraction of time fish i is in the MMC) is negatively correlated with movement variability — direction deviation vs cdir: n=70, r=−0.536, p<10⁻⁶; mean speed vs csp: n=70, r=−0.565, p<10⁻⁶ (and r=−0.516, p<10⁻⁶ in Fig. 6B) — so core fish move more stably and are less affected by others; core membership is distinct from leadership and the core position changes dynamically.
- Boid (Couzin-type) comparison: in the model, max{Φsp_MIP} peaks during milling and max{Φdir_MIP} in the schooling–swarming transition, but real fish show high max{Φsp_MIP} around high alignment (⟨P⟩≈1), so the real information structure is not reproduced by a simple Boid model.

## Critical notes from the literature
- The authors explicitly flag that the high-ΦMIP-equals-critical-state correspondence is validated on SPP but cannot be directly transferred to the heterogeneous fish data: SPP's ΦMIP is independent of Tmax (homogeneous process) while real-fish ΦMIP varies with Tmax, and the Boid model's high transition-phase ΦMIP stems from frequent fission–fusion under periodic boundaries, whereas the recorded fish schools rarely split. They frame this as a fundamental theoretical-vs-empirical gap rather than a method flaw.
- They state their analysis did not prove that high Φsp_MIP values correspond to critical states (in the original SPP model velocity is constant), so the speed-channel criticality claim is weaker than the direction-channel claim.
- The two integrities (Φdir_MIP and Φsp_MIP) are treated as effectively independent: only a weak correlation and no significant transfer-entropy information flow (except at larger Tmax), which the authors attribute possibly to their definition of speed integrity and leave for future work.
- The authors do not claim ΦMIP measures fish consciousness; they reuse the IIT machinery purely as a measure of group integrity / degree of criticality, and note the validity of treating main complexes as information cores "remains to be demonstrated."
- Scope is narrow: one species, group size fixed at N=10, seven samples, small-system IIT (exhaustive MIP feasible only because the system is small), and supporting figures (S1–S7, Tables S1–S4) carry much of the quantitative backing.

## Key topics covered
Integrated Information Theory (IIT 2.0); integrated information Φ / Φ* (mismatch decoding); minimum information partition (MIP); main complex and maximum main complex (MMC); group "integrity" vs "integration"; empirical vs theoretical criticality; heterogeneous / nested / local vs global criticality; collective behaviour of fish schools (Plecoglossus altivelis / ayu); self-propelled particle (Vicsek) model; Boid / Couzin model; polarity and milling order parameters; generalised Hurst exponent / pink (1/f) vs Brownian noise; stretched-exponential (Weibull) MMC lifespan; core individuals vs leadership; internal vs external fluctuation; sandpile-type information avalanches; parallel to gene-expression critical networks.
