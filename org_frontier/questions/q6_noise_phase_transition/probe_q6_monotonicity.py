r"""Q6 / H5 — Φ_MIP is strictly monotone-decreasing in commit noise (no interior Φ maximum).

Form/ensemble: the 51-point Φ(p) sweep over the noisy conjunctive mediated chain
(W'=S, S'=W&C, C'=S; #26/#33/#27), commit noise applied as output noise on the
mediator column of the state-by-node TPM. p = 0.00, 0.01, ..., 0.50 (step 0.01).

Measure: forward differences δ_k = Φ(p_{k+1}) − Φ(p_k), k = 0..49. Count any δ_k > tol
(Φ rises) with tol = 1e-6; locate any interior local maximum (δ_{k−1} > tol and
δ_k < −tol) other than the p=0 left endpoint.

Controls:
  (1) Instrument control: the clean p=0 form must read triadic, max_phi=2.0 (to 1e-6),
      MIP {W,SC}; max_phi_float(noisy_tpm(0.0)) must return 2.0. Abort if it fails.
  (2) Positive rebound-detection control: the symmetric #81 tracking-phase U-shape
      (Φ=2.0 at p=0 and p=1, 0 at p=0.5) must register δ_k > tol on its rising right
      half, proving the test detects a non-monotone rise when one is present.

Decision rule (fixed before run):
  H5 confirmed if every δ_k ≤ tol (Φ non-increasing at every step) with no interior
  local maximum. H5 refuted if any δ_k > tol on the commit-noise sweep or an interior
  local Φ maximum exists.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q6_noise_phase_transition/probe_q6_monotonicity.py \
    2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import os
import sys

# Insert repo root onto sys.path so this runs as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import csv

import numpy as np

from org_frontier.probes.lib import verdict, max_phi_float
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules

TOL = 1e-6

LABELS = ("W", "S", "C")
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # W'=S, S'=W&C, C'=S

# Fixed grid: 51 points, p = 0.00, 0.01, ..., 0.50.
GRID = [round(0.01 * k, 2) for k in range(51)]

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def noisy_tpm(p):
    """Clean state-by-node TPM with commit (mediator S') output noise of strength p.

    P(S'=1) = (1−p)·s_clean + p·(1−s_clean). W and C columns stay deterministic.
    """
    tpm = tpm_from_rules(RULES).astype(float).copy()
    s_clean = tpm[:, 1]
    tpm[:, 1] = (1.0 - p) * s_clean + p * (1.0 - s_clean)
    return tpm


def run_instrument_control():
    """Clean p=0 form must read triadic, max_phi=2.0 (to 1e-6), MIP {W,SC}.
    max_phi_float(noisy_tpm(0.0)) must also return 2.0. Abort if it fails."""
    v = verdict(RULES, LABELS)
    ok_struct = v.structure == "triadic"
    ok_phi = abs(v.max_phi - 2.0) <= 1e-6
    ok_mip = v.mip_partition == "2 parts: {W,SC}"
    phi0, _ = max_phi_float(noisy_tpm(0.0))
    ok_sweep0 = abs(phi0 - 2.0) <= 1e-6
    print("[instrument control]")
    print(f"  verdict.structure   = {v.structure!r}  (expect 'triadic')  -> {ok_struct}")
    print(f"  verdict.max_phi     = {v.max_phi:.6f}  (expect 2.0)        -> {ok_phi}")
    print(f"  verdict.mip         = {v.mip_partition!r}  (expect '2 parts: {{W,SC}}') -> {ok_mip}")
    print(f"  max_phi_float(p=0)  = {phi0:.6f}  (expect 2.0)        -> {ok_sweep0}")
    passed = ok_struct and ok_phi and ok_mip and ok_sweep0
    assert passed, "Instrument control FAILED; aborting (swept values not trusted)."
    print("  instrument control PASSED\n")


def monotonicity_report(name, ps, phis):
    """Return (deltas, n_rises, rise_indices, interior_max_indices) and print the report."""
    phis = np.asarray(phis, dtype=float)
    deltas = np.diff(phis)  # delta_k = phi[k+1] - phi[k], k = 0 .. len-2
    rise_indices = [int(k) for k in range(len(deltas)) if deltas[k] > TOL]
    n_rises = len(rise_indices)
    # Interior local maximum: delta_{k-1} > tol and delta_k < -tol (a rise then a fall),
    # excluding the p=0 left endpoint (k-1 == 0 is allowed; the endpoint exclusion means
    # we do not count a peak that sits exactly at the leftmost grid point p=0, i.e. k=0).
    interior_max = []
    for k in range(1, len(deltas)):
        if deltas[k - 1] > TOL and deltas[k] < -TOL:
            interior_max.append(int(k))  # peak at vertex ps[k]
    print(f"[{name}]")
    print(f"  n points = {len(phis)}, n forward differences = {len(deltas)}")
    print(f"  rises (delta_k > tol={TOL:g}): count = {n_rises}")
    if rise_indices:
        for k in rise_indices:
            print(f"    k={k:2d}  p {ps[k]:.2f}->{ps[k+1]:.2f}  delta = {deltas[k]:+.6e}")
    print(f"  interior local maxima (delta_{{k-1}}>tol and delta_k<-tol, excl. p=0 left endpoint): "
          f"count = {len(interior_max)}")
    for k in interior_max:
        print(f"    interior peak at p = {ps[k]:.4f}  (delta_{{k-1}}={deltas[k-1]:+.4e}, "
              f"delta_k={deltas[k]:+.4e})")
    print(f"  min delta = {deltas.min():+.6e}, max delta = {deltas.max():+.6e}")
    print()
    return deltas, n_rises, rise_indices, interior_max


def main():
    run_instrument_control()

    # --- The commit-noise sweep (51 points). ---
    print("[commit-noise sweep] computing Φ_MIP(p) at 51 grid points ...")
    phis = []
    for p in GRID:
        phi, _ = max_phi_float(noisy_tpm(p))
        phis.append(phi)
    phis = np.asarray(phis, dtype=float)
    print(f"  Φ(0.00)={phis[0]:.6f}  Φ(0.10)={phis[10]:.6f}  Φ(0.25)={phis[25]:.6f}  "
          f"Φ(0.50)={phis[50]:.6f}\n")

    deltas, n_rises, rise_idx, interior_max = monotonicity_report(
        "monotonicity — commit-noise sweep", GRID, phis)

    # --- Positive rebound-detection control: the #81 symmetric U-shape. ---
    # Φ = 2.0 at p=0 and p=1, 0 at p=0.5; symmetric tracking-phase profile that rises
    # on its right half. Built analytically as Φ(p) = 2.0 * (2p - 1)^2 (a parabola with
    # vertex Φ=0 at p=0.5 and Φ=2.0 at p=0 and p=1) sampled on the SAME 51-point spacing,
    # but over the full p in [0,1] so the rising right half is included.
    ctl_ps = [round(0.02 * k, 2) for k in range(51)]  # 0.00 .. 1.00
    ctl_phis = np.array([2.0 * (2.0 * p - 1.0) ** 2 for p in ctl_ps], dtype=float)
    c_deltas, c_rises, c_rise_idx, c_interior_max = monotonicity_report(
        "rebound-detection control — #81 symmetric U-shape", ctl_ps, ctl_phis)
    control_ok = c_rises > 0
    print(f"  control detects a rise (expect True): {control_ok}\n")

    # --- Decision rule. ---
    sweep_monotone = (n_rises == 0)
    no_interior_peak = (len(interior_max) == 0)
    confirmed = sweep_monotone and no_interior_peak
    verdict_str = "confirmed" if confirmed else "refuted"

    print("[decision]")
    print(f"  every delta_k <= tol on the commit-noise sweep : {sweep_monotone} "
          f"(n_rises = {n_rises})")
    print(f"  no interior local Φ maximum                     : {no_interior_peak} "
          f"(n_interior_peaks = {len(interior_max)})")
    print(f"  positive control flags the U-shape rise         : {control_ok} "
          f"(control n_rises = {c_rises})")
    print(f"  VERDICT: H5 {verdict_str.upper()}")
    if not control_ok:
        print("  WARNING: positive control did NOT flag a rise — test sensitivity unproven.")
    print()

    # --- Write CSV. ---
    os.makedirs(RESULTS_DIR, exist_ok=True)
    sweep_csv = os.path.join(RESULTS_DIR, "q6_monotonicity_sweep.csv")
    with open(sweep_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "phi", "delta_forward", "rise_gt_tol", "interior_local_max_vertex"])
        for k, p in enumerate(GRID):
            d = deltas[k] if k < len(deltas) else ""
            rise = (k < len(deltas) and deltas[k] > TOL)
            peak = (k in interior_max)
            w.writerow([f"{p:.2f}", f"{phis[k]:.10f}",
                        (f"{d:.10e}" if d != "" else ""), int(rise), int(peak)])
    ctl_csv = os.path.join(RESULTS_DIR, "q6_monotonicity_control_u_shape.csv")
    with open(ctl_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "phi", "delta_forward", "rise_gt_tol"])
        for k, p in enumerate(ctl_ps):
            d = c_deltas[k] if k < len(c_deltas) else ""
            rise = (k < len(c_deltas) and c_deltas[k] > TOL)
            w.writerow([f"{p:.2f}", f"{ctl_phis[k]:.10f}",
                        (f"{d:.10e}" if d != "" else ""), int(rise)])
    print(f"  wrote {sweep_csv}")
    print(f"  wrote {ctl_csv}")

    return confirmed


if __name__ == "__main__":
    main()
