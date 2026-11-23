"""Never-pivotal (dummy) party added to OR3 and AND3, under input noise and party-side noise.

Run from the repo root: python org_frontier/studies/dummy_party_noise/run.py [--quick] [--write]
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
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, table_of,
)

FORMS = (("OR3+d", (1, 2, 2, 2), 2, "OR3"), ("AND3+d", (1, 2, 2, 2), 6, "AND3"),
         ("OR3", (1, 1, 1), 1, None), ("AND3", (1, 1, 1), 3, None))
ETAS = (0.05, 0.1, 0.2)
EPSS = (0.0, 0.05, 0.1)
QUICK = [("OR3+d", (1, 2, 2, 2), 2, 0.1, 0.05), ("OR3", (1, 1, 1), 1, 0.1, 0.05)]


def noisy_tpm(w, q, eta, eps):
    n = len(w)
    tpm = input_tpm(table_of(w, q), n, eta)
    tpm[:, 1:] = tpm[:, 1:] * (1 - eps) + (1 - tpm[:, 1:]) * eps
    return tpm


def read(case):
    name, w, q, eta, eps = case
    n = len(w)
    labels = labels_for(n)
    tpm = noisy_tpm(w, q, eta, eps)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(n + 1))
    vals, full_raw = [], []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        for s in new_big_phi.reachable_subsystems(net, net.node_indices, state):
            k = tuple(s.node_indices)
            v = float(new_big_phi.sia(s).phi)
            vals.append((k, v))
            if k == full:
                full_raw.append(v)
    top = max(v for _, v in vals)
    ties = sorted({"".join(labels[i] for i in k) for k, v in vals if top > PHI_EPS and top - v <= PHI_EPS})
    return dict(form=name, weights=list(w), q=q, eta=eta, eps=eps, n_states=len(full_raw),
                whole_phi=max(full_raw) if full_raw else 0.0, full_all_zero=all(abs(v) <= PHI_EPS for v in full_raw),
                top_phi=top, ties=ties)


def show(x):
    print(f"{x['form']:<7} eta={x['eta']:<4} eps={x['eps']:<4} states={x['n_states']} whole={x['whole_phi']:.6f} "
          f"full_all_zero={'Y' if x['full_all_zero'] else 'N'} top={x['top_phi']:.6f} ties={','.join(x['ties'])}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, w, q, a, b) for f, w, q, _ in FORMS for a in ETAS for b in EPSS]
    with Pool(os.cpu_count() or 1) as pool:
        rows = pool.map(read, cases)
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["form"], x["eta"], x["eps"]): x for x in rows}
    grid = [(a, b) for a in ETAS for b in EPSS]
    dummies = [(f, c) for f, _, _, c in FORMS if c]
    scores = {
        "H1": all(g[(f, a, b)]["full_all_zero"] for f, _ in dummies for a, b in grid),
        "H2": all(abs(g[(f, a, b)]["top_phi"] - g[(c, a, b)]["whole_phi"]) <= 1e-6
                  and g[(f, a, b)]["ties"] == ["SP2P3P4"] for f, c in dummies for a, b in grid),
        "H3": all(abs(g[("OR3+d", a, b)][k] - g[("AND3+d", a, b)][k]) <= 1e-9
                  for a, b in grid for k in ("whole_phi", "top_phi")),
    }
    scores = {k: "SUPPORTED" if v else "REFUTED" for k, v in scores.items()}
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.write_text(json.dumps(dict(pyphi=version("pyphi"), phi_eps=PHI_EPS, scores=scores, rows=rows),
                                  indent=1) + "\n")


if __name__ == "__main__":
    main()
