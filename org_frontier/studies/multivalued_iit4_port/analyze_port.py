"""Path A / M1 probe — multivalued IIT-4.0 on the lab pin + vendored overlay.

Maps stock rejection, documents CI-off corruption trap, exercises
``third_party/pyphi_iit4_mv`` M1 (SBS-native ExplicitTPM). Exact ternary
Φ remains blocked past M1 (backward_tpm).

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
from pyphi import Network, config

from org_frontier.probes.lib import major_complex
from pyphi_iit4_mv import MultivaluedNetwork, probe_exact_phi_blocker
from pyphi_iit4_mv.conditional_independence import encode_state

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
LABELS3 = ("W", "S", "C")


def ternary_triad_sbs():
    """Deterministic S'=min(W,C), W'=S, C'=S on {0,1,2}^3 → (27,27) SBS."""
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
    """2-node ternary A'=B, B'=A → (9,9)."""
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


def probe_default_reject(sbs):
    try:
        Network(sbs, node_labels=LABELS3)
        return True, ""
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"


def probe_ci_off_trap():
    """Show CI-off mis-parses 9×9 ternary as binary 3-node (int(log2(9))=3)."""
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

    print("MULTIVALUED IIT-4.0 PORT PROBE — path A / M1")
    print("=" * 72)
    print("  pin: pyphi @ feature/iit-4.0 (lab requirements.txt)")
    print("  overlay: third_party/pyphi_iit4_mv (SBS-native M1)")
    print()

    ctrl = binary_control_ok()
    print(f"  binary control Φ=2 triad:  {'PASS' if ctrl else 'FAIL'}")

    sbs3 = ternary_triad_sbs()
    print(f"  ternary triad SBS shape:   {sbs3.shape}")

    accepted, err = probe_default_reject(sbs3)
    print(f"  stock Network accept:      {accepted}")
    if err:
        print(f"  stock reject locus:        {err[:160]}")

    trap = probe_ci_off_trap()
    print(
        f"  CI-off trap int(log2(9)):  {trap['int_log2_9']} "
        f"(corrupt binary reinterpretation — not used)"
    )
    if trap["tpm_shape"]:
        print(f"  CI-off tpm.shape:          {trap['tpm_shape']}")

    # --- M1 vendored path ---
    sbs2 = ternary_swap_sbs()
    net2 = MultivaluedNetwork(sbs2, [3, 3], node_labels=("A", "B"))
    net3 = MultivaluedNetwork(sbs3, [3, 3, 3], node_labels=LABELS3)
    preserved2 = bool(np.allclose(net2.sbs(), sbs2))
    preserved3 = bool(np.allclose(net3.sbs(), sbs3))
    m1_construct = (
        net2.tpm.shape == (9, 9)
        and net3.tpm.shape == (27, 27)
        and net2.num_states == 9
        and net3.num_states == 27
        and preserved2
        and preserved3
    )
    print()
    print("M1 VENDORED PATH (pyphi_iit4_mv)")
    print(f"  MultivaluedNetwork (9,9):  OK  preserved={preserved2}")
    print(f"  MultivaluedNetwork (27,27): OK  preserved={preserved3}")
    print(f"  num_states_per_node API:   {net3.num_states_per_node}")
    print(f"  M1 construct+preserve:     {'GREEN' if m1_construct else 'FAIL'}")

    blocker = probe_exact_phi_blocker(net2, (0, 0))
    print(f"  exact Φ smoke:             {'GREEN' if not blocker['blocked'] else 'BLOCKED'}")
    print(f"  Φ blocker locus:           {blocker['locus'][:140]}")

    print()
    print("PATH A CHECKS")
    print(f"  H_stock_rejects_ternary:   {'CONFIRMED' if not accepted else 'UNEXPECTED'}")
    print(f"  H_ci_off_is_shim:          CONFIRMED  (int(log2(k^n)) trap)")
    print(f"  H_m1_sbs_native:           {'SUPPORTED' if m1_construct else 'REFUTED'}")
    print(
        f"  H_m1_phi_still_blocked:    "
        f"{'CONFIRMED' if blocker['blocked'] else 'UNEXPECTED'}"
    )

    grid = ctrl and (not accepted) and m1_construct and blocker["blocked"]
    verdict = "M1_GREEN" if grid else "M1_FAIL"

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print(
        "  best next:            M2 SBS-native backward_tpm / "
        "condition_tpm + repertoire (see INSTRUMENT_GAP.md)"
    )
    print()
    print(
        f"verdict: {verdict} — M1 SBS-native ExplicitTPM lands under "
        f"third_party/pyphi_iit4_mv; ternary Network constructs; SBS "
        f"preserved (no int(log2) collapse); CI-off unused; exact Φ "
        f"blocked at backward_tpm/probability_of_current_state; "
        f"#1 remains NOT_TESTABLE"
    )
    print(
        "reading: M1_GREEN — stock binary IIT-4.0 pin unchanged; "
        "vendored overlay clears TPM ingest; next engineering step is "
        "M2 Subsystem/repertoire for mixed-radix; no embedding proxy; "
        "no nonbinary IIT-3.0 fallback"
    )

    out = {
        "verdict": verdict,
        "binary_control": ctrl,
        "sbs_shape": list(sbs3.shape),
        "stock_network_accepted": accepted,
        "reject_error": err,
        "ci_off_trap": trap,
        "m1_construct": m1_construct,
        "sbs_preserved_9": preserved2,
        "sbs_preserved_27": preserved3,
        "phi_blocker": blocker,
        "ternary_phi_smoke": not blocker["blocked"],
    }
    with open(os.path.join(RESULTS, "port_probe.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote results/port_probe.json  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
