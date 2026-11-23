"""Onset of the high-noise tie on extreme quorums (OR3, ANY4), eta 0.31-0.39.

Run from the repo root: python org_frontier/studies/high_noise_tie_onset/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md. Reuses tie_set_membership's per-case reader.
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

from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import cm_numeric, labels_for, table_of  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import gate_c1  # noqa: E402
from org_frontier.studies.tie_set_membership.run import read  # noqa: E402

FORMS = (("OR3", 3, 1), ("ANY4", 4, 1))
RATES = tuple(round(0.31 + 0.01 * i, 2) for i in range(9))
QUICK = [("OR3", 3, 1, 0.35), ("OR3", 3, 1, 0.36)]


def full_phi_at(n, e, state):
    """Raw full-group phi PyPhi returns at one state (descriptive; may be negative)."""
    tpm = input_tpm(table_of((1,) * n, 1), n, e)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels_for(n))
    return float(new_big_phi.sia(pyphi.Subsystem(net, state, tuple(range(n + 1)))).phi)


def all_with_s(n):
    return 2 ** n - 1


def show(x):
    ties = ",".join(x["ties"]) if len(x["ties"]) <= 3 else f"{len(x['ties'])} subsets"
    print(f"{x['form']:<4} e={x['e']:<4} whole={x['whole_phi']:.6f} top={x['top_phi']:.6f} "
          f"n_ties={len(x['ties'])} top_states={','.join(x['top_states'])} ties={ties}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    cases = QUICK if args.quick else [(f, n, q, e) for f, n, q in FORMS for e in RATES]
    with Pool(os.cpu_count() or 1) as pool:
        rows = pool.map(read, cases)
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["form"], x["e"]): x for x in rows}
    switch, ok1, ok3 = {}, True, True
    for f, n, _ in FORMS:
        kind = ["unique" if g[(f, e)]["ties"] == ["S" + "".join(f"P{i}" for i in range(1, n + 1))]
                else "all_S" if len(g[(f, e)]["ties"]) == all_with_s(n) else "other" for e in RATES]
        first = next((i for i, k in enumerate(kind) if k == "all_S"), None)
        ok1 &= first is not None and all(k == "unique" for k in kind[:first]) and all(k == "all_S" for k in kind[first:])
        switch[f] = RATES[first] if first is not None else None
        if first:
            ok3 &= g[(f, RATES[first - 1])]["top_states"] == ["0" * (n + 1)] and \
                ("0" + "1" * n) in g[(f, RATES[first])]["top_states"]
        print(f"{f}: kinds={kind} switch={switch[f]}")
    raw = {}
    for f, n, _ in FORMS:
        for e in RATES:
            z, o = full_phi_at(n, e, (0,) * (n + 1)), full_phi_at(n, e, (0,) + (1,) * n)
            raw[f"{f} {e}"] = dict(all_zero=z, s0_parties1=o)
            print(f"{f:<4} e={e:<4} raw full-group phi: all-zero={z:.6f} S=0,parties=1: {o:.6f}")
    scores = {"H1": ok1, "H2": ok1 and switch["OR3"] == switch["ANY4"], "H3": ok1 and ok3}
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, switch=switch, raw_full_phi=raw,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
