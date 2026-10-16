"""Post-hoc design-based concentration bound for Q221 4-node follow-up.

Uses only committed pair identities and binary method decisions, no simulation.
Does NOT replace the registered Wilson tests or provide superpopulation inference.
Run from repo root:
python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.finite_population_tail_bound
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIRS = ROOT / "confirmatory_4node" / "results" / "followup_pairs.json"
RESULTS = ROOT / "confirmatory_4node" / "results" / "followup.json"
POPULATION_SIZE = 1832
METHODS = ("C2_JRR", "C4_SHREC")


def bound(k, n, null_mean=0.5):
    """Finite-pair-population one-sided Chernoff bound under SRSWOR."""
    p = k / n
    if p <= null_mean:
        return 1.0
    divergence = p * math.log(p / null_mean)
    if p < 1:
        divergence += (1 - p) * math.log((1 - p) / (1 - null_mean))
    return math.exp(-n * divergence)


def audit():
    chosen = json.loads(PAIRS.read_text(encoding="utf-8"))["pairs"]
    outcome = json.loads(RESULTS.read_text(encoding="utf-8"))
    rows = outcome["pairs"]
    assert len(chosen) == len(rows) == 600 < POPULATION_SIZE
    assert [int(x["q"]) for x in chosen] == list(range(600))
    assert [int(x["q"]) for x in rows] == list(range(600))
    pair_ids = [tuple(sorted((int(x["orbit_a"]), int(x["orbit_b"])))) for x in chosen]
    assert all(a != b for a, b in pair_ids)
    assert len(set(pair_ids)) == len(pair_ids)
    assert all(x["n_test"] == 400 for x in rows)
    assert all(chosen[i]["a"] == rows[i]["a"] and chosen[i]["b"] == rows[i]["b"] for i in range(600))
    counts = {m: sum(bool(r["separates"][m]) for r in rows) for m in METHODS}
    assert counts == {"C2_JRR": 347, "C4_SHREC": 363}
    assert all(outcome["summary"][m]["pairs_separated"] == counts[m] for m in METHODS)
    ans = {
        "status": "POST_HOC_DESIGN_SENSITIVITY_NOT_PREREGISTERED",
        "population": "1832 eligible orbit pairs not tested in parent study",
        "sample": 600,
        "sampling": "simple random sample without replacement",
        "conditional_simulation": "independent fresh seeds per sampled orbit pair assumed",
        "null": "finite-population average pair separation probability <= 0.5",
        "methods": {
            m: {
                "separated": counts[m],
                "total": len(rows),
                "fraction": counts[m] / len(rows),
                "one_sided_upper_tail_bound": bound(counts[m], len(rows)),
                "bonferroni_two_upper_bound": min(1.0, 2 * bound(counts[m], len(rows))),
            }
            for m in METHODS
        },
        "limits": [
            "Does not replace precommitted Wilson intervals or verdicts",
            "No inference to independent network-orbit superpopulations",
            "Assumes selection uniformly without replacement and pair-index simulation independence",
            "Bound concerns population mean probability of pair-specific separation events, not classifier accuracy",
        ],
    }
    return ans


def main():
    x = audit()
    for m in METHODS:
        r = x["methods"][m]
        print("%s %d/%d fraction %.6f one-sided<=%.9g bonf2<=%.9g" %
              (m, r["separated"], r["total"], r["fraction"],
               r["one_sided_upper_tail_bound"], r["bonferroni_two_upper_bound"]))
    print("design-based finite-pair audit PASS")


if __name__ == "__main__":
    main()
