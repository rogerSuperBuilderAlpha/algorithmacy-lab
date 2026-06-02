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
| `SIM_SPEC.md` | The agent-based simulation — the runnable, non-circular version (transmit-and-agree task, a-priori Q-learning agents, analysis incl. the Φ-beyond-features test). Buildable now. |

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

- [x] Design, conditions, and sim spec drafted (this folder).
- [ ] Confirm the four Φ values reproduce (`../typology_phi.py`).
- [ ] Decision: Paper 3 §4.x vs Paper 4; sim-first vs human-first.
- [ ] Freeze agent rule + hyperparameters (a priori).
- [ ] Build `sim/` and run smoke test.
- [ ] Full runs + analysis (H1 / H1a / H2 / Φ-beyond-features).
- [ ] (If pursued) human-study protocol + IRB.

Nothing here is committed to the dissertation's claims yet; it is planning.
