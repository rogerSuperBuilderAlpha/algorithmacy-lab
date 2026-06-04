"""Probe 124 (K3) — is a CES-or-coupling hybrid an exact cheap predicate?

Question: a CES count predicate misses only the 8 parity forms, and never false-positives (#102); party
coupling MI[W;C] catches exactly those parity forms (#114). Does the disjunction — a higher-order CES
distinction OR high party coupling — give an exact verdict test where neither part alone does?
Hypothesis: yes; the CES part catches the conjunctive forms and the coupling part catches the parity
forms, so the OR is zero-error. Method: over the corpus, compute the CES higher-order flag and MI[W;C] on
a noisy trajectory; report the error of each part alone and of the disjunction over a threshold sweep.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_hybrid_predicate
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from proxy_audit import exact_phi
from proxy_audit.exact_phi import reachable_states
from structure_suite.suite import extract_suite
from ._info import mutual_information

NOISE = 0.08
T = 8000


def main():
    print("PROBE 124 (K3) — CES-or-coupling hybrid predicate")
    print("=" * 64)
    rng = np.random.default_rng(124)
    ces_hi, mi_wc, y = [], [], []
    for _, rules in enumerate_family():
        sbn = tpm_from_rules(rules)
        rs = reachable_states(sbn, 3)
        if not rs:
            continue
        state = [(rs[0] >> i) & 1 for i in range(3)]
        suite = extract_suite(sbn, cm_from_rules(rules), 3, state)
        if suite is None:
            continue
        traj = exact_phi.simulate_trajectory(add_noise(sbn, NOISE), 3, T, rng)
        ces_hi.append(suite["frac_higher_order"] > 0)
        mi_wc.append(mutual_information(traj, [0], [2]))
        y.append(int(classify_rules(rules, labels=("W", "S", "C")).structure == "triadic"))
    ces_hi = np.array(ces_hi)
    mi_wc = np.array(mi_wc)
    y = np.array(y)

    def err(pred):
        pred = np.array(pred, int)
        return int((pred != y).sum()), int(((pred == 1) & (y == 0)).sum()), int(((pred == 0) & (y == 1)).sum())

    e_ces = err(ces_hi)
    print(f"  {len(y)} forms ({int(y.sum())} triadic)")
    print(f"  CES higher-order flag alone : errors={e_ces[0]} (fp={e_ces[1]}, fn={e_ces[2]})")
    # best coupling threshold alone
    best_mi = min(((err((mi_wc >= t).astype(int))[0], t) for t in np.unique(mi_wc)), key=lambda z: z[0])
    print(f"  MI[W;C] >= {best_mi[1]:.4f} alone     : errors={best_mi[0]}")
    # hybrid: CES higher-order OR MI>=t, swept
    best_hy = None
    for t in np.unique(mi_wc):
        e = err((ces_hi | (mi_wc >= t)).astype(int))
        if best_hy is None or e[0] < best_hy[0][0]:
            best_hy = (e, t)
    e, t = best_hy
    print(f"  hybrid (CES-hi OR MI>= {t:.4f}) : errors={e[0]} (fp={e[1]}, fn={e[2]})" + ("  *** EXACT ***" if e[0] == 0 else ""))
    print("=" * 64)
    if e[0] == 0:
        print("  Reading: the disjunction is an exact cheap test. The cause-effect higher-order flag catches")
        print("  the conjunctive triads and party coupling catches the parity triads, so together they")
        print("  define the verdict with no partition search — each part covering the other's blind spot.")
    else:
        print("  Reading: the hybrid lowers the error but does not reach zero; the two cheap signals overlap")
        print("  imperfectly and a cheap predicate that exactly defines the verdict remains unfound.")
    print("=" * 64)


if __name__ == "__main__":
    main()
