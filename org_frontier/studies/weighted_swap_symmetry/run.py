"""Swap symmetry (input noise eta vs party-side noise eps) for weights (1,1,1,2) at quotas 2, 3, 4.

Run from the repo root: python org_frontier/studies/weighted_swap_symmetry/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import json
import os
import sys
from importlib.metadata import version
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import cm_numeric, gate_c1, labels_for  # noqa: E402
from org_frontier.studies.dummy_party_noise.run import noisy_tpm  # noqa: E402

W = (1, 1, 1, 2)
FORMS = (("1112q2", 4, 2), ("1112q3", 4, 3), ("1112q4", 4, 4))
GRID = (0.0, 0.05, 0.2)
QUICK = [("1112q3", 4, 3, 0.05, 0.2), ("1112q3", 4, 3, 0.2, 0.05)]


def whole(case):
    name, n, q, eta, eps = case
    tpm = noisy_tpm(W, q, eta, eps)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels_for(n))
    vals = []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        vals.append(float(new_big_phi.sia(pyphi.Subsystem(net, state, tuple(range(n + 1)))).phi))
    return dict(form=name, n=n, q=q, eta=eta, eps=eps, n_states=len(vals), whole_phi=max(vals))


def show(x):
    print(f"{x['form']:<6} eta={x['eta']:<4} eps={x['eps']:<4} states={x['n_states']} whole={x['whole_phi']:.6f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, n, q, a, b) for f, n, q in FORMS for a in GRID for b in GRID]
    with Pool(os.cpu_count() or 1) as pool:
        rows = pool.map(whole, cases)
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["form"], x["eta"], x["eps"]): x["whole_phi"] for x in rows}
    pairs = [(a, b) for i, a in enumerate(GRID) for b in GRID[i + 1:]]
    maxdiff = {f: max(abs(g[(f, a, b)] - g[(f, b, a)]) for a, b in pairs) for f, _, _ in FORMS}
    for f, d in maxdiff.items():
        print(f, "max swap diff", f"{d:.6g}")
    names = [f for f, _, _ in FORMS]
    rel = {f: [abs(g[(f, a, 0.2)] - g[(f, a, 0.0)]) / g[(f, a, 0.0)] if g[(f, a, 0.0)] > PHI_EPS else None
               for a in GRID if a > 0] for f in names}
    print("relative change eps 0 -> 0.2:", rel)
    scores = {
        "H1": all(maxdiff[f] > 1e-6 for f in names),
        "H2": all(g[(f, 0.0, b)] <= PHI_EPS for f in names for b in GRID),
        "H3": all(r is not None and r < 0.05 for f in names for r in rel[f]),
    }
    scores = {k: "SUPPORTED" if v else "REFUTED" for k, v in scores.items()}
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.write_text(json.dumps(dict(pyphi=version("pyphi"), phi_eps=PHI_EPS, scores=scores,
                                       max_swap_diff=maxdiff, rel_change_eps=rel, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
