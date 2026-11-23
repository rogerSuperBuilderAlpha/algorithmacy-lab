"""Gate census: all 16 two-input rules for a switch-gated relayer under AND, OR and XOR platforms.

Run from the repo root: python org_frontier/studies/gate_census/run.py [--quick] [--write]
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


def gate(code):
    """Truth table code: output for (P, G) is bit 2*P + G of code."""
    return lambda s: (code >> (2 * s[0] + s[4])) & 1


def classify(code):
    outs = [(code >> i) & 1 for i in range(4)]  # index 2*P + G
    if code in (0, 15):
        return "constant", None
    if outs[0] == outs[1] and outs[2] == outs[3]:
        return "P-only", None
    if outs[0] == outs[2] and outs[1] == outs[3]:
        return "G-only", None
    if code in (6, 9):
        return "parity", None
    odd = [i for i in range(4) if outs.count(outs[i]) == 1][0]
    return "single-odd", (odd >> 1, odd & 1)


PLATFORMS = {"AND": AND, "OR": OR, "XOR": XOR}
FORMS = {}
for pname, pf in PLATFORMS.items():
    for code in range(16):
        FORMS[f"{pname}_g{code:02d}"] = (lambda pf=pf, code=code: (L5G, [pf, take(0), take(3), gate(code), take(0)]))
QUICK = ("AND_g08", "XOR_g08")


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
    print(f"{x['form']:<8} {x.get('gate_class', ''):<10} n={x['n']} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"top_states={x['n_top_states']} full_bound={'Y' if x['full_bound'] else 'N'} pooled_ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = [dict(form=f, **analyse(*FORMS[f]())) for f in (QUICK if args.quick else FORMS)]
    g = {x["form"]: x for x in rows}
    for x in rows:
        cls, odd = classify(int(x["form"][-2:]))
        x["gate_class"], x["odd_pattern"] = cls, odd
    if abs(g["AND_g08"]["whole_phi"] - 2.0) > 1e-6 or abs(g["XOR_g08"]["whole_phi"] - 0.5) > 1e-6:
        raise SystemExit("control failed: AND gate should give 2.0 (AND platform) and 0.5 (XOR platform)")
    print("C1 AND gate: AND platform 2.0, XOR platform 0.5: PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    pos = lambda x: x["whole_phi"] > PHI_EPS
    by = lambda plats, cls: [x for x in rows if x["form"].split("_")[0] in plats and x["gate_class"] == cls]
    h1 = all(pos(x) == (x["odd_pattern"][0] == (1 if x["form"].startswith("AND") else 0))
             for x in by(("AND", "OR"), "single-odd"))
    h3 = all(abs(x["whole_phi"] - (0.5 if x["form"].startswith("XOR") else 2.0)) < 1e-6
             for x in by(("AND", "OR", "XOR"), "G-only"))
    scores = {
        "H1": h1,
        "H2": not any(pos(x) for x in by(("AND", "OR", "XOR"), "constant") + by(("AND", "OR", "XOR"), "P-only")),
        "H3": h3,
        "H4": all(pos(x) for x in by(("XOR",), "single-odd")),
        "H5": all(pos(x) for x in by(("AND", "OR", "XOR"), "parity")),
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
