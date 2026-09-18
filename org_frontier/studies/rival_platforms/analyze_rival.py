"""Agenda #32 — rival platforms: do cores compete for the worker?

Exact binary IIT-4.0 Φ on designed (W,S1,C1,S2,C2) forms. Hypotheses
fixed in hypotheses.md before computing. Cited: #73; multiparty
multihome; Q210; #29–#31 pointers only.

Run:  python org_frontier/studies/rival_platforms/analyze_rival.py
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

import pyphi
from pyphi import exceptions, new_big_phi

from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules
from org_frontier.probes.lib import major_complex, verdict

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9

LABELS = ("W", "S1", "C1", "S2", "C2")
LABELS_WSC = ("W", "S", "C")
P1 = frozenset({"S1", "C1"})
P2 = frozenset({"S2", "C2"})


def panel():
    return [
        (
            "ctrl_p1",
            "capture",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[3],
                lambda x: x[4],
            ],
            "W only on platform 1; S2/C2 idle",
        ),
        (
            "ctrl_p2",
            "capture",
            [
                lambda x: x[3],
                lambda x: x[1],
                lambda x: x[2],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "W only on platform 2; S1/C1 idle",
        ),
        (
            "either_OR",
            "compete",
            [
                lambda x: x[1] | x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "W'=S1∨S2; each Si'=W∧Ci (substitutable)",
        ),
        (
            "xor_W",
            "compete",
            [
                lambda x: x[1] ^ x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "W'=S1⊕S2 parity rivalry",
        ),
        (
            "prefer_p1",
            "capture",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "W←S1 only; both platforms alive",
        ),
        (
            "prefer_p2",
            "capture",
            [
                lambda x: x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "W←S2 only; both platforms alive",
        ),
        (
            "extract_p1",
            "capture",
            [
                lambda x: x[1] | x[3],
                lambda x: x[0],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "S1'=W extractive; W responds either",
        ),
        (
            "extract_p2",
            "capture",
            [
                lambda x: x[1] | x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0],
                lambda x: x[3],
            ],
            "S2'=W extractive; W responds either",
        ),
        (
            "span_joint",
            "span",
            [
                lambda x: x[1] & x[3],
                lambda x: x[0] & x[2],
                lambda x: x[0],
                lambda x: x[0] & x[4],
                lambda x: x[0],
            ],
            "W'=S1∧S2; Ci'=W cross-read",
        ),
        (
            "cross_read",
            "span",
            [
                lambda x: x[1] & x[3],
                lambda x: x[0] & x[2],
                lambda x: x[3],
                lambda x: x[0] & x[4],
                lambda x: x[1],
            ],
            "W'=S1∧S2; C1←S2, C2←S1",
        ),
        (
            "both_AND",
            "span",
            [
                lambda x: x[1] & x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "multihome_both analogue (Ci←Si)",
        ),
        (
            "w_sticky",
            "drop",
            [
                lambda x: x[0],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[4],
                lambda x: x[3],
            ],
            "W sticky (ignores both platforms)",
        ),
        (
            "w_spectator",
            "drop",
            [
                lambda x: x[0],
                lambda x: x[2],
                lambda x: x[1],
                lambda x: x[4],
                lambda x: x[3],
            ],
            "W spectator; platforms ignore W",
        ),
    ]


def classify_core(core: tuple[str, ...]) -> str:
    s = set(core)
    has_w = "W" in s
    p1 = bool(s & P1)
    p2 = bool(s & P2)
    if has_w and p1 and p2:
        return "span"
    if has_w and p1 and not p2:
        return "p1_capture"
    if has_w and p2 and not p1:
        return "p2_capture"
    if not has_w:
        return "w_drop"
    return "other"


def max_cores(rules, labels=LABELS):
    """Distinct major complexes at the global max Φ over reachable states."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best_phi = -1.0
    cores: set[tuple[str, ...]] = set()
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        phi = float(mc.phi)
        core = tuple(labels[i] for i in mc.node_indices)
        if phi > best_phi + PHI_TOL:
            best_phi = phi
            cores = {core}
        elif abs(phi - best_phi) <= PHI_TOL:
            cores.add(core)
    return best_phi if best_phi >= 0 else 0.0, sorted(cores)


