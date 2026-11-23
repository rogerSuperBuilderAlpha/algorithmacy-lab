"""Weighted (1,2,2,2) and (1,1,2,3) quorums under input noise: when does a weighted rule act like a counting rule?

Run from the repo root: python org_frontier/studies/weighted_equivalence/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import json
import os
import sys
import time
from importlib.metadata import version
from itertools import combinations
from multiprocessing import Pool
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

A, B = (1, 2, 2, 2), (1, 1, 2, 3)
RATES = (0.05, 0.1, 0.2)
CASES = ([(A, q, e) for q in (2, 4) for e in RATES] + [(A, 3, 0.2)]
         + [(B, q, e) for q in (1, 2, 3, 4) for e in RATES] + [(B, q, 0.2) for q in (5, 6, 7)])
QUICK = [(A, 4, 0.2), (B, 3, 0.2)]


def law(weights, q):
    """Groups of parties (incl. empty) too small to settle the outcome alone."""
    total, n = sum(weights), len(weights)
    count = 0
    for k in range(n + 1):
        for c in combinations(range(n), k):
            w = sum(weights[i] for i in c)
            count += not (w >= q or w >= total - q + 1)
    return count


def read(case):
    weights, q, e = case
    n = len(weights)
    t0 = time.time()
    labels = labels_for(n)
    tpm = input_tpm(table_of(weights, q), n, e)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(n + 1))
    whole, top, ties, top_state = 0.0, 0.0, [], None
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        whole = max(whole, phis.get(full, 0.0))
        t = max(phis.values())
        if t > top + PHI_EPS:
            top, top_state = t, list(state)
            ties = sorted((k for k, v in phis.items() if t - v <= PHI_EPS), key=lambda k: (len(k), k))
    return dict(form="".join(map(str, weights)) + f"q{q}", weights=list(weights), q=q, e=e, whole_phi=whole, top_phi=top,
                ratio=(top / whole if whole > PHI_EPS else None), law=law(weights, q), top_state=top_state,
                ties=["".join(labels[i] for i in k) for k in ties], full_in_ties=full in ties,
                seconds=round(time.time() - t0, 1))


def show(x):
    ratio = f"{x['ratio']:.6f}" if x["ratio"] else "-"
    ties = ",".join(x["ties"]) if len(x["ties"]) <= 6 else f"{len(x['ties'])} subsets"
    print(f"{x['form']:<7} e={x['e']:<4} whole={x['whole_phi']:.6f} top={x['top_phi']:.6f} ratio={ratio} "
          f"law={x['law']} n_ties={len(x['ties'])} full_in_top={'Y' if x['full_in_ties'] else 'N'} ties={ties}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else CASES
    with Pool(min(len(cases), os.cpu_count() or 1)) as pool:
        rows = pool.map(read, cases)
    g = {(tuple(x["weights"]), x["q"], x["e"]): x for x in rows}
    if not args.quick:
        c, ref = g[(A, 3, 0.2)], (0.035822, 0.179110)
        if abs(c["whole_phi"] - ref[0]) > 1e-6 or abs(c["top_phi"] - ref[1]) > 1e-6:
            raise SystemExit("2of4 equivalence control failed")
        print("C2 (1,2,2,2) quota 3 = 2of4 control (whole 0.035822, top 0.179110): PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    rel = lambda a, b: abs(a - b) <= 1e-6 * max(abs(b), 1e-12)  # noqa: E731

    def drifts(w, q):
        r = [g[(w, q, e)]["ratio"] for e in RATES]
        return None not in r and (max(r) - min(r)) / min(r) > 0.01

    def same(k1, k2):
        return rel(g[k1]["whole_phi"], g[k2]["whole_phi"]) and rel(g[k1]["top_phi"], g[k2]["top_phi"])

    scores = {
        "H1": all(g[(A, 4, e)]["ratio"] is not None and rel(g[(A, 4, e)]["ratio"], 4) for e in RATES),
        "H2": all(not g[(A, 2, e)]["full_in_ties"] and g[(A, 2, e)]["ties"] == ["SP2P3P4"] for e in RATES),
        "H3": all(drifts(B, q) for q in (2, 3, 4)),
        "H4": same((B, 5, 0.2), (B, 3, 0.2)) and same((B, 6, 0.2), (B, 2, 0.2)),
        "H5": all(g[(B, q, 0.2)]["ratio"] is not None and rel(g[(B, q, 0.2)]["ratio"], 1)
                  and g[(B, q, 0.2)]["full_in_ties"] for q in (1, 7)),
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
