# Experiment results — the structure axis, tested in silico

**The experiment the dissertation was missing now exists and has run.** Behavioral *consistency check*
(`sim/coordination_sim.py`): independent contextual-bandit agents coordinate through a determination
structure they do not understand; we measure how well they coordinate; Φ is computed separately. The agents
are told nothing about the structure (so the test is not trivially circular), but Φ and difficulty both
derive from the same wiring, so this is a consistency check between the structural classifier and behavior,
NOT an independent validation of Φ against a separately measured criterion. Party count fixed at 3; only the
determination structure varies. Reproduce: `sim/coordination_sim.py` then `sim/analyze.py`.

## Headline

| Condition | Φ | Coordination success | Difficulty |
|---|---|---|---|
| C0 dyadic (direct channel) | 0.00 | 0.951 | 0.049 |
| C1 parity (S = W⊕C, no back-channel) | 0.50 | 0.952 | 0.048 |
| C2 partial (S = W∧C, back-channel) | 0.83 | 0.951 | 0.049 |
| **C3 strict (S = W∧C, no back-channel)** | **2.00** | **0.715** | **0.285** |

Robust: C3 asymptotes at 0.720 at 3,000 rounds vs 0.715 at the committed 600-round run (a genuine
information ceiling, not under-training); the other three hold at 0.951. Committed: `results/sim_runs.csv`
(600) and `results/sim_runs_3000.csv` (3,000). CIs are tight (2 senders × 5 seeds × 120 pairs/cell; C3 95% CI
[0.711, 0.719]). Seeding is deterministic (zlib.crc32, not the salted built-in hash), so the run reproduces.

## What it shows

1. **H1a — the central claim — STRONGLY CONFIRMED.** Removing the direct back-channel and routing
   coordination through a joint AND determination (partial Φ=0.83 → strict Φ=2.0, the determination held
   fixed) makes coordination *much* harder: Δsuccess = +0.236, Cohen's d ≈ 50, robust. This is the
   dissertation's "eliminate the dyad" result and its political-economy claim (a platform's structural
   position is strongest when the parties cannot coordinate except through its determination), **confirmed
   behaviorally as a consistency check** — Φ and difficulty share a structural cause, so this is not an
   independent validation, but it is the behavioral demonstration the cut Chicago anchor could never give,
   because here party count is fixed and the structure is built, not inferred.

2. **H1 — Φ monotonicity — PARTIAL.** Spearman(Φ, difficulty) = +0.40 across the four conditions: positive,
   but driven entirely by C3. Φ magnitude is **not** a clean predictor of difficulty.

3. **H2 — Cerullo / parity — CONFIRMED.** Parity (Φ=0.5, no back-channel) coordinates as easily as the dyad
   (Φ=0), because the XOR determination is **invertible** (the receiver recovers the target from S and its
   own last action). So "no back-channel" is *not* sufficient for difficulty; what makes coordination hard
   is whether the joint determination is **information-losing** (AND is; XOR is not). This is the empirical
   face of Cerullo (2015): Φ magnitude does not track difficulty for parity — exactly the caveat Paper 2
   already carries, now demonstrated rather than asserted.

## The honest interpretation (what Paper 3 should claim)

- The structure axis is **real for the case that matters most** — genuinely irreducible *strict* mediation
  (Uber / court / ATS) is measurably harder to coordinate through. The dissertation's central claim survives
  a behavioral test.
- Φ as a **graded scale is only partly validated**: it correctly flags the hardest form as highest-Φ, but it
  mis-ranks parity. Difficulty is predicted by the determination's information loss, which Φ tracks for the
  conjunctive/strict case but not for parity.
- Therefore: **read Φ ordinally, lean on the strict-vs-rest (binary-ish) distinction, and treat magnitude
  with the Cerullo caveat** — which is precisely what the recast Paper 2/3 already say. The experiment
  *vindicates the dissertation's hedged framing* rather than the overclaimed one.

## Scope / honest bounds

- **In silico, not human.** This establishes the mechanism — the structure axis is not vacuous and the
  central contrast holds — not that humans coordinate as these agents do. The human study (`../DESIGN.md`,
  mode 1) is the external-validity step.
- **Φ-beyond-features.** Difficulty here is largely "is the joint determination invertible." Φ correlates
  with that for these conditions but is not identical to it; a finer synergy/redundancy decomposition (ΦID)
  might separate the parity case. Flagged as the natural refinement.
- **One task (transmit-and-agree), one sender-alternation design.** Replication on other coordination tasks
  is future work.

## Files
- `sim/coordination_sim.py` — the experiment (frozen a-priori agent rule in the docstring).
- `sim/analyze.py` — stats (per-condition CI, H1a contrast, H1 Spearman, H2 probe) + figure.
- `results/sim_runs.csv`, `results/sim_results.png`.
