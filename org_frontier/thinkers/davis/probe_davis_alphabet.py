"""Probe — Davis H3: the all-negative verdict depends on the alphabet.

Question.  The Heider paper found −−− and ++− identical (Φ 6, all three in the core) with one bit per person.
           One bit is two camps. Does the verdict on −−− change when a third camp exists, and does ++−'s?
Hypothesis. H3: mmm has all three in its core at k = 2 and fewer at k = 3, 4; ppm has all three at every k.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.davis.probe_davis_alphabet   (~40 min)
"""

from org_frontier.thinkers.davis import forms as F


def main():
    print("Davis H3 — −−− and ++− across k = 2, 3, 4")
    control = F.run_control()
    recs = {}
    for name in ("mmm", "ppm"):
        for k in (2, 3, 4):
            recs["%s_k%d" % (name, k)] = F.evaluate_phi(name, 3, F.TRIAD_EDGES, F.NAMED[name], k)
    m = [len(recs["mmm_k%d" % k]["core_persons"]) for k in (2, 3, 4)]
    p = [len(recs["ppm_k%d" % k]["core_persons"]) for k in (2, 3, 4)]
    a = m[0] == 3 and m[1] < 3 and m[2] < 3
    b = all(x == 3 for x in p)
    print("  mmm core persons over k=2,3,4: %s → %s   ppm: %s → %s" % (m, a, p, b))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H3 (the all-negative verdict is the two-camp verdict): %s" % status)
    F.save("probe_davis_alphabet", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
