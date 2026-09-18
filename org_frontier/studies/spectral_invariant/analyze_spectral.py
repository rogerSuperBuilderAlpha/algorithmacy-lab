"""Agenda #21 — spectral topology-invariant features vs coupling (#134).

Exact IIT-4.0 labels on a multi-family panel. Hypotheses fixed in
hypotheses.md before computing.

Cited: #134, structure_aware_surrogate (#22), sample_complexity_screen (#23).
Construct/omit/ladder/indeg closed.

Run:  python org_frontier/studies/spectral_invariant/analyze_spectral.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np
from sklearn.metrics import roc_auc_score

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from pyphi import convert

from org_frontier.classifier.classifier import classify_rules, cm_from_rules, tpm_from_rules
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import entropy, mutual_information, o_information
from org_frontier.probes.lib import verdict as vlib
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_threshold_scaling import threshold_hub
from org_frontier.probes.probe_symmetric_multihub import sym_two_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

NOISE = 0.08
T = 2000
SEED = 21

FEATURE_NAMES = [
    # coupling baselines
    "mean_mi", "tc_per_node", "abs_oinfo",
    # connectivity spectral
    "adj_spectral_radius", "lap_lambda2", "lap_lambda_max",
    "lap_gap", "graph_energy", "vn_entropy",
    # transfer operator
    "P_second_mod", "P_spectral_gap",
]


def broadcast(n):
    rules = [None] * n
    rules[0] = lambda x: x[1] if n > 1 else 0
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def chain_ff(n):
    rules = [None] * n
    rules[0] = lambda x: x[0]
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[i - 1])
    return rules


def broken_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n - 1):
        rules[i] = (lambda x, i=i: x[0])
    rules[n - 1] = lambda x: x[n - 1]
    return rules


def or_pool(n):
    rules = [None] * n
    for i in range(n):
        others = [j for j in range(n) if j != i]
        rules[i] = (lambda x, others=others: int(any(x[j] for j in others)))
    return rules


def build_panel():
    forms = []

    def add(family, name, n, rules):
        forms.append({
            "family": family, "name": name, "n": n, "rules": rules,
        })

    for n in (3, 4, 5):
        add("chain", f"chain_and_n{n}", n, chain(n))
        add("chain", f"chain_ff_n{n}", n, chain_ff(n))
        add("pool", f"pool_and_n{n}", n, pool(n))
        add("pool", f"pool_or_n{n}", n, or_pool(n))
        add("single_hub", f"and_hub_n{n}", n, single_hub(n))
        add("single_hub", f"broken_hub_n{n}", n, broken_hub(n))
        add("or_hub", f"or_hub_n{n}", n, or_hub(n))
        add("parity_hub", f"parity_hub_n{n}", n, parity_hub(n))
        add("broadcast", f"broadcast_n{n}", n, broadcast(n))
        add("majority", f"maj_n{n}", n, threshold_hub(n, (n - 1) // 2 + 1))
        add("majority", f"thresh1_n{n}", n, threshold_hub(n, 1))
    for n in (4, 5):
        add("two_hub", f"two_hub_n{n}", n, two_hub(n))
    if True:
        add("two_hub", "two_hub_sym_n5", 5, sym_two_hub(5))
    return forms


def coupling_feats(traj, n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    mean_mi = float(np.mean([mutual_information(traj, [a], [b]) for a, b in pairs]))
    tc = sum(entropy(traj, [i]) for i in range(n)) - entropy(traj, list(range(n)))
    tc_per_node = float(tc) / max(n, 1)
    oi = abs(float(o_information(traj, list(range(n)))))
    return mean_mi, tc_per_node, oi


def spectral_cm(cm):
    """Spectral descriptors of the dependency graph."""
    n = cm.shape[0]
    A = cm.astype(float)
    # spectral radius
    try:
        eigs_a = np.linalg.eigvals(A)
        radius = float(np.max(np.abs(eigs_a)))
        energy = float(np.sum(np.abs(eigs_a)))
    except Exception:
        radius, energy = 0.0, 0.0

    # undirected Laplacian
    und = ((cm + cm.T) > 0).astype(float)
    np.fill_diagonal(und, 0)
    deg = und.sum(axis=1)
    L = np.diag(deg) - und
    try:
        ev = np.sort(np.real(np.linalg.eigvalsh(L)))
        lam2 = float(ev[1]) if n >= 2 else 0.0
        lam_max = float(ev[-1])
        gap = lam_max - lam2
    except Exception:
        lam2, lam_max, gap = 0.0, 0.0, 0.0

    # von Neumann entropy of normalized Laplacian
    try:
        with np.errstate(divide="ignore", invalid="ignore"):
            d_inv_sqrt = np.zeros(n)
            mask = deg > 0
            d_inv_sqrt[mask] = 1.0 / np.sqrt(deg[mask])
            Dhalf = np.diag(d_inv_sqrt)
            Ln = Dhalf @ L @ Dhalf
            evn = np.clip(np.real(np.linalg.eigvalsh(Ln)), 0, None)
            # eigenvalues of normalized Lap in [0,2]; treat as probs after /n
            p = evn / max(n, 1)
            p = p[p > 1e-12]
            vn = float(-np.sum(p * np.log(p))) if len(p) else 0.0
    except Exception:
        vn = 0.0

    return radius, lam2, lam_max, gap, energy, vn


def spectral_P(tpm_noisy):
    """Spectral gap of the state-by-state transfer operator."""
    P = convert.state_by_node2state_by_state(tpm_noisy)
    P = np.asarray(P, dtype=float)
    # row-stochastic cleanup
    rs = P.sum(axis=1, keepdims=True)
    rs[rs == 0] = 1.0
    P = P / rs
    try:
        ev = np.linalg.eigvals(P)
        mods = np.sort(np.abs(ev))[::-1]
        # mods[0] ~ 1
        second = float(mods[1]) if len(mods) > 1 else 0.0
        gap = float(mods[0] - second)
    except Exception:
        second, gap = 0.0, 0.0
    return second, gap


def oriented_auc(scores, labels):
    """AUC with best orientation (feature or −feature)."""
    scores = np.asarray(scores, float)
    labels = np.asarray(labels, int)
    if labels.sum() == 0 or labels.sum() == len(labels):
        return float("nan"), 1
    try:
        a = float(roc_auc_score(labels, scores))
        b = float(roc_auc_score(labels, -scores))
    except ValueError:
        return float("nan"), 1
    if b > a:
        return b, -1
    return a, 1


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return float("nan")

    def rank(a):
        order = np.argsort(a, kind="mergesort")
        ranks = np.empty(len(a), float)
        ranks[order] = np.arange(1, len(a) + 1)
        _, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
        for k, c in enumerate(counts):
            if c > 1:
                ranks[inv == k] = ranks[inv == k].mean()
        return ranks

    return float(np.corrcoef(rank(x), rank(y))[0, 1])


def main():
    print("AGENDA #21 — SPECTRAL TOPOLOGY-INVARIANT FEATURE")
    print("=" * 80)
    print("  cited: #134 coupling invert; #22 NO_STRUCTURE_GAIN; #23 FAST_WITHIN_FAMILY")
    print("  spectral of cm + transfer operator P; coupling baselines")
    print("  protocol: pooled cross-family AUC (oriented); exact IIT-4.0 labels")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rng = np.random.default_rng(SEED)
    panel = build_panel()
    print(f"PANEL  N={len(panel)}  families="
          f"{sorted({f['family'] for f in panel})}")
    print("-" * 80)

    rows = []
    feat_cols = {k: [] for k in FEATURE_NAMES}
    y, phi, families = [], [], []
    t_all = time.time()

    for f in panel:
        n = f["n"]
        rules = f["rules"]
        labels = tuple(f"x{i}" for i in range(n))
        t0 = time.time()
        v = classify_rules(rules, labels=labels)
        cm = cm_from_rules(rules, n)
        tpm = add_noise(tpm_from_rules(rules), NOISE)
        traj = exact_phi.simulate_trajectory(tpm, n, T, rng)

        mi, tc, oi = coupling_feats(traj, n)
        rad, l2, lmax, gap, energy, vn = spectral_cm(cm)
        p2, pgap = spectral_P(tpm)

        feats = {
            "mean_mi": mi,
            "tc_per_node": tc,
            "abs_oinfo": oi,
            "adj_spectral_radius": rad,
            "lap_lambda2": l2,
            "lap_lambda_max": lmax,
            "lap_gap": gap,
            "graph_energy": energy,
            "vn_entropy": vn,
            "P_second_mod": p2,
            "P_spectral_gap": pgap,
        }
        tri = int(v.structure == "triadic")
        for k, val in feats.items():
            feat_cols[k].append(val)

        row = {
            "name": f["name"],
            "family": f["family"],
            "n": n,
            "structure": v.structure,
            "max_phi": float(v.max_phi),
            "triadic": tri,
            "elapsed_s": round(time.time() - t0, 2),
            **feats,
        }
        rows.append(row)
        y.append(tri)
        phi.append(float(v.max_phi))
        families.append(f["family"])
        print(
            f"  {f['name']:<24} {v.structure}/{v.max_phi:.3f}  "
            f"MI={mi:.3f} λ2={l2:.3f} Pgap={pgap:.3f}  t={row['elapsed_s']}s"
        )

    y = np.asarray(y, int)
    phi = np.asarray(phi, float)
    families = np.asarray(families)
    print()
    print(f"  labeled: {int(y.sum())} tri / {len(y) - int(y.sum())} dya  "
          f"elapsed={round(time.time() - t_all, 1)}s")
    print()

    print("POOLED CROSS-FAMILY AUC (oriented)")
    print("-" * 80)
    print(f"  {'feature':<24}{'AUC':>8}{'orient':>8}{'ρ(Φ)':>10}  class")
    ranking = []
    for name in FEATURE_NAMES:
        scores = np.asarray(feat_cols[name], float)
        auc, orient = oriented_auc(scores, y)
        rho = spearman(orient * scores, phi)
        cls = "coupling" if name in ("mean_mi", "tc_per_node", "abs_oinfo") else "spectral"
        ranking.append({
            "feature": name, "auc": auc, "orient": orient,
            "rho_phi": rho, "class": cls,
        })
        auc_s = f"{auc:.3f}" if not np.isnan(auc) else "nan"
        rho_s = f"{rho:.3f}" if not np.isnan(rho) else "nan"
        print(f"  {name:<24}{auc_s:>8}{orient:>8}{rho_s:>10}  {cls}")

    coupling = [r for r in ranking if r["class"] == "coupling"]
    spectral = [r for r in ranking if r["class"] == "spectral"]
    best_c = max(coupling, key=lambda r: r["auc"] if not np.isnan(r["auc"]) else -1)
    best_s = max(spectral, key=lambda r: r["auc"] if not np.isnan(r["auc"]) else -1)
    coup_auc = best_c["auc"]
    spec_auc = best_s["auc"]
    lift = spec_auc - coup_auc

    print()
    print(f"  best coupling: {best_c['feature']} AUC={coup_auc:.3f}")
    print(f"  best spectral: {best_s['feature']} AUC={spec_auc:.3f}  "
          f"lift={lift:+.3f}  ρ(Φ)={best_s['rho_phi']:.3f}")

    # per-family AUC for best spectral (invariance check)
    print()
    print(f"PER-FAMILY AUC — {best_s['feature']} (orient={best_s['orient']})")
    print("-" * 80)
    fam_aucs = []
    for fam in sorted(set(families.tolist())):
        m = families == fam
        if y[m].sum() == 0 or y[m].sum() == m.sum():
            print(f"  {fam:<12} AUC=n/a (mono-class)")
            continue
        scores = best_s["orient"] * np.asarray(feat_cols[best_s["feature"]], float)[m]
        a, _ = oriented_auc(scores, y[m])
        # already oriented globally; use direct auc
        try:
            a = float(roc_auc_score(y[m], scores))
        except ValueError:
            a = float("nan")
        fam_aucs.append(a)
        print(f"  {fam:<12} AUC={a:.3f}  n={int(m.sum())} tri={int(y[m].sum())}")
    fam_spread = float(np.nanmax(fam_aucs) - np.nanmin(fam_aucs)) if fam_aucs else float("nan")
    print(f"  family AUC spread (max−min)={fam_spread:.3f}")

    h1 = ctrl and (not np.isnan(spec_auc)) and spec_auc >= 0.70 and lift >= 0.15
    # H2: all spectral fail
    all_fail = all(
        (np.isnan(r["auc"]) or r["auc"] <= 0.55 or r["auc"] <= coup_auc + 0.05)
        for r in spectral
    )
    h2 = ctrl and all_fail and not h1
    h3 = ctrl and h1 and (np.isnan(best_s["rho_phi"]) or abs(best_s["rho_phi"]) < 0.30)

    if h1 and not h3:
        verdict_word = "SPECTRAL_RANKS"
        reading = (
            f"SPECTRAL_RANKS — {best_s['feature']} cross-family AUC="
            f"{spec_auc:.3f} beats coupling ({coup_auc:.3f}); #21 affirmative"
        )
    elif h1 and h3:
        verdict_word = "SPECTRAL_DETECTS_NOT_MAG"
        reading = (
            f"SPECTRAL_DETECTS_NOT_MAG — {best_s['feature']} AUC="
            f"{spec_auc:.3f}; ρ(Φ)={best_s['rho_phi']:.3f}<0.30"
        )
    elif h2:
        verdict_word = "NO_SPECTRAL_INVARIANT"
        reading = (
            f"NO_SPECTRAL_INVARIANT — best spectral AUC={spec_auc:.3f} "
            f"(coupling best={coup_auc:.3f}); no topology-invariant spectral "
            f"ranker; #21 negative"
        )
    else:
        verdict_word = "SPECTRAL_PARTIAL"
        reading = (
            f"SPECTRAL_PARTIAL — best spectral={best_s['feature']} "
            f"AUC={spec_auc:.3f} lift={lift:+.3f}; clears neither H1 nor H2"
        )

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (spectral ranks across families): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}  "
          f"(AUC_s={spec_auc:.3f}, lift={lift:+.3f})")
    print(f"  H2 (all spectral fail like coupling): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (detect not magnitude):            "
          f"{'SUPPORTED' if h3 else 'REFUTED'}  "
          f"(ρ={best_s['rho_phi']:.3f})")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  best_spectral={best_s['feature']}  auc={spec_auc:.3f}  "
          f"best_coupling={best_c['feature']}  auc={coup_auc:.3f}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = ["name", "family", "n", "structure", "max_phi", "triadic",
                  "elapsed_s"] + FEATURE_NAMES
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = {k: r[k] for k in ["name", "family", "n", "structure",
                                     "triadic", "elapsed_s"]}
            out["max_phi"] = f"{r['max_phi']:.6f}"
            for k in FEATURE_NAMES:
                out[k] = f"{r[k]:.8f}"
            w.writerow(out)
    with open(os.path.join(RESULTS, "ranking.csv"), "w", newline="") as fh:
        fields = ["feature", "class", "auc", "orient", "rho_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in ranking:
            w.writerow({
                "feature": r["feature"],
                "class": r["class"],
                "auc": f"{r['auc']:.6f}" if not np.isnan(r["auc"]) else "",
                "orient": r["orient"],
                "rho_phi": (
                    f"{r['rho_phi']:.6f}" if not np.isnan(r["rho_phi"]) else ""
                ),
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "best_spectral": best_s["feature"],
            "auc_spectral": f"{spec_auc:.6f}",
            "best_coupling": best_c["feature"],
            "auc_coupling": f"{coup_auc:.6f}",
            "lift": f"{lift:.6f}",
            "rho_spectral": f"{best_s['rho_phi']:.6f}",
            "n_forms": len(rows),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
