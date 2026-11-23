"""Ordinal (neighbour-only) vs uniform misreadings on three-valued hubs and triads.

Exact IIT 4.0 on the multivalued overlay third_party/pyphi_iit4_mv. Run from the repo root:
  python org_frontier/studies/ternary_ordinal_noise/run.py [--quick] [--write]
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
HUB_RATES = (0.05, 0.1, 0.2, 0.4)
TRIAD_RATES = (0.01, 0.05, 0.1, 0.2, 0.4)
RULES = {
    "median": lambda x: sorted(x)[len(x) // 2],
    "min": lambda x: min(x),
    "absdiff": lambda x: abs(x[0] - x[1]),
    "xor": lambda x: x[0] ^ x[1],
}


def p_read(actual, seen, k, r, shape):
    if shape == "uniform" or k == 2:
        return (1 - r) if actual == seen else r / (k - 1)
    if actual == seen:
        return 1 - r
    if abs(actual - seen) != 1:
        return 0.0
    return r / 2 if actual == 1 else r


def build(kind, rule, k, r, shape):
    """kind 'hub': S + 3 parties (S node 0). kind 'triad': W, S, C (S node 1)."""
    f = RULES[rule]
    n = 4 if kind == "hub" else 3
    s_idx = 0 if kind == "hub" else 1
    inputs = [i for i in range(n) if i != s_idx]
    ks = (k,) * n
    size = k ** n
    sbs = np.zeros((size, size))
    for i in range(size):
        st = decode_state(i, ks)
        p_s = np.zeros(k)
        for reads in itertools.product(range(k), repeat=len(inputs)):
            p = 1.0
            for j, seen in zip(inputs, reads):
                p *= p_read(st[j], seen, k, r, shape)
            if p:
                p_s[f(reads)] += p
        for v in range(k):
            if p_s[v]:
                nxt = [st[s_idx]] * n
                nxt[s_idx] = v
                sbs[i, encode_state(tuple(nxt), ks)] += p_s[v]
    cm = np.zeros((n, n))
    for j in inputs:
        cm[j, s_idx] = 1
        cm[s_idx, j] = 1
    labels = ("S", "P1", "P2", "P3") if kind == "hub" else ("W", "S", "C")
    return MultivaluedNetwork(sbs, list(ks), cm=cm, node_labels=labels), ks, labels


def read(kind, rule, k, r, shape, complexes=True):
    net, ks, labels = build(kind, rule, k, r, shape)
    sbs = net.sbs()
    per_state = {}
    for j in range(len(sbs)):
        if sbs[:, j].sum() > 0:
            st = decode_state(j, ks)
            per_state["".join(map(str, st))] = exact_phi(net, st)
    whole = max(per_state.values())
    peaks = [s for s, v in per_state.items() if whole > EPS and abs(v - whole) <= 1e-9]
    cores = {}
    if complexes:
        for s in peaks:
            mc = maximal_complex(net, tuple(int(c) for c in s))
            idx = mc.node_indices if getattr(mc, "node_indices", None) is not None else ()
            cores[s] = dict(core=[labels[i] for i in idx], phi=float(mc.phi))
    full = bool(cores) and all(set(c["core"]) == set(labels) for c in cores.values())
    return dict(kind=kind, rule=rule, k=k, r=r, shape=shape, whole_phi=whole, full_core=full,
                peak_states=peaks, peak_cores=cores, per_state=per_state)


def show(x):
    cores = sorted({"{" + ",".join(c["core"]) + "}" for c in x["peak_cores"].values()})
    top = max((c["phi"] for c in x["peak_cores"].values()), default=0.0)
    print(f"{x['kind']:<5} {x['rule']:<7} k={x['k']} {x['shape']:<7} r={x['r']:<4} "
          f"whole={x['whole_phi']:.6f} full={'yes' if x['full_core'] else 'no '} "
          f"core={'|'.join(cores) or '-'} core_phi={top:.6f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    c1a = read("hub", "median", 3, 0.1, "uniform", complexes=False)["whole_phi"]
    c1b = read("triad", "absdiff", 3, 0.1, "uniform", complexes=False)["whole_phi"]
    ok = abs(c1a - 0.022209) < 1e-6 and abs(c1b - 0.759836) < 1e-6
    print(f"C1 uniform controls (0.022209, 0.759836): {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("controls failed")
    if args.quick:
        cases = [("triad", "absdiff", 3, 0.1, "ordinal"), ("triad", "absdiff", 3, 0.4, "uniform"),
                 ("triad", "absdiff", 3, 0.4, "ordinal")]
    else:
        cases = [("hub", rule, 3, r, sh) for rule in ("median", "min") for r in HUB_RATES
                 for sh in ("uniform", "ordinal")]
        cases += [("triad", rule, 3, r, sh) for rule in ("absdiff", "min") for r in TRIAD_RATES
                  for sh in ("uniform", "ordinal")]
        cases += [("triad", "xor", 2, r, "uniform") for r in TRIAD_RATES]
    rows = [read(*c) for c in cases]
    for x in rows:
        show(x)
    if args.quick:
        return
    g = {(x["kind"], x["rule"], x["r"], x["shape"]): x for x in rows}
    triad_rates = [r for r in TRIAD_RATES if r >= 0.05]
    scores = {
        "H1": all(not g[("hub", "median", r, "ordinal")]["full_core"] for r in HUB_RATES),
        "H2": all(g[("hub", "min", r, "ordinal")]["full_core"] for r in HUB_RATES),
        "H3": all(g[("hub", "min", r, "ordinal")]["whole_phi"] >= g[("hub", "min", r, "uniform")]["whole_phi"] - EPS
                  for r in HUB_RATES),
        "H4": all(g[("triad", "absdiff", r, "uniform")]["full_core"] for r in triad_rates),
        "H5": all(g[("triad", "absdiff", r, "ordinal")]["full_core"] for r in triad_rates),
        "H6": not any(g[("triad", "xor", r, "uniform")]["full_core"] for r in TRIAD_RATES),
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
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
