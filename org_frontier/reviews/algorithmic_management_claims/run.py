"""Analysis for the algorithmic_management_claims review: reliability + the three hypothesis tests.

    python3 -m org_frontier.reviews.algorithmic_management_claims.run

Reads coding/ (three independent coder JSONL files) and literature/corpus.jsonl, writes
results/frozen.json (the majority-vote adjudicated dataset) and results/summary.json, and prints the
per-hypothesis verdicts. Standard library only; uses the arm's reusable reliability tool.

Hypotheses:
  H1  outcome mix skews to control + worker_experience; performance is rare.
  H2  evidence is mostly conceptual/qualitative; quantitative (with mixed) is a minority.
  H3  the control stylized-fact subset (claim_type=stylized_fact & outcome=control) is at least as
      conceptual/qualitative as the corpus at large — asserted widely, tested rarely.
"""

import json
import os
from collections import Counter

from org_frontier.reviews.lib import reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["claim_type", "evidence", "outcome"]


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def _pct(a, b):
    return round(100 * a / b, 1) if b else 0.0


def main():
    corpus = _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))
    n_corpus = len(corpus)

    # --- reliability + adjudicated (majority-vote) dataset ---
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))
    n = len(frozen)

    claim = Counter(r["claim_type"] for r in frozen)
    ev = Counter(r["evidence"] for r in frozen)
    out = Counter(r["outcome"] for r in frozen)

    print("\n" + "=" * 72)

    # --- H1: outcome mix ---
    control_exp = out.get("control", 0) + out.get("worker_experience", 0)
    perf = out.get("performance", 0)
    print("H1 (outcomes skew to control + worker experience, performance rare):")
    print(f"   outcome {dict(out)}")
    print(f"   control+worker_experience = {control_exp}/{n} ({_pct(control_exp, n)}%); "
          f"performance = {perf}/{n} ({_pct(perf, n)}%)")

    # --- H2: evidence base ---
    quant = ev.get("quantitative", 0)
    quant_mixed = quant + ev.get("mixed", 0)
    concept_qual = ev.get("conceptual", 0) + ev.get("qualitative", 0)
    print("\nH2 (mostly conceptual/qualitative; quantitative uncommon):")
    print(f"   evidence {dict(ev)}")
    print(f"   conceptual+qualitative = {concept_qual}/{n} ({_pct(concept_qual, n)}%); "
          f"quantitative = {quant}/{n} ({_pct(quant, n)}%); "
          f"quantitative+mixed = {quant_mixed}/{n} ({_pct(quant_mixed, n)}%)")

    # --- H3: the control stylized-fact subset by evidence ---
    sf_control = [r for r in frozen
                  if r["claim_type"] == "stylized_fact" and r["outcome"] == "control"]
    sf_control_ev = Counter(r["evidence"] for r in sf_control)
    m = len(sf_control)
    sf_quant = sf_control_ev.get("quantitative", 0) + sf_control_ev.get("mixed", 0)
    sf_cq = sf_control_ev.get("conceptual", 0) + sf_control_ev.get("qualitative", 0)
    # comparison anchor: also the wider stylized_fact set regardless of outcome
    sf_all = [r for r in frozen if r["claim_type"] == "stylized_fact"]
    print("\nH3 (the 'algorithm controls workers' stylized fact: asserted widely, tested rarely):")
    print(f"   stylized_fact sources total = {len(sf_all)}/{n} ({_pct(len(sf_all), n)}%)")
    print(f"   stylized_fact & outcome=control subset = {m}")
    print(f"   ...its evidence {dict(sf_control_ev)}")
    print(f"   ...conceptual+qualitative = {sf_cq}/{m} ({_pct(sf_cq, m)}%); "
          f"quantitative+mixed = {sf_quant}/{m} ({_pct(sf_quant, m)}%)")
    print(f"   corpus-wide quantitative+mixed share for comparison: {_pct(quant_mixed, n)}%")

    summary = {
        "n_corpus": n_corpus,
        "n_adjudicated": n,
        "claim_type": dict(claim),
        "evidence": dict(ev),
        "outcome": dict(out),
        "H1": {"control_plus_worker_experience": control_exp,
               "control_plus_worker_experience_pct": _pct(control_exp, n),
               "performance": perf, "performance_pct": _pct(perf, n)},
        "H2": {"conceptual_plus_qualitative": concept_qual,
               "conceptual_plus_qualitative_pct": _pct(concept_qual, n),
               "quantitative": quant, "quantitative_pct": _pct(quant, n),
               "quantitative_plus_mixed": quant_mixed,
               "quantitative_plus_mixed_pct": _pct(quant_mixed, n)},
        "H3": {"stylized_fact_total": len(sf_all),
               "stylized_fact_total_pct": _pct(len(sf_all), n),
               "stylized_fact_control_subset": m,
               "stylized_fact_control_evidence": dict(sf_control_ev),
               "stylized_fact_control_conceptual_qualitative_pct": _pct(sf_cq, m),
               "stylized_fact_control_quantitative_mixed_pct": _pct(sf_quant, m),
               "corpus_quantitative_mixed_pct": _pct(quant_mixed, n)},
    }
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print("\nwrote results/frozen.json, results/summary.json")


if __name__ == "__main__":
    main()
