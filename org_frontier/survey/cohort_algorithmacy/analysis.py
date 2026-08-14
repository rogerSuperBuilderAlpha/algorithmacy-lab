"""The cohort-algorithmacy analysis pipeline — runnable now on simulated data, completed with real waves.

This scaffolds the pre-registered analysis (analysis_plan.md) so a researcher can see the pipeline and
its outputs before fielding a single wave, then point it at the real response files. It runs on a
simulated cohort that carries the structure the hypotheses predict — three correlated facets, a positive
growth slope, and a positive association between algorithmacy and perceived system authority — so the
scaffold demonstrates recovering them. It computes facet scores, Cronbach's α per facet, the inter-facet
correlations (the three-factor signal of RQ1), the wave-to-wave growth (RQ2), and the algorithmacy-by-
system-authority association (RQ3 / H3b).

The confirmatory parts of the plan — exploratory and confirmatory factor analysis, McDonald's ω with
bootstrap intervals, longitudinal invariance, and the latent growth model — need a structural-equation
package (semopy, lavaan via rpy2, or statsmodels) the researcher installs and runs on the real data; this
scaffold marks where each goes. To run on real data, write `wave{1,2,3}.csv` with one row per respondent
and the item columns from codebook.md, place them beside this file, and the loader uses them instead of
the simulation.

Run from the repo root:
    PYTHONPATH=. python org_frontier/survey/cohort_algorithmacy/analysis.py
"""

import os

import numpy as np
import pandas as pd

HERE = os.path.dirname(__file__)
FACETS = {
    "ACS-CI": ["acs_ci_1", "acs_ci_2", "acs_ci_3", "acs_ci_4"],
    "ACS-SC": ["acs_sc_1", "acs_sc_2", "acs_sc_3", "acs_sc_4"],
    "ACS-RT": ["acs_rt_1", "acs_rt_2", "acs_rt_3", "acs_rt_4"],
}
ITEMS = [i for items in FACETS.values() for i in items]

# Zhou et al. (2025) algorithmic competency, adapted — the discriminant rival (H4). W2 only.
ZAC_FACETS = {
    "ZAC-UN": ["zac_un_1", "zac_un_2", "zac_un_3"],
    "ZAC-RM": ["zac_rm_1", "zac_rm_2", "zac_rm_3"],
    "ZAC-LV": ["zac_lv_1", "zac_lv_2", "zac_lv_3"],
    "ZAC-EM": ["zac_em_1", "zac_em_2", "zac_em_3"],
}
ZAC_ITEMS = [i for items in ZAC_FACETS.values() for i in items]
# Which algorithmacy facet each ZAC facet is predicted to track most closely (pre-registered, H4).
ZAC_EXPECTED = {"ZAC-UN": "ACS-CI", "ZAC-LV": "ACS-SC", "ZAC-RM": None, "ZAC-EM": None}


def simulate_wave(n, wave, rng):
    """A synthetic wave carrying the predicted structure: three correlated facet factors on a 7-point
    scale, a small positive growth with wave, and a system-authority covariate tied to algorithmacy."""
    # latent facet factors, correlated (the three-factor-but-related structure of RQ1)
    base = rng.normal(0, 1, n)
    facet_latent = {f: 0.6 * base + 0.8 * rng.normal(0, 1, n) for f in FACETS}
    growth = 0.20 * wave   # positive slope (RQ2 / H2)
    cols = {}
    for f, items in FACETS.items():
        for it in items:
            v = 4.0 + 0.9 * facet_latent[f] + growth + rng.normal(0, 0.7, n)
            cols[it] = np.clip(np.round(v), 1, 7)
    # perceived system authority (commit), correlated with the algorithmacy latent (RQ3 / H3b)
    cols["sys_authority_commit"] = np.clip(np.round(4.0 + 0.5 * base + rng.normal(0, 1.0, n)), 1, 7)
    # the discriminant rival, fielded at W2 only. Simulated under H4 as registered: related but
    # separable — Understanding tracks counterpart inference, Leveraging tracks signal compression,
    # Embracing is an attitude with no algorithmacy counterpart and so loads on its own latent.
    if wave == 2:
        attitude = rng.normal(0, 1, n)
        zac_latent = {
            "ZAC-UN": 0.55 * facet_latent["ACS-CI"] + 0.85 * rng.normal(0, 1, n),
            "ZAC-LV": 0.55 * facet_latent["ACS-SC"] + 0.85 * rng.normal(0, 1, n),
            "ZAC-RM": 0.30 * base + 0.95 * rng.normal(0, 1, n),
            "ZAC-EM": attitude,
        }
        for f, items in ZAC_FACETS.items():
            for it in items:
                v = 4.0 + 0.9 * zac_latent[f] + rng.normal(0, 0.7, n)
                cols[it] = np.clip(np.round(v), 1, 7)
    return pd.DataFrame(cols)


