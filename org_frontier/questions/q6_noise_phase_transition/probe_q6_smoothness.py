"""Q6 / H1 — Mean Φ_MIP decays smoothly across commit noise (no kink, no interior jump).

Form / ensemble: triadic conjunctive mediated chain, n=3, labels ("W","S","C"), clean rules
[x[1], x[0]&x[2], x[1]]  (W'=S, S'=W&C, C'=S; probes #26/#33/#27). Commit noise of strength p is
applied as OUTPUT noise on the mediator column (S, col 1) of the state-by-node TPM:
    P(S'=1) = (1-p)*s_clean + p*(1-s_clean)
so the commit lands on its clean value with reliability 1-p and flips with probability p. The W
and C columns stay deterministic. cm is the clean form's cm_from_rules (the noise rescales
transition probabilities, it does not add/remove a dependency).

Measure: Φ_MIP(p) = max_phi_float(noisy_tpm(p)) on the 51-point uniform grid p=0.00..0.50 step
0.01 (computed once). Fit two smooth low-order forms to the 49 interior points (0.01..0.49) by
least squares — exponential a*exp(-b*p)+c and quadratic a*p^2+b*p+c — take the better fit; record
its max abs residual, per-point residuals, and the second difference d2Phi at every interior point.

Controls:
  (1) Instrument control: clean p=0 endpoint must read triadic, max_phi=2.0 to 1e-6, MIP {W,SC}.
      Halt if it fails.
  (2) Positive kink-detection control: re-run the residual / d2Phi test on an artificial piecewise
      curve = Phi(p) for p<=0.25 then a line that kinks down to 0 at p=0.5; it must produce a
      localized residual / d2Phi spike, proving the test can see a kink.

Decision rule (fixed before run):
  H1 CONFIRMED if the better smooth fit has max |residual| <= 0.02 with no interior point above
  3x the median |residual| AND the largest interior |d2Phi| is below 5x the median interior
  |d2Phi| (no localized spike).
  H1 REFUTED if any interior residual > 0.02, or one interior point shows |d2Phi| above 5x median
  while its neighbors do not.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q6_noise_phase_transition/probe_q6_smoothness.py \
    2>&1 | grep -v 'Welcome to PyPhi'
"""

import csv
import os
import sys

# --- repo root on sys.path so this runs as a direct script and imports org_frontier.* / proxy_audit.* ---
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from scipy.optimize import curve_fit

from org_frontier.classifier.classifier import cm_from_rules, classify, tpm_from_rules
from org_frontier.probes.lib import max_phi_float, verdict

# ------------------------------------------------------------------------------------------------
# Fixed form, noise model, grid
# ------------------------------------------------------------------------------------------------
LABELS = ("W", "S", "C")
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # W'=S, S'=W&C, C'=S
CLEAN_TPM = tpm_from_rules(RULES)        # (8, 3) deterministic
CM = cm_from_rules(RULES)                # clean connectivity matrix, reused for every p
S_CLEAN = CLEAN_TPM[:, 1].copy()         # clean mediator column, in {0,1} per row

GRID = np.round(np.arange(0.0, 0.5 + 1e-9, 0.01), 2)  # 51 points 0.00..0.50
INTERIOR = slice(1, 50)                   # 49 interior points 0.01..0.49
PHI_EPS = 1e-6
RESULTS_DIR = os.path.join(_HERE, "results")


def noisy_tpm(p):
    """Clean TPM with commit (mediator, col 1) output-noise of strength p applied."""
    tpm = CLEAN_TPM.copy()
    tpm[:, 1] = (1.0 - p) * S_CLEAN + p * (1.0 - S_CLEAN)
    return tpm


# ------------------------------------------------------------------------------------------------
# Smooth fits
# ------------------------------------------------------------------------------------------------
def _exp_form(p, a, b, c):
    return a * np.exp(-b * p) + c


def _quad_form(p, a, b, c):
    return a * p * p + b * p + c


