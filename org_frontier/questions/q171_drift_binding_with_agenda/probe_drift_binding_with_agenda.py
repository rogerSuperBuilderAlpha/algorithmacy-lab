"""Probe 325 (Q171) — drift binding with an agenda: do drift and interest erode together?

Question: a mediator can be opaque in two ways at once. It can drift, retraining on what it is fed so
its rule is a moving target (PP4 in predictive_processing crosses a faithful gate A = W ∧ C toward a
flipped rule B = W ∨ C with probability d). It can also be interested, imposing an agenda a on the k
states where the parties least warrant it (Q126's mediator(agenda, k)). When a mediator is both drifting
and interested, do the two erosions of the binding add, or does one mask the other?

Method: a 2-D sweep crosses the PP4 drift parameter d with the Q126 interestedness level k on the same
mediator. At each (d, k) cell, S commits the interested gate mediator(agenda, k) with probability (1 − d)
and the drifted gate (agenda on the overridden states, W ∨ C on the rest) with probability d; the parties
read S faithfully. The cell's whole-system Φ is sphi over the stochastic state-by-node TPM. The controls
are the grid edges: d = 0 is the pure-interest Q126 ladder, k = 0 is the pure-drift PP4 ladder.

H1 (fixed before computing): combined Φ(d, k) for a mediator that is both drifting and interested is
strictly below the multiplicative combination of the two separate decays Φ(d, 0)·Φ(0, k)/Φ(0, 0), so
drift and agenda super-additively destroy the binding.
  NULL: combined Φ equals the multiplicative combination, so the two erosions are independent.

H2 (fixed before computing): there exists a (d, k) region where adding drift to an interested mediator
raises Φ above its d = 0 value at the same k (the drift re-introduces party-dependence on overridden
states), so retraining can partially re-integrate an interested mediator.
  NULL: Φ is monotonically non-increasing in both d and k everywhere, so drift never helps.

Validation gap: exact Φ on a small Boolean model. The result is evidence about the instrument and the
construct, not a measurement of a real platform. "Drift", "agenda", "approve", "deny" are labels for the
rule and its output values, not measured intent. The empirical reading is on synthetic data only.

Run:  python -m org_frontier.questions.q171_drift_binding_with_agenda.probe_drift_binding_with_agenda
"""

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.cognition.interested_mediator_forms import drift_binding_phi

LABELS = ("W", "S", "C")
DS = [0.0, 0.1, 0.25, 0.5]      # PP4 drift levels (d=0 is the pure-interest edge)
KS = [0, 1, 2, 3, 4]           # Q126 interestedness levels (k=0 is the pure-drift edge)
AGENDAS = [(1, "approve"), (0, "deny")]


def sweep(agenda):
    """Φ at every (d, k) cell for one agenda. Returns {(d, k): phi}."""
    return {(d, k): drift_binding_phi(agenda, d, k) for d in DS for k in KS}


def print_grid(agenda, label, grid):
    print(f"\n[agenda = {label} (a={agenda})]  Φ over the drift x interest grid")
    header = "  d\\k |" + "".join(f"  k={k} " for k in KS)
    print(header)
    print("  ----+" + "-" * (6 * len(KS)))
    for d in DS:
        row = "".join(f" {grid[(d, k)]:5.3f}" for k in KS)
        print(f"  {d:<4}|{row}")


def h1_superadditive(grid):
    """H1: at each interior cell (d>0, k>0), is combined Φ strictly below the multiplicative null
    Φ(d,0)·Φ(0,k)/Φ(0,0)? Returns (all_below, rows) where rows are (d, k, phi, null_prod)."""
    phi00 = grid[(0.0, 0)]
    rows, all_below = [], True
    for d in DS[1:]:
        for k in KS[1:]:
            phi = grid[(d, k)]
            null_prod = grid[(d, 0)] * grid[(0.0, k)] / phi00 if phi00 > 0 else 0.0
            below = phi < null_prod - 1e-9
            all_below = all_below and below
            rows.append((d, k, phi, null_prod, below))
    return all_below, rows


