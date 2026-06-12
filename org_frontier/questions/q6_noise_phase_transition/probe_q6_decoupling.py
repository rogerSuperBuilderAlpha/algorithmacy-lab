"""Q6 H4 — verdict/Φ decoupling: a step verdict on a smooth-ramping Φ.

H4: The verdict transition is a single step where mean Φ is a smooth ramp — verdict-sharpness
and Φ-smoothness coexist.

Form / ensemble (the single 51-point sweep, read two ways at every grid point on the identical
grid and noise model):
  Triadic conjunctive mediated chain, n=3, labels (W,S,C):
      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]   (#26/#33/#27)
  Commit noise of strength p is output noise on the mediator column (index 1) of the
  state-by-node TPM: the clean column s_clean in {0,1} per row becomes
      P(S'=1) = (1-p)*s_clean + p*(1-s_clean),
  so the commit lands on its clean value with reliability 1-p and flips with probability p.
  W and C columns stay deterministic; cm is the clean form's cm_from_rules (noise rescales
  transition probabilities, it does not add or remove a dependency).
  Grid: p = 0.00, 0.01, ..., 0.50 (51 points, step 0.01).
  Read two ways at every point:
    - continuous Φ_MIP(p) via max_phi_float(noisy_tpm(p))   (H1)
    - binary structure(p) via classify(noisy_tpm(p), cm), PHI_EPS=1e-9   (H3)

Measure:
  (a) verdict step — the binary label change Δstructure concentrated in the one grid interval
      [p_k, p_{k+1}] where structure changes, and its width in p.
  (b) Φ step — the largest single-interval drop max_k |Φ(p_{k+1}) - Φ(p_k)| and the fraction of
      the total fall Φ(0) - Φ(0.5) = 2.0 carried by any one interval.

Controls: instrument control (p=0 = 2.0 triadic, MIP {W,SC}). Read jointly with H1 (no single Φ
interval dominant) and H3 (verdict a clean single flip).

Decision rule (fixed before run): H4 confirmed if the verdict's whole change is a single label
flip confined to one grid interval (constant triadic before, constant dyadic after) AND no single
Φ interval carries more than 25% of the total 2.0 fall. H4 refuted if Φ's fall is dominated by one
interval carrying >25% of the total (Φ has a step too) or the verdict degrades through more than
one interval (no clean step).
Predicted: Φ fades smoothly (every interval <25% of total) while the triadic->dyadic label snaps
in the single p=0.5 interval — a verdict discontinuity on a continuous Φ, matching Niizato (2020).

Run:
  ~/iit-playground/venv-4.0/bin/python \
      org_frontier/questions/q6_noise_phase_transition/probe_q6_decoupling.py
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
MEDIATOR_COL = 1                    # S column


def noisy_tpm(p):
    """Apply commit (output) noise of strength p to the mediator column only.

    P(S'=1) = (1-p)*s_clean + p*(1-s_clean). W and C columns stay deterministic.
    """
    tpm = CLEAN_TPM.copy()
    s_clean = CLEAN_TPM[:, MEDIATOR_COL]
    tpm[:, MEDIATOR_COL] = (1.0 - p) * s_clean + p * (1.0 - s_clean)
    return tpm


def main():
    print("Q6 H4 — verdict/Φ decoupling: a step verdict on a smooth-ramping Φ")
    print("=" * 78)

    # ---- Instrument control (run first; abort on failure) ----
    ctrl = verdict(RULES, LABELS)
    print("Instrument control (strict-mediation triad #26/#33/#27 at p=0):")
    print(f"  structure={ctrl.structure}  max_phi={ctrl.max_phi:.6f}  MIP={ctrl.mip_partition}")
    phi0, _ = max_phi_float(noisy_tpm(0.0))
    print(f"  max_phi_float(noisy_tpm(0.0))={phi0:.6f}")
    ok = (ctrl.structure == "triadic"
          and abs(ctrl.max_phi - 2.0) < 1e-6
          and "{W,SC}" in ctrl.mip_partition.replace(" ", "")
          and abs(phi0 - 2.0) < 1e-6)
    assert ok, (
        f"Instrument control FAILED: expected triadic Φ=2.0 MIP {{W,SC}} and "
        f"max_phi_float(p=0)=2.0, got {ctrl.structure} Φ={ctrl.max_phi:.6f} "
        f"MIP {ctrl.mip_partition}, max_phi_float={phi0:.6f}. Halting."
    )
    print("  instrument control PASSED (triadic, Φ=2.0, MIP {W,SC}, max_phi_float(0)=2.0)")
    print("-" * 78)

    # ---- The single 51-point sweep, read two ways at every grid point ----
    phis = np.zeros(len(GRID))
    structures = []
    for k, p in enumerate(GRID):
        tpm = noisy_tpm(p)
        phi, _ = max_phi_float(tpm)
        v = classify(tpm, CM, labels=LABELS, eps=PHI_EPS)
        phis[k] = phi
        structures.append(v.structure)

    # ---- (a) verdict step: where does the binary label change? ----
    flips = [k for k in range(len(GRID) - 1) if structures[k] != structures[k + 1]]
    n_flips = len(flips)
    if n_flips == 1:
        k = flips[0]
        flip_lo, flip_hi = GRID[k], GRID[k + 1]
        flip_width = flip_hi - flip_lo
        flip_from, flip_to = structures[k], structures[k + 1]
    else:
        flip_lo = flip_hi = flip_width = None
        flip_from = flip_to = None

    constant_before = (n_flips == 1
                       and all(s == structures[0] for s in structures[:flips[0] + 1]))
    constant_after = (n_flips == 1
                      and all(s == structures[-1] for s in structures[flips[0] + 1:]))
    single_clean_flip = (n_flips == 1 and flip_from == "triadic" and flip_to == "dyadic"
                         and constant_before and constant_after)
    flip_at_end = (n_flips == 1 and abs(flip_hi - 0.50) < 1e-9)

    # ---- (b) Φ step: largest single-interval drop and its share of the 2.0 total fall ----
    drops = np.abs(np.diff(phis))                 # |Φ(p_{k+1}) - Φ(p_k)| per interval
    total_fall = phis[0] - phis[-1]               # Φ(0) - Φ(0.5), expected 2.0
    max_drop = float(drops.max())
    max_drop_k = int(drops.argmax())
    # Fraction of the total 2.0 fall carried by the largest single interval.
    max_share = max_drop / 2.0
    max_share_vs_actual = max_drop / total_fall if total_fall != 0 else float("nan")

    print("Sweep summary (51 points, p = 0.00 .. 0.50 step 0.01):")
    print(f"  Φ(0)={phis[0]:.6f}  Φ(0.5)={phis[-1]:.6f}  total fall Φ(0)-Φ(0.5)={total_fall:.6f}")
    print(f"  structure(0)={structures[0]}  structure(0.5)={structures[-1]}")
    print()
    print("(a) Verdict step:")
    print(f"  number of label-change intervals = {n_flips}")
    if n_flips == 1:
        print(f"  flip interval = [{flip_lo:.2f}, {flip_hi:.2f}]  width={flip_width:.2f}  "
              f"{flip_from} -> {flip_to}")
        print(f"  constant {structures[0]} before, constant {structures[-1]} after = "
              f"{constant_before and constant_after}")
        print(f"  flip at p=0.5 endpoint interval = {flip_at_end}")
    else:
        print(f"  flip intervals at k = {flips}  (NOT a single clean step)")
    print()
    print("(b) Φ step:")
    print(f"  largest single-interval drop = {max_drop:.6f} at interval "
          f"[{GRID[max_drop_k]:.2f}, {GRID[max_drop_k + 1]:.2f}]")
    print(f"  share of total 2.0 fall = {max_share:.4f} ({100*max_share:.2f}%)")
    print(f"  share of actual fall ({total_fall:.4f}) = {max_share_vs_actual:.4f} "
          f"({100*max_share_vs_actual:.2f}%)")
    print(f"  Φ-smooth (max interval share of 2.0 fall <= 25%) = {max_share <= 0.25}")
    print("-" * 78)

    # Per-interval table (first few, the flip, and the biggest drop) for the record.
    print("Per-interval drops (|ΔΦ| and share of 2.0):")
    for k in range(len(GRID) - 1):
        mark = ""
        if n_flips == 1 and k == flips[0]:
            mark += " <-flip"
        if k == max_drop_k:
            mark += " <-max"
        if k < 5 or mark:
            print(f"  [{GRID[k]:.2f},{GRID[k+1]:.2f}]  Φ:{phis[k]:.4f}->{phis[k+1]:.4f}  "
                  f"|ΔΦ|={drops[k]:.6f}  share={drops[k]/2.0:.4f}  "
                  f"struct:{structures[k]}->{structures[k+1]}{mark}")
    print("-" * 78)

    # ---- Decision rule (fixed before run) ----
    phi_smooth = max_share <= 0.25
    if single_clean_flip and phi_smooth:
        v = "confirmed"
    elif not phi_smooth and single_clean_flip:
        v = ("refuted (Φ has a step too: one interval carries "
             f">25% of the 2.0 fall, share={max_share:.4f})")
    elif n_flips != 1 or not single_clean_flip:
        v = ("refuted (verdict degrades through more than one interval / "
             f"not a clean triadic->dyadic step: n_flips={n_flips})")
    else:
        v = "refuted (other)"

    print(f"VERDICT: H4 {v}")
    print(f"  verdict step: single clean triadic->dyadic flip = {single_clean_flip}"
          + (f" in [{flip_lo:.2f},{flip_hi:.2f}]" if n_flips == 1 else "")
          + (f", at p=0.5 = {flip_at_end}" if n_flips == 1 else ""))
    print(f"  Φ smooth: max single-interval share of 2.0 fall = {max_share:.4f} "
          f"({100*max_share:.2f}%) <= 25% = {phi_smooth}")

    # ---- CSV ----
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h4_decoupling.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "phi_mip", "structure", "interval_drop_to_next", "share_of_2.0"])
        for k in range(len(GRID)):
            if k < len(GRID) - 1:
                d = drops[k]
                w.writerow([f"{GRID[k]:.2f}", f"{phis[k]:.6f}", structures[k],
                            f"{d:.6f}", f"{d/2.0:.6f}"])
            else:
                w.writerow([f"{GRID[k]:.2f}", f"{phis[k]:.6f}", structures[k], "", ""])
    print(f"  wrote {csv_path}")

    # ---- Summary line for PROBES.md ----
    flip_str = (f"[{flip_lo:.2f},{flip_hi:.2f}]" if n_flips == 1 else f"{n_flips} flips")
    print()
    print("PROBES_ROW: "
          f"H4 verdict/Φ decoupling | {v.split(' (')[0]} | "
          f"single {flip_from}->{flip_to} flip in {flip_str} (width "
          f"{flip_width if n_flips==1 else 'n/a'}); "
          f"max ΔΦ interval={max_drop:.4f} = {100*max_share:.2f}% of 2.0 fall (<25%={phi_smooth}); "
          f"Φ(0)={phis[0]:.3f}->Φ(0.5)={phis[-1]:.3f}")


if __name__ == "__main__":
    main()
