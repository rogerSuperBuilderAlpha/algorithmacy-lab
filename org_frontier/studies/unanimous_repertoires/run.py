"""Cause and effect repertoires at the unanimous state, both noise placements.

Run from the repo root: python org_frontier/studies/unanimous_repertoires/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md before this script ran.
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

from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, table_of,
)
from org_frontier.studies.placement_equality.run import placement_tpm  # noqa: E402

STORED = {
    ("OR3", "mediator", 0.2): 1.0415184462530138,
    ("OR3", "party", 0.2): 1.041518446253012,
    ("OR3", "mediator", 0.4): -0.1242086202819146,
    ("OR3", "party", 0.4): 0.1704462949802986,
    ("1of4", "mediator", 0.2): 1.110953009336554,
    ("1of4", "party", 0.2): 1.1109530093365452,
    ("1of4", "mediator", 0.4): -0.09325477255320004,
    ("1of4", "party", 0.4): 0.13635703598423843,
}
FORMS = (("OR3", 3, 1, (0, 0, 0, 0)), ("1of4", 4, 1, (0, 0, 0, 0, 0)))
PLACEMENTS = ("mediator", "party")
RATES = (0.2, 0.4)
QUICK = (("OR3", 3, 1, (0, 0, 0, 0), "party", 0.2),
         ("OR3", 3, 1, (0, 0, 0, 0), "mediator", 0.4))
PHI_TOL = 1e-6
REP_TOL = 1e-10
HYPOTHESES_COMMIT = "b87dc190bb9418632bcaec8b27e777b686b3ad9c"


def ria_record(ria):
    if ria is None:
        return None
    rep = None if ria.repertoire is None else np.asarray(ria.repertoire).reshape(-1).tolist()
    prep = None if ria.partitioned_repertoire is None else np.asarray(ria.partitioned_repertoire).reshape(-1).tolist()
    sel = None if ria.selectivity is None else float(ria.selectivity)
    return dict(
        phi=float(ria.phi),
        purview=list(ria.purview) if ria.purview is not None else None,
        partition=str(ria.partition) if ria.partition is not None else None,
        repertoire=rep,
        partitioned_repertoire=prep,
        selectivity=sel,
    )


def analyze(name, n, quota, state, placement, r):
    table = table_of((1,) * n, quota)
    tpm = placement_tpm(table, n, placement, r)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels_for(n))
    sia = new_big_phi.sia(pyphi.Subsystem(net, state, tuple(range(n + 1))))
    return dict(
        form=name, placement=placement, r=r, state="".join(map(str, state)),
        system_phi=float(sia.phi),
        mip=str(sia.partition) if sia.partition is not None else None,
        cause=ria_record(sia.cause),
        effect=ria_record(sia.effect),
    )


def arrays_close(a, b, tol=REP_TOL):
    if a is None or b is None:
        return a is None and b is None
    if len(a) != len(b):
        return False
    return all(abs(x - y) <= tol for x, y in zip(a, b))


def side_match(a, b):
    if a is None or b is None:
        return False
    return (
        abs(a["phi"] - b["phi"]) <= PHI_TOL
        and a["purview"] == b["purview"]
        and a["partition"] == b["partition"]
        and arrays_close(a["repertoire"], b["repertoire"])
    )


def show(x):
    c = x["cause"]["phi"] if x["cause"] else float("nan")
    e = x["effect"]["phi"] if x["effect"] else float("nan")
    print(f"{x['form']:<5} {x['placement']:<8} r={x['r']:<4} state={x['state']} "
          f"system={x['system_phi']:.6f} cause={c:.6f} effect={e:.6f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [
        (f, n, q, st, p, r) for f, n, q, st in FORMS for p in PLACEMENTS for r in RATES
    ]
    rows = [analyze(*c) for c in cases]
    for x in rows:
        show(x)
    if args.quick:
        return
    by = {(x["form"], x["placement"], x["r"]): x for x in rows}
    for key, stored in STORED.items():
        got = by[key]["system_phi"]
        if abs(got - stored) > PHI_TOL:
            raise SystemExit(f"control failed at {key}: stored {stored} got {got}")
    print("stored system-phi controls: PASS")

    def pair(form, r):
        return by[(form, "mediator", r)], by[(form, "party", r)]

    def h1_for(form):
        med, par = pair(form, 0.2)
        return side_match(med["cause"], par["cause"]) and side_match(med["effect"], par["effect"])

    def h2_for(form, stored_med, stored_par):
        med, par = pair(form, 0.4)
        mc, me = med["cause"]["phi"], med["effect"]["phi"]
        pc, pe = par["cause"]["phi"], par["effect"]["phi"]
        med_ok = (me < mc) and (abs(me - stored_med) <= PHI_TOL)
        par_ok = (pc > 1e-9) and (pe > 1e-9) and (abs(min(pc, pe) - stored_par) <= PHI_TOL)
        return med_ok and par_ok

    scores = {
        "H1": "SUPPORTED" if h1_for("OR3") else "REFUTED",
        "H2": "SUPPORTED" if h2_for("OR3", STORED[("OR3", "mediator", 0.4)],
                                    STORED[("OR3", "party", 0.4)]) else "REFUTED",
        "H3": "SUPPORTED" if (h1_for("1of4") and h2_for(
            "1of4", STORED[("1of4", "mediator", 0.4)], STORED[("1of4", "party", 0.4)]
        )) else "REFUTED",
    }
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.parent.mkdir(exist_ok=True)
        out.write_text(json.dumps(dict(
            pyphi=version("pyphi"),
            phi_eps=PHI_EPS,
            phi_tol=PHI_TOL,
            rep_tol=REP_TOL,
            hypotheses_commit=HYPOTHESES_COMMIT,
            scores=scores,
            rows=rows,
        ), indent=1) + "\n")


if __name__ == "__main__":
    main()
