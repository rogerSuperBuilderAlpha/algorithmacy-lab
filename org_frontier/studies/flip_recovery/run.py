"""Flip recovery on deterministic quorum hubs: steps back to an attractor after one party's bit flips.

Joins the committed Φ of memory_rules and update_order_quorum. Run from the repo root:
python org_frontier/studies/flip_recovery/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np  # noqa: E402
from scipy.stats import mannwhitneyu, spearmanr  # noqa: E402

from org_frontier.classifier.classifier import PHI_EPS, tpm_from_rules  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import rules_for, table_of  # noqa: E402
from org_frontier.studies.memory_rules.run import memory_rules  # noqa: E402
from org_frontier.studies.update_order_quorum.run import order_tpm  # noqa: E402

N = 3
NN = N + 1
QUOTA = {"OR3": 1, "MAJ3": 2, "AND3": 3}
STUDIES = ROOT / "org_frontier" / "studies"


def step_map(tpm):
    return [sum(int(round(tpm[s, j])) << j for j in range(NN)) for s in range(2 ** NN)]


def attractors(f):
    """Map each state to (attractor id, transient length)."""
    on_cycle, att_of, trans = {}, {}, {}
    for s in range(len(f)):
        seen, x = [], s
        while x not in seen:
            seen.append(x)
            x = f[x]
        cycle = seen[seen.index(x):]
        aid = min(cycle)
        for c in cycle:
            on_cycle[c] = aid
        att_of[s] = aid
        trans[s] = seen.index(x)
    return on_cycle, att_of, trans


def dynamics(tpm):
    f = step_map(tpm)
    on_cycle, att_of, trans = attractors(f)
    rec, same = [], []
    for s, aid in on_cycle.items():
        for i in range(1, NN):
            y = s ^ (1 << i)
            rec.append(trans[y])
            same.append(att_of[y] == aid)
    return dict(n_attractors=len(set(on_cycle.values())), n_attractor_states=len(on_cycle),
                recovery=float(np.mean(rec)), same_rate=float(np.mean(same)),
                transient=float(np.mean([trans[s] for s in range(len(f))])))


def panel():
    rows = []
    mem = json.loads((STUDIES / "memory_rules" / "results" / "results.json").read_text())["rows"]
    for r in mem:
        tpm = np.asarray(tpm_from_rules(memory_rules(QUOTA[r["form"]], r["party"], r["mediator"]), n=NN))
        rows.append(dict(family="memory_rules", case=f"{r['form']}/{r['party']}/{r['mediator']}",
                         whole_phi=r["whole_phi"], top=r["top"], **dynamics(tpm)))
    order = json.loads((STUDIES / "update_order_quorum" / "results" / "results.json").read_text())["rows"]
    for r in order:
        o = tuple(0 if lab == "S" else int(lab[1:]) for lab in r["order_labels"])
        tpm = order_tpm(rules_for(table_of((1, 1, 1), QUOTA[r["form"]]), N), o)
        rows.append(dict(family="update_order_quorum", case=f"{r['form']}/{'-'.join(r['order_labels'])}",
                         whole_phi=r["whole_phi"], top=r["top"], **dynamics(tpm)))
    return rows


def show(x):
    print(f"{x['case']:<22} whole={x['whole_phi']:.6f} top={x['top']:.6f} attractors={x['n_attractors']} "
          f"recovery={x['recovery']:.4f} same={x['same_rate']:.4f} transient={x['transient']:.4f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    # control: the synchronous OR3 hub has two fixed points (all 0, all 1) and a 2-cycle.
    sync = dynamics(np.asarray(tpm_from_rules(rules_for(table_of((1, 1, 1), 1), N)), dtype=float))
    print(f"C1 synchronous OR3 hub: attractors={sync['n_attractors']} states_on_attractors="
          f"{sync['n_attractor_states']}")
    rows = panel()
    if args.quick:
        for x in rows:
            if x["case"] in ("OR3/copy/plain", "OR3/and/plain", "OR3/S-P1-P2-P3"):
                show(x)
        return
    for x in rows:
        show(x)
    mem = [x for x in rows if x["family"] == "memory_rules"]
    bound = [x for x in mem if x["whole_phi"] > PHI_EPS]
    split = [x for x in mem if x["whole_phi"] <= PHI_EPS]

    def mw(key, alt):
        return float(mannwhitneyu([x[key] for x in bound], [x[key] for x in split], alternative=alt).pvalue)

    tests = dict(
        n_bound=len(bound), n_split=len(split),
        recovery_median=(float(np.median([x["recovery"] for x in bound])),
                         float(np.median([x["recovery"] for x in split]))),
        same_median=(float(np.median([x["same_rate"] for x in bound])),
                     float(np.median([x["same_rate"] for x in split]))),
        transient_median=(float(np.median([x["transient"] for x in bound])),
                          float(np.median([x["transient"] for x in split]))),
        p_recovery_less=mw("recovery", "less"),
        p_same_greater=mw("same_rate", "greater"),
        p_transient_two=mw("transient", "two-sided"),
        # exploratory, not pre-registered
        attractors_median=(float(np.median([x["n_attractors"] for x in bound])),
                           float(np.median([x["n_attractors"] for x in split]))),
        p_attractors_two=mw("n_attractors", "two-sided"),
    )
    rho, p = spearmanr([x["recovery"] for x in rows], [x["top"] for x in rows])
    tests.update(spearman_recovery_top=float(rho), spearman_p=float(p))
    for k, v in tests.items():
        print(f"{k}: {v}")
    scores = {
        "H1": tests["p_recovery_less"] < 0.05,
        "H2": tests["p_same_greater"] < 0.05,
        "H3": tests["spearman_recovery_top"] < 0 and tests["spearman_p"] < 0.05,
        "H4": tests["p_transient_two"] >= 0.05,
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            control=sync, tests=tests,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
