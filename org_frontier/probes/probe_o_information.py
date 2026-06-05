"""Probe 46 — O-information: is the triad synergy-dominated?

The O-information (Rosas, Mediano, Gastpar & Jensen 2019) is negative when a system is
synergy-dominated and positive when redundancy-dominated. It is one of the social-science-ready
irreducibility measures the dossier highlights. Do triadic coordination forms come out
synergy-dominated (O < 0) and dyadic ones redundancy-dominated (O > 0)?

H46: triadic forms have negative O-information (synergy); dyadic forms have non-negative O-info
(redundancy or independence). This would tie the exact-Φ verdict to a cheap, scalable measure.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_o_information
"""

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus import forms_library as lib
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.proxy_audit import exact_phi
from . import _info

LABELS = ("W", "S", "C")


def main():
    rng = np.random.default_rng(5)
    print("PROBE 46 — O-information (synergy vs redundancy) vs the verdict")
    print("=" * 74)
    print(f"  {'form':<24}{'verdict':<9}{'O-information':<14}{'character'}")
    by = {"triadic": [], "dyadic": []}
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        v = classify_rules(f.rules, labels=LABELS)
        tpm = add_noise(tpm_from_rules(f.rules), 0.1)
        traj = exact_phi.simulate_trajectory(tpm, 3, 8000, rng)
        o = _info.o_information(traj, [0, 1, 2])
        char = "synergy" if o < -1e-3 else ("redundancy" if o > 1e-3 else "~independent")
        by[v.structure].append(o)
        print(f"  {f.key:<24}{v.structure:<9}{o:<14.4f}{char}")
    print("=" * 74)
    for k, vals in by.items():
        if vals:
            print(f"  {k:<8} mean O-info = {np.mean(vals):+.4f}  (n={len(vals)})")
    print("=" * 74)


if __name__ == "__main__":
    main()
