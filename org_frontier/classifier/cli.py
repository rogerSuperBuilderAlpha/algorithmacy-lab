"""Command-line front end: get a literacy-or-algorithmacy verdict for a coordination form.

Two ways to specify a form.

1. By built-in name:
     python -m org_frontier.classifier.cli --form gig_false_dyad
     python -m org_frontier.classifier.cli --list

2. By a JSON model file describing a state-by-node TPM (and optional connectivity matrix):
     python -m org_frontier.classifier.cli --model my_form.json

   JSON schema:
     {
       "labels": ["W", "S", "C"],            # optional, default W,S,C,...
       "tpm": [[..n floats..], ... 2^n rows], # state-by-node, little-endian states
       "cm":  [[..n ints..], ... n rows]      # optional; inferred-from-tpm not supported here,
                                              # supply cm or use --form / Boolean rules in code
     }
"""

import argparse
import json
import sys

import numpy as np

from .classifier import classify, classify_rules, DEFAULT_LABELS
from . import forms


def _from_model_file(path):
    with open(path) as f:
        spec = json.load(f)
    tpm = np.array(spec["tpm"], dtype=float)
    if "cm" not in spec:
        raise SystemExit("model file must include a connectivity matrix 'cm' "
                         "(state-by-node TPM does not uniquely determine it here)")
    cm = np.array(spec["cm"], dtype=int)
    labels = tuple(spec.get("labels", DEFAULT_LABELS))
    return classify(tpm, cm, labels=labels)


def main(argv=None):
    p = argparse.ArgumentParser(description="Literacy-or-algorithmacy classifier (exact IIT-4.0 Φ).")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--form", help="name of a built-in coordination form")
    g.add_argument("--model", help="path to a JSON model file (tpm + cm)")
    g.add_argument("--list", action="store_true", help="list built-in forms and exit")
    args = p.parse_args(argv)

    if args.list:
        print("Built-in coordination forms:")
        for name in forms.FORMS:
            print(f"  {name:<22} (expected: {forms.EXPECTED.get(name, '?')})")
        return 0

    if args.form:
        if args.form not in forms.FORMS:
            raise SystemExit(f"unknown form '{args.form}'. Use --list to see options.")
        verdict = classify_rules(forms.FORMS[args.form]())
        title = args.form
    else:
        verdict = _from_model_file(args.model)
        title = args.model

    print(f"\nForm: {title}")
    print(verdict)
    print(f"\nVERDICT: this coordination form demands {verdict.competence.upper()}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
