# Research question (Tier A): does the MaxCal information ψ track exact IIT‑4.0 Φ?

## Motivation
Kearney (2026, arXiv:2605.12536) proposes that **information** is the deviation ψ of a system's
realized dynamics from a constrained maximum‑caliber (MaxCal) path ensemble, re‑derives IIT 3.0's
cause/effect repertoires from this principle, and links ψ to the Free Energy Principle and to
prediction error. For a stationary ergodic Markov chain this collapses to a cheap scalar:

> **ψ(π) = log κ − H(π) − h(π)**

The paper studies how ψ depends on network *structure* but **never compares ψ to actual IIT Φ**,
and explicitly calls for that test ("…work must be conducted to … connect the metrics observed
here to those in IIT"). We hold the missing instrument: an exact **IIT‑4.0** Φ oracle
(`proxy_audit/exact_phi.py`, PyPhi `new_big_phi`) and a candidate‑measure validation harness
(`candidate_audit/`, `phiid_vs_phi/`).

## Primary question
**RQ.** Across an ensemble of small discrete systems where exact Φ is computable, does the MaxCal
information ψ(π) track exact IIT‑4.0 integrated information Φ?

Operationally: compute ψ per network from its stationary distribution; compute exact IIT‑4.0 Φ
(mean over reachable states, as in our prior audits); report rank (Spearman) and linear (Pearson)
association and detection AUC for Φ>0 — exactly the protocol of `candidate_audit`.

## Hypotheses
- **H1 — the bridge holds.** ψ correlates positively and substantially with exact Φ. This would be
  the first empirical evidence that Kearney's MaxCal information is a faithful surrogate for IIT
  integration, supporting the MaxCal↔IIT↔FEP unification.
- **H0 / alternative — ψ is a complexity measure, not an integration measure.** ψ tracks the
  order/disorder balance Kearney himself finds (peaks at low mean‑degree / high degree‑variance)
  but **does not** track Φ specifically — i.e. it behaves like the order/disorder proxies our
  `proxy_audit` found do *not* track Φ (e.g. total correlation, which even anti‑correlated).
  Distinguishing H1 from H0 is the crux: ψ is built from entropy/entropy‑rate of the *whole*
  system, with no partition step, whereas Φ is irreducibility *across a partition*.

## Secondary questions
- **Structural coincidence.** Kearney finds ψ maximal at low‑m/high‑σ² TPM structure. Does exact Φ
  peak in the same structural regime, or a different one? (Re‑uses `emergence_vs_phi`‑style
  structure sweeps.)
- **ψ vs i(π).** The paper relates ψ to mutual information i(π)=H(π)−h(π). Does i, ψ, or their
  combination track Φ best? (Adds a clean ablation.)
- **Relative ranking.** Where does ψ sit among the candidate measures we already audited
  (Φ_WMS ρ≈0.47, total correlation ρ≈−0.36, stochastic interaction, causal density)? Adding ψ to
  the same table answers this directly.

## Design sketch (deferred to the build phase)
- **Ensemble + oracle:** reuse `proxy_audit.networks.generate_ensemble` and
  `proxy_audit.exact_phi.network_phi` (mean exact IIT‑4.0 Φ over reachable states).
- **Measure:** implement `psi.py` with ψ(π)=log κ−H(π)−h(π) and i(π); add to a `candidate_audit`‑
  style run/analyze.
- **Analysis:** Spearman/Pearson/AUC of ψ (and i) vs Φ; ablation; structural‑regime overlay;
  insert ψ into the candidate‑measure leaderboard.

## ⚠️ Correctness caveats (must be satisfied before any ψ‑vs‑Φ number is trusted)
1. **Nail κ.** The MaxCal partition constant κ is system‑specific (the paper reports κ∈(22,332)
   for N=20 — *not* a fixed 2·log N). Extract its exact definition from the paper's §5.1–5.2
   before implementing; do not guess.
2. **Validate ψ on the paper's own controls.** ψ must equal **0** when MERW = GRW
   (uniform‑transition / σ²≈0 regimes). Reproduce that before trusting the measure — the same
   discipline that caught the MMI spurious‑synergy bug in `phiid_vs_phi`.
3. **Regime match.** ψ is defined for ergodic, homogeneous Markov chains; ensure our networks'
   state‑by‑state TPMs satisfy ergodicity (or restrict/notify) so ψ is well‑defined.

## Scope
Tier A is the question above. **Tier B** (extend the MaxCal *derivation* of repertoires from IIT
3.0 to IIT 4.0 and verify numerically against PyPhi) is a separate, deeper follow‑up, out of scope
here.
