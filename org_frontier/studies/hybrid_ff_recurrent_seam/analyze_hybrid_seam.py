"""Hybrid feedforward+recurrent seam (RESEARCH_AGENDA_V3 #7).

One recurrent cycle feeding a feedforward chain — does the major-complex
locus still obey V2 #15 closure-decides-locus, or does the hybrid violate
it? Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/hybrid_ff_recurrent_seam/analyze_hybrid_seam.py
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


def _or_of(indices):
    idxs = tuple(indices)

    def f(x, idxs=idxs):
        v = 0
        for i in idxs:
            v |= x[i]
        return v

    return f


def _copy(i):
    return lambda x, i=i: x[i]


def triad_control():
    labels = ("W", "S", "C")
    rules = [
        lambda x: x[1],
        lambda x: x[0] & x[2],
        lambda x: x[1],
    ]
    zone = {lab: "recurrent" for lab in labels}
    return labels, rules, zone, {"family": "control", "seam": "n/a"}


def hub_chain_L2():
    """Pure FF control (V2 #15 / q148): top 2-cycle + one FF AND gate."""
    labels = ("H0", "P0", "H1", "P1")
    rules = [
        _copy(1),  # H0' = P0
        _copy(0),  # P0' = H0
        _and_of([0, 3]),  # H1' = H0 ∧ P1
        _copy(2),  # P1' = H1
    ]
    zone = {"H0": "recurrent", "P0": "recurrent", "H1": "ff", "P1": "ff"}
    return labels, rules, zone, {"family": "hub_chain", "seam": "AND", "L": 2}


def hybrid_triad_ff(seam: str):
    """Classic triad (W,S,C) feeds FF pair (H1,P1) via seam at S.

    W'=S; S'=W∧C; C'=S; H1'= seam(S,P1); P1'=H1.
    Recurrent zone = {W,S,C}; FF = {H1,P1}.
    """
    labels = ("W", "S", "C", "H1", "P1")
    if seam == "AND":
        h1 = _and_of([1, 4])  # S ∧ P1
    elif seam == "OR":
        h1 = _or_of([1, 4])
    else:
        raise KeyError(seam)
    rules = [
        _copy(1),  # W' = S
        _and_of([0, 2]),  # S' = W ∧ C
        _copy(1),  # C' = S
        h1,
        _copy(3),  # P1' = H1
    ]
    zone = {
        "W": "recurrent",
        "S": "recurrent",
        "C": "recurrent",
        "H1": "ff",
        "P1": "ff",
    }
    return labels, rules, zone, {"family": "hybrid_triad_ff", "seam": seam}


def hybrid_tree_ff(seam: str):
    """Recurrent tree d=1,b=2 (S0,L0,L1) feeds FF (H1,P1).

    S0'=L0∧L1; L0'=S0; L1'=S0; H1'=seam(S0,P1); P1'=H1.
    """
    labels = ("S0", "L0", "L1", "H1", "P1")
    if seam == "AND":
        h1 = _and_of([0, 4])
    elif seam == "OR":
        h1 = _or_of([0, 4])
    else:
        raise KeyError(seam)
    rules = [
        _and_of([1, 2]),  # S0
        _copy(0),  # L0
        _copy(0),  # L1
        h1,
        _copy(3),  # P1
    ]
    zone = {
        "S0": "recurrent",
        "L0": "recurrent",
        "L1": "recurrent",
        "H1": "ff",
        "P1": "ff",
    }
    return labels, rules, zone, {"family": "hybrid_tree_ff", "seam": seam}


def run_cell(name, labels, rules, zone, meta):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    core_zones = sorted({zone[lab] for lab in core_t if lab in zone})
    rec_nodes = {lab for lab, z in zone.items() if z == "recurrent"}
    ff_nodes = {lab for lab, z in zone.items() if z == "ff"}
    core_set = set(core_t)
    meets_ff = bool(core_set & ff_nodes)
    in_rec_only = bool(core_set) and core_set.issubset(rec_nodes)
    spans_recurrent = rec_nodes.issubset(core_set) if rec_nodes else False
    top_local_hub = core_set.issubset({"H0", "P0"}) if meta["family"] == "hub_chain" else False
    if in_rec_only and not meets_ff:
        locus = "holds"
    elif meets_ff:
        locus = "violates"
    else:
        locus = "empty_or_other"
    return {
        **meta,
        "name": name,
        "n": len(labels),
        "structure": v.structure,
        "whole_phi_mip": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "core_phi": cp,
        "n_core": len(core_t),
        "core_zones": "|".join(core_zones) if core_zones else "",
        "meets_ff": int(meets_ff),
        "in_rec_only": int(in_rec_only),
        "spans_recurrent": int(spans_recurrent),
        "top_local_hub": int(top_local_hub),
        "locus": locus,
        "seconds": round(time.time() - t0, 2),
    }


def fmt(row):
    return (
        f"{row['name']:18s} {row['structure']:8s} "
        f"whole\u03a6={row['whole_phi_mip']:.3f}  "
        f"core=({row['core']})  core\u03a6={row['core_phi']:.3f}  "
        f"zones={row['core_zones'] or '-'}  locus={row['locus']}  "
        f"t={row['seconds']:.1f}s"
    )


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    builders = [
        ("triad", triad_control),
        ("hub_L2", hub_chain_L2),
        ("hy_triad_AND", lambda: hybrid_triad_ff("AND")),
        ("hy_tree_AND", lambda: hybrid_tree_ff("AND")),
        ("hy_triad_OR", lambda: hybrid_triad_ff("OR")),
    ]

    for name, builder in builders:
        labels, rules, zone, meta = builder()
        rows.append(run_cell(name, labels, rules, zone, meta))

    path = os.path.join(RESULTS, "panel.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("HYBRID FF+RECURRENT SEAM — V3 #7")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}

    triad = by["triad"]
    triad_ok = triad["structure"] == "triadic" and near(triad["core_phi"], 2.0)
    hub = by["hub_L2"]
    hub_ok = bool(hub["top_local_hub"]) and hub["core"] in ("H0|P0", "P0|H0")
    # core order from major_complex may vary; check set
    hub_ok = set(hub["core"].split("|") if hub["core"] else ()) == {"H0", "P0"}
    h1 = triad_ok and hub_ok
    print(f"H1 (triad \u03a6=2 + hub_L2 top-local):           {'SUPPORTED' if h1 else 'REFUTED'}")
    print(
        f"  triad_ok={triad_ok} hub_ok={hub_ok} "
        f"(hub core={hub['core']} top_local={bool(hub['top_local_hub'])})"
    )

    and_cells = [by["hy_triad_AND"], by["hy_tree_AND"]]
    and_holds = all(c["locus"] == "holds" for c in and_cells)
    and_violates = all(c["locus"] == "violates" for c in and_cells)
    if and_holds:
        and_panel = "AND_HOLDS"
    elif and_violates:
        and_panel = "AND_VIOLATES"
    else:
        and_panel = "AND_MIXED"
    h2 = and_panel in ("AND_HOLDS", "AND_VIOLATES", "AND_MIXED")
    print(f"H2 (hybrid AND locus named):               {'SUPPORTED' if h2 else 'REFUTED'}")
    print(
        f"  hy_triad_AND locus={by['hy_triad_AND']['locus']} "
        f"core=({by['hy_triad_AND']['core']})  "
        f"hy_tree_AND locus={by['hy_tree_AND']['locus']} "
        f"core=({by['hy_tree_AND']['core']})  and_panel={and_panel}"
    )

    or_cell = by["hy_triad_OR"]
    or_locus = or_cell["locus"]
    h3 = or_locus in ("holds", "violates", "empty_or_other")
    print(f"H3 (OR seam locus reported):               {'SUPPORTED' if h3 else 'REFUTED'}")
    print(
        f"  hy_triad_OR locus={or_locus} core=({or_cell['core']}) "
        f"structure={or_cell['structure']} core\u03a6={or_cell['core_phi']:.3f}"
    )

    if not h1:
        token = "CONTROLS_FAIL"
    elif and_panel == "AND_HOLDS":
        token = "CLOSURE_HOLDS_HYBRID"
    elif and_panel == "AND_VIOLATES":
        token = "CLOSURE_VIOLATED_HYBRID"
    else:
        token = "MIXED_SEAM_LOCUS"

    h4 = h1 and h2 and token != "CONTROLS_FAIL"
    print(f"H4 (panel closed):                         {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")

    if token == "CLOSURE_HOLDS_HYBRID":
        print(
            "reading: CLOSURE_HOLDS_HYBRID \u2014 hybrid FF+recurrent AND seams keep "
            "the major complex inside the recurrent zone (FF tail excluded); "
            "V2 #15 closure-decides-locus survives the hybrid"
        )
    elif token == "CLOSURE_VIOLATED_HYBRID":
        print(
            "reading: CLOSURE_VIOLATED_HYBRID \u2014 hybrid AND seams pull FF nodes "
            "into the major complex; violates V2 #15 closure-decides-locus"
        )
    elif token == "MIXED_SEAM_LOCUS":
        print(
            "reading: MIXED_SEAM_LOCUS \u2014 hybrid AND cells disagree on whether "
            "FF enters the core; closure rule does not apply uniformly"
        )
    else:
        print(f"reading: {token}")

    print(f"wrote {path}")


if __name__ == "__main__":
    main()
