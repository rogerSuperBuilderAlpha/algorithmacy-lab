"""Probe — Ostrom H2: self-governance against Leviathan and privatization.

Question.  Ostrom (1990: 8–21): the "only way" arguments are a central enforcer or private division; the
           cases are a third way. A star with the enforcer at the center, severed ties, and a clique of
           contingent commitments.
Hypothesis. H2: core(self) all three at Φ > coreΦ(leviathan); L has positive advantage; private binds nothing.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_solutions
"""

from org_frontier.thinkers.ostrom import forms as F


def main():
    print("Ostrom H2 — Leviathan, privatization, self-governance")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("leviathan", "private", "self")}
    c_self = set(recs["self"]["core"]) == {"c1", "c2", "c3"}
    c_phi = recs["self"]["core_phi"] > recs["leviathan"]["core_phi"] + 1e-6
    adv_L = F.advantage(recs["leviathan"], "L") if recs["leviathan"]["core"] else 0.0
    c_adv = adv_L > 1e-6
    c_priv = not recs["private"]["core"]
    print("  self core all three=%s   Φ self>leviathan=%s (%.3f vs %.3f)   L advantage=%.3f (>0: %s)   private binds nothing=%s" % (
        c_self, c_phi, recs["self"]["core_phi"], recs["leviathan"]["core_phi"], adv_L, c_adv, c_priv))
    n = sum([c_self, c_phi, c_adv, c_priv])
    status = "CONFIRMED" if n == 4 else ("PARTIAL" if n >= 2 else "REFUTED")
    print("H2 (self-governance is the tighter whole; the enforcer holds the edge; division binds nothing): %s" % status)
    F.save("probe_ostrom_solutions", {"control": control, "forms": recs, "advantage_L": adv_L, "H2": status})


if __name__ == "__main__":
    main()
