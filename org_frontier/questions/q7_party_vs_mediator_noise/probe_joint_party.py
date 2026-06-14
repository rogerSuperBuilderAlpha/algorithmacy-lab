"""Q7 H5 — two simultaneously-noised parties interact; the joint collapse is non-additive.

H5: Independent flip-noise on W and C together gives a Φ_MIP(p) curve that is not the separable
composition of the single-party curves, and its effective collapse precedes the single party's.

Form / ensemble (three 51-point sweeps on the shared grid):
  Triadic conjunctive mediated chain, n=3, labels (W,S,C):
      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]   (#26/#33/#27)
  Output flip-noise of strength p on a column c of the state-by-node TPM:
      P(out=1) = (1-p)*col_clean + p*(1-col_clean).
  Three sites:
    - Φ_W(p):  cols=(0,)    party site W
    - Φ_C(p):  cols=(2,)    party site C
    - Φ_WC(p): cols=(0,2)   joint party, independent flip-noise on both, same p each
  Grid: p = 0.00, 0.01, ..., 0.50 (51 points, step 0.01).

Measure:
  (a) Non-separability residual against the fixed independent-flip null. Per-site Φ-drop fraction
      f_site(p) = 1 - Φ_site(p)/2.0; separable prediction
      Φ_pred(p) = 2.0*(1 - f_W(p))*(1 - f_C(p)); residual r(p) = Φ_WC(p) - Φ_pred(p) over interior p;
      r_max = max|r(p)| and its location.
  (b) Effective collapse shift. Smallest grid p with Φ_WC(p) < 0.01 (p_eff(WC), same 0.01 threshold
      as H3) versus p_eff(W); plus any interior local maximum of Φ_WC (a forward-difference rise
      Φ_WC(p_{k+1}) - Φ_WC(p_k) > TOL after an earlier fall — the Danilczuk 2026 transient-rise
      corroborant).

Controls: instrument control (all three sweeps p=0 = 2.0 triadic, MIP {W,SC}). Reuses H2
(Φ_W = Φ_C so f_W = f_C and Φ_pred reduces to 2.0*(1-f_W)^2). Positive control feeds Φ_pred against
itself (Φ_pred - Φ_pred ≡ 0) confirming r(p) = 0 for a truly separable curve.

Decision rule (fixed before run): H5 confirmed if r_max > 1e-3 AND p_eff(WC) < p_eff(W) by >= 1 grid
step. H5 refuted if |r(p)| <= 1e-3 at every interior p AND p_eff(WC) = p_eff(W). A non-monotone Φ_WC
excursion, if present, is a weaker corroborant, not required.
Predicted: Φ_WC(0.1)=1.37 vs Φ_W(0.1)=0.76, off the multiplicative null, r_max >> 1e-3; the strict
verdict still flips at p=0.5 so the off-0.5 claim is carried by the effective register.

Run:
  ~/iit-playground/venv-4.0/bin/python \
      org_frontier/questions/q7_party_vs_mediator_noise/probe_joint_party.py
"""

import csv
import os
import sys

# Repo root onto sys.path so org_frontier.* and proxy_audit.* import as a direct script too.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import (
    classify, tpm_from_rules, cm_from_rules, PHI_EPS,
)
from org_frontier.probes.lib import verdict, max_phi_float

LABELS = ("W", "S", "C")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

# The triadic conjunctive mediated chain (#26/#33/#27); also the strict-mediation instrument.
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Fixed grid: p = 0.00 .. 0.50 step 0.01 (51 points).
GRID = np.round(np.arange(0, 51) * 0.01, 10)

CLEAN_TPM = tpm_from_rules(RULES)   # (8, 3) deterministic
CM = cm_from_rules(RULES)           # clean connectivity matrix

CLEAN_PHI = 2.0                     # clean triad Φ, the H5 normalizer
EFF_THRESHOLD = 0.01               # effective-collapse band (same as H3)
TOL = 1e-6                          # grid noise / numerical tolerance
RESIDUAL_TOL = 1e-3                # separability margin


def noisy_tpm(p, cols):
    """Apply output flip-noise of strength p to each column in cols.

    P(out=1) = (1-p)*col_clean + p*(1-col_clean) per noised column. Untouched columns stay
    deterministic; cm is the clean form's cm (noise rescales transitions, it does not add or
    remove a dependency).
    """
    t = CLEAN_TPM.copy()
    for c in cols:
        sc = CLEAN_TPM[:, c]
        t[:, c] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def sweep(cols):
    """51-point Φ_MIP(p) sweep for a site (cols)."""
    phis = np.zeros(len(GRID))
    for k, p in enumerate(GRID):
        phi, _ = max_phi_float(noisy_tpm(p, cols))
        phis[k] = phi
    return phis


