"""n=4 dual-mediator template census (RESEARCH_AGENDA_V3 #1).

Series cascade / parallel mediators / mediator-of-mediators — sixth
template, or do triadic cores factor into the five n=3 templates?
Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/dual_mediator_template_census/analyze_dual_mediator.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from itertools import combinations, permutations, product

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.studies.template_coverage_census.signatures import match_templates

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

FIVE = frozenset({"relay", "conjunctive", "additive", "free", "parity"})
KNOWN_PHI = (0.5, 2.0, 4.0)


def _copy(i):
    return lambda x, i=i: x[i]


def _and2(i, j):
    return lambda x, i=i, j=j: x[i] & x[j]


def _or2(i, j):
    return lambda x, i=i, j=j: x[i] | x[j]


def _xor2(i, j):
    return lambda x, i=i, j=j: x[i] ^ x[j]


def remap_rules(old_rules, perm):
    """perm[new_i] = old_i."""
    out = []
    for new_i, old_i in enumerate(perm):

        def r(x, old_i=old_i, perm=perm):
            old_x = [0] * len(perm)
            for ni, oi in enumerate(perm):
                old_x[oi] = x[ni]
            return old_rules[old_i](old_x)

        out.append(r)
    return out


def classify_triad(rules3):
    hits = set()
    for perm in permutations(range(3)):
        hits |= match_templates(remap_rules(rules3, perm))
    return hits & FIVE


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def is_known_phi(phi):
    return any(near(phi, k) for k in KNOWN_PHI)


def induced_closed(rules, n, comb):
    for oi in comb:
        table = {}
        for state in product([0, 1], repeat=n):
            key = tuple(state[i] for i in comb)
            table.setdefault(key, set()).add(int(rules[oi](state)))
        if any(len(s) > 1 for s in table.values()):
            return False
    return True


def make_induced(rules, n, comb):
    out = []
    for oi in comb:

        def make(oi=oi, comb=comb, n=n):
            def r(x):
                full = [0] * n
                for k, ix in enumerate(comb):
                    full[ix] = x[k]
                return rules[oi](full)

            return r

        out.append(make())
    return out


def triad_and():
    labels = ("W", "S", "C")
    rules = [_copy(1), _and2(0, 2), _copy(1)]
    return labels, rules, {"family": "control", "arch": "triad_and"}


def triad_xor():
    labels = ("W", "S", "C")
    rules = [_copy(1), _xor2(0, 2), _copy(1)]
    return labels, rules, {"family": "control", "arch": "triad_xor"}


def series_aa():
    labels = ("W", "C", "S1", "S2")
    rules = [_copy(2), _copy(3), _and2(0, 3), _and2(1, 2)]
    return labels, rules, {"family": "series", "arch": "series_AA"}


def series_ax():
    labels = ("W", "C", "S1", "S2")
    rules = [_copy(2), _copy(3), _and2(0, 3), _xor2(1, 2)]
    return labels, rules, {"family": "series", "arch": "series_AX"}


def series_xx():
    labels = ("W", "C", "S1", "S2")
    rules = [_copy(2), _copy(3), _xor2(0, 3), _xor2(1, 2)]
    return labels, rules, {"family": "series", "arch": "series_XX"}


def series_chain():
    labels = ("W", "M1", "M2", "C")
    rules = [_copy(3), _copy(0), _and2(1, 3), _copy(2)]
    return labels, rules, {"family": "series", "arch": "series_chain"}


def par_aa_s1():
    labels = ("W", "C", "S1", "S2")
    rules = [_copy(2), _copy(2), _and2(0, 1), _and2(0, 1)]
    return labels, rules, {"family": "parallel", "arch": "par_AA_s1"}


def par_ax_s1():
    labels = ("W", "C", "S1", "S2")
    rules = [_copy(2), _copy(2), _and2(0, 1), _xor2(0, 1)]
    return labels, rules, {"family": "parallel", "arch": "par_AX_s1"}


def par_xx_s1():
    labels = ("W", "C", "S1", "S2")
    rules = [_copy(2), _copy(2), _xor2(0, 1), _xor2(0, 1)]
    return labels, rules, {"family": "parallel", "arch": "par_XX_s1"}


def par_aa_and():
    labels = ("W", "C", "S1", "S2")
    rules = [_and2(2, 3), _and2(2, 3), _and2(0, 1), _and2(0, 1)]
    return labels, rules, {"family": "parallel", "arch": "par_AA_and"}


def par_aa_or():
    labels = ("W", "C", "S1", "S2")
    rules = [_or2(2, 3), _or2(2, 3), _and2(0, 1), _and2(0, 1)]
    return labels, rules, {"family": "parallel", "arch": "par_AA_or"}


def mom_copy():
    labels = ("W", "C", "M1", "M0")
    rules = [_copy(3), _copy(3), _and2(0, 1), _copy(2)]
    return labels, rules, {"family": "mom", "arch": "mom_copy"}


def mom_gate():
    labels = ("A", "B", "M1", "M0")
    rules = [_copy(3), _copy(3), _copy(0), _and2(2, 1)]
    return labels, rules, {"family": "mom", "arch": "mom_gate"}


def mom_two_mid():
    labels = ("A", "M1", "M2", "M0")
    rules = [_copy(3), _copy(0), _copy(0), _and2(1, 2)]
    return labels, rules, {"family": "mom", "arch": "mom_two_mid"}


def mom_xor():
    labels = ("W", "C", "M1", "M0")
    rules = [_copy(3), _copy(3), _xor2(0, 1), _copy(2)]
    return labels, rules, {"family": "mom", "arch": "mom_xor"}


FORMS = [
    triad_and,
    triad_xor,
    series_aa,
    series_ax,
    series_xx,
    series_chain,
    par_aa_s1,
    par_ax_s1,
    par_xx_s1,
    par_aa_and,
    par_aa_or,
    mom_copy,
    mom_gate,
    mom_two_mid,
    mom_xor,
]


def run_cell(builder):
    labels, rules, meta = builder()
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    n = len(labels)

    triad_rows = []
    escapees = []
    for comb in combinations(range(n), 3):
        labs = tuple(labels[i] for i in comb)
        closed = induced_closed(rules, n, comb)
        if not closed:
            triad_rows.append(
                {
                    "subset": "|".join(labs),
                    "closed": 0,
                    "structure": "",
                    "phi": "",
                    "templates": "",
                    "escapee": 0,
                }
            )
            continue
        r3 = make_induced(rules, n, comb)
        vv = verdict(r3, labs)
        hits = classify_triad(r3)
        escapee = int(vv.structure == "triadic" and not hits)
        if escapee:
            escapees.append("|".join(labs))
        triad_rows.append(
            {
                "subset": "|".join(labs),
                "closed": 1,
                "structure": vv.structure,
                "phi": f"{float(vv.max_phi):.6f}",
                "templates": "|".join(sorted(hits)) if hits else "",
                "escapee": escapee,
            }
        )

    return {
        **meta,
        "name": meta["arch"],
        "n": n,
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "core_phi": cp,
        "n_core": len(core_t),
        "n_escapees": len(escapees),
        "escapees": ";".join(escapees),
        "known_phi": int(is_known_phi(cp)) if core_t else 1,
        "seconds": round(time.time() - t0, 2),
        "triads": triad_rows,
    }


def fmt(row):
    return (
        f"{row['name']:14s} {row['structure']:8s} "
        f"whole\u03a6={row['whole_phi']:.3f}  "
        f"core=({row['core']})  core\u03a6={row['core_phi']:.3f}  "
        f"n_core={row['n_core']}  escapees={row['n_escapees']}  "
        f"t={row['seconds']:.1f}s"
    )


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []
    for builder in FORMS:
        rows.append(run_cell(builder))

    panel_path = os.path.join(RESULTS, "panel.csv")
    fields = [
        "family",
        "arch",
        "name",
        "n",
        "structure",
        "whole_phi",
        "core",
        "core_phi",
        "n_core",
        "n_escapees",
        "escapees",
        "known_phi",
        "seconds",
    ]
    with open(panel_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    triad_path = os.path.join(RESULTS, "triads.csv")
    with open(triad_path, "w", newline="") as f:
        tf = [
            "arch",
            "subset",
            "closed",
            "structure",
            "phi",
            "templates",
            "escapee",
        ]
        w = csv.DictWriter(f, fieldnames=tf)
        w.writeheader()
        for r in rows:
            for t in r["triads"]:
                w.writerow({"arch": r["name"], **t})

    print("DUAL-MEDIATOR TEMPLATE CENSUS — V3 #1")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}

    ta, tx = by["triad_and"], by["triad_xor"]
    ta_ok = (
        ta["structure"] == "triadic"
        and near(ta["core_phi"], 2.0)
        and ta["n_escapees"] == 0
        and any(t["closed"] and "conjunctive" in t["templates"] for t in ta["triads"])
    )
    tx_ok = (
        tx["structure"] == "triadic"
        and near(tx["core_phi"], 0.5)
        and tx["n_escapees"] == 0
        and any(t["closed"] and "parity" in t["templates"] for t in tx["triads"])
    )
    h1 = ta_ok and tx_ok
    print(f"H1 (AND \u03a6=2 + XOR \u03a6=0.5 anchors):           {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  triad_and_ok={ta_ok} triad_xor_ok={tx_ok}")

    dual = [r for r in rows if r["family"] != "control"]
    closed_triadic = []
    for r in dual:
        for t in r["triads"]:
            if t["closed"] and t["structure"] == "triadic":
                closed_triadic.append((r["name"], t))
    escapee_list = [(n, t) for n, t in closed_triadic if t["escapee"]]
    h2 = len(escapee_list) == 0 and len(closed_triadic) > 0
    print(f"H2 (no sixth among closed triadic cores):  {'SUPPORTED' if h2 else 'REFUTED'}")
    print(
        f"  closed_triadic={len(closed_triadic)} escapees={len(escapee_list)} "
        f"detail={[e[0] + ':' + e[1]['subset'] for e in escapee_list]}"
    )

    size4 = [r for r in dual if r["n_core"] == 4]
    h3 = all(r["known_phi"] and r["n_escapees"] == 0 for r in size4) if size4 else True
    print(f"H3 (size-4 cores are known-phi products):   {'SUPPORTED' if h3 else 'REFUTED'}")
    print(
        "  size4=["
        + ", ".join(f"{r['name']}:\u03a6={r['core_phi']:.3f}" for r in size4)
        + "]"
    )

    if not h1:
        token = "CONTROLS_FAIL"
    elif not h2:
        token = "SIXTH_TEMPLATE"
    elif not h3:
        token = "NOVEL_TETRAD"
    else:
        token = "FACTORS_INTO_FIVE"

    h4 = token == "FACTORS_INTO_FIVE"
    print(f"H4 (panel closed):                         {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")
    if token == "FACTORS_INTO_FIVE":
        print(
            "reading: FACTORS_INTO_FIVE \u2014 n=4 dual-mediator series / parallel / "
            "mediator-of-mediators yield no sixth template; closed triadic cores "
            "match the five n=3 templates; size-4 cores sit on known landmark "
            "\u03a6 (0.5 / 2 / 4=2+2 product)"
        )
    else:
        print(f"reading: {token}")
    print(f"wrote {panel_path}")
    print(f"wrote {triad_path}")


if __name__ == "__main__":
    main()