def fit_both(xs, ys):
    """Fit exponential and quadratic by least squares; return (name, residuals, params) of the
    better (lower SSE) fit, plus a dict of both for the record."""
    out = {}
    # quadratic — closed form, always succeeds
    qc = np.polyfit(xs, ys, 2)             # [a, b, c]
    q_pred = np.polyval(qc, xs)
    q_res = ys - q_pred
    out["quadratic"] = (q_res, tuple(qc))
    # exponential — nonlinear; seed from data
    try:
        a0 = ys[0] - ys[-1]
        c0 = ys[-1]
        b0 = 5.0
        ep, _ = curve_fit(_exp_form, xs, ys, p0=[a0, b0, c0], maxfev=100000)
        e_pred = _exp_form(xs, *ep)
        e_res = ys - e_pred
        out["exponential"] = (e_res, tuple(ep))
    except Exception as exc:  # pragma: no cover
        out["exponential"] = (np.full_like(ys, np.inf), ("fit-failed", str(exc)))
    e_sse = float(np.sum(out["exponential"][0] ** 2))
    q_sse = float(np.sum(out["quadratic"][0] ** 2))
    best = "exponential" if e_sse <= q_sse else "quadratic"
    return best, out, {"exponential_sse": e_sse, "quadratic_sse": q_sse}


def second_diff(phi, idxs):
    """d2Phi = Phi(k+1) - 2 Phi(k) + Phi(k-1) at the given (interior) global indices."""
    return np.array([phi[k + 1] - 2.0 * phi[k] + phi[k - 1] for k in idxs])


def run_residual_test(xs, ys_full, interior_idxs):
    """Fit the interior, return verdict-relevant diagnostics for one Phi(p) curve.

    xs, ys_full are over the interior grid (49 points). interior_idxs are the GLOBAL grid indices
    of those points (1..49), used for the second difference (which needs neighbours)."""
    best, both, sse = fit_both(xs, ys_full)
    res = both[best][0]
    abs_res = np.abs(res)
    max_abs_res = float(np.max(abs_res))
    med_abs_res = float(np.median(abs_res))
    res_spike_ratio = max_abs_res / med_abs_res if med_abs_res > 0 else float("inf")

    d2 = second_diff(PHI_FULL, interior_idxs)
    abs_d2 = np.abs(d2)
    max_abs_d2 = float(np.max(abs_d2))
    med_abs_d2 = float(np.median(abs_d2))
    d2_spike_ratio = max_abs_d2 / med_abs_d2 if med_abs_d2 > 0 else float("inf")

    return {
        "best_form": best,
        "params": both[best][1],
        "sse": sse,
        "residuals": res,
        "abs_residuals": abs_res,
        "max_abs_res": max_abs_res,
        "med_abs_res": med_abs_res,
        "res_spike_ratio": res_spike_ratio,
        "d2": d2,
        "abs_d2": abs_d2,
        "max_abs_d2": max_abs_d2,
        "med_abs_d2": med_abs_d2,
        "d2_spike_ratio": d2_spike_ratio,
    }


# ------------------------------------------------------------------------------------------------
# Instrument control
# ------------------------------------------------------------------------------------------------
def instrument_control():
    """Clean p=0 endpoint must read triadic, max_phi=2.0 (to 1e-6), MIP a 2-part {W}{SC} cut."""
    v = verdict(RULES, LABELS)
    ok_struct = v.structure == "triadic"
    ok_phi = abs(v.max_phi - 2.0) <= 1e-6
    mip = v.mip_partition
    # MIP must be a 2-part cut isolating W from {S,C}. Accept the canonical reprs.
    mip_l = mip.replace(" ", "")
    ok_mip = ("W" in mip and "S" in mip and "C" in mip
              and ("2parts" in mip_l or mip.count("/") == 1 or mip.count("|") >= 1))
    # also require the p=0 sweep endpoint to reproduce 2.0 via max_phi_float
    phi0, _ = max_phi_float(noisy_tpm(0.0))
    ok_endpoint = abs(phi0 - 2.0) <= 1e-6
    print("INSTRUMENT CONTROL")
    print(f"  verdict(clean): structure={v.structure!r}  max_phi={v.max_phi:.6f}  MIP={mip!r}")
    print(f"  max_phi_float(noisy_tpm(0.0)) = {phi0:.6f}")
    passed = ok_struct and ok_phi and ok_mip and ok_endpoint
    print(f"  -> instrument {'PASS' if passed else 'FAIL'} "
          f"(struct={ok_struct} phi={ok_phi} mip={ok_mip} endpoint={ok_endpoint})")
    if not passed:
        print("HALT: instrument control failed; swept values not trusted.")
        sys.exit(1)
    return phi0


