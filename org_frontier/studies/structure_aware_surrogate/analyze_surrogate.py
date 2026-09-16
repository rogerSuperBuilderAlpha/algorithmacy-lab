"""Agenda #22 — structure-aware vs coupling surrogate across topology.

Leave-one-family-out on a designed multi-topology panel with exact
IIT-4.0 Φ labels. Hypotheses fixed in hypotheses.md before computing.

Cited: #123/#129/#134; probe_surrogate_transfer; probe_invariant_feature.
Construct/omit/ladder arc closed — pointer only.

Run:  python org_frontier/studies/structure_aware_surrogate/analyze_surrogate.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from functools import reduce

import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import roc_auc_score

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import (
    entropy,
    mutual_information,
    o_information,
    transfer_entropy,
)
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_threshold_scaling import threshold_hub
from org_frontier.probes.probe_symmetric_multihub import sym_two_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

NOISE = 0.08
T = 2000  # candid: shorter than probe T=4000 for CI; still enough for MI
RF_N = 200
SEED = 22
N_MAX = 5  # pad structure features to this size


# ---------------------------------------------------------------------------
# Topology constructors + dyadic / gate variants
# ---------------------------------------------------------------------------

def broadcast(n):
    """S relays node 1; others read S; no joint commit — typically dyadic."""
    rules = [None] * n
    rules[0] = lambda x: x[1] if n > 1 else 0
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def or_pool(n):
    rules = [None] * n
    for i in range(n):
        others = [j for j in range(n) if j != i]
        rules[i] = (lambda x, others=others: int(any(x[j] for j in others)))
    return rules


def broken_hub(n):
    """Hub AND without return read from last party — mediation broken."""
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n - 1):
        rules[i] = (lambda x, i=i: x[0])
    rules[n - 1] = lambda x: x[n - 1]  # idle self
    return rules


def build_panel():
    """Designed multi-topology panel. family tag drives LOFO splits."""
    forms = []

    def add(family, name, n, rules):
        forms.append({
            "family": family,
            "name": name,
            "n": n,
            "rules": rules,
        })

    for n in (3, 4, 5):
        add("chain", f"chain_and_n{n}", n, chain(n))
        add("pool", f"pool_and_n{n}", n, pool(n))
        add("pool", f"pool_or_n{n}", n, or_pool(n))
        add("single_hub", f"and_hub_n{n}", n, single_hub(n))
        add("or_hub", f"or_hub_n{n}", n, or_hub(n))
        add("parity_hub", f"parity_hub_n{n}", n, parity_hub(n))
        add("broadcast", f"broadcast_n{n}", n, broadcast(n))
        add("broken", f"broken_hub_n{n}", n, broken_hub(n))
        # majority / thresholds
        k = (n - 1) // 2 + 1
        add("majority", f"maj_hub_n{n}_k{k}", n, threshold_hub(n, k))
        if n >= 4:
            add("majority", f"thresh_hub_n{n}_k2", n, threshold_hub(n, 2))
            add("majority", f"thresh_hub_n{n}_k1", n, threshold_hub(n, 1))

    for n in (4, 5):
        add("two_hub", f"two_hub_asym_n{n}", n, two_hub(n))
        if n >= 5:
            add("two_hub", f"two_hub_sym_n{n}", n, sym_two_hub(n))

    return forms


# ---------------------------------------------------------------------------
# Features
# ---------------------------------------------------------------------------

def coupling_feats(traj, n):
    """Probe-99 eight aggregate trajectory features (coupling class)."""
    ent = [entropy(traj, [i]) for i in range(n)]
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    mi = [mutual_information(traj, [a], [b]) for a, b in pairs]
    te = [transfer_entropy(traj, a, b) for a in range(n) for b in range(n) if a != b]
    oi = o_information(traj, list(range(n)))
    return np.array([
        np.mean(ent), np.min(ent), np.max(ent),
        np.mean(mi), np.max(mi), np.mean(te), np.max(te), float(oi),
    ], dtype=float)


def _node_fn_props(rules, cm, j):
    """Boolean properties of node j over its actual inputs (flip-test parents)."""
    parents = [i for i in range(cm.shape[0]) if cm[i, j] == 1]
    k = len(parents)
    if k == 0:
        return 0.0, 0.0, 0.0, 0.0  # wt, affine, monotone, canalizing
    # truth table over 2^k
    bits = []
    for s in range(2 ** k):
        # build a full state with parents set from s; others 0
        x = [0] * cm.shape[0]
        for t, p in enumerate(parents):
            x[p] = (s >> t) & 1
        bits.append(int(rules[j](tuple(x))) & 1)
    arr = np.array(bits, dtype=int)
    wt = float(arr.mean())
    # affine over GF(2): exists linear form + bias matching table
    affine = 0.0
    # brute for k<=4; for larger skip (panel k small)
    if k <= 4:
        found = False
        for mask in range(2 ** k):
            for bias in (0, 1):
                ok = True
                for s in range(2 ** k):
                    lin = bias
                    for t in range(k):
                        if (mask >> t) & 1:
                            lin ^= (s >> t) & 1
                    if lin != arr[s]:
                        ok = False
                        break
                if ok:
                    found = True
                    break
            if found:
                break
        affine = 1.0 if found else 0.0
    # monotone (nondecreasing in each input)
    mono = 1.0
    for t in range(k):
        for s in range(2 ** k):
            if ((s >> t) & 1) == 0:
                s2 = s | (1 << t)
                if arr[s] > arr[s2]:
                    mono = 0.0
                    break
        if mono == 0.0:
            break
    # canalizing: some input value fixes output
    canal = 0.0
    for t in range(k):
        for val in (0, 1):
            outs = [arr[s] for s in range(2 ** k) if ((s >> t) & 1) == val]
            if outs and len(set(outs)) == 1:
                canal = 1.0
                break
        if canal:
            break
    return wt, affine, mono, canal


def structure_feats(rules, cm, n):
    """Connectivity-plus-function vector (structure-aware input class)."""
    # --- graph ---
    n_edges = float(cm.sum())
    density = n_edges / max(n * (n - 1), 1)
    in_deg = cm.sum(axis=0).astype(float)
    out_deg = cm.sum(axis=1).astype(float)
    n_bidir = float(sum(
        1 for i in range(n) if in_deg[i] > 0 and out_deg[i] > 0
    ))
    recip = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            if cm[i, j] and cm[j, i]:
                recip += 1.0
    # undirected clustering (simple)
    a = ((cm + cm.T) > 0).astype(int)
    np.fill_diagonal(a, 0)
    coeffs = []
    for v in range(n):
        nbrs = np.where(a[v] > 0)[0]
        if len(nbrs) < 2:
            coeffs.append(0.0)
            continue
        sub = a[np.ix_(nbrs, nbrs)]
        coeffs.append(float(sub.sum()) / (len(nbrs) * (len(nbrs) - 1)))
    clustering = float(np.mean(coeffs)) if coeffs else 0.0
    # short directed cycles via traces
    A = cm.astype(float)
    cyc2 = float(np.trace(A @ A)) / 2.0
    cyc3 = float(np.trace(A @ A @ A)) / 3.0
    # spectral radius of directed adj
    try:
        eigs = np.linalg.eigvals(A)
        spec = float(np.max(np.abs(eigs)))
    except Exception:
        spec = 0.0
    # strongly connected (weak check: undirected connected + recip>0 or n==1)
    und = a.copy()
    # BFS
    seen = {0} if n else set()
    stack = [0] if n else []
    while stack:
        u = stack.pop()
        for v in np.where(und[u] > 0)[0]:
            if int(v) not in seen:
                seen.add(int(v))
                stack.append(int(v))
    connected = 1.0 if len(seen) == n else 0.0

    graph = [
        float(n), n_edges, density, float(in_deg.mean()), float(out_deg.mean()),
        float(in_deg.max()), float(out_deg.max()), n_bidir, recip,
        clustering, cyc2, cyc3, spec, connected,
    ]

    # --- function ---
    wts, affs, monos, canals = [], [], [], []
    for j in range(n):
        wt, aff, mono, canal = _node_fn_props(rules, cm, j)
        wts.append(wt)
        affs.append(aff)
        monos.append(mono)
        canals.append(canal)
    fn = [
        float(np.mean(wts)), float(np.max(wts)),
        float(np.mean(affs)), float(np.mean(monos)), float(np.mean(canals)),
        float(np.sum(affs)), float(np.sum(monos)),
    ]

    # --- padded adjacency (upper-ish flatten, directed) ---
    pad = np.zeros((N_MAX, N_MAX), dtype=float)
    pad[:n, :n] = cm
    flat = pad.reshape(-1).tolist()  # 25 dims

    return np.array(graph + fn + flat, dtype=float)


def _auc(scores, labels):
    scores = np.asarray(scores, float)
    labels = np.asarray(labels, int)
    if labels.sum() == 0 or labels.sum() == len(labels):
        return float("nan")
    try:
        return float(roc_auc_score(labels, scores))
    except ValueError:
        return float("nan")


def _spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or x.std() < 1e-12 or y.std() < 1e-12:
        return float("nan")

    def rank(a):
        order = np.argsort(a, kind="mergesort")
        ranks = np.empty(len(a), float)
        ranks[order] = np.arange(1, len(a) + 1)
        # average ties
        _, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
        for k, c in enumerate(counts):
            if c > 1:
                ranks[inv == k] = ranks[inv == k].mean()
        return ranks

    return float(np.corrcoef(rank(x), rank(y))[0, 1])


def main():
    print("AGENDA #22 — STRUCTURE-AWARE SURROGATE ACROSS TOPOLOGY")
    print("=" * 80)
    print("  cited: #123/#129/#134; coupling feats fail cross-topology")
    print("  models: coupling (traj MI/TE) vs structure (cm+function)")
    print("  protocol: leave-one-topology-family-out; exact IIT-4.0 labels")
    print("  note: no torch GNN — RF on connectivity-plus-function features")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    from org_frontier.probes.lib import verdict as vlib
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
    print(f"PANEL  N={len(panel)} designed forms  families="
          f"{sorted({f['family'] for f in panel})}")
    print("-" * 80)

    rows = []
    Xc, Xs, y, phi = [], [], [], []
    t_all = time.time()

    for f in panel:
        n = f["n"]
        rules = f["rules"]
        labels = tuple(f"x{i}" for i in range(n))
        t0 = time.time()
        v = classify_rules(rules, labels=labels)
        cm = cm_from_rules(rules, n)
        # coupling trajectory
        traj = exact_phi.simulate_trajectory(
            add_noise(tpm_from_rules(rules), NOISE), n, T, rng
        )
        fc = coupling_feats(traj, n)
        fs = structure_feats(rules, cm, n)
        tri = int(v.structure == "triadic")
        row = {
            "name": f["name"],
            "family": f["family"],
            "n": n,
            "structure": v.structure,
            "max_phi": float(v.max_phi),
            "triadic": tri,
            "elapsed_s": round(time.time() - t0, 2),
        }
        rows.append(row)
        Xc.append(fc)
        Xs.append(fs)
        y.append(tri)
        phi.append(float(v.max_phi))
        print(
            f"  {f['name']:<28} fam={f['family']:<12} "
            f"{v.structure}/{v.max_phi:.3f}  t={row['elapsed_s']}s"
        )

    Xc = np.vstack(Xc)
    Xs = np.vstack(Xs)
    y = np.asarray(y, int)
    phi = np.asarray(phi, float)
    families = np.array([r["family"] for r in rows])
    uniq = sorted(set(families.tolist()))

    print()
    print(f"  labeled: {int(y.sum())} triadic / {len(y) - int(y.sum())} dyadic  "
          f"({100 * y.mean():.0f}% tri)")
    print(f"  elapsed_panel={round(time.time() - t_all, 1)}s")
    print()

    # ---- Leave-one-family-out ----
    print("LEAVE-ONE-FAMILY-OUT")
    print("-" * 80)
    lofo_rows = []
    auc_c, auc_s, acc_c, acc_s = [], [], [], []
    rho_c, rho_s = [], []

    for fam in uniq:
        te = families == fam
        tr = ~te
        if y[tr].sum() == 0 or y[tr].sum() == tr.sum():
            print(f"  skip {fam}: train class collapse")
            continue
        if te.sum() < 2:
            print(f"  skip {fam}: test too small ({te.sum()})")
            continue

        clf_c = RandomForestClassifier(
            n_estimators=RF_N, random_state=SEED, n_jobs=1
        )
        clf_s = RandomForestClassifier(
            n_estimators=RF_N, random_state=SEED, n_jobs=1
        )
        clf_c.fit(Xc[tr], y[tr])
        clf_s.fit(Xs[tr], y[tr])
        pc = clf_c.predict_proba(Xc[te])[:, 1]
        ps = clf_s.predict_proba(Xs[te])[:, 1]
        ac = float((clf_c.predict(Xc[te]) == y[te]).mean())
        as_ = float((clf_s.predict(Xs[te]) == y[te]).mean())
        uc = _auc(pc, y[te])
        us = _auc(ps, y[te])

        # magnitude: regress Φ
        reg_c = RandomForestRegressor(
            n_estimators=RF_N, random_state=SEED, n_jobs=1
        )
        reg_s = RandomForestRegressor(
            n_estimators=RF_N, random_state=SEED, n_jobs=1
        )
        reg_c.fit(Xc[tr], phi[tr])
        reg_s.fit(Xs[tr], phi[tr])
        rc = _spearman(reg_c.predict(Xc[te]), phi[te])
        rs = _spearman(reg_s.predict(Xs[te]), phi[te])

        maj = max(y[te].mean(), 1 - y[te].mean())
        lofo_rows.append({
            "family": fam,
            "n_test": int(te.sum()),
            "n_tri": int(y[te].sum()),
            "majority": maj,
            "auc_coupling": uc,
            "auc_structure": us,
            "acc_coupling": ac,
            "acc_structure": as_,
            "rho_coupling": rc,
            "rho_structure": rs,
        })
        if not np.isnan(uc):
            auc_c.append(uc)
        if not np.isnan(us):
            auc_s.append(us)
        acc_c.append(ac)
        acc_s.append(as_)
        if not np.isnan(rc):
            rho_c.append(rc)
        if not np.isnan(rs):
            rho_s.append(rs)
        print(
            f"  holdout={fam:<12} n={te.sum():<3} tri={y[te].sum()}  "
            f"AUC c={uc:.3f} s={us:.3f}  "
            f"acc c={ac:.2f} s={as_:.2f}  "
            f"ρ c={rc:.3f} s={rs:.3f}  maj={maj:.2f}"
        )

    mean_auc_c = float(np.nanmean(auc_c)) if auc_c else float("nan")
    mean_auc_s = float(np.nanmean(auc_s)) if auc_s else float("nan")
    mean_acc_c = float(np.mean(acc_c)) if acc_c else float("nan")
    mean_acc_s = float(np.mean(acc_s)) if acc_s else float("nan")
    mean_rho_c = float(np.nanmean(rho_c)) if rho_c else float("nan")
    mean_rho_s = float(np.nanmean(rho_s)) if rho_s else float("nan")
    lift_auc = mean_auc_s - mean_auc_c
    lift_rho = mean_rho_s - mean_rho_c

    print()
    print("AGGREGATE LOFO")
    print("-" * 80)
    print(f"  mean AUC  coupling={mean_auc_c:.3f}  structure={mean_auc_s:.3f}  "
          f"lift={lift_auc:+.3f}")
    print(f"  mean acc  coupling={mean_acc_c:.3f}  structure={mean_acc_s:.3f}")
    print(f"  mean ρ    coupling={mean_rho_c:.3f}  structure={mean_rho_s:.3f}  "
          f"lift={lift_rho:+.3f}")

    # Also: pooled coupling single-feature AUCs (sanity vs #134)
    mean_mi = Xc[:, 3]  # mean MI slot
    pooled_mi_auc = _auc(mean_mi, y)
    print(f"  pooled mean-MI AUC (all forms, no LOFO)={pooled_mi_auc:.3f}  "
          f"(#134-style check)")

    h1 = (
        ctrl
        and lift_auc >= 0.15
        and mean_auc_s >= 0.70
    )
    h2 = ctrl and abs(lift_auc) < 0.05
    det_gain = lift_auc >= 0.15 and mean_auc_s >= 0.70
    mag_gain = lift_rho >= 0.10
    h3 = ctrl and ((det_gain and not mag_gain) or (mag_gain and not det_gain))

    # mutual exclusion cleanup: if H1 and H2 both true somehow, prefer H1
    if h1 and h2:
        h2 = False

    if h1 and not h3:
        verdict_word = "STRUCTURE_GENERALIZES"
        reading = (
            "STRUCTURE_GENERALIZES — connectivity+function LOFO AUC beats "
            "coupling across held-out topologies; #22 affirmative"
        )
    elif h1 and h3:
        verdict_word = "STRUCTURE_DETECTS_NOT_MAG"
        reading = (
            "STRUCTURE_DETECTS_NOT_MAG — structure-aware lifts detection "
            "LOFO but not magnitude (or vice versa)"
        )
    elif h3 and not h1:
        verdict_word = "STRUCTURE_PARTIAL"
        reading = (
            "STRUCTURE_PARTIAL — asymmetric gain (detection vs magnitude)"
        )
    elif h2:
        verdict_word = "NO_STRUCTURE_GAIN"
        reading = (
            "NO_STRUCTURE_GAIN — structure-aware ≈ coupling under LOFO"
        )
    else:
        verdict_word = "STRUCTURE_FAILS"
        reading = (
            "STRUCTURE_FAILS — structure-aware does not clear H1; "
            "cross-topology gap remains"
        )

    # refine H3 labeling when H1 holds with mag failure
    if h1 and not mag_gain:
        verdict_word = "STRUCTURE_DETECTS_NOT_MAG"
        reading = (
            "STRUCTURE_DETECTS_NOT_MAG — structure-aware beats coupling on "
            "LOFO detection; magnitude gain <0.10; #22 partial on mag"
        )
        h3 = True

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (structure beats coupling LOFO): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}  "
          f"(lift={lift_auc:+.3f}, AUC_s={mean_auc_s:.3f})")
    print(f"  H2 (no gain |Δ|<0.05):              "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (detect≠magnitude gain):         "
          f"{'SUPPORTED' if h3 else 'REFUTED'}  "
          f"(ρ_lift={lift_rho:+.3f})")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  mean_auc_coupling={mean_auc_c:.3f}  "
          f"mean_auc_structure={mean_auc_s:.3f}  lift={lift_auc:+.3f}")
    print(f"  mean_rho_coupling={mean_rho_c:.3f}  "
          f"mean_rho_structure={mean_rho_s:.3f}  lift={lift_rho:+.3f}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = ["name", "family", "n", "structure", "max_phi", "triadic",
                  "elapsed_s"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    with open(os.path.join(RESULTS, "lofo.csv"), "w", newline="") as fh:
        if lofo_rows:
            fields = list(lofo_rows[0].keys())
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            for r in lofo_rows:
                out = {}
                for k, v in r.items():
                    if isinstance(v, float):
                        out[k] = f"{v:.6f}" if not np.isnan(v) else ""
                    else:
                        out[k] = v
                w.writerow(out)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "mean_auc_coupling": f"{mean_auc_c:.6f}",
            "mean_auc_structure": f"{mean_auc_s:.6f}",
            "lift_auc": f"{lift_auc:.6f}",
            "mean_rho_coupling": f"{mean_rho_c:.6f}",
            "mean_rho_structure": f"{mean_rho_s:.6f}",
            "lift_rho": f"{lift_rho:.6f}",
            "n_forms": len(rows),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
