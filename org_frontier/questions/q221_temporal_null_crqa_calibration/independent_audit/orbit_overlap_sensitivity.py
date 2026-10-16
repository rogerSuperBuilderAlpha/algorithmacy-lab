"""POST-HOC orbit-overlap sensitivity audit for the 600-pair Q221 follow-up.

Uses only committed pair identities and classifier outcomes; does not rerun the
simulation and DOES NOT replace the preregistered finite-population Wilson rule.

Connected components of the observed orbit-pair incidence graph are resampled
as a deliberately conservative *diagnostic* for superpopulation dependence.
The resulting percentile ranges are NOT calibrated design-based CIs: clusters
are constructed from the observed sample graph, not sampled as independent
population units.

Run:
python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.orbit_overlap_sensitivity
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "confirmatory_4node" / "results"
DRAWS = 12000
SEED = 22155013


class XorShift32:
    def __init__(self, seed=SEED):
        self.state = seed & 0xFFFFFFFF
        if not self.state:
            raise ValueError("seed must be nonzero")

    def index(self, n):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= x >> 17
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x & 0xFFFFFFFF
        return (self.state * n) >> 32


def percentile(sample, pct):
    ordered = sorted(sample)
    return ordered[int(pct * (len(ordered) - 1))]


def component_records(pairs, rows):
    assert len(pairs) == len(rows) == 600
    parent, size = {}, {}

    def find(x):
        if x not in parent:
            parent[x] = x
            size[x] = 1
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]

    for row in pairs:
        union(row["orbit_a"], row["orbit_b"])

    components = {}
    for q, row in enumerate(pairs):
        assert row["q"] == rows[q]["q"] == q
        key = find(row["orbit_a"])
        c = components.setdefault(key, {"n": 0, "jr": 0, "sh": 0})
        c["n"] += 1
        c["jr"] += int(rows[q]["separates"]["C2_JRR"])
        c["sh"] += int(rows[q]["separates"]["C4_SHREC"])
    return list(components.values())


def audit(draws=DRAWS, seed=SEED):
    selected = json.loads((ROOT / "followup_pairs.json").read_text(encoding="utf-8"))["pairs"]
    outcomes = json.loads((ROOT / "followup.json").read_text(encoding="utf-8"))["pairs"]
    components = component_records(selected, outcomes)
    lengths = sorted((c["n"] for c in components), reverse=True)
    assert len(components) == 279
    assert lengths[0] == 34
    assert sum(c["n"] for c in components) == 600
    assert sum(c["jr"] for c in components) == 347
    assert sum(c["sh"] for c in components) == 363

    rng = XorShift32(seed)
    jr_samples, sh_samples, delta_samples = [], [], []
    for _ in range(draws):
        n = j = h = 0
        for _ in range(len(components)):
            c = components[rng.index(len(components))]
            n += c["n"]
            j += c["jr"]
            h += c["sh"]
        jr_samples.append(j / n)
        sh_samples.append(h / n)
        delta_samples.append((h - j) / n)

    def band(values):
        return [percentile(values, 0.025), percentile(values, 0.5), percentile(values, 0.975)]

    result = {
        "status": "POST-HOC HEURISTIC SENSITIVITY, NOT PREREGISTERED INFERENCE",
        "input_receipts": ["followup_pairs.json", "followup.json"],
        "observed_orbit_graph_components": len(components),
        "components_with_single_pair": sum(c["n"] == 1 for c in components),
        "pairs_sharing_an_orbit_with_other_sampled_pairs":
            sum(c["n"] for c in components if c["n"] > 1),
        "largest_component_pairs": lengths[0],
        "point_rates": {"JR": 347 / 600, "SHREC": 363 / 600},
        "component_resample_seed": seed,
        "component_resample_iterations": draws,
        "component_resample_percentile_ranges_NOT_CONFIDENCE_INTERVALS":
            {"JR": band(jr_samples), "SHREC": band(sh_samples),
             "SHREC_minus_JR": band(delta_samples)},
        "largest_component_omitted": {
            "JR": min((347 - c["jr"]) / (600 - c["n"]) for c in components),
            "SHREC": min((363 - c["sh"]) / (600 - c["n"]) for c in components),
        },
        "limitations": [
            "The preregistered primary estimand is the finite population of 1832 orbit pairs, sampled without replacement.",
            "Observed-graph connected components are not independent design-sampled clusters.",
            "The component bootstrap is a heuristic stress test, not calibrated frequentist inference.",
            "Shared orbits do not imply reused trajectories: pair-specific seeds remain disjoint.",
            "Do not overturn or promote the frozen Wilson verdicts from this post-hoc calculation.",
        ],
    }
    return result


def main():
    result = audit()
    print("q221 orbit-overlap sensitivity audit: 600 pairs, 279 components, 34 max-size; JR 347, SHREC 363")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
