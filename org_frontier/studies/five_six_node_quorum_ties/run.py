"""Weighted (1,1,2,2) and five-party 3-of-5 quorums under independent input noise, read as tie sets.

Run from the repo root: python org_frontier/studies/five_six_node_quorum_ties/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import json
import os
import sys
import time
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, table_of,
)

W = (1, 1, 2, 2)
A_CASES = [(f"w{q}", W, q, e) for q in (2, 3, 4, 5) for e in (0.0, 0.05, 0.2, 0.4)]
CONTROL = [("w2", W, 2, 0.1), ("w5", W, 5, 0.1)]
B_CASES = [("3of5", (1,) * 5, 3, 0.1), ("3of5", (1,) * 5, 3, 0.2)]
QUICK = [("w2", W, 2, 0.2)]


def read(name, weights, quota, e):
    t0 = time.time()
    n = len(weights)
    labels = labels_for(n)
    tpm = input_tpm(table_of(weights, quota), n, e)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(n + 1))
    states = []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        top = max(phis.values())
        ties = sorted((k for k, v in phis.items() if top - v <= PHI_EPS and top > PHI_EPS),
                      key=lambda k: (len(k), k))
        states.append(dict(state=list(state), top=top, full_phi=phis.get(full, 0.0),
                           ties=["".join(labels[i] for i in k) for k in ties],
                           full_in_ties=full in ties))
    whole = max(s["full_phi"] for s in states)
    best = max(states, key=lambda s: s["top"])
    return dict(form=name, weights=list(weights), quota=quota, e=e, whole_phi=whole,
                max_subset_phi=best["top"], ratio=(best["top"] / whole if whole > PHI_EPS else None),
                best_state=best["state"], best_ties=best["ties"], full_in_best=best["full_in_ties"],
                states=states, seconds=round(time.time() - t0, 1))


def show(r):
    ratio = f"{r['ratio']:.6f}" if r["ratio"] else "-"
    ties = ",".join(r["best_ties"]) if len(r["best_ties"]) <= 6 else f"{len(r['best_ties'])} subsets"
    print(f"{r['form']:<5} e={r['e']:<5} whole={r['whole_phi']:.6f} max_subset={r['max_subset_phi']:.6f} "
          f"ratio={ratio} full_in_top={'Y' if r['full_in_best'] else 'N'} top_ties={ties}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true", help="CI subset (one weighted case)")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    if args.quick:
        for r in map(lambda c: read(*c), QUICK):
            show(r)
        return
    for r in (read(*c) for c in CONTROL):
        if abs(r["whole_phi"] - 0.015905) > 1e-6:
            raise SystemExit(f"control failed: {r['form']} e=0.1 whole={r['whole_phi']}")
    print("C2 probe 464 control (w2, w5 at e=0.1 whole=0.015905): PASS")
    a = [read(*c) for c in A_CASES]
    b = [read(*c) for c in B_CASES]
    for r in a + b:
        show(r)
    noisy_a = [r for r in a if r["e"] > 0]
    scores = {
        "H1": all("SP3P4" in r["best_ties"] for r in noisy_a if r["quota"] in (2, 5)),
        "H2": all(r["whole_phi"] > PHI_EPS for r in noisy_a),
        "H3": all(r["ratio"] is not None and abs(r["ratio"] - 6) <= 6e-6 for r in b),
        "H4": all(sorted(r["best_ties"]) == sorted(f"SP{i}" for i in range(1, 6)) for r in b),
        "H5": not any(r["full_in_best"] for r in noisy_a + b),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            part_a=a, part_b=b), indent=1) + "\n")


if __name__ == "__main__":
    main()
