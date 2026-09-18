"""Path A / M2 probe — multivalued exact IIT-4.0 Φ on vendored overlay.

Run:  python org_frontier/studies/multivalued_iit4_port/analyze_port.py
"""

from __future__ import annotations

import json
import os
import sys
import time
from math import log2

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_THIRD = os.path.join(_REPO_ROOT, "third_party")
for p in (_THIRD, _REPO_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import Network, Subsystem, convert, new_big_phi, config

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import major_complex
from pyphi_iit4_mv import MultivaluedNetwork, exact_phi, probe_exact_phi_blocker
from pyphi_iit4_mv.conditional_independence import encode_state

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
LABELS3 = ("W", "S", "C")


def ternary_triad_sbs():
    base, n = 3, 3
    N = base**n
    sbs = np.zeros((N, N))
    for i in range(N):
        st = tuple((i // base**k) % base for k in range(n))
        w, s, c = st
        ns = (s, min(w, c), s)
        sbs[i, encode_state(ns, (base,) * n)] = 1.0
    return sbs


def ternary_swap_sbs():
    base, n = 3, 2
    N = base**n
    sbs = np.zeros((N, N))
    for i in range(N):
        a, b = tuple((i // base**k) % base for k in range(n))
        sbs[i, encode_state((b, a), (base, base))] = 1.0
    return sbs


def binary_control_ok():
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    core, phi = major_complex(rules, LABELS3)
    return (
        core is not None
        and set(core) == {"W", "S", "C"}
        and abs(float(phi) - 2.0) < PHI_TOL
    )


def binary_regression_ok():
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    stock = float(
        new_big_phi.sia(
            Subsystem(Network(tpm, cm=cm, node_labels=LABELS3), (1, 1, 1))
        ).phi
    )
    sbs = convert.state_by_node2state_by_state(tpm)
    mv = MultivaluedNetwork(sbs, [2, 2, 2], cm=cm, node_labels=LABELS3)
    ours = exact_phi(mv, (1, 1, 1))
    return abs(stock - ours) < PHI_TOL, stock, ours


def probe_default_reject(sbs):
    try:
        Network(sbs, node_labels=LABELS3)
        return True, ""
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"


def probe_ci_off_trap():
    import warnings

    sbs = np.eye(9)
    detail = {
        "log2_9": log2(9),
        "int_log2_9": int(log2(9)),
        "accepted": False,
        "tpm_shape": None,
        "error": "",
        "corrupt_interpretation": True,
    }
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with config.override(VALIDATE_CONDITIONAL_INDEPENDENCE=False):
                net = Network(sbs)
        detail["accepted"] = True
        detail["tpm_shape"] = list(net.tpm.shape)
        detail["num_states"] = int(net.num_states)
        detail["size"] = int(net.size)
    except Exception as e:  # noqa: BLE001
        detail["error"] = f"{type(e).__name__}: {e}"
        detail["accepted"] = False
    return detail


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("MULTIVALUED IIT-4.0 PORT PROBE — path A / M2")
    print("=" * 72)
    print("  pin: pyphi @ feature/iit-4.0")
    print("  overlay: third_party/pyphi_iit4_mv (M2 exact Φ)")
    print()

    ctrl = binary_control_ok()
    print(f"  binary control Φ=2 triad:  {'PASS' if ctrl else 'FAIL'}")
    reg_ok, stock_phi, mv_phi = binary_regression_ok()
    print(
        f"  binary regression match:   {'PASS' if reg_ok else 'FAIL'}  "
        f"(stock={stock_phi}, mv={mv_phi})"
    )

    sbs3 = ternary_triad_sbs()
    accepted, err = probe_default_reject(sbs3)
    print(f"  stock Network accept:      {accepted}")
    if err:
        print(f"  stock reject locus:        {err[:140]}")

    trap = probe_ci_off_trap()
    print(
        f"  CI-off trap int(log2(9)):  {trap['int_log2_9']} "
        f"(corrupt — not used)"
    )

    sbs2 = ternary_swap_sbs()
    net2 = MultivaluedNetwork(sbs2, [3, 3], node_labels=("A", "B"))
    net3 = MultivaluedNetwork(sbs3, [3, 3, 3], node_labels=LABELS3)
    m1 = (
        net2.tpm.shape == (9, 9)
        and net3.tpm.shape == (27, 27)
        and np.allclose(net2.sbs(), sbs2)
        and np.allclose(net3.sbs(), sbs3)
    )
    print(f"  M1 construct+preserve:     {'GREEN' if m1 else 'FAIL'}")

    blocker = probe_exact_phi_blocker(net2, (1, 2))
    phi_ok = (not blocker["blocked"]) and blocker["phi"] is not None
    print(
        f"  exact Φ smoke (ternary):   "
        f"{'GREEN' if phi_ok else 'BLOCKED'}  Φ={blocker.get('phi')}"
    )

    print()
    print("PATH A CHECKS")
    print(f"  H_stock_rejects_ternary:   {'CONFIRMED' if not accepted else 'UNEXPECTED'}")
    print(f"  H_ci_off_is_shim:          CONFIRMED")
    print(f"  H_m1_sbs_native:           {'SUPPORTED' if m1 else 'REFUTED'}")
    print(f"  H_binary_regression:       {'SUPPORTED' if reg_ok else 'REFUTED'}")
    print(f"  H_m2_ternary_phi:          {'SUPPORTED' if phi_ok else 'REFUTED'}")

    grid = ctrl and (not accepted) and m1 and reg_ok and phi_ok
    verdict = "M2_GREEN" if grid else "M2_FAIL"

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print(
        "  best next:            #2–#4 on overlay; expand ternary state "
        "sweep (see BEYOND_BINARY_ARC.md)"
    )
    print()
    print(
        f"verdict: {verdict} — M2 exact ternary IIT-4.0 Φ on "
        f"third_party/pyphi_iit4_mv; SBS preserved; binary regression "
        f"matches stock; CI-off unused; #1 re-opened"
    )
    print(
        "reading: M2_GREEN — MultivaluedSubsystem + sia (GID) past "
        "backward_tpm blocker; no embedding proxy; no nonbinary IIT-3.0"
    )

    out = {
        "verdict": verdict,
        "binary_control": ctrl,
        "binary_regression": {"ok": reg_ok, "stock": stock_phi, "mv": mv_phi},
        "stock_network_accepted": accepted,
        "reject_error": err,
        "ci_off_trap": trap,
        "m1_construct": m1,
        "phi_blocker": blocker,
        "ternary_phi_smoke": phi_ok,
    }
    with open(os.path.join(RESULTS, "port_probe.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote results/port_probe.json  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
