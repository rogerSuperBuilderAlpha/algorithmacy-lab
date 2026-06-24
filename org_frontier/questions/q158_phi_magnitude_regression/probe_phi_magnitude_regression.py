"""q158 — Do whole-system CRQA measures predict the magnitude of exact major-complex Φ?

QUESTION
    A form has a behavioral signature (whole-system CRQA measures read from a sampled run) and a
    structural ground truth (the exact major-complex Φ read from IIT-4.0). Earlier studies asked
    whether CRQA predicts the binary verdict. This one asks whether whole-system md_recurrence DET
    and recurrence rate predict the continuous magnitude of major-complex Φ across the corpus.

H1  md_recurrence DET correlates positively with major-complex Φ across the corpus and the random
    3- and 4-node ensembles, with Spearman rho above 0.4. Null: the correlation is not different
    from zero.

H2  The relationship saturates. Above a DET ceiling, Φ keeps rising with no further DET gain, so a
    linear DET->Φ fit underpredicts the high-Φ forms. Null: the DET-Φ relation is linear, with no
    systematic high-Φ residual.

METHOD
    Forms: the 3-node forms_library pooled with a random 3-node ensemble (rand_form) and a random
    4-node ensemble (rand_form4). For each form, x is whole-system md_recurrence DET (and RR is
    read for reference), y is the exact major-complex Φ. Forms with no irreducible complex (Φ <= 0)
    are dropped: they carry no magnitude to predict. Trajectory sampling is seeded per form, so the
    feature side reproduces byte-for-byte; exact Φ is deterministic.

    H1 reads the Spearman rho of DET against Φ over the pool. H2 fits an ordinary least-squares
    line Φ ~ DET, then compares the mean residual of the high-Φ forms (top Φ quartile) against the
    rest. A positive high-Φ residual mean means the line underpredicts the high-Φ forms, the
    signature of saturation: DET stops climbing while Φ keeps rising. The control compares the
    linear residual spread against a monotone (isotonic) fit; a smaller isotonic residual is the
    sign that the true relation bends.

    Control = the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels (W,S,C):
    verdict triadic, max_phi 2.0, full 3-node core, major-complex Φ 2.0.

    Every number is exact IIT-4.0 Φ on synthetic Boolean coordination forms. This is an in-silico
    study of the CRQA-to-Φ bridge, not a measurement of any field organization.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q158_phi_magnitude_regression.probe_phi_magnitude_regression
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from scipy.stats import spearmanr
from sklearn.isotonic import IsotonicRegression

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.corpus.forms_library import FORMS
from org_frontier.recurrence.crqa_experiments import rand_form
from org_frontier.recurrence.bridge_four import rand_form4, major_complex as major_complex_n
from org_frontier.recurrence.crqa_phi_bridge import whole_system_recurrence

# ---- fixed configuration (all RNG seeded so the run reproduces byte-for-byte) -------------
N_RAND3 = 120          # random 3-node forms drawn
N_RAND4 = 120          # random 4-node forms drawn
RAND3_SEED = 0
RAND4_SEED = 1
RHO_THRESHOLD = 0.4    # H1 threshold on Spearman rho

# trajectory seeds: a distinct fixed seed per pool member, so features are deterministic.
TRAJ_SEED_LIBRARY = 100    # forms_library member i -> 100 + i
TRAJ_SEED_RAND3 = 1000     # random 3-node form k -> 1000 + k
TRAJ_SEED_RAND4 = 2000     # random 4-node form k -> 2000 + k


def _build_pool():
    """The labeled pool: list of (det, rr, phi). Forms with Φ <= 0 are dropped."""
    pool = []
    # curated 3-node corpus
    for i, f in enumerate(FORMS):
        _core, phi = major_complex(f.rules, ("W", "S", "C"))
        if phi <= 0.0:
            continue
        det, rr = whole_system_recurrence(f.rules, TRAJ_SEED_LIBRARY + i)
        pool.append((det, rr, float(phi)))
    # random 3-node ensemble
    rng = random.Random(RAND3_SEED)
    for k in range(N_RAND3):
        rules = rand_form(rng)
        _core, phi = major_complex_n(rules, 3)
        if phi <= 0.0:
            continue
        det, rr = whole_system_recurrence(rules, TRAJ_SEED_RAND3 + k)
        pool.append((det, rr, float(phi)))
    # random 4-node ensemble
    rng = random.Random(RAND4_SEED)
    for k in range(N_RAND4):
        rules = rand_form4(rng)
        _core, phi = major_complex_n(rules, 4)
        if phi <= 0.0:
            continue
        det, rr = whole_system_recurrence(rules, TRAJ_SEED_RAND4 + k)
        pool.append((det, rr, float(phi)))
    return pool


def instrument_control():
    """Validate the machinery on the known worker-system-counterpart triad."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    labels = ("W", "S", "C")
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < 1e-6, v.max_phi
    assert set(core) == set(labels), core
    assert abs(phi - 2.0) < 1e-6, phi
    det, rr = whole_system_recurrence(rules, TRAJ_SEED_LIBRARY)
    assert np.isfinite(det) and np.isfinite(rr), (det, rr)
    print(
        f"CONTROL worker-system-counterpart triad: verdict={v.structure}, "
        f"max_phi={v.max_phi:.3f}, mc_phi={phi:.3f}, core={core}: PASS"
    )


