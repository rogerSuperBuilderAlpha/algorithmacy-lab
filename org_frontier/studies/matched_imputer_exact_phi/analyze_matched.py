"""Topology-matched imputer under exact Φ (RESEARCH_AGENDA_V4 #5).

Does a topology-matched imputer (hub on hubs, ring on rings) restore
exact-Φ ranking under hide-party where mismatched ring failed in V4
#4 — or is copy-W still uniquely effective?

Exact binary IIT-4.0 via classify_rules. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/matched_imputer_exact_phi/analyze_matched.py
"""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import verdict as vlib
from org_frontier.probes.probe_distributed_mediators import single_hub, two_hub
from org_frontier.probes.probe_topology_map import chain, pool
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_conjunctive_law import or_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_threshold_scaling import threshold_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

_V41_PATH = os.path.join(
    _REPO_ROOT,
    "org_frontier",
    "studies",
    "joint_obs_cliff_exact_phi",
    "analyze_transfer.py",
)
_spec = importlib.util.spec_from_file_location("v41_transfer", _V41_PATH)
_v41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v41)

SEED = 45
HOLD_AUC = 0.85
HOLD_GAP = 0.10
RET_BAR = 0.95
MATCH_GAP = 0.50
EXACT_TOL = 1e-9


def holds(auc, auc_ref):
    if np.isnan(auc) or np.isnan(auc_ref):
        return False
    return auc >= HOLD_AUC or (auc_ref - auc) <= HOLD_GAP


def roles_for(family, n):
    return _v41.roles_for(family, n)


def labels_for(n):
    return tuple(f"N{i}" for i in range(n))


def phi_of(rules, n):
    v = classify_rules(rules, labels=labels_for(n))
    return float(v.max_phi), v.structure


def swap_b(rules, n, a, m, b, mode):
    out = list(rules)
    if mode == "copy_a":
        out[b] = lambda x, a=a: int(x[a])
    elif mode == "hub":
        out[b] = lambda x, m=m: int(x[m])
    elif mode == "ring":
        left, right = (b - 1) % n, (b + 1) % n
        out[b] = lambda x, L=left, R=right: int(x[L] & x[R])
    elif mode == "const0":
        out[b] = lambda x: 0
    else:
        raise ValueError(mode)
    return out


def omit_b(rules, n, b):
    keep = tuple(i for i in range(n) if i != b)

    def make(oi):
        def r(x, oi=oi, keep=keep, n=n):
            full = [0] * n
            for k, ix in enumerate(keep):
                full[ix] = int(x[k])
            return int(rules[oi](full))

        return r

    return [make(oi) for oi in keep], len(keep)


def broken_hub(n):
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n - 1):
        rules[i] = (lambda x, i=i: x[0])
    rules[n - 1] = lambda x: x[n - 1]
    return rules


def broken_ring(n):
    rules = list(ring(n))
    rules[n - 1] = lambda x: x[n - 1]
    return rules


def broadcast(n):
    rules = [None] * n
    rules[0] = lambda x: x[1] if n > 1 else 0
    for i in range(1, n):
        rules[i] = lambda x: x[0]
    return rules


