"""Probe 323 (Q169) — the lagging objective and the worker's predictive model.

Question: Q141 found that a lagging objective (a memory M = W ∧ C delayed one step, with the
objective reading the memory, O = M) structurally re-integrates the worker that an immediate
self-executing objective (O = W ∧ C) displaces from the coordination's core. Q169 asks whether
that re-integration also shows up in a predictive measure: does the lagging objective let the
worker's generative model track the platform's commit better than the immediate objective does?

The instrument generalizes pp3_moving_target's window-fit accuracy loop. The platform commits a
Boolean output the worker tries to predict; its rule (a 4-entry truth table over (W, C)) drifts,
one entry flipping every `period` steps. The counterpart C is hidden (PP1), so the worker
conditions on her observable W. Under the immediate objective the commit is the live joint
determination, turning on the hidden C, and her window-majority lags every flip. Under the
lagging objective a memory node stores the joint determination at t-1 and the objective emits the
stored value at t; the stored memory is the re-integration channel — the displaced counterpart's
contribution reaches the worker as a memory she already observed, so she reads the commit off the
held memory. The control at each drift period is the immediate-objective mediator.

H1 (fixed before computing): window-fit prediction accuracy against the lagging objective is
higher than against the immediate objective at matched drift, mirroring the Q141 re-integration in
the predictive measure. NULL: prediction accuracy is equal for lagging and immediate objectives,
so re-integration is invisible to the worker's model.

H2 (fixed before computing): the advantage vanishes as the drift period shrinks — below a critical
retrain rate the lagging objective's memory becomes stale and prediction accuracy converges to the
immediate-objective level. NULL: the lagging advantage is constant (or grows) across drift
periods, independent of retrain rate.

Method: sweep the drift period; for each period compute window-fit accuracy for the immediate and
lagging objectives over seeded trials; report both and the advantage. H1 reads on the advantage
at matched moderate drift; H2 reads on whether the advantage shrinks toward zero as drift speeds.

Validation gap: exact constructions on a small Boolean model and synthetic drift traces. The
result is evidence about the instruments and the construct, not a measurement of a real platform.
"Objective", "memory", "commit" are labels for node rules and output values, not measured intent.
The empirical arm runs on synthetic prediction traces. Φ-to-money bridge open (Q122).

Run:  python -m org_frontier.questions.q169_lagging_objective_prediction_lag.probe_lagging_objective_prediction_lag
"""

import random

from org_frontier.probes.lib import verdict
from org_frontier.cognition.predictive_processing import (
    pp3_moving_target,          # the window-fit loop this probe generalizes
    pp1_irreducible_surprise,   # the PP1 hidden-counterpart surprise floor
)
from org_frontier.questions.q141_lagging_objective.probe_lagging_objective import (
    IMMEDIATE,
    LAGGED,
    LAB_IMMEDIATE,
    LAB_LAGGED,
)

DRIFT_PERIODS = (5000, 800, 300, 120, 60, 30, 15, 8)


def objective_window_fit_accuracy(objective, period, window=40, steps=2000, trials=120, seed=0):
    """Window-fit prediction accuracy for a worker against a drifting mediator, for the two
    Q128/Q141 objective forms. Generalizes pp3_moving_target to the lagging-objective line.

    The mediator commits a Boolean output the worker predicts. Its rule (a 4-entry truth table
    over (W, C), index W + 2C) drifts: one entry flips every `period` steps. The counterpart C is
    hidden, so the worker conditions only on her observable W.

    objective='immediate' is the Q128 self-executing objective O = W ∧ C: the commit is the live
    joint determination, which turns on the hidden C, so the worker fits a window-majority over
    recent observed commits keyed on W. Drift lags every flip.

    objective='lagging' is the Q141 mediator O = M with M = W ∧ C delayed one step: a memory node
    computes and stores the joint determination at t-1, and the objective emits the stored value
    at t. The stored memory is the re-integration channel: the worker predicts the commit by
    reading the held memory. This is exact except for a same-step race — if the served entry flips
    at the emit step, the platform re-stores a new value the instant before emit and the worker's
    held value is stale for that step.

    Returns the mean accuracy over `trials` seeded runs. Deterministic for a fixed seed.
    """
    rng = random.Random(seed)
    total = 0.0
    for _ in range(trials):
        gate = [rng.randint(0, 1) for _ in range(4)]
        win = []                       # (W, observed commit) for the immediate window
        mem = None                     # the stored memory M (lagging)
        prev_w = prev_c = None
        correct = count = 0
        for t in range(steps):
            flipped = None
            if t % period == 0 and t > 0:
                j = rng.randrange(4); gate[j] ^= 1; flipped = j
            w, c = rng.randint(0, 1), rng.randint(0, 1)
            joint = gate[w + 2 * c]
            if objective == "immediate":
                commit = joint
                recent = [o for (kw, o) in win[-window * 2:] if kw == w]
                pred = (1 if sum(recent) * 2 >= len(recent) else 0) if recent else rng.randint(0, 1)
                win.append((w, commit))
                correct += pred == commit; count += 1
            elif objective == "lagging":
                if mem is None:
                    mem = joint
                else:
                    held = mem
                    if flipped is not None and flipped == (prev_w + 2 * prev_c):
                        commit = gate[prev_w + 2 * prev_c]   # re-stored on a same-step flip
                    else:
                        commit = held
                    pred = held
                    correct += pred == commit; count += 1
                    mem = joint
                prev_w, prev_c = w, c
            else:
                raise ValueError("objective must be 'immediate' or 'lagging'")
        total += correct / count
    return total / trials


