"""Test a candidate split for when the party-noise factor holds.

Run from the repo root: python org_frontier/studies/majority_factor_split/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md before this script ran.
"""
import argparse
import json
import os
import sys
from fractions import Fraction
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

PHI0 = {
    ("MAJ3", 0.05): 0.015760636493609655,
    ("MAJ3", 0.2): 0.03662371603136496,
    ("2of4", 0.05): 0.01814390272790656,
    ("2of4", 0.2): 0.03582202453611982,
    ("3of4", 0.05): 0.018143902727906575,
    ("3of4", 0.2): 0.0358220245361198,
}

PREDICTED = {
    ("MAJ3", 0.05, 0.3): 0.014610535992724626,
    ("MAJ3", 0.05, 0.4): 0.012158205295070305,
    ("MAJ3", 0.2, 0.3): 0.03395117459123833,
    ("MAJ3", 0.2, 0.4): 0.028252580938481542,
    ("2of4", 0.05, 0.3): 0.017551776974094945,
    ("2of4", 0.05, 0.4): 0.015151094030519913,
    ("2of4", 0.2, 0.3): 0.034652973775674334,
    ("2of4", 0.2, 0.4): 0.029913236983770162,
    ("3of4", 0.05, 0.3): 0.01755177697409496,
    ("3of4", 0.05, 0.4): 0.015151094030519924,
    ("3of4", 0.2, 0.3): 0.03465297377567431,
    ("3of4", 0.2, 0.4): 0.029913236983770145,
}

# claim True = match the factor, False = miss it
CLAIM = {k: (k[2] == 0.3 or k[0] == "MAJ3") for k in PREDICTED}

FACTOR = {
    (3, 0.3): Fraction(343, 370),
    (3, 0.4): Fraction(27, 35),
    (4, 0.3): Fraction(2401, 2482),
    (4, 0.4): Fraction(81, 97),
}

# (form, weights, quota, eta, eps)
H12_CASES = [
    ("MAJ3", (1, 1, 1), 2, 0.05, 0.3),
    ("MAJ3", (1, 1, 1), 2, 0.05, 0.4),
    ("MAJ3", (1, 1, 1), 2, 0.2, 0.3),
    ("MAJ3", (1, 1, 1), 2, 0.2, 0.4),
    ("2of4", (1, 1, 1, 1), 2, 0.05, 0.3),
    ("2of4", (1, 1, 1, 1), 2, 0.05, 0.4),
    ("2of4", (1, 1, 1, 1), 2, 0.2, 0.3),
    ("2of4", (1, 1, 1, 1), 2, 0.2, 0.4),
    ("3of4", (1, 1, 1, 1), 3, 0.05, 0.3),
    ("3of4", (1, 1, 1, 1), 3, 0.05, 0.4),
    ("3of4", (1, 1, 1, 1), 3, 0.2, 0.3),
    ("3of4", (1, 1, 1, 1), 3, 0.2, 0.4),
]
H1113_CASES = [
    ("1113q3", (1, 1, 1, 3), 3, 0.2, 0.0),
    ("1113q3", (1, 1, 1, 3), 3, 0.2, 0.3),
    ("1113q3", (1, 1, 1, 3), 3, 0.2, 0.4),
]
CASES = H12_CASES + H1113_CASES
QUICK = [
    ("MAJ3", (1, 1, 1), 2, 0.2, 0.3),
    ("2of4", (1, 1, 1, 1), 2, 0.2, 0.4),
]

REL_TOL = 1e-10
HYPOTHESES_COMMIT = "8ff4fa78b52d0d10ae343b5eaba90bce8e02064c"


def matches(measured, predicted, phi0):
    if phi0 <= 1e-9:
        return measured <= 1e-9
    return abs(measured - predicted) / phi0 <= REL_TOL


