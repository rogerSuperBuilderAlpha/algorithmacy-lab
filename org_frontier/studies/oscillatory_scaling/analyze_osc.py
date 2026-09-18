"""Agenda #11 — oscillatory (limit-cycle) Φ scaling vs #132 zoo.

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #10 DELAY_CORE_SHIFT (pointer); #132; Q11 prior.
Estimation/construct/omit closed.

Run:  python org_frontier/studies/oscillatory_scaling/analyze_osc.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from functools import reduce

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import major_complex, verdict as vlib
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.probes.probe_parity_scaling import parity_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

# candid N: n=3..5 (n=6 exact MC too costly for CI; Q11 prior has n=6)
SIZES = (3, 4, 5)
TOL = 1e-6
PHI_EPS = 1e-9


def rot_ring(n):
    """Pure cyclic shift: x_i' = x_{(i-1)%n}. Period-n traveling wave."""
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules


def and_ring(n):
    """#132 AND-neighbor ring (fixed-point family)."""
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


def period(rules, n):
    tpm = tpm_from_rules(rules, n=n)
    nxt = lambda s: sum(int(tpm[s, j]) << j for j in range(n))
    mp = 1
    for s0 in range(2 ** n):
        seen = {}
        s = s0
        t = 0
        while s not in seen:
            seen[s] = t
            s = nxt(s)
            t += 1
        mp = max(mp, t - seen[s])
    return mp


def law_class(seq):
    """Name Φ(n) sequence (probe_scaling_zoo style; needs ≥3 points)."""
    if len(seq) < 2:
        return "short"
    if max(seq) - min(seq) < TOL:
        return "constant"
    if seq[-1] < seq[0] - TOL:
        return "decay"
    if len(seq) >= 3:
        d1 = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
        if all(abs(x) < TOL for x in d2):
            return "linear"
    return "other"


def structure_of(phi):
    return "triadic" if phi > PHI_EPS else "dyadic"


def measure(build, n):
    rules = build(n)
    labels = tuple(f"x{i}" for i in range(n))
    core, phi = major_complex(rules, labels)
    n_core = len(core) if core else 0
    per = period(rules, n)
    return {
        "phi": float(phi),
        "structure": structure_of(float(phi)),
        "n_core": n_core,
        "period": per,
        "core": "{" + ",".join(core) + "}" if core else "(none)",
    }


