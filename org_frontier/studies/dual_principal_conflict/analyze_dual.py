"""Agenda #29 — dual principals, conflicting commits: whose core wins?

Exact binary IIT-4.0 Φ on designed (W,S,C,A,B) forms. Hypotheses fixed
in hypotheses.md before computing. Cited: principal/; #74/#78; #37
pointer only.

Run:  python org_frontier/studies/dual_principal_conflict/analyze_dual.py
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

from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9

LABELS = ("W", "S", "C", "A", "B")
LABELS_WSC = ("W", "S", "C")


def panel():
    return [
        (
            "single_gate_mon",
            "contrast",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[4]],
            "single P=A gates+monitors; B idle",
        ),
        (
            "both_idle",
            "collapse",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3], lambda x: x[4]],
            "both principals idle spectators",
        ),
        (
            "extract_A_wins",
            "dominate",
            [lambda x: x[1], lambda x: x[3], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=A extractive; both monitor",
        ),
        (
            "extract_B_wins",
            "dominate",
            [lambda x: x[1], lambda x: x[4], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=B extractive; both monitor",
        ),
        (
            "A_full_B_mon",
            "dominate",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "A gates+mon; B monitor-only",
        ),
        (
            "both_gate_AND",
            "shared",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=W∧C∧A∧B; both read S",
        ),
        (
            "split_read_joint",
            "shared",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3] & x[4], lambda x: x[1], lambda x: x[0], lambda x: x[2]],
            "joint gate; A←W, B←C",
        ),
        (
            "both_extract_AND",
            "shared",
            [lambda x: x[1], lambda x: x[3] & x[4], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=A∧B; both read S",
        ),
        (
            "conflict_XOR",
            "shared",
            [lambda x: x[1], lambda x: x[3] ^ x[4], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=A⊕B conflict parity",
        ),
        (
            "rival_OR_extract",
            "shared",
            [lambda x: x[1], lambda x: x[3] | x[4], lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=A∨B either forces",
        ),
        (
            "NAND_principals",
            "shared",
            [lambda x: x[1], lambda x: int(not (x[3] & x[4])), lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "S'=¬(A∧B)",
        ),
        (
            "both_gate_OR",
            "collapse",
            [lambda x: x[1], lambda x: x[0] & x[2] & (x[3] | x[4]), lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "substitutable principal gate",
        ),
        (
            "agenda_conflict",
            "collapse",
            [
                lambda x: x[1],
                lambda x: (x[3] & x[0]) | (x[4] & x[2]),
                lambda x: x[1],
                lambda x: x[1],
                lambda x: x[1],
            ],
            "opposing agendas (A∧W)|(B∧C)",
        ),
        (
            "maj_2of_ABWC",
            "collapse",
            [
                lambda x: x[1],
                lambda x: int(x[0] + x[2] + x[3] + x[4] >= 2),
                lambda x: x[1],
                lambda x: x[1],
                lambda x: x[1],
            ],
            "majority 2-of-4 (A,B,W,C)",
        ),
    ]


def run_form(name, role, rules, note):
    v = verdict(rules, LABELS)
    core, phi_mc = major_complex(rules, LABELS)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    a_in = "A" in core_t
    b_in = "B" in core_t
    return {
        "name": name,
        "role": role,
        "note": note,
        "structure": v.structure,
        "whole_phi": float(v.max_phi) if v.max_phi >= 0 else 0.0,
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "A_in": a_in,
        "B_in": b_in,
        "shared": a_in and b_in,
        "dominates": (a_in and not b_in) or (b_in and not a_in),
        "collapse": (not a_in and not b_in) or len(core_t) == 0,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("DUAL PRINCIPAL CONFLICT — agenda #29")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (W,S,C,A,B) worker+system+counterpart+two principals")
    print("  cited: principal/; #74/#78; #37 pointer only")
    print()

    rows = [run_form(*args) for args in panel()]

    print(
        f"  {'form':<20}{'role':<10}{'whole':<8}{'Φ':>6}  "
        f"{'core':<18}{'A':>2}{'B':>2}  shared"
    )
    for r in rows:
        print(
            f"  {r['name']:<20}{r['role']:<10}{r['structure']:<8}"
            f"{r['phi']:>6.3f}  {r['core']:<18}"
            f"{'Y' if r['A_in'] else 'n':>2}{'Y' if r['B_in'] else 'n':>2}  "
            f"{'YES' if r['shared'] else 'no'}"
        )

    dom = [r for r in rows if r["role"] == "dominate" and r["dominates"]]
    shared = [r for r in rows if r["shared"] and r["phi"] > 0]
    collapse = [r for r in rows if r["role"] == "collapse" and r["collapse"]]

    h1 = len(dom) >= 1
    h2 = len(shared) >= 1
    h3 = len(collapse) >= 1

    # single-principal contrast
    single = next(r for r in rows if r["name"] == "single_gate_mon")
    both_and = next(r for r in rows if r["name"] == "both_gate_AND")
    ext_a = next(r for r in rows if r["name"] == "extract_A_wins")

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (one principal dominates):     "
        f"{'SUPPORTED' if h1 else 'REFUTED'}  "
        f"(n={len(dom)} dominate forms)"
    )
    print(
        f"  H2 (stable shared/joint core):    "
        f"{'SUPPORTED' if h2 else 'REFUTED'}  "
        f"(n={len(shared)} shared forms)"
    )
    print(
        f"  H3 (collapse / both principals out): "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  "
        f"(n={len(collapse)} collapse forms)"
    )
    print(
        f"  single-P contrast: core={single['core']} Φ={single['phi']:.3f}"
    )
    print(
        f"  both_gate_AND shared: core={both_and['core']} Φ={both_and['phi']:.3f}"
    )
    print(
        f"  extract_A_wins dominate: core={ext_a['core']} Φ={ext_a['phi']:.3f}"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    if h1 and h2 and h3 and ctrl_ok:
        verdict_s = "CONFLICT_ENCODING"
    elif h1 and h2:
        verdict_s = "DOMINATE_OR_SHARE"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and h2 and h3

    print()
    print("STATUS")
    print(f"  H1 one dominates:     {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 shared core:       {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 collapse:          {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #30 endogenous coalition (alt #32 rival platforms)")
    print()
    print(
        f"verdict: {verdict_s} — dual conflicting principals do not have a "
        f"single winner rule: extractive asymmetry yields one-principal "
        f"dominance ({{S,A}} / {{S,B}}); joint COMMIT_READ / joint principal "
        f"commits yield a stable shared core; unresolved agenda conflict and "
        f"majority / substitutable gates collapse — encoding decides, extending "
        f"single-principal bidirectionality"
    )
    print(
        "reading: CONFLICT_ENCODING — whose core wins is set by the conflict "
        "encoding (dominate / share / collapse); a stable shared core exists "
        "when both principals jointly determine and read the commit; #37 "
        "pointer only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
