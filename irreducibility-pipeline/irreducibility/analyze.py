"""Analyze a coordinative structure: encodings in, an exact irreducibility analysis out.

    python -m irreducibility.analyze examples/01_gig_dispatch/encodings.json
    python -m irreducibility.analyze my_structure.json --json out.json

For each encoding the report gives:
  * the TPM and connectivity matrix PyPhi receives;
  * Φ over the minimum-information partition in every reachable state, and the MIP at the
    most-integrated state;
  * the verdict (dyadic or triadic) and the major complex (who is bound);
  * the mediator's position (BOTTLENECK, ENRICHER, CAPTURE, BYPASSED);
  * whether the mediator's place is intrinsic or contingent on a forbidden bypass, if one is given;
  * whether the prediction fixed before computing held.

Across rival encodings of the same parties it reports the spread (verdict agreement, Φ gap, core
overlap) and the single rules whose swap flips the verdict, i.e. the facts the evidence must
settle. The script refuses to run if the instrument controls fail or the encodings file is
inadmissible.
"""

import argparse
import json
import sys

from .core import tpm_from_rules, cm_from_rules, classify_rules, major_complex, PHI_EPS
from .contingency import contingency_test
from .encoding import load, validate, labels_of
from .regime import regime
from .rules import compile_rules
from .spread import spread
from .validate import controls_pass


def _fmt_state(state, labels):
    return "".join(str(b) for b in state) + " (" + ",".join(f"{l}={b}" for l, b in zip(labels, state)) + ")"


def analyze_encoding(doc, enc):
    labels = labels_of(doc, enc)
    rules = compile_rules(enc["rules"], labels)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    v = classify_rules(rules, labels)
    core, core_phi = major_complex(rules, labels)
    out = {
        "id": enc["id"],
        "account": enc.get("account", ""),
        "role": enc.get("role", "rival"),
        "labels": list(labels),
        "rules": {p: enc["rules"][p] for p in labels},
        "tpm_shape": list(tpm.shape),
        "cm": cm.tolist(),
        "phi_profile": [{"state": "".join(map(str, s)), "phi": round(p, 6)} for s, p in v.phi_profile],
        "structure": v.structure,
        "max_phi": round(v.max_phi, 6),
        "mip_state": "".join(map(str, v.mip_state)) if v.mip_state else None,
        "mip_partition": v.mip_partition,
        "irreducible_states": f"{v.n_states_irreducible}/{v.n_states_evaluated}",
        "core": list(core) if core else [],
        "core_phi": round(core_phi, 6) if core else 0.0,
    }
    med = doc.get("mediator")
    if med and med in labels:
        out["regime"] = regime(rules, labels, med)
    bp = enc.get("bypass")
    if bp:
        c = contingency_test(rules, labels, bp["party"], downstream=bp["downstream"],
                             upstream=bp["upstream"], mode=bp.get("mode", "replace"))
        out["contingency"] = {"party": c.party, "kind": c.kind, "margin": round(c.margin, 6),
                              "core_constrained": list(c.core_constrained),
                              "core_bypass": list(c.core_bypass)}
    pred = enc.get("predicted", {})
    out["predicted"] = pred
    ok = pred.get("structure") == v.structure
    if ok and pred.get("core"):
        ok = set(pred["core"]) == set(out["core"])
    out["prediction_held"] = ok
    return out, rules


def flip_rules(doc, encA, encB):
    """Parties whose single-rule swap from A to B flips A's verdict to B's."""
    labels = labels_of(doc, encA)
    vA = classify_rules(compile_rules(encA["rules"], labels), labels).structure
    vB = classify_rules(compile_rules(encB["rules"], labels), labels).structure
    if vA == vB:
        return []
    flips = []
    for p in labels:
        if encA["rules"][p].replace(" ", "") == encB["rules"][p].replace(" ", ""):
            continue
        swapped = dict(encA["rules"])
        swapped[p] = encB["rules"][p]
        if classify_rules(compile_rules(swapped, labels), labels).structure == vB:
            flips.append(f"{p}: {encA['rules'][p]!r} -> {encB['rules'][p]!r}")
    return flips


