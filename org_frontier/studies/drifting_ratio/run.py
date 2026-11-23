"""Fitted formula for the drifting ratio on (1,1,1,3), under input noise.

Run from the repo root: python org_frontier/studies/drifting_ratio/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md (committed before any run of this script).
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

W = (1, 1, 1, 3)
RATES = (0.05, 0.1, 0.2)
# Least-squares coefficients from the six disclosed singleton-winning points in hypotheses.md.
ALPHA = 0.46208785675550357
BETA = 1.07585180342645
GAMMA = -0.32856641898784006
MATCH_TOL = 1e-3
REL_TOL = 1e-6
# (1,1,2,3) quota 3 at e=0.1, from weighted_equivalence (harness control, not a test).
CONTROL = ((1, 1, 2, 3), 3, 0.1, 49.999952735680445)
PREDICTED = {
    0.05: 199.9024781081887,
    0.1: 102.76545826383659,
    0.2: 54.04909345311601,
}
CASES = [(q, e) for q in (3, 4) for e in RATES]
QUICK = [(3, 0.2)]


def law(weights, q):
    """Groups of parties (incl. empty) too small to settle the outcome alone."""
    total, n = sum(weights), len(weights)
    count = 0
    for k in range(n + 1):
        for c in combinations(range(n), k):
            w = sum(weights[i] for i in c)
            count += not (w >= q or w >= total - q + 1)
    return count


def predicted_ratio(R, e):
    pairs = R * (R - 1) / 2
    return ALPHA * pairs / e + (R - BETA) + GAMMA * (R - 1) * e


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
    ratio = (top / whole) if whole > PHI_EPS else None
    R = law(weights, q)
    pred = predicted_ratio(R, e) if weights == W else None
    return dict(
        form=f"{''.join(str(w) for w in weights)}q{q}",
        weights=list(weights), q=q, e=e, whole_phi=whole, top_phi=top,
        ratio=ratio, law=R, predicted=pred, top_state=top_state,
        ties=["".join(labels[i] for i in k) for k in ties],
        full_in_ties=full in ties,
        seconds=round(time.time() - t0, 1),
    )


def show(x):
    ratio = f"{x['ratio']:.6f}" if x["ratio"] is not None else "-"
    pred = f"{x['predicted']:.6f}" if x["predicted"] is not None else "-"
    ties = ",".join(x["ties"]) if len(x["ties"]) <= 6 else f"{len(x['ties'])} subsets"
    print(f"{x['form']:<7} e={x['e']:<4} whole={x['whole_phi']:.6f} top={x['top_phi']:.6f} "
          f"ratio={ratio} pred={pred} law={x['law']} n_ties={len(x['ties'])} ties={ties}")


def rel_ok(a, b, tol=REL_TOL):
    if a is None or b is None:
        return False
    return abs(a - b) <= tol * max(abs(b), 1e-12)


def matches_formula(measured, predicted):
    if measured is None or predicted is None:
        return False
    return abs(measured - predicted) / predicted <= MATCH_TOL


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")

    # Harness control always runs, including --quick.
    cw, cq, ce, cexp = CONTROL
    control = read((cq, ce), weights=cw)
    show(control)
    if not rel_ok(control["ratio"], cexp):
        raise SystemExit(
            f"control (1,1,2,3) q3 e=0.1 ratio={control['ratio']} != {cexp}"
        )
    print(f"C2 (1,1,2,3) quota 3 e=0.1 control ratio={control['ratio']:.12f}: PASS")

    cases = QUICK if args.quick else CASES
    with Pool(min(len(cases), os.cpu_count() or 1)) as pool:
        rows = pool.map(read, cases)
    for x in rows:
        show(x)
    if args.quick:
        return

    g = {(x["q"], x["e"]): x for x in rows}
    scores = {
        "H1": all(
            matches_formula(g[(3, e)]["ratio"], PREDICTED[e])
            and rel_ok(g[(3, e)]["predicted"], PREDICTED[e])
            for e in RATES
        ),
        "H2": all(g[(3, e)]["ties"] == ["SP4"] for e in RATES),
        "H3": all(
            rel_ok(g[(4, e)]["whole_phi"], g[(3, e)]["whole_phi"])
            and rel_ok(g[(4, e)]["top_phi"], g[(3, e)]["top_phi"])
            and rel_ok(g[(4, e)]["ratio"], g[(3, e)]["ratio"])
            and g[(4, e)]["ties"] == ["SP4"]
            for e in RATES
        ),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
        if h == "H1":
            for e in RATES:
                m, p = g[(3, e)]["ratio"], PREDICTED[e]
                err = abs(m - p) / p if (m is not None and p) else None
                print(f"  e={e} measured={m} predicted={p} rel_err={err}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            coefficients={"alpha": ALPHA, "beta": BETA, "gamma": GAMMA, "match_tol": MATCH_TOL},
            predicted=PREDICTED,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            control=control,
            rows=rows,
        ), indent=1) + "\n")


if __name__ == "__main__":
    main()
