"""best_time_themes — the values carried by four ChatGPT answers to one prompt.

The first study (best_time_pilot) read the four answers for wording and which eras they name. This study reads
them for values. Three coders, blind to the hypothesis and to each other, rated each answer on five value axes
(progress, equity_critique, value_base, geo_frame, epistemic) and two framing flags (hedge_then_commit,
equity_placement); see data/CODEBOOK.md. The median-of-three coding is frozen in data/values_coding.csv, the
raw coder scores in data/coder_raw.csv.

The analysis tests whether the four answers carry a consistent, directional worldview, whether the push is
overt or subtle (hedge then commit), and where the values genuinely diverge. Inter-coder reliability is the
gate: a slant independent readers do not converge on is not in the text.

Pre-registered gate + H1-H5 are in HYPOTHESES.md, fixed before any coding. N=4 responses, 3 coders: every test
is descriptive, none powered. The interpretation boundary (consistent lean is structure, not proven "nudging")
is fixed in HYPOTHESES.md and FINDINGS.md.

Run:  python org_frontier/llm_variance/best_time_themes/analyze_themes.py
"""

import os
import sys
import itertools

import numpy as np
import pandas as pd

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

_HERE = os.path.dirname(__file__)
DATA = os.path.join(_HERE, "data")

AXES = ("progress", "equity_critique", "value_base", "geo_frame", "epistemic")
IDS = ("r1", "r2", "r3", "r4")
RELIABILITY_FLOOR = 0.50


def load_raw():
    df = pd.read_csv(os.path.join(DATA, "coder_raw.csv"))
    coders = sorted(df["coder"].unique())
    mats = {}
    for c in coders:
        sub = df[df["coder"] == c].set_index("response_id")
        mats[c] = sub.reindex(index=list(IDS))[list(AXES)].to_numpy(dtype=float)
    return coders, mats


def load_coding():
    df = pd.read_csv(os.path.join(DATA, "values_coding.csv")).set_index("response_id").reindex(index=list(IDS))
    return df


def reliability(mats):
    """Mean pairwise Pearson across coders over the value-axis cells."""
    vecs = {c: m.flatten() for c, m in mats.items()}
    cors = []
    for a, b in itertools.combinations(sorted(vecs), 2):
        cors.append(float(np.corrcoef(vecs[a], vecs[b])[0, 1]))
    return float(np.mean(cors)), cors


def sign_agree(vals):
    v = np.asarray(vals, dtype=float)
    return bool(np.all(v > 0) or np.all(v < 0))


def main():
    print("LLM_VARIANCE — best-time themes: the values in four answers")
    print("=" * 73)
    coders, mats = load_raw()
    coding = load_coding()
    print("  n responses: %d   coders: %d   axes: %s" % (len(IDS), len(coders), ", ".join(AXES)))

    # ---- gate: inter-coder reliability ----
    rel, cors = reliability(mats)
    gate = rel >= RELIABILITY_FLOOR
    print("  GATE inter-coder reliability: mean pairwise r=%.3f (floor %.2f): %s"
          % (rel, RELIABILITY_FLOOR, "PASS" if gate else "FAIL"))
    assert gate, "inter-coder reliability below floor; no value verdict trusted"

    # ---- per-axis means and sign-agreement (on median coding) ----
    print("  per-axis (median-of-3): mean and sign-agreement")
    axis_mean, axis_agree = {}, {}
    for ax in AXES:
        vals = coding[ax].to_numpy(dtype=float)
        axis_mean[ax] = float(vals.mean())
        axis_agree[ax] = sign_agree(vals)
        note = ""
        if ax == "progress" and axis_agree[ax]:
            note = "  (all four progressivist)"
        if ax == "value_base" and axis_agree[ax]:
            note = "  (all four material)"
        if not axis_agree[ax]:
            note = "  (divergent axis)"
        print("    %-15s mean=%+.2f  sign_agree=%s%s"
              % (ax, axis_mean[ax], "yes" if axis_agree[ax] else "no", note))

    hedge = coding["hedge_then_commit"].to_numpy(dtype=int)
    place = coding["equity_placement"].to_numpy(dtype=int)
    equity = coding["equity_critique"].to_numpy(dtype=float)
    n_hedge = int((hedge == 1).sum())
    equity_present = int((equity != 0).sum())
    print("  hedge_then_commit: %d/4 responses ; equity caveat present: %d/4 (mean placement %.1f)"
          % (n_hedge, equity_present, place.mean()))

    consensus = [ax for ax in AXES if axis_agree[ax]]
    divergent = [ax for ax in AXES if not axis_agree[ax]]
    print("  consensus axes (sign-agree): %d of 5 ; divergent axis: %s"
          % (len(consensus), ", ".join(divergent) if divergent else "none"))

    # value-profile collapse: distinct median value-vectors among the four responses
    profiles = [tuple(coding.loc[r, list(AXES)].astype(int)) for r in IDS]
    uniq = sorted(set(profiles))
    counts = {p: profiles.count(p) for p in uniq}
    majority = max(counts, key=counts.get)
    diff_ids = [IDS[i] for i, p in enumerate(profiles) if p != majority]
    diff_axes = []
    if diff_ids:
        maj = np.array(majority)
        for did in diff_ids:
            pv = np.array(tuple(coding.loc[did, list(AXES)].astype(int)))
            diff_axes = [AXES[k] for k in range(len(AXES)) if pv[k] != maj[k]]
    print("  worldview collapse: distinct value profiles=%d of 4 (%s share one; %s differs on %s)"
          % (len(uniq),
             "=".join([IDS[i] for i, p in enumerate(profiles) if p == majority]),
             ",".join(diff_ids) if diff_ids else "none",
             ",".join(diff_axes) if diff_axes else "none"))

    # exact two-sided sign-test for a 4/4 one-sign axis under random +/- (p=0.5)
    p_sign = 2 * (0.5 ** 4)
    print("  sign-test per consensus axis: p=%.3f (4/4 one sign); low power at N=4, axes not independent"
          % p_sign)

    h1 = axis_agree["progress"] and axis_mean["progress"] >= 1.0
    h2 = int((equity != 0).sum()) == 4 and int((equity > 0).sum()) >= 3
    h3 = n_hedge == 4 and axis_mean["epistemic"] > 0.0
    h4 = len(consensus) >= 3
    h5 = 1 <= len(divergent) <= 4

    print("=" * 73)
    print("  H1 (consistent progress lean: sign-agree and mean >= +1.0): %s" % _v(h1))
    print("  H2 (progress travels with equity caveat: all nonzero, >=3 positive): %s" % _v(h2))
    print("  H3 (subtle nudge: hedge_then_commit 4/4 and mean epistemic > 0): %s" % _v(h3))
    print("  H4 (one worldview: sign-agree on >= 3 of 5 axes): %s" % _v(h4))
    print("  H5 (genuine divergence on >=1 but not all axes): %s" % _v(h5))
    print("=" * 73)


def _v(b):
    return "SUPPORTED" if b else "REFUTED"


if __name__ == "__main__":
    main()
