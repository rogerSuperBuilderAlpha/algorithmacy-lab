"""Probe 55 (#46) — role-symmetry as an exact automorphism.

Question: is swapping the worker and counterpart an exact symmetry of the verdict, not just a
behavioral one (Probe 22)? Hypothesis: relabeling W↔C preserves both the verdict and Φ exactly, since
node relabeling is an IIT isomorphism. Method: over the strict-mediation n=3 family, build the
W↔C-swapped form (swap nodes 0 and 2, and swap the mediator's two inputs), classify, and compare Φ and
verdict to the original. Count any flips or Φ differences.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_role_symmetry
"""

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family

LABELS = ("W", "S", "C")


def swap_wc(rules):
    """Relabel node 0 (W) and node 2 (C): new node i reads the swapped state, S swaps its inputs."""
    perm = {0: 2, 1: 1, 2: 0}

    def remap(x):
        return (x[2], x[1], x[0])  # present state seen under the swap

    r0, r1, r2 = rules
    # new W (index 0) behaves as old C (index 2); new C as old W; S input order swapped
    new = [
        lambda x: r2(remap(x)),
        lambda x: r1(remap(x)),
        lambda x: r0(remap(x)),
    ]
    return new


def main():
    flips = 0
    max_dphi = 0.0
    n = 0
    for _label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        vs = classify_rules(swap_wc(rules), labels=LABELS)
        n += 1
        flips += v.structure != vs.structure
        max_dphi = max(max_dphi, abs(v.max_phi - vs.max_phi))
    print("PROBE 55 (#46) — role-symmetry (W↔C) as an automorphism (256 forms)")
    print("=" * 70)
    print(f"  verdict flips under W↔C swap : {flips}/{n}")
    print(f"  max |Φ − Φ_swapped|          : {max_dphi:.6f}")
    print("=" * 70)
    print("  Reading: zero flips and zero Φ difference means worker↔counterpart relabeling is an")
    print("  exact automorphism of the verdict — the triad does not privilege either human role,")
    print("  confirming Probe 22's behavioral symmetry as a structural identity.")
    print("=" * 70)


if __name__ == "__main__":
    main()
