"""Ring-of-hubs with private leaves (RESEARCH_AGENDA_V3 #5).

Hubs on a ring, each serving private leaves — combine ring-cap with hub
growth, or pick landmark / collapse? Exact IIT-4.0. Hypotheses fixed in
hypotheses.md.

Run:  python org_frontier/studies/ring_of_hubs/analyze_ring_of_hubs.py
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

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.probes.probe_scaling_zoo import ring

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

LANDMARKS_N6 = {2.0, 4.0, 5.0, 6.0, 8.0, 9.0, 12.0}
RING_PHI = 4.0
HUB6_PHI = 5.0


def _and_of(srcs):
    srcs = tuple(srcs)

    def f(x, srcs=srcs):
        r = 1
        for s in srcs:
            r &= x[s]
        return r

    return f


def _or_of(srcs):
    srcs = tuple(srcs)

    def f(x, srcs=srcs):
        r = 0
        for s in srcs:
            r |= x[s]
        return r

    return f


def triad_control():
    labels = ("W", "S", "C")
    rules = [
        lambda x: x[1],
        lambda x: x[0] & x[2],
        lambda x: x[1],
    ]
    return labels, rules


def roh_leaf_ring():
    """3 hubs + 3 private leaves: H_i = P_i ∧ H_{i-1} ∧ H_{i+1}; P_i = H_i."""
    labels = ("H0", "H1", "H2", "P0", "P1", "P2")
    rules = [
        _and_of((3, 2, 1)),  # H0 <- P0, H2, H1
        _and_of((4, 0, 2)),  # H1 <- P1, H0, H2
        _and_of((5, 1, 0)),  # H2 <- P2, H1, H0
        (lambda x: x[0]),
        (lambda x: x[1]),
        (lambda x: x[2]),
    ]
    return labels, rules


def roh_hubs_ring():
    """Hubs form AND-ring; leaves hang off (copy hub)."""
    labels = ("H0", "H1", "H2", "P0", "P1", "P2")
    rules = [
        _and_of((2, 1)),
        _and_of((0, 2)),
        _and_of((1, 0)),
        (lambda x: x[0]),
        (lambda x: x[1]),
        (lambda x: x[2]),
    ]
    return labels, rules


def roh_2h2p():
    """2 hubs × 2 private leaves each (cyclic couple)."""
    labels = ("H0", "H1", "L00", "L01", "L10", "L11")
    rules = [
        _and_of((1, 2, 3)),
        _and_of((0, 4, 5)),
        (lambda x: x[0]),
        (lambda x: x[0]),
        (lambda x: x[1]),
        (lambda x: x[1]),
    ]
    return labels, rules


def roh_OR_leaf():
    """Like roh_leaf_ring but hubs OR their inputs."""
    labels = ("H0", "H1", "H2", "P0", "P1", "P2")
    rules = [
        _or_of((3, 2, 1)),
        _or_of((4, 0, 2)),
        _or_of((5, 1, 0)),
        (lambda x: x[0]),
        (lambda x: x[1]),
        (lambda x: x[2]),
    ]
    return labels, rules


def roh_directed():
    """Broken ring: H_i = P_i ∧ H_{i-1} only."""
    labels = ("H0", "H1", "H2", "P0", "P1", "P2")
    rules = [
        _and_of((3, 2)),
        _and_of((4, 0)),
        _and_of((5, 1)),
        (lambda x: x[0]),
        (lambda x: x[1]),
        (lambda x: x[2]),
    ]
    return labels, rules


def run_cell(name, labels, rules, meta):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    n = len(labels)
    full = len(core_t) == n
    return {
        **meta,
        "name": name,
        "n": n,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "core_phi": cp,
        "n_core": len(core_t),
        "full_core": int(full),
        "seconds": round(time.time() - t0, 2),
    }


def fmt(row):
    return (
        f"{row['name']:16s} {row['structure']:8s} "
        f"whole\u03a6={row['whole_phi_mip']:.3f}  "
        f"core=({row['core']})  core\u03a6={row['core_phi']:.3f}  "
        f"full={bool(row['full_core'])}  t={row['seconds']:.1f}s"
    )


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def collapsed(r):
    return r["structure"] == "dyadic" or (
        (not r["full_core"]) and r["core_phi"] <= 2.0 + max(PHI_EPS, 1e-6)
    )


def is_landmark(r):
    return (
        r["structure"] == "triadic"
        and r["full_core"]
        and (
            near(r["core_phi"], RING_PHI)
            or near(r["core_phi"], HUB6_PHI)
            or float(r["core_phi"]) in LANDMARKS_N6
        )
    )


def is_combine(r):
    if r["structure"] != "triadic" or not r["full_core"]:
        return False
    phi = float(r["core_phi"])
    eps = max(PHI_EPS, 1e-6)
    between = (phi > RING_PHI + eps) and (phi < HUB6_PHI - eps)
    above_hub = phi > HUB6_PHI + eps
    return between or above_hub


def is_factor(r):
    """Incomplete core with Φ > 2 — hub subsystem integrates, leaves drop."""
    return (not r["full_core"]) and r["core_phi"] > 2.0 + max(PHI_EPS, 1e-6)


def classify(r):
    if is_combine(r):
        return "COMBINE"
    if is_landmark(r):
        return "LANDMARK"
    if collapsed(r) and not is_factor(r):
        return "COLLAPSE"
    if is_factor(r):
        return "FACTOR"
    if collapsed(r):
        return "COLLAPSE"
    return "OTHER"


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    lab, rules = triad_control()
    rows.append(run_cell("triad", lab, rules, {"family": "control"}))

    lab6 = tuple(f"x{i}" for i in range(6))
    rows.append(run_cell("ring6", lab6, ring(6), {"family": "landmark"}))
    rows.append(run_cell("hub6", lab6, single_hub(6), {"family": "landmark"}))

    for name, builder in [
        ("roh_leaf_ring", roh_leaf_ring),
        ("roh_hubs_ring", roh_hubs_ring),
        ("roh_2h2p", roh_2h2p),
        ("roh_OR_leaf", roh_OR_leaf),
        ("roh_directed", roh_directed),
    ]:
        lab, rules = builder()
        rows.append(run_cell(name, lab, rules, {"family": "ring_of_hubs"}))

    path = os.path.join(RESULTS, "panel.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("RING-OF-HUBS — V3 #5")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}
    triad_ok = by["triad"]["structure"] == "triadic" and near(by["triad"]["core_phi"], 2.0)
    ring_ok = by["ring6"]["full_core"] and near(by["ring6"]["core_phi"], 4.0)
    hub_ok = by["hub6"]["full_core"] and near(by["hub6"]["core_phi"], 5.0)
    h1 = triad_ok and ring_ok and hub_ok
    print(f"H1 (controls + landmarks):                 {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  triad_ok={triad_ok} ring6_ok={ring_ok} hub6_ok={hub_ok}")

    roh_names = [
        "roh_leaf_ring",
        "roh_hubs_ring",
        "roh_2h2p",
        "roh_OR_leaf",
        "roh_directed",
    ]
    roh = [by[n] for n in roh_names]
    any_combine = any(is_combine(r) for r in roh)
    h2 = not any_combine
    print(f"H2 (no combine on roh panel):              {'SUPPORTED' if h2 else 'REFUTED'}")
    for r in roh:
        print(
            f"  {r['name']}: core\u03a6={r['core_phi']:.3f} full={bool(r['full_core'])} "
            f"structure={r['structure']} combine={is_combine(r)}"
        )

    h3 = all(is_landmark(r) or collapsed(r) for r in roh)
    print(f"H3 (each roh cell landmark or collapse):   {'SUPPORTED' if h3 else 'REFUTED'}")
    for r in roh:
        print(f"  {r['name']}: {classify(r)}")

    any_factor = any(is_factor(r) for r in roh)
    covered = all(classify(r) in ("LANDMARK", "COLLAPSE", "FACTOR") for r in roh)
    h4 = h2 and covered
    print(f"H4 (no combine; all cells classified):     {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  any_factor={any_factor} covered={covered}")

    if any_combine:
        token = "COMBINE_RING_HUB"
    elif h2 and covered and any_factor:
        token = "FACTORS_NO_COMBINE"
    elif h2 and h3:
        token = "NO_COMBINE"
    else:
        token = "ROH_MIXED"
    print(f"verdict: {token}")
    if token == "FACTORS_NO_COMBINE":
        print(
            "reading: FACTORS_NO_COMBINE \u2014 ring-of-hubs with private leaves does "
            "not combine ring-cap with hub-growth; cells factor (incomplete hub "
            "cores, often \u03a6=6 on hubs alone) or collapse \u2014 not a hybrid law "
            "(extends V2 #17 PICK_ONE / V3 #4 COMPOSE_LANDMARK_OR_COLLAPSE)"
        )
    elif token == "NO_COMBINE":
        print(
            "reading: NO_COMBINE \u2014 ring-of-hubs with private leaves does not "
            "combine ring-cap with hub-growth; cells pick a landmark or collapse"
        )
    else:
        print(f"reading: {token}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
