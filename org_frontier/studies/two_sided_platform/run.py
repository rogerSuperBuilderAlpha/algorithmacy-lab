"""Two-sided platform: two buyers and two sellers around one mediator, read as tie sets.

Run from the repo root: python org_frontier/studies/two_sided_platform/run.py [--quick] [--write]
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

LABELS = ("P", "B1", "B2", "S1", "S2")
P, B1, B2, S1, S2 = range(5)
FORMS = {
    "all_four": lambda s: s[B1] & s[B2] & s[S1] & s[S2],
    "any_one": lambda s: s[B1] | s[B2] | s[S1] | s[S2],
    "side_match": lambda s: (s[B1] | s[B2]) & (s[S1] | s[S2]),
    "fixed_pairs": lambda s: (s[B1] & s[S1]) | (s[B2] & s[S2]),
    "one_per_side": lambda s: (s[B1] ^ s[B2]) & (s[S1] ^ s[S2]),
    "both_sides_full": lambda s: (s[B1] & s[B2]) | (s[S1] & s[S2]),
}
QUICK = ("all_four", "side_match", "fixed_pairs")


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
                top_ties=best["ties"], full_in_top=best["full_in"], states=states)


def form(name):
    mediator = FORMS[name]
    rules = [mediator] + [lambda s: s[P]] * 4
    return dict(form=name, **analyse(rules, LABELS))


def control():
    rules = [lambda s: s[1], lambda s: s[0] & s[2], lambda s: s[1]]
    return analyse(rules, ("W", "S", "C"))


def show(x):
    print(f"{x['form']:<16} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"full_in_top={'Y' if x['full_in_top'] else 'N'} ties={','.join(x['top_ties']) or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    c = control()
    if abs(c["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit(f"control failed: triad whole Φ {c['whole_phi']}")
    print(f"C1 conjunctive triad whole Φ={c['whole_phi']:.6f}: PASS")
    rows = [form(f) for f in (QUICK if args.quick else FORMS)]
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {x["form"]: x for x in rows}
    full = "".join(LABELS)
    scores = {
        "H1": all(abs(g[f]["whole_phi"] - 4.0) < 1e-6 and g[f]["full_in_top"] for f in ("all_four", "any_one")),
        "H2": g["side_match"]["full_in_top"],
        "H3": g["side_match"]["whole_phi"] < 4.0 - 1e-9,
        "H4": (not g["fixed_pairs"]["full_in_top"]
               and set(g["fixed_pairs"]["top_ties"]) == {"PB1S1", "PB2S2"}),
        "H5": g["one_per_side"]["whole_phi"] > PHI_EPS and g["one_per_side"]["full_in_top"],
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, full_label=full,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
