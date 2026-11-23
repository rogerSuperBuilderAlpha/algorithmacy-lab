"""Ternary lifts of the W-S-C triad (W' = S, C' = S, S' = f(W, C)) vs their binary rules.

Exact IIT 4.0 on the multivalued overlay third_party/pyphi_iit4_mv. S misreads each input with
probability r (uniformly to another value). Run from the repo root:
  python org_frontier/studies/ternary_lift_panel/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import itertools
import json
import os
import sys
import time
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
for p in (ROOT / "third_party", ROOT):
    sys.path.insert(0, str(p))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np  # noqa: E402
import pyphi  # noqa: E402

from pyphi_iit4_mv import MultivaluedNetwork, exact_phi, maximal_complex  # noqa: E402
from pyphi_iit4_mv.conditional_independence import decode_state, encode_state  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
EPS = 1e-9
LABELS = ("W", "S", "C")
# name: (binary rule, ternary lift, lift agrees with binary on {0,1})
LIFTS = {
    "AND-min": ("AND", lambda a, b: min(a, b), True),
    "AND-alltop": ("AND", lambda a, b: 2 if a == b == 2 else 0, False),
    "OR-max": ("OR", lambda a, b: max(a, b), True),
    "OR-capsum": ("OR", lambda a, b: min(a + b, 2), True),
    "XOR-absdiff": ("XOR", lambda a, b: abs(a - b), True),
    "XOR-summod3": ("XOR", lambda a, b: (a + b) % 3, False),
    "COPY-W": ("COPY", lambda a, b: a, True),
}
BINARY = {"AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "XOR": lambda a, b: a ^ b,
          "COPY": lambda a, b: a}
RATES = (0.0, 0.1)


def build(f, k, r):
    ks = (k, k, k)
    size = k ** 3
    sbs = np.zeros((size, size))
    for i in range(size):
        w, s, c = decode_state(i, ks)
        p_s = np.zeros(k)
        for rw, rc in itertools.product(range(k), repeat=2):
            p = ((1 - r) if rw == w else r / (k - 1)) * ((1 - r) if rc == c else r / (k - 1))
            if p:
                p_s[f(rw, rc)] += p
        for nxt in range(k):
            if p_s[nxt]:
                sbs[i, encode_state((s, nxt, s), ks)] += p_s[nxt]
    dep_w = any(f(a, b) != f(a2, b) for a, a2, b in itertools.product(range(k), repeat=3))
    dep_c = any(f(a, b) != f(a, b2) for a, b, b2 in itertools.product(range(k), repeat=3))
    cm = np.array([[0, float(dep_w), 0], [1, 0, 1], [0, float(dep_c), 0]])
    return MultivaluedNetwork(sbs, list(ks), cm=cm, node_labels=LABELS), ks


def read(name, k, r):
    binary_rule, lift, agrees = LIFTS[name]
    f = lift if k == 3 else BINARY[binary_rule]
    net, ks = build(f, k, r)
    sbs = net.sbs()
    per_state = {}
    for j in range(len(sbs)):
        if sbs[:, j].sum() > 0:
            st = decode_state(j, ks)
            per_state["".join(map(str, st))] = exact_phi(net, st)
    whole = max(per_state.values())
    peaks = [s for s, v in per_state.items() if whole > EPS and abs(v - whole) <= 1e-9]
    cores = {}
    for s in peaks:
        mc = maximal_complex(net, tuple(int(c) for c in s))
        idx = mc.node_indices if getattr(mc, "node_indices", None) is not None else ()
        cores[s] = dict(core=[LABELS[i] for i in idx], phi=float(mc.phi))
    triadic = bool(cores) and all(set(c["core"]) == set(LABELS) for c in cores.values())
    return dict(lift=name, rule=binary_rule, agrees=agrees, k=k, r=r, whole_phi=whole,
                triadic=triadic, peak_states=peaks, peak_cores=cores, per_state=per_state)


def show(x):
    cores = sorted({"{" + ",".join(c["core"]) + "}" for c in x["peak_cores"].values()})
    label = x["lift"] if x["k"] == 3 else x["rule"]
    print(f"{label:<12} k={x['k']} r={x['r']:<4} whole={x['whole_phi']:.6f} "
          f"triadic={'yes' if x['triadic'] else 'no '} peaks={','.join(x['peak_states']) or '-'} "
          f"core={'|'.join(cores) or '-'}")


def controls():
    net, _ = build(BINARY["AND"], 2, 0.0)
    c1 = abs(exact_phi(net, (1, 1, 1)) - 2.0) < 1e-6
    net, _ = build(LIFTS["AND-min"][1], 3, 0.0)
    c2 = abs(exact_phi(net, (2, 2, 2)) - 3.169925) < 1e-6
    return c1, c2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    c1, c2 = controls()
    print(f"C1 binary AND (1,1,1) = 2.0: {'PASS' if c1 else 'FAIL'}")
    print(f"C2 ternary min (2,2,2) = 3.169925: {'PASS' if c2 else 'FAIL'}")
    if not (c1 and c2):
        raise SystemExit("controls failed")
    names = ("XOR-absdiff",) if args.quick else tuple(LIFTS)
    rates = RATES
    rows = []
    seen_binary = set()
    for name in names:
        for r in rates:
            if (LIFTS[name][0], r) not in seen_binary:
                seen_binary.add((LIFTS[name][0], r))
                rows.append(read(name, 2, r))
            rows.append(read(name, 3, r))
    for x in rows:
        show(x)
    if args.quick:
        return
    b = {(x["rule"], x["r"]): x for x in rows if x["k"] == 2}
    t = {(x["lift"], x["r"]): x for x in rows if x["k"] == 3}
    agree = [n for n in LIFTS if LIFTS[n][2]]
    other = [n for n in LIFTS if not LIFTS[n][2]]
    scores = {
        "H1": all(t[(n, r)]["triadic"] == b[(LIFTS[n][0], r)]["triadic"] for n in agree for r in RATES),
        "H2": all(t[(n, 0.0)]["whole_phi"] >= b[(LIFTS[n][0], 0.0)]["whole_phi"] - EPS for n in agree),
        "H3": all(t[(n, r)]["triadic"] == b[(LIFTS[n][0], r)]["triadic"] for n in other for r in RATES),
        "H4": not any(x["triadic"] for x in rows if x["rule"] == "COPY"),
        "H5": abs(t[("OR-max", 0.0)]["whole_phi"] - t[("OR-capsum", 0.0)]["whole_phi"]) > 1e-6,
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    print(f"elapsed {time.time() - t0:.0f} s")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), eps=EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
