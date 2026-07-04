"""Analysis for the reproducibility_signaling review: reliability + the three hypothesis tests.

    python3 -m org_frontier.reviews.reproducibility_signaling.run

Reads coding/ (independent coder JSONL) and literature/corpus.jsonl, writes results/frozen.json and
results/summary.json, and prints the per-hypothesis verdicts. Standard library only; uses the arm's
reusable reliability tooling.

  H1 — signaling is uncommon overall: the any-signal rate on the adjudicated dataset.
  H2 — signaling rose 2015-2025: any-signal rate by year period (2015-2019 vs 2020-2025).
  H3 — quantitative signals more than qualitative: any-signal rate by method_type.
"""

import json
import os
from collections import Counter, defaultdict

from org_frontier.reviews.lib import reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["open_data", "code_available", "preregistered", "method_type"]
SIGNALS = ["open_data", "code_available", "preregistered"]


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def any_signal(rec):
    return any(rec.get(v) == "yes" for v in SIGNALS)


def rate(records, pred):
    n = len(records)
    k = sum(1 for r in records if pred(r))
    return k, n, (k / n if n else 0.0)


def main():
    corpus = _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))
    year_of = {r["slug"]: r.get("year") for r in corpus}

    # --- reliability + adjudicated dataset ---
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))
    # Prefer the corpus year (authoritative) over the coded year.
    for r in frozen:
        r["year"] = year_of.get(r["slug"], r.get("year"))
    n = len(frozen)

    print("\n" + "=" * 70)

    # --- signaling rates per practice ---
    print("Signaling rates (adjudicated), each a lower bound (abstract-only coding):")
    per_signal = {}
    for v in SIGNALS:
        k, _, p = rate(frozen, lambda r, v=v: r.get(v) == "yes")
        per_signal[v] = {"yes": k, "n": n, "rate": round(p, 4)}
        print(f"  {v:16} {k:3}/{n}  {p:6.1%}")

    # --- H1: any signal overall ---
    ka, _, pa = rate(frozen, any_signal)
    print(f"\nH1 (uncommon overall): any-signal {ka}/{n} = {pa:.1%}  ->  "
          f"{'SUPPORTED' if pa < 0.5 else 'CHALLENGED'} (predicted minority)")

    # --- H2: by year period ---
    def period(y):
        return "2015-2019" if (y or 0) <= 2019 else "2020-2025"
    buckets = defaultdict(list)
    for r in frozen:
        buckets[period(r["year"])].append(r)
    by_period = {}
    print("\nH2 (rising over time): any-signal rate by period:")
    for per in ("2015-2019", "2020-2025"):
        k, m, p = rate(buckets[per], any_signal)
        by_period[per] = {"yes": k, "n": m, "rate": round(p, 4)}
        print(f"  {per}  {k:3}/{m}  {p:6.1%}")
    early = by_period["2015-2019"]["rate"]
    late = by_period["2020-2025"]["rate"]
    h2 = "SUPPORTED" if late > early else ("CHALLENGED" if late < early else "FLAT")
    print(f"  later > earlier ? {late:.1%} vs {early:.1%}  ->  {h2}")

    # by single year, for the trend table
    by_year = {}
    for y in sorted({r["year"] for r in frozen if r["year"]}):
        yr = [r for r in frozen if r["year"] == y]
        k, m, p = rate(yr, any_signal)
        by_year[y] = {"yes": k, "n": m, "rate": round(p, 4)}

    # --- H3: by method_type ---
    print("\nH3 (quantitative > qualitative): any-signal rate by method_type:")
    by_method = {}
    for mt in ("quantitative", "qualitative", "mixed", "conceptual"):
        grp = [r for r in frozen if r.get("method_type") == mt]
        if grp:
            k, m, p = rate(grp, any_signal)
            by_method[mt] = {"yes": k, "n": m, "rate": round(p, 4)}
            print(f"  {mt:13} {k:3}/{m}  {p:6.1%}")
    q = by_method.get("quantitative", {}).get("rate", 0.0)
    ql = by_method.get("qualitative", {}).get("rate", 0.0)
    h3 = "SUPPORTED" if q > ql else ("CHALLENGED" if q < ql else "FLAT")
    print(f"  quantitative > qualitative ? {q:.1%} vs {ql:.1%}  ->  {h3}")

    method_dist = dict(Counter(r.get("method_type") for r in frozen))

    summary = {
        "n": n,
        "per_signal": per_signal,
        "any_signal": {"yes": ka, "n": n, "rate": round(pa, 4)},
        "H1_verdict": "supported" if pa < 0.5 else "challenged",
        "by_period": by_period,
        "H2_verdict": h2.lower(),
        "by_year": {str(k): v for k, v in by_year.items()},
        "by_method": by_method,
        "method_dist": method_dist,
        "H3_verdict": h3.lower(),
    }
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print("\nwrote results/frozen.json, results/summary.json")


if __name__ == "__main__":
    main()
