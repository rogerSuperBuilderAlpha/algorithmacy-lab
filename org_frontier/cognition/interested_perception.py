"""The direct-perception battery extended to the interested mediator (Q126).

The cognition arm's direct-perception battery asks whether a worker can recover a system's rule from
the outcomes she sees. Its two readings are D1, the AUC at which the Phi verdict is recoverable from
W and C outcome traces, and D2, the share of the rule a worker learns when the counterpart C is
hidden and she fits the worker-marginal alone. Both were measured on random strict gates: D1 reads
AUC 0.67, D2 reads 0.77 of the rule learnable from the marginal.

This module is the shared bridge for an empirical line that swaps the random strict gate for the
Q126 interested mediator. The interested mediator holds an agenda a and imposes it on the k input
states where the parties least warrant it, committing the faithful AND elsewhere. The question is
whether an imposed agenda is more, less, or equally perceivable than a merely hidden rule.

Two readings:

  interested_vs_faithful_auc(k_levels, ...) -> the AUC at which an interested (k>0) mediator is
      told from the faithful (k=0) gate by the W<->C cross-recurrence peak prominence of sampled
      outcome traces. Lower AUC means the agenda leaves a fainter trace in the outcomes.

  marginal_fit_error(k, ...) -> the worker-marginal fit error against (a) an interested mediator at
      level k and (b) a faithful hidden-counterpart strict gate, both with C hidden. The error is the
      share of (W, C) input states a best-fit f(W) mispredicts. A larger error means the agenda adds
      inferential opacity the random gate does not.

Everything is seeded; repeated calls reproduce exactly. The forms reuse the Q126 mediator family and
the recurrence module's trajectory and peak. No Phi is recomputed here; the classifier and the
trajectory generator are the existing instruments.

Validation gap: exact constructions on small Boolean models. The result is evidence about the
instruments and the construct, not a measurement of a real platform. "Agenda", "approve", "deny" are
labels for output values, not measured intent. The empirical arms run on synthetic outcome traces.

Run from the repo root:
    PYPHI_WELCOME_OFF=true python -m org_frontier.cognition.interested_perception
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.recurrence.crqa import trajectory, peak
from org_frontier.questions.q126_interested_mediator.probe_interested_mediator import (
    mediator,
    triad_rules,
    STATES,
)

LABELS = ("W", "S", "C")

# The battery's published random-gate readings, the controls this line compares against.
TRIADIC_DETECTION_AUC = 0.67   # D1: AUC at which the Phi verdict is recoverable from outcomes
HIDDEN_GATE_MARGINAL = 0.77    # D2: share of a random strict gate learnable from the worker-marginal


def _rand_strict_tt(rng):
    """A random strict gate as its 4-entry truth table over (W, C), index W + 2C."""
    return [rng.randint(0, 1) for _ in range(4)]


def _wc_peak_prominence(rules, steps, rng, flip, max_lag):
    """The W<->C cross-recurrence peak prominence of a sampled outcome trace of a triad form.

    The worker sees her own outcome W' and the counterpart outcome C'; both echo the mediator's
    commit one step on. A directed coupling through the mediator makes a prominent DCRP peak; a
    mediator that ignores the parties makes a flatter one. Column 0 is W, column 2 is C.
    """
    tr = trajectory(rules, steps, rng, flip=flip)
    return peak(tr[:, 0], tr[:, 2], max_lag=max_lag)[1]


def interested_vs_faithful_auc(n=120, agenda=1, k_interested=2, steps=600, flip=0.08,
                               max_lag=8, seed=11):
    """AUC for telling an interested (k = k_interested) mediator from the faithful (k=0) gate.

    Draws n interested triads and n faithful triads, scores each by its W<->C peak prominence, and
    computes the rank AUC of separating interested from faithful. The faithful class is the same AND
    gate every time; the noise in its trajectory is the only source of spread, which is the right
    null: the faithful gate is one fixed structure, and the question is whether the interested gate's
    traces sit apart from it. Returns (auc, n_pos, n_neg).
    """
    rng = random.Random(seed)
    pos, neg = [], []   # pos = interested, neg = faithful
    interested = triad_rules(agenda, k_interested)
    faithful = triad_rules(agenda, 0)
    for i in range(n):
        pos.append(_wc_peak_prominence(interested, steps, random.Random(7000 + i), flip, max_lag))
        neg.append(_wc_peak_prominence(faithful, steps, random.Random(9000 + i), flip, max_lag))
    # AUC that an interested trace scores HIGHER than a faithful one. If the agenda makes the trace
    # less peaked, this sits below 0.5; the perceivability is |auc - 0.5| read as separation, but the
    # reported AUC is the discrimination AUC = max(auc, 1 - auc) so it is comparable to D1's 0.67.
    raw = sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))
    auc = max(raw, 1.0 - raw)
    return auc, len(pos), len(neg), raw


def _marginal_fit_error(tt, samples, rng):
    """Best-fit worker-marginal error: fit f(W) by majority over hidden C, score on the 4 states.

    tt is a length-4 truth table over (W, C) at index W + 2C. Returns the share of the 4 (W, C)
    states the majority-over-C predictor mispredicts.
    """
    seen = {0: [], 1: []}
    for _ in range(samples):
        w, c = rng.randint(0, 1), rng.randint(0, 1)
        seen[w].append(tt[w + 2 * c])
    fW = {w: (1 if sum(v) * 2 >= len(v) else 0) for w, v in seen.items()}
    wrong = sum(fW[w] != tt[w + 2 * c] for w in (0, 1) for c in (0, 1))
    return wrong / 4.0


def _mediator_tt(agenda, k):
    """The interested mediator at level k as a length-4 truth table over (W, C), index W + 2C."""
    f = mediator(agenda, k)
    return [f(w, c) for w in (0, 1) for c in (0, 1)]


def marginal_fit_error(k, agenda=1, trials=200, samples=200, seed=0):
    """Mean worker-marginal fit error at matched k for the interested mediator vs a random gate.

    Both have the counterpart C hidden. The interested mediator is the Q126 form at level k; the
    random gate is a strict gate matched only on k by overriding k of its 4 states toward the same
    agenda value, so the two differ only in WHICH states carry the agenda and what the baseline is.
    Returns (err_interested, err_random_gate).
    """
    rng = random.Random(seed)
    med_tt = _mediator_tt(agenda, k)
    err_med = err_rand = 0.0
    for _ in range(trials):
        # a random strict gate, then push k of its entries to the agenda value (matched k overrides)
        gate = _rand_strict_tt(rng)
        idx = list(range(4))
        rng.shuffle(idx)
        for j in idx[:k]:
            gate[j] = agenda
        err_med += _marginal_fit_error(med_tt, samples, rng)
        err_rand += _marginal_fit_error(gate, samples, rng)
    return err_med / trials, err_rand / trials


if __name__ == "__main__":
    auc, npos, nneg, raw = interested_vs_faithful_auc()
    print(f"interested-vs-faithful AUC = {auc:.2f}  (raw {raw:.2f}, n+={npos} n-={nneg})")
    print(f"triadic-detection AUC (D1 control) = {TRIADIC_DETECTION_AUC:.2f}")
    for k in range(5):
        em, er = marginal_fit_error(k)
        print(f"k={k}: marginal fit error  interested={em:.3f}  random-gate={er:.3f}")
