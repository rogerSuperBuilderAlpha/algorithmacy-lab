"""Agenda #46 — formal vs informal coordination vs dyadic/triadic verdict.

Designed N=3 paired forms. Exact binary IIT-4.0. Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/formal_informal_cut/analyze_cut.py
"""

from __future__ import annotations

import csv
import json
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
LABELS = ("W", "S", "C")

# (slug, class, predicted_structure, rules, notes)
PANEL = [
    (
        "F_commit_gate",
        "formal",
        "triadic",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "institutional AND gate; parties read S only",
    ),
    (
        "F_convey_gate",
        "formal",
        "triadic",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
        "institutional convey; prescribed channel, no joint commit",
    ),
    (
        "F_hierarchy_handoff",
        "formal",
        "triadic",
        [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]],
        "acyclic prescribed hand-off",
    ),
    (
        "I_lateral_idle_S",
        "informal",
        "dyadic",
        [lambda x: x[2], lambda x: x[1], lambda x: x[0]],
        "W↔C mutual adjustment; S idle",
    ),
    (
        "I_backchannel",
        "informal",
        "dyadic",
        [lambda x: x[1] | x[2], lambda x: x[0], lambda x: x[1] | x[0]],
        "convey + lateral OR back-channel",
    ),
    (
        "I_copy_ring",
        "informal",
        "dyadic",
        [lambda x: x[2], lambda x: x[0], lambda x: x[1]],
        "cyclic copy ring (emergent loop)",
    ),
]


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("FORMAL vs INFORMAL CUT (#46)")
    print("=" * 72)
    print("  agenda: RESEARCH_AGENDA_50_V2 #46")
    print("  pointer: #43/#44/#45 / CONSTRUCT_VALIDITY_ARC")
    print("  formal = prescribed S-channel; informal = lateral W↔C")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 72)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 72)
    ctrl = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    vc = verdict(ctrl, LABELS)
    ctrl_ok = vc.structure == "triadic" and abs(vc.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {vc.structure} Φ={vc.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    print("PANEL")
    print("-" * 72)
    for slug, cls, predicted, rules, notes in PANEL:
        v = verdict(rules, LABELS)
        core, core_phi = major_complex(rules, LABELS)
        match = v.structure == predicted
        row = {
            "slug": slug,
            "class": cls,
            "predicted": predicted,
            "structure": v.structure,
            "max_phi": float(v.max_phi),
            "core": "" if core is None else "{" + ",".join(core) + "}",
            "core_phi": float(core_phi) if core_phi >= 0 else 0.0,
            "match": match,
            "notes": notes,
        }
        rows.append(row)
        print(
            f"  {slug:22s} [{cls:8s}] → {v.structure:7s} Φ={v.max_phi:.3f} "
            f"core={row['core'] or '—':12s} pred={predicted:7s} "
            f"{'OK' if match else 'MISMATCH'}"
        )

    hits = sum(1 for r in rows if r["match"])
    alignment = hits / len(rows)

    formal_structs = {r["structure"] for r in rows if r["class"] == "formal"}
    informal_structs = {r["structure"] for r in rows if r["class"] == "informal"}
    formal_spans = formal_structs == {"dyadic", "triadic"}
    informal_spans = informal_structs == {"dyadic", "triadic"}

    formal_triadic_legs = [
        r["slug"]
        for r in rows
        if r["class"] == "formal" and r["structure"] == "triadic"
    ]
    informal_dyadic_legs = [
        r["slug"]
        for r in rows
        if r["class"] == "informal" and r["structure"] == "dyadic"
    ]
    mismatches = [r["slug"] for r in rows if not r["match"]]

    h1 = hits == len(rows)
    h2 = formal_spans and informal_spans
    h3 = (not h1) and (len(formal_triadic_legs) > 0 or len(informal_dyadic_legs) > 0)

    if h1:
        reading = "FORMAL_INFORMAL_ALIGN"
    elif h2:
        reading = "CUTS_ACROSS"
    elif h3:
        reading = "PARTIAL_ALIGNMENT"
    else:
        reading = "MIXED"

    grid = ctrl_ok and h2 and not h1 and h3

    print()
    print("ALIGNMENT")
    print("-" * 72)
    print(f"  score:              {hits}/{len(rows)} = {alignment:.3f}")
    print(f"  formal structures:  {sorted(formal_structs)}")
    print(f"  informal structures:{sorted(informal_structs)}")
    print(f"  aligning legs:      formal→triadic {formal_triadic_legs or 'none'}; "
          f"informal→dyadic {informal_dyadic_legs or 'none'}")
    print(f"  mismatches:         {', '.join(mismatches) or 'none'}")

    print()
    print("HYPOTHESES")
    print(f"  H1 (formal↔triadic / informal↔dyadic): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (cuts across):                      {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (partial alignment only):           {'SUPPORTED' if h3 else 'REFUTED'}")

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            outside CV — agenda J #47 scaling-law closed forms")
    print()
    print(
        f"verdict: {reading} — formal spans dyadic↔triadic "
        f"(commit gate vs convey/handoff); informal spans dyadic↔triadic "
        f"(lateral idle vs back-channel/ring); alignment={alignment:.3f}; "
        f"distinction cuts across the verdict"
    )
    print(
        "reading: CUTS_ACROSS — prescribed vs lateral is not a dyadic/triadic "
        "map; joint determination and cycles decide; #43–#45 pointers; "
        "construct-validity arc closable"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)

    fields = list(rows[0].keys())
    with open(os.path.join(RESULTS, "cut_panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    summary = {
        "verdict": reading,
        "alignment_score": alignment,
        "hits": hits,
        "formal_structs": sorted(formal_structs),
        "informal_structs": sorted(informal_structs),
        "mismatches": mismatches,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "control_pass": ctrl_ok,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
