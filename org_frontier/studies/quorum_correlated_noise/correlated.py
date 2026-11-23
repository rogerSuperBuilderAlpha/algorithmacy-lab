"""Correlated input noise on three-party quorum hubs (backlog items 1 and 3 of quorum_noise_sweep).

Run from the repo root: python org_frontier/studies/quorum_correlated_noise/correlated.py
--quick runs the CI subset; --write saves results/. Hypotheses are fixed in hypotheses.md.
"""
import argparse
import csv
import json
import math
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

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, classify, tpm_from_rules  # noqa: E402
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, rules_for, table_of,
)

N = 3
FORMS = (("OR3", 1), ("MAJ3", 2), ("AND3", 3))
MODELS = ("indep", "common", "mix")
RATES = (0.0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45)
QUICK = (("MAJ3", "common", 0.2), ("MAJ3", "mix", 0.2), ("OR3", "common", 0.2))


def flip_dist(model, e):
    """Probability of each 3-bit flip mask applied to S's readings; marginal error per reading is e."""
    p = np.zeros(2 ** N)
    full = 2 ** N - 1
    if model == "indep":
        for m in range(2 ** N):
            d = m.bit_count()
            p[m] = e ** d * (1 - e) ** (N - d)
    elif model == "common":
        p[0], p[full] = 1 - e, e
    elif model == "mix":
        q = (1 - math.sqrt(1 - 2 * e)) / 2
        for shared in (0, 1):
            ps = q if shared else 1 - q
            for m in range(2 ** N):
                d = m.bit_count()
                p[m ^ (full if shared else 0)] += ps * q ** d * (1 - q) ** (N - d)
    assert abs(p.sum() - 1) < 1e-12
    marg = sum(p[m] for m in range(2 ** N) if m & 1)
    assert abs(marg - e) < 1e-12, "marginal error rate mismatch"
    return p


def model_tpm(table, model, e):
    p = flip_dist(model, e)
    tpm = np.zeros((2 ** (N + 1), N + 1))
    for state in range(len(tpm)):
        actual = state >> 1
        tpm[state, 0] = sum(p[m] * table[actual ^ m] for m in range(2 ** N))
        tpm[state, 1:] = state & 1
    return tpm


def read(name, quota, model, e):
    labels = labels_for(N)
    table = table_of((1, 1, 1), quota)
    tpm = model_tpm(table, model, e)
    if e == 0:
        assert np.allclose(tpm, tpm_from_rules(rules_for(table, N)), atol=1e-12, rtol=0)
    if model == "indep":
        assert np.allclose(tpm, input_tpm(table, N, e), atol=1e-12, rtol=0)
    cm = cm_numeric(tpm)
    verdict = classify(tpm, cm, labels=labels)
    network = pyphi.Network(tpm, cm=cm, node_labels=labels)
    states = []
    for index in reachable_states(tpm, N + 1):
        state = tuple((index >> i) & 1 for i in range(N + 1))
        cx = new_big_phi.maximal_complex(network, state)
        core, phi = [], 0.0
        if not isinstance(cx, new_big_phi.NullPhiStructure):
            core, phi = [labels[i] for i in cx.node_indices], float(cx.phi)
        states.append(dict(state=list(state), core=core, core_phi=phi))
    top = max((s["core_phi"] for s in states), default=0.0)
    cores = sorted({tuple(s["core"]) for s in states
                    if s["core_phi"] > PHI_EPS and abs(s["core_phi"] - top) <= PHI_EPS})
    full = bool(cores) and all(set(c) == set(labels) for c in cores)
    levels = sorted({round(float(v), 12) for v in tpm[:, 0]})
    return dict(form=name, model=model, e=e, whole_phi=float(verdict.max_phi), max_core_phi=top,
                max_cores=cores, full_group_core=full, s_levels=levels, cores_by_state=states)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true", help="CI subset (3 cases)")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    if args.quick:
        cases = [(f, dict(FORMS)[f], m, e) for f, m, e in QUICK]
    else:
        cases = [(f, q, m, e) for f, q in FORMS for m in MODELS for e in RATES]
    rows = [read(*c) for c in cases]
    print("C2 deterministic identity, indep = probe 464 input_tpm, marginal error = e: PASS")
    for r in rows:
        print(f"{r['form']:<5} {r['model']:<6} e={r['e']:<5} whole={r['whole_phi']:.6f} "
              f"core_phi={r['max_core_phi']:.6f} full={'Y' if r['full_group_core'] else 'N'} "
              f"S_levels={len(r['s_levels'])}")
    if args.quick:
        return
    g = {(r["form"], r["model"], r["e"]): r for r in rows}
    nz = RATES[1:]
    maj_pos = [r for r in rows if r["form"] == "MAJ3" and r["whole_phi"] > PHI_EPS]
    scores = {
        "H1": all(g[("MAJ3", "common", e)]["whole_phi"] <= PHI_EPS for e in nz),
        "H2": all(g[("MAJ3", "mix", e)]["whole_phi"] > PHI_EPS for e in nz),
        "H3": all(g[(f, m, e)]["full_group_core"] for f in ("OR3", "AND3")
                  for m in ("common", "mix") for e in nz),
        "H4": not any(g[("MAJ3", m, e)]["full_group_core"] for m in MODELS for e in nz),
        "H5": all(abs(r["max_core_phi"] / r["whole_phi"] - 4) <= 4e-6 for r in maj_pos),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        with open(out / "results.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["form", "model", "e", "whole_phi", "max_core_phi", "full_group_core",
                        "s_levels", "max_cores"])
            for r in rows:
                w.writerow([r["form"], r["model"], r["e"], f"{r['whole_phi']:.9f}",
                            f"{r['max_core_phi']:.9f}", r["full_group_core"], len(r["s_levels"]),
                            "|".join(",".join(c) for c in r["max_cores"])])
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, rates=RATES,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
