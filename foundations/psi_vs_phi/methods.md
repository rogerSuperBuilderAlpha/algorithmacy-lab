# Methods (draft): testing whether MaxCal information ψ tracks exact IIT‑4.0 Φ

*Structured per the measure‑validation‑on‑simulated‑systems convention used by Mediano, Seth &
Barrett (2019), Tegmark (2016), Olesen & Waade (2023), Mayama et al. (2025), and our own prior
audits: design → system ensemble → ground truth → measure(s) under test → implementation
validation → comparison & statistics → reproducibility. Notation follows Kearney (2026).*

## 2.1 Design

We perform a within‑ensemble measure‑validation study. For each system in a generated ensemble we
compute (i) the exact IIT‑4.0 integrated information Φ (ground truth) and (ii) the candidate
maximum‑caliber information ψ, then quantify how well ψ tracks Φ. Because both quantities are
computed on the *same* systems, the comparison is like‑for‑like, as in candidate‑measure
comparisons (Mediano et al. 2019). Hypotheses are fixed in advance (see `research_question.md`):
**H1**, ψ tracks Φ; **H0**, ψ tracks order/disorder complexity but not integration. The analysis is
designed to discriminate between them.

## 2.2 System ensemble

Systems are networks of `n` binary units, each updating in discrete time as a (possibly noisy)
Boolean gate (OR, AND, PARITY, MAJORITY, COPY) of the units that connect to it, giving a
state‑by‑node transition probability matrix (TPM). We sweep connectivity density and per‑node
noise to span sparse↔dense and deterministic↔stochastic regimes, and use `n ∈ {3, 4}` for the
primary analysis with `n = 5` as a scale check (the regime where exact Φ remains tractable). We
reuse the validated generator `proxy_audit.networks.generate_ensemble` and convert to the
state‑by‑state TPM via `pyphi.convert.state_by_node2state_by_state`.

**Ergodicity.** ψ is defined for ergodic, homogeneous, stationary Markov chains (Kearney 2026); we
therefore test each chain's state‑by‑state TPM for irreducibility and aperiodicity and either
restrict the analysis to ergodic systems or report the ergodic subset explicitly. Multiple
networks are generated per (density, noise) cell, under fixed random seeds, with the full ensemble
size reported and ≥ 2 independent seeds used for stability (Kearney generated 40 samples per cell;
we match that order of magnitude).

## 2.3 Ground truth: exact IIT‑4.0 Φ

Φ is computed exactly (no approximation) with PyPhi's IIT‑4.0 implementation
(`pyphi.new_big_phi.sia`), pinned to a specific `feature/iit-4.0` commit and run single‑threaded
with progress bars disabled. We use **IIT 4.0** (Albantakis et al. 2023), the current canonical,
unique, computable Φ (grounded in the intrinsic‑difference measure), via the oracle
`proxy_audit.exact_phi`. Because Φ is state‑dependent, each network is summarized by the **mean
exact Φ over its reachable states** (with the max reported as a robustness check); a negative
system Φ denotes a reducible system and is clamped to 0, following our prior audits. Reachable
states are those with ≥ 1 predecessor under the dynamics.

## 2.4 Candidate measure under test: ψ

For a stationary distribution π, the maximum‑caliber information is

> **ψ(π) = log κ − H(π) − h(π)**

computed exactly from the TPM (no Monte‑Carlo sampling at these sizes):
- **π** — the stationary distribution, obtained by power iteration on the state‑by‑state TPM.
- **H(π)** — the marginal Shannon entropy of π (bits).
- **h(π)** — the entropy rate, `Σ_s π(s) · H(P(·|s))` (the π‑averaged one‑step conditional entropy).
- **κ** — the MaxCal path‑ensemble partition constant. **κ is system‑specific and its exact
  definition will be transcribed from Kearney (2026) §5.1–5.2 rather than assumed** (the paper
  reports κ ∈ (22, 332) for `N = 20`, so κ is *not* a fixed `2 log N`). This transcription, and a
  cross‑check that our κ reproduces values consistent with the paper, is a prerequisite for the
  study.

We also compute the related mutual‑information quantity `i(π) = H(π) − h(π)` (Kearney's eq. for
i), used as an ablation to test whether any ψ–Φ relationship is carried by ψ specifically or by i.
ψ is added as a new measure to the `candidate_audit` harness so it is computed and analyzed
identically to the previously‑audited measures.

## 2.5 Implementation validation (controls) — performed before any ψ–Φ analysis

Following the correctness discipline that previously caught a spurious‑synergy pathology in our
ΦID experiment, we validate the ψ implementation on systems with known behavior *before* trusting
any ψ–Φ number:
1. **Null control.** ψ ≡ 0 when the maximum‑entropy and generic random walks coincide
   (uniform‑transition / vanishing degree‑variance regimes), as Kearney reports.
2. **Structural reproduction.** ψ should peak at low mean‑degree / high degree‑variance TPM
   structure (Kearney §6.3); reproducing this on our generator is an end‑to‑end sanity check.
3. **Determinism/degeneracy sanity.** ψ on hand‑built deterministic‑permutation and fully‑degenerate
   chains should match analytic expectations.
Only after these pass is ψ correlated with Φ.

## 2.6 Comparison and statistics

- **Primary:** Spearman rank correlation ρ and Pearson r of ψ against mean exact Φ; and the AUC for
  detecting Φ > 0 from ψ (treating "is the system an integrated complex?" as a binary task).
- **Conditional analysis:** because full‑sample rank correlations can be dominated by the mass of
  Φ = 0 systems (ties), we also report the association restricted to Φ > 0 systems, as in our prior
  audits.
- **Ablation:** ψ vs `i(π)` vs their combination, to localize the signal.
- **Relative ranking:** ψ is inserted into the existing candidate‑measure leaderboard
  (Φ whole‑minus‑sum, total correlation, stochastic interaction, causal density, …) so its
  performance is read against measures already validated on the same ensemble.
- **Structural overlay:** we test whether exact Φ peaks in the same (low‑m, high‑σ²) regime where
  ψ peaks, or a different one.
- **Stability:** all statistics are repeated across ≥ 2 independent seeds; bootstrap confidence
  intervals are reported for the headline correlations.

## 2.7 Handling the IIT 3.0 / 4.0 mismatch

Kearney's derivation targets IIT **3.0** cause/effect repertoires (earth‑mover's distance), whereas
the canonical computable Φ is IIT **4.0** (intrinsic difference). The **primary** test is ψ vs
exact 4.0 Φ (the current standard). As a robustness check we additionally compute a 3.0‑style
system Φ (via PyPhi's 3.0 `compute`/`major_complex` path) where feasible and report ψ against both,
so that any (mis)match can be attributed to the formalism rather than left ambiguous.

## 2.8 Reproducibility

The study is implemented as a self‑contained `candidate_audit`‑style package (`psi.py` for the
measure, `run.py` to generate `results/`, `analyze.py` for the comparison), reusing
`proxy_audit.networks`, `proxy_audit.exact_phi`, and the `candidate_audit` analysis scaffolding.
Random seeds, the PyPhi commit, and Python/numpy versions are recorded; the ensemble, per‑network
Φ and ψ values, summary statistics, and figures are committed to the repository so the full
pipeline is re‑runnable end‑to‑end.
