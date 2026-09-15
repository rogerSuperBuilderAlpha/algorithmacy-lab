"""Interior topology between ring and pool (agenda #19).

Designed families: multihub, chordal ring, k-regular ring, lattice strip,
partial pool. Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/interior_ring_pool/analyze_interior.py
"""

from __future__ import annotations

import csv
import math
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
from org_frontier.probes.probe_scaling_zoo import ring
from org_frontier.probes.probe_topology_map import pool

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


def k_regular_ring(n, d):
    """Each node = AND of neighbors at ring distance 1..d."""
    rules = [None] * n
    for i in range(n):
        nbrs = []
        for off in range(1, d + 1):
            nbrs.extend([(i - off) % n, (i + off) % n])
        seen, nb = set(), []
        for x in nbrs:
            if x not in seen and x != i:
                seen.add(x)
                nb.append(x)
        rules[i] = _and_of(nb)
    return rules


def chordal_ring(n, n_chords):
    """Ring plus n_chords opposite chords (i ↔ i+⌊n/2⌋ for i=0..c-1)."""
    extras = {i: set() for i in range(n)}
    half = n // 2
    for c in range(n_chords):
        a = c % n
        b = (a + half) % n
        if a != b:
            extras[a].add(b)
            extras[b].add(a)
    rules = [None] * n
    for i in range(n):
        nbrs = [(i - 1) % n, (i + 1) % n] + sorted(extras[i])
        seen, nb = set(), []
        for x in nbrs:
            if x not in seen:
                seen.add(x)
                nb.append(x)
        rules[i] = _and_of(nb)
    return rules


def lattice_strip(n):
    """2 × (n/2) strip with wrap on the long axis; each node AND of grid nbrs."""
    if n % 2 != 0:
        raise ValueError("lattice_strip needs even n")
    w = n // 2
    rules = [None] * n
    for i in range(n):
        row, col = divmod(i, w)
        nbrs = [
            row * w + (col - 1) % w,
            row * w + (col + 1) % w,
            (1 - row) * w + col,
        ]
        seen, nb = set(), []
        for x in nbrs:
            if x not in seen and x != i:
                seen.add(x)
                nb.append(x)
        rules[i] = _and_of(nb)
    return rules


def partial_pool(n, m):
    """Clique pool on first m nodes; remaining nodes keep ring AND."""
    rules = [None] * n
    clique = list(range(m))
    for i in range(n):
        if i < m and m >= 2:
            others = [j for j in clique if j != i]
            rules[i] = _and_of(others)
        else:
            rules[i] = _and_of([(i - 1) % n, (i + 1) % n])
    return rules


def run_cell(rules, labels, meta, name):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    n = meta["n"]
    ring_phi = 4.0 if n >= 4 else float("nan")
    pool_phi = float(n * (n - 1))
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    full = len(core_t) == n
    interior = (
        v.structure == "triadic"
        and full
        and cp > ring_phi + PHI_EPS
        and cp < pool_phi - PHI_EPS
    )
    return {
        **meta,
        "name": name,
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": core_t,
        "core_phi": cp,
        "n_core": len(core_t),
        "full_core": full,
        "interior": interior,
        "seconds": round(time.time() - t0, 2),
    }


def fmt_core(core):
    return "(" + ",".join(core) + ")" if core else "()"


def ratio_spread(values, transform):
    """Max/min of Φ/transform(n) relative spread; None if undefined."""
    ratios = []
    for n, phi in values:
        t = transform(n)
        if t <= 0:
            return None
        ratios.append(phi / t)
    if not ratios or min(ratios) <= 0:
        return None
    return (max(ratios) - min(ratios)) / min(ratios)


