"""Switch delay: is the R1-driven switch effect just the extra time step? Drivers from_P, from_R1, via_D.

Run from the repo root: python org_frontier/studies/switch_delay/run.py [--quick] [--write]
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
L6D = ("P", "R1", "R2", "C1", "G", "D")


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


PLATFORMS = {"AND": AND, "XOR": XOR}
CASES = (("AND", 8), ("AND", 4), ("XOR", 8))
DRIVERS = ("from_P", "from_R1", "via_D")


def build(driver, pf, code):
    base = [pf, take(0), take(3), gate(code)]
    if driver == "from_P":
        return L5G, base + [take(0)]
    if driver == "from_R1":
        return L5G, base + [take(1)]
    return L6D, base + [take(5), take(0)]


FORMS = {f"{d}:{p}_g{c:02d}": (lambda d=d, p=p, c=c: build(d, PLATFORMS[p], c)) for d in DRIVERS for p, c in CASES}
QUICK = ("from_R1:AND_g04", "via_D:AND_g04")
EXPECT = {"from_P:AND_g08": 2.0, "from_P:AND_g04": 0.415037, "from_P:XOR_g08": 0.5,
          "from_R1:AND_g08": 2.0, "from_R1:AND_g04": 0.830075, "from_R1:XOR_g08": 2.0}


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
    print(f"{x['form']:<16} n={x['n']} states={x['n_states']:<2} whole={x['whole_phi']:.6f} top={x['top']:.6f} "
          f"top_states={x['n_top_states']} full_bound={'Y' if x['full_bound'] else 'N'} pooled_ties={ties or '-'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = [dict(form=f, **analyse(*FORMS[f]())) for f in (QUICK if args.quick else FORMS)]
    w = {x["form"]: x["whole_phi"] for x in rows}
    for f, v in EXPECT.items():
        if f in w and abs(w[f] - v) > 1e-6:
            raise SystemExit(f"control failed: {f} should give {v}")
    print("controls (gate_census / gate_census_r1 values reproduced):", "PASS")
    for x in rows:
        show(x)
    if args.quick:
        return
    scores = {
        "H1": abs(w["via_D:AND_g04"] - 0.830075) < 1e-6,
        "H2": abs(w["via_D:XOR_g08"] - 2.0) < 1e-6,
        "H3": abs(w["via_D:AND_g08"] - 2.0) < 1e-6,
    }
    scores["delay_explanation"] = scores["H1"] and scores["H2"]
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
