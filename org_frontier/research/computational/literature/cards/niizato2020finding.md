---
citekey: niizato2020finding
title: Finding continuity and discontinuity in fish schools via integrated information theory
authors: Niizato, Takayuki and Sakamoto, Kotaro and Mototake, Yoh-ichi and Murakami, Hisashi and Tomaru, Takenori and Hoshika, Tomotaro and Fukushima, Toshiki
year: 2020
doi: 10.1371/journal.pone.0229573
arxiv: null
journal: PLoS ONE
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0229573&type=printable
sha256: 2668df962aab1399f915f4e9d9326ee383f402032db67bbdc2304a5e848633ca
pdf_path: literature/pdfs/niizato2020finding.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether group size changes a fish school's intrinsic causal structure, and applies integrated information theory (IIT 3.0, computed with PyPhi) to tracked trajectories of ayu (*Plecoglossus altivelis*) schools of two to five fish. Each fish's continuous trajectory is discretised into ON/OFF binary states defined as the AND-conjunction of three Boid-like local interaction parameters (effective distance, effective visual field, and turning rate), and Φ is computed over the resulting collective time series. The first main result is that a discontinuity in the average ⟨Φ(N)⟩ distribution emerges between three- and four-fish schools (a qualitative shift not seen below four fish); this transition is not captured by mutual information (MI) or the summed transfer entropy (TE). The second main result is that this discontinuity correlates with the emergence of "leadership": for four- and five-fish schools, a single OFF-state individual highly correlates with the positional leader (head of the group) and the minimum information partition (MIP) cut falls between that single OFF fish and the rest. The authors define this as "IIT leadership" reflecting group autonomy/integrity rather than information transfer. Boids-model simulations run under the same conditions show very different Φ patterns from real fish and fail to reproduce the three-to-four discontinuity, suggesting real fish involve relatively weak interactions.

## Key facts it relies on
- Data: trajectories of ayu (*Plecoglossus altivelis*) schools of N=2, N=4, and N=5 with three samples each, and N=3 with four samples; recording length 10–15 minutes (Table 3 reports per-sample total time steps ~83,000–107,000).
- A fish's binary state is the conjunction (AND:{0,1}^3 → {0,1}) of three Boid-like parameters — distance, visual field, turning rate; only the triple (1,1,1) yields state 1. One time step is defined as 0.05–0.10 s, roughly a fish's reaction timescale; the main analysis uses Δt = 0.05 s.
- Φ is computed using PyPhi (IIT 3.0); the network is assumed completely connected including self-loops, justified because Table 3 shows all fish come within 5 mm contact during events. An n-fish school has 2^n collective states, each with its own Φ.
- Main result 1: a discontinuity in ⟨Φ(N)⟩ distributions emerges for schools of four or more fish; ⟨Φ(N)⟩ for N=2 and N=3 depends only on distance, whereas for N=4 and N=5 it depends on both distance and visual field (Fig 2). Welch t-test p-values for the discontinuity (Table 1) are < 10^-10 (N=2), < 10^-7 (N=3), < 10^-8 (N=4), < 10^-8 (N=5).
- This discontinuity is not observed in MI or summed TE (Fig 3, Fig 4); the peaks of MI and TE concentrate in the low-visual-field area, the opposite trend from ⟨Φ(N)⟩. Fig 5 shows the mean matrix distance of Φ(real) between N=3 and N=4 is significantly larger than for MI, TE, and Φ(boid) (MI p < 10^-10, TE p < 10^-13, PHI(boid) p < 10^-35).
- Main result 2 (leadership): for N=4 and N=5, a single OFF-state individual matches the positional leader (head w.r.t. mean group direction) at high rates — Table 2 match rates (MR) of 82–96% — and the MIP cut lies between the single OFF fish and the rest of the ON fish ({1} ⇸ {2,3,4,5} or {2,3,4,5} ⇸ {1}). The contrast is sharpest when visual field ranges 1.6π–2.0π rad; at 2.0π rad there is no blind spot.
- Mean ⟨Φ(N)⟩ and its standard deviation increase with school size N (Fig 8); peak ⟨Φ(N)⟩ cells (Fig 2) are N=2: D=600 mm/VF=2.0π; N=3: D=400 mm/VF=2.0π; N=4: D=600 mm/VF=1.8π; N=5: D=700 mm/VF=1.6π.
- Boids comparison: Boids trajectories show the same complexity as real fish but very different Φ heat-map patterns (Fig 9, Fig 10) and lack the N=3-to-N=4 discontinuity; reducing Boids coupling strength (C = 1.0, 0.1, 0.01, 0) clearly changes the ⟨Φ⟩ distributions, and C = 0.01 yields a distribution similar to real fish.
- Real fish schools have larger Φ standard deviations than time-homogeneous Markov chains: σ(Φ(2))=0.03±0.04, σ(Φ(3))=0.09±0.03, σ(Φ(4))=0.19±0.06, σ(Φ(5))=0.36±0.07 (Fig 8, Fig 11).

## Critical notes from the literature
- The authors note IIT 3.0 has a current practical computational limit of around seven or eight individuals/neurons; extending the leadership analysis to larger schools would require approximations.
- They acknowledge their interpretation of asymmetric ("feedforward") information flow is hard to fully establish because PyPhi provides no information about opposite-direction information flows; they argue weak opposite flows do not invalidate the leadership interpretation but treat the objection explicitly.
- Timescale is a deliberate scope limit: only a small timescale (~fish reaction time) was used, and the authors state that longer timescales or larger group sizes may yield other patterns of continuity/discontinuity.
- The all-connected network with self-loops is an assumption; the authors note (via S6 Fig) that networks excluding self-loops might be more suitable for finding the MIP-based division of roles, and that real fish may form a stable "α-lattice" network radically different from the Boids model.
- For C=0 Boids the authors observe Φ is non-zero and increases with N, attributed to size effects and boundary effects (the binary-state format makes some asymmetric ON/OFF states impossible under full 2π visual field), cautioning that averaged ⟨Φ⟩ alone can mislead and distributions must be compared.

## Key topics covered
Integrated information theory (IIT 3.0); integrated information Φ and φ; minimum information partition (MIP); PyPhi; fish schooling / collective behaviour; ayu (*Plecoglossus altivelis*); ON/OFF binary state discretisation; Boid-like interaction parameters (distance, visual field, turning rate); mutual information; transfer entropy; cause–effect structure / conceptual structure; positional vs IIT leadership; feedforward vs recurrent interaction; Boids model and coupling strength; time-homogeneous Markov chains; self-organised criticality; group integration / autonomy.
