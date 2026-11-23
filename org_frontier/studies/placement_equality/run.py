"""When does party-side noise give the same whole Φ as mediator-side noise on quorum hubs?

Run from the repo root: python org_frontier/studies/placement_equality/run.py [--quick] [--write]
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

FORMS = (("OR3", 3, 1), ("MAJ3", 3, 2), ("AND3", 3, 3),
         ("1of4", 4, 1), ("2of4", 4, 2), ("3of4", 4, 3), ("4of4", 4, 4))
PLACEMENTS = ("mediator", "party")
RATES = (0.05, 0.1, 0.2, 0.4)
QUICK = (("AND3", 3, 3, "party", 0.1), ("2of4", 4, 2, "party", 0.1))
CONTROLS = {("OR3", "party", 0.1): 1.854569, ("OR3", "party", 0.4): 0.170446,
            ("MAJ3", "mediator", 0.2): 0.036624, ("MAJ3", "party", 0.2): 0.0}


def placement_tpm(table, n, placement, r):
    tpm = input_tpm(table, n, r if placement == "mediator" else 0.0)
    d = r if placement == "party" else 0.0
    for state in range(len(tpm)):
        tpm[state, 1:] = (1 - d) if state & 1 else d
    return tpm


def read(name, n, quota, placement, r):
    labels = labels_for(n)
    table = table_of((1,) * n, quota)
    tpm = placement_tpm(table, n, placement, r)
    assert np.allclose(placement_tpm(table, n, placement, 0.0),
                       tpm_from_rules(rules_for(table, n)), atol=1e-12, rtol=0)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(n + 1))
    best = dict(phi=0.0, state=None)
    per_state = {}
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        phi = float(new_big_phi.sia(pyphi.Subsystem(net, state, full)).phi)
        per_state["".join(map(str, state))] = phi
        if phi > best["phi"] + PHI_EPS:
            best = dict(phi=phi, state=list(state))
    return dict(form=name, placement=placement, r=r, whole_phi=best["phi"], peak_state=best["state"],
                per_state=per_state)


def show(x):
    st = "".join(map(str, x["peak_state"])) if x["peak_state"] else "-"
    print(f"{x['form']:<5} {x['placement']:<8} r={x['r']:<5} whole={x['whole_phi']:.6f} peak={st}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, n, q, p, r) for f, n, q in FORMS for p in PLACEMENTS for r in RATES]
    rows = [read(*c) for c in cases]
    g = {(x["form"], x["placement"], x["r"]): x for x in rows}
    if not args.quick:
        for k, v in CONTROLS.items():
            if abs(g[k]["whole_phi"] - v) > 1e-6:
                raise SystemExit(f"noise_placement control failed at {k}")
    print("C2 deterministic identity and noise_placement controls: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    eq = lambda a, b: abs(a["whole_phi"] - b["whole_phi"]) <= 1e-6  # noqa: E731
    scores = {
        "H1": all(eq(g[("AND3", p, r)], g[("OR3", p, r)]) for p in PLACEMENTS for r in RATES),
        "H2": all(eq(g[("1of4", "party", r)], g[("1of4", "mediator", r)]) for r in (0.05, 0.1)),
        "H3": all(g[(f, "party", r)]["whole_phi"] <= PHI_EPS for f in ("2of4", "3of4") for r in RATES),
        "H4": all(g[("OR3", "party", r)]["peak_state"] == g[("OR3", "mediator", r)]["peak_state"]
                  for r in (0.05, 0.1, 0.2)),
        "H5": all(eq(g[("4of4", "party", r)], g[("4of4", "mediator", r)]) for r in (0.05, 0.1)),
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
