"""Q11 H5 — the detectable band widens with period: grain flips the verdict only at grain >~ p.

H5: reading the rotating ring at a coarser temporal grain flips its verdict to dyadic only near
grain ~ p, and since p = n the n=6 ring tolerates a coarser grain than the n=3 ring (the
grain-flip threshold scales with period, not pinned at k=2).

Form / ensemble: rot_ring(n) (each node copies its left neighbour; a pure cyclic shift of period
n) for n = 3,4,5,6, read under a temporal-grain sweep. The grain-g map is the g-step whole-system
composition of the synchronous next-state map (the #32/#60 k_step coarse-grain composition):
compose the synchronous transition g times into one observed transition, then classify the
composed (tpm, cm) with classify(tpm, cm, labels). g is swept 1,2,3,...,n+1 at each n (covering
the full period p = n and one step past).

Measure: at each n the grain-flip threshold g*(n) = smallest grain g at which the composed map
reads dyadic (Φ_MIP <= PHI_EPS), or 'none in grid' if triadic through g = n+1. The pairing tested
is g*(n) against the attractor period p = period(rot_ring(n)) = n.

Controls: instrument control (run first, abort on failure):
  - ats_strict_bottleneck (strict-mediation triad [x1, x0&x2, x1]) reads triadic Φ_MIP = 2.0,
    MIP `2 parts: {W,SC}`.
  - and_ring(4) reads triadic, max Φ_MIP = 4.0, synchronous period <= 2.
  - and_ring(3) reads triadic, max Φ_MIP = 6.0.
  - parity_hub(5) reads triadic, max Φ_MIP = 2^(2-5) = 0.125.
The positive reference is the corpus grain result #32/#60 where short-period (1-2) forms flip at
g = 2; the ring's longer p = n is the varied input. g = 1 is the grain-1 triadic baseline (from
H1) so the flip is a genuine crossing.

Decision rule (fixed before run):
  CONFIRM H5 if g*(n) is non-decreasing in n with g*(6) > g*(3) (a wider band for the longer-
    period ring) and the flip located near g ~ p = n rather than pinned at 2.
  REFUTE if g*(n) is fixed near 2 for every n (period-independent corpus outcome), OR the ring
    never flips through g = n+1 at any n (no band to scale).

Honest caveat fixed before run: rot_ring is a reversible permutation, so its g-step composition is
again a pure rotation by g positions and may never wash out within a period. If it reads triadic
at every g <= n+1 for all n, that is the 'never flips' refutation branch and H5 is refuted on this
form despite the long period. The rule adjudicates both branches; H5 stands only if a flip is
observed and its location grows with n.

Run:
  ~/iit-playground/venv-4.0/bin/python org_frontier/questions/q11_oscillatory_scaling/probe_probe_q11_grain_band.py
"""

import csv
import os
import sys

# Repo root on the path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import (
    classify, classify_rules, tpm_from_rules, PHI_EPS,
)
from org_frontier.corpus import forms_library as lib
from org_frontier.probes.probe_parity_scaling import parity_hub

N_GRID = (3, 4, 5, 6)
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# ----------------------------------------------------------------------------------------
# The forms (fixed for every test) — methods.md
# ----------------------------------------------------------------------------------------

def rot_ring(n):
    """Rotating-update ring: each node copies its left neighbour; global state rotates one
    position each step. A pure cyclic shift; synchronous attractor period n."""
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules


def and_ring(n):
    """The zoo's capped fixed-point ring (#132): each node is the AND of its two ring
    neighbours. Collapses to a fixed point (period 1-2)."""
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


def labels_for(n):
    return tuple(f"x{i}" for i in range(n))


# ----------------------------------------------------------------------------------------
# Grain-g composition (the #32/#60 k_step coarse-grain composition) and period helper
# ----------------------------------------------------------------------------------------

