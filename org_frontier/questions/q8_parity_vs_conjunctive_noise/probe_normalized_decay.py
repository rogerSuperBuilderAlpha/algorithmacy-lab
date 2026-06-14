"""Q8 / H2 — parity Φ decays faster than conjunctive Φ in flip fraction (normalized decay).

Hypothesis (H2): the parity hub sheds a larger *fraction* of its clean Φ than the conjunctive
hub does, at matched n — a faster normalized decay, not merely a smaller absolute magnitude.

Forms and noise model (methods.md, fixed for every Q8 test). Node 0 is the hub S; nodes
1..n-1 are parties, each reading the hub (party' = S). The two forms differ only in the commit
rule on node 0:
  - Parity (XOR) hub:        S' = x[1] ^ x[2] ^ ... ^ x[n-1]   (parity_hub(n), #115).
                             Clean Φ = 2^(2-n) (0.5 at n=3, 0.25 at n=4), triadic.
  - Conjunctive (AND) hub:   S' = x[1] & x[2] & ... & x[n-1]   (single_hub(n), #116).
                             Clean Φ = n-1 (2.0 at n=3, 3.0 at n=4), triadic.
Both run at n=3 and n=4; labels = tuple(f"n{i}" for i in range(n)).

Flip-noise of strength p is output noise on the hub column (node 0): the clean column value
sc in {0,1} per row is replaced by P(S'=1) = (1-p)*sc + p*(1-sc). Party columns stay
deterministic. Φ_MIP(p) = max_phi_float(noisy_tpm(rules, p))[0] (max exact IIT-4.0 Φ over
reachable states, cm inferred numerically).

Grid (fixed before run): p = 0.00, 0.01, ..., 0.50 (51 points, step 0.01). The four sweeps
(parity-n3, parity-n4, conjunctive-n3, conjunctive-n4) are each computed once.

Normalized curve: Φ̂_form,n(p) = Φ_form,n(p) / Φ_form,n(0); drop fraction f = 1 - Φ̂.

Measure (matched n, parity vs conjunctive):
  (a) count of interior grid points p in {0.01..0.49} where f_parity,n(p) > f_conj,n(p)
      (parity has shed the larger fraction);
  (b) clean-limit log-slope L_form,n = |log Φ̂_form,n(0.01)| / 0.01 (since Φ̂(0)=1).

Controls:
  - Instrument control (run first, abort on failure): the strict-mediation triad
    (W'=S, S'=W&C, C'=S) must read triadic at Φ=2.0; and the four clean p=0 endpoints must
    all give Φ̂=1 (triadic, with their tabled clean Φ).
  - Self/identity control: each normalized curve against itself, f - f ≡ 0, must yield 0
    interior points won, so the point-count statistic reads zero for identical curves.

Decision rule (fixed before run): CONFIRMED if at BOTH n=3 and n=4
    f_parity,n(p) > f_conj,n(p) at all 49 interior p  AND  L_parity,n > L_conj,n.
REFUTED if at either size f_conj,n(p) >= f_parity,n(p) at any interior p, or
    L_conj,n >= L_parity,n.

Pre-registration trial (honest): the conjunctive form sheds the LARGER fraction at every
interior p at both sizes (n=3 p=0.1: Φ̂_parity=0.763 vs conj=0.594; n=4 p=0.1: 0.763 vs
0.407), opposite to H2's direction, and the parity normalized curve is n-independent
(identical at n=3 and n=4). On that evidence H2 is expected to be REFUTED.

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q8_parity_vs_conjunctive_noise/probe_normalized_decay.py
"""

import csv
import math
import os
import sys

# Repo root on sys.path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import max_phi_float
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_distributed_mediators import single_hub

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

# The fixed 51-point grid p = 0.00, 0.01, ..., 0.50.
GRID = [round(k * 0.01, 2) for k in range(51)]
GRID_STEP = 0.01
TOL = 1e-6

# Interior grid points p in {0.01, ..., 0.49} (49 points).
INTERIOR = [p for p in GRID if 0.0 < p < 0.5]

