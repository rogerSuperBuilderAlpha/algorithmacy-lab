"""Q7 / H2 — W-noise and C-noise give the same Phi(p) curve as each other.

Hypothesis (H2): flip-noise on the party column W alone and on the party column C
alone produce identical Phi_MIP(p) over the shared 51-point grid, identical
verdict-flip points, so the "party site" can be reported as one curve.

Form: triadic conjunctive mediated chain, n=3, labels ("W","S","C"), clean rules
    W' = S ;  S' = W & C ;  C' = S         (#26/#33/#27)
Noise model: output flip-noise of strength p on selected node columns (Q6/#140-144):
    col_noisy = (1-p)*col_clean + p*(1-col_clean)
Sites:  S=cols(1,)  W=cols(0,)  C=cols(2,)

H2 test:
  - Two 51-point sweeps Phi_W(p) (cols=(0,)) and Phi_C(p) (cols=(2,)) on the grid
    p = 0.00, 0.01, ..., 0.50.
  - d(p) = Phi_W(p) - Phi_C(p) at all 51 grid points; count |d|>TOL; max|d|.
  - verdict-flip point of each site = smallest p where classify(...).structure
    reads "dyadic".
Controls:
  - Instrument control (run first, abort on failure): clean strict-mediation triad
    reads triadic at max_phi = 2.0, MIP {W,SC}; and noisy_tpm(0.0, cols) = 2.0 for
    every site (S, W, C).
  - W<->C swap (#55) maps cols (0)<->(2) and both clean cols equal S, so the overlay
    is exact.
  - Positive control: Phi_W vs the mediator curve Phi_S through the same d(p)
    machinery -- must report many |d|>TOL points and a nonzero max (the H1 gap),
    proving d(p) is not zero by construction.
Decision rule (fixed before run):
  CONFIRMED iff |d(p)| <= 1e-6 at every one of the 51 grid points AND the two sites'
  flip points are identical.
  REFUTED if any |d(p)| > 1e-6 or the flip points differ.
Pre-registration: exact overlay, 0/51 flips, identical flip at p=0.5.

Run:
  ~/iit-playground/venv-4.0/bin/python \
      org_frontier/questions/q7_party_vs_mediator_noise/probe_wc_symmetry.py
"""

import os
import sys

# Repo root onto sys.path so org_frontier.* and proxy_audit.* import when run as a
# direct script. This file is org_frontier/questions/q7_party_vs_mediator_noise/...,
# so the repo root is three directories up.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import csv

import numpy as np