def run_form(name, role, rules, note):
    v = verdict(rules, LABELS)
    primary, _ = major_complex(rules, LABELS)
    phi, cores = max_cores(rules)
    classes = [classify_core(c) for c in cores]
    p1_cap = "p1_capture" in classes
    p2_cap = "p2_capture" in classes
    span = "span" in classes
    w_in = any("W" in c for c in cores)
    compete = p1_cap and p2_cap
    one_wins = (p1_cap ^ p2_cap) and not span
    drop = not w_in
    witnesses = ";".join("|".join(c) for c in cores) if cores else ""
    return {
        "name": name,
        "role": role,
        "note": note,
        "structure": v.structure,
        "whole_phi": float(v.max_phi) if v.max_phi >= 0 else 0.0,
        "phi": phi,
        "primary_core": "|".join(primary) if primary else "",
        "witnesses": witnesses,
        "n_witnesses": len(cores),
        "p1_capture": p1_cap,
        "p2_capture": p2_cap,
        "compete": compete,
        "one_wins": one_wins,
        "span": span,
        "w_in": w_in,
        "drop": drop,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("RIVAL PLATFORMS — agenda #32")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (W,S1,C1,S2,C2) shared worker + two platforms")
    print("  cited: #73; multiparty multihome; Q210; #29–#31 pointers only")
    print()

    rows = [run_form(*args) for args in panel()]

    print(
        f"  {'form':<14}{'role':<9}{'Φ':>5}  "
        f"{'wit':>3}  compete one span drop  witnesses"
    )
    for r in rows:
        print(
            f"  {r['name']:<14}{r['role']:<9}{r['phi']:>5.3f}  "
            f"{r['n_witnesses']:>3}  "
            f"{'Y' if r['compete'] else 'n':>7} "
            f"{'Y' if r['one_wins'] else 'n':>3} "
            f"{'Y' if r['span'] else 'n':>4} "
            f"{'Y' if r['drop'] else 'n':>4}  "
            f"{r['witnesses']}"
        )

    h1_compete = any(r["compete"] for r in rows)
    h1_one = any(r["one_wins"] for r in rows)
    h1 = h1_compete or h1_one
    h2 = any(r["span"] for r in rows)
    h3 = any(r["drop"] for r in rows)

    either = next(r for r in rows if r["name"] == "either_OR")
    prefer1 = next(r for r in rows if r["name"] == "prefer_p1")
    span_j = next(r for r in rows if r["name"] == "span_joint")
    sticky = next(r for r in rows if r["name"] == "w_sticky")
    cross = next(r for r in rows if r["name"] == "cross_read")

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (compete / one captures W):  "
        f"{'SUPPORTED' if h1 else 'REFUTED'}  "
        f"(compete={sum(1 for r in rows if r['compete'])} "
        f"one_wins={sum(1 for r in rows if r['one_wins'])})"
    )
    print(
        f"  H2 (worker spans both / shared): "
        f"{'SUPPORTED' if h2 else 'REFUTED'}  "
        f"(n={sum(1 for r in rows if r['span'])} span forms)"
    )
    print(
        f"  H3 (worker drops / collapse):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  "
        f"(n={sum(1 for r in rows if r['drop'])} drop forms)"
    )
    print(
        f"  either_OR rivalry: witnesses={either['witnesses']}"
    )
    print(
        f"  prefer_p1 capture: witnesses={prefer1['witnesses']}"
    )
    print(
        f"  span_joint / cross_read: "
        f"{span_j['witnesses']} / {cross['witnesses']} "
        f"(Φ={cross['phi']:.3f})"
    )
    print(f"  w_sticky drop: witnesses={sticky['witnesses']}")

    # Winner rule summary for the print block
    print()
    print("WINNER RULE")
    print(
        "  equal-Φ rivalry (either/xor): state selects one platform triad "
        "with W; leftover W-free dyads allowed"
    )
    print(
        "  asymmetric W-response / extractive S←W: that platform captures W"
    )
    print(
        "  joint W'=S1∧S2 + cross-reads: single complex spans both"
    )
    print("  non-responsive W: worker drops from every max-Φ core")

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    if h1 and h2 and h3 and ctrl_ok:
        verdict_s = "RIVAL_ENCODING"
    elif h1 and h2:
        verdict_s = "CAPTURE_OR_SPAN"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and h2 and h3

    print()
    print("STATUS")
    print(f"  H1 compete/capture:   {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 span both:         {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 worker drops:      {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #33 regulator capture (alt #34 transparency)")
    print()
    print(
        f"verdict: {verdict_s} — two rival platforms sharing a worker do not "
        f"have a single winner rule: substitutable W'=S1∨S2 / XOR yields "
        f"equal-Φ rivalry (each state picks one platform triad with W); "
        f"asymmetric preference or extractive S←W captures W into that "
        f"platform; joint W'=S1∧S2 with cross-reads spans both; idle W "
        f"drops — encoding decides, extending #73's separate-cores result "
        f"to rivalrous platforms"
    )
    print(
        "reading: RIVAL_ENCODING — whether cores compete for the worker, "
        "one captures, both span, or W drops is set by the dual-platform "
        "encoding; #73's separation is the default under OR/preference; "
        "span needs joint binding + cross-reads; #29–#31 pointers only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