def main():
    print("AGENDA #11 — OSCILLATORY Φ SCALING VS #132 ZOO")
    print("=" * 80)
    print("  cited: #10 DELAY_CORE_SHIFT (pointer); #132; Q11 prior")
    print("  oscillatory: rot_ring (cyclic shift, period=n)")
    print("  zoo: and_ring, conjunctive_hub, parity_hub")
    print(f"  sizes: {SIZES} (candid; n=6 deferred for exact-Φ cost)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_faithful = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl_faithful else 'FAIL'}")

    # and_ring anchors from #132 / Q11
    a3 = measure(and_ring, 3)
    a4 = measure(and_ring, 4)
    ok_ring = (
        abs(a3["phi"] - 6.0) < TOL and a3["structure"] == "triadic"
        and abs(a4["phi"] - 4.0) < TOL and a4["structure"] == "triadic"
    )
    print(f"  and_ring(3) Φ={a3['phi']:.6f} (expect 6)  "
          f"and_ring(4) Φ={a4['phi']:.6f} (expect 4)  "
          f"{'PASS' if ok_ring else 'FAIL'}")
    ctrl = ctrl_faithful and ok_ring
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    families = {
        "rot_ring": rot_ring,
        "and_ring": and_ring,
        "conjunctive_hub": single_hub,
        "parity_hub": parity_hub,
    }
    # reuse measured and_ring 3,4
    cache = {("and_ring", 3): a3, ("and_ring", 4): a4}
    rows = []
    series = {}

    for name, build in families.items():
        print(f"SWEEP — {name}")
        print("-" * 80)
        print(f"  {'n':>3}  {'Φ':>10}  {'struct':>8}  {'n_core':>6}  "
              f"{'period':>6}")
        seq = []
        structs = []
        for n in SIZES:
            if (name, n) in cache:
                m = cache[(name, n)]
            else:
                m = measure(build, n)
            seq.append(m["phi"])
            structs.append(m["structure"])
            rows.append({
                "family": name,
                "n": n,
                "phi": m["phi"],
                "structure": m["structure"],
                "n_core": m["n_core"],
                "period": m["period"],
                "core": m["core"],
            })
            print(f"  {n:>3}  {m['phi']:>10.6f}  {m['structure']:>8}  "
                  f"{m['n_core']:>6}  {m['period']:>6}")
        lc = law_class(seq)
        series[name] = {"phi": seq, "structure": structs, "law": lc}
        print(f"  law_class={lc}  Φ={seq}")
        print()

    rot = series["rot_ring"]["phi"]
    and_ = series["and_ring"]["phi"]
    hub = series["conjunctive_hub"]["phi"]
    par = series["parity_hub"]["phi"]

    # H1: separable from and_ring at n>=4 and not hub/parity landmarks
    match_and = all(
        abs(rot[i] - and_[i]) < TOL
        for i, n in enumerate(SIZES) if n >= 4
    )
    match_hub = all(
        abs(rot[i] - (n - 1)) < TOL for i, n in enumerate(SIZES)
    )
    match_par = all(
        abs(rot[i] - 2.0 ** (2 - n)) < TOL for i, n in enumerate(SIZES)
    )
    h1 = ctrl and (not match_and) and (not match_hub) and (not match_par)
    h2 = ctrl and (match_and or match_hub or match_par)

    # H3: structure disagreement at some n
    struct_disagree = any(
        series["rot_ring"]["structure"][i] != series["and_ring"]["structure"][i]
        for i in range(len(SIZES))
    )
    h3 = ctrl and struct_disagree and not h1

    if h1 and h2:
        h2 = False

    if h1 and not h2:
        verdict_word = "DIFFERENT_LAW"
        reading = (
            "DIFFERENT_LAW — rot_ring Φ constant (=2) with period=n; "
            "separable from and_ring cap and hub/parity landmarks "
            "(fifth shape vs #132 zoo)"
        )
    elif h2:
        verdict_word = "SAME_LAW"
        reading = (
            "SAME_LAW — rot_ring reproduces a fixed-point zoo landmark"
        )
    elif h3:
        verdict_word = "VERDICT_SPLIT"
        reading = (
            "VERDICT_SPLIT — rot_ring and and_ring disagree on structure "
            "more than on Φ law"
        )
    else:
        verdict_word = "OSC_MIXED"
        reading = "OSC_MIXED — see series"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  rot_ring Φ={rot}  law={series['rot_ring']['law']}")
    print(f"  and_ring Φ={and_}  law={series['and_ring']['law']}")
    print(f"  conj_hub Φ={hub}  law={series['conjunctive_hub']['law']}")
    print(f"  parity   Φ={par}  law={series['parity_hub']['law']}")
    print(f"  match_and={match_and}  match_hub={match_hub}  "
          f"match_par={match_par}  struct_disagree={struct_disagree}")
    print(f"  H1 (different Φ law):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (same zoo landmark):   "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (verdict split dominates): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "sweep.csv"), "w", newline="") as fh:
        fields = ["family", "n", "phi", "structure", "n_core", "period", "core"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "family": r["family"],
                "n": r["n"],
                "phi": f"{r['phi']:.8f}",
                "structure": r["structure"],
                "n_core": r["n_core"],
                "period": r["period"],
                "core": r["core"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "rot_phis": ";".join(f"{x:.6f}" for x in rot),
            "and_phis": ";".join(f"{x:.6f}" for x in and_),
            "rot_law": series["rot_ring"]["law"],
            "and_law": series["and_ring"]["law"],
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
