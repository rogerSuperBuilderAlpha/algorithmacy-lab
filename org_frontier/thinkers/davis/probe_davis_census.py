"""Probe — Davis H4: Theorem 1 on the complete four-person graph, and uniqueness.

Question.  Over all 64 sign patterns of K4 with four camps: do rest states exist exactly when no cycle has
           one negative line, does the triangle test suffice (Davis 1967: 183), and is the clustering unique?
Hypothesis. H4: rest ⇔ clusterable on all 64; triangle test = cycle test; one partition per clusterable
           pattern.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_census
"""

import itertools

from org_frontier.thinkers.davis import forms as F


def triangle_test(signs):
    for t in itertools.combinations(range(4), 3):
        es = [F.K4_EDGES.index(e) for e in F.K4_EDGES if set(e) <= set(t)]
        if sum(1 for e in es if signs[e] == -1) == 1:
            return False
    return True


def main():
    print("Davis H4 — the K4 census at k = 4 (dynamics only)")
    control = F.run_control()
    rows = []
    for signs in itertools.product((1, -1), repeat=6):
        r = F.dynamics(4, F.K4_EDGES, signs, 4)
        r["triangle_test"] = triangle_test(signs)
        r["n_negative"] = sum(1 for s in signs if s == -1)
        rows.append(r)
    agree = all((r["n_rest"] > 0) == r["clusterable"] for r in rows)
    tri = all(r["triangle_test"] == r["clusterable"] for r in rows)
    uniq = all(len(r["partitions"]) == 1 for r in rows if r["clusterable"])
    n_clus = sum(1 for r in rows if r["clusterable"])
    n_bal = sum(1 for r in rows if r["balanced"])
    n_all_rest = sum(1 for r in rows if r["clusterable"] and r["attractors_all_rest"])
    by_neg = {}
    for r in rows:
        d = by_neg.setdefault(r["n_negative"], [0, 0, 0])
        d[0] += 1
        d[1] += int(r["clusterable"])
        d[2] += int(r["balanced"])
    for k in sorted(by_neg):
        print("  %d negative lines: %2d patterns, %2d clusterable, %2d balanced" % (k, *by_neg[k]))
    print("  64 patterns: %d clusterable (%d balanced); rest⇔clusterable=%s  triangle=cycle test=%s  "
          "unique partition=%s  clusterable with every attractor at rest: %d/%d" % (
              n_clus, n_bal, agree, tri, uniq, n_all_rest, n_clus))
    if agree and tri and uniq:
        status = "CONFIRMED"
    elif agree:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H4 (Theorem 1 on K4; triangles decide; clustering unique): %s" % status)
    F.save("probe_davis_census", {"control": control, "rows": rows, "n_clusterable": n_clus,
                                  "n_balanced": n_bal, "H4": status})


if __name__ == "__main__":
    main()
