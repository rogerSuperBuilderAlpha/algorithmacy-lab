"""Survey of negative raw phi (PyPhi output) across the noisy-quorum panels.

Run from the repo root: python org_frontier/studies/negative_phi_survey/run.py [--quick] [--write]
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

FORMS = (("OR3", (1, 1, 1), 1), ("MAJ3", (1, 1, 1), 2), ("AND3", (1, 1, 1), 3),
         ("ANY4", (1, 1, 1, 1), 1), ("2of4", (1, 1, 1, 1), 2), ("3of4", (1, 1, 1, 1), 3),
         ("ALL4", (1, 1, 1, 1), 4))
RATES_A = (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45)
PANEL_B = [("1222q2", (1, 2, 2, 2), 2), ("1222q4", (1, 2, 2, 2), 4)]
RATES_B = (0.05, 0.1, 0.2)
QUICK = [("A", "OR3", (1, 1, 1), 1, 0.4), ("B", "1222q4", (1, 2, 2, 2), 4, 0.2)]


def survey(case):
    panel, name, w, q, e = case
    n = len(w)
    labels = labels_for(n)
    tpm = input_tpm(table_of(w, q), n, e)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(n + 1))
    vals, full_raw = [], []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        st = "".join(map(str, state))
        for s in new_big_phi.reachable_subsystems(net, net.node_indices, state):
            k = tuple(s.node_indices)
            v = float(new_big_phi.sia(s).phi)
            vals.append((st, "".join(labels[i] for i in k), v))
            if k == full:
                full_raw.append((st, v))
    neg = [x for x in vals if x[2] < -PHI_EPS]
    top = max(v for _, _, v in vals)
    ties = sorted({k for _, k, v in vals if top > PHI_EPS and top - v <= PHI_EPS})
    max_full = max((v for _, v in full_raw), default=None)
    return dict(panel=panel, form=name, weights=list(w), q=q, e=e, n_values=len(vals), n_negative=len(neg),
                min_phi=min(v for _, _, v in vals), negative=[dict(state=s, subset=k, phi=v) for s, k, v in neg],
                full_raw=[dict(state=s, phi=v) for s, v in full_raw], max_full_raw=max_full,
                whole_floored=max(0.0, max_full if max_full is not None else 0.0), top_phi=top, ties=ties)


def show(x):
    full_neg = [f for f in x["full_raw"] if f["phi"] < -PHI_EPS]
    full_zero = all(abs(f["phi"]) <= PHI_EPS for f in x["full_raw"])
    print(f"{x['panel']} {x['form']:<6} e={x['e']:<4} values={x['n_values']} negative={x['n_negative']} "
          f"min={x['min_phi']:.6f} max_full_raw={x['max_full_raw']:.6f} full_neg_states={len(full_neg)} "
          f"full_all_zero={'Y' if full_zero else 'N'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else ([("A", f, w, q, e) for f, w, q in FORMS for e in RATES_A]
                                      + [("B", f, w, q, e) for f, w, q in PANEL_B for e in RATES_B])
    with Pool(os.cpu_count() or 1) as pool:
        rows = pool.map(survey, cases)
    for x in rows:
        show(x)
    if args.quick:
        return
    pub = {(r["form"], r["e"]): r for r in json.loads(
        (ROOT / "org_frontier/studies/tie_set_membership/results/results.json").read_text())["rows"]}
    a = [x for x in rows if x["panel"] == "A"]
    b = [x for x in rows if x["panel"] == "B"]
    h2_detail = []
    for x in a:
        p = pub[(x["form"], x["e"])]
        same = (abs(p["whole_phi"] - x["whole_floored"]) <= PHI_EPS and abs(p["top_phi"] - x["top_phi"]) <= PHI_EPS
                and (p["whole_phi"] <= PHI_EPS or x["max_full_raw"] > PHI_EPS)
                and len(p["ties"]) == len(x["ties"]))
        h2_detail.append(dict(form=x["form"], e=x["e"], unchanged=same))
    scores = {
        "H1": "SUPPORTED" if all(x["n_negative"] == 0 for x in a if x["e"] <= 0.3) else "REFUTED",
        "H2": "SUPPORTED" if all(d["unchanged"] for d in h2_detail) else "REFUTED",
        "H3": "SUPPORTED" if all(abs(f["phi"]) <= PHI_EPS for x in b for f in x["full_raw"]) else "REFUTED",
    }
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.write_text(json.dumps(dict(pyphi=version("pyphi"), phi_eps=PHI_EPS, scores=scores,
                                       h2_detail=h2_detail, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
