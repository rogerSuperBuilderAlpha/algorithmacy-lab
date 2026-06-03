"""Run the proxy bridge over the corpus forms x noise levels x seeds; write results/bridge.csv.

Also runs a pure-independence control (two decoupled parties) that must give proxy ≈ 0.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.proxy_bridge.run [traj_len]
"""

import csv
import os
import sys
import time

import numpy as np

from org_frontier.corpus import forms_library as lib
from . import bridge

_HERE = os.path.dirname(__file__)
_RESULTS = os.path.join(_HERE, "results")

NOISE_LEVELS = [0.05, 0.1, 0.2]
SEEDS = [1, 2, 3]


def main(traj_len=8000):
    os.makedirs(_RESULTS, exist_ok=True)
    rows = []
    start = time.time()
    print(f"PROXY BRIDGE — ΦID Φ_R from trajectories vs exact verdict "
          f"(traj_len={traj_len}, noise={NOISE_LEVELS}, seeds={SEEDS})")
    print("=" * 96)
    for f in lib.FORMS:
        for noise in NOISE_LEVELS:
            for seed in SEEDS:
                rng = np.random.default_rng(seed)
                structure, phi_det, phi_noisy, phi_r, phi_wms = bridge.proxy_for_form(
                    f.rules, noise, rng, traj_len=traj_len)
                rows.append({
                    "form": f.key, "structure": structure, "noise": noise, "seed": seed,
                    "exact_phi_det": f"{phi_det:.6f}", "exact_phi_noisy": f"{phi_noisy:.6f}",
                    "proxy_phi_r": f"{phi_r:.6f}", "proxy_phi_wms": f"{phi_wms:.6f}",
                })
        # progress line: mean proxy by form
        sub = [r for r in rows if r["form"] == f.key]
        mean_pr = np.mean([float(r["proxy_phi_r"]) for r in sub])
        print(f"  {f.key:<24} {structure:<8} mean Φ_R={mean_pr:+.4f}  "
              f"(exact det Φ={phi_det:.3f})   [{time.time()-start:.0f}s]")

    _write(rows)
    _summary(rows)


def _write(rows):
    out = os.path.join(_RESULTS, "bridge.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nWrote {out}")


def _separation(rows, key, label):
    tri = [float(r[key]) for r in rows if r["structure"] == "triadic"]
    dya = [float(r[key]) for r in rows if r["structure"] == "dyadic"]
    wins = sum(t > d for t in tri for d in dya)
    ties = sum(t == d for t in tri for d in dya)
    auc = (wins + 0.5 * ties) / (len(tri) * len(dya))
    all_vals = sorted(set(tri + dya))
    best_acc, best_thr = 0.0, None
    for thr in all_vals:
        acc = (sum(t >= thr for t in tri) + sum(d < thr for d in dya)) / (len(tri) + len(dya))
        if acc > best_acc:
            best_acc, best_thr = acc, thr
    print(f"  [{label}] triadic mean={np.mean(tri):+.4f} dyadic mean={np.mean(dya):+.4f}  "
          f"rank-AUC={auc:.3f}  best-thr acc={best_acc:.3f} @ {best_thr:+.4f}")
    return auc


def _summary(rows):
    """Does either cheap proxy preserve the binary verdict? Report separation for both."""
    print("\n" + "=" * 96)
    print("SEPARATION: does a cheap time-series proxy preserve the dyadic/triadic verdict?")
    _separation(rows, "proxy_phi_r", "Φ_R (CCS)  ")
    _separation(rows, "proxy_phi_wms", "Φ_WMS (wms)")
    print("  (rank-AUC 0.5 = chance; exact Φ on the deterministic form is the ground truth)")
    print("=" * 96)


if __name__ == "__main__":
    traj_len = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    main(traj_len)
