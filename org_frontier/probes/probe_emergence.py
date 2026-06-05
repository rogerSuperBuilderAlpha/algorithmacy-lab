"""Probe 49 — causal emergence on coordination forms (Hoel / Klein & Hoel).

The dossier highlights causal emergence / effective information as social-ready irreducibility
measures. The repo's emergence_vs_phi found, on random nets, that effective information tracks Φ
among integrated systems but causal emergence is nearly orthogonal to Φ. Test on coordination forms:
do triadic forms carry higher effective information, and do they show causal emergence under
coarse-graining?

H49: triadic forms have higher effective information than dyadic; causal emergence is ~orthogonal to
the verdict (triadic forms do not systematically emerge), echoing emergence_vs_phi.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_emergence
"""

from pyphi import convert

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus import forms_library as lib
from foundations.emergence_vs_phi.emergence import effective_information, causal_emergence

LABELS = ("W", "S", "C")


def main():
    print("PROBE 49 — causal emergence / effective information on coordination forms")
    print("=" * 80)
    print(f"  {'form':<24}{'verdict':<9}{'EI':<8}{'causal emergence'}")
    by = {"triadic": [], "dyadic": []}
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        v = classify_rules(f.rules, labels=LABELS)
        sbs = convert.state_by_node2state_by_state(tpm_from_rules(f.rules))
        ei = effective_information(sbs)
        ce = causal_emergence(sbs)[0]
        by[v.structure].append((ei, ce))
        print(f"  {f.key:<24}{v.structure:<9}{ei:<8.3f}{ce:.3f}")
    print("=" * 80)
    for k, vals in by.items():
        if vals:
            mei = sum(x[0] for x in vals) / len(vals)
            mce = sum(x[1] for x in vals) / len(vals)
            print(f"  {k:<8} mean EI={mei:.3f}  mean causal-emergence={mce:.3f}  (n={len(vals)})")
    print("=" * 80)


if __name__ == "__main__":
    main()