def load_or_simulate():
    waves = []
    for w in (1, 2, 3):
        path = os.path.join(HERE, f"wave{w}.csv")
        if os.path.exists(path):
            waves.append(pd.read_csv(path))
        else:
            waves.append(None)
    if all(w is not None for w in waves):
        print("loaded real wave files wave{1,2,3}.csv")
        return waves
    print("no wave files found — running the pipeline on a SIMULATED cohort (replace with real data)")
    rng = np.random.RandomState(0)
    return [simulate_wave(120, w, rng) for w in (1, 2, 3)]


def cronbach_alpha(df, items):
    x = df[items].to_numpy(float)
    k = x.shape[1]
    item_var = x.var(axis=0, ddof=1).sum()
    total_var = x.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - item_var / total_var)


def facet_scores(df):
    s = pd.DataFrame({f: df[items].mean(axis=1) for f, items in FACETS.items()})
    s["ACS-total"] = df[ITEMS].mean(axis=1)
    return s


def main():
    waves = load_or_simulate()
    scores = [facet_scores(w) for w in waves]

    print("\nRQ1 reliability (Cronbach's α per facet per wave; ω with CIs is the pre-registered primary, needs a SEM package):")
    for wi, w in enumerate(waves, 1):
        a = "  ".join(f"{f} {cronbach_alpha(w, items):.2f}" for f, items in FACETS.items())
        print(f"  wave {wi}: {a}")

    print("\nRQ1 three-factor signal (inter-facet correlations at wave 2; distinct but related):")
    corr = scores[1][list(FACETS)].corr()
    for f in FACETS:
        print(f"  {f}: " + "  ".join(f"{g} {corr.loc[f, g]:+.2f}" for g in FACETS))
    print("  [full EFA at W1 + CFA of the 3-factor vs 1-factor model at W2/W3 is the pre-registered test]")

    print("\nRQ2 growth (mean facet/total across waves; the latent growth slope is the pre-registered test):")
    for col in list(FACETS) + ["ACS-total"]:
        means = [s[col].mean() for s in scores]
        print(f"  {col}: W1 {means[0]:.2f} -> W2 {means[1]:.2f} -> W3 {means[2]:.2f}  (Δ {means[2]-means[0]:+.2f})")

    print("\nRQ3 / H3b association (algorithmacy total by perceived system authority-commit, wave 2):")
    df2 = waves[1].assign(acs=scores[1]["ACS-total"])
    r = df2[["acs", "sys_authority_commit"]].corr().iloc[0, 1]
    print(f"  r(ACS total, system-authority commit) = {r:+.2f}  [the formal prediction: positive under commit]")
    print("  [the pre-registered test is a multilevel fixed effect with self-efficacy controlled; see survey_bridge.md]")

    if all(c in waves[1].columns for c in ZAC_ITEMS):
        w2 = waves[1]
        zac = pd.DataFrame({f: w2[items].mean(axis=1) for f, items in ZAC_FACETS.items()})
        zac["ZAC-total"] = w2[ZAC_ITEMS].mean(axis=1)
        print("\nH4 discriminant vs Zhou et al. 2025 (wave 2; the pre-registered test is a two-factor")
        print("second-order CFA with the latent correlation < .85 — this is the observed-score preview):")
        a = "  ".join(f"{f} {cronbach_alpha(w2, items):.2f}" for f, items in ZAC_FACETS.items())
        print(f"  ZAC reliability: {a}")
        r_total = pd.concat([scores[1]["ACS-total"], zac["ZAC-total"]], axis=1).corr().iloc[0, 1]
        print(f"  r(ACS total, ZAC total) = {r_total:+.2f}  [≥ .85 at the latent level would falsify H4]")
        print("  facet correlations (predicted partner marked *):")
        for zf in ZAC_FACETS:
            row = "  ".join(
                f"{af} {pd.concat([zac[zf], scores[1][af]], axis=1).corr().iloc[0, 1]:+.2f}"
                f"{'*' if ZAC_EXPECTED[zf] == af else ' '}"
                for af in FACETS
            )
            print(f"    {zf}: {row}")
        print("  [ZAC-EM is predicted to correlate weakly with every facet — it measures an attitude]")


if __name__ == "__main__":
    main()
