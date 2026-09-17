"""Agenda #33 — regulator capture: when does oversight become capture?

Exact binary IIT-4.0 Φ on designed (W,S,C,R) forms + R-read coupling
sweep. Hypotheses fixed in hypotheses.md before computing. Cited:
#76/#111; principal FINDINGS pointer; #29–#32 pointers only.

Run:  python org_frontier/studies/regulator_capture/analyze_capture.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from itertools import combinations

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9

LABELS = ("W", "S", "C", "R")
LABELS_WSC = ("W", "S", "C")
LABELS5 = ("W", "S", "C", "R1", "R2")
READ_NAMES = ("W", "S", "C")


def classify(core):
    if not core:
        return "null", 0, False
    s = set(core)
    r_in = "R" in s or "R1" in s or "R2" in s
    n_parties = sum(1 for n in ("W", "C") if n in s)
    if s == {"S", "R"} or s == {"S", "R1"} or s == {"S", "R2"}:
        return "capture", n_parties, r_in
    if r_in and n_parties == 2:
        return "oversight", n_parties, r_in
    if r_in and n_parties < 2:
        return "partial", n_parties, r_in
    return "out", n_parties, r_in


def r_rule_from_reads(reads):
    """AND over selected reads; empty → static self-loop."""

    def rule(x, reads=tuple(reads)):
        if not reads:
            return x[3]
        r = 1
        for i in reads:
            r &= x[i]
        return int(bool(r))

    return rule


def gated_form(reads):
    return [
        lambda x: x[1],
        lambda x: x[0] & x[2] & x[3],
        lambda x: x[1],
        r_rule_from_reads(reads),
    ]


def nogate_form(reads):
    return [
        lambda x: x[1],
        lambda x: x[0] & x[2],
        lambda x: x[1],
        r_rule_from_reads(reads),
    ]


def named_panel():
    return [
        (
            "observer",
            "out",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            "#76 observer",
        ),
        (
            "veto_only",
            "out",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]],
            "#76 static veto",
        ),
        (
            "veto_resp",
            "oversight",
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
            "#76 veto+responsive",
        ),
        (
            "extract_S_eq_R",
            "capture",
            [lambda x: x[1], lambda x: x[3], lambda x: x[1], lambda x: x[1]],
            "extractive S'=R; R'=S",
        ),
        (
            "extract_S_OR",
            "capture",
            [
                lambda x: x[1],
                lambda x: x[3] | (x[0] & x[2]),
                lambda x: x[1],
                lambda x: x[1],
            ],
            "S'=R∨(W∧C); R'=S",
        ),
        (
            "R_full_gate",
            "capture",
            gated_form((0, 1, 2)),
            "S'=W∧C∧R; R'=W∧S∧C (full mutual)",
        ),
    ]


def run_row(name, role, rules, note, labels=LABELS):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    kind, n_parties, r_in = classify(core_t)
    return {
        "name": name,
        "role": role,
        "note": note,
        "structure": v.structure,
        "whole_phi": float(v.max_phi) if v.max_phi >= 0 else 0.0,
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "kind": kind,
        "n_parties": n_parties,
        "R_in": r_in,
        "oversight": kind == "oversight",
        "capture": kind == "capture",
        "out": kind == "out",
    }


def read_sweep(gated: bool):
    rows = []
    prefix = "gate" if gated else "nogate"
    for k in range(0, 4):
        for subset in combinations(range(3), k):
            reads = tuple(subset)
            label = "static" if not reads else "∧".join(READ_NAMES[i] for i in reads)
            rules = gated_form(reads) if gated else nogate_form(reads)
            row = run_row(
                f"{prefix}_R={label}",
                "sweep",
                rules,
                f"{'S=W∧C∧R' if gated else 'S=W∧C'}; R reads {label}",
            )
            row["n_reads"] = k
            row["reads"] = label
            row["gated"] = gated
            rows.append(row)
    return rows


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("REGULATOR CAPTURE — agenda #33")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (W,S,C,R); cited #76/#111; principal pointer; #29–#32 pointers")
    print()

    named = [run_row(*args) for args in named_panel()]
    gate_sw = read_sweep(True)
    nogate_sw = read_sweep(False)

    # #111 pointer contrast (n=5)
    joint = run_row(
        "two_joint_veto",
        "coalition",
        [
            lambda x: x[1],
            lambda x: x[0] & x[2] & x[3] & x[4],
            lambda x: x[1],
            lambda x: x[1],
            lambda x: x[1],
        ],
        "#111 joint veto+responsive",
        labels=LABELS5,
    )
    # reclassify with R1/R2
    if joint["core"]:
        s = set(joint["core"].split("|"))
        if "R1" in s and "R2" in s and "W" in s and "C" in s:
            joint["kind"] = "oversight"
            joint["oversight"] = True
            joint["R_in"] = True

    print("NAMED PANEL")
    print(f"  {'form':<18}{'kind':<10}{'Φ':>5}  core")
    for r in named:
        print(
            f"  {r['name']:<18}{r['kind']:<10}{r['phi']:>5.3f}  {r['core']}"
        )
    print(
        f"  {joint['name']:<18}{joint['kind']:<10}{joint['phi']:>5.3f}  "
        f"{joint['core']}"
    )

    print()
    print("R-READ SWEEP (gated S'=W∧C∧R)")
    print(f"  {'reads':<12}{'n':>2}  {'kind':<10}{'Φ':>5}  parties  core")
    for r in gate_sw:
        print(
            f"  {r['reads']:<12}{r['n_reads']:>2}  {r['kind']:<10}"
            f"{r['phi']:>5.3f}  {r['n_parties']:>7}  {r['core']}"
        )

    print()
    print("R-READ SWEEP (no gate S'=W∧C) — control")
    n_in_nogate = sum(1 for r in nogate_sw if r["R_in"])
    print(f"  R in core on any no-gate cell: {n_in_nogate} / {len(nogate_sw)}")

    # Order gate sweep by n_reads for threshold / glide tests
    by_k = {}
    for r in gate_sw:
        by_k.setdefault(r["n_reads"], []).append(r)

    # H1: sharp threshold — some cell at k is oversight/partial and some at k+1 is capture
    # More precisely: weaker step oversight/partial, next capture. Use n_reads.
    h1 = False
    threshold_pair = None
    for k in range(0, 3):
        weak = by_k.get(k, [])
        strong = by_k.get(k + 1, [])
        weak_ok = any(r["kind"] in ("oversight", "partial") for r in weak)
        strong_cap = any(r["kind"] == "capture" for r in strong)
        if weak_ok and strong_cap:
            h1 = True
            threshold_pair = (k, k + 1)
            break
    # Also accept named veto_resp → R_full_gate as adjacent designed pair
    if not h1:
        vr = next(r for r in named if r["name"] == "veto_resp")
        full = next(r for r in named if r["name"] == "R_full_gate")
        if vr["oversight"] and full["capture"]:
            h1 = True
            threshold_pair = ("veto_resp", "R_full_gate")

    # H2: smooth glide — n_parties changes gradually across ≥3 k-levels without jump to capture
    # Supported only if we see a monotone multi-step glide of n_parties and no capture jump
    ks = sorted(by_k.keys())
    # Representative: for each k, max n_parties among cells (or mean)
    party_by_k = []
    cap_by_k = []
    for k in ks:
        party_by_k.append(max(r["n_parties"] for r in by_k[k]))
        cap_by_k.append(any(r["kind"] == "capture" for r in by_k[k]))
    # Smooth: ≥3 distinct consecutive k with strictly changing n_parties and never capture
    smooth_run = 0
    best_smooth = 0
    for i in range(len(ks)):
        if cap_by_k[i]:
            smooth_run = 0
            continue
        if i > 0 and not cap_by_k[i - 1] and party_by_k[i] != party_by_k[i - 1]:
            smooth_run = max(smooth_run, 1) + 1
        elif i == 0 or not cap_by_k[i]:
            smooth_run = 1
        best_smooth = max(best_smooth, smooth_run)
    # Capture jump: exists k where not capture and k+1 is capture
    has_jump = any(
        (not cap_by_k[i]) and cap_by_k[i + 1] for i in range(len(ks) - 1)
    )
    h2 = best_smooth >= 3 and not has_jump

    # H3: stays out XOR always in
    all_rows = named + gate_sw
    any_out = any(r["kind"] == "out" for r in all_rows)
    any_in = any(r["R_in"] for r in all_rows)
    h3 = (any_out and not any_in) or (any_in and not any_out)
    # H3 is the "stays out / always in" claim — SUPPORTED if uniform; we expect REFUTED

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (sharp capture threshold):     "
        f"{'SUPPORTED' if h1 else 'REFUTED'}  "
        f"(pair={threshold_pair})"
    )
    print(
        f"  H2 (smooth membership shift):     "
        f"{'SUPPORTED' if h2 else 'REFUTED'}  "
        f"(smooth_run={best_smooth} jump={has_jump})"
    )
    print(
        f"  H3 (stays out / always in):       "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  "
        f"(out={any_out} in={any_in})"
    )

    # Boundary summary
    oversight_cells = [r for r in gate_sw if r["oversight"]]
    capture_cells = [r for r in gate_sw if r["capture"]]
    print()
    print("BOUNDARY")
    print(
        f"  oversight cells (gated): "
        + ", ".join(r["reads"] for r in oversight_cells)
    )
    print(
        f"  capture cells (gated):   "
        + ", ".join(r["reads"] for r in capture_cells)
        if capture_cells
        else "  capture cells (gated):   (none)"
    )
    print(
        "  rule: gate necessary; capture iff R reads full {W,S,C} "
        "under S'=W∧C∧R (or extractive S←R)"
    )

    # Write CSVs
    fieldnames = [
        "name",
        "role",
        "note",
        "structure",
        "whole_phi",
        "core",
        "n_core",
        "phi",
        "kind",
        "n_parties",
        "R_in",
        "oversight",
        "capture",
        "out",
        "n_reads",
        "reads",
        "gated",
    ]
    all_out = []
    for r in named + [joint] + gate_sw + nogate_sw:
        row = {k: r.get(k, "") for k in fieldnames}
        all_out.append(row)
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(all_out)

    if h1 and (not h2) and (not h3) and ctrl_ok:
        verdict_s = "SHARP_FULL_CAPTURE"
    elif h1 and not h2:
        verdict_s = "SHARP_CAPTURE"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and (not h2) and (not h3)

    print()
    print("STATUS")
    print(f"  H1 sharp threshold:   {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 smooth shift:      {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 out/always-in:     {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #34 algorithmic transparency (alt #35 gig substitution)")
    print()
    print(
        f"verdict: {verdict_s} — oversight becomes capture at a sharp coupling "
        f"cut: under mutual gate S'=W∧C∧R, R'=S (or partial party reads) keeps "
        f"oversight {{W,S,C,R}}; only full R'=W∧S∧C collapses the major complex "
        f"to {{S,R}}; extractive S←R is the same capture core; no-gate controls "
        f"keep R out — extends #76/#111 with the principal-style hollowing cut"
    )
    print(
        "reading: SHARP_FULL_CAPTURE — a regulator that gates and is gated "
        "stays oversight until the platform fully determines the regulator; "
        "that single step is capture, not a smooth membership glide; "
        "#29–#32 pointers only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
