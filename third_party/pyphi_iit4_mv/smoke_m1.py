#!/usr/bin/env python3
"""M1 smoke: ternary Network construct + SBS preserve; Φ blocker locus.

Run from repo root:
  python third_party/pyphi_iit4_mv/smoke_m1.py
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
from pyphi import Network

from pyphi_iit4_mv import MultivaluedNetwork, probe_exact_phi_blocker
from pyphi_iit4_mv.conditional_independence import encode_state


def ternary_sbs(n: int, next_fn) -> np.ndarray:
    base = 3
    N = base**n
    sbs = np.zeros((N, N), dtype=float)
    for i in range(N):
        st = tuple((i // base**k) % base for k in range(n))
        ns = next_fn(st)
        j = encode_state(ns, (base,) * n)
        sbs[i, j] = 1.0
    return sbs


def assert_stock_rejects(sbs, labels):
    try:
        Network(sbs, node_labels=labels)
        return False, "stock unexpectedly accepted"
    except Exception as e:  # noqa: BLE001
        return True, f"{type(e).__name__}: {e}"


def main() -> int:
    t0 = time.time()
    print("M1 SMOKE — SBS-native ExplicitTPM (pyphi_iit4_mv)")
    print("=" * 72)

    # 2-node ternary swap: A'=B, B'=A
    sbs2 = ternary_sbs(2, lambda st: (st[1], st[0]))
    rejected, err = assert_stock_rejects(sbs2, ("A", "B"))
    print(f"  stock pin rejects (9,9):   {rejected}")
    if err:
        print(f"    ({err[:100]})")

    net2 = MultivaluedNetwork(sbs2, [3, 3], node_labels=("A", "B"))
    preserved = np.allclose(net2.sbs(), sbs2)
    no_collapse = net2.tpm.shape == (9, 9) and net2.num_states == 9
    print(f"  MV Network (9,9):          OK size={net2.size} states={net2.num_states}")
    print(f"  SBS preserved:             {preserved}")
    print(f"  no log2 collapse:          {no_collapse}")

    # 3-node ternary min-AND triad (agenda #1 failing case)
    sbs3 = ternary_sbs(3, lambda st: (st[1], min(st[0], st[2]), st[1]))
    net3 = MultivaluedNetwork(sbs3, [3, 3, 3], node_labels=("W", "S", "C"))
    ok3 = net3.tpm.shape == (27, 27) and np.allclose(net3.sbs(), sbs3)
    print(f"  MV Network (27,27):        {'OK' if ok3 else 'FAIL'}")

    # Φ attempt — expect explicit M2 blocker, not proxy Φ
    blocker = probe_exact_phi_blocker(net2, (0, 0))
    print(f"  exact Φ blocked:           {blocker['blocked']}")
    print(f"  blocker locus:             {blocker['locus'][:120]}")
    print(f"  error:                     {blocker['error_type']}: {blocker['error'][:100]}")

    # Refuse CI-off narrative: we never toggle VALIDATE_CONDITIONAL_INDEPENDENCE
    print("  CI-off log2 trap used:     False  (SBS-native path only)")

    grid = rejected and preserved and no_collapse and ok3 and blocker["blocked"]
    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print(
        "  best next:            M2 mixed-radix condition_tpm + "
        "repertoire / Subsystem (see INSTRUMENT_GAP.md)"
    )
    print()
    if grid:
        print(
            "verdict: M1_GREEN — ternary MultivaluedNetwork constructs; "
            "SBS preserved without int(log2) collapse; exact Φ still "
            "blocked past ExplicitTPM at backward_tpm/"
            "probability_of_current_state (treats SBS as binary SBN; M2)"
        )
        print(
            "reading: M1_GREEN — vendored pin path third_party/pyphi_iit4_mv; "
            "stock binary IIT-4.0 unchanged; #1 science still NOT_TESTABLE "
            "until M2–M3"
        )
    else:
        print("verdict: M1_FAIL — see checks above")
        print("reading: M1_FAIL")
    print(f"elapsed {time.time() - t0:.1f}s")
    print("=" * 72)
    return 0 if grid else 1


if __name__ == "__main__":
    raise SystemExit(main())
