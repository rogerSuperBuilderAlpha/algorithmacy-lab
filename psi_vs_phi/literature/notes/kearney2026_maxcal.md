# Kearney (2026) — Information as Maximum-Caliber Deviation

**Cite:** Kearney, A. (2026). *Information as Maximum-Caliber Deviation: A bridge between
Integrated Information Theory and the Free Energy Principle.* arXiv:2605.12536.
**Access:** open (arXiv). PDF in `../pdfs/kearney2026_maxcal_arxiv2605.12536.pdf`.
**This is the anchor paper of the project.**

## Core idea
Defines **information ψ** as the deviation of a system's *realized* dynamics from a constrained
**maximum-caliber (MaxCal)** path ensemble over a finite horizon. (MaxCal = maximum entropy over
*trajectories*, the path-space analogue of MaxEnt.) From this single variational principle:

- **IIT 3.0's cause/effect repertoires are re-derived** as MaxCal solutions (the author's "CMEP",
  constrained maximum-entropy principle). Targets **IIT 3.0**, repertoires only — *not* IIT 4.0,
  and *not* the full Φ-structure (distinctions + relations).
- Bridges to **active inference** (shown dual to CMEP under Langevin dynamics).
- Under the **CLT for Markov chains** and **large-deviations theory** (Ising models), ψ is shown
  equivalent (up to a constant) to **prediction error / Bayesian surprise** in predictive coding.
- Connects to the empirical **"hill-shaped Φ trajectory"** in adapting neuronal cultures
  (Mayama 2025) and to **fluctuation-dissipation** thermodynamic accounts.

## The key scalar (what we can compute)
For a stationary, ergodic, homogeneous Markov chain with stationary distribution π:

> **ψ(π) = log κ − H(π) − h(π)**,  where  **log κ = max[H(X) + h(X)]**

- H(π) = marginal (Shannon) entropy of the stationary state distribution.
- h(π) = entropy rate (avg per-step conditional entropy under π).
- κ = MaxCal partition/normalization ("effective number of paths"); **system-specific**, not a
  fixed 2·log N — measured per-TPM in the paper (e.g. κ ∈ (22, 332) for N=20).  ⚠️ Its precise
  definition lives in §5.1–5.2 and must be extracted exactly before implementing ψ.
- Related identity: mutual information i(π) = H(π) − h(π); so ψ + i = log κ − 2h, ψ − i = log κ − 2H.
- Control: when MERW = GRW (uniform-transition / σ²≈0 regimes) **ψ ≡ 0** — a validation check.

## What the paper actually tests (§6)
Empirically studies how ψ depends on TPM **structure** — mean row-degree m and degree-variance σ²
— sweeping random ergodic TPMs (N = 5..50). Finds ψ peaks at **low mean-degree / high variance**
(m ≈ N/5), tracking a balance of order/disorder; ψ̂_max grows ~ logarithmically with N (≈ linearly
in node count). **It never compares ψ to actual IIT Φ.**

## The explicit open problem (our opening)
> "the explanatory power of our proposal here remains unconfirmed. Experimental or theoretical
> work must be conducted to ascertain either a direct relationship MaxCal and FEP inference, or to
> **connect the metrics observed here to those in IIT**."

Plus: existence of a system formally connecting ψ to FEP "remains unproven"; results "restricted to
ergodic, homogeneous Markovian regimes."

## Relevance to our project (Tier A)
We have an exact **IIT-4.0** Φ oracle (`proxy_audit/exact_phi.py`), a network ensemble generator
(`proxy_audit/networks.py`), and a candidate-measure validation harness (`candidate_audit`,
`phiid_vs_phi`). ψ is a cheap stationary-distribution scalar — exactly the kind of measure our
framework audits. **Tier A = test whether ψ tracks exact IIT-4.0 Φ**, the experiment the paper
explicitly requests. Two outcomes: ψ tracks Φ (supports the bridge) or ψ behaves like the
order/disorder *complexity* proxies our `proxy_audit` found do **not** track Φ.

## Bibliography note
Paper has ≈140+ refs organized thematically (IIT; Predictive Coding/FEP/Active Inference;
IIT-FEP unification; Consciousness; Thermodynamics of cognition; computational neuroscience;
complexity/MERW). Used as the seed list for our curated ingestion.
