"""Agenda #24 — estimability under partial observation.

Exact IIT-4.0 labels; cheap mean-MI screen under full / hidden /
intermittent observation. Hypotheses fixed in hypotheses.md before
computing.

Cited: #122/#23 FAST_WITHIN_FAMILY; #21 SPECTRAL_PARTIAL; #22; #25;
#134; ESTIMATION_ARC. Construct/omit/ladder/indeg closed.

Run:  python org_frontier/studies/partial_observation_screen/analyze_partial_obs.py
"""

from __future__ import annotations

import csv
import hashlib
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
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_threshold_scaling import threshold_hub
from org_frontier.probes.probe_symmetric_multihub import sym_two_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

T = 2000
NOISE = 0.08
SEED = 24
DUTY = (1.0, 0.75, 0.5, 0.25, 0.1, 0.0)
MIN_PAIR_STEPS = 20


def _stable_seed(*parts, base=SEED):
    """Deterministic seed from string parts (Python's hash() is salted)."""
    h = hashlib.md5("|".join(str(p) for p in parts).encode()).hexdigest()
    return base + (int(h[:8], 16) % 10_000)


def labels_for(n):
    if n == 3:
        return ("W", "S", "C")
    return tuple(["W", "S"] + [f"C{i}" for i in range(1, n - 1)])


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
    """Best of feature / −feature (same spirit as #21/#134 reporting)."""
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
    Tlen, n = traj.shape
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


def build_multifamily():
    forms = []

    def add(family, name, n, rules):
        v = classify_rules(rules, labels=labels_for(n))
        forms.append((
            name, rules, int(v.structure == "triadic"), float(v.max_phi), family, n,
        ))

    for n in (3, 4):
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
    for n in (4,):
        add("two_hub", f"two_hub_n{n}", n, two_hub(n))
    return forms


def simulate(rules, n, rng):
    tpm = add_noise(tpm_from_rules(rules), NOISE)
    return exact_phi.simulate_trajectory(tpm, n, T, rng)


def score_panel(forms, n, regime, rng, hidden_idx=None, duty=None, node_idx=None):
    """Return (scores, labels, phis) for one observation regime."""
    scores, labels, phis = [], [], []
    for row in forms:
        name, rules, tri, phi = row[0], row[1], row[2], row[3]
        traj = simulate(rules, n, rng)
        if regime == "full":
            mask = mask_full(T, n)
        elif regime == "hidden":
            mask = mask_hidden(T, n, hidden_idx)
        elif regime == "intermittent":
            mask = mask_intermittent(T, n, node_idx, duty, rng)
        else:
            raise ValueError(regime)
        scores.append(mean_mi_masked(traj, mask))
        labels.append(tri)
        phis.append(phi)
    return np.asarray(scores, float), np.asarray(labels, int), np.asarray(phis, float)


