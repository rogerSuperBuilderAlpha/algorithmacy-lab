"""Q9 H4 — the verdict-flip ratio is tied to the form's synchronous attractor period.

H4: the hold-for-k verdict-flip ratio k* is tied to the form's synchronous attractor period
(a longer-period form flips at a larger k); it is not a period-independent grain-2 constant.

Construction: deterministic hold-for-k (methods.md, construction A) on two forms of differing
synchronous attractor period:
  - gig_false_dyad   rules [1-x1, x0&x2, x2&(1-x1)]  — period 1
  - two_sided_match  rules [x1, x0&x2, x1]            — period 2
Period is computed by attractor_period(rules) from probe_grain_threshold.py (longest cycle over
all initial states under the synchronous map). hold_k_tpm is built for k = 1..6 on each form and
the strict verdict-flip ratio k*_det is the smallest grid k reading dyadic (Φ_MIP <= PHI_EPS).

Decision rule (fixed before run):
  CONFIRMED if k*_det(period-2 two_sided_match) > k*_det(period-1 gig_false_dyad).
  REFUTED   if both flip at the same k*_det (period-independent), or the ordering runs opposite
            to period.

Instrument control (run first, abort on failure): both forms read triadic at k=1, Φ_MIP = 2.0,
MIP `2 parts: {W,SC}`. If the control fails the swept values are not trusted.

Run:
  ~/iit-playground/venv-4.0/bin/python org_frontier/questions/q9_timescale_separation/probe_period_lock.py
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

from org_frontier.classifier.classifier import classify, classify_rules, PHI_EPS
from org_frontier.corpus import forms_library as lib
from org_frontier.probes.probe_grain_threshold import attractor_period

LABELS = ("W", "S", "C")
S_IDX = 1
K_GRID = list(range(1, 7))  # 1..6
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def hold_k_tpm(rules, k, n=3, s_idx=S_IDX):
    """Deterministic hold-for-k composed map (methods.md construction A).

    Inside one observed transition, k micro-steps run. Parties apply their rules every
    micro-step; S holds its own value for the first k-1 micro-steps and commits its
    conjunctive update on the k-th. The observed transition is the macro-state after the
    full k-window.
    """
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]          # S holds its previous value
        return ns

    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))  # commit only on the k-th micro-step
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def instrument_control():
    """Both forms must read triadic at k=1, Φ_MIP = 2.0, MIP `2 parts: {W,SC}`.

    The k=1 hold_k_tpm reduces to the synchronous map. Abort (raise) on any failure.
    """
    print("INSTRUMENT CONTROL (run first) — k=1 endpoints reproduce the corpus verdict")
    print("-" * 78)
    ok = True
    for key in ("gig_false_dyad", "two_sided_match"):
        rules = lib.FORMS_BY_KEY[key].rules
        tpm, cm = hold_k_tpm(rules, 1)
        v = classify(tpm, cm, labels=LABELS)
        triadic = v.structure == "triadic"
        phi_ok = abs(v.max_phi - 2.0) <= 1e-6
        mip_ok = v.mip_partition == "2 parts: {W,SC}"
        passed = triadic and phi_ok and mip_ok
        ok = ok and passed
        print(f"  {key:<18} verdict={v.structure:<8} Φ_MIP={v.max_phi:.6f} "
              f"MIP={v.mip_partition!r:<20} -> {'PASS' if passed else 'FAIL'}")
    print("-" * 78)
    if not ok:
        raise SystemExit("Instrument control FAILED — aborting; swept values not trusted.")
    print("  instrument control PASSED\n")


def flip_ratio(profile_rows):
    """Smallest grid k whose verdict reads dyadic (Φ_MIP <= PHI_EPS), else None."""
    for k, phi, structure in profile_rows:
        if structure == "dyadic":
            return k
    return None


def run_form(key):
    """Sweep hold_k_tpm over k=1..6 on one form. Returns (period, k_star, rows)."""
    rules = lib.FORMS_BY_KEY[key].rules
    period = attractor_period(rules)
    rows = []  # (k, phi, structure, mip)
    for k in K_GRID:
        tpm, cm = hold_k_tpm(rules, k)
        v = classify(tpm, cm, labels=LABELS)
        rows.append((k, v.max_phi, v.structure, v.mip_partition))
    k_star = flip_ratio([(k, phi, st) for (k, phi, st, _) in rows])
    return period, k_star, rows


def main():
    print("=" * 78)
    print("Q9 H4 — verdict-flip ratio k* vs synchronous attractor period (hold-for-k, S-only)")
    print("=" * 78)

    instrument_control()

    forms = ["gig_false_dyad", "two_sided_match"]  # period 1, period 2
    summary = {}
    csv_rows = []
    for key in forms:
        period, k_star, rows = run_form(key)
        summary[key] = (period, k_star)
        print(f"FORM {key}  (synchronous attractor period P = {period})")
        print(f"  {'k':<4}{'Φ_MIP':<14}{'verdict':<10}{'MIP'}")
        for (k, phi, structure, mip) in rows:
            mark = "  <- k*_det" if (k == k_star) else ""
            print(f"  {k:<4}{phi:<14.6f}{structure:<10}{mip}{mark}")
            csv_rows.append({
                "form": key, "period": period, "k": k,
                "phi_mip": f"{phi:.6f}", "verdict": structure,
                "mip": mip, "k_star_det": k_star,
            })
        print(f"  => period P = {period}, k*_det = {k_star}\n")

    p1_period, p1_kstar = summary["gig_false_dyad"]
    p2_period, p2_kstar = summary["two_sided_match"]

    print("=" * 78)
    print("CONTRAST (positive reference #60: whole-system grain-k flips BOTH at grain 2)")
    print(f"  gig_false_dyad   period P={p1_period}  k*_det={p1_kstar}")
    print(f"  two_sided_match  period P={p2_period}  k*_det={p2_kstar}")
    print("=" * 78)

    # Decision rule (fixed before run):
    #   CONFIRMED iff k*_det(period-2) > k*_det(period-1).
    #   REFUTED   iff same k*_det (period-independent) or ordering opposite to period.
    if p1_kstar is None or p2_kstar is None:
        verdict = "refuted"
        reason = ("a form did not flip within the grid; the flip ratio is undefined, "
                  "so the period-tracking ordering cannot hold")
    elif p2_kstar > p1_kstar:
        verdict = "confirmed"
        reason = (f"longer-period form flips at strictly larger k: "
                  f"k*_det(P={p2_period})={p2_kstar} > k*_det(P={p1_period})={p1_kstar}")
    elif p2_kstar == p1_kstar:
        verdict = "refuted"
        reason = (f"both forms flip at the same k*_det={p1_kstar} (period-independent); "
                  f"the grain-2 hold spans a full cycle on the period-1 form")
    else:
        verdict = "refuted"
        reason = (f"ordering runs opposite to period: k*_det(P={p2_period})={p2_kstar} "
                  f"< k*_det(P={p1_period})={p1_kstar}")

    print(f"VERDICT: {verdict.upper()}")
    print(f"  {reason}")
    print("=" * 78)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "q9_period_lock.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["form", "period", "k", "phi_mip",
                                           "verdict", "mip", "k_star_det"])
        w.writeheader()
        w.writerows(csv_rows)
    print(f"  wrote {csv_path}")

    return verdict


if __name__ == "__main__":
    main()