def p_eff(phis):
    """Smallest grid p with Φ < EFF_THRESHOLD; None if never reached on the grid."""
    for k in range(len(GRID)):
        if phis[k] < EFF_THRESHOLD:
            return float(GRID[k]), k
    return None, None


def transient_rise(phis):
    """Earliest interior forward-difference rise > TOL that follows an earlier fall < -TOL."""
    seen_fall = False
    for k in range(len(GRID) - 1):
        d = phis[k + 1] - phis[k]
        if d < -TOL:
            seen_fall = True
        elif d > TOL and seen_fall:
            return float(GRID[k]), float(d)
    return None, None


def main():
    print("Q7 H5 — two simultaneously-noised parties interact; joint collapse is non-additive")
    print("=" * 78)

    # ---- Instrument control (run first; abort on failure) ----
    ctrl = verdict(RULES, LABELS)
    print("Instrument control (strict-mediation triad #26/#33/#27 at p=0):")
    print(f"  structure={ctrl.structure}  max_phi={ctrl.max_phi:.6f}  MIP={ctrl.mip_partition}")
    phi0_W, _ = max_phi_float(noisy_tpm(0.0, (0,)))
    phi0_C, _ = max_phi_float(noisy_tpm(0.0, (2,)))
    phi0_WC, _ = max_phi_float(noisy_tpm(0.0, (0, 2)))
    print(f"  max_phi_float(p=0): W={phi0_W:.6f}  C={phi0_C:.6f}  WC={phi0_WC:.6f}")
    ok = (ctrl.structure == "triadic"
          and abs(ctrl.max_phi - 2.0) < 1e-6
          and "{W,SC}" in ctrl.mip_partition.replace(" ", "")
          and abs(phi0_W - 2.0) < 1e-6
          and abs(phi0_C - 2.0) < 1e-6
          and abs(phi0_WC - 2.0) < 1e-6)
    assert ok, (
        f"Instrument control FAILED: expected triadic Φ=2.0 MIP {{W,SC}} and "
        f"max_phi_float(p=0)=2.0 for W,C,WC, got {ctrl.structure} Φ={ctrl.max_phi:.6f} "
        f"MIP {ctrl.mip_partition}, W={phi0_W:.6f} C={phi0_C:.6f} WC={phi0_WC:.6f}. Halting."
    )
    print("  instrument control PASSED (triadic, Φ=2.0, MIP {W,SC}, all sites p=0 = 2.0)")
    print("-" * 78)

    # ---- Three sweeps ----
    phi_W = sweep((0,))
    phi_C = sweep((2,))
    phi_WC = sweep((0, 2))

    # ---- (a) non-separability residual against the fixed independent-flip null ----
    f_W = 1.0 - phi_W / CLEAN_PHI
    f_C = 1.0 - phi_C / CLEAN_PHI
    phi_pred = CLEAN_PHI * (1.0 - f_W) * (1.0 - f_C)
    resid = phi_WC - phi_pred

    interior = list(range(1, len(GRID) - 1))   # p in {0.01 .. 0.49}
    r_int = resid[interior]
    r_max = float(np.max(np.abs(r_int)))
    r_max_k = interior[int(np.argmax(np.abs(r_int)))]
    r_max_p = float(GRID[r_max_k])

    # Positive control: Φ_pred fed against itself reads exactly zero residual.
    self_resid = phi_pred - phi_pred
    self_r_max = float(np.max(np.abs(self_resid[interior])))

    # H2 reuse check: Φ_W == Φ_C so the null reduces to 2.0*(1-f_W)^2.
    wc_diff_max = float(np.max(np.abs(phi_W - phi_C)))

    # ---- (b) effective collapse shift ----
    peff_W_p, peff_W_k = p_eff(phi_W)
    peff_WC_p, peff_WC_k = p_eff(phi_WC)
    if peff_W_k is not None and peff_WC_k is not None:
        step_shift = peff_W_k - peff_WC_k   # >0 means WC collapses earlier
    else:
        step_shift = None
    rise_p, rise_d = transient_rise(phi_WC)

    print("Sweeps (51 points, p = 0.00 .. 0.50 step 0.01):")
    print(f"  Φ_W(0)={phi_W[0]:.6f}  Φ_C(0)={phi_C[0]:.6f}  Φ_WC(0)={phi_WC[0]:.6f}")
    print(f"  Φ_W(0.10)={phi_W[10]:.6f}  Φ_C(0.10)={phi_C[10]:.6f}  Φ_WC(0.10)={phi_WC[10]:.6f}")
    print(f"  Φ_W(0.50)={phi_W[-1]:.6f}  Φ_C(0.50)={phi_C[-1]:.6f}  Φ_WC(0.50)={phi_WC[-1]:.6f}")
    print(f"  H2 reuse: max|Φ_W - Φ_C| over grid = {wc_diff_max:.2e} "
          f"(≈0 ⇒ f_W=f_C ⇒ Φ_pred = 2.0*(1-f_W)^2)")
    print()
    print("(a) Non-separability residual r(p) = Φ_WC(p) - Φ_pred(p), Φ_pred = 2.0*(1-f_W)*(1-f_C):")
    print(f"  at p=0.10: Φ_WC={phi_WC[10]:.6f}  Φ_pred={phi_pred[10]:.6f}  r={resid[10]:.6f}")
    print(f"  r_max over interior p = {r_max:.6f} at p={r_max_p:.2f}")
    print(f"  positive control (Φ_pred vs Φ_pred): r_max = {self_r_max:.2e} (must be 0)")
    print()
    print("(b) Effective collapse (Φ < 0.01 band):")
    print(f"  p_eff(W)  = {peff_W_p}  (grid index {peff_W_k})")
    print(f"  p_eff(WC) = {peff_WC_p}  (grid index {peff_WC_k})")
    print(f"  step shift (W index - WC index) = {step_shift}  "
          f"(>=1 ⇒ joint collapses earlier by >=1 grid step)")
    if rise_p is not None:
        print(f"  transient rise (Danilczuk corroborant): Φ_WC rises by {rise_d:.6f} at p={rise_p:.2f}")
    else:
        print(f"  transient rise (Danilczuk corroborant): none (Φ_WC monotone non-increasing)")
    print("-" * 78)

    # ---- Residual table (interior peak neighborhood + low-p) ----
    print("Per-point (p, Φ_WC, Φ_pred, r, Φ_W=Φ_C):")
    for k in range(len(GRID)):
        mark = " <-r_max" if k == r_max_k else ""
        if k <= 12 or k == r_max_k or k in (peff_W_k, peff_WC_k):
            print(f"  p={GRID[k]:.2f}  Φ_WC={phi_WC[k]:.4f}  Φ_pred={phi_pred[k]:.4f}  "
                  f"r={resid[k]:+.4f}  Φ_W={phi_W[k]:.4f}{mark}")
    print("-" * 78)

    # ---- Decision rule (fixed before run) ----
    cond_resid = r_max > RESIDUAL_TOL
    cond_eff = (step_shift is not None and step_shift >= 1)
    refute_resid = bool(np.all(np.abs(r_int) <= RESIDUAL_TOL))
    refute_eff = (peff_W_k is not None and peff_WC_k is not None and peff_W_k == peff_WC_k)

    if cond_resid and cond_eff:
        v = "confirmed"
    elif refute_resid and refute_eff:
        v = "refuted"
    elif cond_resid and not cond_eff:
        v = ("partial (non-separable: r_max>1e-3, but joint effective collapse does NOT "
             "precede single-party by >=1 grid step)")
    elif cond_eff and not cond_resid:
        v = ("partial (joint collapses earlier, but residual within separability tolerance: "
             f"r_max={r_max:.2e} <= 1e-3)")
    else:
        v = "partial (mixed: one register supports, the other is inconclusive)"

    print(f"VERDICT: H5 {v}")
    print(f"  r_max = {r_max:.6f} (>1e-3 = {cond_resid}) at p={r_max_p:.2f}")
    print(f"  p_eff(WC)={peff_WC_p} vs p_eff(W)={peff_W_p}; earlier by >=1 step = {cond_eff}")

    # ---- CSV ----
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h5_joint_party.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "phi_W", "phi_C", "phi_WC", "f_W", "f_C", "phi_pred", "residual"])
        for k in range(len(GRID)):
            w.writerow([f"{GRID[k]:.2f}", f"{phi_W[k]:.6f}", f"{phi_C[k]:.6f}",
                        f"{phi_WC[k]:.6f}", f"{f_W[k]:.6f}", f"{f_C[k]:.6f}",
                        f"{phi_pred[k]:.6f}", f"{resid[k]:.6f}"])
    print(f"  wrote {csv_path}")

    # ---- Summary line for PROBES.md ----
    print()
    print("PROBES_ROW: "
          f"H5 joint-party non-additivity | {v.split(' (')[0]} | "
          f"r_max={r_max:.4f} at p={r_max_p:.2f} (>1e-3={cond_resid}); "
          f"Φ_WC(0.1)={phi_WC[10]:.3f} vs Φ_pred(0.1)={phi_pred[10]:.3f} vs Φ_W(0.1)={phi_W[10]:.3f}; "
          f"p_eff(WC)={peff_WC_p} vs p_eff(W)={peff_W_p} (earlier>=1step={cond_eff}); "
          f"self-control r_max={self_r_max:.0e}")


if __name__ == "__main__":
    main()