def whole(case):
    name, w, q, eta, eps = case
    n = len(w)
    tpm = noisy_tpm(w, q, eta, eps)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels_for(n))
    vals = []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        vals.append(float(new_big_phi.sia(pyphi.Subsystem(net, state, tuple(range(n + 1)))).phi))
    return dict(form=name, weights=list(w), q=q, n=n, eta=eta, eps=eps,
                n_states=len(vals), whole_phi=max(vals) if vals else 0.0)


def show(x, pred=None, rel=None, claim=None):
    extra = ""
    if pred is not None:
        extra = f" pred={pred:.15f} rel_err={rel:.3e}"
        if claim is not None:
            got = "match" if (rel is not None and (
                (x["whole_phi"] <= 1e-9 and pred <= 1e-9) or (rel <= REL_TOL)
            )) else "miss"
            extra += f" claim={('match' if claim else 'miss')} got={got}"
    print(f"{x['form']:<7} eta={x['eta']:<4} eps={x['eps']:<4} states={x['n_states']} "
          f"whole={x['whole_phi']:.6f}{extra}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else CASES
    with Pool(os.cpu_count() or 1) as pool:
        rows = pool.map(whole, cases)
    if args.quick:
        for x in rows:
            show(x)
        return
    by = {(x["form"], x["eta"], x["eps"]): x for x in rows}
    detail = []
    h1_ok = True
    h2_ok = True
    for form, w, q, eta, eps in H12_CASES:
        x = by[(form, eta, eps)]
        pred = PREDICTED[(form, eta, eps)]
        phi0 = PHI0[(form, eta)]
        rel = abs(x["whole_phi"] - pred) / phi0 if phi0 > 1e-9 else 0.0
        did_match = matches(x["whole_phi"], pred, phi0)
        claim = CLAIM[(form, eta, eps)]
        agreed = did_match is claim
        if eps == 0.3:
            h1_ok = h1_ok and agreed
        else:
            h2_ok = h2_ok and agreed
        detail.append(dict(form=form, eta=eta, eps=eps, phi0=phi0, predicted=pred,
                           measured=x["whole_phi"], rel_err=rel, matched=did_match,
                           claim_match=claim, agreed=agreed))
        show(x, pred, rel, claim)
    phi0_1113 = by[("1113q3", 0.2, 0.0)]["whole_phi"]
    show(by[("1113q3", 0.2, 0.0)])
    for eps in (0.3, 0.4):
        x = by[("1113q3", 0.2, eps)]
        fac = FACTOR[(4, eps)]
        pred = 0.0 if phi0_1113 <= 1e-9 else phi0_1113 * float(fac)
        rel = abs(x["whole_phi"] - pred) / phi0_1113 if phi0_1113 > 1e-9 else 0.0
        did_match = matches(x["whole_phi"], pred, phi0_1113)
        # claim: miss at both 0.3 and 0.4
        agreed = (not did_match)
        if eps == 0.3:
            h1_ok = h1_ok and agreed
        else:
            h2_ok = h2_ok and agreed
        detail.append(dict(form="1113q3", eta=0.2, eps=eps, phi0=phi0_1113, predicted=pred,
                           measured=x["whole_phi"], rel_err=rel, matched=did_match,
                           claim_match=False, agreed=agreed))
        show(x, pred, rel, False)
    scores = {
        "H1": "SUPPORTED" if h1_ok else "REFUTED",
        "H2": "SUPPORTED" if h2_ok else "REFUTED",
    }
    for k, v in scores.items():
        print(f"{k}: {v}")
    if args.write:
        out = Path(__file__).parent / "results" / "results.json"
        out.parent.mkdir(exist_ok=True)
        out.write_text(json.dumps(dict(
            pyphi=version("pyphi"),
            phi_eps=PHI_EPS,
            rel_tol=REL_TOL,
            hypotheses_commit=HYPOTHESES_COMMIT,
            scores=scores,
            detail=detail,
            rows=rows,
        ), indent=1) + "\n")


if __name__ == "__main__":
    main()
