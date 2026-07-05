"""H3 -- an honest boundary: where do the held-out errors concentrate?

Reads results/test_predictions.csv (written by extrapolate.py) and characterises the misclassified
large-n forms: by construction, by back-channel presence, and by the region of the exact Φ that
separates confident from borderline calls. The output is the deferral rule -- the region where the
cheap screen should hand off to exact Φ rather than trust its own call.

Run extrapolate.py first. Writes results/boundary.json.
"""

import json
import os

import numpy as np
import pandas as pd

_RESULTS = os.path.join(os.path.dirname(__file__), "results")
_PRED = os.path.join(_RESULTS, "test_predictions.csv")


def main():
    if not os.path.exists(_PRED):
        print("Run extrapolate.py first (results/test_predictions.csv missing).")
        return
    df = pd.read_csv(_PRED)
    errors = df[df["correct"] == 0]
    n_err = len(errors)
    report = {
        "n_test": int(len(df)),
        "n_errors": int(n_err),
        "accuracy": round(float(df["correct"].mean()), 4),
    }

    # By construction
    by_con = df.groupby("construction").agg(
        n=("correct", "size"), errors=("correct", lambda s: int((s == 0).sum()))).reset_index()
    report["errors_by_construction"] = {
        r["construction"]: {"n": int(r["n"]), "errors": int(r["errors"])}
        for _, r in by_con.iterrows()}

    # By back-channel
    report["errors_by_backchannel"] = {
        int(bc): {"n": int((df["has_backchannel"] == bc).sum()),
                  "errors": int(((df["has_backchannel"] == bc) & (df["correct"] == 0)).sum())}
        for bc in sorted(df["has_backchannel"].unique())}

    # The confidence / Φ-magnitude region of the errors: are they near-threshold?
    if n_err:
        report["error_phi_max"] = {
            "min": round(float(errors["phi_max"].min()), 4),
            "median": round(float(errors["phi_max"].median()), 4),
            "max": round(float(errors["phi_max"].max()), 4),
        }
        report["error_proba"] = {
            "min": round(float(errors["proba"].min()), 4),
            "median": round(float(errors["proba"].median()), 4),
            "max": round(float(errors["proba"].max()), 4),
        }
        # Missed triads (false negatives) vs false alarms (false positives)
        fn = errors[errors["triadic"] == 1]
        fp = errors[errors["triadic"] == 0]
        report["false_negatives_missed_triads"] = int(len(fn))
        report["false_positives_false_alarms"] = int(len(fp))
        report["error_form_ids"] = errors["form_id"].tolist()[:40]

    # Deferral rule: abstaining on a probability band around 0.5 removes what share of errors at
    # what coverage cost?
    for band in (0.15, 0.25):
        lo, hi = 0.5 - band, 0.5 + band
        abstain = (df["proba"] >= lo) & (df["proba"] <= hi)
        decided = df[~abstain]
        report[f"deferral_band_{band}"] = {
            "abstain_frac": round(float(abstain.mean()), 4),
            "accuracy_on_decided": round(float(decided["correct"].mean()), 4) if len(decided) else None,
            "errors_remaining": int((decided["correct"] == 0).sum()),
        }

    with open(os.path.join(_RESULTS, "boundary.json"), "w") as fh:
        json.dump(report, fh, indent=2)

    print("=" * 78)
    print("H3 -- BOUNDARY (held-out errors)")
    print("=" * 78)
    print(f"  held-out accuracy {report['accuracy']:.3f}  ({n_err} errors / {len(df)} forms)")
    if n_err:
        print(f"  missed triads (FN): {report['false_negatives_missed_triads']}   "
              f"false alarms (FP): {report['false_positives_false_alarms']}")
        print(f"  error Φ_max region: median {report['error_phi_max']['median']:.3f} "
              f"(min {report['error_phi_max']['min']:.3f}, max {report['error_phi_max']['max']:.3f})")
        print("  errors by construction:",
              {k: v["errors"] for k, v in report["errors_by_construction"].items() if v["errors"]})
        for band in (0.15, 0.25):
            d = report[f"deferral_band_{band}"]
            print(f"  defer |p-0.5|<{band}: abstain {d['abstain_frac']:.2f}, "
                  f"decided-accuracy {d['accuracy_on_decided']}, errors left {d['errors_remaining']}")
    print(f"  wrote {os.path.join(_RESULTS, 'boundary.json')}")


if __name__ == "__main__":
    main()
