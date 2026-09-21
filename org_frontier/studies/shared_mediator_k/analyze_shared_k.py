"""Shared-mediator k-lift (RESEARCH_AGENDA_V3 #6).

k local conjunctive triads sharing one mediator — does merge Φ scale as
k, as 2k, or saturate? Does OR still refuse? Exact IIT-4.0. Hypotheses
fixed in hypotheses.md.

Run:  python org_frontier/studies/shared_mediator_k/analyze_shared_k.py
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

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def triad_control():
    labels = ("W", "S", "C")
    rules = [
        lambda x: x[1],
        lambda x: x[0] & x[2],
        lambda x: x[1],
    ]
    return labels, rules


def shared_mediator_k(k: int, bridge: str):
    """k triads sharing S. n=2k+1. Labels W1,C1,...,Wk,Ck,S."""
    labels = []
    for i in range(1, k + 1):
        labels.append(f"W{i}")
        labels.append(f"C{i}")
    labels.append("S")
    labels = tuple(labels)
    s_idx = 2 * k
    owns = [(2 * i, 2 * i + 1) for i in range(k)]

    rules = []
    for _ in range(k):
        rules.append(lambda x, s=s_idx: x[s])  # Wi' = S
        rules.append(lambda x, s=s_idx: x[s])  # Ci' = S

    if bridge == "AND":

        def s_rule(x, owns=owns):
            r = 1
            for wi, ci in owns:
                r &= x[wi] & x[ci]
            return r

    elif bridge == "OR":

        def s_rule(x, owns=owns):
            r = 0
            for wi, ci in owns:
                r |= x[wi] & x[ci]
            return r

    else:
        raise KeyError(bridge)

    rules.append(s_rule)
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
        f"{row['name']:14s} {row['structure']:8s} "
        f"whole\u03a6={row['whole_phi_mip']:.3f}  "
        f"core=({row['core']})  core\u03a6={row['core_phi']:.3f}  "
        f"full={bool(row['full_core'])}  t={row['seconds']:.1f}s"
    )


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    lab, rules = triad_control()
    rows.append(run_cell("triad", lab, rules, {"family": "control", "k": 1, "bridge": "n/a"}))

    for k in (2, 3):
        for bridge in ("AND", "OR"):
            lab, rules = shared_mediator_k(k, bridge)
            rows.append(
                run_cell(
                    f"k{k}_{bridge}",
                    lab,
                    rules,
                    {"family": "shared_S", "k": k, "bridge": bridge},
                )
            )

    path = os.path.join(RESULTS, "panel.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("SHARED-MEDIATOR k-LIFT — V3 #6")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}

    # H1
    triad_ok = by["triad"]["structure"] == "triadic" and near(by["triad"]["core_phi"], 2.0)
    k2_and = by["k2_AND"]
    k2_and_ok = (
        k2_and["structure"] == "triadic"
        and k2_and["full_core"]
        and near(k2_and["core_phi"], 4.0)
    )
    k2_or = by["k2_OR"]
    k2_or_refuse = not (k2_or["full_core"] and k2_or["structure"] == "triadic" and k2_or["n_core"] == 5)
    # refuse = not full five-node merge
    k2_or_refuse = not (k2_or["full_core"] and near(k2_or["core_phi"], 4.0))
    h1 = triad_ok and k2_and_ok and k2_or_refuse
    print(f"H1 (triad + k=2 AND merge \u03a6=4 + k=2 OR refuse): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(
        f"  triad_ok={triad_ok} k2_AND_ok={k2_and_ok} k2_OR_refuse={k2_or_refuse} "
        f"(k2_OR full={bool(k2_or['full_core'])} core\u03a6={k2_or['core_phi']:.3f})"
    )

    # H2
    k3_or = by["k3_OR"]
    k3_or_refuse = not (
        k3_or["full_core"] and k3_or["structure"] == "triadic" and k3_or["n_core"] == 7
    )
    h2 = k3_or_refuse
    print(f"H2 (k=3 OR refuses full merge):              {'SUPPORTED' if h2 else 'REFUTED'}")
    print(
        f"  k3_OR full={bool(k3_or['full_core'])} structure={k3_or['structure']} "
        f"core\u03a6={k3_or['core_phi']:.3f} n_core={k3_or['n_core']}"
    )

    # H3 scaling
    phis = {
        1: by["triad"]["core_phi"],
        2: by["k2_AND"]["core_phi"] if k2_and_ok else float("nan"),
        3: by["k3_AND"]["core_phi"]
        if by["k3_AND"]["full_core"] and by["k3_AND"]["structure"] == "triadic"
        else float("nan"),
    }
    k3_and_merge = by["k3_AND"]["full_core"] and by["k3_AND"]["structure"] == "triadic"
    scale_2k = (
        k3_and_merge
        and near(phis[1], 2.0)
        and near(phis[2], 4.0)
        and near(phis[3], 6.0)
    )
    scale_k = (
        k3_and_merge
        and near(phis[1], 1.0)
        and near(phis[2], 2.0)
        and near(phis[3], 3.0)
    )
    saturate = (
        k3_and_merge
        and near(phis[2], 4.0)
        and near(phis[3], 4.0)
        and near(phis[1], 2.0)
    )
    if scale_2k:
        scale = "scale_2k"
    elif scale_k:
        scale = "scale_k"
    elif saturate:
        scale = "saturate"
    else:
        scale = "OTHER_SCALE"
    h3 = scale in ("scale_2k", "scale_k", "saturate")
    print(f"H3 (AND merge \u03a6 scaling named):             {'SUPPORTED' if h3 else 'REFUTED'}")
    print(
        f"  \u03a6(k=1,2,3 AND)={phis[1]:.3f},{phis[2]:.3f},{phis[3]:.3f}  "
        f"k3_and_merge={k3_and_merge}  scale={scale}"
    )

    h4 = h1 and h2 and h3
    print(f"H4 (panel closed):                           {'SUPPORTED' if h4 else 'REFUTED'}")

    if scale == "scale_2k" and h2:
        token = "SCALE_2K_OR_REFUSES"
    elif scale == "scale_k" and h2:
        token = "SCALE_K_OR_REFUSES"
    elif scale == "saturate" and h2:
        token = "SATURATE_OR_REFUSES"
    elif h2:
        token = "OTHER_SCALE_OR_REFUSES"
    else:
        token = "OR_MERGES_OR_MIXED"
    print(f"verdict: {token}")
    if token == "SCALE_2K_OR_REFUSES":
        print(
            "reading: SCALE_2K_OR_REFUSES \u2014 shared-mediator AND merge \u03a6 = 2k "
            "for k=1,2,3 (2,4,6); OR refuses full merge at k=2 and k=3 "
            "(lift of V2 #16 WIN)"
        )
    else:
        print(f"reading: {token}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
