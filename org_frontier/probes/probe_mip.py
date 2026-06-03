"""Probe 26 — the MIP as the coordination's structural fault line.

The verdict is Φ over the minimum-information partition — the cut the system resists least, i.e.
where it "almost factors." This probe reads the MIP itself across the triadic corpus forms and asks
what it reveals: which party (or grouping) is the weakest structural link.

H26: the MIP isolates the least-pivotal / most-separable party — the cut tells you where the
coordination is most fragile, not just whether it is irreducible.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_mip
"""

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus import forms_library as lib


def main():
    print("PROBE 26 — the minimum-information partition as a fault line")
    print("=" * 84)
    for f in lib.FORMS:
        v = classify_rules(f.rules, labels=("W", "S", "C")[:len(f.rules)] if len(f.rules) == 3 else None)
        if v.structure != "triadic":
            continue
        print(f"  {f.key:<24} Φ={v.max_phi:.3f}   MIP cut: {v.mip_partition}   @state {v.mip_state}")
    print("=" * 84)
    print("  Reading: the MIP cut is the least-damaging partition — the coordination's weakest")
    print("  seam. {W,SC} means the worker is the most separable element; the system+counterpart")
    print("  hold together more tightly than the worker attaches to them.")
    print("=" * 84)


if __name__ == "__main__":
    main()