from org_frontier.classifier.classifier import (
    classify,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import max_phi_float, verdict

# --------------------------------------------------------------------------------------
# Fixed form, noise model, grid, tolerance
# --------------------------------------------------------------------------------------
LABELS = ("W", "S", "C")
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # W'=S, S'=W&C, C'=S
CLEAN_TPM = tpm_from_rules(RULES)
CM = cm_from_rules(RULES)

TOL = 1e-6
GRID = [round(0.01 * k, 2) for k in range(51)]  # 0.00, 0.01, ..., 0.50

SITES = {"S": (1,), "W": (0,), "C": (2,)}

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def noisy_tpm(p, cols):
    """Output flip-noise of strength p on the given columns (Q6/#140-144 model)."""
    t = CLEAN_TPM.copy().astype(float)
    for c in cols:
        sc = CLEAN_TPM[:, c]
        t[:, c] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def phi_of(p, cols):
    """Phi_MIP(p) = max exact IIT-4.0 Phi over reachable states for the noised TPM."""
    return max_phi_float(noisy_tpm(p, cols))[0]


def structure_of(p, cols):
    """Binary verdict ('triadic'/'dyadic') at strength p for the noised site."""
    return classify(noisy_tpm(p, cols), CM, labels=LABELS).structure


def flip_point(cols):
    """Smallest grid p at which the site reads 'dyadic'; None if it never flips."""
    for p in GRID:
        if structure_of(p, cols) == "dyadic":
            return p
    return None


# --------------------------------------------------------------------------------------
# Instrument control (run first; abort on failure)
# --------------------------------------------------------------------------------------
def instrument_control():
    v = verdict(RULES, LABELS)
    assert v.structure == "triadic", f"instrument: structure={v.structure!r}, want triadic"
    assert abs(v.max_phi - 2.0) <= TOL, f"instrument: max_phi={v.max_phi}, want 2.0"
    # MIP must read the {W,SC} 2-part split.
    assert "W" in v.mip_partition and "SC" in v.mip_partition.replace(" ", ""), (
        f"instrument: mip_partition={v.mip_partition!r}, want {{W,SC}}"
    )
    # Each site's p=0 left endpoint must reproduce the clean triad value 2.0.
    for name, cols in SITES.items():
        phi0 = phi_of(0.0, cols)
        assert abs(phi0 - 2.0) <= TOL, (
            f"instrument: site {name} phi(p=0)={phi0}, want 2.0"
        )
    return v


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("Q7 / H2 -- W-noise and C-noise give the same Phi(p) curve as each other")
    print("=" * 78)

    # 1) Instrument control -- abort if it fails.
    v = instrument_control()
    print("[instrument control] PASS")
    print(f"  clean verdict: structure={v.structure}, max_phi={v.max_phi:.6f}, "
          f"MIP={v.mip_partition}")
    print(f"  noisy_tpm(0.0, cols) = 2.0 for sites: {', '.join(SITES)}")
    print()

    # 2) The two H2 sweeps on the shared grid.
    phi_W = [phi_of(p, SITES["W"]) for p in GRID]
    phi_C = [phi_of(p, SITES["C"]) for p in GRID]
    phi_S = [phi_of(p, SITES["S"]) for p in GRID]  # for the positive control

    d = [phi_W[k] - phi_C[k] for k in range(len(GRID))]
    abs_d = [abs(x) for x in d]
    n_over = sum(1 for x in abs_d if x > TOL)
    max_d = max(abs_d)
    p_max_d = GRID[int(np.argmax(abs_d))]

    flip_W = flip_point(SITES["W"])
    flip_C = flip_point(SITES["C"])

    # 3) Positive control: Phi_W vs Phi_S through the same d(p) machinery (H1 gap).
    g = [phi_W[k] - phi_S[k] for k in range(len(GRID))]
    abs_g = [abs(x) for x in g]
    n_over_pc = sum(1 for x in abs_g if x > TOL)
    max_g = max(abs_g)
    p_max_g = GRID[int(np.argmax(abs_g))]

    # 4) Report.
    print("--- H2 measure: d(p) = Phi_W(p) - Phi_C(p) over 51 grid points ---")
    print(f"  points with |d| > TOL ({TOL:g}): {n_over} / {len(GRID)}")
    print(f"  max |d| = {max_d:.3e}  at p = {p_max_d}")
    print(f"  flip point W (first p reading dyadic): {flip_W}")
    print(f"  flip point C (first p reading dyadic): {flip_C}")
    print()
    print("  per-point (p, Phi_W, Phi_C, d):")
    for k, p in enumerate(GRID):
        flag = "  <-- |d|>TOL" if abs_d[k] > TOL else ""
        print(f"    p={p:>4} : Phi_W={phi_W[k]:.6f}  Phi_C={phi_C[k]:.6f}  "
              f"d={d[k]:+.3e}{flag}")
    print()

    print("--- positive control: Phi_W vs Phi_S (must see the H1 gap) ---")
    print(f"  points with |W-S| > TOL: {n_over_pc} / {len(GRID)}")
    print(f"  max |W-S| = {max_g:.6f}  at p = {p_max_g}")
    pc_ok = n_over_pc > 0 and max_g > TOL
    print(f"  positive control {'PASS' if pc_ok else 'FAIL'} "
          f"(d(p) machinery flags a real gap)")
    print()

    # 5) Decision rule.
    overlay_exact = all(x <= TOL for x in abs_d)
    flips_identical = flip_W == flip_C
    confirmed = overlay_exact and flips_identical
    verdict_str = "CONFIRMED" if confirmed else "REFUTED"

    print("--- decision (fixed before run) ---")
    print(f"  |d(p)| <= TOL at every grid point : {overlay_exact}")
    print(f"  flip points identical             : {flips_identical} "
          f"(W={flip_W}, C={flip_C})")
    print(f"  VERDICT: H2 {verdict_str}")
    print()

    # 6) CSV out.
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "wc_symmetry.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "phi_W", "phi_C", "phi_S", "d_WC", "abs_d_WC",
                    "over_tol_WC", "g_WS", "abs_g_WS"])
        for k, p in enumerate(GRID):
            w.writerow([p, f"{phi_W[k]:.10f}", f"{phi_C[k]:.10f}",
                        f"{phi_S[k]:.10f}", f"{d[k]:.3e}", f"{abs_d[k]:.3e}",
                        int(abs_d[k] > TOL), f"{g[k]:.3e}", f"{abs_g[k]:.3e}"])
    print(f"[csv] wrote {csv_path}")

    return {
        "verdict": verdict_str,
        "n_over": n_over,
        "max_d": max_d,
        "p_max_d": p_max_d,
        "flip_W": flip_W,
        "flip_C": flip_C,
        "pc_n_over": n_over_pc,
        "pc_max_g": max_g,
        "pc_ok": pc_ok,
        "csv": csv_path,
    }


if __name__ == "__main__":
    main()
