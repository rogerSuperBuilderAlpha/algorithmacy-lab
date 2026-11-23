"""Gate match test: is a gated relayer bound exactly when its gate rule matches the platform rule?

Run from the repo root: python org_frontier/studies/gate_match_test/run.py [--quick] [--write]
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


L5G = ("P", "R1", "R2", "C1", "G")


def OR(s):
    return s[1] | s[2]


GATES = {"and": lambda s: s[0] & s[4], "or": lambda s: s[0] | s[4], "xor": lambda s: s[0] ^ s[4]}


def gated(platform, gate, g_rule):
    """P=0, R1=1, R2=2, C1=3, G=4."""
    return lambda: (L5G, [platform, take(0), take(3), GATES[gate], g_rule])


FORMS = {
    "orP_or_from_P": gated(OR, "or", take(0)),
    "orP_or_from_R1": gated(OR, "or", take(1)),
    "orP_or_from_R2": gated(OR, "or", take(2)),
    "orP_or_from_C1": gated(OR, "or", take(3)),
    "orP_and_from_R1": gated(OR, "and", take(1)),
    "xorP_xor_from_P": gated(XOR, "xor", take(0)),
    "xorP_and_from_P": gated(XOR, "and", take(0)),
}
QUICK = ("orP_or_from_P", "orP_or_from_R1")


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
    print(f"{x['form']:<15} n={x['n']} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"top_states={x['n_top_states']} full_bound={'Y' if x['full_bound'] else 'N'} pooled_ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = [dict(form=f, **analyse(*FORMS[f]())) for f in (QUICK if args.quick else FORMS)]
    g = {x["form"]: x for x in rows}
    if abs(g["orP_or_from_P"]["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit("control failed: orP_or_from_P should reproduce or_gate_source (whole Φ 2.0)")
    print("C1 orP_or_from_P = or_gate_source orP_or_from_P (whole Φ 2.0): PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    w = lambda f: g[f]["whole_phi"]
    scores = {
        "H1": all(abs(w(f) - 2.0) < 1e-6 for f in ("orP_or_from_R1", "orP_or_from_R2", "orP_or_from_C1")),
        "H2": w("orP_and_from_R1") <= PHI_EPS,
        "H3": w("xorP_xor_from_P") > PHI_EPS,
        "H4": w("xorP_and_from_P") <= PHI_EPS,
    }
    scores["MATCHING_RULE"] = all(scores.values())
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
