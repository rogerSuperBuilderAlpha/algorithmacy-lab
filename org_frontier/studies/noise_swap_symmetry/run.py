"""Swap symmetry of whole phi in input noise (eta) and party-side noise (eps), OR3 and MAJ3.

Run from the repo root: python org_frontier/studies/noise_swap_symmetry/run.py [--quick] [--write]
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

FORMS = (("OR3", 1), ("MAJ3", 2))
GRID = (0.0, 0.02, 0.05, 0.1, 0.2)
QUICK = [("OR3", 1, 0.02, 0.1), ("OR3", 1, 0.1, 0.02)]


def whole(case):
    name, q, eta, eps = case
    tpm = noisy_tpm((1, 1, 1), q, eta, eps)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels_for(3))
    vals = []
    for index in reachable_states(tpm, 4):
        state = tuple((index >> i) & 1 for i in range(4))
        vals.append(float(new_big_phi.sia(pyphi.Subsystem(net, state, (0, 1, 2, 3))).phi))
    return dict(form=name, q=q, eta=eta, eps=eps, n_states=len(vals), whole_phi=max(vals))


def show(x):
    print(f"{x['form']:<4} eta={x['eta']:<6} eps={x['eps']:<6} states={x['n_states']} whole={x['whole_phi']:.6f}")


def comb(a, b):
    return round(a + b - 2 * a * b, 12)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    if args.quick:
        cases = QUICK
    else:
        cases = [(f, q, a, b) for f, q in FORMS for a in GRID for b in GRID]
        extra = sorted({comb(a, b) for a in GRID for b in GRID if a > 0 and b > 0} - set(GRID))
        cases += [("OR3", 1, c, 0.0) for c in extra]
    with Pool(os.cpu_count() or 1) as pool:
        rows = pool.map(whole, cases)
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["form"], x["eta"], x["eps"]): x["whole_phi"] for x in rows}
    pairs = [(a, b) for i, a in enumerate(GRID) for b in GRID[i + 1:]]
    swap = {f: [dict(eta=a, eps=b, ab=g[(f, a, b)], ba=g[(f, b, a)], diff=abs(g[(f, a, b)] - g[(f, b, a)]))
                for a, b in pairs] for f, _ in FORMS}
    combined = [dict(eta=a, eps=b, c=comb(a, b), value=g[("OR3", a, b)], at_c=g[("OR3", comb(a, b), 0.0)],
                     diff=abs(g[("OR3", a, b)] - g[("OR3", comb(a, b), 0.0)]))
                for a in GRID for b in GRID if a > 0 and b > 0]
    scores = {
        "H1": all(d["diff"] <= 1e-6 for d in swap["OR3"]),
        "H2": all(d["diff"] <= 1e-6 for d in swap["MAJ3"]),
        "H3": all(d["diff"] <= 1e-6 for d in combined),
    }
    scores = {k: "SUPPORTED" if v else "REFUTED" for k, v in scores.items()}
    for f in swap:
        print(f, "max swap diff", f"{max(d['diff'] for d in swap[f]):.6g}")
    print("OR3 max combined-rate diff", f"{max(d['diff'] for d in combined):.6g}")
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.write_text(json.dumps(dict(pyphi=version("pyphi"), phi_eps=PHI_EPS, scores=scores, swap=swap,
                                       combined=combined, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
