"""Independent read-only consistency checks on the recorded 4-node confirmatory results.

Post-outcome QA only. Does NOT change the preregistration, decision rules, scripts,
seed selection or raw numerical outcomes. Does not run PyPhi or simulate new data.

From repository root:
 python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.audit_4node_records
"""
import json
import math
from pathlib import Path
from statistics import mean, stdev

from scipy.stats import norm, t

Q221 = Path(__file__).resolve().parent.parent
REC = Q221 / "confirmatory_4node" / "results"


def wilson_lower(k, n, z):
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return mid - half


def check():
    screen = json.loads((REC / "screen4.json").read_text(encoding="utf-8"))
    study = json.loads((REC / "study4.json").read_text(encoding="utf-8"))
    pairs = sorted(screen["study_pairs"], key=lambda x: x["q"])
    outcomes = sorted(study["pairs"], key=lambda x: x["q"])

    assert screen["counts"]["systems"] == 322560
    assert screen["counts"]["orbit_pairs"] == 1872
    assert screen["v1_pass"] == 300
    assert screen["v2_pass"] == 40
    assert study["M"] == len(pairs) == len(outcomes) == 40
    assert [r["q"] for r in pairs] == [r["q"] for r in outcomes] == list(range(40))
    assert all(r["v2_profiles_equal"] and r["v2_tpm_differ"] and r["v2_non_isomorphic"] for r in pairs)

    # The orbit-pair sampling unit is not automatically an independent orbit.
    # For this exact registered sample, every one of the 80 orbit appearances
    # happens to be distinct, so no orbit is reused between evaluated pairs.
    ids = [orbit for r in pairs for orbit in (r["orbit_a"], r["orbit_b"])]
    assert len(set(ids)) == 80, "orbit overlap in current preregistered study sample"
    assert len({tuple(r["a"]) for r in pairs} | {tuple(r["b"]) for r in pairs}) == 80
    assert all(r["n_test"] == 400 for r in outcomes)

    classifiers = tuple(study["summary"])
    assert len(classifiers) == 7
    accuracy = [r["correct"]["R"] / r["n_test"] for r in outcomes]
    m = mean(accuracy)
    tcrit = t.ppf(0.95, 39)
    half = tcrit * stdev(accuracy) / math.sqrt(40)
    assert abs(m - study["H2"]["mean"]) < 1e-12
    assert abs(m - half - study["H2"]["ci90"][0]) < 1e-12
    assert abs(m + half - study["H2"]["ci90"][1]) < 1e-12
    assert 0.45 < m - half and m + half < 0.55 and study["H2"]["supported"]

    assert abs(study["z_pair"] - norm.ppf(1 - 0.05 / (7 * 40) / 2)) < 1e-12
    for key in classifiers:
        separated = 0
        accuracies = []
        for row in outcomes:
            k, n = row["correct"][key], row["n_test"]
            is_sep = wilson_lower(k, n, study["z_pair"]) > 0.5
            assert bool(row["separates"][key]) == is_sep
            separated += int(is_sep)
            accuracies.append(k / n)
        published = study["summary"][key]
        assert published["pairs_separated"] == separated
        assert published["M"] == len(outcomes)
        assert abs(published["mean_acc"] - mean(accuracies)) < 1e-12

    return m, m - half, m + half


def main():
    m, low, high = check()
    print(
        "q221 F4 record integrity: 40 orbit-disjoint pairs; 400 held-out "
        "trajectories each; 7 classifiers reproduced; "
        f"H2 mean={m:.7f}, CI90=[{low:.6f},{high:.6f}] PASS"
    )


if __name__ == "__main__":
    main()
