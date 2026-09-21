"""Local-triad necklace composition (RESEARCH_AGENDA_V3 #4).

Closed AND necklace vs OR/directed variants, with ring/hub/shared-S controls.
Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/local_triad_necklace/analyze_necklace.py
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
from org_frontier.probes.probe_multihub_law import sym_multihub
from org_frontier.probes.probe_scaling_zoo import ring

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

# Landmark atoms at n=6 from the V2 #18/#19 family (panel-local, not exhaustive).
LANDMARKS_N6 = {2.0, 4.0, 5.0, 6.0, 8.0, 9.0, 12.0}


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


def shared_s_and():
    # (W1, C1, W2, C2, S) — two-triad shared mediator AND (V2 #16 reference)
    labels = ("W1", "C1", "W2", "C2", "S")
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: (x[0] & x[1]) & (x[2] & x[3]),
    ]
    return labels, rules


def necklace(hub_op: str, party_op: str, directed: bool = False):
    """n=6: P0,P1,P2,H0,H1,H2.

    H_i <- (P_i, P_{i+1}); P_i <- (H_{i-1}, H_i) unless directed (P_i <- H_i).
    """
    labels = ("P0", "P1", "P2", "H0", "H1", "H2")
    hop = _and_of if hub_op == "AND" else _or_of
    pop = _and_of if party_op == "AND" else _or_of
    if directed:
        party_rules = [
            (lambda x: x[3]),
            (lambda x: x[4]),
            (lambda x: x[5]),
        ]
    else:
        party_rules = [
            pop((5, 3)),  # P0 <- H2, H0
            pop((3, 4)),  # P1 <- H0, H1
            pop((4, 5)),  # P2 <- H1, H2
        ]
    hub_rules = [
        hop((0, 1)),  # H0 <- P0, P1
        hop((1, 2)),  # H1 <- P1, P2
        hop((2, 0)),  # H2 <- P2, P0
    ]
    return labels, list(party_rules) + list(hub_rules)


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
        f"{row['name']:22s} {row['structure']:8s} "
        f"wholeΦ={row['whole_phi_mip']:.3f}  "
        f"core=({row['core']})  coreΦ={row['core_phi']:.3f}  "
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


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    lab, rules = triad_control()
    rows.append(run_cell("triad", lab, rules, {"family": "control"}))

    lab6 = tuple(f"x{i}" for i in range(6))
    rows.append(run_cell("ring6", lab6, ring(6), {"family": "landmark"}))
    rows.append(run_cell("hub6", lab6, single_hub(6), {"family": "landmark"}))
    rows.append(run_cell("mh6_m3", lab6, sym_multihub(6, 3), {"family": "contrast"}))

    lab, rules = shared_s_and()
    rows.append(run_cell("shared_S_AND", lab, rules, {"family": "merge_ref"}))

    for name, hop, pop, directed in [
        ("neck_AND", "AND", "AND", False),
        ("neck_OR_hub", "OR", "AND", False),
        ("neck_OR_party", "AND", "OR", False),
        ("neck_directed", "AND", "AND", True),
    ]:
        lab, rules = necklace(hop, pop, directed=directed)
        rows.append(run_cell(name, lab, rules, {"family": "necklace"}))

    path = os.path.join(RESULTS, "panel.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("LOCAL-TRIAD NECKLACE — V3 #4")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}
    triad_ok = by["triad"]["structure"] == "triadic" and near(by["triad"]["core_phi"], 2.0)
    ring_ok = by["ring6"]["full_core"] and near(by["ring6"]["core_phi"], 4.0)
    hub_ok = by["hub6"]["full_core"] and near(by["hub6"]["core_phi"], 5.0)
    shared = by["shared_S_AND"]
    shared_ok = (
        shared["full_core"]
        and shared["structure"] == "triadic"
        and near(shared["core_phi"], 4.0)
    )
    h1 = triad_ok and ring_ok and hub_ok and shared_ok
    print(f"H1 (controls + landmarks + shared-S Φ=4):  {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  triad_ok={triad_ok} ring6_ok={ring_ok} hub6_ok={hub_ok} shared_S_ok={shared_ok}")

    neck = by["neck_AND"]
    landmark_match = neck["structure"] == "triadic" and neck["full_core"] and (
        near(neck["core_phi"], 4.0)
        or near(neck["core_phi"], by["hub6"]["core_phi"])
        or float(neck["core_phi"]) in LANDMARKS_N6
    )
    new_law = (
        neck["structure"] == "triadic"
        and neck["full_core"]
        and float(neck["core_phi"]) not in LANDMARKS_N6
        and not near(neck["core_phi"], 4.0)
        and not near(neck["core_phi"], 5.0)
    )
    h2 = landmark_match and not new_law
    print(f"H2 (AND necklace = landmark, not new law): {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"neck_AND core\u03a6={neck['core_phi']:.3f} full={bool(neck['full_core'])}")
    print(f"  structure={neck['structure']} new_law={new_law}")

    asym = [by[n] for n in ("neck_OR_hub", "neck_OR_party", "neck_directed")]
    h3 = all(collapsed(r) for r in asym)
    print(f"H3 (OR/directed necklaces collapse):       {'SUPPORTED' if h3 else 'REFUTED'}")
    for r in asym:
        print(
            f"  {r['name']}: structure={r['structure']} "
            f"full={bool(r['full_core'])} coreΦ={r['core_phi']:.3f}"
        )

    any_new = new_law
    for r in asym:
        if (
            r["structure"] == "triadic"
            and r["full_core"]
            and float(r["core_phi"]) not in LANDMARKS_N6
            and r["core_phi"] > 2.0 + max(PHI_EPS, 1e-6)
        ):
            any_new = True
    h4 = h2 and h3 and not any_new
    print(f"H4 (no new compose law on panel):          {'SUPPORTED' if h4 else 'REFUTED'}")

    if h2 and h3 and h4:
        token = "COMPOSE_LANDMARK_OR_COLLAPSE"
    elif new_law:
        token = "NEW_COMPOSE_LAW"
    elif h2 and not h3:
        token = "NECKLACE_IS_RING"
    else:
        token = "COMPOSE_MIXED"
    print(f"verdict: {token}")
    if token == "COMPOSE_LANDMARK_OR_COLLAPSE":
        print(
            "reading: COMPOSE_LANDMARK_OR_COLLAPSE — closed AND necklace recovers ring landmark Φ=4; OR/directed variants collapse; no new compose law"
        )
    else:
        print(f"reading: {token}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
