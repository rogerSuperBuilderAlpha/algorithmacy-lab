#!/usr/bin/env python
r"""Q6 / H2 — the phase-transition signature lives in the susceptibility dΦ/dp, not in mean Φ.

H2: the sharp feature of the noisy conjunctive chain is in the susceptibility χ(p) = dΦ/dp,
which peaks at an interior p, while mean Φ(p) itself is smooth (H1).

Form / ensemble (fixed, shared with H1): the triadic conjunctive mediated chain at n=3,
labels (W,S,C), clean rules W' = S, S' = W & C, C' = S (#26/#33/#27). Commit noise of
strength p is output noise on the mediator (S') column of the state-by-node TPM:
    P(S'=1 | row) = (1-p)*s_clean + p*(1-s_clean),
so the commit lands on its clean value with reliability 1-p and flips with probability p.
W and C columns stay deterministic. The connectivity matrix is the clean form's
cm_from_rules(...). Φ_MIP(p) is read with max_phi_float(noisy_tpm(p)).

Grid (fixed before run): p = 0.00, 0.01, ..., 0.50 (51 points, step 0.01). The single sweep
is computed once. The susceptibility is the centered difference
    χ(p_k) = (Φ(p_{k+1}) - Φ(p_{k-1})) / (2*0.01)
on interior points, forward/backward differences at the two endpoints.

Measure: p_χ = argmax_p |χ(p)| and the shape of |χ(p)| — recorded at every interior point,
its maximum located, and checked that it rises to that maximum and falls on both sides (a
single interior peak) versus being largest at an endpoint.

Controls: instrument control (run first) — the clean form at p=0 must read triadic,
max_phi = 2.0 (to 1e-6), MIP "2 parts: {W,SC}"; abort if it fails. H2 is read jointly with
H1: it counts as a susceptibility-not-mean result only if H1 (mean Φ smooth) holds on the
same sweep; H1 is re-checked here (better of exponential / quadratic fit, max interior
residual <= 0.02, no localized Δ²Φ spike).

Decision rule (fixed before run): H2 is confirmed if |χ(p)| has an interior maximum — an
interior grid point p_χ with 0.01 < p_χ < 0.49 where |χ(p_χ)| exceeds both immediate
neighbors and exceeds |χ| at each endpoint — while H1 holds. H2 is refuted if |χ| is
monotone or attains its maximum at an endpoint. A maximum forced onto the first interior
point p=0.01 with |χ| monotone-decreasing thereafter is scored as an endpoint peak, not
interior. Predicted: |χ| peaks at an interior p_χ biased toward small p and falls on either
side (Niizato 2020 / Popiel 2020).

Run:
  ~/iit-playground/venv-4.0/bin/python \
      org_frontier/questions/q6_noise_phase_transition/probe_q6_susceptibility.py \
      2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import csv
import os
import sys

# Repo root onto sys.path so this runs as a direct script and via the package.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict, max_phi_float

# ---------------------------------------------------------------------------
# The form and the noise model (fixed for every Q6 test)
# ---------------------------------------------------------------------------
LABELS = ("W", "S", "C")
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # W'=S, S'=W&C, C'=S
COMMIT_COL = 1          # the mediator S' column
STEP = 0.01
GRID = [round(k * STEP, 2) for k in range(51)]  # 0.00, 0.01, ..., 0.50


def noisy_tpm(p):
    """State-by-node TPM with commit (output) noise of strength p on the mediator column."""
    tpm = tpm_from_rules(RULES).astype(float)
    s_clean = tpm[:, COMMIT_COL]
    tpm[:, COMMIT_COL] = (1.0 - p) * s_clean + p * (1.0 - s_clean)
    return tpm


# ---------------------------------------------------------------------------
# Instrument control
# ---------------------------------------------------------------------------
def instrument_control():
    """The clean form at p=0 must read triadic, max_phi=2.0 (1e-6), MIP '2 parts: {W,SC}'."""
    v = verdict(RULES, LABELS)
    ok_struct = v.structure == "triadic"
    ok_phi = abs(v.max_phi - 2.0) <= 1e-6
    ok_mip = "{W,SC}" in v.mip_partition.replace(" ", "")
    # The p=0 endpoint of the sweep must reproduce 2.0 via the stochastic-TPM path too.
    phi0, _ = max_phi_float(noisy_tpm(0.0))
    ok_sweep = abs(phi0 - 2.0) <= 1e-6
    print("INSTRUMENT CONTROL (clean form, p=0):")
    print(f"  verdict.structure   = {v.structure!r}        (need 'triadic')   -> {ok_struct}")
    print(f"  verdict.max_phi     = {v.max_phi:.6f}     (need 2.0 +/-1e-6) -> {ok_phi}")
    print(f"  verdict.mip         = {v.mip_partition!r} -> {ok_mip}")
    print(f"  max_phi_float(p=0)  = {phi0:.6f}     (need 2.0 +/-1e-6) -> {ok_sweep}")
    if not (ok_struct and ok_phi and ok_mip and ok_sweep):
        print("INSTRUMENT CONTROL FAILED — aborting; swept values are not trusted.")
        sys.exit(1)
    print("  PASS\n")


# ---------------------------------------------------------------------------
# H1 re-check on the same sweep (smoothness of mean Φ) — H2 counts only if H1 holds
# ---------------------------------------------------------------------------
def h1_holds(grid, phi):
    """Return (holds, info) re-checking H1: better smooth fit max interior residual <= 0.02
    with no point > 3x median, and no localized Δ²Φ spike (largest interior |Δ²Φ| < 5x median).
    """
    g = np.array(grid)
    f = np.array(phi)
    interior_mask = (g > 0.0) & (g < 0.5)            # the 49 points 0.01..0.49
    gi, fi = g[interior_mask], f[interior_mask]

    # Exponential fit  Φ = a*exp(-b*p) + c  (least squares over a grid of b, linear in a,c).
    def fit_exp(x, y):
        best = None
        for b in np.linspace(0.01, 30.0, 4000):
            basis = np.column_stack([np.exp(-b * x), np.ones_like(x)])
            coef, *_ = np.linalg.lstsq(basis, y, rcond=None)
            resid = y - basis @ coef
            sse = float(resid @ resid)
            if best is None or sse < best[0]:
                best = (sse, b, coef, resid)
        return best  # (sse, b, [a,c], resid)

    # Quadratic fit  Φ = a*p^2 + b*p + c.
    def fit_quad(x, y):
        basis = np.column_stack([x ** 2, x, np.ones_like(x)])
        coef, *_ = np.linalg.lstsq(basis, y, rcond=None)
        resid = y - basis @ coef
        return float(resid @ resid), coef, resid

    sse_e, b_e, _, resid_e = fit_exp(gi, fi)
    sse_q, _, resid_q = fit_quad(gi, fi)
    if sse_e <= sse_q:
        which, resid = "exponential", resid_e
    else:
        which, resid = "quadratic", resid_q
    abs_resid = np.abs(resid)
    max_resid = float(abs_resid.max())
    med_resid = float(np.median(abs_resid))
    resid_ok = (max_resid <= 0.02) and (med_resid == 0.0 or max_resid <= 3.0 * med_resid)

    # Second difference on every interior point of the FULL grid.
    d2 = f[2:] - 2.0 * f[1:-1] + f[:-2]              # indices 1..49
    abs_d2 = np.abs(d2)
    med_d2 = float(np.median(abs_d2))
    max_d2 = float(abs_d2.max())
    d2_ok = (med_d2 == 0.0 and max_d2 == 0.0) or (max_d2 < 5.0 * med_d2)

    holds = resid_ok and d2_ok
    info = dict(which=which, b_exp=b_e, max_resid=max_resid, med_resid=med_resid,
                resid_ok=resid_ok, max_d2=max_d2, med_d2=med_d2, d2_ok=d2_ok)
    return holds, info


# ---------------------------------------------------------------------------
# H2 — susceptibility χ(p) = dΦ/dp
# ---------------------------------------------------------------------------
def susceptibility(grid, phi):
    """Centered difference on interior points, forward/backward at the endpoints."""
    g = np.array(grid)
    f = np.array(phi)
    chi = np.empty_like(f)
    chi[0] = (f[1] - f[0]) / STEP                      # forward at left endpoint
    chi[-1] = (f[-1] - f[-2]) / STEP                   # backward at right endpoint
    chi[1:-1] = (f[2:] - f[:-2]) / (2.0 * STEP)        # centered on interior
    return chi


def main():
    instrument_control()

    # The single 51-point Φ(p) sweep, computed once.
    print("Sweeping Φ_MIP(p) over the 51-point grid p=0.00..0.50 ...")
    phi = []
    for p in GRID:
        ph, _ = max_phi_float(noisy_tpm(p))
        phi.append(float(ph))
    phi = [round(x, 12) for x in phi]

    # H1 re-check.
    h1_ok, h1_info = h1_holds(GRID, phi)

    # H2 susceptibility.
    chi = susceptibility(GRID, phi)
    abs_chi = np.abs(chi)

    # argmax over the whole array; classify whether it is an interior maximum.
    k_max = int(np.argmax(abs_chi))
    p_max = GRID[k_max]
    chi_max = float(abs_chi[k_max])

    # Endpoint |χ| values for the comparison in the decision rule.
    chi_left = float(abs_chi[0])     # p = 0.00
    chi_right = float(abs_chi[-1])   # p = 0.50

    # Interior maximum: an interior grid point 0.01 < p < 0.49 (indices 2..48) whose |χ|
    # strictly exceeds both immediate neighbors and exceeds both endpoint values. The first
    # and last interior points (indices 1 and 49, p=0.01 and p=0.49) are excluded from
    # counting as an interior peak per the spec; a max forced onto p=0.01 that decreases
    # monotonically thereafter is an endpoint peak.
    interior_peak_idx = None
    for k in range(2, 49):  # p = 0.02 .. 0.48 strictly inside (0.01, 0.49)
        if (abs_chi[k] > abs_chi[k - 1] and abs_chi[k] > abs_chi[k + 1]
                and abs_chi[k] > chi_left and abs_chi[k] > chi_right):
            if interior_peak_idx is None or abs_chi[k] > abs_chi[interior_peak_idx]:
                interior_peak_idx = k

    has_interior_peak = interior_peak_idx is not None
    p_chi = GRID[interior_peak_idx] if has_interior_peak else None

    # Monotonicity of |χ| (for the refutation branch).
    diffs = np.diff(abs_chi)
    monotone_dec = bool(np.all(diffs <= 1e-12))
    monotone_inc = bool(np.all(diffs >= -1e-12))
    is_monotone = monotone_dec or monotone_inc
    max_at_endpoint = k_max == 0 or k_max == len(GRID) - 1

    # ---- verdict ----
    if has_interior_peak and h1_ok:
        h2_verdict = "confirmed"
    elif has_interior_peak and not h1_ok:
        h2_verdict = "partial"   # susceptibility peaks interiorly but H1 (smooth mean) fails
    else:
        h2_verdict = "refuted"

    # ---- print exact numbers ----
    print("\nΦ(p) sweep and susceptibility χ(p)=dΦ/dp (|χ| = |dΦ/dp|):")
    print(f"  {'p':>5}  {'Phi':>12}  {'chi':>12}  {'|chi|':>12}")
    for k, p in enumerate(GRID):
        tag = ""
        if k == k_max:
            tag = "  <- argmax|chi|"
        if has_interior_peak and k == interior_peak_idx:
            tag += "  [interior peak]"
        print(f"  {p:>5.2f}  {phi[k]:>12.6f}  {chi[k]:>12.6f}  {abs_chi[k]:>12.6f}{tag}")

    print("\nH1 re-check on the same sweep (H2 counts only if H1 holds):")
    print(f"  better fit          = {h1_info['which']} (exp b={h1_info['b_exp']:.4f})")
    print(f"  max interior resid  = {h1_info['max_resid']:.6f}  (need <= 0.02) -> {h1_info['resid_ok']}")
    print(f"  median resid        = {h1_info['med_resid']:.6f}")
    print(f"  max interior |d2Phi|= {h1_info['max_d2']:.6f}  median={h1_info['med_d2']:.6f}"
          f"  (need max < 5x median) -> {h1_info['d2_ok']}")
    print(f"  H1 holds            = {h1_ok}")

    print("\nH2 susceptibility result:")
    print(f"  |chi| at p=0.00 (left endpoint)  = {chi_left:.6f}")
    print(f"  |chi| at p=0.50 (right endpoint) = {chi_right:.6f}")
    print(f"  global argmax |chi|              = {chi_max:.6f} at p={p_max:.2f} (index {k_max})")
    print(f"  |chi| monotone over grid?        = {is_monotone} "
          f"(dec={monotone_dec}, inc={monotone_inc})")
    print(f"  global max at an endpoint?       = {max_at_endpoint}")
    print(f"  interior maximum found?          = {has_interior_peak}"
          + (f" at p_chi={p_chi:.2f} (|chi|={float(abs_chi[interior_peak_idx]):.6f})"
             if has_interior_peak else ""))
    print(f"\nH2 VERDICT: {h2_verdict.upper()}")
    if h2_verdict == "partial":
        print("  (|chi| peaks interiorly but H1 mean-smoothness fails on this sweep)")

    # ---- write CSV ----
    results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(results_dir, exist_ok=True)
    csv_path = os.path.join(results_dir, "q6_susceptibility.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["p", "phi", "chi", "abs_chi", "is_global_argmax", "is_interior_peak"])
        for k, p in enumerate(GRID):
            w.writerow([f"{p:.2f}", f"{phi[k]:.12f}", f"{chi[k]:.12f}", f"{abs_chi[k]:.12f}",
                        int(k == k_max),
                        int(has_interior_peak and k == interior_peak_idx)])
    print(f"\nWrote {csv_path}")

    return h2_verdict


if __name__ == "__main__":
    main()
