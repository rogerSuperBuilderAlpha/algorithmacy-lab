"""Agenda #47 — verify closed-form scaling laws (exact Φ smoke).

Claims fixed in hypotheses.md; analytic status in PROOFS.md.
Small-n exact IIT-4.0 Φ checks verify; they are not the proof.

Run:  python org_frontier/studies/scaling_laws_closed_form/verify_laws.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import pyphi
from pyphi import new_big_phi

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_topology_map import pool

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9

# Smoke grid: exact Φ, candid N (n≤5; hub also n=6 for the linear law).
GRID = (
    ("conjunctive_hub", single_hub, lambda n: n - 1, (3, 4, 5, 6)),
    ("pool", pool, lambda n: n * (n - 1), (3, 4, 5)),
    ("parity_hub", parity_hub, lambda n: 2 ** (2 - n), (3, 4, 5)),
)


def _faithful_triad_rules():
    # W'=S, S'=W∧C, C'=S — canonical Φ=2 control.
    return [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]]


def _sia_gid_at_all_ones(build, n):
    rules = build(n)
    labels = tuple(f"n{i}" for i in range(n))
    net = pyphi.Network(
        tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels
    )
    state = tuple(1 for _ in range(n))
    sub = pyphi.Subsystem(net, state)
    sia = new_big_phi.sia(sub)
    c, e = sia.cause, sia.effect
    return {
        "sia_phi": float(sia.phi),
        "phi_c": float(c.phi),
        "phi_e": float(e.phi),
        "sel_c": float(c.selectivity),
        "sel_e": float(e.selectivity),
        "fwd_c": float(c.repertoire),
        "fwd_e": float(e.repertoire),
        "ppart_c": float(c.partitioned_repertoire),
        "ppart_e": float(e.partitioned_repertoire),
        "mip": str(sia.partition).split("\n")[0],
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(_faithful_triad_rules(), labels=("W", "S", "C"))
    ctrl_phi = float(ctrl.max_phi)
    ctrl_struct = str(ctrl.structure).lower()
    ctrl_ok = "triadic" in ctrl_struct and abs(ctrl_phi - 2.0) < PHI_TOL
    print("SCALING LAWS CLOSED-FORM — agenda #47 verification")
    print("=" * 64)
    print(
        f"  faithful triad: triadic Φ={ctrl_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print(
        "  instrument: major-complex sia.phi; "
        "GENERALIZED_INTRINSIC_DIFFERENCE; SET_UNI/BI"
    )
    print()

    rows = []
    all_hold = True
    print(
        f"  {'form':<18}{'n':>3}  {'Φ':>8}  {'law':>8}  "
        f"{'sel_c':>6}  {'p_part':>10}  {'hold':>5}"
    )
    for name, build, law_fn, ns in GRID:
        for n in ns:
            core, phi = major_complex(build(n), tuple(f"n{i}" for i in range(n)))
            pred = float(law_fn(n))
            gid = _sia_gid_at_all_ones(build, n)
            hold = (
                abs(phi - pred) < PHI_TOL
                and abs(gid["sia_phi"] - pred) < PHI_TOL
                and core is not None
                and len(core) == n
            )
            all_hold = all_hold and hold
            print(
                f"  {name:<18}{n:>3}  {phi:>8.6f}  {pred:>8.6f}  "
                f"{gid['sel_c']:>6.4f}  {gid['ppart_c']:>10.6g}  "
                f"{'YES' if hold else 'NO':>5}"
            )
            rows.append(
                {
                    "form": name,
                    "n": n,
                    "phi_major": f"{phi:.10f}",
                    "law": f"{pred:.10f}",
                    "sia_phi_all1": f"{gid['sia_phi']:.10f}",
                    "phi_c": f"{gid['phi_c']:.10f}",
                    "phi_e": f"{gid['phi_e']:.10f}",
                    "sel_c": f"{gid['sel_c']:.10f}",
                    "sel_e": f"{gid['sel_e']:.10f}",
                    "fwd_c": f"{gid['fwd_c']:.10f}",
                    "ppart_c": f"{gid['ppart_c']:.10g}",
                    "mip": gid["mip"],
                    "core_size": len(core) if core else 0,
                    "hold": hold,
                }
            )

    out = os.path.join(RESULTS, "verification.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print()
    print("STATUS (analytic; see PROOFS.md)")
    print("  C1 conjunctive Φ=n-1:     PARTIAL (cut proved; MIP id partial)")
    print("  C2 pool Φ=n(n-1):         PARTIAL (cut proved; MIP id partial)")
    print("  C3 parity Φ=2^(2-n):      PARTIAL (cut+sel proved; MIP id partial)")
    print(
        f"  verification grid:        "
        f"{'PASS' if all_hold and ctrl_ok else 'FAIL'}  ({len(rows)} cells)"
    )
    print("  best next:                #49 min-cut MIP (closes MIP gaps)")
    print()
    print(
        "verdict: PARTIAL_PROOFS — GID cut formulas proved for all three laws; "
        "MIP identity verified n≤5 (hub n≤6), conjectured for general n"
    )
    print(
        "reading: PARTIAL_PROOFS — conjunctive/pool/parity closed forms follow "
        "from selectivity × PMI on the hub-preserving or complete atomic cut; "
        "remaining gap is SET_UNI/BI MIP uniqueness (#49)"
    )
    print(f"wrote {out}  ({time.time() - t0:.1f}s)")
    print("=" * 64)


if __name__ == "__main__":
    main()