def build_topo_panel():
    forms = []

    def add(topo, family, name, n, rules):
        phi, structure = phi_of(rules, n)
        forms.append({
            "topo": topo,
            "family": family,
            "name": name,
            "n": n,
            "rules": rules,
            "phi_full": phi,
            "triadic": int(structure == "triadic"),
        })

    for n in (3, 4, 5):
        add("hub", "hub", f"and_hub_n{n}", n, single_hub(n))
        add("hub", "or_hub", f"or_hub_n{n}", n, or_hub(n))
        add("hub", "broadcast", f"broadcast_n{n}", n, broadcast(n))
        add("hub", "broken", f"broken_hub_n{n}", n, broken_hub(n))
        add("hub", "parity", f"parity_n{n}", n, parity_hub(n))
        add("ring", "ring", f"ring_n{n}", n, ring(n))
        add("ring", "broken_ring", f"broken_ring_n{n}", n, broken_ring(n))
    for n in (3, 4):
        add("other", "chain", f"chain_n{n}", n, chain(n))
        add("other", "pool", f"pool_n{n}", n, pool(n))
        add("other", "maj", f"maj_n{n}", n, threshold_hub(n, (n - 1) // 2 + 1))
    add("other", "two_hub", "two_hub_n4", 4, two_hub(4))
    return forms


def score_form(form):
    n = form["n"]
    rules = form["rules"]
    a, m, b = roles_for(form["family"], n)
    out = {
        "topo": form["topo"],
        "family": form["family"],
        "name": form["name"],
        "n": n,
        "triadic": form["triadic"],
        "phi_full": form["phi_full"],
    }
    for mode in ("hub", "ring", "copy_a", "const0"):
        phi, _ = phi_of(swap_b(rules, n, a, m, b, mode), n)
        out[f"phi_{mode}"] = phi
        out[f"exact_{mode}"] = int(abs(phi - form["phi_full"]) < EXACT_TOL)
    omit_rules, nn = omit_b(rules, n, b)
    phi_omit, _ = phi_of(omit_rules, nn)
    out["phi_omit"] = phi_omit

    if form["topo"] == "hub":
        out["phi_matched"] = out["phi_hub"]
        out["phi_mismatched"] = out["phi_ring"]
        out["exact_matched"] = out["exact_hub"]
        out["exact_mismatched"] = out["exact_ring"]
    elif form["topo"] == "ring":
        out["phi_matched"] = out["phi_ring"]
        out["phi_mismatched"] = out["phi_hub"]
        out["exact_matched"] = out["exact_ring"]
        out["exact_mismatched"] = out["exact_hub"]
    else:
        out["phi_matched"] = out["phi_copy_a"]
        out["phi_mismatched"] = out["phi_hub"]
        out["exact_matched"] = out["exact_copy_a"]
        out["exact_mismatched"] = out["exact_hub"]
    return out


def panel_auc(rows, key):
    return _v41.oriented_auc(
        [r[key] for r in rows],
        [r["triadic"] for r in rows],
    )


def exact_rate(rows, key):
    if not rows:
        return float("nan")
    return float(np.mean([r[key] for r in rows]))


def main():
    print("AGENDA V4 #5 — TOPOLOGY-MATCHED IMPUTER UNDER EXACT Φ")
    print("=" * 80)
    print("  cited: V4 #4 COPY_RESTORES_RING_FAILS; V3 #15 IMPUTER_RESTORES_AUC")
    print("  pointer: matched hub/ring priors vs copy-A ranking")
    print(
        f"  protocol: restore AUC≥{HOLD_AUC} or within {HOLD_GAP} of full; "
        f"retention exact≥{RET_BAR}; matched gap≥{MATCH_GAP}"
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

    t_all = time.time()

    print("BUILD PANELS")
    print("-" * 80)
    med_raw = _v41.build_family_n3(np.random.default_rng(15))
    mediation = []
    for row in med_raw:
        mediation.append({
            "topo": "mediation",
            "family": "mediation",
            "name": row["name"],
            "n": row["n"],
            "rules": row["rules"],
            "phi_full": float(row["phi_full"]),
            "triadic": int(row["triadic"]),
        })
    topo_panel = build_topo_panel()
    print(
        f"  mediation: {len(mediation)} "
        f"({sum(r['triadic'] for r in mediation)} tri)"
    )
    print(
        f"  topo panel: {len(topo_panel)} "
        f"(hub={sum(1 for r in topo_panel if r['topo']=='hub')}, "
        f"ring={sum(1 for r in topo_panel if r['topo']=='ring')}, "
        f"other={sum(1 for r in topo_panel if r['topo']=='other')})"
    )
    print()

    print("SCORE exact-Φ imputers")
    print("-" * 80)
    t0 = time.time()
    scored = [score_form(r) for r in mediation + topo_panel]
    print(f"  scored {len(scored)} forms ({time.time() - t0:.1f}s)")
    print()

    hub_nat = [r for r in scored if r["topo"] == "hub"]
    ring_nat = [r for r in scored if r["topo"] == "ring"]
    hub_ring = hub_nat + ring_nat
    med = [r for r in scored if r["topo"] == "mediation"]
    hub_tri = [r for r in hub_nat if r["triadic"]]
    ring_tri = [r for r in ring_nat if r["triadic"]]

    print("PANEL AUCs")
    print("-" * 80)
    aucs = {}
    keys = [
        "phi_full", "phi_omit", "phi_hub", "phi_ring", "phi_copy_a",
        "phi_matched", "phi_mismatched", "phi_const0",
    ]
    for pname, rows in [
        ("mediation", med),
        ("hub_native", hub_nat),
        ("ring_native", ring_nat),
        ("hub_ring", hub_ring),
    ]:
        for key in keys:
            auc, orient = panel_auc(rows, key)
            aucs[f"{pname}:{key}"] = (auc, orient)
            print(
                f"  {pname:12s} {key:16s}  AUC={auc:.3f}  orient={orient:+d}"
            )
    print()

    ret_hub = exact_rate(hub_tri, "exact_matched")
    ret_hub_mis = exact_rate(hub_tri, "exact_mismatched")
    ret_ring = exact_rate(ring_tri, "exact_matched")
    ret_ring_mis = exact_rate(ring_tri, "exact_mismatched")

    print("RETENTION (triadic natives)")
    print("-" * 80)
    print(
        f"  hub-native tri n={len(hub_tri)}: matched_exact={ret_hub:.3f}  "
        f"mismatched_exact={ret_hub_mis:.3f}"
    )
    print(
        f"  ring-native tri n={len(ring_tri)}: matched_exact={ret_ring:.3f}  "
        f"mismatched_exact={ret_ring_mis:.3f}"
    )
    print()

    def A(panel, key):
        return aucs[f"{panel}:{key}"][0]

    auc_full_m = A("mediation", "phi_full")
    auc_copy_m = A("mediation", "phi_copy_a")
    auc_hub_m = A("mediation", "phi_hub")
    auc_ring_m = A("mediation", "phi_ring")
    auc_c0_m = A("mediation", "phi_const0")
    auc_full_hr = A("hub_ring", "phi_full")
    auc_matched_hr = A("hub_ring", "phi_matched")
    auc_mis_hr = A("hub_ring", "phi_mismatched")
    auc_copy_hr = A("hub_ring", "phi_copy_a")

    h1 = ctrl and (not np.isnan(ret_hub)) and ret_hub >= RET_BAR
    h2 = ctrl and (not np.isnan(ret_ring)) and ret_ring >= RET_BAR
    h3 = (
        ctrl
        and (ret_hub - ret_hub_mis) >= MATCH_GAP
        and (ret_ring - ret_ring_mis) >= MATCH_GAP
    )
    h4 = ctrl and holds(auc_copy_m, auc_full_m)
    h5 = ctrl and (not holds(auc_matched_hr, auc_full_hr))
    h6 = (
        ctrl
        and holds(auc_full_m, auc_full_m)
        and holds(auc_full_hr, auc_full_hr)
        and (not holds(auc_c0_m, auc_full_m))
    )

    if not h6:
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H6={h6}; full_m={auc_full_m:.3f} "
            f"full_hr={auc_full_hr:.3f} const0_m={auc_c0_m:.3f}"
        )
    elif not (h1 and h2):
        verdict = "MATCHED_FAILS"
        reading = (
            f"MATCHED_FAILS — hub_ret={ret_hub:.3f} ring_ret={ret_ring:.3f} "
            f"(need ≥{RET_BAR}); mismatched hub={ret_hub_mis:.3f} "
            f"ring={ret_ring_mis:.3f}"
        )
    elif not h4:
        verdict = "COPY_FAILS"
        reading = (
            f"COPY_FAILS — copy_a mediation AUC={auc_copy_m:.3f} fails "
            f"restore vs full={auc_full_m:.3f}; matched_hr={auc_matched_hr:.3f}"
        )
    elif h1 and h2 and h3 and h4 and (not h5):
        verdict = "MATCHED_RESTORES_RANK"
        reading = (
            f"MATCHED_RESTORES_RANK — matched retains natives "
            f"(hub={ret_hub:.3f}, ring={ret_ring:.3f}) and restores "
            f"hub∪ring ranking (AUC={auc_matched_hr:.3f}); copy_m="
            f"{auc_copy_m:.3f}"
        )
    elif h1 and h2 and h3 and h4 and h5:
        verdict = "MATCHED_RETAINS_COPY_RANKS"
        reading = (
            f"MATCHED_RETAINS_COPY_RANKS — matched retains native Φ "
            f"(hub exact={ret_hub:.3f}, ring exact={ret_ring:.3f}; "
            f"mismatched {ret_hub_mis:.3f}/{ret_ring_mis:.3f}) but does "
            f"not restore hub∪ring ranking (matched={auc_matched_hr:.3f} "
            f"vs full={auc_full_hr:.3f}, copy={auc_copy_hr:.3f}); "
            f"copy-A restores mediation ({auc_copy_m:.3f})"
        )
    else:
        verdict = "MATCHED_PARTIAL"
        reading = (
            f"MATCHED_PARTIAL — H1={h1} H2={h2} H3={h3} H4={h4} H5={h5}; "
            f"hub_ret={ret_hub:.3f} ring_ret={ret_ring:.3f} "
            f"matched_hr={auc_matched_hr:.3f} copy_m={auc_copy_m:.3f}"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  mediation: full={auc_full_m:.3f}  copy={auc_copy_m:.3f}  "
        f"hub={auc_hub_m:.3f}  ring={auc_ring_m:.3f}  const0={auc_c0_m:.3f}"
    )
    print(
        f"  hub∪ring:  full={auc_full_hr:.3f}  matched={auc_matched_hr:.3f}  "
        f"mismatched={auc_mis_hr:.3f}  copy={auc_copy_hr:.3f}"
    )
    print(
        f"  H1 (hub-matched retains hub triadics):    "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (ring-matched retains ring triadics):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (matched beats mismatched retention):  "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (copy-A restores mediation ranking):   "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (matched fails hub∪ring ranking):      "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print(
        f"  H6 (full holds; const0 fails mediation):  "
        f"{'SUPPORTED' if h6 else 'REFUTED'}"
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
        f"H5={('SUPPORTED' if h5 else 'REFUTED')}  "
        f"H6={('SUPPORTED' if h6 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(
        f"  metrics: full_m={auc_full_m:.3f}; copy_m={auc_copy_m:.3f}; "
        f"hub_m={auc_hub_m:.3f}; ring_m={auc_ring_m:.3f}; "
        f"full_hr={auc_full_hr:.3f}; matched_hr={auc_matched_hr:.3f}; "
        f"mismatched_hr={auc_mis_hr:.3f}; copy_hr={auc_copy_hr:.3f}; "
        f"ret_hub={ret_hub:.3f}; ret_hub_mis={ret_hub_mis:.3f}; "
        f"ret_ring={ret_ring:.3f}; ret_ring_mis={ret_ring_mis:.3f}; "
        f"n_hub_tri={len(hub_tri)}; n_ring_tri={len(ring_tri)}"
    )
    print("  best next:         V4 #6 W+n landmark under fielded instrument")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["panel", "screen", "n_forms", "n_tri", "auc", "orient"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for pname, rows in [
            ("mediation", med),
            ("hub_native", hub_nat),
            ("ring_native", ring_nat),
            ("hub_ring", hub_ring),
        ]:
            n_tri = sum(r["triadic"] for r in rows)
            for key in keys:
                auc, orient = aucs[f"{pname}:{key}"]
                w.writerow({
                    "panel": pname,
                    "screen": key,
                    "n_forms": len(rows),
                    "n_tri": n_tri,
                    "auc": f"{auc:.6f}" if not np.isnan(auc) else "",
                    "orient": orient,
                })

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = [
            "topo", "family", "name", "n", "triadic",
            "phi_full", "phi_omit", "phi_hub", "phi_ring", "phi_copy_a",
            "phi_matched", "phi_mismatched", "phi_const0",
            "exact_matched", "exact_mismatched",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in scored:
            w.writerow({
                "topo": r["topo"],
                "family": r["family"],
                "name": r["name"],
                "n": r["n"],
                "triadic": r["triadic"],
                "phi_full": f"{r['phi_full']:.6f}",
                "phi_omit": f"{r['phi_omit']:.6f}",
                "phi_hub": f"{r['phi_hub']:.6f}",
                "phi_ring": f"{r['phi_ring']:.6f}",
                "phi_copy_a": f"{r['phi_copy_a']:.6f}",
                "phi_matched": f"{r['phi_matched']:.6f}",
                "phi_mismatched": f"{r['phi_mismatched']:.6f}",
                "phi_const0": f"{r['phi_const0']:.6f}",
                "exact_matched": r["exact_matched"],
                "exact_mismatched": r["exact_mismatched"],
            })

    summary = {
        "verdict": verdict,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "h6": "SUPPORTED" if h6 else "REFUTED",
        "ret_hub": round(float(ret_hub), 6),
        "ret_hub_mis": round(float(ret_hub_mis), 6),
        "ret_ring": round(float(ret_ring), 6),
        "ret_ring_mis": round(float(ret_ring_mis), 6),
        "auc_copy_mediation": round(float(auc_copy_m), 6),
        "auc_matched_hub_ring": round(float(auc_matched_hr), 6),
        "auc_mismatched_hub_ring": round(float(auc_mis_hr), 6),
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
