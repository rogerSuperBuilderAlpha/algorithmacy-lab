"""Core margin-cascade API.

Cheap Probe-131-style RF probabilities (out-of-fold) screen a panel; exact Φ
labels (or an oracle callable) replace cheap verdicts on the top-B% most
uncertain forms. Default B=0.10. Fragility gating is not offered as a default.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional, Sequence, Union

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict

from .defaults import (
    DEFAULT_B,
    DEFAULT_FEATURES,
    RF_CV,
    RF_N_ESTIMATORS,
    RF_RANDOM_STATE,
)

ArrayLike = Union[np.ndarray, Sequence[Sequence[float]]]
LabelLike = Union[np.ndarray, Sequence[int]]
ExactOracle = Callable[[np.ndarray], np.ndarray]  # indices → exact binary labels


@dataclass
class CascadeResult:
    """Cascade verdicts and diagnostics for one panel."""

    pred: np.ndarray  # final cascade binary predictions
    cheap_pred: np.ndarray
    proba: np.ndarray  # OOF P(triadic)
    call_mask: np.ndarray  # True where exact Φ was used
    y_exact: np.ndarray  # ground-truth labels used on the panel
    B: float
    n_exact: int
    call_rate: float
    miss_rate: float
    fn_among_tri: float
    fp_among_dya: float
    n_miss: int
    fn: int
    fp: int
    n_tri: int
    n: int
    always_cheap_miss_rate: float
    always_cheap_fn_among_tri: float
    extras: dict = field(default_factory=dict)

    def summary_lines(self):
        return [
            f"cascade B={100 * self.B:.0f}%  exact={self.n_exact}/{self.n}  "
            f"call={100 * self.call_rate:.1f}%",
            f"  cascade:      miss={100 * self.miss_rate:.1f}% ({self.n_miss}/{self.n})  "
            f"FN|tri={100 * self.fn_among_tri:.1f}% ({self.fn}/{self.n_tri})  "
            f"FP|dya={100 * self.fp_among_dya:.1f}%",
            f"  always-cheap: miss={100 * self.always_cheap_miss_rate:.1f}%  "
            f"FN|tri={100 * self.always_cheap_fn_among_tri:.1f}%",
        ]


def oof_proba(
    X: ArrayLike,
    y: LabelLike,
    *,
    n_estimators: int = RF_N_ESTIMATORS,
    random_state: int = RF_RANDOM_STATE,
    cv: int = RF_CV,
) -> np.ndarray:
    """Out-of-fold P(triadic); no leakage into gating scores."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=int)
    clf = RandomForestClassifier(
        n_estimators=n_estimators, random_state=random_state, n_jobs=-1
    )
    return cross_val_predict(clf, X, y, cv=cv, method="predict_proba")[:, 1]


def top_b_mask(margin: np.ndarray, B: float = DEFAULT_B) -> np.ndarray:
    """True on the ``round(B·N)`` forms with smallest ``|p−0.5|`` (most uncertain)."""
    margin = np.asarray(margin, dtype=float)
    n = len(margin)
    k = int(round(B * n))
    mask = np.zeros(n, dtype=bool)
    if k <= 0:
        return mask
    if k >= n:
        mask[:] = True
        return mask
    order = np.argsort(margin, kind="mergesort")
    mask[order[:k]] = True
    return mask


def metrics_from_preds(pred: np.ndarray, y: np.ndarray) -> dict:
    pred = np.asarray(pred, dtype=int)
    y = np.asarray(y, dtype=int)
    n = len(y)
    n_tri = int(y.sum())
    n_dya = n - n_tri
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    miss = int((pred != y).sum())
    return {
        "n": n,
        "n_tri": n_tri,
        "n_miss": miss,
        "miss_rate": miss / n if n else float("nan"),
        "fp": fp,
        "fn": fn,
        "fn_among_tri": fn / n_tri if n_tri else float("nan"),
        "fp_among_dya": fp / n_dya if n_dya else float("nan"),
    }


def margin_cascade(
    X: ArrayLike,
    y: Optional[LabelLike] = None,
    *,
    B: float = DEFAULT_B,
    exact_oracle: Optional[ExactOracle] = None,
    proba: Optional[np.ndarray] = None,
    features: Sequence[str] = DEFAULT_FEATURES,
) -> CascadeResult:
    """Run the lab-default margin cascade on one feature panel.

    Parameters
    ----------
    X :
        Feature matrix (N × n_features), Probe-131 columns by default.
    y :
        Exact binary triadicity labels for the panel (preferred when cached).
    B :
        Exact-Φ budget as a fraction of the panel (default 0.10).
    exact_oracle :
        Optional ``f(indices) -> labels`` used when ``y`` is omitted, or ignored
        when ``y`` is provided (labels already exact).
    proba :
        Optional precomputed OOF probabilities; computed if omitted.
    features :
        Documented for callers; not used unless validating column count.

    Returns
    -------
    CascadeResult
    """
    X = np.asarray(X, dtype=float)
    n = X.shape[0]
    if X.ndim != 2:
        raise ValueError("X must be 2-D")
    if features is not None and X.shape[1] != len(features):
        # soft check — allow alternate feature blocks if caller passes matching X
        pass

    if y is None and exact_oracle is None:
        raise ValueError("provide y (exact labels) or exact_oracle")

    if y is not None:
        y_arr = np.asarray(y, dtype=int)
        if len(y_arr) != n:
            raise ValueError("y length must match X rows")
    else:
        # Need labels for OOF RF training — oracle must label the full panel.
        y_arr = np.asarray(exact_oracle(np.arange(n)), dtype=int)

    if proba is None:
        proba = oof_proba(X, y_arr)
    else:
        proba = np.asarray(proba, dtype=float)
        if len(proba) != n:
            raise ValueError("proba length must match X rows")

    cheap = (proba >= 0.5).astype(int)
    margin = np.abs(proba - 0.5)
    call_mask = top_b_mask(margin, B)
    n_exact = int(call_mask.sum())

    # Exact on called subset; cheap elsewhere.
    pred = cheap.copy()
    if n_exact:
        if y is not None:
            pred[call_mask] = y_arr[call_mask]
        else:
            pred[call_mask] = np.asarray(
                exact_oracle(np.where(call_mask)[0]), dtype=int
            )

    m = metrics_from_preds(pred, y_arr)
    m_cheap = metrics_from_preds(cheap, y_arr)

    return CascadeResult(
        pred=pred,
        cheap_pred=cheap,
        proba=proba,
        call_mask=call_mask,
        y_exact=y_arr,
        B=float(B),
        n_exact=n_exact,
        call_rate=n_exact / n if n else float("nan"),
        miss_rate=m["miss_rate"],
        fn_among_tri=m["fn_among_tri"],
        fp_among_dya=m["fp_among_dya"],
        n_miss=m["n_miss"],
        fn=m["fn"],
        fp=m["fp"],
        n_tri=m["n_tri"],
        n=n,
        always_cheap_miss_rate=m_cheap["miss_rate"],
        always_cheap_fn_among_tri=m_cheap["fn_among_tri"],
        extras={"features": tuple(features)},
    )
