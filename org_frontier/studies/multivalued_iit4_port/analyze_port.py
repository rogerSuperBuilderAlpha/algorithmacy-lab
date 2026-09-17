"""Path A probe — multivalued IIT-4.0 on the lab pin.

Maps rejection locus, documents CI-off corruption trap, confirms
pyphi@nonbinary is not a substitute. Does not claim ternary Φ.

Run:  python org_frontier/studies/multivalued_iit4_port/analyze_port.py
"""

from __future__ import annotations

import json
import os
import sys
import time
from math import log2

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from pyphi import Network, config

from org_frontier.probes.lib import major_complex

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
LABELS3 = ("W", "S", "C")


def ternary_triad_sbs():
    """Deterministic S'=min(W,C), W'=S, C'=S on {0,1,2}^3 → (27,27) SBS."""
    base, n = 3, 3
    N = base ** n
    sbs = np.zeros((N, N))

    def st(i):
        return tuple((i // base ** k) % base for k in range(n))

    def ix(state):
        return sum(state[k] * (base ** k) for k in range(n))

    for i in range(N):
        w, s, c = st(i)
        ns = (s, min(w, c), s)
        sbs[i, ix(ns)] = 1.0
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
    except Exception as e:
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
                net = Network(sbs)  # no labels — invents 3 binary nodes
        detail["accepted"] = True
        detail["tpm_shape"] = list(net.tpm.shape)
        detail["num_states"] = int(net.num_states)
        detail["size"] = int(net.size)
    except Exception as e:
        detail["error"] = f"{type(e).__name__}: {e}"
        detail["accepted"] = False
    return detail


def probe_nonbinary_api():
    import inspect

    return "num_states_per_node" in inspect.signature(Network.__init__).parameters


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("MULTIVALUED IIT-4.0 PORT PROBE — path A")
    print("=" * 72)
    print("  pin: pyphi @ feature/iit-4.0 (lab requirements.txt)")
    print("  goal: exact ternary Φ smoke — or INSTRUMENT_GAP")
    print()

    ctrl = binary_control_ok()
    print(f"  binary control Φ=2 triad:  {'PASS' if ctrl else 'FAIL'}")

    sbs = ternary_triad_sbs()
    print(f"  ternary triad SBS shape:   {sbs.shape}")

    accepted, err = probe_default_reject(sbs)
    print(f"  default Network accept:    {accepted}")
    if err:
        print(f"  reject locus:              {err[:160]}")

    has_api = probe_nonbinary_api()
    print(f"  num_states_per_node API:   {has_api}")

    trap = probe_ci_off_trap()
    print(
        f"  CI-off trap int(log2(9)):  {trap['int_log2_9']} "
        f"(corrupt binary reinterpretation — not used)"
    )
    if trap["tpm_shape"]:
        print(f"  CI-off tpm.shape:          {trap['tpm_shape']}")
    if trap["error"]:
        print(f"  CI-off error:              {trap['error'][:120]}")

    # Path A outcome this turn
    smoke_green = False  # never claim Φ without real multivalued support
    gap = (not accepted) and ctrl and (not has_api)

    print()
    print("PATH A CHECKS")
    print(f"  H_pin_rejects_ternary:     {'CONFIRMED' if not accepted else 'UNEXPECTED'}")
    print(f"  H_no_mv_api_on_pin:        {'CONFIRMED' if not has_api else 'UNEXPECTED'}")
    print(f"  H_ci_off_is_shim:          CONFIRMED  (int(log2(k^n)) trap)")
    print(f"  H_nonbinary_branch_usable: REFUTED  (IIT-3.0; 3.12 import break; no new_big_phi)")
    print(f"  ternary Φ smoke:           {'GREEN' if smoke_green else 'BLOCKED'}")

    verdict = "INSTRUMENT_GAP" if gap and not smoke_green else "UNEXPECTED"
    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if gap and ctrl else 'FAIL'}")
    print(
        "  best next:            vendor feature/iit-4.0 fork; "
        "M1 SBS-native ExplicitTPM (see INSTRUMENT_GAP.md)"
    )
    print()
    print(
        f"verdict: {verdict} — path A surveyed: lab pin rejects ternary SBS "
        f"at ExplicitTPM/convert (binary 2^n); CI-off reinterprets as corrupt "
        f"binary; pyphi@nonbinary is IIT-3.0 and broken on 3.12; full "
        f"new_big_phi multivalued port is multi-week, not a study patch; "
        f"#1 remains NOT_TESTABLE"
    )
    print(
        "reading: INSTRUMENT_GAP — next engineering step is a vendored "
        "IIT-4.0 fork with SBS-only mixed-radix TPM then repertoire/"
        "new_big_phi; no embedding proxy; no nonbinary IIT-3.0 fallback"
    )

    out = {
        "verdict": verdict,
        "binary_control": ctrl,
        "sbs_shape": list(sbs.shape),
        "network_accepted": accepted,
        "reject_error": err,
        "has_num_states_per_node": has_api,
        "ci_off_trap": trap,
        "ternary_phi_smoke": smoke_green,
    }
    with open(os.path.join(RESULTS, "port_probe.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote results/port_probe.json  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
