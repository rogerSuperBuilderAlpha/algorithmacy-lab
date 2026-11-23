"""Partial synchrony on quorum hubs: members update in ordered blocks (all 75 ordered partitions).

Run from the repo root: python org_frontier/studies/partial_sync_quorum/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import itertools
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

from org_frontier.classifier.classifier import PHI_EPS, tpm_from_rules  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    gate_c1, labels_for, rules_for, table_of,
)
from org_frontier.studies.update_order_quorum.run import order_tpm, phi_read  # noqa: E402

pyphi.config.PROGRESS_BARS = False
N = 3
NN = N + 1
FORMS = (("OR3", 1), ("MAJ3", 2), ("AND3", 3))
KNOWN = {"OR3": 3.0, "MAJ3": 0.0, "AND3": 3.0}
LABELS = labels_for(N)


def ordered_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    for k in range(1, len(items) + 1):
        for block in itertools.combinations(items, k):
            rest = [x for x in items if x not in block]
            for tail in ordered_partitions(rest):
                yield [block] + tail


SCHEDULES = tuple(tuple(p) for p in ordered_partitions(range(NN)))
QUICK_NAMES = ("S|P1P2P3", "P1P2P3|S", "SP1|P2P3")


def name(schedule):
    return "|".join("".join(LABELS[i] for i in b) for b in schedule)


def block_tpm(rules, schedule):
    tpm = np.zeros((2 ** NN, NN))
    for s in range(2 ** NN):
        x = [(s >> i) & 1 for i in range(NN)]
        for block in schedule:
            new = {j: int(rules[j](tuple(x))) for j in block}
            for j, v in new.items():
                x[j] = v
        tpm[s] = x
    return tpm


def read(form, quota, schedule):
    rules = rules_for(table_of((1, 1, 1), quota), N)
    tpm = block_tpm(rules, schedule)
    if len(schedule) == 1:
        assert np.allclose(tpm, tpm_from_rules(rules), atol=1e-12, rtol=0)
    if len(schedule) == NN:
        assert np.allclose(tpm, order_tpm(rules, tuple(b[0] for b in schedule)), atol=1e-12, rtol=0)
    return dict(form=form, schedule=name(schedule), n_blocks=len(schedule), **phi_read(tpm, LABELS))


def show(x):
    ties = ",".join(x["top_ties"]) if len(x["top_ties"]) <= 6 else f"{len(x['top_ties'])} subsets"
    print(f"{x['form']:<5} sched={x['schedule']:<14} blocks={x['n_blocks']} states={x['n_states']:<2} "
          f"whole={x['whole_phi']:.6f} top={x['top']:.6f} full_in_top={'Y' if x['full_in_top'] else 'N'} "
          f"ties={ties or '-'}", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    assert len(SCHEDULES) == 75
    sync = {f: read(f, q, SCHEDULES[0] if len(SCHEDULES[0]) == 1 else ((0, 1, 2, 3),)) for f, q in FORMS}
    for f, x in sync.items():
        if abs(x["whole_phi"] - KNOWN[f]) > 1e-6:
            raise SystemExit(f"synchronous control failed for {f}")
    print("C2 75 schedules, synchronous and one-at-a-time controls: PASS")
    if args.quick:
        rows = [read("OR3", 1, s) for s in SCHEDULES if name(s) in QUICK_NAMES]
    else:
        rows = [read(f, q, s) for f, q in FORMS for s in SCHEDULES]
    for x in rows:
        show(x)
    if args.quick:
        return
    pos = {f: [x["schedule"] for x in rows if x["form"] == f and x["whole_phi"] > PHI_EPS] for f, _ in FORMS}
    print("schedules with whole Phi > 0:", pos)
    g = {(x["form"], x["schedule"]): x for x in rows}
    h4 = g[("OR3", "S|P1P2P3")]
    scores = {
        "H1": pos["OR3"] == ["SP1P2P3"],
        "H2": pos["AND3"] == ["SP1P2P3"],
        "H3": pos["MAJ3"] == [],
        "H4": h4["top_ties"] == ["P1P2P3"] and h4["top"] > 3.0 + PHI_EPS,
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, positive_schedules=pos,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