def grain_g(rules, g, n):
    """g-step whole-system composition of the synchronous next-state map (k_step / #60).

    Compose the synchronous transition g times into one observed transition; return the
    composed state-by-node TPM and its numerically inferred connectivity matrix.
    """
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        return sum(int(rules[j](b)) << j for j in range(n))

    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        t = s
        for _ in range(g):
            t = succ(t)
        for j in range(n):
            tpm[s, j] = float((t >> j) & 1)
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def period(rules, n):
    """Synchronous attractor period: longest cycle length over all 2^n initial states
    under the synchronous next-state map read from tpm_from_rules (methods.md helper)."""
    tpm = tpm_from_rules(rules)
    nxt = lambda s: sum(int(tpm[s, j]) << j for j in range(n))
    mp = 1
    for s0 in range(2 ** n):
        seen = {}
        s = s0
        t = 0
        while s not in seen:
            seen[s] = t
            s = nxt(s)
            t += 1
        mp = max(mp, t - seen[s])
    return mp


# ----------------------------------------------------------------------------------------
# Instrument control (run first; abort on failure)
# ----------------------------------------------------------------------------------------

def instrument_control():
    """Known forms must reproduce their known verdicts before any Q11 value is trusted.

      - ats_strict_bottleneck (strict-mediation triad): triadic, Φ_MIP = 2.0, MIP `2 parts: {W,SC}`.
      - and_ring(4): triadic, max Φ_MIP = 4.0, synchronous period <= 2.
      - and_ring(3): triadic, max Φ_MIP = 6.0.
      - parity_hub(5): triadic, max Φ_MIP = 0.125.
    Raise (abort) on any failure.
    """
    print("INSTRUMENT CONTROL (run first) — known forms reproduce known verdicts")
    print("-" * 78)
    ok = True

    # 1) strict-mediation triad at grain 1.
    v = classify_rules(lib.FORMS_BY_KEY["ats_strict_bottleneck"].rules, labels=("W", "S", "C"))
    passed = (v.structure == "triadic" and abs(v.max_phi - 2.0) <= 1e-6
              and v.mip_partition == "2 parts: {W,SC}")
    ok = ok and passed
    print(f"  ats_strict_bottleneck  verdict={v.structure:<8} Φ_MIP={v.max_phi:.6f} "
          f"MIP={v.mip_partition!r:<18} -> {'PASS' if passed else 'FAIL'}")

    # 2) and_ring(4): triadic, Φ=4.0, synchronous period <= 2.
    v = classify_rules(and_ring(4), labels=labels_for(4))
    p4 = period(and_ring(4), 4)
    passed = (v.structure == "triadic" and abs(v.max_phi - 4.0) <= 1e-6 and p4 <= 2)
    ok = ok and passed
    print(f"  and_ring(4)            verdict={v.structure:<8} Φ_MIP={v.max_phi:.6f} "
          f"period={p4:<10} -> {'PASS' if passed else 'FAIL'}")

    # 3) and_ring(3): triadic, Φ=6.0.
    v = classify_rules(and_ring(3), labels=labels_for(3))
    passed = (v.structure == "triadic" and abs(v.max_phi - 6.0) <= 1e-6)
    ok = ok and passed
    print(f"  and_ring(3)            verdict={v.structure:<8} Φ_MIP={v.max_phi:.6f} "
          f"{'':<17} -> {'PASS' if passed else 'FAIL'}")

    # 4) parity_hub(5): triadic, Φ=0.125.
    v = classify_rules(parity_hub(5), labels=labels_for(5))
    passed = (v.structure == "triadic" and abs(v.max_phi - 0.125) <= 1e-6)
    ok = ok and passed
    print(f"  parity_hub(5)          verdict={v.structure:<8} Φ_MIP={v.max_phi:.6f} "
          f"{'':<17} -> {'PASS' if passed else 'FAIL'}")

    print("-" * 78)
    if not ok:
        raise SystemExit("Instrument control FAILED — aborting; swept values not trusted.")
    print("  instrument control PASSED\n")


# ----------------------------------------------------------------------------------------
# The H5 sweep
# ----------------------------------------------------------------------------------------

def run_n(n):
    """Sweep grain g = 1..n+1 on rot_ring(n). Returns (p, g_star, rows)."""
    rules = rot_ring(n)
    labels = labels_for(n)
    p = period(rules, n)
    rows = []  # (g, phi, structure, mip)
    for g in range(1, n + 2):
        tpm, cm = grain_g(rules, g, n)
        v = classify(tpm, cm, labels=labels)
        rows.append((g, v.max_phi, v.structure, v.mip_partition))
    g_star = None
    for (g, phi, structure, _mip) in rows:
        if phi <= PHI_EPS:  # dyadic
            g_star = g
            break
    return p, g_star, rows


