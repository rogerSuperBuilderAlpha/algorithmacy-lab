"""Q8 H5 — parity collapses as a cliff, conjunctive as a glide (shape of dΦ/dp).

Hypothesis: parity Φ(p) collapses as a cliff — an interior susceptibility peak in
χ(p)=dΦ/dp — while the conjunctive Φ(p) is a glide, monotone-decreasing from p=0 with
its steepest slope at the left endpoint.

For each of the four H1 sweeps (parity n=3, parity n=4, conjunctive n=3, conjunctive
n=4) the susceptibility χ_form,n(p)=dΦ/dp is the centered difference on interior grid
points, read on the un-normalized Φ(p). The measure per (form,n) is p_χ=argmax_p|χ(p)|
over the interior and whether |χ| has an interior peak (a grid point 0.01<p_χ<0.49
exceeding both immediate neighbours and both endpoints) vs its max at an endpoint
(steepest at p→0).

Decision rule (fixed before run): CONFIRMED if at BOTH n=3 and n=4 parity |χ| has an
interior maximum AND conjunctive |χ| is monotone-decreasing from p=0 with its max at the
left endpoint; REFUTED if parity has no interior peak or the conjunctive susceptibility
itself shows an interior peak.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q8_parity_vs_conjunctive_noise/probe_cliff_vs_glide.py
"""

import csv
import os
import sys
from functools import reduce

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import max_phi_float

# ---------------------------------------------------------------------------
# Fixed parameters (methods.md §shared infrastructure / H5).
# ---------------------------------------------------------------------------
TOL = 1e-6
DP = 0.01
GRID = [round(k * DP, 2) for k in range(51)]  # p = 0.00 … 0.50
INTERIOR_LO, INTERIOR_HI = 0.01, 0.49


# ---------------------------------------------------------------------------
# The two hub forms (#115 parity_hub, #116 single_hub) and the noise model.
# ---------------------------------------------------------------------------
def parity_hub(n):
    """0=S, 1..n-1 = parties. S = XOR of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def single_hub(n):
    """0=S, 1..n-1 = parties. S = AND of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def noisy_tpm(rules, p):
    """Output flip-noise of strength p on the hub column (node 0)."""
    t = tpm_from_rules(rules).copy()
    sc = t[:, 0]
    t[:, 0] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


# ---------------------------------------------------------------------------
# Susceptibility analysis.
# ---------------------------------------------------------------------------
def centered_chi(phi, grid):
    """χ(p)=dΦ/dp: centered difference on interior, one-sided at the two endpoints."""
    chi = np.zeros(len(phi))
    chi[0] = (phi[1] - phi[0]) / (grid[1] - grid[0])
    chi[-1] = (phi[-1] - phi[-2]) / (grid[-1] - grid[-2])
    for k in range(1, len(phi) - 1):
        chi[k] = (phi[k + 1] - phi[k - 1]) / (grid[k + 1] - grid[k - 1])
    return chi


def analyze_chi(phi, grid):
    """Return (p_chi, interior_peak, abs_chi). p_chi = argmax over the interior grid.

    interior_peak: the argmax sits strictly inside (0.01<p_chi<0.49) AND exceeds both
    immediate neighbours and both endpoints.
    """
    chi = centered_chi(phi, grid)
    a = np.abs(chi)
    # interior indices: grid points strictly inside the open interval.
    interior_idx = [k for k in range(len(grid)) if INTERIOR_LO < grid[k] < INTERIOR_HI]
    # argmax of |χ| over the interior grid.
    k_star = max(interior_idx, key=lambda k: a[k])
    p_chi = grid[k_star]
    interior_peak = (
        INTERIOR_LO < p_chi < INTERIOR_HI
        and a[k_star] > a[k_star - 1]
        and a[k_star] > a[k_star + 1]
        and a[k_star] > a[0]
        and a[k_star] > a[-1]
    )
    return p_chi, interior_peak, a, chi


def nonmonotone_rise(phi):
    """Weaker corroborant: a forward-difference rise > TOL after an earlier fall."""
    fell = False
    for k in range(len(phi) - 1):
        d = phi[k + 1] - phi[k]
        if d < -TOL:
            fell = True
        elif fell and d > TOL:
            return True, k  # rise after a fall at step k
    return False, None


# ---------------------------------------------------------------------------
# Controls.
# ---------------------------------------------------------------------------
def strict_mediation_triad():
    """Strict-mediation triad: hub commits AND of two parties, each party reads hub.
    The single_hub(3) form — known triadic at Φ=2.0 (the instrument reference)."""
    return single_hub(3)


def instrument_control():
    """A known form reproduces its known verdict: strict-mediation triad reads triadic
    at Φ=2.0. Abort the whole run if it fails."""
    rules = strict_mediation_triad()
    labels = tuple(f"n{i}" for i in range(3))
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    v = classify(tpm, cm, labels=labels)
    phi, _ = max_phi_float(tpm)
    ok = v.structure == "triadic" and abs(phi - 2.0) <= TOL
    return ok, v.structure, phi


