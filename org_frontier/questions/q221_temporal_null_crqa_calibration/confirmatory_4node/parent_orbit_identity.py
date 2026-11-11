"""Independent, fast integrity check for the preregistered 40-pair parent study.

This is a post-hoc QA check on committed pair identities only, not an
amendment to the preregistration, sample, outcomes or decision rules.
Run: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.confirmatory_4node.parent_orbit_identity
"""
import json
from collections import Counter
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "results" / "screen4.json"
    record = json.loads(source.read_text(encoding="utf-8"))
    rows = record["study_pairs"]
    assert len(rows) == 40, "Unexpected number of parent study orbit pairs"
    keys = [tuple(sorted((int(p["orbit_a"]), int(p["orbit_b"])))) for p in rows]
    assert all(a != b for a, b in keys), "Self-pair in study"
    assert len(set(keys)) == len(keys), "Duplicate unordered orbit pair"
    counts = Counter(x for pair in keys for x in pair)
    reused = sum(v > 1 for v in counts.values())
    assert (len(counts), reused, max(counts.values())) == (80, 0, 1), (
        "Selected network-orbit overlap detected"
    )
    print("q221 parent pair identity: 40 distinct pairs; 80 distinct orbits; 0 shared orbits")


if __name__ == "__main__":
    main()
