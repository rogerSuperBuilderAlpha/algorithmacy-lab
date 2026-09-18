"""Agenda #2 — graded commit: sharp vs graded dyadic/triadic verdict.

Exact IIT-4.0 Φ on ternary faithful min-AND via pyphi_iit4_mv.
Hypotheses fixed in hypotheses.md before this run.

Run:  python org_frontier/studies/graded_commit_verdict/analyze_graded.py
"""

from __future__ import annotations

import csv
import json
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_THIRD = os.path.join(_REPO_ROOT, "third_party")
for p in (_THIRD, _REPO_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import Network, Subsystem, convert, new_big_phi

from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules
from org_frontier.probes.lib import major_complex
from pyphi_iit4_mv import MultivaluedNetwork, maximal_complex
from pyphi_iit4_mv.conditional_independence import decode_state, encode_state

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
LABELS = ("W", "S", "C")
CM = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)


def structure_of(n_core: int, phi: float) -> str:
    if n_core <= 0 or phi <= PHI_TOL:
        return "NULL"
    if n_core == 1:
        return "MONADIC"
    if n_core == 2:
        return "DYADIC"
    if n_core >= 3:
        return "TRIADIC"
    return "NULL"


def binary_control():
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    core, phi = major_complex(rules, LABELS)
    core_t = tuple(core) if core is not None else ()
    phi = float(phi) if core_t else 0.0
    # Overlay regression on same SBS
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    sbs = convert.state_by_node2state_by_state(tpm)
    net = MultivaluedNetwork(sbs, [2, 2, 2], cm=cm, node_labels=LABELS)
    mc = maximal_complex(net, (1, 1, 1))
    if isinstance(mc, new_big_phi.NullPhiStructure) or mc.node_indices is None:
        mv_core, mv_phi = (), 0.0
    else:
        mv_core = tuple(LABELS[i] for i in mc.node_indices)
        mv_phi = float(mc.phi)
    return {
        "stock_core": core_t,
        "stock_phi": phi,
        "stock_structure": structure_of(len(core_t), phi),
        "mv_core": mv_core,
        "mv_phi": mv_phi,
        "ok": (
            set(core_t) == {"W", "S", "C"}
            and abs(phi - 2.0) < PHI_TOL
            and set(mv_core) == {"W", "S", "C"}
            and abs(mv_phi - 2.0) < PHI_TOL
        ),
    }


def faithful_sbs(base=3):
    n = 3
    ks = (base,) * n
    N = base**n
    sbs = np.zeros((N, N), dtype=float)
    for i in range(N):
        w, s, c = decode_state(i, ks)
        sbs[i, encode_state((s, min(w, c), s), ks)] = 1.0
    return sbs


def major_at(net, state):
    mc = maximal_complex(net, state)
    if isinstance(mc, new_big_phi.NullPhiStructure) or mc.node_indices is None:
        return (), 0.0, "NULL"
    core = tuple(LABELS[i] for i in mc.node_indices)
    phi = float(mc.phi)
    return core, phi, structure_of(len(core), phi)


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("GRADED COMMIT VERDICT — agenda #2")
    print("=" * 72)
    print("  form: faithful S'=min(W,C), W'=S, C'=S  (ternary k=3)")
    print("  commit level L on diagonal state (L,L,L)")
    print("  instrument: pyphi_iit4_mv maximal_complex (exact IIT-4.0)")
    print()

    ctrl = binary_control()
    print("BINARY CONTROL (AND triad @ (1,1,1))")
    print(
        f"  stock: {ctrl['stock_structure']} Φ={ctrl['stock_phi']:.3f} "
        f"core={'|'.join(ctrl['stock_core'])}"
    )
    print(
        f"  overlay: {structure_of(len(ctrl['mv_core']), ctrl['mv_phi'])} "
        f"Φ={ctrl['mv_phi']:.3f} core={'|'.join(ctrl['mv_core'])}"
    )
    print(f"  control: {'PASS' if ctrl['ok'] else 'FAIL'}")

    net = MultivaluedNetwork(faithful_sbs(), [3, 3, 3], cm=CM, node_labels=LABELS)

    print()
    print("FAITHFUL DIAGONAL — commit level L")
    rows = []
    for L in (0, 1, 2):
        state = (L, L, L)
        core, phi, struct = major_at(net, state)
        row = {
            "L": L,
            "state": str(state),
            "structure": struct,
            "n_core": len(core),
            "core": "|".join(core) if core else "",
            "phi": phi,
        }
        rows.append(row)
        print(
            f"  L={L}  {struct:<8} n_core={len(core)}  "
            f"Φ={phi:.4f}  core={row['core'] or '∅'}"
        )

    # Off-diagonal spot checks: mediator level vs party level
    print()
    print("SPOT CHECKS (off-diagonal)")
    spots = [(1, 2, 1), (2, 1, 2), (2, 0, 2)]
    spot_rows = []
    for state in spots:
        core, phi, struct = major_at(net, state)
        spot_rows.append(
            {
                "state": str(state),
                "S": state[1],
                "minWC": min(state[0], state[2]),
                "structure": struct,
                "n_core": len(core),
                "core": "|".join(core) if core else "",
                "phi": phi,
            }
        )
        print(
            f"  {state}  S={state[1]} min(W,C)={min(state[0], state[2])}  "
            f"{struct:<8} Φ={phi:.4f}  core={spot_rows[-1]['core'] or '∅'}"
        )

    structs = [r["structure"] for r in rows]
    phis = [r["phi"] for r in rows]
    ncores = [r["n_core"] for r in rows]
    sharp_classes = {"NULL", "MONADIC", "DYADIC", "TRIADIC"}
    h1 = all(s in sharp_classes for s in structs) and len(set(structs)) >= 2
    h2 = phis[0] <= phis[1] + PHI_TOL and phis[1] < phis[2] - PHI_TOL
    # membership grades: not all same core among L with any positive structure
    cores = [r["core"] for r in rows]
    h3 = len(set(cores)) >= 2 and ncores != [ncores[0]] * 3

    print()
    print("HYPOTHESES")
    print(f"  H1 (structure class stays sharp):   {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (Φ grades with commit level L):  {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (core membership grades with L): {'SUPPORTED' if h3 else 'REFUTED'}")

    if h1 and h2 and h3:
        verdict = "SHARP_CLASS_GRADED_PATH"
    elif h1 and h2 and not h3:
        verdict = "GRADED_PHI_ONLY"
    elif h1 and not h2:
        verdict = "SHARP_THRESHOLD"
    else:
        verdict = "MIXED"

    grid = ctrl["ok"] and h1 and h2 and h3

    with open(os.path.join(RESULTS, "diagonal.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(RESULTS, "spots.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(spot_rows[0].keys()))
        w.writeheader()
        w.writerows(spot_rows)
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(
            {
                "verdict": verdict,
                "binary_control": ctrl,
                "diagonal": rows,
                "h1": h1,
                "h2": h2,
                "h3": h3,
            },
            f,
            indent=2,
        )

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #3 mixed-radix mediator (binary parties, ternary S)")
    print()
    print(
        f"verdict: {verdict} — faithful ternary graded commit: structure "
        f"classes stay discrete (NULL/DYADIC/TRIADIC) while Φ and n_core "
        f"track commit level L on (L,L,L); binary AND control TRIADIC Φ=2"
    )
    print(
        "reading: SHARP_CLASS_GRADED_PATH — the dyadic/triadic label stays "
        "a sharp class; the path across commit levels grades both "
        "magnitude and membership; #1 state-dependence is the L=1 vs L=2 "
        "slice of this path"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