# ------------------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------------------
PHI_FULL = None  # filled in main; module-level so second_diff helpers can reach it


def main():
    global PHI_FULL
    print("=" * 78)
    print("Q6 / H1 — mean Φ_MIP decays smoothly across commit noise (no kink, no jump)")
    print("=" * 78)

    instrument_control()

    # ---- compute the single 51-point sweep once ----
    print("\nΦ_MIP(p) sweep (51 points, p=0.00..0.50 step 0.01):")
    phi = np.zeros(len(GRID))
    for k, p in enumerate(GRID):
        phi[k], _ = max_phi_float(noisy_tpm(float(p)))
    PHI_FULL = phi
    for k, p in enumerate(GRID):
        print(f"  p={p:.2f}  Φ={phi[k]:.6f}")

    interior_idxs = list(range(1, 50))                 # global indices 0.01..0.49
    xs = GRID[INTERIOR].astype(float)
    ys = phi[INTERIOR].astype(float)

    # ---- the real test ----
    print("\n" + "-" * 78)
    print("H1 RESIDUAL / SECOND-DIFFERENCE TEST (real Φ(p) curve, interior 0.01..0.49)")
    print("-" * 78)
    real = run_residual_test(xs, ys, interior_idxs)
    print(f"  fit SSE: exponential={real['sse']['exponential_sse']:.3e}  "
          f"quadratic={real['sse']['quadratic_sse']:.3e}  -> better fit: {real['best_form']}")
    print(f"  fit params ({real['best_form']}): {tuple(round(v, 6) for v in real['params'])}")
    print(f"  max |residual| = {real['max_abs_res']:.6f}   "
          f"median |residual| = {real['med_abs_res']:.6f}   "
          f"max/median = {real['res_spike_ratio']:.2f}x")
    print(f"  max |Δ²Φ| = {real['max_abs_d2']:.6f}   "
          f"median |Δ²Φ| = {real['med_abs_d2']:.6f}   "
          f"max/median = {real['d2_spike_ratio']:.2f}x")
    print("  per-point interior residuals and Δ²Φ:")
    for j, k in enumerate(interior_idxs):
        print(f"    p={GRID[k]:.2f}  Φ={phi[k]:.6f}  resid={real['residuals'][j]:+.6f}  "
              f"Δ²Φ={real['d2'][j]:+.6f}")

    # ---- decision rule on the real curve ----
    # Confirmation (all three): max|resid|<=0.02 AND no interior resid >3x median AND
    #                           largest |Δ²Φ| < 5x median.
    # Refutation (either):      some interior resid > 0.02 OR a localized Δ²Φ spike (>5x median
    #                           with flat neighbours). The 3x-residual sub-clause is a
    #                           confirmation gate only — failing it alone does NOT refute.
    res_mag_ok = real["max_abs_res"] <= 0.02
    res_spike_ok = real["res_spike_ratio"] <= 3.0
    d2_ok = real["d2_spike_ratio"] < 5.0
    confirm = res_mag_ok and res_spike_ok and d2_ok
    refute = (not res_mag_ok) or (not d2_ok)  # a localized Δ²Φ spike or an oversized residual
    if confirm:
        h1_verdict = "CONFIRMED"
    elif refute:
        h1_verdict = "REFUTED"
    else:
        h1_verdict = "PARTIAL"
    print("\n  decision (real curve):")
    print(f"    max|residual| <= 0.02 ............ {real['max_abs_res']:.6f} -> "
          f"{'PASS' if res_mag_ok else 'FAIL'}")
    print(f"    no interior residual > 3x median . ratio {real['res_spike_ratio']:.2f}x -> "
          f"{'PASS' if res_spike_ok else 'FAIL'}")
    print(f"    largest |Δ²Φ| < 5x median ........ ratio {real['d2_spike_ratio']:.2f}x -> "
          f"{'PASS' if d2_ok else 'FAIL'}")
    print(f"    => H1 {h1_verdict}")

    # ---- positive kink-detection control ----
    print("\n" + "-" * 78)
    print("POSITIVE CONTROL — injected corner at p=0.25 (test must SEE a kink)")
    print("-" * 78)
    phi_kink = phi.copy()
    p25_idx = int(np.argmin(np.abs(GRID - 0.25)))
    phi25 = phi[p25_idx]
    for k, p in enumerate(GRID):
        if p > 0.25:
            phi_kink[k] = phi25 * (0.5 - p) / 0.25  # line kinking down to 0 at p=0.5
    # residual/d2 test on the kinked curve (reuse the same machinery; d2 from the kinked curve)
    ks = GRID[INTERIOR].astype(float)
    kys = phi_kink[INTERIOR].astype(float)
    kbest, kboth, ksse = fit_both(ks, kys)
    kres = kboth[kbest][0]
    kabs = np.abs(kres)
    k_max_res, k_med_res = float(np.max(kabs)), float(np.median(kabs))
    k_d2 = np.array([phi_kink[k + 1] - 2 * phi_kink[k] + phi_kink[k - 1] for k in interior_idxs])
    k_absd2 = np.abs(k_d2)
    k_max_d2, k_med_d2 = float(np.max(k_absd2)), float(np.median(k_absd2))
    k_res_ratio = k_max_res / k_med_res if k_med_res > 0 else float("inf")
    k_d2_ratio = k_max_d2 / k_med_d2 if k_med_d2 > 0 else float("inf")
    k_spike_loc = GRID[interior_idxs[int(np.argmax(k_absd2))]]
    print(f"  better fit: {kbest}")
    print(f"  max |residual| = {k_max_res:.6f}  median = {k_med_res:.6f}  "
          f"max/median = {k_res_ratio:.2f}x")
    print(f"  max |Δ²Φ| = {k_max_d2:.6f}  median = {k_med_d2:.6f}  "
          f"max/median = {k_d2_ratio:.2f}x  (spike at p={k_spike_loc:.2f})")
    kink_seen = (k_max_res > 0.02) or (k_res_ratio > 3.0) or (k_d2_ratio >= 5.0)
    print(f"  -> injected corner {'DETECTED (control PASS)' if kink_seen else 'MISSED (control FAIL)'}")

    # ---- write CSV ----
    os.makedirs(RESULTS_DIR, exist_ok=True)
    sweep_csv = os.path.join(RESULTS_DIR, "q6_smoothness_sweep.csv")
    with open(sweep_csv, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["p", "phi_mip", "interior", "residual_bestfit", "d2phi",
                    "kink_control_phi", "kink_control_d2phi"])
        # build interior-indexed lookups
        res_by_k = {k: real["residuals"][j] for j, k in enumerate(interior_idxs)}
        d2_by_k = {k: real["d2"][j] for j, k in enumerate(interior_idxs)}
        kd2_by_k = {k: k_d2[j] for j, k in enumerate(interior_idxs)}
        for k, p in enumerate(GRID):
            inter = 1 if k in res_by_k else 0
            w.writerow([
                f"{p:.2f}", f"{phi[k]:.8f}", inter,
                f"{res_by_k.get(k, float('nan')):.8f}" if inter else "",
                f"{d2_by_k.get(k, float('nan')):.8f}" if inter else "",
                f"{phi_kink[k]:.8f}",
                f"{kd2_by_k.get(k, float('nan')):.8f}" if inter else "",
            ])
    print(f"\nCSV written: {sweep_csv}")

    # ---- final verdict line ----
    print("\n" + "=" * 78)
    verdict_str = h1_verdict
    print(f"H1 VERDICT: {verdict_str}")
    print(f"  Φ(0)={phi[0]:.4f}  Φ(0.5)={phi[-1]:.4f}  best fit={real['best_form']}  "
          f"max|resid|={real['max_abs_res']:.4f}  d2 spike={real['d2_spike_ratio']:.2f}x  "
          f"kink-control={'spikes' if kink_seen else 'flat'}")
    print("=" * 78)
    return {"CONFIRMED": 0, "PARTIAL": 1, "REFUTED": 2}[h1_verdict]


if __name__ == "__main__":
    sys.exit(main())
