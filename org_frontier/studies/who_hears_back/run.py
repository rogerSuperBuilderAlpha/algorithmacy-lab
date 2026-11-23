"""Who hears back: a platform that reads some users and answers some users, read as tie sets.

Run from the repo root: python org_frontier/studies/who_hears_back/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import json
import os
import sys
from functools import reduce
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules, tpm_from_rules  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("P", "A1", "A2", "A3", "A4")
QUICK = (("AND", 4, 4), ("AND", 2, 4), ("AND", 4, 2))


def rules_for(op, r, t):
    def platform(s):
        vals = [s[i] for i in range(1, r + 1)]
        return reduce((lambda a, b: a & b) if op == "AND" else (lambda a, b: a | b), vals)
    rules = [platform]
    for i in range(1, 5):
        rules.append((lambda s: s[0]) if i <= t else (lambda s, i=i: s[i]))
    return rules


def analyse(rules, labels):
    n = len(rules)
    tpm = tpm_from_rules(rules, n)
    net = pyphi.Network(tpm, cm=cm_from_rules(rules, n), node_labels=labels)
    full = tuple(range(n))
    states = []
    for index in reachable_states(tpm, n):
        state = tuple((index >> i) & 1 for i in range(n))
        phis = {tuple(s.node_indices): float(new_big_phi.sia(s).phi)
                for s in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
        top = max(phis.values())
        ties = sorted((k for k, v in phis.items() if top > PHI_EPS and top - v <= PHI_EPS),
                      key=lambda k: (len(k), k))
        states.append(dict(state=list(state), top=top, full_phi=phis.get(full, 0.0),
                           ties=["".join(labels[i] for i in k) for k in ties], full_in=full in ties))
    best = max(states, key=lambda s: s["top"])
    return dict(n_states=len(states), whole_phi=max(s["full_phi"] for s in states), top=best["top"],
                top_state=best["state"], top_ties=best["ties"], full_in_top=best["full_in"], states=states)


def show(x):
    ties = ",".join(x["top_ties"]) if len(x["top_ties"]) <= 6 else f"{len(x['top_ties'])} subsets"
    print(f"{x['op']:<3} r={x['r']} t={x['t']} states={x['n_states']:<2} whole={x['whole_phi']:.6f} "
          f"top={x['top']:.6f} ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    c = analyse([lambda s: s[1], lambda s: s[0] & s[2], lambda s: s[1]], ("W", "S", "C"))
    if abs(c["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit(f"control failed: triad whole Φ {c['whole_phi']}")
    print(f"C1 conjunctive triad whole Φ={c['whole_phi']:.6f}: PASS")
    cases = QUICK if args.quick else ([("AND", r, t) for r in range(1, 5) for t in range(0, 5)]
                                      + [("OR", 4, 4), ("OR", 2, 4)])
    rows = [dict(op=op, r=r, t=t, **analyse(rules_for(op, r, t), LABELS)) for op, r, t in cases]
    g = {(x["op"], x["r"], x["t"]): x for x in rows}
    if abs(g[("AND", 4, 4)]["whole_phi"] - 4.0) > 1e-6:
        raise SystemExit("control failed: AND (4, 4) should equal the 4-party hub, whole Φ 4.0")
    print("C2 AND (4,4) = two_sided_platform all_four, whole Φ 4.0: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    grid = [x for x in rows if x["op"] == "AND"]

    def loop_label(m):
        return "P" + "".join(f"A{i}" for i in range(1, m + 1))
    h2 = [x for x in grid if min(x["r"], x["t"]) >= 1]
    scores = {
        "H1": all((x["whole_phi"] > PHI_EPS) == (x["r"] == 4 and x["t"] == 4) for x in grid),
        "H2": all(abs(x["top"] - min(x["r"], x["t"])) < 1e-6
                  and x["top_ties"] == [loop_label(min(x["r"], x["t"]))] for x in h2),
        "H3": all(all("P" not in s for s in x["top_ties"]) for x in grid if x["t"] == 0),
        "H4": abs(g[("OR", 2, 4)]["top"] - g[("AND", 2, 4)]["top"]) < 1e-6,
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
