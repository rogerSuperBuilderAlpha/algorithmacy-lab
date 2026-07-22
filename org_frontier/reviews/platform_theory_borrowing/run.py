"""Analysis for the platform_theory_borrowing review: reliability + the three hypothesis tests.

    python3 -m org_frontier.reviews.platform_theory_borrowing.run

Reads coding/ (independent coder JSONL) and literature/corpus.jsonl, writes results/frozen.json and
results/summary.json, and prints the per-hypothesis verdicts:

  H1 — parent-theory mix by period (pre-2015 vs 2015+): economics early, institutional/ecosystem late.
  H2 — borrowing-mode distribution (share apply).
  H3 — multi-theory rate (share yes).

Standard library only; uses the arm's reusable reliability tooling.
"""

import json
import os
from collections import Counter

from org_frontier.reviews.lib import reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["parent_theory", "borrowing_mode", "multi_theory"]
ECON = {"tce", "two_sided_market"}
ORGTHEORY = {"institutional", "ecosystem"}


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def _pct(part, whole):
    return f"{100 * part / whole:.0f}%" if whole else "n/a"


def _dist(counter, n):
    return {k: {"n": v, "pct": round(100 * v / n, 1)} for k, v in counter.most_common()}


def main():
    corpus = _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))
    year_of = {r["slug"]: r.get("year") for r in corpus}

    # --- reliability + adjudicated dataset ---
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))
    for r in frozen:
        r["year"] = r.get("year") or year_of.get(r["slug"])
    n = len(frozen)

    print("\n" + "=" * 72)

    # --- H1: parent-theory mix by period ---
    theory = Counter(r["parent_theory"] for r in frozen)
    early = [r for r in frozen if r["year"] and r["year"] < 2015]
    late = [r for r in frozen if r["year"] and r["year"] >= 2015]
    t_early = Counter(r["parent_theory"] for r in early)
    t_late = Counter(r["parent_theory"] for r in late)
    econ_early = sum(t_early[k] for k in ECON)
    econ_late = sum(t_late[k] for k in ECON)
    org_early = sum(t_early[k] for k in ORGTHEORY)
    org_late = sum(t_late[k] for k in ORGTHEORY)
    print(f"H1 (economics early, org theory late): n={n}; pre-2015={len(early)}, 2015+={len(late)}")
    print(f"   overall parent_theory: {dict(theory.most_common())}")
    print(f"   pre-2015: economics(tce+2sm)={econ_early}/{len(early)} ({_pct(econ_early,len(early))}); "
          f"inst+ecosystem={org_early}/{len(early)} ({_pct(org_early,len(early))})")
    print(f"   2015+  : economics(tce+2sm)={econ_late}/{len(late)} ({_pct(econ_late,len(late))}); "
          f"inst+ecosystem={org_late}/{len(late)} ({_pct(org_late,len(late))})")
    print(f"   pre-2015 mix: {dict(t_early.most_common())}")
    print(f"   2015+   mix: {dict(t_late.most_common())}")

    # --- H2: borrow-and-apply ---
    mode = Counter(r["borrowing_mode"] for r in frozen)
    apply_n = mode.get("apply", 0)
    print(f"\nH2 (borrow-and-apply): borrowing_mode {dict(mode.most_common())}; "
          f"apply {apply_n}/{n} ({_pct(apply_n,n)})")

    # --- H3: single-theory imports dominate ---
    multi = Counter(r["multi_theory"] for r in frozen)
    yes = multi.get("yes", 0)
    print(f"H3 (single-theory imports): multi_theory {dict(multi.most_common())}; "
          f"multi=yes {yes}/{n} ({_pct(yes,n)})")

    summary = {
        "n": n,
        "reliability_note": "Fleiss kappa printed above; see results/frozen.json for the adjudicated set",
        "parent_theory_overall": _dist(theory, n),
        "period": {
            "pre2015": {"n": len(early), "mix": _dist(t_early, len(early)) if early else {},
                        "economics": econ_early, "inst_ecosystem": org_early},
            "y2015plus": {"n": len(late), "mix": _dist(t_late, len(late)) if late else {},
                          "economics": econ_late, "inst_ecosystem": org_late},
        },
        "borrowing_mode": _dist(mode, n),
        "multi_theory": _dist(multi, n),
    }
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print("\nwrote results/frozen.json, results/summary.json")


if __name__ == "__main__":
    main()
