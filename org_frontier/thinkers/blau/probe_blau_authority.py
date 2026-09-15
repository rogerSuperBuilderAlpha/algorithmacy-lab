"""Probe — Blau H4: legitimate authority is carried by the subordinates.

Question.  Blau (1964: 23): subordinates' consensus "finds expression in group pressures that promote
           compliance with the ruler's directives." If the superior stops serving, do legitimated
           subordinates keep complying, and are they one complex?
Hypothesis. H4: next(authority, S=0 B=11) keeps B = 11; next(power, 011) does not; {B1, B2} ⊆ core(authority).
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.blau.probe_blau_authority
"""

from org_frontier.thinkers.blau import forms as F


def main():
    print("Blau H4 — power and legitimate authority")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("power", "authority")}
    start = (0, 1, 1)   # S, B1, B2
    nxt = {name: F.next_state(name, start) for name in ("power", "authority")}
    for name in nxt:
        print("    %-10s S off, both complying -> %s" % (name, "".join(map(str, nxt[name]))))
    holds = nxt["authority"][1:] == (1, 1)
    lapses = nxt["power"][1:] != (1, 1)
    together = {"B1", "B2"} <= set(recs["authority"]["core"])
    print("  authority holds without service=%s   power lapses=%s   subordinates one complex under authority=%s" % (
        holds, lapses, together))
    n = sum([holds, lapses, together])
    status = "CONFIRMED" if n == 3 else ("PARTIAL" if n == 2 else "REFUTED")
    print("H4 (legitimate authority is carried by the subordinates): %s" % status)
    F.save("probe_blau_authority", {"control": control, "forms": recs,
                                    "next_from_011": {k: "".join(map(str, v)) for k, v in nxt.items()}, "H4": status})


if __name__ == "__main__":
    main()
