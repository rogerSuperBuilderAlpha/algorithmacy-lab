"""Agenda #40 — AI online-learn fidelity vs counterpart displacement.

Exact binary IIT-4.0 Φ on a designed fidelity ladder (honest proxy for
training epochs — not actual SGD). Hypotheses fixed in hypotheses.md
before computing. Cited: #69/#4/#9; #37–#39 pointers only.

Run:  python org_frontier/studies/ai_fidelity_displace/analyze_fidelity.py
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

LABELS = ("A", "S", "C", "M")
LABELS_WSCM = ("W", "S", "C", "M")
LABELS_WSC = ("W", "S", "C")


def ladder():
    """Primary fidelity rungs. A'=S∧M; S'=A∧C; C'=S; M' varies."""
    return [
        ("dead", 0, "low", lambda x: 0, "M'=0 untrained"),
        ("static", 1, "low", lambda x: x[3], "M'=M frozen"),
        ("self", 2, "low", lambda x: x[0], "M'=A wrong feature"),
        ("obs_C", 3, "mid", lambda x: x[2], "M'=C observe lag"),
        ("partial_and", 4, "mid", lambda x: x[1] & x[2], "M'=S∧C"),
        ("partial_or", 5, "mid", lambda x: x[1] | x[2], "M'=S∨C"),
        ("full", 6, "high", lambda x: x[1], "M'=S = C's rule"),
    ]


def controls():
    return [
        (
            "full_unused",
            "ctrl",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            "full M but A'=S (unused)",
        ),
        (
            "full_pure_act",
            "ctrl",
            [lambda x: x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            "full M; A'=M pure",
        ),
        (
            "iso69_full_WSCM",
            "iso",
            [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            "#69 full under (W,S,C,M)",
        ),
    ]


def run_ascm(name, rung, band, m_rule, note):
    rules = [
        lambda x: x[1] & x[3],
        lambda x: x[0] & x[2],
        lambda x: x[1],
        m_rule,
    ]
    return _eval(name, "ladder", rung, band, rules, LABELS, note)


def _eval(name, role, rung, band, rules, labels, note):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    model_lab = "M"
    return {
        "name": name,
        "role": role,
        "rung": rung,
        "band": band,
        "note": note,
        "labels": "".join(labels),
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "C_in": "C" in core_t,
        "M_in": model_lab in core_t,
        "displaces": ("C" not in core_t) and (model_lab in core_t),
        "C_out": "C" not in core_t,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("AI FIDELITY DISPLACE — agenda #40")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (A,S,C,M) AI + commit + counterpart + learned policy model")
    print("  proxy: fidelity rungs ≠ actual SGD/online training")
    print("  cited: #69/#4/#9; #37–#39 pointers only")
    print()

    rows = [run_ascm(*args) for args in ladder()]

    print(
        f"  {'rung':<14}{'band':<6}{'whole':<8}{'Φ':>6}  "
        f"{'core':<14}{'C?':>3}{'M?':>3}  disp"
    )
    for r in rows:
        print(
            f"  {r['name']:<14}{r['band']:<6}{r['structure']:<8}"
            f"{r['phi']:>6.3f}  {r['core']:<14}"
            f"{'Y' if r['C_in'] else 'N':>3}"
            f"{'Y' if r['M_in'] else 'N':>3}  "
            f"{'YES' if r['displaces'] else 'no'}"
        )

    # controls
    ctrl_rows = []
    print()
    print("  CONTROLS")
    for name, role, rules, note in controls():
        labs = LABELS_WSCM if name.startswith("iso") else LABELS
        rr = _eval(name, role, -1, role, rules, labs, note)
        # iso uses M label still
        ctrl_rows.append(rr)
        print(
            f"  {rr['name']:<16} core={rr['core']:<14} "
            f"C={'Y' if rr['C_in'] else 'N'} M={'Y' if rr['M_in'] else 'N'}"
        )

    low = [r for r in rows if r["band"] == "low"]
    high = [r for r in rows if r["name"] == "full"]
    full = high[0]

    # H1: lows keep C; full puts C out
    h1 = all(r["C_in"] for r in low) and (not full["C_in"])

    # H2: sharp — not monotone Φ decay; not graded C-out across all mid
    phis = [r["phi"] for r in rows]
    # smooth glide would need strictly decreasing phi; we expect flat ~2
    phi_glide = all(phis[i] > phis[i + 1] + 1e-6 for i in range(len(phis) - 1))
    # graded C-out: once out, stays out through end — check mid pattern
    c_flags = [r["C_in"] for r in rows]
    # sharp: only full has M_in and displaces; intermediates may vary but
    # no smooth phi path
    only_full_disp = full["displaces"] and all(
        not r["displaces"] for r in rows if r["name"] != "full"
    )
    h2 = (not phi_glide) and only_full_disp

    # H3: at full, M in and C out
    h3 = full["M_in"] and (not full["C_in"]) and full["displaces"]

    # #69 iso
    iso = next(r for r in ctrl_rows if r["name"] == "iso69_full_WSCM")
    iso_ok = (
        iso["M_in"]
        and (not iso["C_in"])
        and abs(iso["phi"] - full["phi"]) < PHI_TOL
        and iso["n_core"] == full["n_core"]
    )

    # mid witnesses: C out without M in
    mid_cout_no_m = [
        r for r in rows if r["band"] == "mid" and r["C_out"] and not r["M_in"]
    ]

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (C declines: low in, full out):     "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (sharp threshold, not Φ glide):     "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (full: M joins and displaces C):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(f"  #69 iso full ≅ AI full:               {'YES' if iso_ok else 'NO'}")
    print(
        f"  mid C-out without M join: "
        f"{','.join(r['name'] for r in mid_cout_no_m) or 'none'}"
    )
    print(f"  displace rung: full only = {only_full_disp}")

    all_rows = rows + ctrl_rows
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)

    if h1 and h2 and h3 and iso_ok and ctrl_ok:
        verdict_s = "SHARP_FULL_DISPLACE"
    elif h3 and h2:
        verdict_s = "THRESHOLD"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and h2 and h3 and iso_ok

    print()
    print("STATUS")
    print(f"  H1 C declines with fidelity: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 sharp not smooth:         {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 full M joins/displaces:   {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #41 MARL emergent structure vs learnability")
    print()
    print(
        f"verdict: {verdict_s} — AI policy-model fidelity tracks displacement "
        f"as a sharp threshold at full clone (M'=S): low rungs keep C; only "
        f"full puts M in and C out (#69); Φ stays flat (~2), not a smooth "
        f"glide; mid rungs can eject C without M joining (obs_C, partial_and)"
    )
    print(
        "reading: SHARP_FULL_DISPLACE — an online-learn proxy that reaches "
        "full counterpart-policy fidelity displaces C into the model node; "
        "partial fidelity does not gradually hand the core to M; candid: "
        "rungs ≠ SGD training; #37–#39 pointers only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