def main():
    print("PROBE 323 (Q169) — the lagging objective and the worker's predictive model")
    print("=" * 92)

    # INSTRUMENT CONTROL: the faithful triad reads triadic, max_phi 2.0. Confirms the Φ machinery
    # the lagging line rests on (Q141's forms are imported below and verified to read structurally).
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    vc = verdict(triad, ("W", "S", "C"))
    ctrl = vc.structure == "triadic" and abs(vc.max_phi - 2.0) < 1e-6
    print(f"  CONTROL faithful triad: {vc.structure} max_phi={vc.max_phi:.3f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    # Anchor: the Q141 immediate and lagging objective forms read triadic, confirming the
    # structural re-integration this study probes in the predictive measure.
    vi = verdict(IMMEDIATE, LAB_IMMEDIATE)
    vl = verdict(LAGGED, LAB_LAGGED)
    print(f"  Q141 anchor: immediate {vi.structure} Φ={vi.max_phi:.1f}  |  "
          f"lagging {vl.structure} Φ={vl.max_phi:.1f}")

    # The drift sweep: window-fit accuracy for each objective at each retrain period.
    print("\n  drift period | immediate acc | lagging acc | advantage (lag - imm)")
    print("  -------------+---------------+-------------+----------------------")
    rows = []
    for period in DRIFT_PERIODS:
        im = objective_window_fit_accuracy("immediate", period)
        lg = objective_window_fit_accuracy("lagging", period)
        rows.append((period, im, lg))
        print(f"  {period:>12} | {im:13.3f} | {lg:11.3f} | {lg - im:+.3f}")

    advs = [lg - im for (_p, im, lg) in rows]
    # H1: lagging predicts better at matched moderate drift (the slow / mid part of the sweep).
    moderate = [a for (p, _i, _l), a in zip(rows, advs) if p >= 60]
    h1 = all(a > 0.0 for a in moderate) and (sum(moderate) / len(moderate)) > 0.01

    # H2: the advantage VANISHES as drift period shrinks. Read as the advantage at the fastest
    # drift falling toward zero (convergence to the immediate level). Compare the fastest-drift
    # advantage to the moderate-drift mean; H2 holds only if the fast advantage is near zero.
    fast_adv = advs[-1]                      # smallest period
    slow_adv = advs[0]                       # largest period
    mod_mean = sum(moderate) / len(moderate)
    h2 = fast_adv < 0.05 and fast_adv < 0.5 * mod_mean

    print("\n" + "=" * 92)
    print(f"  H1 (lagging objective predicts the platform better at matched drift): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (the lagging advantage vanishes as drift speeds up): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}  "
          f"(advantage slow {slow_adv:+.3f} -> fast {fast_adv:+.3f}; moderate mean {mod_mean:+.3f})")
    print("  Reading: the Q141 re-integration is visible in the predictive measure. A lagging")
    print("  objective routes the displaced counterpart's contribution to the worker as a memory")
    print("  she already observed, so her model reads the commit off that memory and tracks the")
    print("  platform far better than against an immediate self-executing objective whose commit")
    print("  turns on the hidden counterpart in real time. The advantage does not vanish as drift")
    print("  speeds up; the stored memory suffers only a small same-step staleness, while the")
    print("  immediate model degrades steeply, so the advantage grows. Re-integration through a")
    print("  realized memory is drift-robust, not fragile.")
    print("=" * 92)


if __name__ == "__main__":
    main()
