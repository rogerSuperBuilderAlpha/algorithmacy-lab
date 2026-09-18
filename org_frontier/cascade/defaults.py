"""Documented defaults for the margin cascade (do not drift silently)."""

# Lab default budget: call exact Φ on this fraction (top-B% by OOF |p−0.5|).
DEFAULT_B = 0.10

# Probe-125/131 cheap-feature panel (same order as residual studies).
DEFAULT_FEATURES = (
    "n_edges",
    "n_bidir",
    "strongly_connected",
    "syn_sum",
    "syn_min",
    "syn_max",
    "n_fixed",
    "n_reachable",
    "invertible",
    "max_period",
)

# RF protocol matching Probe-131 / residual studies.
RF_N_ESTIMATORS = 400
RF_RANDOM_STATE = 0
RF_CV = 5

# On-panel equivalent τ for n=4 unc at B=10% — prose/documentation only.
# Do NOT freeze this across panel sizes (margin_cascade_tau H2 REFUTED).
TAU_STAR_N4_B10 = 0.287565
