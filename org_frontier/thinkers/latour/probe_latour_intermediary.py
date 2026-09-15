"""Probe — Latour H1: the intermediary counts for one.

Question.  Latour (2005: 39): an intermediary "transports meaning or force without transformation" and can
           be taken as "a black box counting for one, even if it is internally made of many parts." Insert
           k copy-relays into the tie of a mutual dyad: does Φ stay put and do the relays stay out of the
           core?
Hypothesis. H1 (Latour): Φ(chain k) = Φ(chain 0) for k = 1..3 and no relay is in any core.
Method.    chain(k) for k = 0..3 (n = 2..5); Φ_MIP and major complex.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_intermediary
"""

from org_frontier.thinkers.latour import forms as F


def main():
    print("Latour H1 — a chain of intermediaries in a dyad loop, k = 0..3")
    control = F.run_control()
    recs = {}
    for k in range(4):
        labels, rules = F.chain(k)
        recs["chain%d" % k] = F.evaluate("chain%d" % k, rules, labels)
    phi0 = recs["chain0"]["phi_mip"]
    phi_same = all(abs(recs["chain%d" % k]["phi_mip"] - phi0) < 1e-9 for k in range(1, 4))
    relays_in = sorted({c for k in range(1, 4) for c in recs["chain%d" % k]["core"] if c.startswith("I")})
    print("  Φ unchanged across k=%s  relays in some core: %s" % (phi_same, ",".join(relays_in) or "none"))
    if phi_same and not relays_in:
        status = "CONFIRMED"
    elif not relays_in:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H1 (intermediaries leave Φ unchanged and stay out of the core): %s" % status)
    F.save("probe_latour_intermediary", {"control": control, "forms": recs, "phi_same": phi_same,
                                          "relays_in_core": relays_in, "H1": status})


if __name__ == "__main__":
    main()
