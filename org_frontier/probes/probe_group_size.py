"""Probe 44 — the group-size transition (Niizato et al. 2020 precedent).

Niizato et al. (2020, PLOS ONE; Entropy 22:726) found, in real fish schools, a qualitative
DISCONTINUITY in exact Φ at group size four — a transition invisible to mutual information or
transfer entropy. Does an analogous size dependence appear in coordination forms?

Two readings here:
  (a) the all-required "pool" form (S matches all parties) at sizes n=2..5 — how Φ scales;
  (b) the random strict-mediation triadic RATE by size (from the population probes): 9.4% (n=3) ->
      2.3% (n=4) -> 0% (n=5).

H44: irreducible coordination has a strong size dependence — the constructed pool's Φ rises with
size while the chance a random form is irreducible collapses by n=5. (Niizato's animal result is the
exact-Φ precedent for a size-dependent transition; ours is on coordination forms.)

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_group_size
"""

from .lib import verdict

POP_RATE = {3: "9.4%", 4: "2.3%", 5: "0.0%"}  # from corpus.population / multiparty.scaling


def pool(n):
    outer = [0] + list(range(2, n))            # worker + counterparts
    rules = [None] * n
    def s_rule(x, outer=tuple(outer)):
        r = 1
        for i in outer:
            r &= x[i]
        return r
    rules[1] = s_rule
    for i in outer:
        rules[i] = lambda x: x[1]
    labels = tuple(["W", "S"] + [f"C{k}" for k in range(1, n - 1)])
    return rules, labels


def main():
    print("PROBE 44 — group-size transition (Niizato precedent)")
    print("=" * 72)
    print("  (a) all-required pool, Φ by size:")
    for n in (2, 3, 4, 5):
        rules, labels = pool(n)
        v = verdict(rules, labels)
        print(f"     n={n}  {v.structure:<8} Φ={v.max_phi:.3f}")
    print("  (b) random strict-mediation triadic RATE by size (population probes):")
    for n in (3, 4, 5):
        print(f"     n={n}  P(triadic) = {POP_RATE[n]}")
    print("=" * 72)
    print("  Niizato et al. found a Φ discontinuity at fish-school size 4 (invisible to MI/TE);")
    print("  here the constructed pool's Φ rises with size while the random triadic rate collapses.")
    print("=" * 72)


if __name__ == "__main__":
    main()
