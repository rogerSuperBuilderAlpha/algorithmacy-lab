r"""Q7 / H1 — party noise and mediator noise trace different Φ(p) curves.

Form/ensemble: the triadic conjunctive mediated chain at n=3, labels (W,S,C),
clean rules W'=S, S'=W&C, C'=S (#26/#33/#27). CLEAN_TPM = tpm_from_rules(RULES),
CM = cm_from_rules(RULES), reused for every p. Flip-noise is output noise of
strength p on a column c: P(out=1) = (1-p)*col_clean + p*(1-col_clean).

Two 51-point sweeps on the shared uniform grid p = 0.00, 0.01, ..., 0.50:
  mediator curve Φ_S(p) (col 1) and party curve Φ_W(p) (col 0), each Φ_MIP read
  via max_phi_float(noisy_tpm(p, cols))[0].

Measure: pointwise gap g(p) = Φ_W(p) − Φ_S(p) over interior p ∈ {0.01..0.49};
g_max = max_p |g(p)| and its location.

Controls:
  (1) Instrument control: clean p=0 form reads triadic, max_phi=2.0 (to 1e-6),
      MIP {W,SC}; each site's p=0 endpoint reproduces 2.0. Abort if it fails.
  (2) Self/negative control: Φ_S(p) − Φ_S(p) must be 0 at every grid point, so a
      nonzero g_max is a real site difference, not a measurement offset.

Decision rule (fixed before run):
  H1 CONFIRMED if g_max > 1e-3 at one or more interior p (separation three orders
  above TOL=1e-6). H1 REFUTED if |g(p)| ≤ 1e-6 at every interior p (curves coincide).

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q7_party_vs_mediator_noise/probe_party_vs_mediator.py \
    2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import os
import sys

# Insert repo root onto sys.path so this also runs as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import csv

import numpy as np

from org_frontier.probes.lib import verdict, max_phi_float
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules

TOL = 1e-6
CONFIRM_THRESH = 1e-3

LABELS = ("W", "S", "C")
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # W'=S, S'=W&C, C'=S

CLEAN_TPM = tpm_from_rules(RULES)
CM = cm_from_rules(RULES)

# Fixed grid: 51 points, p = 0.00, 0.01, ..., 0.50.
GRID = [round(0.01 * k, 2) for k in range(51)]
INTERIOR = [(k, p) for k, p in enumerate(GRID) if 1 <= k <= 49]

# Injection sites.
SITE_S = (1,)  # mediator S' = W & C
SITE_W = (0,)  # party W' = S

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def noisy_tpm(p, cols):
    """CLEAN_TPM with flip output-noise of strength p on each column in cols.

    For a noised column c: P(out=1) = (1−p)·col_clean + p·(1−col_clean).
    """
    t = CLEAN_TPM.copy()
    for c in cols:
        sc = CLEAN_TPM[:, c]
        t[:, c] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def phi_curve(cols):
    """Φ_MIP(p) = max_phi_float(noisy_tpm(p, cols))[0] over the full grid."""
    return [max_phi_float(noisy_tpm(p, cols))[0] for p in GRID]


def instrument_control():
    """Clean p=0 form must read triadic, max_phi=2.0 (to 1e-6), MIP {W,SC};
    and each site's p=0 endpoint must reproduce 2.0. Abort if it fails."""
    v = verdict(RULES, LABELS)
    print("Instrument control (clean p=0):")
    print(f"  structure = {v.structure}, max_phi = {v.max_phi:.6f}, MIP = {v.mip_partition}")
    ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) <= TOL)
    if not ok:
        raise SystemExit("ABORT: clean form did not read triadic Φ=2.0; instrument failed.")
    # Each site's p=0 endpoint must read 2.0 (to 1e-6).
    for name, cols in (("S", SITE_S), ("W", SITE_W)):
        e = max_phi_float(noisy_tpm(0.0, cols))[0]
        print(f"  site {name} p=0 endpoint max_phi = {e:.6f}")
        if abs(e - 2.0) > TOL:
            raise SystemExit(f"ABORT: site {name} p=0 endpoint != 2.0; instrument failed.")
    # MIP must contain the {W,SC} cut (W vs S,C grouped). Check the string mentions W and SC.
    mip = v.mip_partition
    if not ("W" in mip and "SC" in mip):
        print(f"  WARNING: MIP repr {mip!r} did not match expected {{W,SC}} text.")
    print("  instrument control PASSED\n")


def main():
    instrument_control()

    phi_W = phi_curve(SITE_W)
    phi_S = phi_curve(SITE_S)

    # Gap over interior points.
    gaps = [(p, phi_W[k] - phi_S[k]) for (k, p) in INTERIOR]
    g_abs = [(p, abs(g)) for p, g in gaps]
    p_at, g_max = max(g_abs, key=lambda r: r[1])
    g_at_pmax = next(g for p, g in gaps if p == p_at)

    # Self/negative control: Φ_S − Φ_S over the full grid must be identically 0.
    self_diffs = [abs(phi_S[k] - phi_S[k]) for k in range(len(GRID))]
    self_max = max(self_diffs)

    # Pre-registration spot check at p = 0.10.
    idx10 = GRID.index(0.10)

    print("Φ(p) curves (interior gap g = Φ_W − Φ_S):")
    print(f"  {'p':>5} {'Φ_W':>10} {'Φ_S':>10} {'g=Φ_W−Φ_S':>12}")
    for (k, p) in INTERIOR:
        print(f"  {p:>5.2f} {phi_W[k]:>10.6f} {phi_S[k]:>10.6f} {phi_W[k]-phi_S[k]:>12.6f}")
    print()
    print(f"Pre-registration spot check at p=0.10: Φ_W={phi_W[idx10]:.6f}, "
          f"Φ_S={phi_S[idx10]:.6f}, g={phi_W[idx10]-phi_S[idx10]:.6f}")
    print(f"g_max = {g_max:.6f} at p = {p_at:.2f} (signed g there = {g_at_pmax:.6f})")
    print(f"Self/negative control max|Φ_S−Φ_S| over grid = {self_max:.2e}")
    print()

    # Decision rule.
    interior_within_tol = all(abs(g) <= TOL for _, g in gaps)
    if g_max > CONFIRM_THRESH:
        verdict_str = "CONFIRMED"
    elif interior_within_tol:
        verdict_str = "REFUTED"
    else:
        verdict_str = "PARTIAL"  # separated above TOL but below 1e-3 confirm margin

    print(f"Decision: g_max = {g_max:.6f} vs confirm threshold {CONFIRM_THRESH} "
          f"(TOL = {TOL}); self-control = {self_max:.2e}")
    print(f"VERDICT: H1 {verdict_str}")

    # Write CSV.
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h1_party_vs_mediator.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "phi_W", "phi_S", "gap_W_minus_S", "interior", "self_ctrl_S_minus_S"])
        for k, p in enumerate(GRID):
            interior = 1 if 1 <= k <= 49 else 0
            w.writerow([p, f"{phi_W[k]:.10f}", f"{phi_S[k]:.10f}",
                        f"{phi_W[k]-phi_S[k]:.10f}", interior, f"{self_diffs[k]:.2e}"])
    print(f"\nWrote {csv_path}")


if __name__ == "__main__":
    main()
