"""Fixed update order on three-party quorum hubs: the four members act one after another.

Run from the repo root: python org_frontier/studies/update_order_quorum/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import itertools
import json
import os
import sys
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np  # noqa: E402
import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, tpm_from_rules  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, rules_for, table_of,
)
from org_frontier.studies.timescale_separation.analyze_timescale import sequential_tpm  # noqa: E402

pyphi.config.PROGRESS_BARS = False
N = 3
FORMS = (("OR3", 1), ("MAJ3", 2), ("AND3", 3))
ORDERS = tuple(itertools.permutations(range(N + 1)))
QUICK = (("OR3", 1, (0, 1, 2, 3)), ("OR3", 1, (1, 2, 3, 0)), ("OR3", 1, (1, 0, 2, 3)))
KNOWN = {"OR3": 3.0, "MAJ3": 0.0, "AND3": 3.0}


def order_tpm(rules, order):
    tpm = np.zeros((2 ** (N + 1), N + 1))
    for s in range(2 ** (N + 1)):
        x = [(s >> i) & 1 for i in range(N + 1)]
        for j in order:
            x[j] = int(rules[j](tuple(x)))
        tpm[s] = x
    return tpm


def phi_read(tpm, labels):
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(N + 1))
    states = []
    for index in reachable_states(tpm, N + 1):
        state = tuple((index >> i) & 1 for i in range(N + 1))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        top = max(phis.values()) if phis else 0.0
        ties = sorted((k for k, v in phis.items() if top > PHI_EPS and top - v <= PHI_EPS),
                      key=lambda k: (len(k), k))
        states.append(dict(state=list(state), top=top, full_phi=phis.get(full, 0.0),
                           ties=["".join(labels[i] for i in k) for k in ties], full_in=full in ties))
    best = max(states, key=lambda s: s["top"])
    return dict(n_states=len(states), whole_phi=max(s["full_phi"] for s in states), top=best["top"],
                top_ties=best["ties"], full_in_top=best["full_in"], states=states)


def read(name, quota, order):
    labels = labels_for(N)
    rules = rules_for(table_of((1, 1, 1), quota), N)
    tpm = order_tpm(rules, order)
    assert set(np.unique(tpm)) <= {0.0, 1.0}
    ref, _ = sequential_tpm(rules, order, N + 1)
    assert np.allclose(tpm, ref, atol=1e-12, rtol=0)
    out = dict(form=name, order="".join(labels[i] for i in order).replace("P", "")
               .replace("S", "S"), order_labels=[labels[i] for i in order],
               s_last=order[-1] == 0, s_first=order[0] == 0, **phi_read(tpm, labels))
    return out


def show(x):
    ties = ",".join(x["top_ties"]) if len(x["top_ties"]) <= 6 else f"{len(x['top_ties'])} subsets"
    print(f"{x['form']:<5} order={'-'.join(x['order_labels']):<12} states={x['n_states']:<2} "
          f"whole={x['whole_phi']:.6f} top={x['top']:.6f} full_in_top={'Y' if x['full_in_top'] else 'N'} "
          f"ties={ties or '-'}", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    labels = labels_for(N)
    for name, quota in FORMS:
        sync = tpm_from_rules(rules_for(table_of((1, 1, 1), quota), N))
        if abs(phi_read(np.asarray(sync, dtype=float), labels)["whole_phi"] - KNOWN[name]) > 1e-6:
            raise SystemExit(f"synchronous control failed for {name}")
    print("C2 deterministic, #62 construction and synchronous controls: PASS")
    cases = QUICK if args.quick else [(f, q, o) for f, q in FORMS for o in ORDERS]
    rows = []
    for c in cases:
        rows.append(read(*c))
        show(rows[-1])
    if args.quick:
        return
    tri = {f: [x for x in rows if x["form"] == f and x["whole_phi"] > PHI_EPS] for f, _ in FORMS}
    counts = {f: len(v) for f, v in tri.items()}
    print("orders with whole Phi > 0, of 24:", counts)
    g = {(x["form"], tuple(x["order_labels"])): x for x in rows}
    first = ("S", "P1", "P2", "P3")
    scores = {
        "H1": counts["OR3"] > 0 and counts["AND3"] > 0,
        "H2": all(g[(f, first)]["whole_phi"] > PHI_EPS for f in ("OR3", "AND3")),
        "H3": all(x["whole_phi"] <= PHI_EPS for x in rows if x["s_last"]),
        "H4": counts["MAJ3"] == 0,
        "H5": counts["OR3"] == counts["AND3"],
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, triadic_counts=counts,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
