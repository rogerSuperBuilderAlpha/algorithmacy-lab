"""Probe 36 — cause-effect-structure richness: triadic vs dyadic.

Beyond the scalar Φ, IIT-4.0 unfolds a full cause-effect structure (distinctions + relations). Do
triadic coordination forms have richer structure than dyadic ones? Reuse the repo's
structure_suite.suite.extract_suite (one pyphi.new_big_phi.phi_structure call).

H36: triadic forms carry more distinctions and (especially) more relations than dyadic forms — the
irreducible coordination is structurally richer, not just higher-Φ.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ces_richness
"""

from org_frontier.classifier.classifier import classify_rules, tpm_from_rules, cm_from_rules
from org_frontier.corpus import forms_library as lib
from foundations.proxy_audit.exact_phi import reachable_states
from foundations.structure_suite.suite import extract_suite

LABELS = ("W", "S", "C")


def main():
    print("PROBE 36 — cause-effect-structure richness (triadic vs dyadic)")
    print("=" * 78)
    print(f"  {'form':<24}{'verdict':<9}{'#distinct':<11}{'#relations'}")
    by_verdict = {"triadic": [], "dyadic": []}
    for f in lib.FORMS:
        if len(f.rules) != 3:
            continue
        v = classify_rules(f.rules, labels=LABELS)
        tpm, cm = tpm_from_rules(f.rules), cm_from_rules(f.rules)
        best = {"n_distinctions": 0, "n_relations": 0}
        for s in reachable_states(tpm, 3):
            state = tuple((s >> i) & 1 for i in range(3))
            try:
                su = extract_suite(tpm, cm, 3, state)
            except Exception:
                continue
            if su["n_distinctions"] > best["n_distinctions"] or su["n_relations"] > best["n_relations"]:
                best = su
        by_verdict[v.structure].append((best["n_distinctions"], best["n_relations"]))
        print(f"  {f.key:<24}{v.structure:<9}{best['n_distinctions']:<11}{best['n_relations']}")
    print("=" * 78)
    for verdict, rows in by_verdict.items():
        if rows:
            md = sum(r[0] for r in rows) / len(rows)
            mr = sum(r[1] for r in rows) / len(rows)
            print(f"  {verdict:<8} mean #distinctions {md:.1f}, mean #relations {mr:.1f}  (n={len(rows)})")
    print("=" * 78)


if __name__ == "__main__":
    main()
