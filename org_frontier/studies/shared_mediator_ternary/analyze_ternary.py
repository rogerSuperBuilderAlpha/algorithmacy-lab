"""Beyond-binary probe of shared-mediator AND (agenda structural queue).

Binary IIT-4.0 control + ternary min-AND lift. Multivalued exact IIT-4.0 is
probed for capability; if absent, H3–H5 are reported NOT_TESTABLE.

Run:  python org_frontier/studies/shared_mediator_ternary/analyze_ternary.py
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

import numpy as np

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

LABELS = ("W1", "C1", "W2", "C2", "S")
EXCLUSIVE = (("W1", "C1"), ("W2", "C2"))


# ---------------------------------------------------------------------------
# Lifts (documented in hypotheses.md)
# ---------------------------------------------------------------------------

def binary_shared_mediator_and():
    """Binary shared-mediator AND — same construction as two_triad_shared_member."""
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: (x[0] & x[1]) & (x[2] & x[3]),
    ]
    return LABELS, rules


def min_and(a, b):
    return a if a <= b else b


def ternary_next_state(state):
    """Primary lift: min-AND shared mediator on {0,1,2}^5."""
    w1, c1, w2, c2, s = state
    own1 = min_and(w1, c1)
    own2 = min_and(w2, c2)
    sp = min_and(own1, own2)
    return (s, s, s, s, sp)


def ternary_agrees_with_binary_on_01():
    """Unit check: min on {0,1} equals ∧; dynamics match binary on the {0,1}^5 cube."""
    from itertools import product

    labels, bin_rules = binary_shared_mediator_and()
    # evaluate binary next via truth table enumeration
    ok = True
    for st in product((0, 1), repeat=5):
        bn = tuple(int(r(st)) for r in bin_rules)
        tn = ternary_next_state(st)
        if bn != tn:
            ok = False
            break
    return ok


def build_ternary_sbs_tpm(n_nodes=5, base=3):
    """Deterministic state-by-state TPM for ternary min-AND architecture."""
    n_states = base ** n_nodes

    def idx_to_state(idx):
        out = []
        for _ in range(n_nodes):
            out.append(idx % base)
            idx //= base
        return tuple(out)

    def state_to_idx(state):
        idx = 0
        mul = 1
        for s in state:
            idx += int(s) * mul
            mul *= base
        return idx

    sbs = np.zeros((n_states, n_states), dtype=float)
    for i in range(n_states):
        j = state_to_idx(ternary_next_state(idx_to_state(i)))
        sbs[i, j] = 1.0
    return sbs


def spans_both(core):
    c = set(core)
    left, right = EXCLUSIVE
    return bool(c & set(left)) and bool(c & set(right))


def probe_iit4_multivalued_capability():
    """Return (ok, detail). ok True only if Network accepts ternary + new_big_phi usable."""
    import pyphi
    from pyphi import Network

    detail = {
        "has_new_big_phi": hasattr(pyphi, "new_big_phi"),
        "network_accepts_num_states_per_node": False,
        "ternary_network_built": False,
        "error": "",
    }
    sbs = build_ternary_sbs_tpm()
    cm = np.array(
        [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
        ],
        dtype=int,
    )
    try:
        import inspect

        sig = inspect.signature(Network.__init__)
        detail["network_accepts_num_states_per_node"] = (
            "num_states_per_node" in sig.parameters
        )
    except Exception as e:
        detail["error"] = f"signature: {e}"

    if detail["network_accepts_num_states_per_node"]:
        try:
            net = Network(
                sbs,
                cm=cm,
                node_labels=LABELS,
                num_states_per_node=[3] * 5,
            )
            detail["ternary_network_built"] = True
            # require new_big_phi path
            if not detail["has_new_big_phi"]:
                return False, detail
            return True, detail
        except Exception as e:
            detail["error"] = f"{type(e).__name__}: {e}"
            return False, detail

    # Also try feeding SBS blindly (will fail on binary pin — expected)
    try:
        Network(sbs, cm=cm, node_labels=LABELS)
        detail["ternary_network_built"] = True
        detail["error"] = "unexpected: binary Network accepted 3^5 SBS"
        return False, detail
    except Exception as e:
        detail["error"] = f"{type(e).__name__}: {e}"
        return False, detail


def main():
    print("SHARED-MEDIATOR TERNARY — beyond-binary merge survival")
    print("=" * 80)
    print("  primary lift: min-AND on {0,1,2} (extends binary ∧)")
    print("  instrument:   exact IIT-4.0 (pyphi.new_big_phi); cited two_triad_shared_member")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("LIFT UNIT CHECK")
    print("-" * 80)
    agree = ternary_agrees_with_binary_on_01()
    print(f"  min-AND agrees with binary AND on {{0,1}}^5: "
          f"{'PASS' if agree else 'FAIL'}")
    if not agree:
        raise SystemExit("ABORT: ternary lift does not extend binary AND")
    sbs = build_ternary_sbs_tpm()
    print(f"  ternary SBS TPM shape: {sbs.shape}  (expect (243, 243))")
    print(f"  row-stochastic: {bool(np.allclose(sbs.sum(axis=1), 1.0))}")
    print()

    print("H1 BINARY CONTROL (IIT-4.0)")
    print("-" * 80)
    labels, rules = binary_shared_mediator_and()
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    span = spans_both(core_t)
    dt = time.time() - t0
    print(f"  whole: {v.structure} Φ_MIP={v.max_phi:.4f}")
    print(f"  core:  {core_t}  coreΦ={core_phi:.3f}  spans_both={span}  ({dt:.1f}s)")
    h1 = (
        span
        and abs(core_phi - 4.0) < 1e-3
        and set(core_t) == set(LABELS)
    )
    print(f"  H1 (binary merge Φ=4.0, full core): {'SUPPORTED' if h1 else 'REFUTED'}")
    if not h1:
        raise SystemExit("ABORT: binary control failed; do not interpret ternary")
    print()

    print("H2 IIT-4.0 MULTIVALUED CAPABILITY")
    print("-" * 80)
    h2, detail = probe_iit4_multivalued_capability()
    print(f"  has new_big_phi:                    {detail['has_new_big_phi']}")
    print(f"  Network(num_states_per_node=...):   "
          f"{detail['network_accepts_num_states_per_node']}")
    print(f"  ternary network built:              {detail['ternary_network_built']}")
    print(f"  error: {detail['error']}")
    print(f"  H2 (IIT-4.0 accepts ternary TPM):   {'SUPPORTED' if h2 else 'REFUTED'}")
    print()

    h3 = h4 = h5 = None
    ternary_row = {
        "structure": "",
        "whole_phi_mip": "",
        "core": "",
        "core_phi": "",
        "spans_both": "",
        "status": "NOT_TESTABLE",
    }

    print("H3–H5 TERNARY MIN-AND (exact IIT-4.0)")
    print("-" * 80)
    if not h2:
        print("  SKIPPED — multivalued IIT-4.0 capability absent on this pin")
        print("  (WAVE10 #5 / nonbinary API not on feature/iit-4.0; new_big_phi is binary)")
        print("  H3 (ternary spans both):           NOT_TESTABLE")
        print("  H4 (ternary core not local-only):  NOT_TESTABLE")
        print("  H5 (membership/Φ differs):         NOT_TESTABLE")
        reading = (
            "TOOLING_GAP — binary merge stands; ternary IIT-4.0 not computable here"
        )
    else:
        # Placeholder path if capability appears in a future pin.
        print("  capability present — ternary exact path not yet implemented in this study")
        print("  H3–H5: NOT_TESTABLE (implementation deferred)")
        reading = "PARTIAL — capability present but ternary path not implemented"

    print()
    print("OPTIONAL LEAF CONTROLS (ternary)")
    print("-" * 80)
    print("  shared-worker / shared-counterpart ternary: SKIPPED (same tooling gate)")
    print()

    print("=" * 80)
    print("SUMMARY")
    print(f"  binary shared-S/AND: spans={span} coreΦ={core_phi:.3f} core={core_t}")
    print(f"  ternary lift:        min-AND (unit check PASS)")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3=NOT_TESTABLE  H4=NOT_TESTABLE  H5=NOT_TESTABLE")
    print(f"  reading: {reading}")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "NOT_TESTABLE",
            "h4": "NOT_TESTABLE",
            "h5": "NOT_TESTABLE",
            "binary_spans": str(span),
            "binary_core_phi": f"{float(core_phi):.6f}",
            "binary_core": "|".join(core_t),
            "lift_unit_check": "PASS" if agree else "FAIL",
            "reading": reading,
            "capability_error": detail.get("error", ""),
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
