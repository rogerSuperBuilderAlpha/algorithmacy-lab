"""Classify the built-in library and write results/verdicts.csv.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.run
"""

import csv
import os

from .classifier import classify_rules
from . import forms

_HERE = os.path.dirname(__file__)
_RESULTS = os.path.join(_HERE, "results")


def main():
    os.makedirs(_RESULTS, exist_ok=True)
    rows = []
    print("=" * 80)
    print("LITERACY-OR-ALGORITHMACY CLASSIFIER — built-in coordination forms")
    print("=" * 80)
    for fname, builder in forms.FORMS.items():
        v = classify_rules(builder())
        print(f"\n### {fname}")
        print("  " + str(v).replace("\n", "\n  "))
        rows.append({
            "form": fname,
            "structure": v.structure,
            "competence": v.competence,
            "max_phi_mip": f"{v.max_phi:.6f}",
            "n_states_evaluated": v.n_states_evaluated,
            "n_states_irreducible": v.n_states_irreducible,
            "max_phi_state": "".join(str(b) for b in v.mip_state) if v.mip_state else "",
            "mip_partition": v.mip_partition,
            "expected_structure": forms.EXPECTED.get(fname, ""),
        })

    out = os.path.join(_RESULTS, "verdicts.csv")
    with open(out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
