"""Deterministic memory rules on three-party quorum hubs: nodes that read their own last state.

Run from the repo root: python org_frontier/studies/memory_rules/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
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

pyphi.config.PROGRESS_BARS = False
N = 3
FORMS = (("OR3", 1), ("MAJ3", 2), ("AND3", 3))
PARTY = ("copy", "and", "or", "toggle")
MEDIATOR = ("plain", "toggle", "vote")
QUICK = (("MAJ3", 2, "copy", "toggle"), ("MAJ3", 2, "toggle", "plain"), ("OR3", 1, "copy", "vote"))
KNOWN = {"OR3": 3.0, "MAJ3": 0.0, "AND3": 3.0}


def memory_rules(quota, party, mediator):
    table = table_of((1, 1, 1), quota)

    def q(x):
        return table[x[1] + 2 * x[2] + 4 * x[3]]

    s_rule = {
        "plain": q,
        "toggle": lambda x: q(x) ^ x[0],
        "vote": lambda x: int(x[0] + x[1] + x[2] + x[3] >= quota + 1),
    }[mediator]
    p_rule = {
        "copy": lambda x, i: x[0],
        "and": lambda x, i: x[0] & x[i],
        "or": lambda x, i: x[0] | x[i],
        "toggle": lambda x, i: x[0] ^ x[i],
    }[party]
    return [s_rule] + [(lambda x, i=i: p_rule(x, i)) for i in range(1, N + 1)]


def read(name, quota, party, mediator):
    labels = labels_for(N)
    tpm = np.asarray(tpm_from_rules(memory_rules(quota, party, mediator), n=N + 1), dtype=float)
    if party == "copy" and mediator == "plain":
        ref = tpm_from_rules(rules_for(table_of((1, 1, 1), quota), N))
        assert np.allclose(tpm, ref, atol=1e-12, rtol=0)
    cm = cm_numeric(tpm)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
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
    return dict(form=name, party=party, mediator=mediator, n_states=len(states),
                self_loops=[labels[i] for i in range(N + 1) if cm[i, i]],
                whole_phi=max(s["full_phi"] for s in states), top=best["top"],
                top_ties=best["ties"], full_in_top=best["full_in"], states=states)


def show(x):
    ties = ",".join(x["top_ties"]) if len(x["top_ties"]) <= 6 else f"{len(x['top_ties'])} subsets"
    print(f"{x['form']:<5} party={x['party']:<6} med={x['mediator']:<6} states={x['n_states']:<2} "
          f"whole={x['whole_phi']:.6f} top={x['top']:.6f} full_in_top={'Y' if x['full_in_top'] else 'N'} "
          f"ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, q, p, m) for f, q in FORMS for m in MEDIATOR for p in PARTY]
    rows = [read(*c) for c in cases]
    for x in rows:
        if x["party"] == "copy" and x["mediator"] == "plain":
            if abs(x["whole_phi"] - KNOWN[x["form"]]) > 1e-6:
                raise SystemExit(f"known-hub control failed for {x['form']}")
    print("C2 copy/plain identity and known-hub controls: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["form"], x["party"], x["mediator"]): x for x in rows}
    count = {m: sum(g[(f, p, m)]["full_in_top"] for f, _ in FORMS for p in PARTY) for m in MEDIATOR}
    print("full group in top tie set, of 12:", count)
    scores = {
        "H1": all(g[("MAJ3", p, "plain")]["whole_phi"] <= PHI_EPS for p in PARTY),
        "H2": g[("MAJ3", "copy", "toggle")]["whole_phi"] > PHI_EPS,
        "H3": all(g[(f, p, "plain")]["whole_phi"] > PHI_EPS for f in ("OR3", "AND3") for p in PARTY),
        "H4": g[("MAJ3", "copy", "vote")]["whole_phi"] > PHI_EPS,
        "H5": count["toggle"] < count["plain"] and count["vote"] < count["plain"],
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, full_in_top_counts=count,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
