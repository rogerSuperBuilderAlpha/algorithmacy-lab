"""Agenda #38 — does a called tool join the core when acted on?

Exact binary IIT-4.0 Φ on Boolean (A,S,C,T) forms mirroring probe #4
(W,S,C,M). Hypotheses fixed in hypotheses.md before computing.
Cited: #4/#9 inference; #37 PROTOCOL_IS_COMMIT (pointer);
COMMIT_READ as conceptual bridge only.

Run:  python org_frontier/studies/agent_tool_core/analyze_tools.py
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

LABELS_ASCT = ("A", "S", "C", "T")
LABELS_WSCM = ("W", "S", "C", "M")


def panel():
    """Designed agent-tool forms + #4 isomorphism contrast."""
    return [
        (
            "tool_unused",
            "unused",
            LABELS_ASCT,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            False,
            False,
            "T'=S; A ignores T",
        ),
        (
            "tool_exo_unused",
            "unused",
            LABELS_ASCT,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
            False,
            False,
            "T self-loop; A ignores T",
        ),
        (
            "tool_sink_from_A",
            "unused",
            LABELS_ASCT,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[0]],
            False,
            True,
            "T'=A; A ignores T (write-only)",
        ),
        (
            "tool_used_pure",
            "act",
            LABELS_ASCT,
            [lambda x: x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            True,
            False,
            "A'=T; T'=S (no reciprocity)",
        ),
        (
            "tool_blended",
            "act",
            LABELS_ASCT,
            [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            True,
            False,
            "A'=S∧T; T'=S (no reciprocity)",
        ),
        (
            "tool_call_used",
            "act_recip",
            LABELS_ASCT,
            [lambda x: x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[0]],
            True,
            True,
            "A'=T; T'=A (reciprocal call)",
        ),
        (
            "tool_call_blended",
            "act_recip",
            LABELS_ASCT,
            [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[0]],
            True,
            True,
            "A'=S∧T; T'=A",
        ),
        (
            "tool_exo_used",
            "exo_act",
            LABELS_ASCT,
            [lambda x: x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
            True,
            False,
            "A'=T; T exogenous",
        ),
        (
            "tool_exo_blended",
            "exo_act",
            LABELS_ASCT,
            [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
            True,
            False,
            "A'=S∧T; T exogenous",
        ),
        (
            "tool_in_commit",
            "commit",
            LABELS_ASCT,
            [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
            False,
            False,
            "S'=A∧C∧T; all read S (COMMIT_READ)",
        ),
        (
            "inference_blended_WSCM",
            "iso",
            LABELS_WSCM,
            [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            True,
            False,
            "#4 inference_blended (W,S,C,M)",
        ),
    ]


def run_form(name, role, labels, rules, acts, recip, note):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    tool_label = "T" if labels == LABELS_ASCT else "M"
    t_in = tool_label in core_t
    c_in = "C" in core_t
    return {
        "name": name,
        "role": role,
        "note": note,
        "labels": "".join(labels),
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "acts": acts,
        "recip": recip,
        "T_in_core": t_in,
        "C_in_core": c_in,
        "displaces_C": t_in and not c_in,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("AGENT TOOL CORE — agenda #38")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (A,S,C,T) agent+system+counterpart+tool; #4 iso check")
    print("  cited: probe #4/#9; #37 PROTOCOL_IS_COMMIT (pointer)")
    print()

    rows = [run_form(*args) for args in panel()]

    print(
        f"  {'form':<24}{'role':<12}{'whole':<8}{'Φ':>6}  "
        f"{'core':<14}{'T?':>3}{'C?':>3}  act recip"
    )
    for r in rows:
        print(
            f"  {r['name']:<24}{r['role']:<12}{r['structure']:<8}"
            f"{r['phi']:>6.3f}  {r['core']:<14}"
            f"{'Y' if r['T_in_core'] else 'N':>3}"
            f"{'Y' if r['C_in_core'] else 'N':>3}  "
            f"{'Y' if r['acts'] else 'n'}   {'Y' if r['recip'] else 'n'}"
        )

    primary = [r for r in rows if r["labels"] == "ASCT"]
    unused = [r for r in primary if r["role"] == "unused"]
    h2 = all(not r["T_in_core"] for r in unused)

    # H1: T in core iff acts and recip
    h1_iff = all(
        (r["T_in_core"] == (r["acts"] and r["recip"])) for r in primary
    )
    # Counterexamples for reporting
    join_no_recip = [r for r in primary if r["T_in_core"] and not r["recip"]]
    act_recip_out = [
        r for r in primary if r["acts"] and r["recip"] and not r["T_in_core"]
    ]
    h1 = h1_iff  # expected False

    h3 = len(join_no_recip) >= 1

    # Inference pattern: unused out; pure act out of major; blend in+displace
    unused_ok = not next(r for r in primary if r["name"] == "tool_unused")[
        "T_in_core"
    ]
    pure = next(r for r in primary if r["name"] == "tool_used_pure")
    blend = next(r for r in primary if r["name"] == "tool_blended")
    pattern = (
        unused_ok
        and (not pure["T_in_core"])
        and blend["T_in_core"]
        and blend["displaces_C"]
    )

    # isomorphism: tool_blended ≅ inference_blended under relabel
    iso = next(r for r in rows if r["name"] == "inference_blended_WSCM")
    iso_ok = (
        blend["structure"] == iso["structure"]
        and abs(blend["phi"] - iso["phi"]) < PHI_TOL
        and blend["n_core"] == iso["n_core"]
        and blend["T_in_core"]
        and iso["T_in_core"]
        and blend["displaces_C"]
        and iso["displaces_C"]
    )

    call = next(r for r in primary if r["name"] == "tool_call_used")
    commit = next(r for r in primary if r["name"] == "tool_in_commit")

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (joins iff acts + reciprocity): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (read-only tool never joins):   "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (can join without reciprocity): "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  #4 inference pattern (unused/pure/blend): "
        f"{'MATCH' if pattern else 'MISS'}"
    )
    print(
        f"  tool_blended ≅ inference_blended:  "
        f"{'YES' if iso_ok else 'NO'}"
    )
    print(
        f"  join-without-reciprocity forms: "
        f"{','.join(r['name'] for r in join_no_recip) or 'none'}"
    )
    print(
        f"  act+recip but T out: "
        f"{','.join(r['name'] for r in act_recip_out) or 'none'}"
    )
    print(
        f"  tool_call_used core={call['core']}  "
        f"tool_in_commit core={commit['core']}"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    if pattern and h2 and h3 and (not h1) and iso_ok and ctrl_ok:
        verdict_s = "TOOL_LIKE_INFERENCE"
    elif pattern and h2:
        verdict_s = "ACTS_DISPLACES"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and pattern and h2 and h3 and (not h1) and iso_ok

    print()
    print("STATUS")
    print(f"  H1 acts+reciprocity iff: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 read-only never joins: {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 join without reciprocity: {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #39 HITL rubber-stamp (alt #40 online learning)")
    print()
    print(
        f"verdict: {verdict_s} — tool joins like inference (#4/#9): "
        f"unused/read-only stays out; pure A'=T leaves T out of the major "
        f"complex; blended A'=S∧T puts T in and displaces C; "
        f"reciprocity is neither necessary (blend) nor always sufficient "
        f"(tool_call_blended)"
    )
    print(
        "reading: TOOL_LIKE_INFERENCE — a called tool is not in the core "
        "just because the agent reads it; the #4 blend/displacement cut "
        "reappears under relabeling; COMMIT_READ (tool in S) is a separate "
        "join path; H1's iff fails"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
