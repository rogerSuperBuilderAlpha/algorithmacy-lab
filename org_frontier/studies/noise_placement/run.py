"""Party-side vs mediator-side input noise on three-party quorum hubs, read as tie sets.

Run from the repo root: python org_frontier/studies/noise_placement/run.py [--quick] [--write]
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

N = 3
FORMS = (("OR3", 1), ("MAJ3", 2))
PLACEMENTS = ("mediator", "party", "both")
RATES = (0.0, 0.05, 0.1, 0.2, 0.4)
QUICK = (("MAJ3", 2, "party", 0.2), ("MAJ3", 2, "both", 0.2))


def placement_tpm(table, placement, r):
    tpm = input_tpm(table, N, r if placement in ("mediator", "both") else 0.0)
    d = r if placement in ("party", "both") else 0.0
    for state in range(len(tpm)):
        tpm[state, 1:] = (1 - d) if state & 1 else d
    return tpm


def read(name, quota, placement, r):
    labels = labels_for(N)
    table = table_of((1, 1, 1), quota)
    tpm = placement_tpm(table, placement, r)
    if r == 0:
        assert np.allclose(tpm, tpm_from_rules(rules_for(table, N)), atol=1e-12, rtol=0)
    if placement == "mediator":
        assert np.allclose(tpm, input_tpm(table, N, r), atol=1e-12, rtol=0)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(N + 1))
    states = []
    for index in reachable_states(tpm, N + 1):
        state = tuple((index >> i) & 1 for i in range(N + 1))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        top = max(phis.values())
        ties = sorted((k for k, v in phis.items() if top > PHI_EPS and top - v <= PHI_EPS),
                      key=lambda k: (len(k), k))
        states.append(dict(state=list(state), top=top, full_phi=phis.get(full, 0.0),
                           ties=["".join(labels[i] for i in k) for k in ties], full_in=full in ties))
    best = max(states, key=lambda s: s["top"])
    return dict(form=name, placement=placement, r=r, n_states=len(states),
                whole_phi=max(s["full_phi"] for s in states), top=best["top"],
                top_ties=best["ties"], full_in_top=best["full_in"], states=states)


def show(x):
    ties = ",".join(x["top_ties"]) if len(x["top_ties"]) <= 6 else f"{len(x['top_ties'])} subsets"
    print(f"{x['form']:<5} {x['placement']:<8} r={x['r']:<5} states={x['n_states']:<2} "
          f"whole={x['whole_phi']:.6f} top={x['top']:.6f} full_in_top={'Y' if x['full_in_top'] else 'N'} "
          f"ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, q, p, r) for f, q in FORMS for p in PLACEMENTS for r in RATES]
    rows = [read(*c) for c in cases]
    if not args.quick:
        m = next(x for x in rows if x["form"] == "MAJ3" and x["placement"] == "mediator" and x["r"] == 0.1)
        if abs(m["whole_phi"] - 0.026981) > 1e-6:
            raise SystemExit("probe 464 control failed")
    print("C2 deterministic identity and probe 464 TPM/value controls: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["form"], x["placement"], x["r"]): x for x in rows}
    nz = RATES[1:]
    scores = {
        "H1": all(g[("MAJ3", "party", r)]["whole_phi"] <= PHI_EPS for r in RATES),
        "H2": all(g[("MAJ3", "both", r)]["whole_phi"] > PHI_EPS for r in nz),
        "H3": all(g[("OR3", "party", r)]["full_in_top"] for r in nz),
        "H4": not any(g[("MAJ3", p, r)]["full_in_top"] for p in PLACEMENTS for r in nz),
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
