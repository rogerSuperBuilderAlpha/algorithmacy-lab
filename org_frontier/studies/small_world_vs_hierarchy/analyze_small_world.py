"""Small-world rewire vs hierarchy (agenda #17).

Controlled ring→hub morph at fixed n, plus in-degree-preserving hub-targeted
rewires. Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/small_world_vs_hierarchy/analyze_small_world.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.probes.probe_scaling_zoo import ring

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def _and_of(srcs):
    srcs = tuple(srcs)

    def f(x, srcs=srcs):
        r = 1
        for s in srcs:
            r &= x[s]
        return r

    return f


def _copy(i):
    return lambda x, i=i: x[i]


def morph_ring_to_hub(n: int, k: int):
    """k parties hub-gated; hub = AND(those k); remainder keep ring AND.

    k=0 → ring; k=n-1 → single_hub.
    """
    labels = tuple(f"N{i}" for i in range(n))
    if k == 0:
        return ring(n), labels, {"family": "morph", "n": n, "k": k, "r": ""}
    if k == n - 1:
        return single_hub(n), labels, {"family": "morph", "n": n, "k": k, "r": ""}
    converted = list(range(1, k + 1))
    rules = [None] * n
    rules[0] = _and_of(converted)
    for i in converted:
        rules[i] = _copy(0)
    for i in range(1, n):
        if i in converted:
            continue
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = _and_of([a, b])
    return rules, labels, {"family": "morph", "n": n, "k": k, "r": ""}


def hub_rewire(n: int, r: int):
    """Ring with r non-hub nodes each replacing left-neighbour input with hub 0.

    In-degree 2 preserved. r=0 → ring.
    """
    labels = tuple(f"N{i}" for i in range(n))
    ins = {i: [(i - 1) % n, (i + 1) % n] for i in range(n)}
    for i in range(1, min(r, n - 1) + 1):
        if 0 not in ins[i]:
            ins[i][0] = 0
        else:
            ins[i][0] = 0
    rules = [_and_of(ins[i]) for i in range(n)]
    return rules, labels, {"family": "hub_rewire", "n": n, "k": "", "r": r}


def hierarchy_star(n: int):
    """Recurrent d=1 star: apex AND all leaves; each leaf copies apex."""
    labels = ("A",) + tuple(f"L{i}" for i in range(n - 1))
    rules = [None] * n
    rules[0] = _and_of(list(range(1, n)))
    for i in range(1, n):
        rules[i] = _copy(0)
    return rules, labels, {"family": "hierarchy_star", "n": n, "k": "", "r": ""}


def run_cell(rules, labels, meta, name):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    return {
        **meta,
        "name": name,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": core_t,
        "core_phi": float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan"),
        "n_core": len(core_t),
        "full_core": len(core_t) == meta["n"],
        "seconds": round(time.time() - t0, 2),
    }


def fmt_core(core):
    return "(" + ",".join(core) + ")" if core else "()"


def main():
    print("SMALL-WORLD REWIRE VS HIERARCHY — agenda #17")
    print("=" * 80)
    print("  cited: #132/q143 ring cap Φ=4; single_hub Φ=n-1; q146 random WS falls;")
    print("         hierarchy census; spanning multi-hub WIN (pool ceiling)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    by_name = {}

    def add(name, rules, labels, meta):
        r = run_cell(rules, labels, meta, name)
        rows.append(r)
        by_name[name] = r
        print(
            f"  {name:<28} n={r['n']}  whole={r['structure']:<8} "
            f"Φ_MIP={r['whole_phi_mip']:.3f}  core={fmt_core(r['core']):<32} "
            f"coreΦ={r['core_phi']:.3f}  full={r['full_core']}  ({r['seconds']}s)"
        )
        return r

    print("ANCHORS")
    print("-" * 80)
    for n in (5, 6):
        add(f"ring{n}", ring(n), tuple(f"N{i}" for i in range(n)),
            {"family": "ring", "n": n, "k": "", "r": ""})
        add(f"hub{n}", single_hub(n), tuple(f"N{i}" for i in range(n)),
            {"family": "hub", "n": n, "k": "", "r": ""})
    print()

    print("MORPH ring→hub (k parties hub-gated)")
    print("-" * 80)
    morph_rows = []
    for n in (5, 6):
        for k in range(0, n):
            name = f"morph_n{n}_k{k}"
            # Reuse anchors at endpoints (same forms; avoids double n=6 exact-Φ cost).
            if k == 0:
                src = by_name[f"ring{n}"]
                r = {**src, "name": name, "family": "morph", "k": k, "r": ""}
                rows.append(r)
                by_name[name] = r
                morph_rows.append(r)
                print(
                    f"  {name:<28} n={r['n']}  whole={r['structure']:<8} "
                    f"Φ_MIP={r['whole_phi_mip']:.3f}  core={fmt_core(r['core']):<32} "
                    f"coreΦ={r['core_phi']:.3f}  full={r['full_core']}  (alias ring)"
                )
                continue
            if k == n - 1:
                src = by_name[f"hub{n}"]
                r = {**src, "name": name, "family": "morph", "k": k, "r": ""}
                rows.append(r)
                by_name[name] = r
                morph_rows.append(r)
                print(
                    f"  {name:<28} n={r['n']}  whole={r['structure']:<8} "
                    f"Φ_MIP={r['whole_phi_mip']:.3f}  core={fmt_core(r['core']):<32} "
                    f"coreΦ={r['core_phi']:.3f}  full={r['full_core']}  (alias hub)"
                )
                continue
            rules, labels, meta = morph_ring_to_hub(n, k)
            r = add(name, rules, labels, meta)
            morph_rows.append(r)
    print()

    print("HUB-TARGETED REWIRE (in-degree 2, n=5)")
    print("-" * 80)
    rewire_rows = []
    for rcount in (0, 1, 2, 3):
        rules, labels, meta = hub_rewire(5, rcount)
        r = add(f"hub_rewire_n5_r{rcount}", rules, labels, meta)
        rewire_rows.append(r)
    print()

    print("HIERARCHY CONTRAST (recurrent star n=5)")
    print("-" * 80)
    rules, labels, meta = hierarchy_star(5)
    star = add("hierarchy_star_n5", rules, labels, meta)
    print()

    # ---- Hypothesis tests ----
    ring5, ring6 = by_name["ring5"], by_name["ring6"]
    hub5, hub6 = by_name["hub5"], by_name["hub6"]

    h1 = (
        ctrl
        and abs(ring5["core_phi"] - 4.0) < PHI_EPS
        and abs(ring6["core_phi"] - 4.0) < PHI_EPS
        and abs(hub5["core_phi"] - 4.0) < PHI_EPS
        and abs(hub6["core_phi"] - 5.0) < PHI_EPS
        and abs(by_name["morph_n5_k0"]["core_phi"] - ring5["core_phi"]) < PHI_EPS
        and abs(by_name["morph_n5_k4"]["core_phi"] - hub5["core_phi"]) < PHI_EPS
        and abs(by_name["morph_n6_k0"]["core_phi"] - ring6["core_phi"]) < PHI_EPS
        and abs(by_name["morph_n6_k5"]["core_phi"] - hub6["core_phi"]) < PHI_EPS
    )

    def is_interior(r):
        return r["family"] == "morph" and 0 < int(r["k"]) < r["n"] - 1

    interiors = [r for r in morph_rows if is_interior(r)]

    def combines(r):
        """Strict between ring and hub when they differ, triadic full core; or
        at n where ring==hub, any interior full-core triadic with Φ in (0, ring)
        does NOT count as combine — need raise toward a distinct hub law.
        """
        n = r["n"]
        ring_phi = by_name[f"ring{n}"]["core_phi"]
        hub_phi = by_name[f"hub{n}"]["core_phi"]
        if not (r["structure"] == "triadic" and r["full_core"]):
            return False
        lo, hi = sorted((ring_phi, hub_phi))
        if hi - lo < PHI_EPS:
            # anchors equal: combine would require exceeding the shared value
            return r["core_phi"] > hi + PHI_EPS
        return lo + PHI_EPS < r["core_phi"] < hi - PHI_EPS

    any_combine = any(combines(r) for r in interiors)
    h2 = not any_combine

    def collapses(r):
        ring_phi = by_name[f"ring{r['n']}"]["core_phi"]
        hub_phi = by_name[f"hub{r['n']}"]["core_phi"]
        floor = min(ring_phi, hub_phi)
        return (
            r["structure"] == "dyadic"
            or (r["core_phi"] <= floor + PHI_EPS and not r["full_core"])
            or r["core_phi"] + PHI_EPS < floor
        )

    h3 = all(collapses(r) for r in interiors)

    # H4: at n=6, no interior in (4,5) or at hub 5.0; pick-one
    n6_int = [r for r in interiors if r["n"] == 6]
    n6_hits_hub = any(abs(r["core_phi"] - 5.0) < PHI_EPS for r in n6_int)
    n6_between = any(4.0 + PHI_EPS < r["core_phi"] < 5.0 - PHI_EPS for r in n6_int)
    h4 = h2 and h3 and (not n6_hits_hub) and (not n6_between)

    # H5: hub rewires r=1..3 never exceed ring
    rewire_interior = [r for r in rewire_rows if int(r["r"]) > 0]
    h5 = all(r["core_phi"] <= ring5["core_phi"] + PHI_EPS for r in rewire_interior)

    if h1 and h4 and h5:
        reading = (
            "PICK_ONE — interiors collapse; only pure ring (cap Φ=4) and pure hub "
            "(Φ=n-1) recover; no combine"
        )
        verdict_word = "PICK_ONE"
    elif h1 and h2 and not h3:
        reading = "PARTIAL — no between-band combine, but interiors not cleanly collapsed"
        verdict_word = "PARTIAL"
    elif any_combine:
        reading = "COMBINE — interior morph sits between ring cap and hub growth"
        verdict_word = "COMBINE"
    else:
        reading = "NEITHER — anchors or morph pattern failed to resolve"
        verdict_word = "NEITHER"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  ring Φ:  n5={ring5['core_phi']:.3f}  n6={ring6['core_phi']:.3f}")
    print(f"  hub Φ:   n5={hub5['core_phi']:.3f}  n6={hub6['core_phi']:.3f}")
    print(f"  morph interiors: {len(interiors)}  any_combine={any_combine}  "
          f"all_collapse={h3}")
    print(f"  n6 interiors coreΦ: "
          f"{[round(r['core_phi'], 3) for r in n6_int]}")
    print(f"  hub_rewire n5 r=1..3 coreΦ: "
          f"{[round(r['core_phi'], 3) for r in rewire_interior]}")
    print(f"  hierarchy_star_n5: coreΦ={star['core_phi']:.3f} "
          f"(hub-equivalent recurrent star)")
    print(f"  H1 (anchors + morph endpoints):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (interiors do not combine):      "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (interiors collapse):            "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (pick-one at n=6 size contrast): "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (hub-rewire ≤ ring at n=5):      "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  combine ring-cap with hub-growth? "
          f"{'YES' if verdict_word == 'COMBINE' else 'NO'}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "name", "family", "n", "k", "r", "structure", "whole_phi_mip",
            "core", "core_phi", "n_core", "full_core", "seconds",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "family": r["family"],
                "n": r["n"],
                "k": r.get("k", ""),
                "r": r.get("r", ""),
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "full_core": str(r["full_core"]),
                "seconds": r["seconds"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
