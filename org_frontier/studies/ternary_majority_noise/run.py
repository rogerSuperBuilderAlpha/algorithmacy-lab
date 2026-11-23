"""Three-valued majority (median) and its min/max lifts under mediator input noise.

Mediator S and three parties, alphabet {0,1,2} (or {0,1} for the binary controls). S misreads each
party independently with probability r (uniformly to another value); S commits a rule over its
readings; parties copy S exactly. Exact IIT 4.0 on the multivalued overlay third_party/pyphi_iit4_mv.

Run from the repo root: python org_frontier/studies/ternary_majority_noise/run.py [--quick] [--write]
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
N_PARTIES = 3
LABELS = ("S", "P1", "P2", "P3")
RULES = {"median": lambda x: sorted(x)[len(x) // 2], "min": min, "max": max}
BINARY_NAME = {"median": "MAJ3", "min": "AND3", "max": "OR3"}
RATES = (0.0, 0.05, 0.1, 0.2, 0.4)
QUICK = (("median", 3, 0.0), ("median", 2, 0.2), ("median", 3, 0.1))


def build(rule, k, r, n=N_PARTIES):
    ks = (k,) * (n + 1)
    size = k ** (n + 1)
    sbs = np.zeros((size, size))
    for i in range(size):
        st = decode_state(i, ks)
        p_s = np.zeros(k)
        for reads in itertools.product(range(k), repeat=n):
            p = 1.0
            for actual, seen in zip(st[1:], reads):
                p *= (1 - r) if actual == seen else r / (k - 1)
            if p:
                p_s[rule(reads)] += p
        for s in range(k):
            if p_s[s]:
                sbs[i, encode_state((s,) + (st[0],) * n, ks)] += p_s[s]
    cm = np.zeros((n + 1, n + 1))
    cm[1:, 0] = 1
    cm[0, 1:] = 1
    return MultivaluedNetwork(sbs, list(ks), cm=cm, node_labels=LABELS[: n + 1]), ks


def read(rule_name, k, r, complexes=True):
    net, ks = build(RULES[rule_name], k, r)
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
            cores[s] = dict(core=[LABELS[i] for i in idx], phi=float(mc.phi))
    name = rule_name if k == 3 else BINARY_NAME[rule_name]
    return dict(rule=rule_name, form=name, k=k, r=r, whole_phi=whole, peak_states=peaks,
                peak_cores=cores, per_state=per_state)


def full_core(x):
    return all(set(c["core"]) == set(LABELS) for c in x["peak_cores"].values())


def show(x):
    cores = sorted({"{" + ",".join(c["core"]) + "}" for c in x["peak_cores"].values()})
    top = max((c["phi"] for c in x["peak_cores"].values()), default=0.0)
    print(f"{x['form']:<6} k={x['k']} r={x['r']:<4} whole={x['whole_phi']:.6f} "
          f"peaks={','.join(x['peak_states']) or '-'} core={'|'.join(cores) or '-'} core_phi={top:.6f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    if args.quick:
        rows = [read(*c, complexes=False) for c in QUICK]
        if abs(rows[1]["whole_phi"] - 0.036624) > 1e-4:
            raise SystemExit("C1 binary MAJ3 control failed")
        print("C1 binary MAJ3 control: PASS")
        for x in rows:
            show(x)
        return
    rows = [read(rule, k, r) for rule in RULES for k in (2, 3) for r in RATES]
    g = {(x["rule"], x["k"], x["r"]): x for x in rows}
    c1 = (abs(g[("median", 2, 0.2)]["whole_phi"] - 0.036624) <= 1e-4
          and abs(g[("max", 2, 0.0)]["whole_phi"] - 3.0) <= 1e-4
          and abs(g[("max", 2, 0.2)]["whole_phi"] - 1.0415) <= 1e-4)
    c2 = all(abs(g[("min", 3, r)]["whole_phi"] - g[("max", 3, r)]["whole_phi"]) <= 1e-6 for r in RATES)
    print(f"C1 binary controls: {'PASS' if c1 else 'FAIL'}")
    print(f"C2 ternary min = max: {'PASS' if c2 else 'FAIL'}")
    for x in rows:
        show(x)
    if not (c1 and c2):
        raise SystemExit("controls failed")
    noisy = [r for r in RATES if r > 0]
    scores = {
        "H1": g[("median", 3, 0.0)]["whole_phi"] <= EPS,
        "H2": all(g[("median", 3, r)]["whole_phi"] > EPS for r in noisy),
        "H3": all(not full_core(g[("median", 3, r)]) for r in noisy),
        "H4": g[("min", 3, 0.0)]["whole_phi"] > g[("min", 2, 0.0)]["whole_phi"] + EPS,
        "H5": all(full_core(g[("min", 3, r)]) for r in RATES),
        "H6": all(g[("median", 3, r)]["whole_phi"] <= g[("median", 2, r)]["whole_phi"] + EPS for r in noisy),
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
