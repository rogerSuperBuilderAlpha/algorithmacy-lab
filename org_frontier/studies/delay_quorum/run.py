"""Delay on quorum hubs: the mediator's decision reaches the parties through a chain of d relays.

Run from the repo root: python org_frontier/studies/delay_quorum/run.py [--quick] [--write]
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
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, rules_for, table_of,
)

pyphi.config.PROGRESS_BARS = False
N = 3
FORMS = (("OR3", 1), ("MAJ3", 2), ("AND3", 3))
NOISE = (0.0, 0.1)
DELAYS = (0, 1, 2)
QUICK = (("OR3", 1, 0.0, 0), ("OR3", 1, 0.0, 1), ("MAJ3", 2, 0.1, 1))
KNOWN = {("OR3", 0.0): 3.0, ("AND3", 0.0): 3.0, ("MAJ3", 0.0): 0.0, ("MAJ3", 0.1): 0.026981}


def delay_tpm(table, r, d):
    """Nodes: 0 = S, 1..3 = parties, 4..3+d = relays B1..Bd. S misreads each party w.p. r."""
    nn = N + 1 + d
    tpm = np.zeros((2 ** nn, nn))
    last = 0 if d == 0 else N + d
    for state in range(2 ** nn):
        actual = (state >> 1) & 0b111
        for observed, output in enumerate(table):
            dist = (actual ^ observed).bit_count()
            tpm[state, 0] += output * r ** dist * (1 - r) ** (N - dist)
        for i in range(1, N + 1):
            tpm[state, i] = (state >> last) & 1
        for k in range(d):
            src = 0 if k == 0 else N + k
            tpm[state, N + 1 + k] = (state >> src) & 1
    return tpm


def read(name, quota, r, d):
    labels = labels_for(N) + tuple(f"B{k + 1}" for k in range(d))
    table = table_of((1, 1, 1), quota)
    tpm = delay_tpm(table, r, d)
    if d == 0:
        ref = tpm_from_rules(rules_for(table, N)) if r == 0 else input_tpm(table, N, r)
        assert np.allclose(tpm, ref, atol=1e-12, rtol=0)
    nn = tpm.shape[1]
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(nn))
    states = []
    for index in reachable_states(tpm, nn):
        state = tuple((index >> i) & 1 for i in range(nn))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        top = max(phis.values()) if phis else 0.0
        ties = sorted((k for k, v in phis.items() if top > PHI_EPS and top - v <= PHI_EPS),
                      key=lambda k: (len(k), k))
        states.append(dict(state=list(state), top=top, full_phi=phis.get(full, 0.0),
                           ties=["".join(labels[i] for i in k) for k in ties], full_in=full in ties))
    best = max(states, key=lambda s: s["top"])
    return dict(form=name, r=r, d=d, n_nodes=nn, n_states=len(states),
                whole_phi=max(s["full_phi"] for s in states), top=best["top"],
                top_ties=best["ties"], full_in_top=best["full_in"], states=states)


def show(x):
    ties = ",".join(x["top_ties"]) if len(x["top_ties"]) <= 6 else f"{len(x['top_ties'])} subsets"
    print(f"{x['form']:<5} r={x['r']:<4} d={x['d']} states={x['n_states']:<2} "
          f"whole={x['whole_phi']:.6f} top={x['top']:.6f} full_in_top={'Y' if x['full_in_top'] else 'N'} "
          f"ties={ties or '-'}", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, q, r, d) for f, q in FORMS for r in NOISE for d in DELAYS]
    rows = []
    for c in cases:
        rows.append(read(*c))
        if not args.quick:
            show(rows[-1])
    for x in rows:
        k = (x["form"], x["r"])
        if x["d"] == 0 and k in KNOWN and abs(x["whole_phi"] - KNOWN[k]) > 1e-6:
            raise SystemExit(f"known-hub control failed for {k}")
    print("C2 d=0 identity and known-hub controls: PASS")
    if args.quick:
        for x in rows:
            show(x)
        return
    g = {(x["form"], x["r"], x["d"]): x for x in rows}
    scores = {
        "H1": all(g[(f, 0.0, d)]["whole_phi"] > PHI_EPS for f in ("OR3", "AND3") for d in DELAYS),
        "H2": all(g[("MAJ3", 0.0, d)]["whole_phi"] <= PHI_EPS for d in DELAYS),
        "H3": all(g[("MAJ3", 0.1, d)]["whole_phi"] > PHI_EPS for d in DELAYS),
        "H4": g[("OR3", 0.0, 1)]["whole_phi"] < g[("OR3", 0.0, 0)]["whole_phi"],
        "H5": not g[("OR3", 0.0, 1)]["full_in_top"],
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