def analyze(doc):
    results, compiled = [], {}
    for enc in doc["encodings"]:
        r, rules = analyze_encoding(doc, enc)
        results.append(r)
        compiled[enc["id"]] = (tuple(r["labels"]), rules, enc)
    rivals = [e for e in doc["encodings"] if e.get("role", "rival") == "rival"]
    pairs = []
    for i, a in enumerate(rivals):
        for b in rivals[i + 1:]:
            la, ra, _ = compiled[a["id"]]
            lb, rb, _ = compiled[b["id"]]
            if la != lb:
                continue
            s = spread(ra, rb, la)
            pairs.append({"pair": [a["id"], b["id"]],
                          "verdict_agreement": s["verdict_agreement"],
                          "phi_gap": round(s["phi_gap"], 6),
                          "core_jaccard": round(s["core_jaccard"], 6),
                          "verdicts": list(s["both_verdicts"]),
                          "rules_that_flip_the_verdict": flip_rules(doc, a, b)})
    rival_verdicts = {r["structure"] for r in results if r["role"] == "rival"}
    held = sum(r["prediction_held"] for r in results)
    if not rival_verdicts:
        robust = (f"DESIGN COMPARISON: {len(results)} designs; predictions fixed before computing "
                  f"held in {held}/{len(results)}")
    elif len(rival_verdicts) == 1:
        robust = f"ROBUST: every rival encoding reads {rival_verdicts.pop()}"
    else:
        robust = "CONTESTED: the verdict depends on which encoding the evidence supports"
    return {"structure": doc["structure"], "encodings": results, "spread": pairs, "summary": robust}


def print_report(rep, doc):
    W = 92
    print("=" * W)
    print(f"IRREDUCIBILITY ANALYSIS - {rep['structure']}")
    print("=" * W)
    for r in rep["encodings"]:
        print(f"\n[{r['id']}] {r['account']}  ({r['role']})")
        for p in r["labels"]:
            print(f"    {p}' = {r['rules'][p]}")
        print(f"  PyPhi input: TPM {r['tpm_shape'][0]}x{r['tpm_shape'][1]} (state-by-node), "
              f"connectivity {r['cm']}")
        prof = ", ".join(f"{d['state']}:{d['phi']:.3f}" for d in r["phi_profile"])
        print(f"  Φ_MIP by reachable state: {prof}")
        print(f"  verdict: {r['structure'].upper()}  max Φ_MIP = {r['max_phi']:.3f}"
              f"  ({r['irreducible_states']} states irreducible)")
        if r["mip_state"]:
            print(f"  MIP at state {r['mip_state']}: {r['mip_partition']}")
        print(f"  major complex (who is bound): {{{', '.join(r['core'])}}}" if r["core"]
              else "  major complex: none")
        if "regime" in r:
            print(f"  mediator ({doc['mediator']}) position: {r['regime']}")
        if "contingency" in r:
            c = r["contingency"]
            print(f"  bypass test on {c['party']}: {c['kind']} (Φ lost when the bypass opens: "
                  f"{c['margin']:.3f}; core {{{','.join(c['core_constrained'])}}} -> "
                  f"{{{','.join(c['core_bypass'])}}})")
        pred = r["predicted"]
        print(f"  predicted before computing: {pred.get('structure')}"
              + (f", core {{{','.join(pred['core'])}}}" if pred.get("core") else "")
              + f"  -> {'HELD' if r['prediction_held'] else 'FAILED'}")
    if rep["spread"]:
        print("\n" + "-" * W)
        print("SPREAD ACROSS RIVAL ENCODINGS")
        for s in rep["spread"]:
            print(f"  {s['pair'][0]} vs {s['pair'][1]}: verdicts {s['verdicts'][0]}/{s['verdicts'][1]}, "
                  f"Φ gap {s['phi_gap']:.3f}, core overlap {s['core_jaccard']:.3f}")
            for f in s["rules_that_flip_the_verdict"]:
                print(f"      single rule that flips it: {f}")
    print("\n" + "=" * W)
    print(f"  {rep['summary']}")
    print("=" * W)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("encodings", help="path to an encodings JSON file")
    ap.add_argument("--json", help="also write the full report as JSON to this path")
    args = ap.parse_args(argv)

    if not controls_pass():
        print("INSTRUMENT CONTROLS FAILED - refusing to analyze. Run python -m irreducibility.validate")
        return 1
    doc = load(args.encodings)
    problems = validate(doc)
    if problems:
        print("ENCODINGS FILE IS NOT ADMISSIBLE:")
        for p in problems:
            print("  - " + p)
        return 2
    rep = analyze(doc)
    print_report(rep, doc)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(rep, f, indent=2, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