def main():
    instrument_control()
    print("=" * 88)
    print("q158 — whole-system CRQA predicting the magnitude of major-complex Φ")
    print("=" * 88)

    pool = _build_pool()
    det = np.array([p[0] for p in pool], dtype=float)
    rr = np.array([p[1] for p in pool], dtype=float)
    phi = np.array([p[2] for p in pool], dtype=float)
    n = len(phi)

    rho_det, p_det = spearmanr(det, phi)
    rho_rr, p_rr = spearmanr(rr, phi)

    print(
        f"pool: n={n} forms with major-complex Φ > 0 "
        f"(Φ range {phi.min():.3f}–{phi.max():.3f}, median {np.median(phi):.3f})"
    )
    print("-" * 88)
    print(f"  {'x':<28}{'Spearman rho vs Φ':<22}{'p-value'}")
    print(f"  {'md_recurrence DET':<28}{rho_det:<22.4f}{p_det:.2e}")
    print(f"  {'whole-system RR':<28}{rho_rr:<22.4f}{p_rr:.2e}")
    print("-" * 88)

    # ---- H2: linear fit Φ ~ DET, high-Φ residual sign, isotonic comparison -------------
    slope, intercept = np.polyfit(det, phi, 1)
    lin_pred = slope * det + intercept
    lin_resid = phi - lin_pred

    q75 = np.quantile(phi, 0.75)
    hi = phi >= q75
    lo = ~hi
    hi_resid_mean = float(lin_resid[hi].mean())
    lo_resid_mean = float(lin_resid[lo].mean())

    iso = IsotonicRegression(increasing=True, out_of_bounds="clip")
    iso_pred = iso.fit_transform(det, phi)
    lin_rmse = float(np.sqrt(np.mean(lin_resid ** 2)))
    iso_rmse = float(np.sqrt(np.mean((phi - iso_pred) ** 2)))

    print(f"  linear fit Φ ~ DET: slope={slope:.4f}, intercept={intercept:.4f}")
    print(f"  {'high-Φ residual mean (top quartile)':<40}{hi_resid_mean:+.4f}")
    print(f"  {'rest residual mean':<40}{lo_resid_mean:+.4f}")
    print(f"  {'linear RMSE':<40}{lin_rmse:.4f}")
    print(f"  {'isotonic (monotone) RMSE':<40}{iso_rmse:.4f}")
    print("=" * 88)

    # ---- H1 -----------------------------------------------------------------------------
    h1_supported = (rho_det > RHO_THRESHOLD) and (p_det < 0.05)
    print(
        f"H1 summary: Spearman rho(DET, Φ) = {rho_det:.4f} "
        f"{'>' if rho_det > RHO_THRESHOLD else '<='} {RHO_THRESHOLD} "
        f"(p={p_det:.2e})."
    )
    # ---- H2 -----------------------------------------------------------------------------
    h2_supported = (hi_resid_mean > 0.0) and (hi_resid_mean > lo_resid_mean) and (iso_rmse < lin_rmse)
    print(
        f"H2 summary: high-Φ residual mean {hi_resid_mean:+.4f} "
        f"(rest {lo_resid_mean:+.4f}); isotonic RMSE {iso_rmse:.4f} "
        f"{'<' if iso_rmse < lin_rmse else '>='} linear RMSE {lin_rmse:.4f}."
    )
    print("=" * 88)

    print(
        "H1 DET correlates positively with major-complex Φ (rho>0.4): "
        + ("SUPPORTED" if h1_supported else "REFUTED")
    )
    print(
        "H2 the DET-Φ relation saturates (high-Φ underprediction): "
        + ("SUPPORTED" if h2_supported else "REFUTED")
    )


if __name__ == "__main__":
    main()
