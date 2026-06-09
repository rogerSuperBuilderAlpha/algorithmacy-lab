"""Probe Q74 (H1-H4) — whole-system verdict vs the maximal complex, by excluded-element coupling.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q74_verdict_vs_complex.probe_verdict_vs_complex
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.questions.q74_verdict_vs_complex.forms import FORMS, SPECTATOR_FORMS


def coupling_class(cm, x_idx, core_idx):
    reads_core = any(cm[c, x_idx] for c in core_idx)   # some core element feeds x (x reads it)
    fed_to_core = any(cm[x_idx, c] for c in core_idx)   # x feeds some core element
    if reads_core and fed_to_core:
        return "bidirectional"
    if reads_core:
        return "read-only"
    if fed_to_core:
        return "emit-only"
    return "uncoupled"


def main():
    print("PROBE Q74 (H1-H4) — whole-system verdict vs maximal complex")
    print("=" * 78)
    rows, data = [], {}
    for name, rules, labels in FORMS:
        v = verdict(rules, labels)
        core, cphi = major_complex(rules, labels)
        cm = cm_from_rules(rules)
        core_idx = [labels.index(l) for l in (core or ())]
        excluded = [l for l in labels if l not in (core or ())]
        excl_classes = {l: coupling_class(cm, labels.index(l), core_idx) for l in excluded}
        any_bidir = any(c == "bidirectional" for c in excl_classes.values())
        data[name] = dict(whole=v.structure, wphi=v.max_phi, core=core, cphi=cphi,
                          excluded=excl_classes, any_bidir=any_bidir)
        print(f"  {name:<11} whole={v.structure:<8}Φ={v.max_phi:.3f} | core={core} Φ={cphi:.3f} | "
              f"excluded={excl_classes}")
        rows.append((name, v.structure, f"{v.max_phi:.4f}", "|".join(core or ()), f"{cphi:.4f}",
                     ";".join(f"{k}:{v2}" for k, v2 in excl_classes.items())))

    spec = [data[n] for n in SPECTATOR_FORMS]
    h1 = all(d["whole"] == "dyadic" and d["cphi"] > 1e-9 for d in spec)
    h2 = all(all(c != "bidirectional" for c in d["excluded"].values()) for d in spec)
    ch = data["chain"]
    h3 = ch["whole"] == "triadic" and len(ch["core"] or ()) < 4 and ch["any_bidir"]
    h4 = all(d["any_bidir"] == (d["whole"] == "triadic") for d in data.values())
    print("=" * 78)
    print(f"  H1 spectator forms whole-dyadic, core-triadic: {h1}")
    print(f"  H2 excluded elements non-bidirectional in those: {h2}")
    print(f"  H3 chain whole-triadic, proper subset, excluded bidirectional: {h3}")
    print(f"  H4 excluded bidirectional iff whole-system triadic: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "verdict_vs_complex.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "whole", "whole_phi", "core", "core_phi", "excluded_coupling"]); w.writerows(rows)


if __name__ == "__main__":
    main()
