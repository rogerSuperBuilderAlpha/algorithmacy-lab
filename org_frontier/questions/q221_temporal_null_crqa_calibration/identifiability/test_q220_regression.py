"""Regression test: the repo's q220 pipeline must reproduce the saved intermediates for the lead pair exactly
(prominence, centrality, scores, raw-trajectory hash). Fast (<2 s)."""
import json

import numpy as np

from org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.q220_intermediates import OUT, compute


def test_q220_intermediates_reproduce():
    saved = json.load(open(OUT))
    now = json.loads(json.dumps(compute(), sort_keys=True))
    for nm in ("P", "Q"):
        for a, b in zip(saved[nm]["runs"], now[nm]["runs"]):
            assert a["traj_sha256"] == b["traj_sha256"]
            assert np.allclose(a["prom"], b["prom"], atol=1e-12, equal_nan=True)
            assert np.allclose(a["centrality"], b["centrality"], atol=1e-12, equal_nan=True)
            assert (a["score_own"], a["score_other"], a["no_evidence"]) == (b["score_own"], b["score_other"], b["no_evidence"])
