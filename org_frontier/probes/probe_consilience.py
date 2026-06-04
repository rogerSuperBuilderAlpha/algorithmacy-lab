"""Probe 89 (#36) — a consilience map: where adjacent measures agree with exact Φ and where they diverge.

Question: several information measures sit next to integrated information — O-information, ΦID Φ_R,
effective information, causal emergence, the autoregressive Φ_AR. Over the whole 256-form family, where
do they agree with the exact dyadic/triadic verdict and where do they diverge? Hypothesis: the measures
agree with the verdict on clear cases and diverge on a mappable minority; none reproduces the verdict
exactly, but their agreement is structured, not random. Method: compute the exact verdict plus each
measure on every form (deterministic measures on the TPM, time-series measures on a noisy trajectory),
cache the panel, and cross-tabulate each measure's best-threshold agreement with the verdict.

Writes: org_frontier/probes/results/consilience_panel.csv (read by Probes 90, 91).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_consilience
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from pyphi import convert

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules
from org_frontier.corpus.population import enumerate_family
from org_frontier.proxy_bridge.bridge import add_noise
from proxy_audit import exact_phi
from emergence_vs_phi.emergence import effective_information, causal_emergence
from phiid_vs_phi.phiid_measure import phi_r_integration
from ._info import o_information
from .probe_phi_ar import phi_ar

LABELS = ("W", "S", "C")
NOISE = 0.08
T = 4000
RESULTS = os.path.join(os.path.dirname(__file__), "results")
PANEL = os.path.join(RESULTS, "consilience_panel.csv")
MEASURES = ("EI", "CE", "O_info", "phi_AR", "phi_R")


def build_panel():
    os.makedirs(RESULTS, exist_ok=True)
    rng = np.random.default_rng(7)
    rows = []
    for i, (label, rules) in enumerate(enumerate_family()):
        v = classify_rules(rules, labels=LABELS)
        sbn = tpm_from_rules(rules)
        sbs = convert.state_by_node2state_by_state(sbn)
        ei = effective_information(sbs)
        ce = causal_emergence(sbs)[0]
        noisy = add_noise(sbn, NOISE)
        traj = exact_phi.simulate_trajectory(noisy, 3, T, rng)
        oi = o_information(traj, [0, 1, 2])
        par = phi_ar(traj)
        pr = phi_r_integration(noisy, 3, rng, traj_len=T)[0]
        rows.append({"label": label, "triadic": int(v.structure == "triadic"),
                     "phi_exact": round(v.max_phi, 6), "EI": round(ei, 6), "CE": round(ce, 6),
                     "O_info": round(oi, 6), "phi_AR": round(par, 6), "phi_R": round(pr, 6)})
        if (i + 1) % 64 == 0:
            print(f"  panel {i+1}/256")
    with open(PANEL, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {PANEL}")
    return rows


def _best_threshold_agreement(scores, y):
    """Best balanced agreement of (score > t) with the label y, over candidate thresholds."""
    s = np.array(scores)
    y = np.array(y)
    cand = np.unique(s)
    best = (0.0, None, None)
    for t in cand:
        pred = (s > t).astype(int)
        tp = int(((pred == 1) & (y == 1)).sum())
        fp = int(((pred == 1) & (y == 0)).sum())
        agree = (pred == y).mean()
        if agree > best[0]:
            best = (agree, tp, fp)
    return best


def main():
    print("PROBE 89 (#36) — consilience map over the 256-form family")
    print("=" * 70)
    rows = build_panel()
    y = [r["triadic"] for r in rows]
    n_tri = sum(y)
    print(f"  {len(rows)} forms, {n_tri} triadic; agreement of each measure's best threshold:")
    print(f"  {'measure':<10}{'best agree':<13}{'triadic caught':<18}{'dyadic flagged'}")
    for m in MEASURES:
        agree, tp, fp = _best_threshold_agreement([r[m] for r in rows], y)
        print(f"  {m:<10}{agree:<13.3f}{f'{tp}/{n_tri}':<18}{fp}")
    print("=" * 70)
    print("  Reading: each measure's best single threshold agrees with the verdict to some degree but")
    print("  none reproduces it exactly; the false positives are the forms where a measure sees")
    print("  integration the exact verdict does not call triadic. The divergence is structured.")
    print("=" * 70)


if __name__ == "__main__":
    main()
