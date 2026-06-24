"""q157 — Transfer entropy vs DCRP peak-lag for recovering directed read-edge orientation.

QUESTION
On directed read edges across a random Boolean ensemble, does DCRP peak-lag sign or pairwise
transfer entropy more faithfully recover the true edge direction the connectivity matrix encodes?

A read edge i -> j means node j's rule depends on node i (cm[i, j] = 1), so i leads j. Two
behavioral methods read direction from a sampled trajectory:
  DCRP peak-lag sign     - peak lag of the diagonal cross-recurrence profile for the ordered pair
                           (i, j); a positive lag says i leads j.
  pairwise transfer ent. - TE(i -> j) vs TE(j -> i); the larger direction wins.
Each method is scored against the ground-truth orientation from cm_from_rules.

H1 (fixed before computing): pairwise transfer entropy recovers true directed-edge orientation at
a higher rate than DCRP peak-lag sign on the random ensemble, exceeding it by more than 5
percentage points. Null: the two methods recover direction at indistinguishable rates.

H2 (fixed before computing): DCRP and transfer entropy fail on the same edges (common-driver and
reciprocal pairs), so their errors are correlated rather than complementary. The phi coefficient
of the per-edge hit/miss contingency table is positive. Null: their errors are independent, so
combining the two methods would raise recovery above either alone.

METHOD
Forms: a random 3-node (rand_form) and 4-node (rand_form4) ensemble. Ground truth is the directed
read edges of cm_from_rules. For each form, sample one seeded trajectory and, for every true
directed edge, record whether DCRP peak-lag sign and transfer entropy each orient it correctly.
Report per-method recovery, the agreement/disagreement contingency table, the phi coefficient of
the two error vectors, and the recovery of an OR-combine (either method correct).

Scope: in-silico. The forms are synthetic Boolean coordination models scored by exact IIT-4.0 Φ
machinery for ground truth. Every number is a property of these models, not a field measurement.

Run from the repo root:
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q157_te_vs_dcrp_direction.probe_te_vs_dcrp_direction
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "yes")

import numpy as np

from org_frontier.recurrence.crqa import trajectory
from org_frontier.recurrence.crqa_phi_bridge import (
    te_orients_edge, dcrp_orients_edge, transfer_entropy_binary)
from org_frontier.recurrence.crqa_experiments import rand_form
from org_frontier.recurrence.bridge_four import rand_form4
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.probes.lib import verdict

STEPS = 800
FLIP = 0.08
MAX_LAG = 10


def directed_edges(cm):
    """Ordered pairs (i, j) with cm[i, j] = 1 and no self-loop: j reads i, so i leads j."""
    n = cm.shape[0]
    return [(i, j) for i in range(n) for j in range(n) if i != j and cm[i, j]]


def instrument_control():
    """Validate the machinery on the faithful worker-system-counterpart triad.

    The triad [x[1], x[0]&x[2], x[1]] reads verdict 'triadic' with max_phi 2.0. Its wiring is a
    clean directed cycle, so both methods must orient its read edges, and TE must be directional
    on a known one-way driver.
    """
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    assert v.structure == "triadic", f"control verdict {v.structure}, expected triadic"
    assert abs(v.max_phi - 2.0) < 1e-6, f"control max_phi {v.max_phi}, expected 2.0"

    # A clean one-way driver: y copies x's previous state, x is independent noise.
    rng = np.random.default_rng(0)
    x = rng.integers(0, 2, size=2000)
    y = np.empty_like(x)
    y[0] = 0
    y[1:] = x[:-1]
    te_fwd = transfer_entropy_binary(x, y)   # x -> y, the true direction
    te_rev = transfer_entropy_binary(y, x)   # y -> x, the wrong direction
    assert te_fwd > te_rev, f"control TE not directional: fwd {te_fwd}, rev {te_rev}"
    print(f"CONTROL triad verdict={v.structure} max_phi={v.max_phi:.4f}; "
          f"TE driver fwd={te_fwd:.4f} > rev={te_rev:.4f}: PASS")


def run_ensemble(label, draw_form, n_forms, draw_seed, traj_base):
    """Score both methods over an ensemble; return per-edge hit vectors and a summary dict."""
    draw_rng = random.Random(draw_seed)
    dcrp_hits = []
    te_hits = []
    n_with_edges = 0
    for k in range(n_forms):
        rules = draw_form(draw_rng)
        cm = cm_from_rules(rules)
        edges = directed_edges(cm)
        if not edges:
            continue
        n_with_edges += 1
        traj = trajectory(rules, STEPS, random.Random(traj_base + k), flip=FLIP)
        for (i, j) in edges:
            dcrp_hits.append(bool(dcrp_orients_edge(traj, i, j, max_lag=MAX_LAG)))
            te_hits.append(bool(te_orients_edge(traj, i, j)))
    dcrp_hits = np.array(dcrp_hits, dtype=bool)
    te_hits = np.array(te_hits, dtype=bool)
    return {
        "label": label,
        "n_forms": n_forms,
        "n_with_edges": n_with_edges,
        "n_edges": int(dcrp_hits.size),
        "dcrp_hits": dcrp_hits,
        "te_hits": te_hits,
    }


def phi_coefficient(a, b):
    """Phi coefficient between two boolean vectors (here: per-edge hit indicators)."""
    a = np.asarray(a, dtype=int)
    b = np.asarray(b, dtype=int)
    n11 = int(((a == 1) & (b == 1)).sum())
    n10 = int(((a == 1) & (b == 0)).sum())
    n01 = int(((a == 0) & (b == 1)).sum())
    n00 = int(((a == 0) & (b == 0)).sum())
    num = n11 * n00 - n10 * n01
    den = np.sqrt((n11 + n10) * (n01 + n00) * (n11 + n01) * (n10 + n00))
    if den == 0:
        return 0.0, (n11, n10, n01, n00)
    return num / den, (n11, n10, n01, n00)


def main():
    instrument_control()
    print()

    ensembles = [
        run_ensemble("rand_form3", rand_form, n_forms=200, draw_seed=0, traj_base=9000),
        run_ensemble("rand_form4", rand_form4, n_forms=120, draw_seed=1, traj_base=7000),
    ]

    # Pool the two ensembles into the random-ensemble result H1/H2 are stated on.
    dcrp_all = np.concatenate([e["dcrp_hits"] for e in ensembles])
    te_all = np.concatenate([e["te_hits"] for e in ensembles])
    n_edges = int(dcrp_all.size)

    dcrp_rate = float(dcrp_all.mean())
    te_rate = float(te_all.mean())
    or_rate = float((dcrp_all | te_all).mean())
    gap_pp = 100.0 * (te_rate - dcrp_rate)

    print("PER-ENSEMBLE recovery of true directed-edge orientation")
    print(f"  {'ensemble':<12} {'forms':>6} {'w/edges':>8} {'edges':>6} "
          f"{'DCRP':>8} {'TE':>8}")
    for e in ensembles:
        dr = float(e["dcrp_hits"].mean()) if e["n_edges"] else 0.0
        tr = float(e["te_hits"].mean()) if e["n_edges"] else 0.0
        print(f"  {e['label']:<12} {e['n_forms']:>6} {e['n_with_edges']:>8} "
              f"{e['n_edges']:>6} {100*dr:>7.1f}% {100*tr:>7.1f}%")
    print(f"  {'POOLED':<12} {'':>6} {'':>8} {n_edges:>6} "
          f"{100*dcrp_rate:>7.1f}% {100*te_rate:>7.1f}%")
    print()

    print("AGREEMENT contingency (per directed edge, pooled)")
    phi, (n11, n10, n01, n00) = phi_coefficient(dcrp_all, te_all)
    print(f"  both correct       : {n11}")
    print(f"  DCRP only correct  : {n10}")
    print(f"  TE only correct    : {n01}")
    print(f"  both wrong         : {n00}")
    print(f"  phi(DCRP hit, TE hit) = {phi:+.4f}")
    print()

    print("COMBINE (either method correct = OR-rule)")
    print(f"  DCRP recovery : {100*dcrp_rate:.1f}%")
    print(f"  TE recovery   : {100*te_rate:.1f}%")
    print(f"  OR recovery   : {100*or_rate:.1f}%")
    print(f"  OR lift over best single = "
          f"{100*(or_rate - max(dcrp_rate, te_rate)):.1f} pp")
    print()

    # ----- H1 -----
    h1_supported = gap_pp > 5.0
    print(f"H1 (TE beats DCRP peak-lag by > 5 pp on directed-edge orientation): "
          f"{'SUPPORTED' if h1_supported else 'REFUTED'} "
          f"[TE {100*te_rate:.1f}% - DCRP {100*dcrp_rate:.1f}% = {gap_pp:+.1f} pp]")

    # ----- H2 -----
    # H2 predicts correlated errors: phi > 0 AND the OR-combine gives no meaningful lift
    # (errors not complementary). Treat lift <= 1 pp as "no meaningful lift".
    or_lift_pp = 100.0 * (or_rate - max(dcrp_rate, te_rate))
    h2_supported = (phi > 0.0) and (or_lift_pp <= 1.0)
    print(f"H2 (errors correlated, not complementary; phi>0 and OR-lift<=1pp): "
          f"{'SUPPORTED' if h2_supported else 'REFUTED'} "
          f"[phi={phi:+.4f}, OR-lift={or_lift_pp:+.1f} pp]")


if __name__ == "__main__":
    main()
