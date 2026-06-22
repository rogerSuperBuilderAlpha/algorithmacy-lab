"""Run one coordination through both recurrence instruments — runnable now on a bundled example.

This is the end-to-end scaffold a recurrence study instantiates (see README.md). It runs the paired
reading on a bundled committing-triad example, so a researcher sees the machinery and its outputs before
encoding a single real series, then swaps in the encoded series and the elicited Boolean model. Cross-
recurrence reads the behavior of one run and needs no model; exact Φ reads the structure of the model.
The cross-recurrence half runs on numpy alone; the Φ half needs the PyPhi venv, and the scaffold runs the
behavioral half and says where the structural half goes when the venv is absent.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/recurrence/packets/template/run_study.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence import crqa

# The Φ half needs PyPhi; degrade gracefully when the venv is absent.
try:
    from org_frontier.threads.mediation_boundary._probe import probe
    _HAVE_PHI = True
except Exception as _e:   # pyphi not installed
    _HAVE_PHI = False
    _PHI_ERR = _e

# ---------------------------------------------------------------------------------------------
# The bundled example: a committing triad. REPLACE the model and the series with your own.
#   parties D (a worker), S (the apparatus), R (a counterpart).
#   S commits a determination reading both parties (S = D & R); each party acts on the commit.
# Node order in the tuple: 0 = D, 1 = S, 2 = R.
# ---------------------------------------------------------------------------------------------
LABELS = ("D", "S", "R")
MODEL = [
    lambda x: x[1],          # D acts on the apparatus's commit (D <- S)
    lambda x: x[0] & x[2],   # S commits reading both parties (S = D & R)
    lambda x: x[1],          # R acts on the commit (R <- S)
]


def load_series():
    """Return the per-party binary series as columns of an array, one row per time step.

    The bundled example generates the series from MODEL as a stochastic trajectory. To run on real data,
    replace this with a loader for your encoded series — a CSV with one column per party and one row per
    time step, 1 active / 0 inactive (real_series/encode.py is the worked encoding step)."""
    rng = np.random.RandomState(0)
    return np.asarray(crqa.trajectory(MODEL, steps=400, rng=rng))


def behavioral(series):
    """Cross-recurrence on every pair of series — the behavioral reading, model-free."""
    print("=== the behavioral reading (cross-recurrence; no model) ===")
    n = series.shape[1]
    for i in range(n):
        for j in range(i + 1, n):
            x, y = series[:, i], series[:, j]
            m = crqa.crqa(x, y)
            lag, prom = crqa.peak(x, y)
            lead = LABELS[i] if lag > 0 else (LABELS[j] if lag < 0 else "synchronous")
            print(f"  {LABELS[i]}-{LABELS[j]}: RR {m['rr']:.2f}  DET {m['det']:.2f}  "
                  f"Lmean {m['lmean']:.1f}  peak lag {lag:+d} (prom {prom:+.2f}) -> leads: {lead}")
    print("  read: sustained tracking shows in DET and Lmean; the peak lag reads leader from follower")
    print("  when its prominence clears the binary recurrence floor.")


def structural():
    """Exact Φ on the model — the structural reading. Needs the PyPhi venv."""
    print("\n=== the structural reading (exact Φ on the model) ===")
    if not _HAVE_PHI:
        print(f"  [Φ half skipped: PyPhi not importable ({type(_PHI_ERR).__name__}). Install the venv from")
        print("   GETTING_STARTED.md, then re-run for the paired verdict.]")
        return
    dec = probe([lambda x: x[0], lambda x: x[1], lambda x: x[2]], LABELS)   # decoupled -> Φ 0
    cpl = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)   # coupled -> Φ > 0
    ok = dec["phi"] == 0.0 and cpl["phi"] > 0.0
    print(f"  controls: decoupled Φ={dec['phi']} (must be 0), coupled Φ={cpl['phi']} (must be >0) "
          f"-> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("  instrument failed — do not read the verdict"); return
    p = probe(MODEL, LABELS)
    print(f"  model verdict: {p['structure']}, Φ={p['phi']}, major complex={p['core']}")
    print("  read: a triadic verdict with the apparatus in the core is the committing form; a dyadic")
    print("  verdict (Φ_MIP=0) is the relay or the false dyad the behavioral half can still flag.")


def main():
    series = load_series()
    behavioral(series)
    structural()
    print("\nthe pairing: cross-recurrence reads the behavior of one run, Φ reads the structure of the")
    print("model. Agreement on the committing form, and the one place they part, is the study's result.")


if __name__ == "__main__":
    main()
