"""Probe 464: exact input-observation noise on counting and weighted quorums.

Run: python -m org_frontier.probes.weighted_quorum.input_noise.probe_input_noise
Add --write to save results.json; default and CI runs only print. Predictions,
controls and scoring were fixed in hypotheses.md before the first computation.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pyphi
from pyphi import new_big_phi

from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.classifier.classifier import PHI_EPS, classify, tpm_from_rules
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (
    cm_numeric, gate_c1, labels_for, rules_for, table_of,
)

FORMS = (
    ("OR", (1, 1, 1), 1),
    ("majority", (1, 1, 1), 2),
    ("AND", (1, 1, 1), 3),
    ("weighted-2", (1, 1, 2, 2), 2),
    ("weighted-5", (1, 1, 2, 2), 5),
)
RATES = (0.0, 0.1, 0.5)


def input_tpm(table, n, eta):
    """Marginalize independent observation errors; actual parties copy S."""
    tpm = np.zeros((2 ** (n + 1), n + 1))
    for state in range(len(tpm)):
        actual = state >> 1
        for observed, output in enumerate(table):
            distance = (actual ^ observed).bit_count()
            tpm[state, 0] += output * eta ** distance * (1 - eta) ** (n - distance)
        tpm[state, 1:] = state & 1
    return tpm


def read_case(name, weights, quota, eta):
    n = len(weights)
    labels = labels_for(n)
    table = table_of(weights, quota)
    tpm = input_tpm(table, n, eta)
    if eta == 0:
        assert np.allclose(tpm, tpm_from_rules(rules_for(table, n)), atol=1e-12, rtol=0)
    if eta == 0.5:
        assert np.ptp(tpm[:, 0]) <= 1e-12, "independent-input endpoint failed"
    cm = cm_numeric(tpm)
    verdict = classify(tpm, cm, labels=labels)
    network = pyphi.Network(tpm, cm=cm, node_labels=labels)
    states = []
    for index in reachable_states(tpm, n + 1):
        state = tuple((index >> i) & 1 for i in range(n + 1))
        complex_ = new_big_phi.maximal_complex(network, state)
        core, phi = [], 0.0
        if not isinstance(complex_, new_big_phi.NullPhiStructure):
            core = [labels[i] for i in complex_.node_indices]
            phi = float(complex_.phi)
        states.append(dict(state=list(state), core=core, core_phi=phi))
    max_core = max((row["core_phi"] for row in states), default=0.0)
    winners = [row for row in states if row["core_phi"] > PHI_EPS
               and abs(row["core_phi"] - max_core) <= PHI_EPS]
    if eta == 0.5:
        assert verdict.max_phi <= PHI_EPS, "independent-input endpoint binds whole system"
        assert all(not ("S" in row["core"] and len(row["core"]) > 1) for row in states)
    return dict(form=name, weights=list(weights), quota=quota, eta=eta,
                max_phi=verdict.max_phi, max_core_phi=max_core,
                phi_profile=[dict(state=list(state), phi=phi) for state, phi in verdict.phi_profile],
                cores_by_state=states, maximizing_cores=winners)


def has_core(row, target):
    return bool(row["maximizing_cores"]) and all(
        set(state["core"]) == target for state in row["maximizing_cores"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="save deterministic results.json")
    args = parser.parse_args()
    if not gate_c1():
        raise RuntimeError("C1 controls failed")
    rows = [read_case(name, weights, quota, eta)
            for name, weights, quota in FORMS for eta in RATES]
    print("C2 deterministic TPM identity: PASS")
    print("C3 independent-input endpoint: PASS")
    for row in rows:
        cores = sorted({tuple(state["core"]) for state in row["maximizing_cores"]})
        print(f"{row['form']:<12} eta={row['eta']:.1f} whole={row['max_phi']:.6f} "
              f"core_phi={row['max_core_phi']:.6f} cores={cores}")
    noisy = {row["form"]: row for row in rows if row["eta"] == 0.1}
    scores = {
        "H1": all(has_core(noisy[name], {"S", "P1", "P2", "P3"}) for name in ("OR", "AND")),
        "H2": noisy["majority"]["max_phi"] <= PHI_EPS,
        "H3": all(has_core(noisy[name], {"S", "P3", "P4"})
                  and noisy[name]["max_phi"] <= PHI_EPS for name in ("weighted-2", "weighted-5")),
    }
    for name, supported in scores.items():
        print(f"{name}: {'SUPPORTED' if supported else 'REFUTED'}")
    if args.write:
        result = dict(pyphi_version=pyphi.__version__, phi_eps=PHI_EPS,
                      hypotheses={name: "SUPPORTED" if ok else "REFUTED" for name, ok in scores.items()},
                      rows=rows)
        Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
