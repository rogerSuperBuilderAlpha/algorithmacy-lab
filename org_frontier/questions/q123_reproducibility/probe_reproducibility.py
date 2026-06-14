"""Probe Q123 (H1-H4) — is the verdict reproducible and config-invariant? (critical-review T6)

Pins the build, records the config, and tests the binary verdict's invariance across the contested config
knobs over the full 256-form family, plus the admissibility of alternative repertoire-distance measures.

Run:  ~/iit-playground/venv-4.0/bin/python -m \
      org_frontier.questions.q123_reproducibility.probe_reproducibility
"""

import csv
import os

from org_frontier.questions.q123_reproducibility import forms as F


def main():
    print("PROBE Q123 (H1-H4) — reproducibility and config-invariance of the verdict")
    print("=" * 78)
    cfg = F.live_config()
    print(f"  pinned build commit: {F.BUILD_COMMIT}")
    print(f"  live config: {cfg}")

    base = F.family_verdicts()
    n_tri = sum(v == "triadic" for v in base)
    print(f"  baseline: {n_tri}/256 triadic")

    d_cuts = F.disagreements(base, F.family_verdicts({"SYSTEM_CUTS": "CONCEPT_STYLE"}))
    d_short = F.disagreements(base, F.family_verdicts({"SHORTCIRCUIT_SIA": False}))
    d_par = F.disagreements(base, F.family_verdicts({"PARALLEL": True}))
    d_rerun = F.disagreements(base, F.family_verdicts())
    n_alt, n_nondegen, detail = F.alt_measure_admissibility()
    print(f"  verdict disagreements vs baseline (out of 256):")
    print(f"     SYSTEM_CUTS=CONCEPT_STYLE: {d_cuts}   SHORTCIRCUIT_SIA=False: {d_short}   "
          f"PARALLEL=True: {d_par}   rerun: {d_rerun}")
    print(f"  alternative repertoire measures: {n_alt} tested, {n_nondegen} admissible-and-nondegenerate")

    h1 = d_cuts == 0                                   # SYSTEM_CUTS (the flagged knob) does not move the verdict
    h2 = d_short == 0                                  # the SIA optimization does not move the verdict
    h3 = d_par == 0 and d_rerun == 0                   # deterministic and parallelism-invariant
    h4 = n_nondegen == 0                               # no alternative measure is admissible-and-nondegenerate
    print("=" * 78)
    print(f"  H1 SYSTEM_CUTS does not change the verdict (0/256):              {h1} ({d_cuts})")
    print(f"  H2 the SIA optimization does not change the verdict (0/256):     {h2} ({d_short})")
    print(f"  H3 the verdict is deterministic and parallelism-invariant:       {h3} "
          f"(par {d_par}, rerun {d_rerun})")
    print(f"  H4 no alternative repertoire measure is admissible+nondegenerate:{h4} ({n_nondegen})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "reproducibility.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["item", "value"])
        w.writerow(["build_commit", F.BUILD_COMMIT])
        for k, v in cfg.items():
            w.writerow([f"config.{k}", v])
        w.writerow(["disagree_system_cuts", d_cuts])
        w.writerow(["disagree_shortcircuit", d_short])
        w.writerow(["disagree_parallel", d_par])
        w.writerow(["disagree_rerun", d_rerun])
        w.writerow(["alt_measures_tested", n_alt])
        w.writerow(["alt_measures_admissible_nondegenerate", n_nondegen])
        for m, info in detail.items():
            w.writerow([f"alt.{m}", info])


if __name__ == "__main__":
    main()
