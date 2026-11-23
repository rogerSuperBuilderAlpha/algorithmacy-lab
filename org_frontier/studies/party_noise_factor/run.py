"""Test the post-hoc party-noise factor on new cases.

Run from the repo root: python org_frontier/studies/party_noise_factor/run.py [--quick] [--write]
Hypotheses were committed in 7d33c987418d1f5014eda8a19a9d5c5b1b16176e before this script ran.
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

# Committed Φ(η, 0) from hypotheses.md (weighted_swap_symmetry and five_six_node_quorum_ties).
PHI0 = {
    ("1112q2", 0.05): 0.014972604668929156,
    ("1112q2", 0.2): 0.02929897282509204,
    ("1112q3", 0.05): 0.0038968042400468897,
    ("1112q3", 0.2): 0.008896660359373351,
    ("1112q4", 0.05): 0.014972604668929098,
    ("1112q4", 0.2): 0.029298972825091963,
    ("1122q3", 0.05): 0.015392814378989862,
    ("1122q3", 0.2): 0.03247030028231149,
    ("3of5", 0.1): 0.0017702875158729103,
    ("3of5", 0.2): 0.004260017707949414,
}

# Pre-registered predicted whole Φ, computed as committed Φ(η, 0) times the exact factor.
PREDICTED = {
    ("1112q2", 0.05, 0.3): 0.014483974137831951,
    ("1112q2", 0.05, 0.4): 0.012502896682301666,
    ("1112q2", 0.2, 0.3): 0.02834280167326591,
    ("1112q2", 0.2, 0.4): 0.024466152565283044,
    ("1112q3", 0.05, 0.3): 0.003769632143574773,
    ("1112q3", 0.05, 0.4): 0.003254032406637094,
    ("1112q3", 0.2, 0.3): 0.00860631809945827,
    ("1112q3", 0.2, 0.4): 0.007429169990816923,
    ("1112q4", 0.05, 0.3): 0.014483974137831895,
    ("1112q4", 0.05, 0.4): 0.012502896682301618,
    ("1112q4", 0.2, 0.3): 0.028342801673265836,
    ("1112q4", 0.2, 0.4): 0.02446615256528298,
    ("1122q3", 0.05, 0.3): 0.014890470315856026,
    ("1122q3", 0.05, 0.4): 0.012853793450496689,
    ("1122q3", 0.2, 0.3): 0.03141063294836015,
    ("1122q3", 0.2, 0.4): 0.02711437446254877,
    ("3of5", 0.1, 0.3): 0.001745057025177476,
    ("3of5", 0.1, 0.4): 0.00156429042311679,
    ("3of5", 0.2, 0.3): 0.004199303086070716,
    ("3of5", 0.2, 0.4): 0.003764306556478937,
}

FACTOR = {
    (4, 0.3): Fraction(2401, 2482),
    (4, 0.4): Fraction(81, 97),
    (5, 0.3): Fraction(16807, 17050),
    (5, 0.4): Fraction(243, 275),
}

# (form, weights, quota, eta, eps) — H1 cases, plus H2 cases including ε = 0 baselines.
H1_CASES = [
    ("1112q2", (1, 1, 1, 2), 2, 0.05, 0.3),
    ("1112q2", (1, 1, 1, 2), 2, 0.05, 0.4),
    ("1112q2", (1, 1, 1, 2), 2, 0.2, 0.3),
    ("1112q2", (1, 1, 1, 2), 2, 0.2, 0.4),
    ("1112q3", (1, 1, 1, 2), 3, 0.05, 0.3),
    ("1112q3", (1, 1, 1, 2), 3, 0.05, 0.4),
    ("1112q3", (1, 1, 1, 2), 3, 0.2, 0.3),
    ("1112q3", (1, 1, 1, 2), 3, 0.2, 0.4),
    ("1112q4", (1, 1, 1, 2), 4, 0.05, 0.3),
    ("1112q4", (1, 1, 1, 2), 4, 0.05, 0.4),
    ("1112q4", (1, 1, 1, 2), 4, 0.2, 0.3),
    ("1112q4", (1, 1, 1, 2), 4, 0.2, 0.4),
    ("1122q3", (1, 1, 2, 2), 3, 0.05, 0.3),
    ("1122q3", (1, 1, 2, 2), 3, 0.05, 0.4),
    ("1122q3", (1, 1, 2, 2), 3, 0.2, 0.3),
    ("1122q3", (1, 1, 2, 2), 3, 0.2, 0.4),
    ("3of5", (1, 1, 1, 1, 1), 3, 0.1, 0.3),
    ("3of5", (1, 1, 1, 1, 1), 3, 0.1, 0.4),
    ("3of5", (1, 1, 1, 1, 1), 3, 0.2, 0.3),
    ("3of5", (1, 1, 1, 1, 1), 3, 0.2, 0.4),
]
H2_CASES = [
    ("2of5", (1, 1, 1, 1, 1), 2, 0.2, 0.0),
    ("2of5", (1, 1, 1, 1, 1), 2, 0.2, 0.3),
    ("2of5", (1, 1, 1, 1, 1), 2, 0.2, 0.4),
    ("4of5", (1, 1, 1, 1, 1), 4, 0.2, 0.0),
    ("4of5", (1, 1, 1, 1, 1), 4, 0.2, 0.3),
    ("4of5", (1, 1, 1, 1, 1), 4, 0.2, 0.4),
]
CASES = H1_CASES + H2_CASES
QUICK = [
    ("1112q3", (1, 1, 1, 2), 3, 0.2, 0.3),
    ("1122q3", (1, 1, 2, 2), 3, 0.2, 0.4),
]

REL_TOL = 1e-10
HYPOTHESES_COMMIT = "7d33c987418d1f5014eda8a19a9d5c5b1b16176e"


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


def show(x, pred=None, rel=None):
    extra = ""
    if pred is not None:
        extra = f" pred={pred:.15f} rel_err={rel:.3e}" if rel is not None else f" pred={pred:.15f}"
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
    h1_rows = []
    h1_ok = True
    for form, w, q, eta, eps in H1_CASES:
        x = by[(form, eta, eps)]
        pred = PREDICTED[(form, eta, eps)]
        phi0 = PHI0[(form, eta)]
        rel = abs(x["whole_phi"] - pred) / phi0 if phi0 > 1e-9 else 0.0
        ok = matches(x["whole_phi"], pred, phi0)
        h1_ok = h1_ok and ok
        h1_rows.append(dict(form=form, eta=eta, eps=eps, phi0=phi0, predicted=pred,
                            measured=x["whole_phi"], rel_err=rel, match=ok))
        show(x, pred, rel)
    h2_rows = []
    h2_ok = True
    for form in ("2of5", "4of5"):
        phi0 = by[(form, 0.2, 0.0)]["whole_phi"]
        show(by[(form, 0.2, 0.0)])
        for eps in (0.3, 0.4):
            x = by[(form, 0.2, eps)]
            fac = FACTOR[(5, eps)]
            pred = 0.0 if phi0 <= 1e-9 else phi0 * float(fac)
            rel = abs(x["whole_phi"] - pred) / phi0 if phi0 > 1e-9 else 0.0
            ok = matches(x["whole_phi"], pred, phi0)
            h2_ok = h2_ok and ok
            h2_rows.append(dict(form=form, eta=0.2, eps=eps, phi0=phi0, factor=float(fac),
                                predicted=pred, measured=x["whole_phi"], rel_err=rel, match=ok))
            show(x, pred, rel)
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
            h1=h1_rows,
            h2=h2_rows,
            rows=rows,
        ), indent=1) + "\n")


if __name__ == "__main__":
    main()
