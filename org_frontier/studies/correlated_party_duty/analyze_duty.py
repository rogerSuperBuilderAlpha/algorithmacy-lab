"""Correlated party duty cycles vs δ=0 cliff (RESEARCH_AGENDA_V3 #16).

Does alternating observation of two parties soften V2 #24's
intermittent cliff at δ=0, or does any zero-duty party recreate it?

Exact binary IIT-4.0 labels; mean-MI screen. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/correlated_party_duty/analyze_duty.py
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
SEED = 16
MIN_PAIR_STEPS = 20
SOFTEN_AUC = 0.85
SOFTEN_GAP = 0.10
CLIFF_AUC = 0.70
CLIFF_DROP = 0.20

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


def mask_full(Tlen, n):
    return np.ones((Tlen, n), dtype=bool)


def mask_hidden(Tlen, n, hidden_idx):
    m = np.ones((Tlen, n), dtype=bool)
    m[:, hidden_idx] = False
    return m


def mask_intermittent(Tlen, n, node_idx, duty, rng):
    m = np.ones((Tlen, n), dtype=bool)
    if duty <= 0.0:
        m[:, node_idx] = False
    elif duty >= 1.0:
        pass
    else:
        m[:, node_idx] = rng.random(Tlen) < duty
    return m


def mask_alt_wc(Tlen, n):
    """W on even slots, C on odd; S always. No joint WC observation."""
    m = np.ones((Tlen, n), dtype=bool)
    even = np.arange(Tlen) % 2 == 0
    m[:, IDX_W] = even
    m[:, IDX_C] = ~even
    return m


def mask_phase_wc(Tlen, n):
    """W and C both on even slots only (δ=0.5); joint WC preserved."""
    m = np.ones((Tlen, n), dtype=bool)
    even = np.arange(Tlen) % 2 == 0
    m[:, IDX_W] = even
    m[:, IDX_C] = even
    return m


def build_family_n3(rng):
    tri, dya = [], []
    for name, rules in enumerate_family():
        v = classify_rules(rules, labels=labels_for(3))
        row = (
            name,
            rules,
            int(v.structure == "triadic"),
            float(v.max_phi),
            "strict_med",
        )
        (tri if v.structure == "triadic" else dya).append(row)
    n_take = min(24, len(tri), len(dya))
    pick_t = [tri[i] for i in rng.choice(len(tri), n_take, replace=False)]
    pick_d = [dya[i] for i in rng.choice(len(dya), n_take, replace=False)]
    return pick_t + pick_d


def simulate(rules, n, rng):
    tpm = add_noise(tpm_from_rules(rules), NOISE)
    return exact_phi.simulate_trajectory(tpm, n, T, rng)


def softens(auc, auc_full):
    if np.isnan(auc) or np.isnan(auc_full):
        return False
    return auc >= SOFTEN_AUC or (auc_full - auc) <= SOFTEN_GAP


def cliffs(auc, auc_full):
    if np.isnan(auc) or np.isnan(auc_full):
        return False
    return auc < CLIFF_AUC or (auc_full - auc) >= CLIFF_DROP


def score_regime(forms, rng_key, mask_fn):
    scores, labels = [], []
    local = np.random.default_rng(_stable_seed("fam", rng_key))
    for row in forms:
        _name, rules, tri, _phi = row[0], row[1], row[2], row[3]
        traj = simulate(rules, 3, local)
        mask = mask_fn(local)
        scores.append(mean_mi_masked(traj, mask))
        labels.append(tri)
    return np.asarray(scores, float), np.asarray(labels, int)


def main():
    print("AGENDA V3 #16 — CORRELATED PARTY DUTY CYCLES vs δ=0 CLIFF")
    print("=" * 80)
    print("  cited: V2 #24 HIDDEN_COLLAPSE_INTERMITTENT_CLIFF; V3 #15")
    print("  pointer: ESTIMATION_ARC; family_n3 mean-MI screen")
    print(
        f"  protocol: T={T}, noise={NOISE}; soften AUC≥{SOFTEN_AUC} "
        f"or within {SOFTEN_GAP} of full; cliff AUC<{CLIFF_AUC} "
        f"or drop≥{CLIFF_DROP}"
    )
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
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl else 'FAIL'}"
    )
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rng = np.random.default_rng(SEED)
    t_all = time.time()

    print("BUILD PANEL (exact labels)")
    print("-" * 80)
    family = build_family_n3(rng)
    n_tri = sum(r[2] for r in family)
    print(
        f"  family_n3: {len(family)} forms ({n_tri} tri / "
        f"{len(family) - n_tri} dya)"
    )
    print()

    regimes = [
        ("full", lambda _rng: mask_full(T, 3)),
        ("zero_duty_C", lambda _rng: mask_hidden(T, 3, IDX_C)),
        ("zero_duty_W", lambda _rng: mask_hidden(T, 3, IDX_W)),
        (
            "sparse_C_d0.10",
            lambda r: mask_intermittent(T, 3, IDX_C, 0.10, r),
        ),
        ("alt_WC", lambda _rng: mask_alt_wc(T, 3)),
        ("phase_WC_d0.50", lambda _rng: mask_phase_wc(T, 3)),
        ("hide_mediator", lambda _rng: mask_hidden(T, 3, IDX_S)),
    ]

    print("FAMILY_N3 — observation regimes")
    print("-" * 80)
    aucs = {}
    curve_rows = []
    for tag, mask_fn in regimes:
        t0 = time.time()
        sc, y = score_regime(family, tag, mask_fn)
        auc, orient = oriented_auc(sc, y)
        aucs[tag] = auc
        print(
            f"  {tag:18s}  MI AUC={auc:.3f}  orient={orient:+d}  "
            f"n={len(y)}  ({time.time() - t0:.1f}s)"
        )
        curve_rows.append({
            "regime": tag,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": auc,
            "orient": orient,
        })
    print()

    auc_full = aucs["full"]
    auc_zC = aucs["zero_duty_C"]
    auc_zW = aucs["zero_duty_W"]
    auc_sparse = aucs["sparse_C_d0.10"]
    auc_alt = aucs["alt_WC"]
    auc_phase = aucs["phase_WC_d0.50"]
    auc_med = aucs["hide_mediator"]

    h1 = ctrl and cliffs(auc_zC, auc_full) and cliffs(auc_zW, auc_full)
    h2 = ctrl and softens(auc_alt, auc_full)
    h3 = ctrl and softens(auc_phase, auc_full)
    h4 = ctrl and softens(auc_sparse, auc_full)
    h5 = ctrl and (not np.isnan(auc_med)) and auc_med >= 0.85

    if not h4 or not h5:
        verdict_word = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H4={h4} H5={h5}; sparse={auc_sparse:.3f} "
            f"hide_med={auc_med:.3f}; full={auc_full:.3f}"
        )
    elif not h1:
        verdict_word = "CLIFF_UNRELATED"
        reading = (
            f"CLIFF_UNRELATED — zero-duty does not cliff "
            f"(zC={auc_zC:.3f}, zW={auc_zW:.3f}; full={auc_full:.3f})"
        )
    elif h2:
        verdict_word = "CORRELATED_SOFTENS_CLIFF"
        reading = (
            f"CORRELATED_SOFTENS_CLIFF — alt_WC softens "
            f"(AUC={auc_alt:.3f}); zero-duty recreates cliff "
            f"(zC={auc_zC:.3f}, zW={auc_zW:.3f}); phase={auc_phase:.3f}; "
            f"sparse_d0.10={auc_sparse:.3f}"
        )
    else:
        verdict_word = "ALTERNATION_RECREATES_CLIFF"
        reading = (
            f"ALTERNATION_RECREATES_CLIFF — alt_WC fails soften bar "
            f"(AUC={auc_alt:.3f} vs full={auc_full:.3f}); zero-duty "
            f"still cliffs (zC={auc_zC:.3f}); losing joint WC "
            f"observation is enough to recreate the δ=0 cliff"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  full={auc_full:.3f}  zero_C={auc_zC:.3f}  zero_W={auc_zW:.3f}")
    print(
        f"  sparse_d0.10={auc_sparse:.3f}  alt_WC={auc_alt:.3f}  "
        f"phase_WC={auc_phase:.3f}  hide_med={auc_med:.3f}"
    )
    print(
        f"  H1 (zero-duty recreates cliff):         "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (alt_WC softens cliff):              "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (phase_WC softens):                  "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (sparse δ=0.10 holds):               "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (hide mediator stays ≥0.85):         "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
        f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
        f"H5={('SUPPORTED' if h5 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(
        f"  metrics: full={auc_full:.3f}; zero_C={auc_zC:.3f}; "
        f"zero_W={auc_zW:.3f}; sparse={auc_sparse:.3f}; "
        f"alt_WC={auc_alt:.3f}; phase_WC={auc_phase:.3f}; "
        f"hide_med={auc_med:.3f}"
    )
    print("  best next:         V3 lane closed — see V3_LANE_CLOSE.md")
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
                "panel": "family_n3",
                "family": fam,
                "n": 3,
                "name": name,
                "triadic": tri,
                "max_phi": f"{phi:.6f}",
            })

    summary = {
        "verdict": verdict_word,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "full_auc": round(float(auc_full), 6),
        "zero_duty_C_auc": round(float(auc_zC), 6),
        "zero_duty_W_auc": round(float(auc_zW), 6),
        "sparse_C_d010_auc": round(float(auc_sparse), 6),
        "alt_WC_auc": round(float(auc_alt), 6),
        "phase_WC_auc": round(float(auc_phase), 6),
        "hide_mediator_auc": round(float(auc_med), 6),
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
