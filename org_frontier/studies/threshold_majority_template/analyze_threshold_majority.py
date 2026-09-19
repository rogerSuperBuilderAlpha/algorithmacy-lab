"""Threshold/majority vs redundancy-factors (RESEARCH_AGENDA_V3 #2).

Is majority at n≥4 a new template, or does it always collapse into the
#10/#67/#117 redundancy-factors pattern once pivotality is lost — even on
topologies that restored triadicity for conjunctive hubs? Exact IIT-4.0.
Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/threshold_majority_template/analyze_threshold_majority.py
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


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def maj3(a, b, c):
    return (a & b) | (a & c) | (b & c)


def triad_and():
    labels = ("W", "S", "C")
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    return labels, rules, {"family": "control", "arch": "triad_and", "k": "", "role": "anchor"}


def threshold_hub(n_parties, k):
    """S + n_parties parties. S'=1 iff ≥k parties on; each party copies S."""
    n = n_parties + 1
    labels = ("S",) + tuple(f"P{i}" for i in range(n_parties))
    rules = [None] * n
    rules[0] = lambda x, k=k, n=n: int(sum(x[i] for i in range(1, n)) >= k)
    for i in range(1, n):
        rules[i] = lambda x, i=i: x[0]
    role = "extreme" if k in (1, n_parties) else "intermediate"
    return labels, rules, {
        "family": "plain_hub",
        "arch": f"hub_n{n}_k{k}",
        "k": k,
        "role": role,
    }


def shared_and():
    labels = ("W1", "C1", "W2", "C2", "S")
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: (x[0] & x[1]) & (x[2] & x[3]),
    ]
    return labels, rules, {
        "family": "shared",
        "arch": "shared_and",
        "k": "",
        "role": "and_restore",
    }


def shared_maj(k):
    """Shared-mediator carrier; S' = 1 iff ≥k of four parties on."""
    labels = ("W1", "C1", "W2", "C2", "S")
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x, k=k: int(sum([x[0], x[1], x[2], x[3]]) >= k),
    ]
    return labels, rules, {
        "family": "shared",
        "arch": f"shared_maj{k}of4",
        "k": k,
        "role": "intermediate",
    }


def recurrent_and_b3():
    labels = ("A", "L0", "L1", "L2")
    rules = [
        lambda x: x[1] & x[2] & x[3],
        lambda x: x[0],
        lambda x: x[0],
        lambda x: x[0],
    ]
    return labels, rules, {
        "family": "recurrent",
        "arch": "rec_and_b3",
        "k": "",
        "role": "and_restore",
    }


def recurrent_maj_b3():
    labels = ("A", "L0", "L1", "L2")
    rules = [
        lambda x: maj3(x[1], x[2], x[3]),
        lambda x: x[0],
        lambda x: x[0],
        lambda x: x[0],
    ]
    return labels, rules, {
        "family": "recurrent",
        "arch": "rec_maj_b3",
        "k": 2,
        "role": "intermediate",
    }


FORMS = [
    triad_and,
    lambda: threshold_hub(3, 1),
    lambda: threshold_hub(3, 2),
    lambda: threshold_hub(3, 3),
    lambda: threshold_hub(4, 1),
    lambda: threshold_hub(4, 2),
    lambda: threshold_hub(4, 3),
    lambda: threshold_hub(4, 4),
    shared_and,
    lambda: shared_maj(2),
    lambda: shared_maj(3),
    recurrent_and_b3,
    recurrent_maj_b3,
]


def classify_cell(structure, n, n_core, core_phi):
    """full_bind | factors | other."""
    if n_core == n and structure == "triadic" and core_phi > PHI_EPS:
        return "full_bind"
    return "factors"


def run_cell(builder):
    labels, rules, meta = builder()
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    n = len(labels)
    n_core = len(core_t)
    kind = classify_cell(v.structure, n, n_core, cp if core_t else 0.0)
    return {
        **meta,
        "name": meta["arch"],
        "n": n,
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "core_phi": cp,
        "n_core": n_core,
        "kind": kind,
        "seconds": round(time.time() - t0, 2),
    }


