"""Probe — Davis H5: the incomplete graph.

Question.  The path p –– o –– q, both lines negative, no p–q line. Clusterable (no cycles at all) with two
           consistent clusterings. Does it dissolve like the clusterable class, or bind like the lab's
           mediated triad?
Hypothesis. H5: ≥ 2 partitions at rest and fewer than three persons in the core.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_path   (~8 min)
"""

from org_frontier.thinkers.davis import forms as F


def main():
    print("Davis H5 — the negative path at k = 4")
    control = F.run_control()
    rec = F.evaluate_phi("path−−", 3, F.PATH_EDGES, (-1, -1), 4)
    a = len(rec["partitions"]) >= 2
    b = len(rec["core_persons"]) < 3
    print("  partitions at rest=%d (≥2: %s)   core persons=%s (<3: %s)" % (
        len(rec["partitions"]), a, "".join(rec["core_persons"]) or "-", b))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H5 (the incomplete clusterable graph has several clusterings and dissolves): %s" % status)
    F.save("probe_davis_path", {"control": control, "form": rec, "H5": status})


if __name__ == "__main__":
    main()
