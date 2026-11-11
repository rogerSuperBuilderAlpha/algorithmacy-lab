"""Independent read-only audit of preregistered Q221 follow-up receipts.

Validates pair disjointness, chunk aggregation, primary Wilson-Bonferroni
decisions, manipulation checks, and secondary agreement counts. Adds a
POST-HOC paired method comparison without changing the preregistered verdicts.

Run:
python -m org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node.audit_followup_receipts
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from statistics import NormalDist

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
M = 600
N_TEST = 400
Z_PAIR = NormalDist().inv_cdf(1 - 0.05 / (7 * 40) / 2)
Z_CLASS = NormalDist().inv_cdf(1 - 0.05 / 2 / 2)


def read(name):
    return json.loads((OUT / name).read_text(encoding="utf-8"))


def wilson(k, n, z):
    p = k / n
    z2 = z * z
    denominator = 1 + z2 / n
    mid = (p + z2 / (2 * n)) / denominator
    half = z * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / denominator
    return (mid - half, mid + half)


def paired_exact_pvalue(discordant_a, discordant_b):
    """Two-sided exact McNemar/binomial p-value; descriptive only."""
    n = discordant_a + discordant_b
    lo = min(discordant_a, discordant_b)
    probability = 2.0 ** (-n)
    tail = probability
    for k in range(lo):
        probability *= (n - k) / (k + 1)
        tail += probability
    return min(1.0, 2.0 * tail)


def audit():
    selected = read("followup_pairs.json")
    parent = read("screen4.json")
    summary = read("followup.json")
    assert summary["M"] == M
    assert selected["exact_checks_passed"] == M
    assert abs(summary["z_pair"] - Z_PAIR) < 1e-10
    assert abs(summary["z_cls"] - Z_CLASS) < 1e-10
    original = {(p["orbit_a"], p["orbit_b"]) for p in parent["study_pairs"]}
    proposed = selected["pairs"]
    assert len(original) == 40 and len(proposed) == M
    fresh_keys = [(p["orbit_a"], p["orbit_b"]) for p in proposed]
    assert len(set(fresh_keys)) == M
    assert not (set(fresh_keys) & original)
    assert [p["q"] for p in proposed] == list(range(M))
    for p in proposed:
        assert p["v_profiles_equal"] and p["v_tpm_differ"] and p["v_non_isomorphic"]

    parts = sorted(OUT.glob("followup_part_???_???.json"))
    assert len(parts) == 12
    raw = []
    for part in parts:
        raw.extend(json.loads(part.read_text(encoding="utf-8"))["pairs"])
    raw.sort(key=lambda row: row["q"])
    rows = summary["pairs"]
    assert len(rows) == M and [row["q"] for row in rows] == list(range(M))
    assert [row["q"] for row in raw] == list(range(M))
    for p, observed, src in zip(proposed, rows, raw):
        assert observed["a"] == p["a"] and observed["b"] == p["b"]
        assert observed["n_test"] == src["n_test"] == N_TEST
        for name in ("a", "b", "q", "correct", "exact_maxdiff", "n_test"):
            assert observed[name] == src[name]
        for method, correct in observed["correct"].items():
            assert isinstance(correct, int) and 0 <= correct <= N_TEST
            assert observed["separates"][method] == (wilson(correct, N_TEST, Z_PAIR)[0] > 0.5)

    counts = {method: sum(row["separates"][method] for row in rows)
              for method in ("R", "C0_likelihood", "C1_TE", "C1_TE_MM", "C2_JRR", "C4_SHREC")}
    assert counts["R"] == 1 and counts["C0_likelihood"] == M
    r_accuracy = sum(row["correct"]["R"] for row in rows) / (M * N_TEST)
    assert 0.45 <= r_accuracy <= 0.55
    assert summary["manipulation_checks_pass"] is True

    for method in ("C2_JRR", "C4_SHREC"):
        item = summary["summary"][method]
        k = counts[method]
        assert item["pairs_separated"] == k and item["M"] == M
        assert abs(item["prop"] - k / M) < 1e-12
        actual = wilson(k, M, Z_CLASS)
        assert max(abs(actual[i] - item["wilson_bonf2"][i]) for i in (0, 1)) < 1e-10
        verdict = "generally separates" if actual[0] > 0.5 else "generally fails" if actual[1] < 0.5 else "unresolved"
        assert item["verdict"] == verdict
        mean_accuracy = sum(row["correct"][method] for row in rows) / (M * N_TEST)
        assert abs(item["mean_acc"] - mean_accuracy) < 1e-10

    for method in ("C1_TE", "C1_TE_MM", "C2_JRR"):
        exact_key = "C1_TE" if "TE" in method else "C2_JRR"
        truth = [row["exact_maxdiff"][exact_key] > 1e-12 for row in rows]
        classified = [row["separates"][method] for row in rows]
        calc = {
            "exact_separates": sum(truth),
            "finite_separates": sum(classified),
            "agree": sum(a == b for a, b in zip(truth, classified)),
            "exact_only": sum(a and not b for a, b in zip(truth, classified)),
            "finite_only": sum(b and not a for a, b in zip(truth, classified)),
        }
        assert summary["secondary"][method] == calc

    both = sum(row["separates"]["C2_JRR"] and row["separates"]["C4_SHREC"] for row in rows)
    jr_only = sum(row["separates"]["C2_JRR"] and not row["separates"]["C4_SHREC"] for row in rows)
    shrec_only = sum(row["separates"]["C4_SHREC"] and not row["separates"]["C2_JRR"] for row in rows)
    neither = M - both - jr_only - shrec_only
    assert (both, jr_only, shrec_only, neither) == (231, 116, 132, 121)
    return {
        "M": M, "parts": len(parts), "parent_overlaps": 0,
        "JR": counts["C2_JRR"], "SHREC": counts["C4_SHREC"],
        "R": counts["R"], "C0": counts["C0_likelihood"],
        "paired": (both, jr_only, shrec_only, neither),
        "posthoc_exact_mcnemar_p": paired_exact_pvalue(jr_only, shrec_only),
        "posthoc_separation_fraction_difference": (shrec_only - jr_only) / M,
    }


def main():
    r = audit()
    print("q221 followup receipts PASS: 600 pairs, 12 parts, 0 parent overlaps; JR=347, SHREC=363; R=1, C0=600")
    print("paired JR/SHREC: both=231 JR_only=116 SHREC_only=132 neither=121")
    print(f"POST-HOC difference SHREC-JR: {r['posthoc_separation_fraction_difference']:+.4f}; exact McNemar p={r['posthoc_exact_mcnemar_p']:.4f} (not a preregistered claim)")


if __name__ == "__main__":
    main()