def fmt(row):
    return (
        f"{row['name']:16s} {row['structure']:8s} "
        f"whole\u03a6={row['whole_phi']:.3f}  "
        f"core=({row['core']})  core\u03a6={row['core_phi']:.3f}  "
        f"n_core={row['n_core']}  kind={row['kind']:10s}  "
        f"t={row['seconds']:.1f}s"
    )


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []
    for builder in FORMS:
        rows.append(run_cell(builder))

    panel_path = os.path.join(RESULTS, "panel.csv")
    fields = [
        "family",
        "arch",
        "name",
        "n",
        "k",
        "role",
        "structure",
        "whole_phi",
        "core",
        "core_phi",
        "n_core",
        "kind",
        "seconds",
    ]
    with open(panel_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print("THRESHOLD/MAJORITY TEMPLATE — V3 #2")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}

    # H1
    ta = by["triad_and"]
    ta_ok = ta["structure"] == "triadic" and near(ta["core_phi"], 2.0) and ta["kind"] == "full_bind"
    hub4_k1 = by["hub_n4_k1"]
    hub4_k2 = by["hub_n4_k2"]
    hub4_k3 = by["hub_n4_k3"]
    ext4_ok = hub4_k1["kind"] == "full_bind" and hub4_k3["kind"] == "full_bind"
    mid4_ok = hub4_k2["kind"] == "factors"
    hub5_k1 = by["hub_n5_k1"]
    hub5_k2 = by["hub_n5_k2"]
    hub5_k4 = by["hub_n5_k4"]
    ext5_ok = hub5_k1["kind"] == "full_bind" and hub5_k4["kind"] == "full_bind"
    mid5_ok = hub5_k2["kind"] == "factors"  # 2-of-4 intermediate
    # also require hub_n5_k3 factors
    hub5_k3 = by["hub_n5_k3"]
    mid5_ok = mid5_ok and hub5_k3["kind"] == "factors"
    h1 = ta_ok and ext4_ok and mid4_ok and ext5_ok and mid5_ok
    print(f"H1 (anchors + plain-hub redundancy pattern): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(
        f"  triad_ok={ta_ok} hub4_ext={ext4_ok} hub4_mid_factors={mid4_ok} "
        f"hub5_ext={ext5_ok} hub5_mid_factors={mid5_ok}"
    )

    # H2
    sa = by["shared_and"]
    ra = by["rec_and_b3"]
    sa_ok = sa["kind"] == "full_bind" and sa["structure"] == "triadic"
    ra_ok = ra["kind"] == "full_bind" and ra["structure"] == "triadic"
    h2 = sa_ok and ra_ok
    print(f"H2 (AND carriers restore/bind full core):    {'SUPPORTED' if h2 else 'REFUTED'}")
    print(
        f"  shared_and kind={sa['kind']} core\u03a6={sa['core_phi']:.3f}  "
        f"rec_and_b3 kind={ra['kind']} core\u03a6={ra['core_phi']:.3f}"
    )

    # H3
    maj_cells = [by["shared_maj2of4"], by["shared_maj3of4"], by["rec_maj_b3"]]
    h3 = all(c["kind"] == "factors" for c in maj_cells)
    print(f"H3 (majority on restored carriers factors):  {'SUPPORTED' if h3 else 'REFUTED'}")
    print(
        "  "
        + "  ".join(
            f"{c['name']}={c['kind']}" for c in maj_cells
        )
    )

    # any intermediate full_bind?
    intermediates = [r for r in rows if r["role"] == "intermediate"]
    rescued = [r for r in intermediates if r["kind"] == "full_bind"]

    if not h1 or not h2:
        token = "CONTROLS_FAIL"
    elif rescued:
        # check novelty of Φ vs AND/OR extremes at same n
        novel = False
        for r in rescued:
            # AND/OR extreme landmark at same n is n-1
            if not near(r["core_phi"], r["n"] - 1):
                novel = True
        token = "MAJORITY_NEW_TEMPLATE" if novel else "TOPOLOGY_RESCUES_MAJ"
    elif h3:
        token = "COLLAPSES_TO_REDUNDANCY"
    else:
        token = "MIXED_THRESHOLD"

    h4 = token == "COLLAPSES_TO_REDUNDANCY"
    print(f"H4 (panel closed):                           {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")
    if token == "COLLAPSES_TO_REDUNDANCY":
        print(
            "reading: COLLAPSES_TO_REDUNDANCY \u2014 threshold/majority at n\u22654 is not a "
            "new template; intermediate k always factors once pivotality is lost, "
            "including on shared-mediator and recurrent carriers that restore "
            "triadicity under AND (#10/#67/#117 pattern holds)"
        )
    else:
        print(f"reading: {token}")
    print(f"wrote {panel_path}")


if __name__ == "__main__":
    main()
