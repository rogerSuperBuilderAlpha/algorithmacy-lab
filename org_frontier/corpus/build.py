"""Build the labeled coordination-form corpus and the 'what toggles irreducibility' table.

Two artifacts, both written to results/:
  corpus.csv   — every form with exact IIT-4.0 Φ_MIP, the verdict, and structural tags.
  toggles.csv  — single-feature ablations on the triadic forms: which one structural change
                 flips Φ from > 0 to 0. This is the structure-first finding — irreducibility of
                 a small mediated system is decided by the reads, not by topology alone.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.build
"""

import csv
import os

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus import forms_library as lib

_HERE = os.path.dirname(__file__)
_RESULTS = os.path.join(_HERE, "results")


def build_corpus():
    rows = []
    print("=" * 86)
    print("COORDINATION-FORM CORPUS — exact IIT-4.0 Φ over each form")
    print("=" * 86)
    for f in lib.FORMS:
        v = classify_rules(f.rules)
        tags = lib.structural_tags(f.rules)
        match = "ok" if v.structure == f.expected else "MISMATCH"
        rows.append({
            "key": f.key,
            "title": f.title,
            "validated": f.validated,
            "structure": v.structure,
            "competence": v.competence,
            "max_phi_mip": f"{v.max_phi:.6f}",
            "strict_mediation": tags["strict_mediation"],
            "mediator_reads_both": tags["mediator_reads_both"],
            "back_channel": tags["back_channel"],
            "expected": f.expected,
            "expected_check": match,
        })
        flag = "" if match == "ok" else "  <-- " + match
        print(f"  {f.key:<24} {v.structure:<8} {v.competence:<12} "
              f"Φ={v.max_phi:.4f}  strict_med={tags['strict_mediation']!s:<5} "
              f"reads_both={tags['mediator_reads_both']!s:<5}{flag}")
    _write(os.path.join(_RESULTS, "corpus.csv"), rows)
    return rows


def build_toggles():
    """For each triadic form, ablate one structural feature at a time and recompute the verdict.

    Two ablations, both single-change:
      drop_C_from_S : the mediator stops reading the counterpart (S' = its W-only restriction).
                      Removes 'mediator_reads_both'. Tests whether reading the third party is
                      what makes the form irreducible.
      add_backchannel : restore a direct W<->C edge (C also reads W). Removes 'strict_mediation'.
                        Tests whether the bottleneck is what makes the form irreducible.
    """
    print("\n" + "=" * 86)
    print("WHAT TOGGLES IRREDUCIBILITY — single-feature ablations on the triadic forms")
    print("=" * 86)
    rows = []
    triadic = [f for f in lib.FORMS if classify_rules(f.rules).structure == "triadic"]
    for f in triadic:
        base = classify_rules(f.rules)

        # Ablation 1: mediator stops reading C (S' depends on W only). We replace S's rule with
        # one that ignores x[2]: S'(x) := S'(x with C forced to a fixed reference, here C=1),
        # collapsing the C-dependence while preserving the W-dependence shape.
        s_rule = f.rules[1]
        drop_C = [f.rules[0], lambda x, s=s_rule: s((x[0], x[1], 1)), f.rules[2]]
        v_dropC = classify_rules(drop_C)

        # Ablation 2: add a direct back-channel (C also reads W): C' := C' OR W.
        c_rule = f.rules[2]
        add_bc = [f.rules[0], f.rules[1], lambda x, c=c_rule: int(bool(c(x)) or bool(x[0]))]
        v_addbc = classify_rules(add_bc)

        for label, v in [("drop_C_from_S", v_dropC), ("add_backchannel", v_addbc)]:
            flipped = (v.structure == "dyadic")
            rows.append({
                "form": f.key,
                "base_structure": base.structure,
                "base_phi": f"{base.max_phi:.4f}",
                "ablation": label,
                "ablated_structure": v.structure,
                "ablated_phi": f"{v.max_phi:.4f}",
                "flipped_to_dyadic": flipped,
            })
            print(f"  {f.key:<24} base Φ={base.max_phi:.4f}  --{label:<16}-> "
                  f"{v.structure:<8} Φ={v.max_phi:.4f}  "
                  f"{'FLIPPED to dyadic' if flipped else 'still triadic'}")
    _write(os.path.join(_RESULTS, "toggles.csv"), rows)
    return rows


def _write(path, rows):
    os.makedirs(_RESULTS, exist_ok=True)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path}")


def main():
    corpus = build_corpus()
    toggles = build_toggles()
    mism = [r for r in corpus if r["expected_check"] != "ok"]
    print("\n" + "=" * 86)
    print(f"SUMMARY: {len(corpus)} forms; "
          f"{sum(r['structure']=='triadic' for r in corpus)} triadic, "
          f"{sum(r['structure']=='dyadic' for r in corpus)} dyadic. "
          f"{len(mism)} expected-verdict mismatch(es).")
    if mism:
        for r in mism:
            print(f"  MISMATCH {r['key']}: got {r['structure']}, expected {r['expected']}")
    print("=" * 86)


if __name__ == "__main__":
    main()
