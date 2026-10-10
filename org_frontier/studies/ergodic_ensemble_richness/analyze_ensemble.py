"""B5 — Φ_MIP vs basin entropy and attractor count on the 256-form census.

Hypotheses and decision rules were committed before this file existed.
See hypotheses.md. This script prints the pre-registered words. It does
not choose them.

Run:  python org_frontier/studies/ergodic_ensemble_richness/analyze_ensemble.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from scipy.stats import spearmanr

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.ergodicity._boolean_ergo import (
    N3,
    basin_entropy,
    find_attractors,
    instrument_gates,
    next_map,
)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
RHO_MIN = 0.20
RHO_HALF = 0.10
DELTA_H = 0.1
DELTA_C = 0.5
N_PERM = 2000
PERM_SEED = 7
SPLIT = 128


def _rho(x, y):
    if len(x) < 3 or np.unique(x).size < 2 or np.unique(y).size < 2:
        return float("nan")
    return float(spearmanr(x, y).statistic)


def _perm_ps(phi, target, obs):
    rng = np.random.default_rng(PERM_SEED)
    null = np.empty(N_PERM)
    for i in range(N_PERM):
        null[i] = _rho(rng.permutation(phi), target)
    valid = null[np.isfinite(null)]
    if not np.isfinite(obs) or valid.size == 0:
        return float("nan"), float("nan")
    p_pos = (1 + np.sum(valid >= obs)) / (valid.size + 1)
    p_neg = (1 + np.sum(valid <= obs)) / (valid.size + 1)
    return float(p_pos), float(p_neg)


def _pos(rho, p):
    return np.isfinite(rho) and np.isfinite(p) and rho >= RHO_MIN and p < 0.05


def _neg(rho, p):
    return np.isfinite(rho) and np.isfinite(p) and rho <= -RHO_MIN and p < 0.05


def _word(flag):
    return "SUPPORTED" if flag else "REFUTED"


def main():
    print("ERGODIC RICHNESS vs Φ_MIP — Strand B5 census")
    print("=" * 80)
    print("  hypotheses fixed in hypotheses.md before this script existed")
    print("  ensemble: enumerate_family() strict-mediation n=3, 256 forms")
    print("=" * 80)
    print()

    t_all = time.time()
    gates = instrument_gates()
    print("INSTRUMENT CONTROL")
    print("-" * 80)
    print(
        f"  memoryless whole: {gates['memoryless'].structure} "
        f"Φ={gates['memoryless'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_memoryless'] else 'FAIL'}"
    )
    print(
        f"  sticky whole:     {gates['sticky'].structure} "
        f"Φ={gates['sticky'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_sticky'] else 'FAIL'}"
    )
    if not gates["ok"]:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    start = time.time()
    print("CENSUS")
    print("-" * 80)
    for k, (label, rules) in enumerate(enumerate_family()):
        whole = classify_rules(rules)
        attrs = find_attractors(next_map(rules))
        sizes = [len(b) for _, b in attrs]
        rows.append({
            "label": label,
            "structure": whole.structure,
            "max_phi": float(whole.max_phi),
            "n_components": len(attrs),
            "basin_entropy": basin_entropy(sizes, N3),
        })
        if (k + 1) % 32 == 0:
            print(f"  {k + 1}/256  ({time.time() - start:.0f}s)")

    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, "forms.csv")
    with open(path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "label": row["label"],
                "structure": row["structure"],
                "max_phi": f"{row['max_phi']:.6f}",
                "n_components": row["n_components"],
                "basin_entropy": f"{row['basin_entropy']:.6f}",
            })
    print(f"Wrote {path}")
    print()

    phi = np.array([r["max_phi"] for r in rows], dtype=float)
    entropy = np.array([r["basin_entropy"] for r in rows], dtype=float)
    counts = np.array([r["n_components"] for r in rows], dtype=float)
    rho_h = _rho(phi, entropy)
    rho_c = _rho(phi, counts)
    p_h_pos, p_h_neg = _perm_ps(phi, entropy, rho_h)
    p_c_pos, p_c_neg = _perm_ps(phi, counts, rho_c)
    h1 = _pos(rho_h, p_h_pos)
    h2 = _pos(rho_c, p_c_pos)

    tri = [r for r in rows if r["structure"] == "triadic"]
    dya = [r for r in rows if r["structure"] == "dyadic"]

    def _mean(group, key):
        if not group:
            return float("nan")
        return float(np.mean([r[key] for r in group]))

    mean_h_tri = _mean(tri, "basin_entropy")
    mean_h_dya = _mean(dya, "basin_entropy")
    mean_c_tri = _mean(tri, "n_components")
    mean_c_dya = _mean(dya, "n_components")
    h3 = (
        np.isfinite(mean_h_tri)
        and np.isfinite(mean_h_dya)
        and (mean_h_tri - mean_h_dya) >= DELTA_H
    )
    h4 = (
        np.isfinite(mean_c_tri)
        and np.isfinite(mean_c_dya)
        and (mean_c_tri - mean_c_dya) >= DELTA_C
    )

    rho_lo = _rho(phi[:SPLIT], entropy[:SPLIT])
    rho_hi = _rho(phi[SPLIT:], entropy[SPLIT:])
    h5 = (
        np.isfinite(rho_lo)
        and np.isfinite(rho_hi)
        and np.sign(rho_lo) == np.sign(rho_hi)
        and np.sign(rho_lo) != 0
        and abs(rho_lo) >= RHO_HALF
        and abs(rho_hi) >= RHO_HALF
    )

    if h1 and h2:
        verdict = "RICHNESS_TRACKS_PHI"
    elif h1:
        verdict = "ENTROPY_ONLY"
    elif h2:
        verdict = "COUNT_ONLY"
    elif _neg(rho_h, p_h_neg) or _neg(rho_c, p_c_neg):
        verdict = "NEGATIVE_ASSOCIATION"
    else:
        verdict = "NO_ENSEMBLE_LINK"

    print("HYPOTHESES")
    print("-" * 80)
    print(f"  n_forms={len(rows)} n_triadic={len(tri)} n_dyadic={len(dya)}")
    print(f"  rho_entropy={rho_h:.4f} p_pos_entropy={p_h_pos:.4f} p_neg_entropy={p_h_neg:.4f}")
    print(f"  rho_count={rho_c:.4f} p_pos_count={p_c_pos:.4f} p_neg_count={p_c_neg:.4f}")
    print(f"  mean_entropy triadic={mean_h_tri:.4f} dyadic={mean_h_dya:.4f}")
    print(f"  mean_count triadic={mean_c_tri:.4f} dyadic={mean_c_dya:.4f}")
    print(f"  rho_entropy_first128={rho_lo:.4f} rho_entropy_last128={rho_hi:.4f}")
    print(f"H1 (basin entropy tracks Φ):     {_word(h1)}")
    print(f"H2 (attractor count tracks Φ):   {_word(h2)}")
    print(f"H3 (entropy mean tracks triadic):{_word(h3)}")
    print(f"H4 (count mean tracks triadic):  {_word(h4)}")
    print(f"H5 (split-half entropy ρ):       {_word(h5)}")
    print(f"verdict: {verdict}")
    print(f"  elapsed_s={time.time() - t_all:.0f}")


if __name__ == "__main__":
    main()
