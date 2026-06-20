"""Categorical cross-recurrence quantification analysis, and a trajectory generator for the
lab's Boolean coordination models.

CRQA reads coordination from two observed time series. It compares every point of one series
against every point of the other, marks the pairs that match (recurrence), and quantifies the
pattern. This module implements the categorical case, where each series is a sequence of discrete
states and two points match when they are equal. The lab's parties hold Boolean states, so the
categorical case is the exact one: embedding dimension one, delay one, an exact-match radius. The
continuous case with phase-space embedding (Marwan et al. 2007) is the generalization the framework
note describes but does not need here.

The measures follow the standard set (Webber and Zbilut 1994; Marwan et al. 2007; Coco and Dale
2014): recurrence rate, determinism, mean and maximum diagonal line length, and the diagonal
cross-recurrence profile whose peak lag reads leader from follower.

Pairing with Phi: `trajectory` runs one of the lab's Boolean forms as a stochastic dynamical system,
so the same model yields an exact Phi verdict from its transition matrix and a CRQA reading from a
sampled run. The bridge demonstration in bridge_demo.py uses both on one model.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np


def trajectory(rules, steps, rng, flip=0.05, warmup=20):
    """A run of a Boolean form as a stochastic dynamical system.

    From a random start, each step sets every node to its rule's value on the current global state,
    then flips each node independently with probability `flip`. The noise keeps the run exploring
    rather than collapsing into a short limit cycle, which is what a real coordination produces and
    what CRQA needs to see. Returns an array of shape (steps, n): column j is node j's series.
    """
    n = len(rules)
    state = tuple(int(rng.random() < 0.5) for _ in range(n))
    out = []
    for t in range(warmup + steps):
        nxt = [int(rules[j](state)) for j in range(n)]
        for j in range(n):
            if rng.random() < flip:
                nxt[j] ^= 1
        state = tuple(nxt)
        if t >= warmup:
            out.append(state)
    return np.array(out, dtype=int)


def cross_recurrence_matrix(x, y):
    """The categorical cross-recurrence matrix R, with R[i, j] = 1 when x[i] == y[j]."""
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()
    return (x[:, None] == y[None, :]).astype(int)


def _diagonal_lines(R):
    """Lengths of every maximal run of 1s along a diagonal (constant j - i) of R."""
    nx, ny = R.shape
    lengths = []
    for k in range(-(nx - 1), ny):
        diag = np.diagonal(R, offset=k)
        run = 0
        for v in diag:
            if v:
                run += 1
            elif run:
                lengths.append(run)
                run = 0
        if run:
            lengths.append(run)
    return lengths


def crqa(x, y, minline=2):
    """The recurrence measures for two categorical series.

    Returns a dict with:
      rr    - recurrence rate: density of matching pairs, the gross degree of shared states.
      det   - determinism: fraction of recurrent points on diagonal lines of length >= minline,
              the part of the coupling that is sustained rather than coincidental.
      lmean - mean diagonal line length (lines >= minline): typical duration of a tracked episode.
      lmax  - longest diagonal line: the longest stretch the two series run in parallel.
    """
    R = cross_recurrence_matrix(x, y)
    total = int(R.sum())
    if total == 0:
        return {"rr": 0.0, "det": 0.0, "lmean": 0.0, "lmax": 0}
    lines = [L for L in _diagonal_lines(R) if L >= minline]
    on_lines = int(sum(lines))
    return {
        "rr": total / R.size,
        "det": on_lines / total,
        "lmean": float(np.mean(lines)) if lines else 0.0,
        "lmax": max(lines) if lines else 0,
    }


def dcrp(x, y, max_lag=20):
    """The diagonal cross-recurrence profile: recurrence rate by lag k = j - i.

    Returns (lags, profile). A peak at lag 0 is synchronous coupling. A peak at positive k means
    y's states recur k steps after x's, so x leads and y follows by k. The sign of the peak lag is
    the leader-follower read-out, the empirical analog of a directed read edge in the Boolean model.
    """
    R = cross_recurrence_matrix(x, y)
    lags = list(range(-max_lag, max_lag + 1))
    profile = []
    for k in lags:
        diag = np.diagonal(R, offset=k)
        profile.append(float(diag.mean()) if diag.size else 0.0)
    return np.array(lags), np.array(profile)


def peak_lag(x, y, max_lag=20):
    """The lag of the DCRP peak: >0 means x leads y, <0 means y leads x, 0 is synchronous."""
    lags, profile = dcrp(x, y, max_lag)
    return int(lags[int(np.argmax(profile))])


def peak(x, y, max_lag=20):
    """The DCRP peak as (lag, prominence), where prominence is the peak height above the profile's
    median. A directed coupling makes a sharp peak at a consistent lag, so prominence is high. Two
    series with no preferred lag give a flat profile, so prominence is near zero and the lag is not
    meaningful. Binary series sit near a 0.5 recurrence floor, so prominence, not the rate, separates
    a real lead-lag from chance."""
    lags, profile = dcrp(x, y, max_lag)
    i = int(np.argmax(profile))
    return int(lags[i]), float(profile[i] - np.median(profile))
