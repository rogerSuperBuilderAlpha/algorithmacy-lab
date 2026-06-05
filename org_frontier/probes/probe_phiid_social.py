"""Probe 47 — ΦID atoms on coordination time series (a stated white-space).

The dossier's clean gap: integrated information decomposition (ΦID) has never been applied to any
social/behavioral/economic time series. Apply it here. For each coordination form, decompose the
worker-vs-{system,counterpart} information flow into ΦID atoms (phyid, CCS redundancy) and read off
the persistent-synergy atom (sts) and the double-redundancy atom (rtr).

H47: triadic forms carry more persistent synergy (sts) than dyadic forms — the irreducible
coordination shows up as synergistic information the parts do not have separately — while dyadic
forms are redundancy/transfer dominated.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phiid_social
"""

import numpy as np
from phyid.calculate import calc_PhiID

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus import forms_library as lib
from org_frontier.proxy_bridge.bridge import add_noise
from foundations.phiid_vs_phi.phiid_measure import _part_int_series
from foundations.proxy_audit import exact_phi

LABELS = ("W", "S", "C")


def main():
    rng = np.random.default_rng(7)
    print("PROBE 47 — ΦID atoms on coordination series (synergy vs redundancy)")
    print("=" * 78)
    print(f"  {'form':<24}{'verdict':<9}{'synergy(sts)':<14}{'redundancy(rtr)'}")
    by = {"triadic": [], "dyadic": []}
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        v = classify_rules(f.rules, labels=LABELS)
        tpm = add_noise(tpm_from_rules(f.rules), 0.1)
        traj = exact_phi.simulate_trajectory(tpm, 3, 8000, rng)
        A = _part_int_series(traj, (0,))         # worker
        B = _part_int_series(traj, (1, 2))       # system + counterpart
        atoms, _ = calc_PhiID(A, B, tau=1, kind="discrete", redundancy="CCS")
        sts = float(np.mean(atoms["sts"]))
        rtr = float(np.mean(atoms["rtr"]))
        by[v.structure].append(sts)
        print(f"  {f.key:<24}{v.structure:<9}{sts:<14.4f}{rtr:.4f}")
    print("=" * 78)
    for k, vals in by.items():
        if vals:
            print(f"  {k:<8} mean persistent synergy (sts) = {np.mean(vals):+.4f}  (n={len(vals)})")
    print("  (ΦID applied to a coordination series — a measure the dossier notes has never been")
    print("   used on social/behavioral/economic data.)")
    print("=" * 78)


if __name__ == "__main__":
    main()
