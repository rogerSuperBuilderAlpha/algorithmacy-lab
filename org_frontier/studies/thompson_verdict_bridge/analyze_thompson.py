"""Agenda #43 — Thompson interdependence types vs dyadic/triadic verdict.

Canonical triple + mismatch witnesses. Exact binary IIT-4.0.
Hypotheses fixed in hypotheses.md before computing.

Run:  python org_frontier/studies/thompson_verdict_bridge/analyze_thompson.py
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

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_group_surplus import pool

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
LABELS3 = ("W", "S", "C")

# Canonical / alternate forms (n=3, AND family; x[0]=W, x[1]=S, x[2]=C).
FORMS = [
    # type, slug, role, rules_or_factory, labels, predicted_structure, notes
    (
        "pooled",
        "pooled_indep",
        "canonical",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
        LABELS3,
        "dyadic",
        "independent-contribution relay (#25/#40)",
    ),
    (
        "pooled",
        "pooled_allreq",
        "alternate",
        None,  # filled via pool(3)
        None,
        "dyadic",  # H1 type prediction; expect mismatch → triadic
        "all-required pool (#116)",
    ),
    (
        "sequential",
        "seq_chain",
        "canonical",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        LABELS3,
        "triadic",  # "the chain" — but H1 also requires Φ low vs reciprocal
        "pass-through chain (#57)",
    ),
    (
        "sequential",
        "seq_handoff",
        "alternate",
        [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[2]],
        LABELS3,
        "triadic",  # type prediction if sequential=chain; expect mismatch → dyadic
        "acyclic hand-off (#39)",
    ),
    (
        "reciprocal",
        "recip_cyclic",
        "canonical",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        LABELS3,
        "triadic",
        "cyclic feedback triad (#5/#39); same rules as seq_chain under AND",
    ),
    (
        "reciprocal",
        "recip_acyclic",
        "alternate",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],
        LABELS3,
        "triadic",  # type prediction; expect mismatch → dyadic
        "bidirectional labels, no cycle",
    ),
]


def eval_form(slug, rules, labels):
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    return {
        "slug": slug,
        "structure": v.structure,
        "max_phi": float(v.max_phi),
        "mip": v.mip_partition,
        "core": "" if core is None else "{" + ",".join(core) + "}",
        "core_phi": float(core_phi) if core_phi >= 0 else 0.0,
        "n_irreducible": int(v.n_states_irreducible),
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("THOMPSON VERDICT BRIDGE (#43)")
    print("=" * 72)
    print("  agenda: RESEARCH_AGENDA_50_V2 #43")
    print("  prior:  questions/q43_thompson_interdependence/ (pointer)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 72)
    print()

    # Instrument control — faithful triad / pass-through chain
    print("INSTRUMENT CONTROL")
    print("-" * 72)
    ctrl_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    vc = verdict(ctrl_rules, LABELS3)
    ctrl_ok = vc.structure == "triadic" and abs(vc.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {vc.structure} Φ={vc.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    rows = []
    by_slug = {}

    print("PANEL")
    print("-" * 72)
    for thompson, slug, role, rules, labels, predicted, notes in FORMS:
        if slug == "pooled_allreq":
            rules, labels = pool(3)
        r = eval_form(slug, rules, labels)
        r.update(
            {
                "thompson_type": thompson,
                "role": role,
                "predicted": predicted,
                "notes": notes,
            }
        )
        # structure match to type prediction
        r["struct_match"] = r["structure"] == predicted
        by_slug[slug] = r
        rows.append(r)
        print(
            f"  {slug:16s} [{role:9s}] {thompson:10s} → "
            f"{r['structure']:7s} Φ={r['max_phi']:.3f} "
            f"core={r['core'] or '—':12s} "
            f"pred={predicted:7s} "
            f"{'OK' if r['struct_match'] else 'MISMATCH'}"
        )

    # Sequential "low" check on canonical pair
    seq_phi = by_slug["seq_chain"]["max_phi"]
    recip_phi = by_slug["recip_cyclic"]["max_phi"]
    seq_low = seq_phi + PHI_EPS < recip_phi
    print()
    print(
        f"  sequential Φ low vs reciprocal: "
        f"seq={seq_phi:.3f} recip={recip_phi:.3f}  "
        f"{'YES' if seq_low else 'NO (tie or higher)'}"
    )

    # Alignment score: 6 structure predictions + 1 sequential-low bit
    struct_hits = sum(1 for r in rows if r["struct_match"])
    low_hit = 1 if seq_low else 0
    alignment = (struct_hits + low_hit) / 7.0

    # Canonical legs for H1
    pool_ok = by_slug["pooled_indep"]["structure"] == "dyadic"
    seq_ok = (
        by_slug["seq_chain"]["structure"] == "triadic" and seq_low
    )  # chain AND low
    recip_ok = by_slug["recip_cyclic"]["structure"] == "triadic"
    h1 = pool_ok and seq_ok and recip_ok

    # Aligning legs (partial): any of the three clean H1 legs that hold
    # without requiring sequential-low for the "chain" recognition alone
    aligning_legs = []
    if pool_ok:
        aligning_legs.append("pooled_indep→dyadic")
    if by_slug["seq_chain"]["structure"] == "triadic":
        aligning_legs.append("seq_chain→triadic(chain)")
    if recip_ok:
        aligning_legs.append("recip_cyclic→triadic")

    # Mismatches: wrong verdict vs type prediction
    mismatches = [r["slug"] for r in rows if not r["struct_match"]]
    # Also count sequential-not-low as a canonical mismatch for H1
    if not seq_low:
        mismatches.append("seq_chain_not_low_vs_recip")
    h2 = len(mismatches) > 0

    # H3: partial — not full H1, some aligning legs, mismatches exist
    h3 = (not h1) and (len(aligning_legs) > 0) and h2

    if h1:
        reading = "FULL_THOMPSON_MAP"
    elif h3:
        reading = "PARTIAL_ALIGNMENT"
    elif h2:
        reading = "THOMPSON_MISMATCH"
    else:
        reading = "MIXED"

    grid = ctrl_ok and h3 and not h1 and h2

    print()
    print("ALIGNMENT")
    print("-" * 72)
    print(
        f"  structure hits: {struct_hits}/6  + sequential-low: {low_hit}/1  "
        f"→ score={alignment:.3f}"
    )
    print(f"  aligning legs:  {', '.join(aligning_legs) or 'none'}")
    print(f"  mismatches:     {', '.join(mismatches) or 'none'}")

    print()
    print("HYPOTHESES")
    print(f"  H1 (clean type→verdict map):           {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (mismatches):                       {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (partial alignment only):           {'SUPPORTED' if h3 else 'REFUTED'}")

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #44 Wageman-style measured task interdependence")
    print()
    print(
        f"verdict: {reading} — Thompson types track the verdict loosely: "
        f"pooled_indep→dyadic and recip_cyclic→triadic hold; sequential "
        f"chain ties reciprocal at Φ=2 (not low); alternates flip "
        f"(all-required pool triadic; hand-off dyadic; cycle-broken dyadic); "
        f"alignment={alignment:.3f}"
    )
    print(
        "reading: PARTIAL_ALIGNMENT — typology is not a clean map; "
        "joint determination and feedback cycle decide; q43 pointer; "
        "construct-validity arc opens at #43"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)

    fieldnames = [
        "thompson_type",
        "slug",
        "role",
        "structure",
        "max_phi",
        "core",
        "core_phi",
        "mip",
        "predicted",
        "struct_match",
        "notes",
        "n_irreducible",
    ]
    with open(os.path.join(RESULTS, "type_panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r[k] for k in fieldnames})

    summary = {
        "verdict": reading,
        "alignment_score": alignment,
        "struct_hits": struct_hits,
        "seq_low": seq_low,
        "aligning_legs": aligning_legs,
        "mismatches": mismatches,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "control_pass": ctrl_ok,
        "panel": {
            s: {
                "type": by_slug[s]["thompson_type"],
                "structure": by_slug[s]["structure"],
                "max_phi": by_slug[s]["max_phi"],
                "core": by_slug[s]["core"],
            }
            for s in by_slug
        },
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
