"""Weighted (1,1,1,2) quorums under input noise: strongest-subset/whole ratio against generalized R.

Run from the repo root: python org_frontier/studies/weighted_ratio_law/run.py [--quick] [--write]
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

W = (1, 1, 1, 2)
RATES = (0.05, 0.1, 0.2)
CASES = [(q, e) for q in range(1, 6) for e in RATES]
QUICK = [(3, 0.2), (2, 0.2)]
CONTROL = ((1, 1, 2, 2), 3, 0.2, 0.032470)


def law(weights, q):
    """Groups of parties (incl. empty) too small to settle the outcome alone."""
    total, n = sum(weights), len(weights)
    count = 0
    for k in range(n + 1):
        for c in combinations(range(n), k):
            w = sum(weights[i] for i in c)
            count += not (w >= q or w >= total - q + 1)
    return count


def read(case, weights=W):
    q, e = case
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
    return dict(form=f"w{q}", weights=list(weights), q=q, e=e, whole_phi=whole, top_phi=top,
                ratio=(top / whole if whole > PHI_EPS else None), law=law(weights, q), top_state=top_state,
                ties=["".join(labels[i] for i in k) for k in ties], full_in_ties=full in ties,
                seconds=round(time.time() - t0, 1))


def show(x):
    ratio = f"{x['ratio']:.6f}" if x["ratio"] else "-"
    ties = ",".join(x["ties"]) if len(x["ties"]) <= 6 else f"{len(x['ties'])} subsets"
    print(f"{x['form']:<3} e={x['e']:<4} whole={x['whole_phi']:.6f} top={x['top_phi']:.6f} ratio={ratio} "
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
    g = {(x["q"], x["e"]): x for x in rows}
    if not args.quick:
        w, q, e, v = CONTROL
        c = read((q, e), weights=w)
        if abs(c["whole_phi"] - v) > 1e-6:
            raise SystemExit("five_six_node_quorum_ties control failed")
        print(f"C2 (1,1,2,2) quota 3 control whole={c['whole_phi']:.6f} ratio={c['ratio']:.6f} law={c['law']}: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    rel = lambda a, b: abs(a - b) <= 1e-6 * max(abs(b), 1e-12)  # noqa: E731
    r2 = [g[(2, e)]["ratio"] for e in RATES]
    scores = {
        "H1": all(g[(3, e)]["ratio"] is not None and rel(g[(3, e)]["ratio"], 8) for e in RATES),
        "H2": None not in r2 and (max(r2) - min(r2)) / min(r2) > 0.01,
        "H3": all(rel(g[(4, e)]["whole_phi"], g[(2, e)]["whole_phi"]) and rel(g[(4, e)]["top_phi"], g[(2, e)]["top_phi"])
                  for e in RATES),
        "H4": all(g[(q, e)]["ratio"] is not None and rel(g[(q, e)]["ratio"], 1) and g[(q, e)]["full_in_ties"]
                  for q in (1, 5) for e in RATES),
        "H5": not any(g[(q, e)]["full_in_ties"] for q in (2, 3, 4) for e in RATES),
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