def main():
    print("INTERIOR TOPOLOGY BETWEEN RING AND POOL — agenda #19")
    print("=" * 80)
    print("  cited: ring cap Φ=4; pool Φ=n(n-1); small_world PICK_ONE; q146/q150;")
    print("         #119 multihub → pool")
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
        flag = "INTERIOR" if r["interior"] else (
            "POLE" if r["full_core"] and r["structure"] == "triadic" else "other"
        )
        print(
            f"  {name:<22} n={r['n']}  whole={r['structure']:<8} "
            f"Φ_MIP={r['whole_phi_mip']:.3f}  coreΦ={r['core_phi']:.3f}  "
            f"full={r['full_core']}  {flag}  ({r['seconds']}s)"
        )
        return r

    # ---- Anchors ----
    print("ANCHORS (ring / pool)")
    print("-" * 80)
    for n in (4, 5, 6):
        labels = tuple(f"N{i}" for i in range(n))
        add(f"ring{n}", ring(n), labels, {"family": "ring", "n": n, "param": 0})
        add(f"pool{n}", pool(n), labels, {"family": "pool", "n": n, "param": n})
    print()

    # ---- Multihub m=2 sweep (candidate intermediate law) ----
    print("MULTI-HUB m=2 (n-sweep)")
    print("-" * 80)
    for n in (4, 5, 6):
        labels = tuple(f"N{i}" for i in range(n))
        add(f"mh2_n{n}", sym_multihub(n, 2), labels,
            {"family": "multihub_m2", "n": n, "param": 2})
    # one denser multihub interior at n=5,6
    add("mh3_n5", sym_multihub(5, 3), tuple(f"N{i}" for i in range(5)),
        {"family": "multihub_m3", "n": 5, "param": 3})
    add("mh3_n6", sym_multihub(6, 3), tuple(f"N{i}" for i in range(6)),
        {"family": "multihub_m3", "n": 6, "param": 3})
    print()

    # ---- Chordal rings ----
    print("CHORDAL RINGS")
    print("-" * 80)
    for n, chords in ((5, (0, 1, 2)), (6, (0, 2, 3))):
        labels = tuple(f"N{i}" for i in range(n))
        for c in chords:
            add(f"chord_n{n}_c{c}", chordal_ring(n, c), labels,
                {"family": "chordal", "n": n, "param": c})
    print()

    # ---- k-regular ----
    print("K-REGULAR RINGS")
    print("-" * 80)
    for n, degrees in ((5, (1, 2)), (6, (1, 2))):
        labels = tuple(f"N{i}" for i in range(n))
        for d in degrees:
            add(f"kreg_n{n}_d{d}", k_regular_ring(n, d), labels,
                {"family": "kregular", "n": n, "param": d})
    print()

    # ---- lattice strip (even n) ----
    print("LATTICE STRIP")
    print("-" * 80)
    for n in (4, 6):
        labels = tuple(f"N{i}" for i in range(n))
        add(f"strip_n{n}", lattice_strip(n), labels,
            {"family": "lattice_strip", "n": n, "param": n // 2})
    print()

    # ---- partial pool collapse control (n=5 only) ----
    print("PARTIAL POOL (collapse control, n=5)")
    print("-" * 80)
    labels5 = tuple(f"N{i}" for i in range(5))
    for m in (2, 3, 4, 5):
        add(f"ppool_n5_m{m}", partial_pool(5, m), labels5,
            {"family": "partial_pool", "n": 5, "param": m})
    print()

    # ---- Hypothesis tests ----
    h1 = (
        ctrl
        and all(abs(by_name[f"ring{n}"]["core_phi"] - 4.0) < PHI_EPS for n in (4, 5, 6))
        and all(
            abs(by_name[f"pool{n}"]["core_phi"] - n * (n - 1)) < PHI_EPS
            for n in (4, 5, 6)
        )
    )

    interiors = [r for r in rows if r["interior"]]
    h2 = len(interiors) >= 1

    # H3: check multihub_m2 full-core series and chordal full-core by n
    def full_series(family):
        pts = [
            (r["n"], r["core_phi"])
            for r in rows
            if r["family"] == family and r["full_core"] and r["structure"] == "triadic"
        ]
        # unique n keep first
        by_n = {}
        for n, phi in pts:
            by_n.setdefault(n, phi)
        return sorted(by_n.items())

    def claims_log_or_sqrt(series):
        if len(series) < 2:
            return False
        # exclude pure constant (ring) and pure pool
        phis = [p for _, p in series]
        if max(phis) - min(phis) < PHI_EPS:
            return False
        if all(abs(p - n * (n - 1)) < PHI_EPS for n, p in series):
            return False
        log_sp = ratio_spread(series, math.log)
        sqrt_sp = ratio_spread(series, math.sqrt)
        # "constant ratio within 10%" ⇒ claims that shape
        log_ok = log_sp is not None and log_sp <= 0.10
        sqrt_ok = sqrt_sp is not None and sqrt_sp <= 0.10
        return log_ok or sqrt_ok

    series_checked = {
        "multihub_m2": full_series("multihub_m2"),
        "chordal_c2": [
            (r["n"], r["core_phi"])
            for r in rows
            if r["family"] == "chordal"
            and int(r["param"]) == 2
            and r["full_core"]
            and r["structure"] == "triadic"
        ],
        "lattice_strip": full_series("lattice_strip"),
        "kregular_d2": [
            (r["n"], r["core_phi"])
            for r in rows
            if r["family"] == "kregular"
            and int(r["param"]) == 2
            and r["full_core"]
            and r["structure"] == "triadic"
        ],
    }
    any_log_sqrt = any(claims_log_or_sqrt(s) for s in series_checked.values() if s)
    h3 = not any_log_sqrt

    ppools = [r for r in rows if r["family"] == "partial_pool" and int(r["param"]) < 5]
    h4 = all(
        (r["structure"] == "dyadic") or (not r["full_core"]) or (not r["interior"])
        for r in ppools
    ) and not any(r["interior"] for r in ppools)

    # H5: at n=6, full-core chord/kreg steps between 4 and 30
    n6_steps = sorted({
        round(r["core_phi"], 6)
        for r in rows
        if r["n"] == 6
        and r["full_core"]
        and r["structure"] == "triadic"
        and r["family"] in ("chordal", "kregular", "multihub_m2", "lattice_strip", "ring", "pool")
    })
    between_n6 = [p for p in n6_steps if 4.0 + PHI_EPS < p < 30.0 - PHI_EPS]
    h5 = len(between_n6) >= 2  # at least two distinct interior step values

    if h1 and h2 and h3 and h5:
        reading = (
            "NO_INTERMEDIATE_LAW — discrete full-core interiors exist (hub/chord/"
            "degree steps); no log or √n scaling in n; not pole-only collapse"
        )
        verdict_word = "NO_INTERMEDIATE_LAW"
    elif h1 and h2 and not h3:
        reading = "INTERMEDIATE_LAW — a designed family tracks log or √n in n"
        verdict_word = "INTERMEDIATE_LAW"
    elif h1 and not h2 and h4:
        reading = "COLLAPSE — no stable full-core interior; forms jump to poles or factor"
        verdict_word = "COLLAPSE"
    else:
        reading = "PARTIAL — anchors or interior pattern incomplete"
        verdict_word = "PARTIAL"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  ring Φ:  {[by_name[f'ring{n}']['core_phi'] for n in (4, 5, 6)]}")
    print(f"  pool Φ:  {[by_name[f'pool{n}']['core_phi'] for n in (4, 5, 6)]}")
    print(f"  interiors ({len(interiors)}): "
          f"{[(r['name'], round(r['core_phi'], 3)) for r in interiors]}")
    print(f"  series multihub_m2: {series_checked['multihub_m2']}")
    print(f"  series chord_c2:    {series_checked['chordal_c2']}")
    print(f"  series kreg_d2:     {series_checked['kregular_d2']}")
    print(f"  series strip:       {series_checked['lattice_strip']}")
    print(f"  any_log_sqrt_claim: {any_log_sqrt}")
    print(f"  n6 full-core Φ steps: {n6_steps}")
    print(f"  H1 (ring cap + pool n(n-1)):        "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (fixed-n interiors exist):       "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (no log/√n intermediate law):    "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  H4 (partial pools collapse):        "
          f"{'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"  H5 (discrete steps at n=6):         "
          f"{'SUPPORTED' if h5 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  log/√n intermediate law? {'YES' if verdict_word == 'INTERMEDIATE_LAW' else 'NO'}")
    print(f"  stable full-core interiors (not only poles)? {'YES' if h2 else 'NO'}")
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
            "name", "family", "n", "param", "structure", "whole_phi_mip",
            "core", "core_phi", "n_core", "full_core", "interior", "seconds",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "name": r["name"],
                "family": r["family"],
                "n": r["n"],
                "param": r.get("param", ""),
                "structure": r["structure"],
                "whole_phi_mip": f"{r['whole_phi_mip']:.6f}",
                "core": "|".join(r["core"]),
                "core_phi": f"{r['core_phi']:.6f}",
                "n_core": r["n_core"],
                "full_core": str(r["full_core"]),
                "interior": str(r["interior"]),
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
            "n_interiors": len(interiors),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
