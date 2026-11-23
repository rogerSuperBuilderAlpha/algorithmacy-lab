"""Relay length: a platform's loop closed through a chain of L relayers; tie sets pooled over states.

Run from the repo root: python org_frontier/studies/relay_length/run.py [--quick] [--write]
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


def arm(L):
    """Nodes: P=0, R1=1, R2=2, C1..CL=3..2+L."""
    labels = ("P", "R1", "R2") + tuple(f"C{i}" for i in range(1, L + 1))
    rules = [lambda s: s[1] & s[2], take(0), take(2 + L) if L else take(0)]
    for i in range(1, L + 1):
        rules.append(take(0) if i == 1 else take(2 + i - 1))
    return labels, rules


def both_1():
    """P=0, R1=1, R2=2, C1=3 (relays to R1), C2=4 (relays to R2)."""
    return ("P", "R1", "R2", "C1", "C2"), [lambda s: s[1] & s[2], take(3), take(4), take(0), take(0)]


FORMS = {f"arm_{L}": (lambda L=L: arm(L)) for L in range(4)}
FORMS["both_1"] = both_1
QUICK = ("arm_0", "arm_1", "both_1")


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
    print(f"{x['form']:<7} n={x['n']} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"top_states={x['n_top_states']} full_bound={'Y' if x['full_bound'] else 'N'} pooled_ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = [dict(form=f, **analyse(*FORMS[f]())) for f in (QUICK if args.quick else FORMS)]
    g = {x["form"]: x for x in rows}
    if abs(g["arm_0"]["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit("control failed: arm_0 should be the conjunctive triad (whole Φ 2.0)")
    if abs(g["both_1"]["whole_phi"] - 2.0) > 1e-6:
        raise SystemExit("control failed: both_1 should reproduce indirect_loops relay_both (whole Φ 2.0)")
    print("C1 arm_0 = conjunctive triad, C2 both_1 = indirect_loops relay_both (whole Φ 2.0): PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    arms = [g[f"arm_{L}"] for L in range(4)]
    scores = {
        "H1": all(x["whole_phi"] > PHI_EPS for x in arms),
        "H2": all(abs(x["top"] - 2.0) < 1e-6 for x in arms),
        "H3": all(x["full_bound"] for x in arms),
        "H4": all(arms[i + 1]["whole_phi"] <= arms[i]["whole_phi"] + PHI_EPS for i in range(3)),
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
