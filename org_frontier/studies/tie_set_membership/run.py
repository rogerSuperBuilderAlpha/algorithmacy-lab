"""Quorum membership re-scored on tie sets (all subsets within 1e-9 of the top), quorum_noise_sweep panel.

Run from the repo root: python org_frontier/studies/tie_set_membership/run.py [--quick] [--write]
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

FORMS = (("OR3", 3, 1), ("MAJ3", 3, 2), ("AND3", 3, 3),
         ("ANY4", 4, 1), ("2of4", 4, 2), ("3of4", 4, 3), ("ALL4", 4, 4))
RATES = (0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45)
QUICK = [("ANY4", 4, 1, 0.4), ("MAJ3", 3, 2, 0.05)]
INTERIOR = ("MAJ3", "2of4", "3of4")


def read(case):
    name, n, q, e = case
    labels = labels_for(n)
    tpm = input_tpm(table_of((1,) * n, q), n, e)
    net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
    full = tuple(range(n + 1))
    per_state, whole = [], 0.0
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        whole = max(whole, phis.get(full, 0.0))
        per_state.append((state, phis))
    top = max(max(p.values()) for _, p in per_state)
    ties, states = set(), []
    for state, phis in per_state:
        t = {k for k, v in phis.items() if top > PHI_EPS and top - v <= PHI_EPS}
        if t:
            states.append("".join(map(str, state)))
        ties |= t
    ties = sorted(ties, key=lambda k: (len(k), k))
    parties = sorted({labels[i] for k in ties for i in k if i > 0})
    return dict(form=name, n=n, q=q, e=e, whole_phi=whole, top_phi=top, top_states=states,
                ties=["".join(labels[i] for i in k) for k in ties], full_in_ties=full in ties,
                parties_in_ties=parties, all_parties_in_ties=len(parties) == n)


def show(x):
    ties = ",".join(x["ties"]) if len(x["ties"]) <= 6 else f"{len(x['ties'])} subsets"
    print(f"{x['form']:<5} e={x['e']:<5} whole={x['whole_phi']:.6f} top={x['top_phi']:.6f} "
          f"n_ties={len(x['ties'])} full_in={'Y' if x['full_in_ties'] else 'N'} "
          f"all_parties={'Y' if x['all_parties_in_ties'] else 'N'} ties={ties}")


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
    g = {(x["form"], x["e"]): x for x in rows}
    if not args.quick:
        if abs(g[("MAJ3", 0.2)]["whole_phi"] - 0.036624) > 1e-6 or abs(g[("ANY4", 0.4)]["top_phi"] - 0.009264) > 1e-6:
            raise SystemExit("quorum_noise_sweep control failed")
        print("C2 quorum_noise_sweep controls (MAJ3 0.036624 at 0.2; ANY4 top 0.009264 at 0.4): PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    scores = {
        "H1": not any(g[(f, e)]["full_in_ties"] for f in INTERIOR for e in RATES),
        "H2": all(g[(f, e)]["all_parties_in_ties"] for f in INTERIOR for e in RATES),
        "H3": all(g[(f, 0.4)]["full_in_ties"] for f in ("ANY4", "ALL4")),
        "H4": all(g[(f, e)]["ties"] == [f"SP1P2P3"] for f in ("OR3", "AND3") for e in RATES),
        "H5": all(g[(f, e)]["full_in_ties"] for f in ("ANY4", "ALL4") for e in RATES),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
