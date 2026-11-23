"""Relay flips: relayers that flip, gate, or sit on unequal arms; tie sets pooled over states.

Run from the repo root: python org_frontier/studies/relay_flips/run.py [--quick] [--write]
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


def take(j):
    return lambda s: s[j]


def flip(j):
    return lambda s: 1 - s[j]


def AND(s):
    return s[1] & s[2]


def XOR(s):
    return s[1] ^ s[2]


L4 = ("P", "R1", "R2", "C1")
L5 = ("P", "R1", "R2", "C1", "C2")
L5G = ("P", "R1", "R2", "C1", "G")

FORMS = {
    # P=0, R1=1, R2=2, C1=3
    "copy_1": lambda: (L4, [AND, take(0), take(3), take(0)]),
    "flip_1": lambda: (L4, [AND, take(0), take(3), flip(0)]),
    "flip_2": lambda: (L5, [AND, take(0), take(4), flip(0), flip(3)]),
    "gated_1": lambda: (L5G, [AND, take(0), take(3), lambda s: s[0] & s[4], take(4)]),
    "xor_copy_1": lambda: (L4, [XOR, take(0), take(3), take(0)]),
    "xor_flip_1": lambda: (L4, [XOR, take(0), take(3), flip(0)]),
    # P=0, R1=1, R2=2, A1=3 (relays to R1), B1=4, B2=5 (relay chain to R2)
    "unequal_1_2": lambda: (("P", "R1", "R2", "A1", "B1", "B2"),
                            [AND, take(3), take(5), take(0), take(0), take(4)]),
}
QUICK = ("copy_1", "flip_1", "xor_flip_1")


def analyse(labels, rules):
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
    top = max(s["top"] for s in states)
    at_top = [s for s in states if top > PHI_EPS and top - s["top"] <= PHI_EPS]
    pooled = sorted({t for s in at_top for t in s["ties"]}, key=lambda t: (len(t), t))
    return dict(n=n, n_states=len(states), whole_phi=max(s["full_phi"] for s in states), top=top,
                n_top_states=len(at_top), pooled_ties=pooled,
                full_bound=any(s["full_in"] for s in at_top), states=states)


def show(x):
    ties = ",".join(x["pooled_ties"]) if len(x["pooled_ties"]) <= 6 else f"{len(x['pooled_ties'])} subsets"
    print(f"{x['form']:<11} n={x['n']} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"top_states={x['n_top_states']} full_bound={'Y' if x['full_bound'] else 'N'} pooled_ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = [dict(form=f, **analyse(*FORMS[f]())) for f in (QUICK if args.quick else FORMS)]
    g = {x["form"]: x for x in rows}
    if abs(g["copy_1"]["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit("control failed: copy_1 should reproduce relay_length arm_1 (whole Φ 2.0)")
    print("C1 copy_1 = relay_length arm_1 (whole Φ 2.0): PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    eq = lambda a, b: abs(g[a]["whole_phi"] - g[b]["whole_phi"]) < 1e-6
    scores = {
        "H1": eq("flip_1", "copy_1"),
        "H2": eq("flip_2", "copy_1"),
        "H3": eq("xor_flip_1", "xor_copy_1"),
        "H4": g["gated_1"]["whole_phi"] > PHI_EPS and any("G" in t for t in g["gated_1"]["pooled_ties"]),
        "H5": abs(g["unequal_1_2"]["whole_phi"] - 2.0) < 1e-6 and g["unequal_1_2"]["full_bound"],
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
