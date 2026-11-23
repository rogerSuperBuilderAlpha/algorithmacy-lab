"""Swap symmetry (input noise eta vs party-side noise eps) across AND3, ANY4, ALL4, 2of4, 3of4.

Run from the repo root: python org_frontier/studies/swap_symmetry_panel/run.py [--quick] [--write]
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

FORMS = (("AND3", 3, 3), ("ANY4", 4, 1), ("ALL4", 4, 4), ("2of4", 4, 2), ("3of4", 4, 3))
GRID = (0.0, 0.02, 0.05, 0.1, 0.2)
QUICK = [("ANY4", 4, 1, 0.02, 0.1), ("ANY4", 4, 1, 0.1, 0.02)]


def whole(case):
    name, n, q, eta, eps = case
    tpm = noisy_tpm((1,) * n, q, eta, eps)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels_for(n))
    vals = []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        vals.append(float(new_big_phi.sia(pyphi.Subsystem(net, state, tuple(range(n + 1)))).phi))
    return dict(form=name, n=n, q=q, eta=eta, eps=eps, n_states=len(vals), whole_phi=max(vals))


def show(x):
    print(f"{x['form']:<4} eta={x['eta']:<4} eps={x['eps']:<4} states={x['n_states']} whole={x['whole_phi']:.6f}")


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
    scores = {
        "H1": all(maxdiff[f] <= 1e-6 for f in ("AND3", "ANY4", "ALL4")),
        "H2": all(maxdiff[f] > 1e-6 for f in ("2of4", "3of4")),
        "H3": all(g[(f, 0.0, b)] <= PHI_EPS for f in ("2of4", "3of4") for b in GRID),
    }
    scores = {k: "SUPPORTED" if v else "REFUTED" for k, v in scores.items()}
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.write_text(json.dumps(dict(pyphi=version("pyphi"), phi_eps=PHI_EPS, scores=scores,
                                       max_swap_diff=maxdiff, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
