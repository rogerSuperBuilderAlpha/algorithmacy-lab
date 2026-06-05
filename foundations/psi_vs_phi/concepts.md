# Concept map: the theories Kearney's MaxCal bridge connects

This is the conceptual scaffolding of the project — the theories and constructs that Kearney
(2026, arXiv:2605.12536) draws together, and how each relates to our research question (does the
MaxCal information ψ track exact IIT‑4.0 Φ?). Clusters mirror the paper's thematic bibliography.

---

## 1. Integrated Information Theory (IIT)
- **Φ (integrated information)** — the irreducible, intrinsic cause‑effect power of a system in a
  state; the central quantity, intractable to compute at scale.
- **Cause/effect repertoires** — probability distributions a mechanism specifies over its inputs
  (cause) and outputs (effect). *Kearney re‑derives these from MaxCal.*
- **Cause‑effect structure / Φ‑structure** — distinctions (concepts) + relations; the "shape" of
  experience under IIT.
- **IIT 3.0** (Oizumi, Albantakis, Tononi 2014) — the version whose repertoires Kearney targets.
- **IIT 4.0** (Albantakis et al. 2023) — current formalism; intrinsic information, explicit
  relations. *This is the Φ we can compute exactly (PyPhi `new_big_phi`).* Kearney does **not**
  address 4.0 — a gap (our Tier B).
- **Weak vs strong IIT** (Mediano, Rosas, Bor, Seth, Barrett) — Φ as complexity index vs Φ as
  literal consciousness.
- **The unfolding argument** (Doerig et al. 2019) — causal‑structure theories may be
  unfalsifiable by behavior; relevant to why a *bridge to dynamics* (FEP) matters.

## 2. Free Energy Principle (FEP) & active inference
- **Variational free energy (VFE)** — an upper bound on surprise that self‑organizing systems
  minimize (Friston). *Kearney shows a free‑energy functional equivalent to "information".*
- **Active inference** — perception + action as VFE/expected‑free‑energy minimization. *Shown
  mathematically dual to CMEP under Langevin dynamics.*
- **Markov blankets / Bayesian mechanics** — the statistical boundary separating internal states
  from the environment; the formal object FEP organizes around.

## 3. Maximum caliber (MaxCal), maximum entropy (MaxEnt), path ensembles
- **MaxEnt** — least‑biased distribution consistent with constraints (Jaynes).
- **Maximum caliber (MaxCal)** — MaxEnt over *trajectories* (paths), not states; the engine of
  the paper. The **path‑ensemble partition constant κ** normalizes it.
- **CMEP** — Kearney's "constrained maximum‑entropy principle" from which IIT repertoires emerge.
- **Maximum‑Entropy Random Walks (MERW)** vs generic random walks (GRW) — when they coincide,
  ψ ≡ 0 (a control); their divergence (Burda–Duda) signals "information"/localization.

## 4. Predictive coding
- **Prediction error / Bayesian surprise** — the discrepancy between predicted and realized input
  (Rao & Ballard; Friston). *Under CLT/LDT limits, Kearney's ψ ≡ prediction error.*

## 5. Limit theorems & statistical‑mechanics models
- **CLT for Markov chains** — Gaussian limit used to extend ψ to long trajectories.
- **Large‑deviations theory (LDT)** — rate‑function machinery; used for the Ising‑model regime.
- **Ising models** — pairwise spin systems; where ψ is connected to free energy.
- **Langevin dynamics** — stochastic differential dynamics; the regime where active inference and
  CMEP are dual.

## 6. Thermodynamics of cognition
- **Fluctuation–dissipation theorem (FDT)** — links response to fluctuations; recent work grounds
  consciousness in FDT *violations* (the paper situates ψ alongside this).
- **Non‑equilibrium thermodynamics / entropy production** — the physical substrate of the bridge.
- **Neural complexity** (Tononi, Sporns, Edelman 1994) — the original segregation/integration
  measure, ancestral to Φ.

## 7. Complexity & criticality
- **Self‑organized criticality, edge of chaos, neuronal avalanches, metastability** — the
  dynamical regime in which "information" (per ψ) is hypothesized to be maximal.
- **Information bottleneck** — representation learning as a complexity tradeoff (the ANN link).

## 8. IIT–FEP unification (prior attempts — mostly informal/empirical)
- **IWMT** (Safron 2020/2022) — integrated world modeling: IIT + GNWT + FEP, conceptual.
- **Albantakis et al. 2014 (animats)** — Φ develops only as far as task demands require.
- **Olesen & Waade 2023** — "Φ fluctuates with surprisal" (empirical pre‑study).
- **Mayama et al. 2025** — IIT↔FEP in living neuronal cultures; the **"hill‑shaped Φ trajectory."**
- **INTREPID consortium 2026** — adversarial collaborative review of IIT vs predictive processing.
- *Common thread Kearney targets: these are conceptual/empirical, lacking a **rigorous
  mathematical mapping** — which his MaxCal derivation aims to supply.*

## 9. Measure validation & the proxy problem ← where OUR prior work connects
- **Perturbational Complexity Index (PCI)** — the clinical Lempel‑Ziv proxy used on EEG/TMS.
- **Candidate Φ measures** (Mediano, Seth, Barrett 2018/2019) — Φ_WMS, Φ*, stochastic interaction,
  decoding‑Φ, ΦID/synergy.
- **"IIT: the good, the bad and the misunderstood"** (Barrett et al. 2026) — Φ never computed on a
  real system; only *proxies*, never validated against Φ; replace Φ with a *suite*.
- **Our sibling experiments** — `proxy_audit` (empirical proxies don't track exact Φ),
  `candidate_audit` (theoretical measures track only moderately), `phiid_vs_phi` (data‑style ΦID
  estimation halves the tracking). **ψ is the next candidate measure to put through this exact
  validation** — and uniquely, the one whose author explicitly asked for the test.

---

### How the bridge fits together (one paragraph)
FEP says self‑organizing systems minimize variational free energy / prediction error; IIT says a
system's existence/experience is its irreducible cause‑effect structure. Kearney's move is to
define **information ψ as a MaxCal path‑deviation**, from which (a) IIT's repertoires fall out as
constrained‑MaxEnt solutions and (b) ψ equals prediction error in the appropriate limits — placing
IIT and FEP on one variational footing. The untested link in that chain is **ψ ↔ Φ itself**, which
our exact IIT‑4.0 oracle can finally check.