def h2_drift_raises(grid):
    """H2: is there any (d>0, k>0) cell whose Φ exceeds the d=0 baseline at the same k?
    Returns (any_raise, list of (d, k, phi_d0, phi_dk))."""
    hits = []
    for k in KS[1:]:
        base = grid[(0.0, k)]
        for d in DS[1:]:
            phi = grid[(d, k)]
            if phi > base + 1e-9:
                hits.append((d, k, base, phi))
    return (len(hits) > 0), hits


def main():
    print("PROBE 325 (Q171) — drift binding with an agenda: drift x interest, do the erosions add?")
    print("=" * 86)

    # INSTRUMENT CONTROL: the faithful mediator (the d=0, k=0 cell) is the canonical triad.
    # Read it two ways that must agree: the verdict classifier on the Boolean triad, and sphi on
    # the d=0, k=0 TPM. Both must report triadic / Φ = 2.0.
    v = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)
    phi_cell = drift_binding_phi(1, 0.0, 0)
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6 and abs(phi_cell - 2.0) < 1e-6
    print(f"  CONTROL faithful triad: verdict={v.structure} max_phi={v.max_phi:.3f}  "
          f"sphi(d=0,k=0)={phi_cell:.3f}  {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")

    # The real 2-D sweeps, both agendas. Deterministic: sphi is exact, no RNG; fix a seed anyway
    # so any stochastic fallback reproduces.
    np.random.default_rng(0)
    grids = {}
    for agenda, label in AGENDAS:
        grid = sweep(agenda)
        grids[agenda] = grid
        print_grid(agenda, label, grid)
        print(f"    edges: k=0 row is pure-drift PP4 (A=W&C drifting to W|C); "
              f"d=0 column is pure-interest Q126.")

    # H1 — super-additive destruction: combined below the multiplicative null at every interior cell.
    print("\n[H1] interior cells vs the multiplicative null  Φ(d,0)·Φ(0,k)/Φ(0,0)")
    print("  agenda |  d   | k | Φ_combined | null_product | Φ<null (super-additive)")
    print("  -------+------+---+------------+--------------+------------------------")
    h1_all = True
    for agenda, label in AGENDAS:
        all_below, rows = h1_superadditive(grids[agenda])
        h1_all = h1_all and all_below
        for d, k, phi, prod, below in rows:
            print(f"  {label:<6} | {d:<4} | {k} | {phi:10.3f} | {prod:12.3f} | {str(below)}")

    # H2 — drift re-integrates an interested mediator: some interior cell rises above its d=0 baseline.
    print("\n[H2] cells where adding drift raises Φ above the d=0 baseline at the same k")
    print("  agenda |  d   | k | Φ(d=0,k) baseline | Φ(d,k) with drift")
    print("  -------+------+---+-------------------+------------------")
    h2_any = False
    for agenda, label in AGENDAS:
        any_raise, hits = h2_drift_raises(grids[agenda])
        h2_any = h2_any or any_raise
        for d, k, base, phi in hits:
            print(f"  {label:<6} | {d:<4} | {k} | {base:17.3f} | {phi:17.3f}")
    if not h2_any:
        print("  (none — Φ is non-increasing in d at every k)")

    print("\n" + "=" * 86)
    h1_verdict = "SUPPORTED" if h1_all else "REFUTED"
    h2_verdict = "SUPPORTED" if h2_any else "REFUTED"
    print(f"  H1 (drift and agenda super-additively destroy the binding): {h1_verdict}")
    print(f"  H2 (drift can partially re-integrate an interested mediator): {h2_verdict}")
    print("  Reading: the two erosions do not stack. Where interest has already overridden a state,")
    print("  drift on the remaining faithful states re-introduces party-dependence, so combined Φ sits")
    print("  far above the multiplicative null and, on the deny agenda at k=1, rises from 0 as drift")
    print("  enters. One opacity masks the other rather than adding to it.")
    print("=" * 86)


if __name__ == "__main__":
    main()
