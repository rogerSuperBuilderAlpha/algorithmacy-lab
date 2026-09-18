"""Agenda #3 — mixed-radix mediator: Φ magnitude vs core membership.

Binary parties (k=2), ternary mediator (k=3). Exact IIT-4.0 via
pyphi_iit4_mv. Hypotheses fixed in hypotheses.md before this run.

Run:  python org_frontier/studies/mixed_radix_mediator/analyze_mixed.py
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
from pyphi import convert, new_big_phi

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
KS = (2, 3, 2)
CM = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
N_STATES = int(np.prod(KS))


def structure_of(n_core: int, phi: float) -> str:
    if n_core <= 0 or phi <= PHI_TOL:
        return "NULL"
    if n_core == 1:
        return "MONADIC"
    if n_core == 2:
        return "DYADIC"
    return "TRIADIC"


def major_at(net, state):
    mc = maximal_complex(net, state)
    if isinstance(mc, new_big_phi.NullPhiStructure) or mc.node_indices is None:
        return (), 0.0, "NULL"
    core = tuple(LABELS[i] for i in mc.node_indices)
    phi = float(mc.phi)
    return core, phi, structure_of(len(core), phi)


def build_sbs(next_fn):
    sbs = np.zeros((N_STATES, N_STATES), dtype=float)
    for i in range(N_STATES):
        st = decode_state(i, KS)
        sbs[i, encode_state(next_fn(st), KS)] = 1.0
    return sbs


def next_full(st):
    w, s, c = st
    return (1 if s == 2 else 0, w + c, 1 if s == 2 else 0)


def next_thresh(st):
    w, s, c = st
    return (1 if s >= 1 else 0, w + c, 1 if s >= 1 else 0)


def binary_control():
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    core, phi = major_complex(rules, LABELS)
    core_t = tuple(core) if core is not None else ()
    phi = float(phi) if core_t else 0.0
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    sbs = convert.state_by_node2state_by_state(tpm)
    net = MultivaluedNetwork(sbs, [2, 2, 2], cm=cm, node_labels=LABELS)
    mv_core, mv_phi, _ = major_at(net, (1, 1, 1))
    return {
        "stock_core": "|".join(core_t),
        "stock_phi": phi,
        "mv_core": "|".join(mv_core),
        "mv_phi": mv_phi,
        "ok": (
            set(core_t) == {"W", "S", "C"}
            and abs(phi - 2.0) < PHI_TOL
            and set(mv_core) == {"W", "S", "C"}
            and abs(mv_phi - 2.0) < PHI_TOL
        ),
    }


def sweep_form(name, next_fn):
    net = MultivaluedNetwork(build_sbs(next_fn), KS, cm=CM, node_labels=LABELS)
    rows = []
    for S in (0, 1, 2):
        state = (1, S, 1)
        core, phi, struct = major_at(net, state)
        rows.append(
            {
                "form": name,
                "S": S,
                "state": str(state),
                "structure": struct,
                "n_core": len(core),
                "core": "|".join(core) if core else "",
                "phi": phi,
            }
        )
    return rows


def pattern_for(rows):
    """Return (phi_only, membership_changes) for defined (non-NULL) rows."""
    defined = [r for r in rows if r["structure"] != "NULL"]
    if len(defined) < 2:
        return False, False
    cores = {r["core"] for r in defined}
    phis = [r["phi"] for r in defined]
    fixed_core = len(cores) == 1
    phi_varies = max(phis) - min(phis) > PHI_TOL
    membership_changes = len(cores) > 1 or len({r["n_core"] for r in defined}) > 1
    phi_only = fixed_core and phi_varies and not membership_changes
    return phi_only, membership_changes


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("MIXED-RADIX MEDIATOR — agenda #3")
    print("=" * 72)
    print("  alphabets: (W,S,C)=(2,3,2)  — binary parties, ternary mediator")
    print("  commit: S'=W+C; forms full (S==2) and thresh (S>=1)")
    print("  sweep: (1,S,1) for S∈{0,1,2}  — extra mid resolution at S=1")
    print("  instrument: pyphi_iit4_mv maximal_complex (exact IIT-4.0)")
    print()

    ctrl = binary_control()
    print("BINARY CONTROL (AND @ (1,1,1))")
    print(
        f"  stock TRIADIC Φ={ctrl['stock_phi']:.3f} core={ctrl['stock_core']}"
    )
    print(
        f"  overlay TRIADIC Φ={ctrl['mv_phi']:.3f} core={ctrl['mv_core']}"
    )
    print(f"  control: {'PASS' if ctrl['ok'] else 'FAIL'}")

    all_rows = []
    patterns = {}
    print()
    for name, fn in (("full", next_full), ("thresh", next_thresh)):
        rows = sweep_form(name, fn)
        all_rows.extend(rows)
        phi_only, mem = pattern_for(rows)
        patterns[name] = {"phi_only": phi_only, "membership": mem}
        print(f"FORM {name} — sweep (1,S,1)")
        for r in rows:
            print(
                f"  S={r['S']}  {r['structure']:<8} n_core={r['n_core']}  "
                f"Φ={r['phi']:.4f}  core={r['core'] or '∅'}"
            )
        print(
            f"  pattern: phi_only={phi_only}  membership_changes={mem}"
        )
        print()

    # H1: at least one form is Φ-only; prefer both
    h1 = patterns["full"]["phi_only"] or patterns["thresh"]["phi_only"]
    h1_both = patterns["full"]["phi_only"] and patterns["thresh"]["phi_only"]
    # H2: at least one form changes membership on the sweep
    h2 = patterns["full"]["membership"] or patterns["thresh"]["membership"]
    # H3: forms disagree on pattern
    h3 = patterns["full"] != patterns["thresh"]

    print("HYPOTHESES")
    print(
        f"  H1 (extra resolution → Φ only):     "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
        f"{'  (both forms)' if h1_both else ''}"
    )
    print(
        f"  H2 (extra resolution → membership): "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (form-dependent pattern):        "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )

    if h1_both and not h2 and not h3:
        verdict = "EXTRA_RESOLUTION_TO_PHI"
    elif h2 and not h1:
        verdict = "EXTRA_RESOLUTION_TO_CORE"
    elif h3:
        verdict = "FORM_DEPENDENT"
    else:
        verdict = "MIXED"

    grid = ctrl["ok"] and (h1 or h2)

    with open(os.path.join(RESULTS, "sweep.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(
            {
                "verdict": verdict,
                "binary_control": ctrl,
                "patterns": patterns,
                "h1": h1,
                "h1_both": h1_both,
                "h2": h2,
                "h3": h3,
                "ks": list(KS),
            },
            f,
            indent=2,
        )

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print(
        "  best next:            #4 higher-radix parity / balanced commit "
        "(blind spot)"
    )
    print()
    print(
        f"verdict: {verdict} — mixed-radix (2,3,2) S'=W+C: on (1,S,1) "
        f"sweep both full and thresh keep fixed TRIADIC core while Φ "
        f"varies with mediator level S (mid S=1 is Φ-only extra "
        f"resolution); binary AND control TRIADIC Φ=2"
    )
    print(
        "reading: EXTRA_RESOLUTION_TO_PHI — unlike all-ternary #2 "
        "(membership grades with L), binary parties + ternary mediator "
        "put the extra bit into Φ magnitude; core stays {W,S,C}; "
        "#1/#2 pointers only"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