# The four sweeps: (form, n) with its rule builder and tabled clean Φ.
FORMS = [
    ("parity", 3, parity_hub, 0.5),
    ("parity", 4, parity_hub, 0.25),
    ("conjunctive", 3, single_hub, 2.0),
    ("conjunctive", 4, single_hub, 3.0),
]


def labels_for(n):
    return tuple(f"n{i}" for i in range(n))


def noisy_tpm(rules, n, p):
    """State-by-node TPM with flip-noise p as output noise on the hub column (node 0).

    The clean hub value sc in {0,1} per row becomes P(S'=1) = (1-p)*sc + p*(1-sc): the commit
    lands on its clean value with reliability 1-p and flips with probability p. Party columns
    stay deterministic.
    """
    t = tpm_from_rules(rules, n=n).copy()
    sc = t[:, 0]
    t[:, 0] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def instrument_control():
    """Run first; abort on failure.

    (1) Known-form reproduces its known verdict: the strict-mediation triad
        (W'=S, S'=W&C, C'=S) reads triadic at Φ=2.0.
    (2) The four clean p=0 endpoints reproduce their tabled clean Φ and triadic, so Φ̂(0)=1.
    """
    print("INSTRUMENT CONTROL")
    triad_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = classify_rules(triad_rules, labels=("W", "S", "C"))
    ok_triad = (v.structure == "triadic") and (abs(v.max_phi - 2.0) <= 1e-6)
    print(f"  strict-mediation triad: structure={v.structure}  max_phi={v.max_phi:.6f}  "
          f"-> ok={ok_triad}")

    ok_endpoints = True
    for form, n, build, clean_phi in FORMS:
        rules = build(n)
        phi0, _ = max_phi_float(noisy_tpm(rules, n, 0.0))
        ok = abs(phi0 - clean_phi) <= 1e-6 and phi0 > PHI_EPS
        ok_endpoints = ok_endpoints and ok
        phihat0 = phi0 / clean_phi
        print(f"  {form:<11} n={n}: clean Φ={phi0:.6f} (tabled {clean_phi})  "
              f"Φ̂(0)={phihat0:.6f}  triadic={phi0 > PHI_EPS}  ok={ok}")

    passed = ok_triad and ok_endpoints
    print(f"  control passed: {passed}")
    print("=" * 72)
    if not passed:
        sys.exit("ABORT: instrument control failed; swept values not trusted.")


def sweep(form, n, build):
    """Return the list of Φ_MIP(p) over the 51-point grid for one (form, n) sweep."""
    rules = build(n)
    phis = []
    for p in GRID:
        phi, _ = max_phi_float(noisy_tpm(rules, n, p))
        phis.append(phi)
    return phis


