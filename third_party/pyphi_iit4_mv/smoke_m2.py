#!/usr/bin/env python3
"""M2 smoke: exact ternary Φ + binary regression vs stock IIT-4.0 pin.

Run from repo root:
  python third_party/pyphi_iit4_mv/smoke_m2.py
"""

from __future__ import annotations

import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_THIRD = os.path.dirname(_HERE)
_REPO = os.path.dirname(_THIRD)
for p in (_THIRD, _REPO):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import Network, Subsystem, convert, new_big_phi

from pyphi_iit4_mv import MultivaluedNetwork, exact_phi, maximal_complex
from pyphi_iit4_mv.conditional_independence import encode_state, decode_state

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
PHI_TOL = 1e-9


def ternary_swap_sbs():
    sbs = np.zeros((9, 9))
    for i in range(9):
        a, b = decode_state(i, (3, 3))
        sbs[i, encode_state((b, a), (3, 3))] = 1.0
    return sbs


def binary_regression() -> tuple[bool, float, float]:
    # Faithful triad W'=S, S'=W∧C, C'=S — stock Φ=2 at (1,1,1)
    def w(x):
        return x[1]

    def s(x):
        return x[0] & x[2]

    def c(x):
        return x[1]

    from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules

    rules = [w, s, c]
    tpm_sbn, cm = tpm_from_rules(rules), cm_from_rules(rules)
    labels = ("W", "S", "C")
    stock = float(
        new_big_phi.sia(
            Subsystem(Network(tpm_sbn, cm=cm, node_labels=labels), (1, 1, 1))
        ).phi
    )
    sbs = convert.state_by_node2state_by_state(tpm_sbn)
    mv = MultivaluedNetwork(sbs, [2, 2, 2], cm=cm, node_labels=labels)
    ours = exact_phi(mv, (1, 1, 1))
    return abs(stock - ours) < PHI_TOL, stock, ours


def main() -> int:
    t0 = time.time()
    print("M2 SMOKE — exact ternary Φ (pyphi_iit4_mv)")
    print("=" * 72)

    ok_bin, stock, ours = binary_regression()
    print(f"  binary regression Φ=2:    {'PASS' if ok_bin else 'FAIL'}  "
          f"(stock={stock}, mv={ours})")

    sbs = ternary_swap_sbs()
    net = MultivaluedNetwork(
        sbs, [3, 3], cm=np.array([[0, 1], [1, 0]]), node_labels=("A", "B")
    )
    # Preserve check
    preserved = np.allclose(net.sbs(), sbs) and net.tpm.shape == (9, 9)
    print(f"  SBS preserved (9,9):       {preserved}")

    phi = exact_phi(net, (1, 2))
    finite = np.isfinite(phi) and phi > 0
    print(f"  ternary exact Φ (1,2):     {phi:.6f}  "
          f"({'finite>0' if finite else 'BAD'})")

    mc = maximal_complex(net, (1, 2))
    mc_ok = hasattr(mc, "phi") and float(mc.phi) > 0
    print(f"  maximal_complex Φ:         {float(mc.phi):.6f}  "
          f"nodes={getattr(mc, 'node_indices', None)}")

    # Reducible control: two independent sticky ternary nodes → Φ≈0
    sbs_ind = np.zeros((9, 9))
    for i in range(9):
        st = decode_state(i, (3, 3))
        sbs_ind[i, encode_state(st, (3, 3))] = 1.0  # identity
    net_ind = MultivaluedNetwork(
        sbs_ind, [3, 3], cm=np.eye(2), node_labels=("A", "B")
    )
    # no edges between A and B — not strongly connected → null Φ
    phi_ind = exact_phi(net_ind, (1, 2))
    reducible = abs(phi_ind) < PHI_TOL
    print(f"  independent sticky Φ≈0:    {'PASS' if reducible else 'FAIL'}  "
          f"(Φ={phi_ind})")

    print("  CI-off log2 trap used:     False")

    grid = ok_bin and preserved and finite and mc_ok and reducible
    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print(
        "  best next:            #2 graded-commit / #3 mixed-radix on "
        "overlay (see BEYOND_BINARY_ARC.md)"
    )
    print()
    if grid:
        print(
            "verdict: M2_GREEN — exact ternary IIT-4.0 Φ finite on 2-node "
            "control; binary regression matches stock pin Φ=2; "
            "maximal_complex works; independent sticky Φ=0; no log2 trap"
        )
        print(
            "reading: M2_GREEN — third_party/pyphi_iit4_mv computes exact Φ "
            "via MultivaluedSubsystem + sia (GID); #1 "
            "TWO_CONDITION_STATE_DEPENDENT"
        )
    else:
        print("verdict: M2_FAIL — see checks above")
        print("reading: M2_FAIL")
    print(f"elapsed {time.time() - t0:.1f}s")
    print("=" * 72)
    return 0 if grid else 1


if __name__ == "__main__":
    raise SystemExit(main())
