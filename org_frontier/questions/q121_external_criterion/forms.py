"""Q121: an external criterion for the verdict — responding to the critical review's T1.

The critical review (CRITICAL_REVIEW_Q111_Q117.md, T1) found the construct's behavioral validation unmet:
every independent agent-difficulty check failed or was weak (Probes 98, 107, 108), and the one supporting
check (18) is circular. The defense agenda's first question asks for a non-circular criterion on which triadic
forms are reliably distinct.

This study reframes and answers the weak form of that question. Two facts sharpen it. First, the family is
class-imbalanced (24 triadic, 232 dyadic), so a high rank-AUC on the full family is a trivial bar: the
topology-only feedback cycle (Q117) already scores ~0.97. The severe test is the 40 full-cycle forms, where
Q117 showed topology and logic split 24/16 and connectivity cannot decide. Second, Q117 found the verdict
lives in the determination's logic, not its wiring, which predicts that an observational criterion will fail
there and an interventional one may succeed.

Two non-Φ criteria, from formalisms independent of IIT, are tested against the exact verdict:

- `total_correlation_next` — observational: the multi-information among the next-state components under a
  uniform current state. Pure statistical dependence of the dynamics' output, no intervention.
- `damage_spreading` — interventional: the Boolean-network damage-spreading measure (Kauffman; Derrida &
  Pomeau 1986). Flip one party, run the deterministic dynamics, and average the Hamming divergence from the
  unperturbed trajectory over a horizon. A do-intervention probe, no Φ.

Imported by `probe_external_criterion.py`.
"""

import math
import os
import sys
from collections import Counter

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q93_fragility_margin import forms as q93
from org_frontier.questions.q117_phi_free_test import forms as q117
from org_frontier.classifier.classifier import tpm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states

DAMAGE_HORIZON = 4          # steps; the result is stable for any horizon >= 2 (see methods)


def _next(tpm, n, s):
    return tuple(int(round(tpm[s, j])) for j in range(n))


def total_correlation_next(rules):
    """Observational: multi-information Σ H(Y_i) − H(Y) of the next-state joint under uniform current state."""
    n = len(rules)
    tpm = tpm_from_rules(rules)
    S = 2 ** n
    joint = Counter()
    marg = [Counter() for _ in range(n)]
    for s in range(S):
        y = _next(tpm, n, s)
        joint[y] += 1
        for i in range(n):
            marg[i][y[i]] += 1

    def H(c):
        return -sum((v / S) * math.log2(v / S) for v in c.values() if v > 0)

    return sum(H(marg[i]) for i in range(n)) - H(joint)


def damage_spreading(rules, horizon=DAMAGE_HORIZON):
    """Interventional: average Hamming divergence after a single-party flip, over the horizon, over reachable
    starts and all parties (a Boolean-network damage-spreading / Derrida measure)."""
    n = len(rules)
    tpm = tpm_from_rules(rules)
    starts = list(reachable_states(tpm, n)) or list(range(2 ** n))
    total = 0.0
    count = 0
    for s0 in starts:
        for flip in range(n):
            a, b = s0, s0 ^ (1 << flip)
            for _ in range(horizon):
                a = sum(_next(tpm, n, a)[i] << i for i in range(n))
                b = sum(_next(tpm, n, b)[i] << i for i in range(n))
                total += sum((((a >> i) & 1) != ((b >> i) & 1)) for i in range(n))
                count += 1
    return total / max(count, 1)


def rank_auc(scores, labels):
    """Mann-Whitney rank-AUC: the probability a triadic form outscores a dyadic one (ties count 0.5)."""
    pos = [s for s, l in zip(scores, labels) if l]
    neg = [s for s, l in zip(scores, labels) if not l]
    if not pos or not neg:
        return float("nan")
    c = sum((1.0 if p > q else 0.5 if p == q else 0.0) for p in pos for q in neg)
    return c / (len(pos) * len(neg))


def evaluate():
    """Compute both criteria and the verdict over the 256-form family; return AUCs on the full family and on
    the full-cycle hard subset, plus the cycle-only AUC for reference."""
    labels, cyc, obs, inter = [], [], [], []
    for bits, rules in q93.enumerate_family():
        labels.append(q93.is_triadic(rules))
        cyc.append(1 if q117.cycle_present(bits) else 0)
        obs.append(total_correlation_next(rules))
        inter.append(damage_spreading(rules))
    hard = [i for i in range(len(labels)) if cyc[i] == 1]
    h_lab = [labels[i] for i in hard]

    def sub(xs):
        return [xs[i] for i in hard]

    return {
        "n": len(labels), "triadic": sum(labels),
        "n_hard": len(hard), "triadic_hard": sum(h_lab),
        "auc_cycle_full": rank_auc(cyc, labels),
        "auc_obs_full": rank_auc(obs, labels),
        "auc_inter_full": rank_auc(inter, labels),
        "auc_obs_hard": rank_auc(sub(obs), h_lab),
        "auc_inter_hard": rank_auc(sub(inter), h_lab),
    }
