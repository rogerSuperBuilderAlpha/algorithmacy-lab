"""Off-platform deals: buyer–seller links that bypass a two-sided platform, read as tie sets.

Run from the repo root: python org_frontier/studies/off_platform_deals/run.py [--quick] [--write]
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

L5 = ("P", "B1", "B2", "S1", "S2")
L6 = ("P", "B1", "B2", "B3", "S1", "S2")


def copy(s):
    return s[0]


def side_match(s):
    return (s[1] | s[2]) & (s[3] | s[4])


L7 = ("P", "B1", "B2", "B3", "B4", "S1", "S2")
FORMS = {
    "side_link_and": (L5, [side_match, lambda s: s[0] & s[2], lambda s: s[0] & s[1],
                           lambda s: s[0] & s[4], lambda s: s[0] & s[3]]),
    "cross_and": (L5, [side_match, lambda s: s[0] & s[3], lambda s: s[0] & s[4],
                       lambda s: s[0] & s[1], lambda s: s[0] & s[2]]),
    "cross_or": (L5, [side_match, lambda s: s[0] | s[3], lambda s: s[0] | s[4],
                      lambda s: s[0] | s[1], lambda s: s[0] | s[2]]),
    "one_pair_off": (L5, [side_match, lambda s: s[3], copy, lambda s: s[1], copy]),
    "one_pair_and": (L5, [side_match, lambda s: s[0] & s[3], copy, lambda s: s[0] & s[1], copy]),
    "strict_buyers_4": (L7, [lambda s: (s[1] & s[2] & s[3] & s[4]) & (s[5] | s[6])] + [copy] * 6),
}
QUICK = ("side_link_and", "cross_and", "one_pair_off")


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
    print(f"{x['form']:<16} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
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
    rows = []
    for name in (QUICK if args.quick else FORMS):
        labels, rules = FORMS[name]
        rows.append(dict(form=name, **analyse(rules, labels)))
    g = {x["form"]: x for x in rows}
    if abs(g["side_link_and"]["whole_phi"] - 0.830075) > 1e-6:
        raise SystemExit("control failed: asymmetric_sides side_link_and whole Φ should be 0.830075")
    print("C2 asymmetric_sides side_link_and whole 0.830075: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    scores = {
        "H1": g["cross_and"]["whole_phi"] > PHI_EPS and set(g["cross_and"]["top_ties"]) == {"B1S1", "B2S2"},
        "H2": all("P" in t for t in g["cross_or"]["top_ties"]),
        "H3": (all("P" not in t for t in g["one_pair_off"]["top_ties"])
               and "B1S1" in g["one_pair_off"]["top_ties"]),
        "H4": g["one_pair_and"]["whole_phi"] > PHI_EPS,
        "H5": (abs(g["strict_buyers_4"]["top"] - 4.0) < 1e-6
               and g["strict_buyers_4"]["top_ties"] == ["PB1B2B3B4"]),
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
