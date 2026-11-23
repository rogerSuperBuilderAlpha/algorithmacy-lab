"""Shared-error share sweep (Part A) and per-subset tie enumeration (Part B) on noisy quorum hubs.

Run from the repo root: python org_frontier/studies/shared_share_ties/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import itertools
import json
import os
import sys
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np  # noqa: E402
import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, classify  # noqa: E402
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import input_tpm  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import (  # noqa: E402
    cm_numeric, gate_c1, labels_for, table_of,
)
from org_frontier.studies.quorum_correlated_noise.correlated import model_tpm  # noqa: E402

N = 3
SHARES = (0.0, 0.25, 0.5, 0.75, 0.9, 1.0)
A_RATES = (0.1, 0.2)
A_FORMS = (("OR3", 1), ("MAJ3", 2))
B_CASES = (("MAJ3", (1, 1, 1), 2, 0.05), ("MAJ3", (1, 1, 1), 2, 0.1), ("MAJ3", (1, 1, 1), 2, 0.2),
           ("2of4", (1, 1, 1, 1), 2, 0.1), ("2of4", (1, 1, 1, 1), 2, 0.2))


def share_tpm(table, e, s):
    a = s * e
    b = (e - a) / (1 - 2 * a)
    full = 2 ** N - 1
    p = np.zeros(2 ** N)
    for shared in (0, 1):
        ps = a if shared else 1 - a
        for m in range(2 ** N):
            d = m.bit_count()
            p[m ^ (full if shared else 0)] += ps * b ** d * (1 - b) ** (N - d)
    assert abs(p.sum() - 1) < 1e-12
    assert abs(sum(p[m] for m in range(2 ** N) if m & 1) - e) < 1e-12, "marginal error mismatch"
    tpm = np.zeros((2 ** (N + 1), N + 1))
    for state in range(len(tpm)):
        tpm[state, 0] = sum(p[m] * table[(state >> 1) ^ m] for m in range(2 ** N))
        tpm[state, 1:] = state & 1
    return tpm


def part_a(rates, forms, shares):
    rows = []
    for name, quota in forms:
        table = table_of((1, 1, 1), quota)
        for e in rates:
            for s in shares:
                tpm = share_tpm(table, e, s)
                if s == 0:
                    assert np.allclose(tpm, input_tpm(table, N, e), atol=1e-12, rtol=0)
                if s == 1:
                    assert np.allclose(tpm, model_tpm(table, "common", e), atol=1e-12, rtol=0)
                v = classify(tpm, cm_numeric(tpm), labels=labels_for(N))
                rows.append(dict(form=name, e=e, s=s, whole_phi=float(v.max_phi)))
    return rows


def part_b(cases):
    out = []
    for name, weights, quota, e in cases:
        n = len(weights)
        labels = labels_for(n)
        tpm = input_tpm(table_of(weights, quota), n, e)
        net = pyphi.Network(tpm, cm=cm_numeric(tpm), node_labels=labels)
        for index in reachable_states(tpm, n + 1):
            state = tuple((index >> i) & 1 for i in range(n + 1))
            # same subset enumeration maximal_complex uses: subsets whose state is unreachable are skipped
            phis = {tuple(sub.node_indices): float(new_big_phi.sia(sub).phi)
                    for sub in new_big_phi.reachable_subsystems(net, net.node_indices, state)}
            skipped = 2 ** (n + 1) - 1 - len(phis)
            top = max(phis.values())
            winners = sorted((sub for sub, v in phis.items() if top - v <= PHI_EPS), key=len)
            sizes = {len(w) for w in winners}
            k = len(winners[0])
            cls = [c for c in itertools.combinations(range(n + 1), k) if 0 in c]
            h4 = (top > PHI_EPS and len(sizes) == 1 and k < n + 1 and sorted(winners) == sorted(cls))
            full = phis[tuple(range(n + 1))]
            out.append(dict(form=name, e=e, state=list(state), max_phi=top,
                            winners=[[labels[i] for i in w] for w in winners], winner_size=k,
                            full_phi=full, skipped=skipped, h4=h4, h5=top - full > PHI_EPS))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true", help="CI subset")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    if args.quick:
        a = part_a((0.2,), (("MAJ3", 2),), (0.0, 0.5, 1.0))
        b = part_b((B_CASES[2],))
    else:
        a = part_a(A_RATES, A_FORMS, SHARES)
        b = part_b(B_CASES)
    print("C2 marginal error, s=0 = input_tpm, s=1 = common TPM: PASS")
    for r in a:
        print(f"A {r['form']:<5} e={r['e']:<4} s={r['s']:<5} whole={r['whole_phi']:.6f}")
    for r in b:
        print(f"B {r['form']:<5} e={r['e']:<5} state={''.join(map(str, r['state']))} max={r['max_phi']:.6f} "
              f"k={r['winner_size']} skipped={r['skipped']} n_winners={len(r['winners'])} full={r['full_phi']:.6f} "
              f"H4={'Y' if r['h4'] else 'N'} H5={'Y' if r['h5'] else 'N'}")
    if args.quick:
        return
    g = {(r["form"], r["e"], r["s"]): r["whole_phi"] for r in a}
    scores = {
        "H1": all(g[("MAJ3", e, s1)] > g[("MAJ3", e, s2)] for e in A_RATES
                  for s1, s2 in zip(SHARES, SHARES[1:])),
        "H2": all(g[("MAJ3", e, s)] > PHI_EPS for e in A_RATES for s in SHARES[:-1])
        and all(g[("MAJ3", e, 1.0)] <= PHI_EPS for e in A_RATES),
        "H3": all(g[("OR3", e, s1)] < g[("OR3", e, s2)] for e in A_RATES
                  for s1, s2 in zip(SHARES, SHARES[1:])),
        "H4": all(r["h4"] for r in b),
        "H5": all(r["h5"] for r in b),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            part_a=a, part_b=b), indent=1) + "\n")


if __name__ == "__main__":
    main()