def main():
    instrument_control()

    print("Q8 / H2 — parity vs conjunctive normalized decay across the 51-point flip-noise grid")
    print("=" * 72)
    print(f"  grid: {len(GRID)} points p=0.00..0.50 step {GRID_STEP}; "
          f"{len(INTERIOR)} interior points p=0.01..0.49")
    print("=" * 72)

    # --- Compute the four sweeps and their normalized curves / drop fractions. ---
    raw = {}        # (form, n) -> [Φ(p)]
    phihat = {}     # (form, n) -> {p: Φ̂(p)}
    frac = {}       # (form, n) -> {p: f(p)=1-Φ̂(p)}
    clean = {}      # (form, n) -> Φ(0)

    for form, n, build, _clean_phi in FORMS:
        phis = sweep(form, n, build)
        raw[(form, n)] = phis
        phi0 = phis[0]
        clean[(form, n)] = phi0
        hat = {p: phis[i] / phi0 for i, p in enumerate(GRID)}
        phihat[(form, n)] = hat
        frac[(form, n)] = {p: 1.0 - hat[p] for p in GRID}
        print(f"{form:<11} n={n}: clean Φ(0)={phi0:.6f}")
        for p in (0.05, 0.10, 0.20, 0.30, 0.40):
            print(f"    p={p:.2f}  Φ={hat[p]*phi0:.6f}  Φ̂={hat[p]:.6f}  f={1.0 - hat[p]:.6f}")
    print("-" * 72)

    # --- Write per-(form,n) sweep CSV. ---
    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q8_normalized_decay.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "n", "p", "phi_mip", "phi_hat", "drop_fraction"])
        for form, n, _build, _clean_phi in FORMS:
            for i, p in enumerate(GRID):
                w.writerow([form, n, p, round(raw[(form, n)][i], 9),
                            round(phihat[(form, n)][p], 9),
                            round(frac[(form, n)][p], 9)])

    # --- Self/identity control: each normalized curve against itself must win 0 interior points. ---
    print("SELF / IDENTITY CONTROL (f_form,n - f_form,n ≡ 0 must give 0 interior points won)")
    self_ok = True
    for form, n, _build, _clean_phi in FORMS:
        f = frac[(form, n)]
        won = sum(1 for p in INTERIOR if f[p] > f[p])  # strictly greater than itself: always 0
        self_ok = self_ok and (won == 0)
        print(f"  {form:<11} n={n}: interior points where f > f = {won}")
    print(f"  self-control passed: {self_ok}")
    print("-" * 72)
    if not self_ok:
        sys.exit("ABORT: self/identity control failed; point-count statistic is not zero on "
                 "identical curves.")

    # --- Measure (a): interior points where f_parity > f_conj, at matched n. ---
    # --- Measure (b): clean-limit log-slope L = |log Φ̂(0.01)| / 0.01. ---
    def log_slope(form, n):
        hat01 = phihat[(form, n)][0.01]
        return abs(math.log(hat01)) / GRID_STEP

    results = {}
    print("PER-SIZE COMPARISON (parity vs conjunctive at matched n)")
    for n in (3, 4):
        fpar = frac[("parity", n)]
        fconj = frac[("conjunctive", n)]
        # (a) count interior points where parity sheds strictly larger fraction.
        par_wins = sum(1 for p in INTERIOR if fpar[p] > fconj[p] + 0.0)
        conj_ge = [p for p in INTERIOR if fconj[p] >= fpar[p]]  # conj >= parity (refute trigger)
        # (b) clean-limit log-slopes.
        L_par = log_slope("parity", n)
        L_conj = log_slope("conjunctive", n)
        results[n] = {
            "par_wins": par_wins,
            "n_interior": len(INTERIOR),
            "conj_ge_count": len(conj_ge),
            "L_par": L_par,
            "L_conj": L_conj,
        }
        print(f"  n={n}:")
        print(f"    (a) interior points where f_parity > f_conj: {par_wins} / {len(INTERIOR)}")
        print(f"        interior points where f_conj >= f_parity: {len(conj_ge)} "
              f"(first few: {conj_ge[:5]})")
        print(f"    (b) clean-limit log-slope  L_parity={L_par:.6f}  L_conj={L_conj:.6f}  "
              f"(L_parity > L_conj: {L_par > L_conj})")
        # Spot values at p=0.10 for the record.
        print(f"        at p=0.10: Φ̂_parity={phihat[('parity', n)][0.10]:.6f}  "
              f"Φ̂_conj={phihat[('conjunctive', n)][0.10]:.6f}")
    print("-" * 72)

    # --- Decision rule (fixed before run). ---
    def size_confirms(n):
        r = results[n]
        a = (r["par_wins"] == r["n_interior"])             # all 49 interior won by parity
        b = (r["L_par"] > r["L_conj"])                     # steeper parity log-slope
        return a and b

    def size_refutes(n):
        r = results[n]
        a = (r["conj_ge_count"] > 0)                       # conj >= parity at some interior p
        b = (r["L_conj"] >= r["L_par"])                    # conj log-slope at least as steep
        return a or b

    confirmed = size_confirms(3) and size_confirms(4)
    refuted = size_refutes(3) or size_refutes(4)

    if confirmed:
        verdict = "CONFIRMED"
    elif refuted:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"

    print("DECISION")
    for n in (3, 4):
        r = results[n]
        print(f"  n={n}: parity-wins-all-interior={r['par_wins'] == r['n_interior']}  "
              f"L_parity>L_conj={r['L_par'] > r['L_conj']}  "
              f"conj>=parity-count={r['conj_ge_count']}")
    print("=" * 72)
    print(f"  H2 VERDICT: {verdict}")
    print(f"  CSV: {csv_path}")
    return verdict, results, phihat


if __name__ == "__main__":
    main()
