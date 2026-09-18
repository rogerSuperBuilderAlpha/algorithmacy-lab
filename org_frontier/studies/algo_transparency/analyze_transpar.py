"""Agenda #34 — algorithmic transparency of the commit rule (not channel #24).

Exact binary IIT-4.0 Φ on opaque vs rule-open encodings. Hypotheses
fixed in hypotheses.md before computing. Cited: #24; #41 pointer;
COMMIT_READ conceptual bridge only; #29–#33 pointers only.

Run:  python org_frontier/studies/algo_transparency/analyze_transpar.py
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

LABELS3 = ("W", "S", "C")
LABELS4 = ("W", "S", "C", "F")
LABELS_WSC = ("W", "S", "C")


def run(name, family, rules, labels, note, opaque_match=None, party_reads_F=None):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    return {
        "name": name,
        "family": family,
        "note": note,
        "opaque_match": opaque_match or "",
        "n": len(labels),
        "structure": v.structure,
        "whole_phi": float(v.max_phi) if v.max_phi >= 0 else 0.0,
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "F_in": "F" in core_t,
        "party_reads_F": bool(party_reads_F) if party_reads_F is not None else "",
        "W_in": "W" in core_t,
        "C_in": "C" in core_t,
        "S_in": "S" in core_t,
    }


def panel():
    rows = []

    # --- opaque baselines ---
    rows.append(
        run(
            "opaque_AND",
            "opaque",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            LABELS3,
            "classic opaque triad",
        )
    )
    rows.append(
        run(
            "opaque_XOR",
            "opaque",
            [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
            LABELS3,
            "opaque parity commit",
        )
    )
    rows.append(
        run(
            "opaque_conveyor",
            "opaque",
            [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
            LABELS3,
            "opaque conveyor S'=W (dyadic)",
        )
    )

    # --- #24 channel contrast (not rule-open) ---
    rows.append(
        run(
            "channel_p1",
            "channel",
            [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[1]],
            LABELS3,
            "#24 p=1: W'=C direct",
            opaque_match="opaque_AND",
        )
    )
    rows.append(
        run(
            "channel_mutual",
            "channel",
            [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]],
            LABELS3,
            "mutual party observation",
            opaque_match="opaque_AND",
        )
    )

    # --- rule open: parties read commit inputs ---
    rows.append(
        run(
            "open_both_inputs",
            "rule_inputs",
            [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1] & x[0]],
            LABELS3,
            "both parties read other input + S",
            opaque_match="opaque_AND",
        )
    )
    rows.append(
        run(
            "open_W_reads_C",
            "rule_inputs",
            [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1]],
            LABELS3,
            "only W reads C input",
            opaque_match="opaque_AND",
        )
    )
    rows.append(
        run(
            "open_XOR_both",
            "rule_inputs",
            [lambda x: x[1] & x[2], lambda x: x[0] ^ x[2], lambda x: x[1] & x[0]],
            LABELS3,
            "XOR commit; both read inputs",
            opaque_match="opaque_XOR",
        )
    )
    rows.append(
        run(
            "open_conveyor_inputs",
            "rule_inputs",
            [lambda x: x[1] & x[2], lambda x: x[0], lambda x: x[1] & x[0]],
            LABELS3,
            "conveyor + both read inputs",
            opaque_match="opaque_conveyor",
        )
    )

    # --- explicit rule node F ---
    rows.append(
        run(
            "F_publish_unread",
            "rule_F",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "F publishes rule; parties still only read S",
            opaque_match="opaque_AND",
            party_reads_F=False,
        )
    )
    rows.append(
        run(
            "F_parties_read",
            "rule_F",
            [
                lambda x: x[3],
                lambda x: x[0] & x[2],
                lambda x: x[3],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "parties read F (act on opened rule)",
            opaque_match="opaque_AND",
            party_reads_F=True,
        )
    )
    rows.append(
        run(
            "F_is_commit",
            "rule_F",
            [
                lambda x: x[3],
                lambda x: x[3],
                lambda x: x[3],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "S follows F; parties read F",
            opaque_match="opaque_AND",
            party_reads_F=True,
        )
    )
    rows.append(
        run(
            "F_act_blend",
            "rule_F",
            [
                lambda x: x[3] & x[1],
                lambda x: x[0] & x[2],
                lambda x: x[3] & x[1],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "parties blend F with S",
            opaque_match="opaque_AND",
            party_reads_F=True,
        )
    )
    rows.append(
        run(
            "F_parties_gate",
            "rule_F",
            [
                lambda x: x[3],
                lambda x: x[3] & x[0] & x[2],
                lambda x: x[3],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "opened F gates S with parties",
            opaque_match="opaque_AND",
            party_reads_F=True,
        )
    )
    rows.append(
        run(
            "F_one_acts",
            "rule_F",
            [
                lambda x: x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "only W reads F; C opaque",
            opaque_match="opaque_AND",
            party_reads_F=True,
        )
    )
    rows.append(
        run(
            "F_read_S_and_F",
            "rule_F",
            [
                lambda x: x[1] & x[3],
                lambda x: x[0] & x[2],
                lambda x: x[1] & x[3],
                lambda x: x[0] & x[2],
            ],
            LABELS4,
            "parties require S∧F",
            opaque_match="opaque_AND",
            party_reads_F=True,
        )
    )
    return rows


def party_core(row):
    """Party-bearing core labels excluding F (for publish-unread compare)."""
    nodes = [n for n in row["core"].split("|") if n and n != "F"]
    return "|".join(nodes)


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("ALGORITHMIC TRANSPARENCY — agenda #34")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  cited: #24; #41 pointer; COMMIT_READ bridge only; #29–#33 pointers")
    print()

    rows = panel()
    by_name = {r["name"]: r for r in rows}

    print(
        f"  {'form':<22}{'fam':<12}{'whole':<8}{'Φ':>5}  core"
    )
    for r in rows:
        print(
            f"  {r['name']:<22}{r['family']:<12}{r['structure']:<8}"
            f"{r['phi']:>5.3f}  {r['core']}"
        )

    # Matched opaque→transparent pairs (rule + channel)
    pairs = []
    for r in rows:
        if r["opaque_match"] and r["opaque_match"] in by_name:
            o = by_name[r["opaque_match"]]
            struct_flip = r["structure"] != o["structure"]
            # compare cores on shared alphabet: for F forms, compare full core
            # including F as membership change; also party-core change
            core_flip = r["core"] != o["core"] and not (
                r["n"] > o["n"] and party_core(r) == o["core"] and not r["F_in"]
            )
            # publish-unread: party core same, F out → not a core flip for H1
            if r["name"] == "F_publish_unread":
                core_flip = party_core(r) != o["core"]
            same_core_set = r["core"] == o["core"]
            phi_only = (
                (not struct_flip)
                and same_core_set
                and abs(r["phi"] - o["phi"]) > PHI_TOL
            )
            membership_change = core_flip or (
                r["n"] > o["n"] and r["F_in"] and party_core(r) != o["core"]
            )
            # F joining while party core same still counts as membership change
            if r["F_in"] and party_core(r) == o["core"]:
                membership_change = True
            if r["n"] > o["n"] and party_core(r) != o["core"]:
                membership_change = True
            if r["n"] == o["n"] and r["core"] != o["core"]:
                membership_change = True
            pairs.append(
                {
                    "trans": r["name"],
                    "opaque": o["name"],
                    "family": r["family"],
                    "struct_flip": struct_flip,
                    "membership_change": membership_change,
                    "phi_only": phi_only,
                    "dphi": r["phi"] - o["phi"],
                    "o_core": o["core"],
                    "t_core": r["core"],
                    "o_phi": o["phi"],
                    "t_phi": r["phi"],
                    "o_struct": o["structure"],
                    "t_struct": r["structure"],
                }
            )

    # H1: core membership change (or structure flip with party-core change).
    # Exclude publish-unread whole-system spectator dyadic (F idle) with party core held.
    h1_pairs = [
        p
        for p in pairs
        if p["family"] != "channel"
        and p["membership_change"]
        and p["trans"] != "F_publish_unread"
    ]
    channel_pairs = [
        p
        for p in pairs
        if p["family"] == "channel" and p["membership_change"]
    ]
    h2_pairs = [
        p
        for p in pairs
        if p["family"] != "channel" and p["phi_only"]
    ]

    h1 = len(h1_pairs) >= 1
    h2 = len(h2_pairs) >= 1

    # H3: F in core only if party_reads_F; publish-unread F out + party core = opaque
    f_rows = [r for r in rows if r["family"] == "rule_F"]
    f_ok = True
    for r in f_rows:
        reads = r["party_reads_F"]
        if r["F_in"] and not reads:
            f_ok = False
        if (not r["F_in"]) and reads and r["name"] in (
            "F_parties_read",
            "F_is_commit",
            "F_act_blend",
            "F_read_S_and_F",
        ):
            # expected act forms that should put F in — if none do, weaken
            pass
    pub = by_name["F_publish_unread"]
    opaque = by_name["opaque_AND"]
    pub_ok = (not pub["F_in"]) and party_core(pub) == opaque["core"]
    act_with_F = any(
        r["F_in"] and r["party_reads_F"]
        for r in f_rows
    )
    # converse: no F-in without act
    no_spy = all(
        (not r["F_in"]) or r["party_reads_F"] for r in f_rows
    )
    h3 = pub_ok and act_with_F and no_spy and f_ok

    print()
    print("MATCHED PAIRS (vs opaque)")
    print(
        f"  {'trans':<22}{'opaque':<16}{'Δstruct':>7}{'Δcore':>6}{'Φ-only':>7}  "
        f"cores"
    )
    for p in pairs:
        print(
            f"  {p['trans']:<22}{p['opaque']:<16}"
            f"{'Y' if p['struct_flip'] else 'n':>7}"
            f"{'Y' if p['membership_change'] else 'n':>6}"
            f"{'Y' if p['phi_only'] else 'n':>7}  "
            f"{p['o_core']} → {p['t_core']} "
            f"(Φ {p['o_phi']:.3f}→{p['t_phi']:.3f})"
        )

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (rule-open flips structure/core): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}  "
        f"(n={len(h1_pairs)} rule pairs"
        f"{'; channel also Δcore' if channel_pairs else ''})"
    )
    print(
        f"  H2 (verdict invariant, Φ only):      "
        f"{'SUPPORTED' if h2 else 'REFUTED'}  "
        f"(n={len(h2_pairs)} Φ-only pairs)"
    )
    print(
        f"  H3 (enter via open only if act):     "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  "
        f"(publish_unread ok={pub_ok}; act→F={act_with_F}; no_spy={no_spy})"
    )

    # vs #24
    ch = by_name["channel_p1"]
    print()
    print("VS #24 CHANNEL")
    print(
        f"  channel_p1: whole={ch['structure']} Φ={ch['phi']:.3f} "
        f"core={ch['core']} (Φ_max stays ~2; major complex can drop W)"
    )
    print(
        "  rule-open is not channel visibility: both-input open can keep "
        "{W,S,C} and raise Φ; F-act can move the core to {W,C,F}"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(RESULTS, "pairs.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(pairs[0].keys()))
        w.writeheader()
        w.writerows(pairs)

    if h1 and h2 and h3 and ctrl_ok:
        verdict_s = "OPEN_ACT_CUT"
    elif h1 and h3:
        verdict_s = "OPEN_FLIPS"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and h2 and h3

    print()
    print("STATUS")
    print(f"  H1 structure/core flip: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 Φ-only invariant:    {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 act required:        {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #35 gig substitution (alt #36 ejection order)")
    print()
    print(
        f"verdict: {verdict_s} — opening the commit *rule* to the parties is "
        f"not the same as channel transparency (#24): publish-unread is "
        f"theater (F out, party core unchanged); parties acting on the opened "
        f"rule can flip core membership (e.g. to {{W,C,F}}); both-input open "
        f"can keep {{W,S,C}} and raise Φ only — encoding of how the rule is "
        f"opened decides, COMMIT_READ bridge only"
    )
    print(
        "reading: OPEN_ACT_CUT — algorithmic transparency of the rule changes "
        "the structural verdict when parties act on the opened function; "
        "mere publication does not; Φ-only and core-flip regimes both exist; "
        "#29–#33 pointers only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
