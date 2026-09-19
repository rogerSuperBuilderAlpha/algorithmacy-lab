"""Joint-observation cliff under exact Φ, cross-topo (RESEARCH_AGENDA_V4 #1).

Does V3 #16 ALTERNATION_RECREATES_CLIFF transfer when the screen is
exact Φ (not MI-only) on a multifamily panel?

Exact binary IIT-4.0 via classify_rules. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/joint_obs_cliff_exact_phi/analyze_transfer.py
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
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_threshold_scaling import threshold_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

T = 2000
NOISE = 0.08
SEED = 41
MIN_PAIR_STEPS = 20
HOLD_AUC = 0.85
HOLD_GAP = 0.10
CLIFF_AUC = 0.70
CLIFF_DROP = 0.20


def _stable_seed(*parts, base=SEED):
    h = hashlib.md5("|".join(str(p) for p in parts).encode()).hexdigest()
    return base + (int(h[:8], 16) % 10_000)


def labels_for(n):
    if n == 3:
        return ("W", "S", "C")
    return tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)])


def roles_for(family, n):
    """(party_a, mediator, party_b)."""
    if family == "mediation":
        return 0, 1, 2
    return 1, 0, n - 1


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


def holds(auc, auc_ref):
    if np.isnan(auc) or np.isnan(auc_ref):
        return False
    return auc >= HOLD_AUC or (auc_ref - auc) <= HOLD_GAP


def cliffs(auc, auc_ref):
    if np.isnan(auc_ref):
        return False
    if np.isnan(auc):
        return auc_ref >= HOLD_AUC
    return auc < CLIFF_AUC or (auc_ref - auc) >= CLIFF_DROP


def induce(rules, n, keep):
    keep = tuple(keep)
    out = []
    for oi in keep:

        def make(oi=oi, keep=keep, n=n):
            def r(x):
                full = [0] * n
                for k, ix in enumerate(keep):
                    full[ix] = int(x[k])
                return int(rules[oi](full))

            return r

        out.append(make())
    return out


def phi_of(rules, n, keep=None):
    if keep is None:
        keep = tuple(range(n))
        sub = rules
        nn = n
    else:
        keep = tuple(keep)
        sub = induce(rules, n, keep)
        nn = len(keep)
    labs = tuple(f"N{i}" for i in range(nn))
    v = classify_rules(sub, labels=labs)
    return float(v.max_phi), v.structure


def mean_mi_masked(traj, obs_mask):
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


def mask_alt_parties(Tlen, n, party_a, party_b):
    m = np.ones((Tlen, n), dtype=bool)
    even = np.arange(Tlen) % 2 == 0
    m[:, party_a] = even
    m[:, party_b] = ~even
    return m


def simulate(rules, n, rng):
    tpm = add_noise(tpm_from_rules(rules), NOISE)
    return exact_phi.simulate_trajectory(tpm, n, T, rng)


def build_family_n3(rng):
    tri, dya = [], []
    for name, rules in enumerate_family():
        v = classify_rules(rules, labels=labels_for(3))
        row = {
            "name": name,
            "family": "mediation",
            "n": 3,
            "rules": rules,
            "triadic": int(v.structure == "triadic"),
            "phi_full": float(v.max_phi),
        }
        (tri if v.structure == "triadic" else dya).append(row)
    n_take = min(24, len(tri), len(dya))
    pick_t = [tri[i] for i in rng.choice(len(tri), n_take, replace=False)]
    pick_d = [dya[i] for i in rng.choice(len(dya), n_take, replace=False)]
    return pick_t + pick_d


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


def build_multifamily():
    forms = []

    def add(family, name, n, rules):
        v = classify_rules(rules, labels=labels_for(n))
        forms.append({
            "name": name,
            "family": family,
            "n": n,
            "rules": rules,
            "triadic": int(v.structure == "triadic"),
            "phi_full": float(v.max_phi),
        })

    for n in (3, 4):
        add("chain", f"chain_and_n{n}", n, chain(n))
        add("chain", f"chain_ff_n{n}", n, chain_ff(n))
        add("pool", f"pool_and_n{n}", n, pool(n))
        add("pool", f"pool_or_n{n}", n, or_pool(n))
        add("hub", f"and_hub_n{n}", n, single_hub(n))
        add("hub", f"broken_hub_n{n}", n, broken_hub(n))
        add("or_hub", f"or_hub_n{n}", n, or_hub(n))
        add("parity", f"parity_hub_n{n}", n, parity_hub(n))
        add("broadcast", f"broadcast_n{n}", n, broadcast(n))
        add("majority", f"maj_n{n}", n, threshold_hub(n, (n - 1) // 2 + 1))
        add("majority", f"thresh1_n{n}", n, threshold_hub(n, 1))
        if n >= 4:
            add("ring", f"ring_n{n}", n, ring(n))
    add("two_hub", "two_hub_n4", 4, two_hub(4))
    return forms


def score_phi_screens(form):
    n = form["n"]
    rules = form["rules"]
    a, m, b = roles_for(form["family"], n)
    phi_full = form["phi_full"]
    keep_omit = tuple(i for i in range(n) if i != b)
    phi_zero, _ = phi_of(rules, n, keep_omit)
    phi_ma, _ = phi_of(rules, n, (m, a))
    phi_mb, _ = phi_of(rules, n, (m, b))
    phi_alt = 0.5 * (phi_ma + phi_mb)
    return {
        "phi_full": phi_full,
        "phi_zero_duty_B": phi_zero,
        "phi_alt": phi_alt,
        "phi_phase": phi_full,
        "phi_MA": phi_ma,
        "phi_MB": phi_mb,
    }


def score_mi_screens(form, rng):
    n = form["n"]
    a, _m, b = roles_for(form["family"], n)
    traj = simulate(form["rules"], n, rng)
    mi_full = mean_mi_masked(traj, mask_full(T, n))
    mi_alt = mean_mi_masked(traj, mask_alt_parties(T, n, a, b))
    return {"mi_full": mi_full, "mi_alt": mi_alt}


def panel_auc(rows, key):
    scores = [r[key] for r in rows]
    labels = [r["triadic"] for r in rows]
    return oriented_auc(scores, labels)


def main():
    print("AGENDA V4 #1 — JOINT-OBS CLIFF UNDER EXACT Φ (CROSS-TOPO)")
    print("=" * 80)
    print("  cited: V3 #16 ALTERNATION_RECREATES_CLIFF; V2 #24")
    print("  pointer: V3_LANE_CLOSE; exact Φ via classify_rules")
    print(
        f"  protocol: hold AUC≥{HOLD_AUC} or within {HOLD_GAP} of phi_full; "
        f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}"
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

    print("BUILD PANELS")
    print("-" * 80)
    family = build_family_n3(rng)
    multi = build_multifamily()
    n_tri_f = sum(r["triadic"] for r in family)
    n_tri_m = sum(r["triadic"] for r in multi)
    print(
        f"  family_n3: {len(family)} forms ({n_tri_f} tri / "
        f"{len(family) - n_tri_f} dya)"
    )
    print(
        f"  multifamily: {len(multi)} forms ({n_tri_m} tri / "
        f"{len(multi) - n_tri_m} dya)"
    )
    print()

    print("SCORE exact-Φ screens")
    print("-" * 80)
    t0 = time.time()
    for row in family + multi:
        row.update(score_phi_screens(row))
    print(f"  scored {len(family) + len(multi)} forms ({time.time() - t0:.1f}s)")
    print()

    print("SCORE MI screens (family_n3 only; #16 control)")
    print("-" * 80)
    t0 = time.time()
    for row in family:
        local = np.random.default_rng(_stable_seed("mi", row["name"]))
        row.update(score_mi_screens(row, local))
    print(f"  scored {len(family)} forms ({time.time() - t0:.1f}s)")
    print()

    aucs = {}
    print("PANEL AUCs")
    print("-" * 80)
    for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
        keys = ["phi_full", "phi_zero_duty_B", "phi_alt", "phi_phase"]
        if panel_name == "family_n3":
            keys = keys + ["mi_full", "mi_alt"]
        for key in keys:
            auc, orient = panel_auc(rows, key)
            aucs[f"{panel_name}:{key}"] = (auc, orient)
            print(
                f"  {panel_name:12s} {key:16s}  AUC={auc:.3f}  "
                f"orient={orient:+d}"
            )
    print()

    def A(panel, key):
        return aucs[f"{panel}:{key}"][0]

    auc_phi_full_f = A("family_n3", "phi_full")
    auc_phi_alt_f = A("family_n3", "phi_alt")
    auc_phi_zero_f = A("family_n3", "phi_zero_duty_B")
    auc_phi_full_m = A("multifamily", "phi_full")
    auc_phi_alt_m = A("multifamily", "phi_alt")
    auc_mi_full = A("family_n3", "mi_full")
    auc_mi_alt = A("family_n3", "mi_alt")

    h1 = (
        ctrl
        and (not np.isnan(auc_mi_full))
        and auc_mi_full >= HOLD_AUC
        and cliffs(auc_mi_alt, auc_mi_full)
    )
    h2 = (
        ctrl
        and (not np.isnan(auc_phi_full_f))
        and auc_phi_full_f >= HOLD_AUC
        and cliffs(auc_phi_alt_f, auc_phi_full_f)
    )
    h3 = ctrl and cliffs(auc_phi_alt_m, auc_phi_full_m)
    h4 = (
        ctrl
        and (not np.isnan(auc_phi_full_f))
        and (not np.isnan(auc_phi_full_m))
        and auc_phi_full_f >= HOLD_AUC
        and auc_phi_full_m >= HOLD_AUC
    )
    h5 = ctrl and cliffs(auc_phi_zero_f, auc_phi_full_f)

    if (not h1) or (not h4):
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H1={h1} H4={h4}; mi_full={auc_mi_full:.3f} "
            f"mi_alt={auc_mi_alt:.3f}; phi_full_f={auc_phi_full_f:.3f} "
            f"phi_full_m={auc_phi_full_m:.3f}"
        )
    elif h1 and h2 and h3 and h4:
        verdict = "TRANSFER_HOLDS_EXACT_PHI"
        reading = (
            f"TRANSFER_HOLDS_EXACT_PHI — MI replicate cliffs; exact-Φ alt "
            f"cliffs on family_n3 ({auc_phi_full_f:.3f}→{auc_phi_alt_f:.3f}) "
            f"and multifamily ({auc_phi_full_m:.3f}→{auc_phi_alt_m:.3f}); "
            f"phi_full holds; zero_duty_f={auc_phi_zero_f:.3f}"
        )
    elif h1 and (not h2) and h3 and h4:
        verdict = "TRANSFER_PARTIAL_EXACT_PHI"
        reading = (
            f"TRANSFER_PARTIAL_EXACT_PHI — MI alt cliffs "
            f"({auc_mi_full:.3f}→{auc_mi_alt:.3f}); exact-Φ alt soft on "
            f"family_n3 ({auc_phi_full_f:.3f}→{auc_phi_alt_f:.3f}, no "
            f"cliff bar) but cliffs on multifamily "
            f"({auc_phi_full_m:.3f}→{auc_phi_alt_m:.3f}); "
            f"zero_duty_f={auc_phi_zero_f:.3f}"
        )
    elif h1 and (not h2) and (not h3) and h4:
        verdict = "EXACT_PHI_ROBUST_MI_ONLY"
        reading = (
            f"EXACT_PHI_ROBUST_MI_ONLY — MI alt cliffs "
            f"({auc_mi_full:.3f}→{auc_mi_alt:.3f}) but exact-Φ alt holds "
            f"on family_n3 ({auc_phi_full_f:.3f}→{auc_phi_alt_f:.3f}) and "
            f"multifamily ({auc_phi_full_m:.3f}→{auc_phi_alt_m:.3f})"
        )
    elif h1 and h2 and (not h3) and h4:
        verdict = "FAMILY_N3_ONLY"
        reading = (
            f"FAMILY_N3_ONLY — exact-Φ alt cliffs on family_n3 "
            f"({auc_phi_full_f:.3f}→{auc_phi_alt_f:.3f}) but not on "
            f"multifamily ({auc_phi_full_m:.3f}→{auc_phi_alt_m:.3f})"
        )
    else:
        verdict = "TRANSFER_MIXED"
        reading = (
            f"TRANSFER_MIXED — H1={h1} H2={h2} H3={h3} H4={h4} H5={h5}; "
            f"phi_alt_f={auc_phi_alt_f:.3f} phi_alt_m={auc_phi_alt_m:.3f} "
            f"zero_f={auc_phi_zero_f:.3f}"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  family_n3:   phi_full={auc_phi_full_f:.3f}  "
        f"phi_alt={auc_phi_alt_f:.3f}  phi_zero={auc_phi_zero_f:.3f}"
    )
    print(
        f"  family_n3:   mi_full={auc_mi_full:.3f}  mi_alt={auc_mi_alt:.3f}"
    )
    print(
        f"  multifamily: phi_full={auc_phi_full_m:.3f}  "
        f"phi_alt={auc_phi_alt_m:.3f}"
    )
    print(
        f"  H1 (MI alt cliffs on family_n3):           "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (exact-Φ alt cliffs on family_n3):      "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (exact-Φ alt cliffs on multifamily):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (exact-Φ full holds both panels):       "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (exact-Φ zero-duty cliffs family_n3):   "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
        f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
        f"H5={('SUPPORTED' if h5 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(
        f"  metrics: phi_full_f={auc_phi_full_f:.3f}; "
        f"phi_alt_f={auc_phi_alt_f:.3f}; phi_zero_f={auc_phi_zero_f:.3f}; "
        f"phi_full_m={auc_phi_full_m:.3f}; phi_alt_m={auc_phi_alt_m:.3f}; "
        f"mi_full={auc_mi_full:.3f}; mi_alt={auc_mi_alt:.3f}"
    )
    print("  best next:         V4 #2 phase-lock under exact Φ")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["panel", "screen", "n_forms", "n_tri", "auc", "orient"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
            n_tri = sum(r["triadic"] for r in rows)
            keys = ["phi_full", "phi_zero_duty_B", "phi_alt", "phi_phase"]
            if panel_name == "family_n3":
                keys = keys + ["mi_full", "mi_alt"]
            for key in keys:
                auc, orient = aucs[f"{panel_name}:{key}"]
                w.writerow({
                    "panel": panel_name,
                    "screen": key,
                    "n_forms": len(rows),
                    "n_tri": n_tri,
                    "auc": f"{auc:.6f}" if not np.isnan(auc) else "",
                    "orient": orient,
                })

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = [
            "panel", "family", "n", "name", "triadic", "phi_full",
            "phi_zero_duty_B", "phi_alt", "phi_MA", "phi_MB",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for panel_name, rows in [("family_n3", family), ("multifamily", multi)]:
            for r in rows:
                w.writerow({
                    "panel": panel_name,
                    "family": r["family"],
                    "n": r["n"],
                    "name": r["name"],
                    "triadic": r["triadic"],
                    "phi_full": f"{r['phi_full']:.6f}",
                    "phi_zero_duty_B": f"{r['phi_zero_duty_B']:.6f}",
                    "phi_alt": f"{r['phi_alt']:.6f}",
                    "phi_MA": f"{r['phi_MA']:.6f}",
                    "phi_MB": f"{r['phi_MB']:.6f}",
                })

    summary = {
        "verdict": verdict,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "phi_full_family_auc": round(float(auc_phi_full_f), 6),
        "phi_alt_family_auc": round(float(auc_phi_alt_f), 6),
        "phi_zero_family_auc": round(float(auc_phi_zero_f), 6),
        "phi_full_multi_auc": round(float(auc_phi_full_m), 6),
        "phi_alt_multi_auc": round(float(auc_phi_alt_m), 6),
        "mi_full_auc": round(float(auc_mi_full), 6),
        "mi_alt_auc": round(float(auc_mi_alt), 6),
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
