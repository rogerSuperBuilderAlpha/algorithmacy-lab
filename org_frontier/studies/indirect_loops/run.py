"""Indirect loops: answered parties pass the platform's decision to the parties it reads; tie sets.

Run from the repo root: python org_frontier/studies/indirect_loops/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
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

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules, tpm_from_rules  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("P", "A1", "A2", "A3", "A4")
P_AND = lambda s: s[1] & s[2]  # noqa: E731
P_OR = lambda s: s[1] | s[2]  # noqa: E731
CP = lambda s: s[0]  # noqa: E731


def keep(i):
    return lambda s: s[i]


def take(j):
    return lambda s: s[j]


FORMS = {
    "direct": [P_AND, CP, CP, keep(3), keep(4)],
    "disjoint_and": [P_AND, keep(1), keep(2), CP, CP],
    "disjoint_or": [P_OR, keep(1), keep(2), CP, CP],
    "relay_both": [P_AND, take(3), take(4), CP, CP],
    "relay_one": [P_AND, take(3), keep(2), CP, CP],
    "relay_cross": [P_AND, take(4), take(3), CP, CP],
}
QUICK = ("direct", "relay_both", "relay_one")


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
    print(f"{x['form']:<13} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"full_in_top={'Y' if x['full_in_top'] else 'N'} ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    c = analyse([lambda s: s[1], lambda s: s[0] & s[2], lambda s: s[1]], ("W", "S", "C"))
    if abs(c["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit(f"control failed: triad whole Φ {c['whole_phi']}")
    print(f"C1 conjunctive triad whole Φ={c['whole_phi']:.6f}: PASS")
    rows = [dict(form=f, **analyse(FORMS[f], LABELS)) for f in (QUICK if args.quick else FORMS)]
    g = {x["form"]: x for x in rows}
    d = g["direct"]
    if abs(d["top"] - 2.0) > 1e-6 or d["top_ties"] != ["PA1", "PA2", "PA1A2"]:
        raise SystemExit("control failed: direct should reproduce who_hears_back (2, 2)")
    print("C2 direct = who_hears_back r=2 t=2 (top 2.0, ties PA1,PA2,PA1A2): PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    scores = {
        "H1": all("P" not in t for f in ("disjoint_and", "disjoint_or") for t in g[f]["top_ties"]),
        "H2": g["relay_both"]["whole_phi"] > PHI_EPS and g["relay_both"]["full_in_top"],
        "H3": bool(g["relay_one"]["top_ties"]) and all(
            "P" in t and "A1" in t and "A3" in t for t in g["relay_one"]["top_ties"]),
        "H4": (abs(g["relay_cross"]["whole_phi"] - g["relay_both"]["whole_phi"]) <= PHI_EPS
               and abs(g["relay_cross"]["top"] - g["relay_both"]["top"]) <= PHI_EPS),
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
