"""Mixed-algebra seats on one mediator (RESEARCH_AGENDA_V3 #3).

One conjunctive seat + one parity seat feeding a single S — hybrid
signature, or does the V2 #4 parity blind-spot dominate the whole form?
Exact IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/mixed_algebra_seats/analyze_mixed_seats.py
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

from org_frontier.classifier.classifier import PHI_EPS
from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

PARITY_BAND = 0.5 + 1e-6
CONJ_LANDMARKS = (2.0, 3.0, 4.0)


def near(a, b, eps=None):
    if eps is None:
        eps = max(PHI_EPS, 1e-6)
    return abs(float(a) - float(b)) <= eps


def in_parity_band(phi):
    return float(phi) <= PARITY_BAND + max(PHI_EPS, 1e-6)


def is_conj_landmark(phi):
    return any(near(phi, c) for c in CONJ_LANDMARKS)


def and_triad():
    labels = ("W", "S", "C")
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    return labels, rules, {"family": "control", "arch": "and_triad", "role": "anchor"}


def xor_triad():
    labels = ("W", "S", "C")
    rules = [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]]
    return labels, rules, {"family": "control", "arch": "xor_triad", "role": "anchor"}


def _shared(s_rule, arch, role):
    labels = ("W1", "C1", "W2", "C2", "S")
    rules = [
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        lambda x: x[4],
        s_rule,
    ]
    return labels, rules, {"family": "shared", "arch": arch, "role": role}


def shared_aa():
    return _shared(
        lambda x: (x[0] & x[1]) & (x[2] & x[3]),
        "shared_AA",
        "pure_conj",
    )


def shared_xx_or():
    return _shared(
        lambda x: (x[0] ^ x[1]) | (x[2] ^ x[3]),
        "shared_XX_or",
        "pure_parity",
    )


def mix_and():
    return _shared(
        lambda x: (x[0] & x[1]) & (x[2] ^ x[3]),
        "mix_AND",
        "mixed",
    )


def mix_or():
    return _shared(
        lambda x: (x[0] & x[1]) | (x[2] ^ x[3]),
        "mix_OR",
        "mixed",
    )


def mix_xor():
    return _shared(
        lambda x: (x[0] & x[1]) ^ (x[2] ^ x[3]),
        "mix_XOR",
        "mixed",
    )


def mix_and_xnor():
    return _shared(
        lambda x: (x[0] & x[1]) & (1 ^ (x[2] ^ x[3])),
        "mix_AND_XNOR",
        "mixed",
    )


FORMS = [
    and_triad,
    xor_triad,
    shared_aa,
    shared_xx_or,
    mix_and,
    mix_or,
    mix_xor,
    mix_and_xnor,
]


def seat_tags(core, labels):
    """Which seats appear in the major complex."""
    if not core:
        return ""
    s = set(core)
    has_and = bool(s & {"W1", "C1"})
    has_xor = bool(s & {"W2", "C2"})
    has_s = "S" in s or "S" in labels and "S" in s
    parts = []
    if has_and:
        parts.append("conj_seat")
    if has_xor:
        parts.append("parity_seat")
    if "S" in s:
        parts.append("S")
    # triad anchors
    if s >= {"W", "S", "C"} or s >= {"W", "C", "S"}:
        return "full_triad"
    return "+".join(parts) if parts else "other"


def classify_whole(structure, whole_phi):
    if is_conj_landmark(whole_phi) and structure == "triadic":
        return "conj_landmark"
    if in_parity_band(whole_phi) and structure == "triadic":
        return "parity_band"
    if structure == "dyadic" or whole_phi <= PHI_EPS:
        return "factors"
    if structure == "triadic" and whole_phi > PARITY_BAND and not is_conj_landmark(whole_phi):
        return "hybrid_candidate"
    return "other"


def run_cell(builder):
    labels, rules, meta = builder()
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core_t = tuple(core) if core else ()
    cp = float(core_phi) if core_phi is not None and core_phi >= 0 else float("nan")
    kind = classify_whole(v.structure, float(v.max_phi))
    seats = seat_tags(core_t, labels)
    # hybrid: hybrid_candidate OR (full core both seats + novel phi)
    both = "conj_seat" in seats and "parity_seat" in seats
    novel = (
        v.structure == "triadic"
        and both
        and len(core_t) == len(labels)
        and not in_parity_band(v.max_phi)
        and not is_conj_landmark(v.max_phi)
    )
    is_hybrid = kind == "hybrid_candidate" or novel
    return {
        **meta,
        "name": meta["arch"],
        "n": len(labels),
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "|".join(core_t) if core_t else "",
        "core_phi": cp,
        "n_core": len(core_t),
        "seats": seats,
        "kind": kind,
        "hybrid": int(is_hybrid),
        "seconds": round(time.time() - t0, 2),
    }


def fmt(row):
    return (
        f"{row['name']:14s} {row['structure']:8s} "
        f"whole\u03a6={row['whole_phi']:.3f}  "
        f"core=({row['core']})  core\u03a6={row['core_phi']:.3f}  "
        f"seats={row['seats'] or '-':20s}  kind={row['kind']:16s}  "
        f"hybrid={bool(row['hybrid'])}  t={row['seconds']:.1f}s"
    )


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = [run_cell(b) for b in FORMS]

    path = os.path.join(RESULTS, "panel.csv")
    fields = [
        "family",
        "arch",
        "name",
        "n",
        "role",
        "structure",
        "whole_phi",
        "core",
        "core_phi",
        "n_core",
        "seats",
        "kind",
        "hybrid",
        "seconds",
    ]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print("MIXED-ALGEBRA SEATS — V3 #3")
    print("hypotheses fixed in hypotheses.md before this run")
    for r in rows:
        print(fmt(r))

    by = {r["name"]: r for r in rows}

    # H1
    a, x = by["and_triad"], by["xor_triad"]
    h1 = (
        a["structure"] == "triadic"
        and near(a["whole_phi"], 2.0)
        and x["structure"] == "triadic"
        and near(x["whole_phi"], 0.5)
    )
    print(f"H1 (AND \u03a6=2 + XOR \u03a6=0.5 anchors):           {'SUPPORTED' if h1 else 'REFUTED'}")

    # H2
    aa, xx = by["shared_AA"], by["shared_XX_or"]
    h2 = (
        aa["kind"] == "conj_landmark"
        and near(aa["whole_phi"], 4.0)
        and aa["n_core"] == aa["n"]
        and in_parity_band(xx["whole_phi"])
        and xx["structure"] == "triadic"
    )
    print(f"H2 (pure shared AND \u03a6=4 + XOR band):        {'SUPPORTED' if h2 else 'REFUTED'}")
    print(
        f"  shared_AA kind={aa['kind']} \u03a6={aa['whole_phi']:.3f}  "
        f"shared_XX_or kind={xx['kind']} \u03a6={xx['whole_phi']:.3f}"
    )

    # H3
    mixed = [r for r in rows if r["role"] == "mixed"]
    no_conj_whole = all(not is_conj_landmark(r["whole_phi"]) for r in mixed)
    all_band_or_factor = all(
        r["kind"] in ("parity_band", "factors", "other")
        and not is_conj_landmark(r["whole_phi"])
        for r in mixed
    )
    # allow other only if still ≤0.5 or factors
    all_band_or_factor = all(
        (in_parity_band(r["whole_phi"]) or r["structure"] == "dyadic" or r["whole_phi"] <= PHI_EPS)
        and not is_conj_landmark(r["whole_phi"])
        for r in mixed
    )
    h3 = no_conj_whole and all_band_or_factor and len(mixed) >= 3
    print(f"H3 (mixed: no conjunctive whole landmark):   {'SUPPORTED' if h3 else 'REFUTED'}")
    for r in mixed:
        print(
            f"  {r['name']}: whole\u03a6={r['whole_phi']:.3f} kind={r['kind']} "
            f"seats={r['seats']} hybrid={bool(r['hybrid'])}"
        )

    hybrids = [r for r in mixed if r["hybrid"]]
    if not h1 or not h2:
        token = "CONTROLS_FAIL"
    elif hybrids:
        token = "HYBRID_SIGNATURE"
    elif h3:
        token = "BLINDSPOT_DOMINATES"
    else:
        token = "MIXED_UNCLEAR"

    h4 = token == "BLINDSPOT_DOMINATES"
    print(f"H4 (panel closed):                           {'SUPPORTED' if h4 else 'REFUTED'}")
    print(f"verdict: {token}")
    if token == "BLINDSPOT_DOMINATES":
        print(
            "reading: BLINDSPOT_DOMINATES \u2014 mixed conjunctive+parity seats on one "
            "mediator never restore a conjunctive whole-form \u03a6; the form stays in "
            "the parity blind-spot band or factors (V2 #4 pattern dominates; no hybrid)"
        )
    else:
        print(f"reading: {token}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
