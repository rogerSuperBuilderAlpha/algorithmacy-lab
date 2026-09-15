"""Probe — Heider H5: degree of balance (Cartwright & Harary 1956).

Question.  Cartwright & Harary grade imbalance: b(G) = positive cycles / all cycles. Over the eight
           switching classes of the signed complete graph on four persons, under signed majority with hold,
           is Φ monotone non-decreasing in b(G) with the balanced class at the maximum?
Hypothesis. H5: yes. Lab prior: against — the balanced class is expected at Φ = 0.
Method.    One representative per switching class (fewest negatives); Φ_MIP, core, attractors, rest states.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_degree
"""

from org_frontier.thinkers.heider import forms as F


def main():
    print("Heider H5 — degree of balance on four persons: eight switching classes")
    control = F.run_control()
    classes = F.switching_classes_k4()
    rows = []
    for rep, members in sorted(classes.items(), key=lambda kv: -F.degree_of_balance(kv[0])[0]):
        b, pos, tot = F.degree_of_balance(rep)
        name = "k4_" + F.sign_str(rep).replace("−", "m").replace("+", "p")
        rec = F.evaluate(name, F.k4(rep), F.K4_LABELS, F.K4_EDGES, rep)
        rec["degree_of_balance"] = round(b, 4)
        rec["positive_cycles"] = pos
        rec["class_size"] = len(members)
        rows.append(rec)
        print("  %-12s b=%d/%d=%.3f  size=%2d  Φ_MIP=%.6f  core=%-18s attractors: %d fixed, %d cycles  rest=%d"
              % (F.sign_str(rep), pos, tot, b, len(members), rec["phi_mip"], tuple(rec["core"]),
                 rec["n_fixed"], rec["n_cycles"], len(rec["rest_states"])))
    # monotone non-decreasing in b, pairwise over classes with strictly different b (ties in b impose nothing)
    pairs = [(x, y) for x in rows for y in rows if x["degree_of_balance"] < y["degree_of_balance"]]
    monotone = all(x["phi_mip"] <= y["phi_mip"] + 1e-9 for x, y in pairs)
    inverse = all(x["phi_mip"] >= y["phi_mip"] - 1e-9 for x, y in pairs)
    max_phi = max(r["phi_mip"] for r in rows)
    balanced_max = abs(next(r for r in rows if r["degree_of_balance"] == 1.0)["phi_mip"] - max_phi) < 1e-9
    levels = sorted({r["degree_of_balance"] for r in rows})
    print("  distinct b levels: %s" % ", ".join("%.3f (n=%d)" % (b, sum(1 for r in rows if r["degree_of_balance"] == b)) for b in levels))
    flat = max_phi - min(r["phi_mip"] for r in rows) < 1e-9
    print("  Φ monotone non-decreasing in b=%s  balanced class at max Φ=%s  Φ monotone non-increasing in b=%s  Φ constant across classes=%s"
          % (monotone, balanced_max, inverse, flat))
    if monotone and balanced_max and flat:
        status = "CONFIRMED (vacuously: Φ is constant across all eight classes)"
    elif monotone and balanced_max:
        status = "CONFIRMED"
    elif monotone or balanced_max:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H5 (Φ rises with the degree of balance, balanced class at the maximum): %s" % status)
    F.save("probe_heider_degree", {"control": control, "classes": rows, "monotone": monotone,
                                    "balanced_max": balanced_max, "inverse": inverse, "flat": flat,
                                    "H5": status})


if __name__ == "__main__":
    main()
