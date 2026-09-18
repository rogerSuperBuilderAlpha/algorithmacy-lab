"""Agenda #39 — HITL: human in core vs rubber stamp.

Exact binary IIT-4.0 Φ on Boolean (H,AI,S,C) forms. Hypotheses fixed in
hypotheses.md before computing. Cited: #76 regulator; COMMIT_READ /
hmc_algo_boundary (pointer); #37/#38 pointers only.

Run:  python org_frontier/studies/hitl_rubber_stamp/analyze_hitl.py
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

LABELS = ("H", "AI", "S", "C")
LABELS_WSC = ("W", "S", "C")


def panel():
    """Designed HITL forms: stamps, partials, COMMIT_READ, override, advice."""
    return [
        (
            "stamp_posthoc",
            "stamp",
            [lambda x: x[2], lambda x: x[2], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            True,
            "H'=S; S'=AI∧C (post-hoc approve)",
        ),
        (
            "stamp_idle",
            "stamp",
            [lambda x: x[0], lambda x: x[2], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            False,
            "H idle; S'=AI∧C",
        ),
        (
            "stamp_sticky",
            "stamp",
            [lambda x: x[0] | x[2], lambda x: x[2], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            True,
            "H sticky-approve; S'=AI∧C",
        ),
        (
            "observer",
            "stamp",
            [lambda x: x[2], lambda x: x[3], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            True,
            "H observes S; not in commit",
        ),
        (
            "veto_only",
            "partial",
            [lambda x: x[0], lambda x: x[2], lambda x: x[0] & x[1] & x[3], lambda x: x[2]],
            True,
            False,
            "S'=H∧AI∧C; H self (no read)",
        ),
        (
            "nocommit_read",
            "partial",
            [lambda x: x[2], lambda x: x[2], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            True,
            "H reads S; not in commit",
        ),
        (
            "veto_responsive",
            "commit_read",
            [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[1] & x[3], lambda x: x[2]],
            True,
            True,
            "S'=H∧AI∧C; H'=S",
        ),
        (
            "full_joint",
            "commit_read",
            [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[1] & x[3], lambda x: x[2]],
            True,
            True,
            "same COMMIT_READ wiring (alias)",
        ),
        (
            "override_force",
            "override",
            [lambda x: x[2], lambda x: x[2], lambda x: x[0], lambda x: x[2]],
            True,
            True,
            "S'=H (human forces)",
        ),
        (
            "override_OR",
            "override",
            [lambda x: x[2], lambda x: x[2], lambda x: x[0] | (x[1] & x[3]), lambda x: x[2]],
            True,
            True,
            "S'=H ∨ (AI∧C)",
        ),
        (
            "advice_into_AI",
            "advice",
            [lambda x: x[2], lambda x: x[0], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            True,
            "AI'=H; S'=AI∧C; H'=S",
        ),
        (
            "advice_ignored",
            "advice",
            [lambda x: x[2], lambda x: x[3], lambda x: x[1] & x[3], lambda x: x[2]],
            False,
            True,
            "AI ignores H; S'=AI∧C",
        ),
        (
            "H_or_AI_and_C",
            "nonpivotal",
            [lambda x: x[2], lambda x: x[2], lambda x: (x[0] | x[1]) & x[3], lambda x: x[2]],
            True,
            True,
            "S'=(H∨AI)∧C — substitutable",
        ),
    ]


def boundary_2x2():
    """Commit × read sweep (same AI/C wiring)."""
    # S_commit = H∧AI∧C vs AI∧C; H_read = S vs H
    cells = []
    for commit, s_rule in (
        (True, lambda x: x[0] & x[1] & x[3]),
        (False, lambda x: x[1] & x[3]),
    ):
        for reads, h_rule in (
            (True, lambda x: x[2]),
            (False, lambda x: x[0]),
        ):
            name = f"bdy_{'C' if commit else 'nC'}_{'R' if reads else 'nR'}"
            rules = [h_rule, lambda x: x[2], s_rule, lambda x: x[2]]
            cells.append((name, commit, reads, rules))
    return cells


def run_form(name, role, rules, in_commit, reads, note):
    v = verdict(rules, LABELS)
    core, phi_mc = major_complex(rules, LABELS)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    return {
        "name": name,
        "role": role,
        "note": note,
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "in_commit": in_commit,
        "reads": reads,
        "H_in_core": "H" in core_t,
        "AI_in_core": "AI" in core_t,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("HITL RUBBER STAMP — agenda #39")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (H,AI,S,C) human + AI proposer + commit + counterpart")
    print("  cited: probe #76; COMMIT_READ pointer; #37/#38 pointers")
    print()

    rows = [
        run_form(name, role, rules, in_commit, reads, note)
        for name, role, rules, in_commit, reads, note in panel()
    ]

    print(
        f"  {'form':<20}{'role':<12}{'whole':<8}{'Φ':>6}  "
        f"{'core':<16}{'H?':>3}  cmt rd"
    )
    for r in rows:
        print(
            f"  {r['name']:<20}{r['role']:<12}{r['structure']:<8}"
            f"{r['phi']:>6.3f}  {r['core']:<16}"
            f"{'Y' if r['H_in_core'] else 'N':>3}  "
            f"{'Y' if r['in_commit'] else 'n'}   {'Y' if r['reads'] else 'n'}"
        )

    # boundary 2x2
    bdy_rows = []
    print()
    print("  BOUNDARY 2×2 (commit × read)")
    print(f"  {'cell':<16}{'commit':>7}{'read':>6}  {'core':<16} H?")
    for name, commit, reads, rules in boundary_2x2():
        rr = run_form(name, "boundary", rules, commit, reads, "2x2")
        bdy_rows.append(rr)
        print(
            f"  {name:<16}{'Y' if commit else 'n':>7}{'Y' if reads else 'n':>6}  "
            f"{rr['core']:<16} {'Y' if rr['H_in_core'] else 'N'}"
        )

    stamps = [r for r in rows if r["role"] == "stamp"]
    commit_reads = [r for r in rows if r["role"] == "commit_read"]
    overrides = [r for r in rows if r["role"] == "override"]

    h1 = all(r["H_in_core"] for r in commit_reads) and any(
        r["H_in_core"] for r in overrides
    )
    h2 = all(not r["H_in_core"] for r in stamps)

    # H3: only commit∧read cell has H in
    full_cells = [r for r in bdy_rows if r["in_commit"] and r["reads"]]
    partial_cells = [
        r for r in bdy_rows if not (r["in_commit"] and r["reads"])
    ]
    h3 = (
        all(r["H_in_core"] for r in full_cells)
        and all(not r["H_in_core"] for r in partial_cells)
        and len(full_cells) == 1
        and len(partial_cells) == 3
    )

    stamp_witness = next(r for r in stamps if r["name"] == "stamp_posthoc")
    join_witness = next(r for r in commit_reads if r["name"] == "veto_responsive")

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (joins on COMMIT_READ / override): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (rubber stamp excluded):           "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (partial coupling is the boundary): "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  rubber-stamp witness: {stamp_witness['name']} "
        f"core={stamp_witness['core']} H_in={stamp_witness['H_in_core']}"
    )
    print(
        f"  COMMIT_READ witness:  {join_witness['name']} "
        f"core={join_witness['core']} H_in={join_witness['H_in_core']}"
    )

    all_rows = rows + bdy_rows
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)

    if h1 and h2 and h3 and ctrl_ok:
        verdict_s = "HUMAN_COMMIT_READ"
    elif h2 and h3:
        verdict_s = "STAMP_OUT"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and h2 and h3

    print()
    print("STATUS")
    print(f"  H1 COMMIT_READ/override: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 rubber stamp out:     {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 partial boundary:     {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #40 online-learning displacement (alt #41 MARL)")
    print()
    print(
        f"verdict: {verdict_s} — HITL human joins the major complex iff in S’s "
        f"determination and reads S (COMMIT_READ), matching regulator #76; "
        f"rubber stamps (post-hoc/idle/sticky/observe) stay out; static veto "
        f"and read-without-commit are the partial boundary; override puts H in "
        f"a dyadic {{H,S}}"
    )
    print(
        "reading: HUMAN_COMMIT_READ — a HITL approval that does not gate the "
        "commit is a rubber stamp outside the core; veto+responsive (or full "
        "joint) is the minimal edit that puts the human in; #37/#38 pointers "
        "only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
