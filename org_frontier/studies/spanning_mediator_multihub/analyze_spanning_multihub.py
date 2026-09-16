"""Spanning mediator atop multi-hub (agenda #20 / extends q145).

Exact IIT-4.0 census: multi-hub base ± spanning top mediator vs pool ceiling
and shared-mediator AND merge. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/spanning_mediator_multihub/analyze_spanning_multihub.py
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
from org_frontier.probes.probe_multihub_law import sym_multihub
from org_frontier.probes.probe_topology_map import pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")


def _and_of(indices):
    idxs = tuple(indices)

    def f(x, idxs=idxs):
        v = 1
        for i in idxs:
            v &= x[i]
        return v

    return f


def spanning_atop(n_hubs: int, n_parties: int, mode: str):
    """Top T + symmetric multi-hub layer.

    Indices: 0 = T; 1..n_hubs = hubs; then parties.
    modes:
      recurrent — T' = AND(hubs); each hub also reads T; parties AND hubs
      ff        — T' = AND(hubs); hubs/parties as base multi-hub (no T readback)
      full      — T' = AND(hubs+parties); hubs and parties also read T
    """
    hubs = list(range(1, 1 + n_hubs))
    parties = list(range(1 + n_hubs, 1 + n_hubs + n_parties))
    labels = (
        ("T",)
        + tuple(f"H{i}" for i in range(n_hubs))
        + tuple(f"P{i}" for i in range(n_parties))
    )
    n = len(labels)
    rules = [None] * n

    if mode == "recurrent":
        rules[0] = _and_of(hubs)
        for h in hubs:
            others = [x for x in hubs if x != h]
            rules[h] = _and_of(list(parties) + others + [0])
        for p in parties:
            rules[p] = _and_of(hubs)
    elif mode == "ff":
        rules[0] = _and_of(hubs)
        for h in hubs:
            others = [x for x in hubs if x != h]
            rules[h] = _and_of(list(parties) + others)
        for p in parties:
            rules[p] = _and_of(hubs)
    elif mode == "full":
        below = list(hubs) + list(parties)
        rules[0] = _and_of(below)
        for h in hubs:
            others = [x for x in hubs if x != h]
            rules[h] = _and_of(list(parties) + others + [0])
        for p in parties:
            rules[p] = _and_of(list(hubs) + [0])
    else:
        raise KeyError(mode)

    return rules, labels, {
        "family": f"span_{mode}",
        "mode": mode,
        "n_hubs": n_hubs,
        "n_parties": n_parties,
        "n": n,
    }


def shared_mediator_and():
    """two_triad_shared_member shared-S AND merge reference."""
    labels = ("W1", "C1", "W2", "C2", "S")
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: (x[0] & x[1]) & (x[2] & x[3]),
    ]
    return rules, labels, {"family": "shared_S_AND", "mode": "AND", "n_hubs": "", "n_parties": "", "n": 5}


def run_cell(rules, labels, meta):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    labs = set(core_t)
    return {
        **meta,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": core_t,
        "core_phi": float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan"),
        "n_core": len(core_t),
        "T_in_core": "T" in labs or "S" in labs,
        "hub_in_core": any(x.startswith("H") for x in labs),
        "leaf_in_core": any(x.startswith("P") or x.startswith("W") or x.startswith("C") for x in labs),
        "full_core": len(core_t) == meta["n"],
        "seconds": round(time.time() - t0, 2),
    }


def fmt_core(core):
    return "(" + ",".join(core) + ")" if core else "()"


def main():
    print("SPANNING MEDIATOR ATOP MULTI-HUB — agenda #20 (extends q145)")
    print("=" * 80)
    print("  cited: q145 spanning-mediator law; #119 / sym_multihub → pool ceiling;")
    print("         two_triad shared-S AND merge Φ=4.0; hierarchy census WIN")
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
        r = run_cell(rules, labels, meta)
        r["name"] = name
        rows.append(r)
        by_name[name] = r
        print(
            f"  {name:<28} n={r['n']}  whole={r['structure']:<8} "
            f"Φ_MIP={r['whole_phi_mip']:.3f}  core={fmt_core(r['core']):<28} "
            f"coreΦ={r['core_phi']:.3f}  T={r['T_in_core']} "
            f"hub={r['hub_in_core']} leaf={r['leaf_in_core']}  ({r['seconds']}s)"
        )
        return r

    print("CEILINGS AND BASES")
    print("-" * 80)
    add("pool4", pool(4), tuple(f"x{i}" for i in range(4)),
        {"family": "pool", "mode": "", "n_hubs": "", "n_parties": "", "n": 4})
    add("pool5", pool(5), tuple(f"x{i}" for i in range(5)),
        {"family": "pool", "mode": "", "n_hubs": "", "n_parties": "", "n": 5})
    add("mh4_m2", sym_multihub(4, 2), ("H0", "H1", "P0", "P1"),
        {"family": "multihub", "mode": "base", "n_hubs": 2, "n_parties": 2, "n": 4})
    add("mh5_m2", sym_multihub(5, 2), ("H0", "H1", "P0", "P1", "P2"),
        {"family": "multihub", "mode": "base", "n_hubs": 2, "n_parties": 3, "n": 5})
    add("mh5_m3", sym_multihub(5, 3), ("H0", "H1", "H2", "P0", "P1"),
        {"family": "multihub", "mode": "base", "n_hubs": 3, "n_parties": 2, "n": 5})
    print()

    print("SHARED-MEDIATOR MERGE REFERENCE")
    print("-" * 80)
    rules, labels, meta = shared_mediator_and()
    add("shared_S_AND", rules, labels, meta)
    print()

    print("SPANNING TOP ATOP MULTI-HUB")
    print("-" * 80)
    for n_hubs, n_parties in ((2, 1), (2, 2), (3, 1)):
        for mode in ("recurrent", "ff", "full"):
            rules, labels, meta = spanning_atop(n_hubs, n_parties, mode)
            add(f"span_{mode}_{n_hubs}h{n_parties}p", rules, labels, meta)
    print()

    # ---- Hypothesis tests ----
    pool4 = by_name["pool4"]
    pool5 = by_name["pool5"]
    mh4 = by_name["mh4_m2"]
    mh5 = by_name["mh5_m2"]
    shared = by_name["shared_S_AND"]
    rec_2h2p = by_name["span_recurrent_2h2p"]
    ff_2h2p = by_name["span_ff_2h2p"]
    full_2h1p = by_name["span_full_2h1p"]
    full_3h1p = by_name["span_full_3h1p"]

    h1 = (
        ctrl
        and abs(pool4["core_phi"] - 12.0) < PHI_EPS
        and abs(pool5["core_phi"] - 20.0) < PHI_EPS
        and shared["full_core"]
        and abs(shared["core_phi"] - 4.0) < PHI_EPS
    )
    h2 = (
        mh4["core_phi"] + PHI_EPS < pool4["core_phi"]
        and mh5["core_phi"] + PHI_EPS < pool5["core_phi"]
    )

    spanning = [r for r in rows if str(r["family"]).startswith("span_")]
    h3 = all(
        r["core_phi"] <= by_name[f"pool{r['n']}"]["core_phi"] + PHI_EPS
        for r in spanning
    )

    h4 = (
        rec_2h2p["T_in_core"]
        and rec_2h2p["hub_in_core"]
        and rec_2h2p["leaf_in_core"]
        and rec_2h2p["full_core"]
    )
    h5 = not ff_2h2p["T_in_core"]
    h6 = (
        (
            abs(full_2h1p["core_phi"] - pool4["core_phi"]) < PHI_EPS
            and full_2h1p["full_core"]
        )
        or (
            abs(full_3h1p["core_phi"] - pool5["core_phi"]) < PHI_EPS
            and full_3h1p["full_core"]
        )
    ) and h3

    beyond_pool = any(
        r["core_phi"] > by_name[f"pool{r['n']}"]["core_phi"] + PHI_EPS
        for r in spanning
    )

    if h3 and h4 and h5 and h6:
        reading = (
            "WIN — spanning top does not beat pool; recurrent hub-span merges "
            "membership like shared-S; full span saturates pool"
        )
    elif h3 and (h4 or h6):
        reading = (
            "PARTIAL — pool ceiling holds; merge analogy or full-span saturation incomplete"
        )
    elif h3:
        reading = "NULL-leaning — pool ceiling holds; merge/saturate pattern failed"
    else:
        reading = "REFUTED ceiling — spanning cell exceeded same-n pool"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  pool Φ:     n4={pool4['core_phi']:.3f}  n5={pool5['core_phi']:.3f}")
    print(f"  mh base Φ:  mh4_m2={mh4['core_phi']:.3f}  mh5_m2={mh5['core_phi']:.3f}")
    print(f"  shared_S_AND: core={fmt_core(shared['core'])} coreΦ={shared['core_phi']:.3f}")
    print(f"  span_recurrent_2h2p: core={fmt_core(rec_2h2p['core'])} "
          f"coreΦ={rec_2h2p['core_phi']:.3f} T/hub/leaf="
          f"{rec_2h2p['T_in_core']}/{rec_2h2p['hub_in_core']}/{rec_2h2p['leaf_in_core']}")
    print(f"  span_ff_2h2p:        core={fmt_core(ff_2h2p['core'])} "
          f"T_in_core={ff_2h2p['T_in_core']}")
    print(f"  span_full_2h1p/3h1p: Φ={full_2h1p['core_phi']:.3f}/{full_3h1p['core_phi']:.3f} "
          f"full={full_2h1p['full_core']}/{full_3h1p['full_core']}")
    print(f"  beyond_pool_any:     {beyond_pool}")
    print(f"  H1 (control + pool ceilings + shared-S Φ=4.0):  "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (multi-hub below pool):                      "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (spanning ≤ pool at same n):                 "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (recurrent 2h2p merges T+hubs+leaves):       "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (feedforward top excluded from core):        "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print(f"  H6 (full span reaches pool, does not exceed):   "
          f"{'SUPPORTED' if h6 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  beyond pool? {'YES' if beyond_pool else 'NO'} "
          f"(max spanning coreΦ vs pool5={pool5['core_phi']:.1f})")
    print(f"  merge analogy (recurrent 2h2p full core w/ T)? "
          f"{'YES' if h4 else 'NO'}; coreΦ={rec_2h2p['core_phi']:.1f} "
          f"vs shared-S={shared['core_phi']:.1f} vs mh5_m2={mh5['core_phi']:.1f}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
          f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
          f"H5={('SUPPORTED' if h5 else 'REFUTED')}  "
          f"H6={('SUPPORTED' if h6 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = [
            "name", "family", "mode", "n_hubs", "n_parties", "n", "structure",
            "whole_phi_mip", "core", "core_phi", "n_core", "full_core",
            "T_in_core", "hub_in_core", "leaf_in_core", "seconds",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "family": r["family"],
                "mode": r.get("mode", ""),
                "n_hubs": r.get("n_hubs", ""),
                "n_parties": r.get("n_parties", ""),
                "n": r["n"],
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "full_core": str(r["full_core"]),
                "T_in_core": str(r["T_in_core"]),
                "hub_in_core": str(r["hub_in_core"]),
                "leaf_in_core": str(r["leaf_in_core"]),
                "seconds": r["seconds"],
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "h4": "SUPPORTED" if h4 else "REFUTED",
            "h5": "SUPPORTED" if h5 else "REFUTED",
            "h6": "SUPPORTED" if h6 else "REFUTED",
            "beyond_pool": str(beyond_pool),
            "rec_2h2p_core_phi": f"{rec_2h2p['core_phi']:.3f}",
            "pool5_core_phi": f"{pool5['core_phi']:.3f}",
            "shared_S_core_phi": f"{shared['core_phi']:.3f}",
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