def main():
    print("=" * 78)
    print("Q11 H5 — grain-flip threshold g*(n) vs attractor period p for the rotating ring")
    print("=" * 78)

    instrument_control()

    summary = {}   # n -> (p, g_star)
    csv_rows = []
    for n in N_GRID:
        p, g_star, rows = run_n(n)
        summary[n] = (p, g_star)
        print(f"FORM rot_ring(n={n})  (synchronous attractor period p = {p}; grain g = 1..{n + 1})")
        print(f"  {'g':<4}{'Φ_MIP':<14}{'verdict':<10}{'MIP'}")
        for (g, phi, structure, mip) in rows:
            mark = "  <- g*" if (g_star is not None and g == g_star) else ""
            print(f"  {g:<4}{phi:<14.6f}{structure:<10}{mip}{mark}")
            csv_rows.append({
                "n": n, "period": p, "g": g,
                "phi_mip": f"{phi:.6f}", "verdict": structure,
                "mip": mip,
                "g_star": "none in grid" if g_star is None else g_star,
            })
        gs = "none in grid" if g_star is None else g_star
        print(f"  => period p = {p}, g*(n) = {gs}\n")

    print("=" * 78)
    print("SUMMARY (positive reference #32/#60: short-period 1-2 corpus forms flip at grain g=2)")
    print(f"  {'n':<4}{'period p':<12}{'g*(n)'}")
    for n in N_GRID:
        p, g_star = summary[n]
        gs = "none in grid" if g_star is None else g_star
        print(f"  {n:<4}{p:<12}{gs}")
    print("=" * 78)

    # Decision rule (fixed before run).
    g3 = summary[3][1]
    g6 = summary[6][1]
    g_list = [summary[n][1] for n in N_GRID]
    any_none = any(g is None for g in g_list)
    all_none = all(g is None for g in g_list)

    if all_none:
        verdict = "refuted"
        reason = ("the rotating ring never flips through g = n+1 at any n (no band to scale): "
                  "as a reversible permutation its g-step composition is again a pure rotation "
                  "and never washes out within a period — the 'never flips' branch")
    elif any_none:
        # Some n flip, some do not: g*(n) is not defined for all n, so the
        # non-decreasing-with-g*(6)>g*(3) ordering cannot be established.
        if g3 is None or g6 is None:
            verdict = "refuted"
            reason = ("the ring fails to flip within the grid at n=3 or n=6, so the ordering "
                      "g*(6) > g*(3) is undefined")
        else:
            verdict = "partial"
            reason = ("the ring flips at some n but not all; g*(n) is undefined at some sizes, "
                      "so a clean non-decreasing band cannot be read across the full sweep")
    else:
        non_decreasing = all(g_list[i] <= g_list[i + 1] for i in range(len(g_list) - 1))
        near_period = all(summary[n][1] > 2 for n in N_GRID)  # not pinned at 2
        if non_decreasing and g6 > g3 and near_period:
            verdict = "confirmed"
            reason = (f"g*(n) is non-decreasing in n with g*(6)={g6} > g*(3)={g3} (a wider band "
                      f"for the longer-period ring) and the flip sits near g ~ p = n, not pinned at 2")
        elif all(g == 2 for g in g_list):
            verdict = "refuted"
            reason = ("g*(n) is fixed at 2 for every n (period-independent corpus outcome): "
                      "the flip is pinned at grain 2 and does not scale with the period")
        elif non_decreasing and g6 > g3:
            verdict = "partial"
            reason = (f"g*(n) is non-decreasing with g*(6)={g6} > g*(3)={g3}, but at least one "
                      f"flip lands at g=2 (pinned-at-2 rather than near g ~ p = n), so the "
                      f"period-scaling location is only partly met")
        else:
            verdict = "refuted"
            reason = (f"g*(n) is not non-decreasing with g*(6) > g*(3): g*(3)={g3}, g*(6)={g6}, "
                      f"sequence {g_list} — the band does not widen with the period")

    print(f"VERDICT: {verdict.upper()}")
    print(f"  {reason}")
    print("=" * 78)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "q11_grain_band.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["n", "period", "g", "phi_mip",
                                           "verdict", "mip", "g_star"])
        w.writeheader()
        w.writerows(csv_rows)
    print(f"  wrote {csv_path}")

    return verdict


if __name__ == "__main__":
    main()
