"""Lab-default margin cascade: cheap RF screen + selective exact IIT-4.0 Φ.

Default rule (from ``margin_cascade_phi`` / ``margin_cascade_tau``):
call exact Φ on the top **B=10%** of forms by smallest out-of-fold ``|p−0.5|``,
**recomputed per panel**. Do not freeze τ across panel sizes.

Warrant (cited, not reopened): size-series residual 4.8%→7.5%→9.0%; F28 phase
boundary; FN-feature redesign honest null; cascade WIN; τ-calibration → top-B%.
"""

from .core import (
    DEFAULT_B,
    DEFAULT_FEATURES,
    CascadeResult,
    margin_cascade,
    metrics_from_preds,
    oof_proba,
    top_b_mask,
)
from .defaults import TAU_STAR_N4_B10

__all__ = [
    "DEFAULT_B",
    "DEFAULT_FEATURES",
    "TAU_STAR_N4_B10",
    "CascadeResult",
    "margin_cascade",
    "metrics_from_preds",
    "oof_proba",
    "top_b_mask",
]
