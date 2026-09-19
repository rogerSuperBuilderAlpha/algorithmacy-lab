"""Topology-aware imputer under role-gated collapse (RESEARCH_AGENDA_V3 #15).

Under V2 #24 hide-party MI collapse, do ring vs hub priors restore AUC,
or is party absence a hard information cut?

Exact binary IIT-4.0 labels; mean-MI screen. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/topology_aware_imputer/analyze_imputer.py
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import sys
import time

import numpy as np
from sklearn.metrics import roc_auc_score

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from org_frontier.probes._info import mutual_information
from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

T = 2000
NOISE = 0.08
SEED = 15
MIN_PAIR_STEPS = 20
RESTORE_AUC = 0.85
RESTORE_GAP = 0.10
NAIVE_LIFT = 0.05

# Role indices on family_n3 labels (W, S, C)
IDX_W, IDX_S, IDX_C = 0, 1, 2


def _stable_seed(*parts, base=SEED):
    h = hashlib.md5("|".join(str(p) for p in parts).encode()).hexdigest()
    return base + (int(h[:8], 16) % 10_000)


def labels_for(n):
    if n == 3:
        return ("W", "S", "C")
    return tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)])


def _auc(scores, labels):
    scores = np.asarray(scores, float)
    labels = np.asarray(labels, int)
    if labels.sum() == 0 or labels.sum() == len(labels):
        return float("nan")
    finite = np.isfinite(scores)
    if finite.sum() < 4 or labels[finite].sum() == 0 or labels[finite].sum() == finite.sum():
        return float("nan")
    try:
        return float(roc_auc_score(labels[finite], scores[finite]))
    except ValueError:
        return float("nan")


def oriented_auc(scores, labels):
    a = _auc(scores, labels)
    b = _auc(-np.asarray(scores, float), labels)
    if np.isnan(a) and np.isnan(b):
        return float("nan"), 0
    if np.isnan(a):
        return b, -1
    if np.isnan(b):
        return a, +1
    if b > a:
        return b, -1
    return a, +1


def mean_mi_masked(traj, obs_mask):
    """Mean pairwise MI using complete cases under a T×n observation mask."""
    _Tlen, n = traj.shape
    pair_mis = []
    for i in range(n):
        for j in range(i + 1, n):
            keep = obs_mask[:, i] & obs_mask[:, j]
            if int(keep.sum()) < MIN_PAIR_STEPS:
                continue
            sub = traj[keep][:, [i, j]]
            pair_mis.append(mutual_information(sub, [0], [1]))
    if not pair_mis:
        return float("nan")
    return float(np.mean(pair_mis))


def mean_mi_full(traj):
    return mean_mi_masked(traj, np.ones(traj.shape, dtype=bool))


def mask_hidden(Tlen, n, hidden_idx):
    m = np.ones((Tlen, n), dtype=bool)
    m[:, hidden_idx] = False
    return m


def build_family_n3(rng):
    tri, dya = [], []
    for name, rules in enumerate_family():
        v = classify_rules(rules, labels=labels_for(3))
        row = (name, rules, int(v.structure == "triadic"), float(v.max_phi), "strict_med")
        (tri if v.structure == "triadic" else dya).append(row)
    n_take = min(24, len(tri), len(dya))
    pick_t = [tri[i] for i in rng.choice(len(tri), n_take, replace=False)]
    pick_d = [dya[i] for i in rng.choice(len(dya), n_take, replace=False)]
    return pick_t + pick_d


def simulate(rules, n, rng):
    tpm = add_noise(tpm_from_rules(rules), NOISE)
    return exact_phi.simulate_trajectory(tpm, n, T, rng)


def impute_hub_prior(traj):
    """Fill C under conjunctive-hub prior (parties mirror; AND consistency)."""
    out = traj.copy()
    W = traj[:, IDX_W].astype(int)
    S = traj[:, IDX_S].astype(int)
    C = np.empty(len(traj), dtype=int)
    C[0] = int(S[0])
    C[1:] = S[:-1]
    for t in range(1, len(traj)):
        if S[t] == 1:
            C[t - 1] = 1
        elif W[t - 1] == 1:
            C[t - 1] = 0
    # final step: mirror only
    C[-1] = int(S[-1])
    out[:, IDX_C] = C
    return out


def impute_ring_prior(traj):
    """Fill C under 3-cycle copy prior: C'=S, W'=C → C_t≈W_{t+1} else S_{t-1}."""
    out = traj.copy()
    W = traj[:, IDX_W].astype(int)
    S = traj[:, IDX_S].astype(int)
    C = np.empty(len(traj), dtype=int)
    C[:-1] = W[1:]
    C[-1] = int(S[-2]) if len(S) > 1 else int(S[-1])
    # where lookahead unavailable already set; reinforce lag-copy at t=0
    # (W_1 = C_0 under ring, already used). Optional lag fill if needed:
    for t in range(len(traj)):
        if t + 1 < len(traj):
            C[t] = int(W[t + 1])
        elif t > 0:
            C[t] = int(S[t - 1])
        else:
            C[t] = int(S[t])
    out[:, IDX_C] = C
    return out


def impute_copy_w(traj):
    out = traj.copy()
    out[:, IDX_C] = traj[:, IDX_W]
    return out


def impute_copy_s(traj):
    out = traj.copy()
    out[:, IDX_C] = traj[:, IDX_S]
    return out


def impute_const0(traj):
    out = traj.copy()
    out[:, IDX_C] = 0
    return out


def impute_bernoulli(traj, rng):
    out = traj.copy()
    out[:, IDX_C] = rng.integers(0, 2, size=len(traj))
    return out


IMPUTERS = {
    "hub_prior": lambda traj, rng: impute_hub_prior(traj),
    "ring_prior": lambda traj, rng: impute_ring_prior(traj),
    "naive_copy_w": lambda traj, rng: impute_copy_w(traj),
    "naive_copy_s": lambda traj, rng: impute_copy_s(traj),
    "naive_const0": lambda traj, rng: impute_const0(traj),
    "naive_bernoulli": lambda traj, rng: impute_bernoulli(traj, rng),
}


def restores(auc, auc_full):
    if np.isnan(auc) or np.isnan(auc_full):
        return False
    return auc >= RESTORE_AUC or (auc_full - auc) <= RESTORE_GAP


def score_regime(forms, rng_key, mode, hidden_idx=None, imputer=None):
    """mode: full | hidden | impute."""
    scores, labels = [], []
    local = np.random.default_rng(_stable_seed("fam", rng_key))
    for row in forms:
        name, rules, tri, _phi = row[0], row[1], row[2], row[3]
        traj = simulate(rules, 3, local)
        if mode == "full":
            score = mean_mi_full(traj)
        elif mode == "hidden":
            mask = mask_hidden(T, 3, hidden_idx)
            score = mean_mi_masked(traj, mask)
        elif mode == "impute":
            filled = IMPUTERS[imputer](traj, local)
            # observed W,S kept; only C replaced — score as full completed traj
            score = mean_mi_full(filled)
        else:
            raise ValueError(mode)
        scores.append(score)
        labels.append(tri)
    return np.asarray(scores, float), np.asarray(labels, int)


def main():
    print("AGENDA V3 #15 — TOPOLOGY-AWARE IMPUTER (ROLE-GATED COLLAPSE)")
    print("=" * 80)
    print("  cited: V2 #24 HIDDEN_COLLAPSE_INTERMITTENT_CLIFF; #122/#23")
    print("  pointer: ESTIMATION_ARC; family_n3 mean-MI screen")
    print(f"  protocol: T={T}, noise={NOISE}; restore AUC≥{RESTORE_AUC} "
          f"or within {RESTORE_GAP} of full")
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
    t_all = time.time()

    print("BUILD PANEL (exact labels)")
    print("-" * 80)
    family = build_family_n3(rng)
    n_tri = sum(r[2] for r in family)
    print(f"  family_n3: {len(family)} forms ({n_tri} tri / "
          f"{len(family) - n_tri} dya)")
    print()

    regimes = []
    # baselines
    for tag, mode, hidx, imp in [
        ("full", "full", None, None),
        ("hide_party_C", "hidden", IDX_C, None),
        ("hide_mediator_S", "hidden", IDX_S, None),
        ("hub_prior", "impute", IDX_C, "hub_prior"),
        ("ring_prior", "impute", IDX_C, "ring_prior"),
        ("naive_copy_w", "impute", IDX_C, "naive_copy_w"),
        ("naive_copy_s", "impute", IDX_C, "naive_copy_s"),
        ("naive_const0", "impute", IDX_C, "naive_const0"),
        ("naive_bernoulli", "impute", IDX_C, "naive_bernoulli"),
    ]:
        regimes.append((tag, mode, hidx, imp))

    print("FAMILY_N3 — observation / imputation regimes")
    print("-" * 80)
    aucs = {}
    orients = {}
    curve_rows = []
    for tag, mode, hidx, imp in regimes:
        t0 = time.time()
        sc, y = score_regime(family, tag, mode, hidden_idx=hidx, imputer=imp)
        auc, orient = oriented_auc(sc, y)
        aucs[tag] = auc
        orients[tag] = orient
        print(f"  {tag:18s}  MI AUC={auc:.3f}  orient={orient:+d}  "
              f"n={len(y)}  ({time.time() - t0:.1f}s)")
        curve_rows.append({
            "regime": tag,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": auc,
            "orient": orient,
        })
    print()

    auc_full = aucs["full"]
    auc_hid = aucs["hide_party_C"]
    auc_med = aucs["hide_mediator_S"]
    auc_hub = aucs["hub_prior"]
    auc_ring = aucs["ring_prior"]
    naive_tags = [
        "naive_copy_w", "naive_copy_s", "naive_const0", "naive_bernoulli",
    ]
    naive_best = max(aucs[t] for t in naive_tags)
    topo_best = max(auc_hub, auc_ring)
    drop = auc_full - auc_hid

    h1 = (
        ctrl
        and (not np.isnan(auc_full)) and auc_full >= 0.90
        and (not np.isnan(auc_hid))
        and (drop >= 0.20 or auc_hid < 0.70)
    )
    h2 = ctrl and restores(auc_hub, auc_full)
    h3 = ctrl and restores(auc_ring, auc_full)
    h4 = (
        ctrl
        and (not np.isnan(topo_best)) and (not np.isnan(naive_best))
        and (topo_best - naive_best) >= NAIVE_LIFT
    )
    h5 = ctrl and (not np.isnan(auc_med)) and auc_med >= 0.85

    if not h1 or not h5:
        verdict_word = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H1={h1} H5={h5}; full={auc_full:.3f} "
            f"hid={auc_hid:.3f} med={auc_med:.3f}"
        )
    elif h2 or h3:
        verdict_word = "IMPUTER_RESTORES_AUC"
        which = []
        if h2:
            which.append(f"hub={auc_hub:.3f}")
        if h3:
            which.append(f"ring={auc_ring:.3f}")
        reading = (
            f"IMPUTER_RESTORES_AUC — hide-party collapse "
            f"(full={auc_full:.3f}→{auc_hid:.3f}) repaired by "
            + " & ".join(which)
            + f"; naive_best={naive_best:.3f}; topo_lift="
            f"{topo_best - naive_best:.3f}"
        )
    else:
        verdict_word = "PARTY_ABSENCE_HARD_CUT"
        reading = (
            f"PARTY_ABSENCE_HARD_CUT — hide-party collapse "
            f"(full={auc_full:.3f}→{auc_hid:.3f}) survives hub="
            f"{auc_hub:.3f} and ring={auc_ring:.3f}; naive_best="
            f"{naive_best:.3f}; no topology prior restores the MI screen"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  full={auc_full:.3f}  hide_party={auc_hid:.3f}  "
          f"hide_mediator={auc_med:.3f}")
    print(f"  hub_prior={auc_hub:.3f}  ring_prior={auc_ring:.3f}  "
          f"topo_best={topo_best:.3f}  naive_best={naive_best:.3f}")
    print(f"  drop_party={drop:.3f}  topo−naive={topo_best - naive_best:.3f}")
    print(f"  H1 (hide party collapses):              "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (hub prior restores):                "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (ring prior restores):               "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (topo beats naive by ≥{NAIVE_LIFT}):        "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (hide mediator stays ≥0.85):         "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(
        f"  metrics: full={auc_full:.3f}; hide_party={auc_hid:.3f}; "
        f"hide_mediator={auc_med:.3f}; hub={auc_hub:.3f}; "
        f"ring={auc_ring:.3f}; naive_best={naive_best:.3f}"
    )
    print("  best next:         #16 correlated party duty cycles (last V3 cell)")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["regime", "n_forms", "n_tri", "mi_auc", "orient"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in curve_rows:
            w.writerow({
                "regime": r["regime"],
                "n_forms": r["n_forms"],
                "n_tri": r["n_tri"],
                "mi_auc": (
                    f"{r['mi_auc']:.6f}" if not np.isnan(r["mi_auc"]) else ""
                ),
                "orient": r["orient"],
            })

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["panel", "family", "n", "name", "triadic", "max_phi"],
        )
        w.writeheader()
        for name, _, tri, phi, fam in family:
            w.writerow({
                "panel": "family_n3", "family": fam, "n": 3,
                "name": name, "triadic": tri, "max_phi": f"{phi:.6f}",
            })

    summary = {
        "verdict": verdict_word,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "full_auc": round(float(auc_full), 6),
        "hide_party_auc": round(float(auc_hid), 6),
        "hide_mediator_auc": round(float(auc_med), 6),
        "hub_prior_auc": round(float(auc_hub), 6),
        "ring_prior_auc": round(float(auc_ring), 6),
        "naive_best_auc": round(float(naive_best), 6),
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
