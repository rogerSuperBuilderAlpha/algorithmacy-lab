"""Probe Q80 (H1-H4) — does the outreach verdict survive asynchronous update?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q80_async_update.probe_async_update
"""
import csv, os
from org_frontier.probes.lib import verdict, max_phi_float
from org_frontier.questions.q80_async_update import forms as F

CASES = [("read_recipient", F.READ_RECIPIENT, "triadic"),
         ("broadcast", F.BROADCAST, "dyadic"),
         ("all_required", F.ALL_REQUIRED, "triadic")]


def main():
    print("PROBE Q80 (H1-H4) — asynchronous update")
    print("=" * 64)
    rows, res = [], {}
    for name, (rules, labels), sync_expect in CASES:
        sv = verdict(rules, labels)
        aphi, _ = max_phi_float(F.async_tpm(rules))
        averdict = "triadic" if aphi > 1e-6 else "dyadic"
        res[name] = (sv.structure, sv.max_phi, averdict, aphi)
        print(f"  {name:<15} sync={sv.structure:<8}Φ={sv.max_phi:.3f} | async={averdict:<8}Φ={aphi:.4f}  "
              f"(verdict preserved: {sv.structure == averdict})")
        rows.append((name, sv.structure, f"{sv.max_phi:.4f}", averdict, f"{aphi:.4f}"))
    h1 = res["read_recipient"][2] == "triadic"
    h2 = res["broadcast"][2] == "dyadic"
    h3 = res["all_required"][2] == "triadic"
    h4 = all(res[n][0] == res[n][2] for n, _, _ in CASES)
    print("=" * 64)
    print(f"  read_recipient stays triadic async: {h1}")
    print(f"  broadcast stays dyadic async: {h2}")
    print(f"  all_required stays triadic async: {h3}")
    print(f"  verdict preserved under async for all keystones: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "async_update.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "sync", "sync_phi", "async", "async_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()
