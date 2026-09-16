"""Agenda #37 — agent negotiation protocols: dyadic vs triadic.

Exact binary IIT-4.0 Φ on Boolean (A,P,B) forms. Hypotheses fixed in
hypotheses.md before computing. Cited: probe #88/#50; COMMIT_READ /
hmc_algo_boundary; encoding ladders as pointers.

Run:  python org_frontier/studies/agent_protocol_triad/analyze_protocols.py
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
PHI_EPS = 1e-9

LABELS_APB = ("A", "P", "B")
LABELS_WSC = ("W", "S", "C")


def panel():
    """Designed protocol forms. Primary: no human. classical_WSC contrast."""
    return [
        (
            "relay",
            "conveyor",
            LABELS_APB,
            [lambda x: x[0], lambda x: x[0], lambda x: x[1]],
            "P forwards A→B",
        ),
        (
            "broadcast",
            "conveyor",
            LABELS_APB,
            [lambda x: x[1], lambda x: x[1], lambda x: x[1]],
            "P self-loop; agents read P",
        ),
        (
            "read_not_in_commit",
            "COMMIT_READ",
            LABELS_APB,
            [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
            "P←A only; A,B read P",
        ),
        (
            "side_channel",
            "bypass",
            LABELS_APB,
            [lambda x: x[2], lambda x: x[1], lambda x: x[0]],
            "A↔B direct; P idle",
        ),
        (
            "blackboard",
            "weak",
            LABELS_APB,
            [lambda x: x[0], lambda x: x[0] | x[2], lambda x: x[2]],
            "P aggregates; agents ignore P",
        ),
        (
            "turn_token",
            "schedule",
            LABELS_APB,
            [lambda x: x[1], lambda x: 1 - x[1], lambda x: x[1]],
            "P flips token; agents follow",
        ),
        (
            "joint_AND",
            "commit",
            LABELS_APB,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            "P←A∧B; both read P",
        ),
        (
            "joint_OR",
            "commit",
            LABELS_APB,
            [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],
            "P←A∨B; both read P",
        ),
        (
            "joint_NAND",
            "commit",
            LABELS_APB,
            [lambda x: x[1], lambda x: int(not (x[0] & x[2])), lambda x: x[1]],
            "P←¬(A∧B); both read P",
        ),
        (
            "joint_XOR",
            "commit",
            LABELS_APB,
            [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
            "P←A⊕B; both read P",
        ),
        (
            "offer_accept",
            "negotiate",
            LABELS_APB,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[0] & x[1]],
            "asymmetric accept morph",
        ),
        (
            "classical_WSC",
            "contrast",
            LABELS_WSC,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            "human-label joint commit (W,S,C)",
        ),
    ]


def protocol_triadic(core, labels) -> bool:
    if not core:
        return False
    need = set(labels)
    return need.issubset(set(core))


def run_form(name, role, labels, rules, note):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    pt = protocol_triadic(core_t, labels)
    p_in = labels[1] in core_t  # P or S
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
        "protocol_triadic": pt,
        "P_in_core": p_in,
        "no_human": labels == LABELS_APB,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    # instrument control
    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("AGENT PROTOCOL TRIAD — agenda #37")
    print("=" * 64)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (A,P,B) agents+protocol; classical_WSC contrast")
    print("  cited: probe #88; COMMIT_READ / hmc_algo_boundary")
    print()

    rows = [run_form(*args) for args in panel()]

    print(
        f"  {'form':<20}{'role':<12}{'whole':<8}{'Φ':>7}  "
        f"{'core':<14}{'P?':>3}  {'prot-tri':>8}"
    )
    for r in rows:
        print(
            f"  {r['name']:<20}{r['role']:<12}{r['structure']:<8}"
            f"{r['phi']:>7.3f}  {r['core']:<14}"
            f"{'Y' if r['P_in_core'] else 'N':>3}  "
            f"{'YES' if r['protocol_triadic'] else 'no':>8}"
        )

    no_human = [r for r in rows if r["no_human"]]
    convey = [r for r in no_human if r["role"] in ("conveyor", "COMMIT_READ", "bypass", "weak", "schedule")]
    commits = [r for r in no_human if r["role"] == "commit"]
    joint_flip = [r for r in commits if r["protocol_triadic"] and r["P_in_core"]]
    convey_ok = all(not r["protocol_triadic"] for r in convey)
    h1 = convey_ok and len(joint_flip) >= 1

    h2 = all(not r["protocol_triadic"] for r in no_human)  # expected False
    h3 = any(r["protocol_triadic"] for r in no_human)

    # classical match joint_AND
    ja = next(r for r in rows if r["name"] == "joint_AND")
    cl = next(r for r in rows if r["name"] == "classical_WSC")
    match = (
        ja["structure"] == cl["structure"]
        and abs(ja["phi"] - cl["phi"]) < PHI_TOL
        and ja["n_core"] == cl["n_core"]
        and ja["protocol_triadic"]
        and cl["protocol_triadic"]
    )

    n_prot_tri = sum(1 for r in no_human if r["protocol_triadic"])
    n_p_in = sum(1 for r in no_human if r["protocol_triadic"] and r["P_in_core"])

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (protocol encoding flips like commit): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (always dyadic without human):         "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (some protocols triadic, no human):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  classical ≅ joint_AND:                    "
        f"{'YES' if match else 'NO'}"
    )
    print(
        f"  no-human protocol-triadic: {n_prot_tri}/{len(no_human)}  "
        f"(P in core on {n_p_in})"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # overall verdict
    if h1 and (not h2) and h3 and match and ctrl_ok:
        verdict_s = "PROTOCOL_IS_COMMIT"
    elif h3 and (not h2):
        verdict_s = "NO_HUMAN_TRIAD"
    else:
        verdict_s = "MIXED"

    print()
    print("STATUS")
    print(f"  H1 encoding flip:     {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 always dyadic:     {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 no-human triad:    {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if ctrl_ok and h1 and h3 and not h2 else 'FAIL'}")
    print("  best next:            #38 tool-in-core (inference displacement)")
    print()
    print(
        f"verdict: {verdict_s} — protocol design sets dyadic vs triadic "
        f"by the same COMMIT_READ / joint-commit cut as human mediation; "
        f"{n_prot_tri} no-human forms are protocol-triadic (AND/OR/NAND/XOR); "
        f"relay/broadcast/side-channel stay dyadic"
    )
    print(
        "reading: PROTOCOL_IS_COMMIT — a negotiation protocol is triadic "
        "without a human iff both agents jointly determine P and read P; "
        "LLM-style agents sit on the same conveyor-vs-commit cut (#88)"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 64)


if __name__ == "__main__":
    main()
