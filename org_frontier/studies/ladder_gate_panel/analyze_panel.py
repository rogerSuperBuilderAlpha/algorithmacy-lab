"""Stratified panel stress-test of MONO_EXTREMAL_VS_AFFINE.

4-input Boolean gates; n=5 full joint bind; exact IIT-4.0 Φ.
Hypotheses fixed in hypotheses.md.

Run:  python org_frontier/studies/ladder_gate_panel/analyze_panel.py
"""

from __future__ import annotations

import csv
import os
import random
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

L = ("W1", "S", "W2", "W3", "C")
N = len(L)
N_MINUS_1 = N - 1
WT_EXTREMAL = {1, 15}
SEED = 20260916
N_RANDOM = 64


def _eval(mask: int, a: int, b: int, c: int, d: int) -> int:
    idx = (a << 3) | (b << 2) | (c << 1) | d
    return (mask >> idx) & 1


def _props(mask: int) -> dict:
    wt = bin(mask).count("1")
    dep = []
    for i in range(4):
        differs = False
        for x in range(16):
            bits = [(x >> 3) & 1, (x >> 2) & 1, (x >> 1) & 1, x & 1]
            b2 = bits[:]
            b2[i] = 1 - b2[i]
            if _eval(mask, *bits) != _eval(mask, *b2):
                differs = True
                break
        dep.append(differs)
    mono_inc = mono_dec = True
    for x in range(16):
        for i in range(4):
            bitpos = 3 - i
            if (x >> bitpos) & 1:
                continue
            y = x | (1 << bitpos)
            fx = _eval(mask, (x >> 3) & 1, (x >> 2) & 1, (x >> 1) & 1, x & 1)
            fy = _eval(mask, (y >> 3) & 1, (y >> 2) & 1, (y >> 1) & 1, y & 1)
            if fy < fx:
                mono_inc = False
            if fy > fx:
                mono_dec = False
    monotone = mono_inc or mono_dec
    fz = _eval(mask, 0, 0, 0, 0)
    affine = True
    for x in range(16):
        xb = ((x >> 3) & 1, (x >> 2) & 1, (x >> 1) & 1, x & 1)
        for y in range(16):
            yb = ((y >> 3) & 1, (y >> 2) & 1, (y >> 1) & 1, y & 1)
            zb = tuple(xb[i] ^ yb[i] for i in range(4))
            if (
                _eval(mask, *xb)
                ^ _eval(mask, *yb)
                ^ fz
                ^ _eval(mask, *zb)
            ):
                affine = False
                break
        if not affine:
            break
    all_dep = all(dep)
    extremal_wt = wt in WT_EXTREMAL
    return {
        "wt": wt,
        "all_dep": all_dep,
        "monotone": monotone,
        "affine": affine,
        "extremal_wt": extremal_wt,
    }


def _predict(p: dict) -> str:
    if p["all_dep"] and p["affine"]:
        return "B"
    if p["all_dep"] and p["monotone"] and p["extremal_wt"]:
        return "A"
    return "C"


def _observed(structure: str, n_core: int, core_phi: float) -> str:
    """A/B require full 5-core triadic flip; else C (incl. partial triadic)."""
    flip = structure == "triadic" and n_core == N
    if flip and abs(core_phi - N_MINUS_1) < PHI_EPS:
        return "A"
    if flip and core_phi < 1.0 - PHI_EPS:
        return "B"
    if flip:
        return "?"  # full flip, unexpected Φ
    return "C"


def _build_panel():
    """Stratified masks with stratum tags."""
    print("  enumerating strata over 2^16 gates…")
    mono, aff, ext = [], [], []
    apred, bpred = [], []
    for m in range(65536):
        p = _props(m)
        if p["monotone"]:
            mono.append(m)
        if p["affine"]:
            aff.append(m)
        if p["extremal_wt"]:
            ext.append(m)
        if p["all_dep"] and p["monotone"] and p["extremal_wt"]:
            apred.append(m)
        if p["all_dep"] and p["affine"]:
            bpred.append(m)

    covered = set(mono) | set(aff) | set(ext)
    residual = [m for m in range(65536) if m not in covered]
    rng = random.Random(SEED)
    rand_sample = rng.sample(residual, min(N_RANDOM, len(residual)))

    # stratum priority for labeling (first match wins in display)
    entries = []  # (mask, stratum)
    seen = set()

    def add_all(masks, stratum):
        for m in masks:
            if m not in seen:
                seen.add(m)
                entries.append((m, stratum))

    add_all(apred, "A_pred")
    add_all(bpred, "B_pred")
    add_all(mono, "monotone")
    add_all(ext, "extremal_wt")
    add_all(aff, "affine")
    add_all(rand_sample, "random")

    print(
        f"  strata: A_pred={len(apred)} B_pred={len(bpred)} "
        f"monotone={len(mono)} extremal_wt={len(ext)} affine={len(aff)} "
        f"random={len(rand_sample)}  panel={len(entries)}"
    )
    return entries