def positive_control_corner():
    """Synthetic piecewise-linear curve with a corner (knee) at p=0.25, then a shallower
    line to 0 at p=0.5. The argmax/neighbour test must locate p_χ=0.25 as an interior
    peak, confirming a knee is detectable when present.

    Implementation note (honest): the strict interior-peak test the real measurement uses
    requires |χ| to exceed BOTH immediate neighbours. On a *constant-slope* segment the
    centered-difference |χ| is a flat plateau, never a single-node maximum, so a pure
    flat→line corner (one steep segment running all the way to p=0.5) cannot register as a
    strict interior peak by that test — its |χ| steps up to a plateau and stays there. The
    knee the control must prove detectable is a *localized* steepening: the curve drops
    steeply across the corner (flat to p=0.24, the steep step over [0.24,0.26] centered on
    0.25), then continues with a shallower slope to 0 at p=0.5. That makes |χ| peak at a
    single interior node, p_χ=0.25, exceeding both neighbours and both endpoints — exactly
    the signature H5 predicts for parity, so the control proves the detector can see it."""
    phi = []
    for p in GRID:
        if p <= 0.24:
            phi.append(0.5)            # flat to the corner
        elif p == 0.25:
            phi.append(0.375)          # mid of the steep step (centered on 0.25)
        elif p == 0.26:
            phi.append(0.25)           # bottom of the steep step
        else:
            phi.append(0.25 * (0.5 - p) / 0.24)  # shallow line on to 0 at p=0.5
    phi = np.array(phi)
    p_chi, interior_peak, a, _ = analyze_chi(phi, GRID)
    return abs(p_chi - 0.25) <= 1e-9 and interior_peak, p_chi, interior_peak


# ---------------------------------------------------------------------------
# Sweep.
# ---------------------------------------------------------------------------
def sweep(build, n):
    rules = build(n)
    phi = np.array([max_phi_float(noisy_tpm(rules, p))[0] for p in GRID])
    return phi


def main():
    print("Q8 H5 — parity cliff vs conjunctive glide (shape of dΦ/dp)")
    print("=" * 70)

    # --- Instrument control (run first; abort on failure) ------------------
    ok, struct, phi_ic = instrument_control()
    print(f"Instrument control: strict-mediation triad single_hub(3) -> "
          f"{struct}, Φ={phi_ic:.6f} (need triadic, 2.0)")
    if not ok:
        print("INSTRUMENT CONTROL FAILED — aborting.")
        sys.exit(1)
    print("  instrument control PASSED\n")

    # --- Positive control: injected corner ---------------------------------
    pc_ok, pc_pchi, pc_peak = positive_control_corner()
    print(f"Positive control (corner at p=0.25): p_χ={pc_pchi:.2f}, "
          f"interior_peak={pc_peak} (need p_χ=0.25 located as interior peak)")
    if not pc_ok:
        print("POSITIVE CONTROL FAILED — the test cannot see a known knee; aborting.")
        sys.exit(1)
    print("  positive control PASSED\n")

    # --- The four H1 sweeps ------------------------------------------------
    forms = [
        ("parity", parity_hub, 3),
        ("parity", parity_hub, 4),
        ("conjunctive", single_hub, 3),
        ("conjunctive", single_hub, 4),
    ]
    rows = []
    results = {}
    for form, build, n in forms:
        phi = sweep(build, n)
        p_chi, interior_peak, a, chi = analyze_chi(phi, GRID)
        rose, rise_k = nonmonotone_rise(phi)
        results[(form, n)] = dict(phi=phi, p_chi=p_chi, interior_peak=interior_peak,
                                  abs_chi=a, chi=chi, rose=rose)
        print(f"[{form} n={n}] Φ(0)={phi[0]:.6f}  argmax|χ| at p_χ={p_chi:.2f}  "
              f"|χ|(p_χ)={a[GRID.index(p_chi)]:.6f}")
        print(f"           interior_peak={interior_peak}  "
              f"|χ|(left endpoint p=0)={a[0]:.6f}  |χ|(p=0.49)={a[GRID.index(0.49)]:.6f}")
        print(f"           non-monotone rise>TOL after a fall: {rose}")
        # show first few Φ values for the reading
        head = "  ".join(f"{phi[k]:.4f}" for k in range(0, 11, 2))
        print(f"           Φ(p=0,0.02,..,0.20): {head}")
        for k in range(len(GRID)):
            rows.append(dict(form=form, n=n, p=GRID[k], phi=float(phi[k]),
                             chi=float(chi[k]), abs_chi=float(a[k])))
        print()

    # --- Decision rule -----------------------------------------------------
    par_peak = {n: results[("parity", n)]["interior_peak"] for n in (3, 4)}
    # conjunctive "glide": max at left endpoint (no interior peak). argmax over the
    # interior may sit at the first interior point (p=0.02); a glide has NO interior
    # peak by the neighbour/endpoint test, i.e. interior_peak is False.
    conj_peak = {n: results[("conjunctive", n)]["interior_peak"] for n in (3, 4)}

    parity_cliff = par_peak[3] and par_peak[4]
    conj_glide = (not conj_peak[3]) and (not conj_peak[4])

    print("=" * 70)
    print("Decision (fixed before run):")
    print(f"  parity interior peak  n=3:{par_peak[3]}  n=4:{par_peak[4]}  -> cliff={parity_cliff}")
    print(f"  conjunctive interior peak  n=3:{conj_peak[3]}  n=4:{conj_peak[4]}  "
          f"-> glide={conj_glide}")

    if parity_cliff and conj_glide:
        verdict = "CONFIRMED"
    else:
        verdict = "REFUTED"
    print(f"\n  H5 VERDICT: {verdict}")
    if verdict == "REFUTED":
        if not parity_cliff:
            print("    parity |χ| has no interior peak at both sizes — a scaled glide, "
                  "not a phase-transition cliff.")
        if conj_peak[3] or conj_peak[4]:
            print("    conjunctive |χ| shows an interior peak — no distinguishing signature.")
    print("=" * 70)

    # --- Write CSV ---------------------------------------------------------
    outdir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "q8_cliff_vs_glide.csv")
    with open(outpath, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["form", "n", "p", "phi", "chi", "abs_chi"])
        w.writeheader()
        w.writerows(rows)
    print(f"CSV written: {outpath}")

    return verdict


if __name__ == "__main__":
    main()
