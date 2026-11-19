"""Check two stipulated crew-offer forms against the field protocol controls.

These relabel M2 from mocks.py. No real crew workflow is encoded here.
Run from the repository root: python -m org_frontier.field.crew_offer_model_demo
"""

from org_frontier.classifier.classifier import classify_rules
from org_frontier.classifier.validate import factoring_control, irreducible_control
from org_frontier.probes.lib import major_complex


def relay():
    # Node order: producer, system, crew member.
    return [lambda x: x[1], lambda x: x[0], lambda x: x[1]]


def binding():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def main():
    for name, rules, expected in (
        ("relay", relay(), "dyadic"),
        ("binding", binding(), "triadic"),
    ):
        decoupled = classify_rules(factoring_control())
        coupled = classify_rules(irreducible_control())
        if decoupled.structure != "dyadic" or coupled.structure != "triadic":
            raise RuntimeError("field protocol controls failed; no toy verdict computed")
        print(f"{name}: controls passed")
        result = classify_rules(rules, labels=("P", "S", "C"))
        core, core_phi = major_complex(rules, ("P", "S", "C"))
        print(f"{name}: {result.structure}; whole-system Φ={result.max_phi:.3f}; "
              f"major complex={','.join(core) if core else 'none'} "
              f"(Φ={max(core_phi, 0.0):.3f})")
        if result.structure != expected:
            raise RuntimeError(f"{name}: predicted {expected}, got {result.structure}")
    print("Toy method check passed; no field verdict.")


if __name__ == "__main__":
    main()