def main():
    print("AGENDA #24 — PARTIAL OBSERVATION / ESTIMABILITY")
    print("=" * 80)
    print("  cited: #122/#23 FAST_WITHIN_FAMILY; #21 SPECTRAL_PARTIAL; #25 AL_NO_GAIN")
    print("  pointer: ESTIMATION_ARC (topology bottleneck; lane closable pending #24)")
    print(f"  protocol: T={T}, noise={NOISE}; complete-case mean MI under mask")
    print(f"  duty grid: {list(DUTY)}")
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

    print("BUILD PANELS (exact labels)")
    print("-" * 80)
    family = build_family_n3(rng)
    multi = build_multifamily()
    n_tri_f = sum(r[2] for r in family)
    n_tri_m = sum(r[2] for r in multi)
    print(f"  family_n3: {len(family)} forms ({n_tri_f} tri / {len(family) - n_tri_f} dya)")
    print(f"  multifamily: {len(multi)} forms ({n_tri_m} tri / {len(multi) - n_tri_m} dya)")
    print()

    curve_rows = []
    family_rows = []

    # --- family_n3: full / hidden party / hidden mediator / intermittent ---
    print("FAMILY_N3 — full and hidden")
    print("-" * 80)
    # party indices: W=0, S=1, C=2
    regimes_hidden = [
        ("full", None, None),
        ("hidden_party_C", "hidden", 2),
        ("hidden_party_W", "hidden", 0),
        ("hidden_mediator_S", "hidden", 1),
    ]
    family_auc = {}
    for tag, kind, hidx in regimes_hidden:
        t0 = time.time()
        # reseed so trajectory draws are comparable across regimes
        local = np.random.default_rng(_stable_seed("fam", tag))
        if kind is None:
            sc, y, _ = score_panel(family, 3, "full", local)
        else:
            sc, y, _ = score_panel(family, 3, "hidden", local, hidden_idx=hidx)
        auc, orient = oriented_auc(sc, y)
        family_auc[tag] = auc
        print(f"  {tag:22s}  AUC={auc:.3f}  orient={orient:+d}  ({time.time() - t0:.1f}s)")
        curve_rows.append({
            "panel": "family_n3",
            "regime": tag,
            "duty": 1.0 if kind is None else 0.0,
            "hidden_or_node": "" if hidx is None else hidx,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": auc,
            "orient": orient,
        })
        for i, row in enumerate(family):
            family_rows.append({
                "panel": "family_n3",
                "regime": tag,
                "name": row[0],
                "triadic": row[2],
                "max_phi": row[3],
                "mean_mi": sc[i],
            })
    print()

    print("FAMILY_N3 — intermittent party C (duty cycle)")
    print("-" * 80)
    intermittent_auc = []
    for d in DUTY:
        tag = f"intermittent_C_d{d}"
        t0 = time.time()
        local = np.random.default_rng(_stable_seed("intC", d))
        sc, y, _ = score_panel(
            family, 3, "intermittent", local, duty=d, node_idx=2,
        )
        auc, orient = oriented_auc(sc, y)
        intermittent_auc.append((d, auc))
        print(f"  δ={d:.2f}  AUC={auc:.3f}  orient={orient:+d}  ({time.time() - t0:.1f}s)")
        curve_rows.append({
            "panel": "family_n3",
            "regime": "intermittent_party_C",
            "duty": d,
            "hidden_or_node": 2,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": auc,
            "orient": orient,
        })
    print()

    print("FAMILY_N3 — intermittent mediator S (duty cycle)")
    print("-" * 80)
    intermittent_med = []
    for d in DUTY:
        tag = f"intermittent_S_d{d}"
        t0 = time.time()
        local = np.random.default_rng(_stable_seed("intS", d))
        sc, y, _ = score_panel(
            family, 3, "intermittent", local, duty=d, node_idx=1,
        )
        auc, orient = oriented_auc(sc, y)
        intermittent_med.append((d, auc))
        print(f"  δ={d:.2f}  AUC={auc:.3f}  orient={orient:+d}  ({time.time() - t0:.1f}s)")
        curve_rows.append({
            "panel": "family_n3",
            "regime": "intermittent_mediator_S",
            "duty": d,
            "hidden_or_node": 1,
            "n_forms": len(y),
            "n_tri": int(y.sum()),
            "mi_auc": auc,
            "orient": orient,
        })
    print()

    # --- multifamily: full vs hidden party (last party index) ---
    print("MULTIFAMILY — full vs hidden party (per family)")
    print("-" * 80)
    # Group by family; score full and hidden last-party
    by_family = {}
    for row in multi:
        fam = row[4]
        by_family.setdefault(fam, []).append(row)

    family_delta = {}
    # Score each form at its own n, then pool within family (and pooled overall).
    sc_full_all, y_full_all = [], []
    sc_hid_all, y_hid_all = [], []
    for fam, forms in sorted(by_family.items()):
        sc_full, y_full = [], []
        sc_hid, y_hid = [], []
        for row in forms:
            name, rules, tri, phi, _, n_size = row
            slim = [(name, rules, tri, phi)]
            local_f = np.random.default_rng(_stable_seed("mf", fam, name, "f"))
            local_h = np.random.default_rng(_stable_seed("mf", fam, name, "h"))
            sc, y, _ = score_panel(slim, n_size, "full", local_f)
            sc_full.extend(sc.tolist())
            y_full.extend(y.tolist())
            sc2, y2, _ = score_panel(
                slim, n_size, "hidden", local_h, hidden_idx=n_size - 1,
            )
            sc_hid.extend(sc2.tolist())
            y_hid.extend(y2.tolist())
        sc_full_all.extend(sc_full)
        y_full_all.extend(y_full)
        sc_hid_all.extend(sc_hid)
        y_hid_all.extend(y_hid)
        auc_f, o_f = oriented_auc(sc_full, y_full)
        auc_h, o_h = oriented_auc(sc_hid, y_hid)
        delta = (
            float("nan") if (np.isnan(auc_f) or np.isnan(auc_h))
            else float(auc_f - auc_h)
        )
        family_delta[fam] = (auc_f, auc_h, delta)
        d_s = f"{delta:.3f}" if not np.isnan(delta) else "nan"
        print(f"  {fam:12s}  full={auc_f:.3f}  hid_party={auc_h:.3f}  "
              f"Δ={d_s}  n={len(y_full)}")
        curve_rows.append({
            "panel": f"multifamily_{fam}",
            "regime": "full",
            "duty": 1.0,
            "hidden_or_node": "",
            "n_forms": len(y_full),
            "n_tri": int(sum(y_full)),
            "mi_auc": auc_f,
            "orient": o_f,
        })
        curve_rows.append({
            "panel": f"multifamily_{fam}",
            "regime": "hidden_party",
            "duty": 0.0,
            "hidden_or_node": "last",
            "n_forms": len(y_hid),
            "n_tri": int(sum(y_hid)),
            "mi_auc": auc_h,
            "orient": o_h,
        })
    auc_mf_f, _ = oriented_auc(sc_full_all, y_full_all)
    auc_mf_h, _ = oriented_auc(sc_hid_all, y_hid_all)
    print(f"  {'POOLED':12s}  full={auc_mf_f:.3f}  hid_party={auc_mf_h:.3f}  "
          f"n={len(y_full_all)}")
    curve_rows.append({
        "panel": "multifamily_pooled",
        "regime": "full",
        "duty": 1.0,
        "hidden_or_node": "",
        "n_forms": len(y_full_all),
        "n_tri": int(sum(y_full_all)),
        "mi_auc": auc_mf_f,
        "orient": 0,
    })
    curve_rows.append({
        "panel": "multifamily_pooled",
        "regime": "hidden_party",
        "duty": 0.0,
        "hidden_or_node": "last",
        "n_forms": len(y_hid_all),
        "n_tri": int(sum(y_hid_all)),
        "mi_auc": auc_mf_h,
        "orient": 0,
    })
    print()

    # --- Hypothesis tests ---
    auc_full = family_auc["full"]
    auc_hid_c = family_auc["hidden_party_C"]
    auc_hid_w = family_auc["hidden_party_W"]
    auc_hid_s = family_auc["hidden_mediator_S"]
    # primary hidden-party: hide C (counterpart); also report W
    auc_hid_party = min(auc_hid_c, auc_hid_w)  # worst-case party hide for H1 sharpness
    # H1 uses hide-C as the pre-registered "one party" (counterpart)
    drop_c = auc_full - auc_hid_c
    h1 = (
        ctrl
        and (not np.isnan(auc_full)) and auc_full >= 0.90
        and (not np.isnan(auc_hid_c))
        and (drop_c >= 0.20 or auc_hid_c < 0.70)
    )

    # H2: monotone non-decreasing in δ (0.05 slack); max consec drop ≤ 0.25
    duties_sorted = sorted(intermittent_auc, key=lambda z: z[0])
    mono_ok = True
    max_consec_drop = 0.0
    for (d0, a0), (d1, a1) in zip(duties_sorted, duties_sorted[1:]):
        if np.isnan(a0) or np.isnan(a1):
            mono_ok = False
        elif a1 + 0.05 < a0:
            mono_ok = False
    for (d0, a0), (d1, a1) in zip(duties_sorted[::-1], duties_sorted[::-1][1:]):
        # d0 > d1; drop when AUC falls as missingness rises
        if np.isnan(a0) or np.isnan(a1):
            continue
        drop = a0 - a1
        if drop > max_consec_drop:
            max_consec_drop = drop
    h2 = ctrl and mono_ok and max_consec_drop <= 0.25

    # H3: family ΔAUC spread ≥ 0.15 OR |mediator vs party| ≥ 0.10
    deltas = [v[2] for v in family_delta.values() if not np.isnan(v[2])]
    spread = (max(deltas) - min(deltas)) if len(deltas) >= 2 else float("nan")
    med_vs_party = abs(auc_hid_s - auc_hid_c)
    h3 = ctrl and (
        (not np.isnan(spread) and spread >= 0.15)
        or (not np.isnan(med_vs_party) and med_vs_party >= 0.10)
    )

    # Verdict word
    if h1 and h2:
        verdict_word = "HIDDEN_SHARP_INTERMITTENT_SMOOTH"
        reading = (
            f"HIDDEN_SHARP_INTERMITTENT_SMOOTH — family_n3 full AUC={auc_full:.3f}; "
            f"hidden party C AUC={auc_hid_c:.3f} (Δ={drop_c:.3f}); "
            f"intermittent max consec drop={max_consec_drop:.3f}; "
            f"mediator-vs-party |Δ|={med_vs_party:.3f}; family ΔAUC spread={spread:.3f}"
        )
    elif h1 and not h2:
        verdict_word = "HIDDEN_COLLAPSE_INTERMITTENT_CLIFF"
        reading = (
            f"HIDDEN_COLLAPSE_INTERMITTENT_CLIFF — hidden party collapses "
            f"(full={auc_full:.3f}→{auc_hid_c:.3f}); intermittent not smooth "
            f"(max consec drop={max_consec_drop:.3f}, mono={mono_ok})"
        )
    elif (not h1) and h2:
        verdict_word = "PARTIAL_OBS_ROBUST"
        reading = (
            f"PARTIAL_OBS_ROBUST — hidden party does not sharply collapse "
            f"(full={auc_full:.3f}, hid_C={auc_hid_c:.3f}); intermittent smooth"
        )
    else:
        verdict_word = "PARTIAL_OBS_MIXED"
        reading = (
            f"PARTIAL_OBS_MIXED — H1/H2 pattern; full={auc_full:.3f} "
            f"hid_C={auc_hid_c:.3f} max_drop={max_consec_drop:.3f}"
        )
    if h3:
        reading += "; family/role mediates degradation"
    else:
        reading += "; family/role does not clearly mediate"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  full AUC={auc_full:.3f}  hid_C={auc_hid_c:.3f}  hid_W={auc_hid_w:.3f}  "
          f"hid_S={auc_hid_s:.3f}")
    print(f"  drop_C={drop_c:.3f}  med_vs_party={med_vs_party:.3f}  "
          f"family_Δ_spread={spread:.3f}")
    print(f"  intermittent_C AUCs: "
          + ", ".join(f"δ={d:.2f}:{a:.3f}" for d, a in duties_sorted))
    print(f"  mono_ok={mono_ok}  max_consec_drop={max_consec_drop:.3f}")
    print(f"  H1 (hidden party collapses):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (intermittent smooth in δ):   "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (topology/family mediates):   "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  full_auc={auc_full:.3f}  hidden_party_auc={auc_hid_c:.3f}  "
          f"hidden_mediator_auc={auc_hid_s:.3f}")
    print(f"  max_consec_drop={max_consec_drop:.3f}  family_delta_spread={spread:.3f}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = [
            "panel", "regime", "duty", "hidden_or_node",
            "n_forms", "n_tri", "mi_auc", "orient",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in curve_rows:
            w.writerow({
                "panel": r["panel"],
                "regime": r["regime"],
                "duty": r["duty"],
                "hidden_or_node": r["hidden_or_node"],
                "n_forms": r["n_forms"],
                "n_tri": r["n_tri"],
                "mi_auc": (
                    f"{r['mi_auc']:.6f}" if not np.isnan(r["mi_auc"]) else ""
                ),
                "orient": r["orient"],
            })

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "full_auc": f"{auc_full:.6f}",
            "hidden_party_auc": f"{auc_hid_c:.6f}",
            "hidden_mediator_auc": f"{auc_hid_s:.6f}",
            "max_consec_drop": f"{max_consec_drop:.6f}",
            "family_delta_spread": (
                f"{spread:.6f}" if not np.isnan(spread) else ""
            ),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)

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
        for name, _, tri, phi, fam, n in multi:
            w.writerow({
                "panel": "multifamily", "family": fam, "n": n,
                "name": name, "triadic": tri, "max_phi": f"{phi:.6f}",
            })


if __name__ == "__main__":
    main()
