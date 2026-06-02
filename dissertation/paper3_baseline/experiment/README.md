# Experiment: validating the structure axis of the Φ model

**Internal planning folder — not reader-facing.** Organizes the experiment that tests whether the Paper 3
model's score (Φ) actually predicts coordination difficulty. This is the empirical step the dissertation
currently defers, and the thing the cut Chicago anchor (`../exploratory/`) could not do because it only
varied party count.

## The one-line idea

**Hold party count fixed at three, vary only the determination structure, and test whether higher Φ means
harder coordination.** Because we *build* the structure instead of inferring it from a messy real org, the
three modeling choices become exact controls rather than assumptions — which is what makes a clean test
possible at all.

## Docs

| File | What it is |
|---|---|
| `DESIGN.md` | Master design: the problem it fixes, RQ, hypotheses (H1 structure axis; H1a "eliminate the dyad"; H0 null; H2 Cerullo/parity), IV/DV, the three run-modes, threats to validity, success/failure criteria. |
| `CONDITIONS.md` | The 4 conditions (C0 dyadic Φ=0 / C1 parity Φ=0.5 / C2 partial Φ=0.83 / C3 strict Φ=2.0), exact node rules, and how the **three modeling choices map to exact experimental controls**. |
| `SIM_SPEC.md` | The agent-based simulation — the runnable version, read as a consistency check (transmit-and-agree task, a-priori Q-learning agents, analysis incl. the Φ-beyond-features test). Buildable now. |

## Why this is worth doing (in one place)

- It directly answers "we built the methods section but didn't run an experiment."
- It tests the model's **novel content** (structure at fixed party count), not the trivial party-count axis.
- The clean planned contrast (C2 vs C3 = back-channel present vs absent, AND held fixed) is the behavioral
  test of the dissertation's central political-economy claim ("removing the dyad raises the demand").
- It is the empirical chapter the three-paper-format audit flagged as possibly required by Bentley.

## Open decisions (resolve before building)

1. **Strengthen Paper 3, or stand up a new empirical Paper 4?** The sim/human study could become §4.x of
   Paper 3, or a standalone fourth chapter. Affects framing and length balance (Paper 1 is already long).
2. **Sim first, or go straight to the human study?** Recommendation in `DESIGN.md`: sim first (cheap,
   runnable now, de-risks design and settles H0/H1/H2 in silico), human study if/when an empirical chapter
   is required.
3. **The exact coordination task.** `SIM_SPEC.md` proposes transmit-and-agree; confirm it is the right task
   (does its difficulty depend on structure in the way the construct predicts?) before committing code.

## Status

- [x] Design, conditions, and sim spec drafted.
- [x] Decision: experiment folded into **Paper 3** (§3.5 method, §4.4 result); **sim-first**.
- [x] Agent rule + hyperparameters frozen a priori (`sim/coordination_sim.py` docstring).
- [x] Built `sim/` and ran it; `sim/analyze.py` produces stats + figure.
- [x] Full runs + analysis done — see `RESULTS.md`. **Headline: H1a (strict mediation harder,
      back-channel contrast) CONFIRMED, d≈29, robust; H2 (parity anomaly / Cerullo) CONFIRMED;
      H1 (clean Φ-monotonicity) NOT supported — magnitude is ordinal.**
- [x] Integrated into Paper 3 draft (abstract, §3.5, §4.4, discussion, limitations, conclusion);
      Paper 2 §7 handoff re-pointed to the test.
- [ ] (Future / external validity) human-study protocol + IRB; replication on other tasks; ΦID
      decomposition to separate the parity case.

The **in-silico** result is now part of the dissertation's claims (Paper 3 §4.4), carefully bounded as
one controlled test with agents, not a field validation.