def main():
    print("LADDER-GATE STRATIFIED PANEL — stress-test MONO_EXTREMAL_VS_AFFINE")
    print("=" * 80)
    print("  cited: ladder_gate_properties MONO_EXTREMAL_VS_AFFINE")
    print("  hypotheses fixed in hypotheses.md before computing")
    print(f"  labels: {L}  seed={SEED}  n_random={N_RANDOM}")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = verdict(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("PANEL")
    print("-" * 80)
    panel = _build_panel()
    rows = []
    t_all = time.time()
    mismatches = []
    ambiguous = []
    confusion = {(a, b): 0 for a in "ABC?" for b in "ABC?"}

    for i, (mask, stratum) in enumerate(panel, 1):
        p = _props(mask)
        pred = _predict(p)
        sfn = lambda x, m=mask: _eval(m, x[0], x[2], x[3], x[4])
        rules = [
            lambda x: x[1],
            sfn,
            lambda x: x[1],
            lambda x: x[1],
            lambda x: x[1],
        ]
        t0 = time.time()
        v = verdict(list(rules), L)
        core, cphi = major_complex(list(rules), L)
        core_t = tuple(core) if core else ()
        cphi_f = float(cphi) if cphi is not None and cphi >= 0 else float("nan")
        obs = _observed(
            v.structure,
            len(core_t),
            cphi_f if cphi_f == cphi_f else -1.0,
        )
        match = int(pred == obs)
        confusion[(pred, obs)] = confusion.get((pred, obs), 0) + 1
        row = {
            "mask": f"{mask:04x}",
            "mask_int": mask,
            "stratum": stratum,
            "wt": p["wt"],
            "all_dep": int(p["all_dep"]),
            "monotone": int(p["monotone"]),
            "affine": int(p["affine"]),
            "extremal_wt": int(p["extremal_wt"]),
            "pred": pred,
            "obs": obs,
            "match": match,
            "structure": v.structure,
            "whole_phi": float(v.max_phi),
            "core": "|".join(core_t),
            "core_phi": cphi_f,
            "n_core": len(core_t),
            "elapsed_s": round(time.time() - t0, 2),
        }
        rows.append(row)
        if not match:
            mismatches.append(row)
        if obs == "?":
            ambiguous.append(row)
        if i % 50 == 0 or i == len(panel) or not match or obs == "?":
            mark = "✓" if match else "✗"
            print(
                f"  [{i}/{len(panel)}] mask={mask:04x} {stratum:<12} "
                f"pred={pred} obs={obs} {mark}  "
                f"Φ={cphi_f if cphi_f == cphi_f else float('nan'):.3f}  "
                f"n_core={len(core_t)}  t={row['elapsed_s']}s"
            )

    n = len(rows)
    n_match = sum(r["match"] for r in rows)
    acc = n_match / n if n else 0.0

    # Per-stratum accuracy
    strata = sorted({r["stratum"] for r in rows})
    print()
    print("STRATUM ACCURACY")
    print("-" * 80)
    for s in strata:
        sub = [r for r in rows if r["stratum"] == s]
        sm = sum(r["match"] for r in sub)
        print(f"  {s:<14} {sm}/{len(sub)}")

    print()
    print("CONFUSION (pred → obs)")
    print("-" * 80)
    for pred in "AB":
        for obs in "ABC?":
            c = confusion.get((pred, obs), 0)
            if c:
                print(f"  {pred}→{obs}: {c}")
    for obs in "ABC?":
        c = confusion.get(("C", obs), 0)
        if c:
            print(f"  C→{obs}: {c}")

    h1 = ctrl and n_match == n and not ambiguous
    h2 = ctrl and n_match < n
    h3 = ctrl and (bool(ambiguous) or (n_match < n))

    if h1 and not h2:
        verdict_word = "RULE_HOLDS_PANEL"
        reading = (
            f"RULE_HOLDS_PANEL — MONO_EXTREMAL_VS_AFFINE accuracy "
            f"{n_match}/{n} on stratified panel; no counterexamples; "
            f"no ambiguous Φ"
        )
    elif h2 and not ambiguous:
        verdict_word = "COUNTEREXAMPLES"
        ce = "/".join(r["mask"] for r in mismatches[:8])
        reading = (
            f"COUNTEREXAMPLES — accuracy {n_match}/{n}; "
            f"mismatches include {ce}"
        )
    elif ambiguous:
        verdict_word = "NEEDS_REFINEMENT"
        reading = (
            f"NEEDS_REFINEMENT — {len(ambiguous)} ambiguous full-flip Φ; "
            f"accuracy {n_match}/{n}"
        )
    else:
        verdict_word = "PARTIAL"
        reading = f"PARTIAL — accuracy {n_match}/{n}"

    print()
    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  H1 (rule holds on panel):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (counterexamples appear):  "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (refinement needed):       "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    if mismatches:
        print("  mismatches:")
        for r in mismatches[:12]:
            print(
                f"    mask={r['mask']} pred={r['pred']} obs={r['obs']} "
                f"stratum={r['stratum']} Φ={r['core_phi']} "
                f"n_core={r['n_core']} mono={r['monotone']} "
                f"aff={r['affine']} wt={r['wt']}"
            )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  accuracy: {n_match}/{n}")
    print(f"  panel_size: {n}")
    print(f"  n_mismatch: {len(mismatches)}")
    print(f"  n_ambiguous: {len(ambiguous)}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "census.csv"), "w", newline="") as fh:
        fields = list(rows[0].keys())
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = dict(r)
            out["whole_phi"] = f"{r['whole_phi']:.6f}"
            out["core_phi"] = f"{r['core_phi']:.6f}"
            w.writerow(out)
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "accuracy": f"{n_match}/{n}",
            "panel_size": n,
            "n_mismatch": len(mismatches),
            "n_ambiguous": len(ambiguous),
            "reading": reading,
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
