"""Alphabet ladder: median and min hubs (mediator + three parties) with k = 2, 3, 4 answer values.

Reuses the model of org_frontier/studies/ternary_majority_noise (uniform input noise, parties copy S).
Exact IIT 4.0 on the multivalued overlay third_party/pyphi_iit4_mv. Run from the repo root:
  python org_frontier/studies/alphabet_ladder_hub/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import json
import math
import sys
import time
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
for p in (ROOT / "third_party", ROOT):
    sys.path.insert(0, str(p))

from org_frontier.studies.ternary_majority_noise.run import EPS, LABELS, RULES, build  # noqa: E402
from pyphi_iit4_mv import exact_phi, maximal_complex  # noqa: E402
from pyphi_iit4_mv.conditional_independence import decode_state  # noqa: E402

CASES = ([("median", 4, r) for r in (0.0, 0.05, 0.1, 0.2)] + [("min", 4, r) for r in (0.0, 0.1)])
CONTROLS = {("median", 2, 0.1): 0.026981, ("median", 3, 0.1): 0.022209}


def read(rule, k, r, complexes=True):
    net, ks = build(RULES[rule], k, r)
    sbs = net.sbs()
    per_state = {}
    for j in range(len(sbs)):
        if sbs[:, j].sum() > 0:
            st = decode_state(j, ks)
            per_state["".join(map(str, st))] = exact_phi(net, st)
    whole = max(per_state.values())
    peaks = [s for s, v in per_state.items() if whole > EPS and abs(v - whole) <= 1e-9]
    core, core_phi = [], 0.0
    if complexes and peaks:
        mc = maximal_complex(net, tuple(int(c) for c in peaks[0]))
        idx = mc.node_indices if getattr(mc, "node_indices", None) is not None else ()
        core, core_phi = [LABELS[i] for i in idx], float(mc.phi)
    ratio = core_phi / whole if whole > EPS else None
    return dict(rule=rule, k=k, r=r, whole_phi=whole, peak_states=peaks, core_state=peaks[0] if peaks else None,
                core=core, core_phi=core_phi, ratio=ratio, per_state=per_state)


def show(x):
    ratio = f"{x['ratio']:.6f}" if x["ratio"] is not None else "-"
    print(f"{x['rule']:<6} k={x['k']} r={x['r']:<4} whole={x['whole_phi']:.6f} "
          f"core={'{' + ','.join(x['core']) + '}' if x['core'] else '-'} core_phi={x['core_phi']:.6f} ratio={ratio}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    ctrl = {key: read(*key, complexes=False)["whole_phi"] for key in CONTROLS}
    ok = all(abs(ctrl[key] - v) < 1e-6 for key, v in CONTROLS.items())
    print(f"C1 k=2,3 median controls (0.026981, 0.022209): {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("controls failed")
    cases = [("median", 4, 0.0)] if args.quick else CASES
    rows = []
    for c in cases:
        rows.append(read(*c))
        show(rows[-1])
        sys.stdout.flush()
    if args.quick:
        return
    g = {(x["rule"], x["r"]): x for x in rows}
    noisy = [g[("median", r)] for r in (0.05, 0.1, 0.2)]
    ratios = [x["ratio"] for x in noisy]
    full = set(LABELS)
    scores = {
        "H1": g[("median", 0.0)]["whole_phi"] <= EPS,
        "H2": all(x["whole_phi"] > EPS and set(x["core"]) != full for x in noisy),
        "H3": all(abs(rt - ratios[0]) <= 1e-6 * ratios[0] for rt in ratios),
        "H4": all(abs(rt - 10.0) <= 1e-5 for rt in ratios),
        "H5": (abs(g[("min", 0.0)]["whole_phi"] - 3 * math.log2(4)) <= 1e-6
               and set(g[("min", 0.0)]["core"]) == full and set(g[("min", 0.1)]["core"]) == full),
    }
    for h, v in scores.items():
        print(f"{h}: {'SUPPORTED' if v else 'REFUTED'}")
    print(f"elapsed {time.time() - t0:.0f} s")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), eps=EPS,
            hypotheses={h: "SUPPORTED" if v else "REFUTED" for h, v in scores.items()},
            controls={f"{k[0]} k={k[1]} r={k[2]}": v for k, v in ctrl.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
